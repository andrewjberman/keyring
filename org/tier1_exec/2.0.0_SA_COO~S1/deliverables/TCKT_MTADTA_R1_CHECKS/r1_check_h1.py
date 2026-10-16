"""TCKT_MTADTA round 1, cell MD-h-1 checks. Run from the repo (worktree) root.

  python r1_check_h1.py rows    -> H1-ROWS-OK   (registry rows, builder output, generated targets in sync)
  python r1_check_h1.py ledger  -> H1-R20-OK    (the R20 entry for the drop at collection)
  python r1_check_h1.py tf      -> H1-TF-OK     (the bucket and key, and nothing of the access policies)
"""
import filecmp
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "lib"))

WANT_BRONZE = "s3://opal-data-trino/m365-metadata/trino/bronze/audit_events/date=20261016/events.json.gz"
WANT_STATE = "s3://opal-data-trino/m365-metadata/trino/state/subscription_cursor/current/cursor.json"


def rows():
    import opal_naming as n

    try:
        n.validate()
    except Exception as e:  # noqa: BLE001
        print("H1-ROWS-REFUSED validate: %s" % e)
        return 1
    try:
        got = n.address("m365-metadata", "trino", "bronze", "audit_events", "date=20261016", object="events.json.gz")
        st = n.address("m365-metadata", "trino", "state", "subscription_cursor", "current", object="cursor.json")
        nm = n.name("m365-metadata", None, "trino-collector", "lambda")
        b = n.grade("opal-data-trino", "S3_BUCKET")
        s = n.grade("m365-metadata/trino/api-credentials", "SECRET")
    except Exception as e:  # noqa: BLE001
        print("H1-ROWS-REFUSED builder: %s" % e)
        return 1
    bad = []
    if got != WANT_BRONZE:
        bad.append("bronze address %r" % got)
    if st != WANT_STATE:
        bad.append("state address %r" % st)
    if nm != "m365-metadata-trino-collector-lambda":
        bad.append("name %r" % nm)
    if b[0] != "CONFORMANT":
        bad.append("bucket grade %r" % (b,))
    if s[0] != "CONFORMANT":
        bad.append("secret grade %r" % (s,))
    out = tempfile.mkdtemp()
    p = subprocess.run([sys.executable, "lib/opal_naming.py", "generate", "--out", out], capture_output=True, text=True)
    if p.returncode != 0:
        bad.append("generate rc=%d" % p.returncode)
    moved = []
    for d, _, fs in os.walk(out):
        for f in fs:
            fresh = os.path.join(d, f)
            rel = os.path.relpath(fresh, out)
            cur = os.path.join(ROOT, rel)
            if rel.replace(os.sep, "/").startswith("portal/") and not os.path.isdir(os.path.join(ROOT, "portal", "src")):
                continue  # no portal checkout in this worktree: the report names it
            if not os.path.exists(cur) or not filecmp.cmp(fresh, cur, shallow=False):
                moved.append(rel.replace(os.sep, "/"))
    if moved:
        bad.append("targets stale n=%d first=%s" % (len(moved), moved[:3]))
    if bad:
        print("H1-ROWS-REFUSED " + "; ".join(bad))
        return 1
    print("H1-ROWS-OK targets=%d" % sum(len(f) for _, _, f in os.walk(out)))
    return 0


def ledger():
    p = os.path.join(ROOT, "infra", "logic", "06_CONFORMANCE_LEDGER.md")
    t = open(p, encoding="utf-8").read()
    need = ["m365-metadata", "dropped at the outset", "R9", "Andrew-direct", "opal-data-trino", "PERMANENT"]
    miss = [k for k in need if k not in t]
    key_ok = ("KMS" in t and "key" in t and "m365-metadata" in t)
    if miss or not key_ok:
        print("H1-R20-MISSING %s" % miss)
        return 1
    print("H1-R20-OK")
    return 0


def tf():
    p = os.path.join(ROOT, "infra", "aws", "terraform", "trino", "main.tf")
    if not os.path.exists(p):
        print("H1-TF-REFUSED no main.tf")
        return 1
    t = open(p, encoding="utf-8").read()
    bad = []
    for res in ("aws_s3_bucket", "aws_kms_key", "aws_s3_bucket_server_side_encryption_configuration",
                "aws_s3_bucket_public_access_block"):
        if not re.search(r'resource\s+"%s"' % res, t):
            bad.append("missing " + res)
    for res in ("aws_s3_bucket_policy", "aws_kms_key_policy", "aws_iam_role", "aws_lambda_function", "aws_iam_group"):
        if re.search(r'resource\s+"%s"' % res, t):
            bad.append("belongs to MD-a-1, found " + res)
    if re.search(r'"opal-data-trino"', t):
        bad.append("literal bucket name; read it from the scopes.json row")
    if "enable_key_rotation" not in t or "sse_algorithm" not in t or "aws:kms" not in t:
        bad.append("key rotation or SSE-KMS default missing")
    if bad:
        print("H1-TF-REFUSED " + "; ".join(bad))
        return 1
    print("H1-TF-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"rows": rows, "ledger": ledger, "tf": tf}.get(mode)
    sys.exit(fn() if fn else 2)
