#!/usr/bin/env python3
"""Read the settings-table lines of ONE kept refused vendor PDF, by its artifact id. Read-only; no vendor call.

    python kept_pdf_settings_rows.py <tenant> <ART-id> <portfolio name>

The PDF is fetched by the version its index row names to a scratch directory OUTSIDE the repo and deleted afterwards;
it is never committed or uploaded. Printed: the index row's family, owner firm and byte count; the reader's verdict
for the name (extract.calculation_settings) and its census (extract.settings_census); and, for each page that carries
the settings table, the lines from the table's title to two lines past the last line starting with the name, with the
request id shortened. Meant for this lane's own test uploads (AAPL and VNQ); do not run it on a client's report.
ASCII only.
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "..", ".."))
AWS = os.path.join(REPO, ".tools", "aws.cmd")
sys.path.insert(0, os.path.join(REPO, "infra", "aws", "lambda", "investor-reporting", "ycharts", "extract"))
import extract  # noqa: E402


def aws(*args):
    out = subprocess.run([AWS, *args], capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit("ERROR: aws %s rc=%d %s" % (args[1], out.returncode, out.stderr.strip()[:300]))
    return out.stdout


def main(argv):
    tenant, artifact, name = argv[1], argv[2], argv[3]
    if not re.fullmatch(r"ART-[0-9a-f]{64}", artifact):
        raise SystemExit("ERROR: an ART-<64 hex> artifact id is required")
    row = json.loads(aws("dynamodb", "get-item", "--table-name", "irpt-requests", "--consistent-read", "--key",
                         json.dumps({"tenant": {"S": tenant}, "request_revision": {"S": "ARTIFACT#" + artifact}}),
                         "--output", "json")).get("Item")
    if not row:
        raise SystemExit("ERROR: no index row for that artifact in that firm")
    blob = {k: list(v.values())[0] for k, v in row["blob"]["M"].items()}
    ref = {k: list(v.values())[0] for k, v in row["ref"]["M"].items()}
    owner = {k: list(v.values())[0] for k, v in row["owner"]["M"].items()}
    print("index row: family %s | owner firm %s | bytes %s | sha256 %s" % (
        ref.get("family"), owner.get("firm_id"), ref.get("byte_length"), str(ref.get("sha256"))[:12]))
    scratch = tempfile.mkdtemp(prefix="irpt_kept_pdf_")
    try:
        target = os.path.join(scratch, "kept.pdf")
        aws("s3api", "get-object", "--bucket", blob["bucket"], "--key", blob["key"],
            "--version-id", blob["version_id"], target, "--output", "json")
        data = open(target, "rb").read()
        printed = extract.calculation_settings(data, name)
        print("reader: %s" % (printed if printed is None else {"type": printed.get("type"), "as_of": printed.get("as_of")}))
        print("census: %s" % json.dumps(extract.settings_census(data, name)))
        with extract._plumber().open(io.BytesIO(data)) as pdf:
            for number, page in enumerate(pdf.pages, 1):
                text = page.extract_text() or ""
                at = text.find(extract.SETTINGS_TABLE)
                if at < 0:
                    continue
                lines = text[at:].splitlines()
                last = max((i for i, line in enumerate(lines) if line.startswith(name + " ")), default=3)
                print("--- page %d of %d" % (number, len(pdf.pages)))
                for line in lines[:last + 3]:
                    print("   | " + re.sub(r"REQ-[0-9a-f]{24}", "REQ-<id>", line)[:170])
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
        print("scratch removed: %s" % (not os.path.exists(scratch)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
