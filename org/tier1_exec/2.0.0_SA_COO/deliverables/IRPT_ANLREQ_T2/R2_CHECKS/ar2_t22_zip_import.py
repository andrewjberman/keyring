"""W41-S1 precondition: the BUILT transcripts-pull zip admits a valid analysis_ready message (keys.py + firm registry load from the zip),
and a negative control (keys.py removed from the extract) refuses with KEYS_MODULE_UNAVAILABLE. Counts and verdicts only."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

REPO = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or os.getcwd()
BASH = os.environ.get("BASH_EXE") or shutil.which("bash")
out = {}
r = subprocess.run([BASH, "infra/aws/lambda/transcripts-pull/build.sh"], cwd=REPO, capture_output=True, text=True)
out["build_rc"] = r.returncode
out["build_tail"] = (r.stdout.strip().splitlines() or [""])[-1]
zpath = os.path.join(REPO, "infra", "aws", "lambda", "transcripts-pull", "dist", "transcripts-pull.zip")
with zipfile.ZipFile(zpath) as z:
    names = z.namelist()
out["zip_files"] = len(names)
out["zip_has_keys"] = any(n.endswith("investor-reporting/_keys/keys.py") for n in names)
out["zip_has_registry"] = "data/firm_registry.json" in names
reg = json.load(open(os.path.join(REPO, "data", "firm_registry.json"), encoding="utf-8"))
firms = reg.get("firms", reg) if isinstance(reg, dict) else reg
tenant = next(iter(firms)) if isinstance(firms, dict) else (firms[0].get("firm_id") if isinstance(firms[0], dict) else firms[0])

PROBE = r'''
import json, sys
sys.path.insert(0, ".")
from data.transcripts.scripts.commentary import lambda_handler as h
body = json.dumps({"kind": "analysis_ready", "request_id": "REQ-%s", "tenant": "%s"}, sort_keys=True, separators=(",", ":"))
res = h.admit_ready_message(body)
print(json.dumps(res if isinstance(res, dict) else {"result": repr(res)[:200]}, default=str)[:400])
'''


def probe(extract):
    code = PROBE % ("0" * 24, tenant)
    p = subprocess.run([sys.executable, "-I", "-c", code], cwd=extract, capture_output=True, text=True)
    return {"rc": p.returncode, "out": (p.stdout.strip() or p.stderr.strip().splitlines()[-1] if (p.stdout or p.stderr) else "")[:400]}


d = tempfile.mkdtemp(prefix="w41s1_")
try:
    with zipfile.ZipFile(zpath) as z:
        z.extractall(d)
    out["positive"] = probe(d)
    for root, _, files in os.walk(d):
        for f in files:
            if f == "keys.py" and "_keys" in root:
                os.remove(os.path.join(root, f))
    out["negative_control_keys_removed"] = probe(d)
finally:
    shutil.rmtree(d, ignore_errors=True)
ok = (out["build_rc"] == 0 and out["zip_has_keys"] and out["zip_has_registry"] and out["positive"]["rc"] == 0
      and out["negative_control_keys_removed"]["rc"] != 0 and "KEYS_MODULE_UNAVAILABLE" in out["negative_control_keys_removed"]["out"])
print("AR2-T22-%s files=%d positive_rc=%d negative_rc=%d" % ("OK" if ok else "FAIL", out["zip_files"], out["positive"]["rc"],
      out["negative_control_keys_removed"]["rc"]))
sys.exit(0 if ok else 1)
