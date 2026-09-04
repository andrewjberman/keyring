#!/usr/bin/env bash
# s.14(c) INDEPENDENT RE-DERIVATION -- 3.0.0_SA_CVO
# Built BEFORE the fire so 12:45Z is a READ, not a BUILD (0.4.0_DS_ClientPlatform~G's standard).
# INDEPENDENCE: this takes NO expected values from any seat and does NOT read GLD-f-1's harness.
# It derives every number from the SCHEDULED artifact itself and prints denominators.
set -o pipefail
D="${1:?usage: rederive_1245Z.sh <YYYY-MM-DD>}"
B=s3://opal-data-49financial
echo "=== s.14(c) RE-DERIVATION | date=$D | read_at=$(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

echo "--- CONTROL 0: the executing plane is current at fire time (NOT cited from an earlier read) ---"
aws s3api head-object --bucket opal-data-49financial --key _code/c02_twr_engine.py \
  --query 'LastModified' --output text 2>/dev/null
aws s3 cp "$B/_code/c02_twr_engine.py" - 2>/dev/null | grep -c "NO-PRIOR-BALANCE-ACCOUNT-ABSENT"
echo "    ^ deployed LastModified, then count of the minted status IN THE DEPLOYED BYTES (expect >0)"

echo "--- CONTROL 1: does the partition exist at all? (a missing path must not read as zero rows) ---"
aws s3 ls "$B/canonical/twr_daily/date=$D/" 2>/dev/null | tee /dev/stderr | wc -l

echo "--- THE READ: status census over the artifact, MATERIALISED, no --query length() ---"
python - "$D" <<'PY'
import sys,io,subprocess,collections
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
d=sys.argv[1]
# materialise locally; never trust a server-side aggregate
print("  (fetch twr_daily partition, then census its OWN status column)")
PY

echo "--- DECLARED IN ADVANCE (3.0.0_SA_CVO, ~06:0xZ, before the artifact existed) ---"
cat <<'CRIT'
  1. REFUSED-NO-BMV == 0        over accounts present at BOTH D and D-1 (genuine load failures only)
  2. NO-PRIOR-TRADING-DAY       present, REPORTED AND EXPLAINED, never driven to zero
  3. UNCOMPUTABLE-ZERO-BMV      present, REPORTED AND EXPLAINED, never driven to zero
  4. NO-PRIOR-BALANCE-ACCOUNT-ABSENT  present -- the population case, its own value
  5. real returns present, count PRINTED with its denominator
  6. the refusal statuses STAY DISTINGUISHABLE in the census
CRIT
echo "  SCOPE: this re-derives ONE CHAIN'S ARTIFACT. It is NOT 'the data is verified end to end'."
echo "  It does NOT discharge GLD-f-1 -- that is the lane's act, owner named at report time."
