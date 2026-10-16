"""SOC2_MSLOGS round 1, cell SM-g-1 checks (the registry rows and the R20 ledger). Run from the repo (worktree) root.

  python s1_check_g1.py rows   -> G1-ROWS-OK   (validate; owner_directive D12; the audit_records address; targets in sync)
  python s1_check_g1.py ledger -> G1-LEDGER-OK (X18 departure (1) retired, departure (2) kept)
"""
import filecmp
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "lib"))
WANT = "s3://opal-data-trino/m365-metadata/trino/bronze/audit_records/date=20261015/20261015120000000001$20261015120000000001$audit_exchange$Audit_Exchange$na0001.json.gz"
OBJ = "20261015120000000001$20261015120000000001$audit_exchange$Audit_Exchange$na0001.json.gz"


def rows():
    import opal_naming as n

    bad = []
    try:
        n.validate()
    except Exception as e:  # noqa: BLE001
        print("G1-ROWS-REFUSED validate: %s" % str(e)[:160])
        return 1
    reg = json.load(open(os.path.join(ROOT, "infra", "logic", "registry", "systems.json"), encoding="utf-8"))
    row = [r for r in reg["systems"] if r.get("key") == "m365-metadata"]
    if len(row) != 1:
        bad.append("no single m365-metadata system row")
    else:
        if row[0].get("owner_directive") != "D12":
            bad.append("owner_directive is %r, not D12" % row[0].get("owner_directive"))
        if "SOC2_MSLOGS" not in json.dumps(row[0]):
            bad.append("owner_basis does not cite SOC2_MSLOGS")
    try:
        got = n.address("m365-metadata", "trino", "bronze", "audit_records", "date=20261015", object=OBJ)
    except Exception as e:  # noqa: BLE001
        got = "REFUSED %s" % str(e)[:100]
    if got != WANT:
        bad.append("audit_records address %r" % got)
    out = tempfile.mkdtemp()
    p = subprocess.run([sys.executable, "lib/opal_naming.py", "generate", "--out", out], capture_output=True, text=True)
    if p.returncode != 0:
        bad.append("generate rc=%d" % p.returncode)
    moved = []
    for d, _, fs in os.walk(out):
        for f in fs:
            fresh = os.path.join(d, f)
            rel = os.path.relpath(fresh, out).replace(os.sep, "/")
            if rel.startswith("portal/"):
                continue  # the portal targets are carried separately, never committed by a worker
            cur = os.path.join(ROOT, rel)
            if not os.path.exists(cur) or not filecmp.cmp(fresh, cur, shallow=False):
                moved.append(rel)
    if moved:
        bad.append("targets stale n=%d first=%s" % (len(moved), moved[:3]))
    if bad:
        print("G1-ROWS-REFUSED " + "; ".join(bad))
        return 1
    print("G1-ROWS-OK")
    return 0


def ledger():
    p = os.path.join(ROOT, "infra", "logic", "06_CONFORMANCE_LEDGER.md")
    lines = [ln for ln in open(p, encoding="utf-8").read().splitlines() if "X18" in ln]
    if not lines:
        print("G1-LEDGER-REFUSED no X18 row")
        return 1
    t = "\n".join(lines)
    low = t.lower()
    need = {"SOC2_MSLOGS": "SOC2_MSLOGS" in t, "retired": "retired" in low, "departure (1)": "departure (1)" in low, "departure (2)": "departure (2)" in low,
            "KMS": "KMS" in t, "raw audit pull": "raw audit pull" in low, "Andrew-direct": "Andrew-direct" in t}
    miss = [k for k, v in need.items() if not v]
    if miss:
        print("G1-LEDGER-REFUSED X18 lacks %s" % miss)
        return 1
    print("G1-LEDGER-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"rows": rows, "ledger": ledger}.get(mode)
    sys.exit(fn() if fn else 2)
