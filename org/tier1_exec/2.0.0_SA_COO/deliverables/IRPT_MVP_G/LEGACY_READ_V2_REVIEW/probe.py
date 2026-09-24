"""Independent probes of the ad628ba502 LEGACY-READ recognizer (2.0.0_SA_COO~G). Calls the candidate's
own functions on in-memory mutations of the real post-image; executes no source under test."""
import ast
import hashlib
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ng", os.path.join(HERE, "naming_gate_v2.py"))
ng = importlib.util.module_from_spec(spec)
sys.argv = ["ng"]
spec.loader.exec_module(ng)
ng.REPO = os.environ["WS_REPO"]

src = open(os.path.join(HERE, "holdings_v2.py"), encoding="utf-8").read()
entry = json.load(open(os.path.join(HERE, "carrier.json"), encoding="utf-8"))["entries"][0]
want = entry["read_context"]["helper_body_sha256"]


def helper_sha(text, name="_latest_date_partition"):
    tree = ast.parse(text)
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return hashlib.sha256(ng._norm_body(ast.get_source_segment(text, n)).encode()).hexdigest()


print("carrier helper sha      :", want[:16])
print("helper sha @ad628 source:", helper_sha(src)[:16], "MATCH" if helper_sha(src) == want else "DIFF")

# M's cutoff-patched helper, reconstructed from the CTO-captured candidate.diff post-image
diff = open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "candidate.diff"), encoding="utf-8").read() \
    if os.path.exists(os.path.join(HERE, "candidate.diff")) else ""
m = re.search(r"\n\+def _latest_date_partition.*?\n     return sorted\(dates\)\[-1\] if dates else None\n", diff, re.S)
if m:
    post = "\n".join(ln[1:] for ln in m.group(0).strip("\n").split("\n") if not ln.startswith("-"))
    print("helper sha M-patched    :", helper_sha(post)[:16], "MATCH" if helper_sha(post) == want else "DIFF")

    # THE APPROVED POST-IMAGE: M's cutoff-patched helper + the as_of call, spliced into the ad628 source
    tree = ast.parse(src)
    old = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "_latest_date_partition"][0]
    src = src.replace(ast.get_source_segment(src, old), post.rstrip("\n"), 1)
    src = src.replace('"silver/api_dims/accounts_v2/", date_prefix="snapshot_date=")',
                      '"silver/api_dims/accounts_v2/", date_prefix="snapshot_date=", as_of=as_of)', 1)
    print("helper sha spliced      :", helper_sha(src)[:16], "MATCH" if helper_sha(src) == want else "DIFF")

rows = []


def arm(name, text, expect):
    ok, note = ng.legacy_read_ok(entry, text)
    got = "PASS" if ok else "REFUSE"
    rows.append((name, expect, got, note))
    flag = "ok " if got == expect else "XX "
    print("%s%-44s expect %-6s got %-6s %s" % (flag, name, expect, got, note[:110]))


CALL = '_latest_date_partition(s3, bucket, "silver/api_dims/accounts_v2/", date_prefix="snapshot_date=", as_of=as_of)'
assert CALL in src

arm("P0 baseline (unmutated ad628 post-image)", src, "PASS")

# D1: a decorator on the helper -- outside get_source_segment(FunctionDef)?
d1 = src.replace("def _latest_date_partition(", "@_writes_too\ndef _latest_date_partition(", 1)
d1 = d1.replace("def build_inf(", "def _writes_too(f):\n    return f\n\n\ndef build_inf(", 1)
arm("D1 decorator added to the helper", d1, "REFUSE")

# D2: nested def inside build_inf whose PARAMETER rebinds bucket
d2 = src.replace("    acc_date = " + CALL,
                 "    def _probe(bucket):\n        return " + CALL + "\n    acc_date = _probe(\"any-other-bucket\")", 1)
arm("D2 nested def param rebinds bucket", d2, "REFUSE")

# D3: nested def inside build_inf whose PARAMETER rebinds the helper name
d3 = src.replace("    acc_date = " + CALL,
                 "    def _probe(_latest_date_partition):\n        return " + CALL
                 + "\n    acc_date = _probe(lambda *a, **k: None)", 1)
arm("D3 nested def param rebinds helper", d3, "REFUSE")

# D4: class-body / nonlocal style indirection: module-level globals() rebind of helper
d4 = src + "\nglobals()['_latest_date_partition'] = lambda *a, **k: None\n"
arm("D4 globals() rebind of helper (dataflow)", d4, "REFUSE")

# D5: decorator on build_inf itself
d5 = src.replace("def build_inf(", "@_wrap\ndef build_inf(", 1).replace(
    "def _latest_date_partition(", "def _wrap(f):\n    return f\n\n\ndef _latest_date_partition(", 1)
arm("D5 decorator on enclosing build_inf", d5, "REFUSE")

# D6: default argument of a nested lambda capturing a different bucket
d6 = src.replace("    acc_date = " + CALL,
                 "    acc_date = (lambda bucket=\"x\": " + CALL + ")()", 1)
arm("D6 lambda default param rebinds bucket", d6, "REFUSE")

# D7: class body inside build_inf binding bucket
d7 = src.replace("    acc_date = " + CALL,
                 "    class _K:\n        bucket = \"other\"\n        v = " + CALL + "\n    acc_date = _K.v", 1)
arm("D7 class body rebinds bucket", d7, "REFUSE")

# authority: substring id and unreachable pin
print("\nauthority_ok substring probe:")
print("  id 'LEGACY' ->", ng.authority_ok(entry["authority"], "LEGACY"))
print("  id 'IRPT-M-LEGACY-READ-0' ->", ng.authority_ok(entry["authority"], "IRPT-M-LEGACY-READ-0"))

bad = [r for r in rows if r[1] != r[2]]
print("\nARMS %d, AS-EXPECTED %d, UNEXPECTED %d" % (len(rows), len(rows) - len(bad), len(bad)))
json.dump(rows, open(os.path.join(HERE, "probe_results.json"), "w"), indent=1)
