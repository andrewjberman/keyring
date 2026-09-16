"""Semantic re-derivation lens (3.0.0_SA_CVO): compare a rectangle's cell values to facts re-derived
independently from pinned sources and artifacts. Usage: python check_c.py <rectangle.json>
Exit 0 = every check agrees; 1 = at least one MISMATCH. Read-only against the repository."""
import ast
import json
import os
import re
import subprocess
import sys

rect_path = os.path.abspath(sys.argv[1])
ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
os.chdir(ROOT)
APP = "infra/aws/ec2/opal-gateway/app"
PKG = "org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MENACHEM_SCHWAB_CLAUDE_ACCESS_20260914"
SRC1, SRC2, ART = "5dd24300f7", "c9a44aa896", "39a8c5eeca"
rect = json.load(open(rect_path, encoding="utf-8"))
cells = {(e["entity_id"], f): c for e in rect["entities"] for f, c in e["cells"].items()}
results = []


def txt(commit, path):
    r = subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True)
    return r.stdout.decode("utf-8", "replace").replace("\r\n", "\n") if r.returncode == 0 else None


def chk(cell, name, derived, claimed):
    results.append((cell, name, derived, claimed, "OK" if derived == claimed else "MISMATCH"))


# 1. S3 footers vs observed-metadata.json
om = json.loads(txt(ART, f"{PKG}/observed-metadata.json"))
art = {}
for o in om["parquet_footers"]["objects"]:
    parts = o["key"].split("/")
    cols = o["columns"] if isinstance(o["columns"], int) else len(o["columns"])
    art[(parts[1], parts[3])] = (o["rows"], o["object_bytes"], cols, o["version_id"])
fos = cells[("S3-data", "recorded_observation")]["value"]["footer_objects"]
chk("S3-data.recorded_observation", "footer record count", len(art), len(fos))
for fo in fos:
    k = (fo["master"], fo["dataset"])
    chk("S3-data.recorded_observation", f"footer {k[0]}/{k[1]} (rows,bytes,cols,version)", art.get(k),
        (fo["rows"], fo["object_bytes"], fo["columns"], fo["version_id"]))

# 2. necessary-inequality over every contained_in pair
for (eid, f), c in cells.items():
    ds = c["evidence"].get("denominator", [])
    by = {d["of_what"]: d["n"] for d in ds}
    for d in ds:
        if "contained_in" in d:
            chk(f"{eid}.{f}", f"contained_in {d['n']} <= {by.get(d['contained_in'])}", True,
                by.get(d["contained_in"]) is not None and d["n"] <= by[d["contained_in"]])

# 3. S4 proposed limits vs entitlement JSON
lim = json.loads(txt(ART, f"{PKG}/menachem-entitlement.proposed.json"))
m = {"query_timeout_seconds": "query_timeout_seconds", "source_objects": "max_source_objects",
     "source_bytes": "max_source_bytes", "chat_rows": "chat_max_rows", "chat_characters": "chat_max_characters",
     "chat_bytes": "chat_max_bytes", "export_rows": "export_max_rows", "export_bytes": "export_max_bytes"}
pl = cells[("S4-query", "recorded_observation")]["value"]["proposed_limits"]
chk("S4-query.recorded_observation", "limit key set", sorted(m), sorted(pl))
for k, v in m.items():
    chk("S4-query.recorded_observation", f"limit {k}", lim["limits"][v], pl.get(k))

# 4. S2 profile vs entitlement JSON
pp = cells[("S2-authorization", "recorded_observation")]["value"]["proposed_profile"]
chk("S2-authorization.recorded_observation", "status", lim["status"], pp["status"])
chk("S2-authorization.recorded_observation", "policy_revision", lim["policy_revision"], pp["policy_revision"])
chk("S2-authorization.recorded_observation", "tenant/object ids", (lim["identity"]["entra_tenant_id"], lim["identity"]["entra_object_id"]),
    (pp["entra_tenant_id"], pp["entra_object_id"]))
chk("S2-authorization.recorded_observation", "allowed_tools", lim["allowed_tools"], pp["allowed_tools"])
chk("S2-authorization.recorded_observation", "masters", sorted(lim["masters"]), sorted(pp["masters"]))
chk("S2-authorization.recorded_observation", "datasets", sorted(lim["datasets"]), sorted(pp["datasets"]))

# 5. simulation counts (S2 and S6) vs iam-simulation-results.json
sim = json.loads(txt(ART, f"{PKG}/iam-simulation-results.json"))
cases = sim["cases"]
npass = sum(1 for c in cases if c.get("passed") is True)
rs = cells[("S2-authorization", "recorded_observation")]["value"]["recorded_iam"]["custom_policy_simulation"]
chk("S2-authorization.recorded_observation", "sim cases/passed", (len(cases), npass), (rs["cases"], rs["passed"]))
pos = {}
for c in cases:
    if str(c.get("expected")).lower() == "allowed":
        pos[c["action"]] = pos.get(c["action"], 0) + 1
s6 = cells[("S6-operations", "recorded_observation")]["value"]["simulation"]
mm = re.search(r"(\d+) cases and (\d+) passes", s6)
chk("S6-operations.recorded_observation", "sim cases/passes in prose", (len(cases), npass), (int(mm.group(1)), int(mm.group(2))) if mm else None)
chk("S6-operations.recorded_observation", "positive GetObjectVersion count", pos.get("s3:GetObjectVersion"),
    1 if "ONE GetObjectVersion" in s6 else None)
chk("S6-operations.recorded_observation", "positive total", sum(pos.values()), 13 if s6.startswith("2026") and "Thirteen positives" in s6 else None)

# 6. S5 route declarations via AST vs value + denominator
tree = ast.parse(txt(SRC1, f"{APP}/server.py"))
calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and getattr(n.func, "id", "") in ("Route", "Mount")]
paths = [c.args[0].value for c in calls if c.args and isinstance(c.args[0], ast.Constant)]
sc = cells[("S5-download", "source_contract")]
den = [d["n"] for d in sc["evidence"]["denominator"] if d["unit"] == "route_declarations" and "contained_in" not in d]
chk("S5-download.source_contract", "Route/Mount declarations (denominator)", len(calls), den[0] if den else None)
mv = re.search(r"declares (\d+) Route/Mount", sc["value"]["existing"][0])
chk("S5-download.source_contract", "Route/Mount declarations (value prose)", len(calls), int(mv.group(1)) if mv else None)
den0 = [d["n"] for d in sc["evidence"]["denominator"] if "contained_in" in d]
chk("S5-download.source_contract", "schwab/export/ticket/download routes", len([p for p in paths if re.search(r"schwab|export|ticket|download", p, re.I)]), den0[0] if den0 else None)

# 7. S2 native tool counts via AST
tree = ast.parse(txt(SRC1, f"{APP}/tools.py"))
tools = callers = 0
for node in ast.walk(tree):
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        if any(isinstance(d.func if isinstance(d, ast.Call) else d, ast.Attribute) and (d.func if isinstance(d, ast.Call) else d).attr == "tool" for d in node.decorator_list):
            tools += 1
            if any(isinstance(n, ast.Call) and getattr(n.func, "id", "") == "_run" for n in ast.walk(node)):
                callers += 1
d2 = cells[("S2-authorization", "source_contract")]["evidence"]["denominator"]
chk("S2-authorization.source_contract", "native tools / calling _run", (tools, callers), (d2[0]["n"], d2[1]["n"]))

# 8. S1 recorded HTTP vs requirements-review-evidence.json
ev = json.loads(txt(ART, f"{PKG}/requirements-review-evidence.json"))
arts = {h["path"]: h for h in ev["http"]}
rh = cells[("S1-auth", "recorded_observation")]["value"]["recorded_http"]
chk("S1-auth.recorded_observation", "record count", len(arts), len(rh))
for h in rh:
    a = arts.get(h["path"], {})
    chk("S1-auth.recorded_observation", f"{h['path']} (status,elapsed_ms)", (a.get("status"), a.get("elapsed_ms")), (h["status"], h["elapsed_ms"]))
chk("S1-auth.recorded_observation", "record_time", ev["measured_at"], cells[("S1-auth", "recorded_observation")]["value"]["record_time"])

# 9. S6 recorded EC2 manifest claim: every factual token in the claim must appear in the named artifact entry
emj = json.loads(txt(SRC2, "infra/aws/ec2/EC2_MANIFEST.json"))


def find(o, key):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key and isinstance(v, dict) and "instance_id" in v:
                return v
            r = find(v, key)
            if r is not None:
                return r
    return None


g = find(emj, "opal-gateway") or {}
claim = cells[("S6-operations", "recorded_observation")]["value"]["ec2_manifest"]
blob = json.dumps(g)
for tok in re.findall(r"i-[0-9a-f]{17}|t[0-9][a-z]?\.[a-z0-9]+|[0-9a-f]{40}|20\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ", claim):
    chk("S6-operations.recorded_observation", f"claim token {tok!r} recorded in EC2_MANIFEST opal-gateway entry", True, tok in blob)

# 10. S3 footer column counts = projection vendor columns + provenance (necessary equality)
proj = txt(SRC2, "data/assets/scripts/silver/schwab_projections.py")
ptree = ast.parse(proj)
pcounts = {}
for node in ast.walk(ptree):
    if isinstance(node, ast.AnnAssign) and getattr(node.target, "id", "") == "PROJECTIONS":
        for k, v in zip(node.value.keys, node.value.values):
            cols = v.elts[2]
            pcounts[k.value] = len(cols.elts) if isinstance(cols, ast.Tuple) else None
stree = ast.parse(txt(SRC2, "data/assets/scripts/silver/schwab_schemas.py"))
specs, prov = None, None
for node in ast.walk(stree):
    if isinstance(node, (ast.Assign, ast.AnnAssign)):
        tgt = node.targets[0] if isinstance(node, ast.Assign) else node.target
        if getattr(tgt, "id", "") == "SPECS":
            try:
                specs = ast.literal_eval(node.value)
            except Exception:  # noqa: BLE001
                specs = None
        if getattr(tgt, "id", "") == "PROVENANCE_COLS":
            prov = ast.literal_eval(node.value)
if pcounts.get("dim_balance") is None and isinstance(specs, dict):
    pcounts["dim_balance"] = len(specs[("RPS", 2)])
for fo in fos:
    if prov is not None and pcounts.get(fo["dataset"]) is not None:
        chk("S3-data.recorded_observation", f"columns {fo['master']}/{fo['dataset']} = vendor+provenance",
            pcounts[fo["dataset"]] + len(prov), fo["columns"])

bad = [r for r in results if r[4] != "OK"]
for r in results:
    if r[4] != "OK":
        print(f"MISMATCH {r[0]} :: {r[1]} :: derived={r[2]!r} claimed={r[3]!r}")
print(f"check_c: {len(results)} checks, {len(results) - len(bad)} OK, {len(bad)} MISMATCH  [{os.path.basename(rect_path)}]")
sys.exit(1 if bad else 0)
