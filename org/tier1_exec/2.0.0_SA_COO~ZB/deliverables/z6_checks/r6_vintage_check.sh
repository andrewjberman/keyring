#!/usr/bin/env bash
# OPAL_BBGTML R6 -- check: portal_lookup.py quotes the DATA vintage, never the write time, as the vintage.
# ARM 1 (the defect): platinum/mdpf/49financial/aum-metrics.json carries no as_of_date; its true vintage is
#   _provenance.source_vintages. The VINTAGE line must name that date (read from the object itself here, never typed)
#   and must not tell the reader to quote LastModified.
# ARM 2 (control, unchanged path): json/macro/macro_data.json carries data_as_of; its VINTAGE line still names data_as_of.
# Read-only S3 GETs on opal-data-portal-v2. Usage (repo root):
#   bash org/tier1_exec/2.0.0_SA_COO~ZB/deliverables/z6_checks/r6_vintage_check.sh
set -u
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT" || exit 3
PY="${R6_PYTHON:-/c/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311/python.exe}"
TOOL=org/tier0_utility/0.0.3_BG_BBGTerminal/tools/portal_lookup.py
KEY=platinum/mdpf/49financial/aum-metrics.json
want="$("$PY" - "$KEY" <<'EOF'
import boto3, json, sys
d = json.loads(boto3.client("s3", region_name="us-east-1").get_object(Bucket="opal-data-portal-v2", Key=sys.argv[1])["Body"].read())
v = sorted(set((d.get("_provenance") or {}).get("source_vintages", {}).values()))
print(v[0] if v else "NONE")
EOF
)"; want="$(echo "$want" | tr -d '\r' | tail -1)"
echo "expected vintage (the object's own _provenance.source_vintages): $want"
o1="$("$PY" "$TOOL" get mdpf-platinum "$KEY" --project period 2>&1 | tr -d '\r')"
v1="$(echo "$o1" | grep '^VINTAGE')"; echo "ARM 1: $v1"
o2="$("$PY" "$TOOL" get macro json/macro/macro_data.json --project data_as_of 2>&1 | tr -d '\r')"
v2="$(echo "$o2" | grep '^VINTAGE')"; echo "ARM 2: $v2"
ok=0
if [ "$want" = "NONE" ]; then echo "ARM 1: NOT-EXERCISED (object carries no source_vintages)"; ok=2
elif echo "$v1" | grep -q "$want" && echo "$v1" | grep -q 'source_vintages' && ! echo "$o1" | grep -q 'quote LastModified'; then echo "ARM 1: PASS"
else echo "ARM 1: FAIL"; ok=1; fi
if echo "$v2" | grep -q 'VINTAGE (data_as_of)'; then echo "ARM 2: PASS"; else echo "ARM 2: FAIL"; ok=1; fi
[ $ok -eq 0 ] && echo "R6: PASS" || echo "R6: FAIL"
exit $ok
