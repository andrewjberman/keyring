"""Read-only census of the upload lane's rows in irpt-requests for one tenant (consistent reads, all pages).

    python upload_rows.py [tenant]

Prints each prefix's count and, per row, the key plus the state/input_id/upload_id/reason fields. It makes no writes.
Control: the SELECTION# count, a prefix already known to be non-empty.
"""
import json
import subprocess
import sys

AWS = r"C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\aws.cmd"
TABLE = "irpt-requests"
TENANT = sys.argv[1] if len(sys.argv) > 1 else "cottonwood"
FIELDS = ("state", "upload_id", "input_id", "normalization_revision", "dispatched_at", "reason", "findings_total")


def query(prefix):
    items, start = [], None
    while True:
        cmd = [AWS, "dynamodb", "query", "--table-name", TABLE, "--consistent-read", "--output", "json",
               "--key-condition-expression", "tenant = :t AND begins_with(request_revision, :p)",
               "--expression-attribute-values", json.dumps({":t": {"S": TENANT}, ":p": {"S": prefix}})]
        if start:
            cmd += ["--exclusive-start-key", json.dumps(start)]
        out = subprocess.run(cmd, capture_output=True, text=True)
        if out.returncode != 0:
            raise SystemExit("ERROR: query %s rc=%d %s" % (prefix, out.returncode, out.stderr.strip()[:300]))
        page = json.loads(out.stdout)
        items += page.get("Items", [])
        start = page.get("LastEvaluatedKey")
        if not start:
            return items


def scalar(value):
    return next(iter(value.values())) if isinstance(value, dict) and len(value) == 1 else value


for prefix in ("UPLOAD#", "NORMALIZATION#", "INPUT#", "SELECTION#"):
    rows = query(prefix)
    print("%s %s count=%d" % (TENANT, prefix, len(rows)))
    if prefix == "SELECTION#":
        continue
    for row in rows:
        shown = {k: scalar(row[k]) for k in FIELDS if k in row}
        print("   ", scalar(row["request_revision"]), json.dumps(shown, default=str))
