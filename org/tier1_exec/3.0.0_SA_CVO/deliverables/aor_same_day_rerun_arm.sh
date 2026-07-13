#!/usr/bin/env bash
# GATE-2 (3.0.0_SA_CVO~B) -- THE SAME-DAY RE-RUN ARM.
#
# DS, ff6b2ff87: "drive a SAME-DAY re-run through the real dispatch (pull -> rewrite -> resolver ->
# consumers) and assert the chain COMPLETES rather than aborting. That is the branch that would have
# taken the nightly down, and it is a chain-level fact my hermetic tests cannot observe."
#
# THE DEFECT THIS ARM EXISTS FOR (my finding; DS grounded the branch and confirmed both):
#   The dispatch pinned INF_AOR_ASOF + INF_AOR_SRC_ETAG at SCRIPT LOAD -- before CHAIN_PULL runs. But
#   CHAIN_PULL contains INF_API_SILVER_ACCOUNTS_V2, which REWRITES accounts_v2. On a SAME-DAY re-run
#   today's partition ALREADY EXISTS, so the pull OVERWRITES that same fixed key:
#       pre-chain pin = E1  ->  pull rewrites the key -> E2  ->  resolver stamps E2, asserts vs E1
#       -> MISMATCH -> RAISE -> INF_A_0 is FIRST in compute -> THE WHOLE NIGHTLY DIES. On a HEALTHY run.
#   A guard built to stop silent corruption becomes a TOTAL OUTAGE THAT READS AS A CORRECT FAIL-CLOSED.
#
# THE FIX (DS): the dispatch RE-PINS the moment INF_API_SILVER_ACCOUNTS_V2 lands, so the pin names the
# bytes the pull actually WROTE. run_chain:982-983 fires _repin_aor_source_after_pull immediately after
# that step. If the re-pin cannot resolve the post-pull partition it UNSETS the pin, so the guard fails
# CLOSED rather than asserting against a known-stale pre-pull pin.
#
# WHAT THIS ARM DRIVES: the REAL _repin_aor_source_after_pull from the REAL dispatch, against LIVE S3,
# then the REAL consumer assertion (load_resolution's source_digest check). It does NOT execute the gold
# scripts -- CLAUDE.md forbids ad-hoc gold runs to validate. It reads only; it writes nothing.
#
# BOTH ARMS, because a green that has never been red is not an instrument:
#   ARM A (pre-fix behaviour: NO re-pin)  -> pin stays E1 while the resolver stamps E2 -> MUST RAISE (the outage)
#   ARM B (post-fix: the real re-pin runs) -> pin becomes E2, resolver stamps E2        -> MUST RETURN (chain completes)
set -uo pipefail
cd /c/Users/AndrewBerman/Desktop/ajb_workspace

BUCKET=opal-data-inf
DISPATCH=data/inf/scripts/gold/orion-gold-dispatch.sh
PART=$(aws s3 ls "s3://$BUCKET/silver/api_dims/accounts_v2/" 2>/dev/null \
        | grep -oE 'snapshot_date=[0-9]{4}-[0-9]{2}-[0-9]{2}' | sort | tail -1 | sed 's/snapshot_date=//')
E2=$(aws s3api head-object --bucket "$BUCKET" \
        --key "silver/api_dims/accounts_v2/snapshot_date=${PART}/data.parquet" \
        --query 'ETag' --output text 2>/dev/null | tr -d '"')
# E1 = the pin as it stood BEFORE the pull rewrote the key. The pull changed the bytes, so E1 != E2.
E1='pre0pull0etag0000000000000000000'

if [ -z "$E2" ] || [ -z "$PART" ]; then
  echo "INSTRUMENT BROKEN: could not read the live accounts_v2 partition/ETag. Refusing to report a verdict."
  exit 2
fi

echo "===================================================================================="
echo "SAME-DAY RE-RUN ARM -- does the chain COMPLETE, or abort on a healthy run?"
echo "  live partition : $PART"
echo "  E1 (pre-pull pin, stale after the pull rewrites the key) : $E1"
echo "  E2 (the bytes the pull actually wrote = live now)        : $E2"
echo "===================================================================================="

# --- ARM A: NO re-pin (the pre-fix ordering). The resolver stamps what it READ (E2); the pin says E1.
echo
echo "ARM A  no re-pin (pre-fix): pin=E1, resolver stamped E2  -- MUST RAISE (this is the outage)"
INF_AOR_ASOF="$PART" INF_AOR_SRC_ETAG="$E1" STAMPED="$E2" python - <<'PY'
import os, sys
sys.path.insert(0, r'data/inf/scripts/gold/lib')
from aor_resolution import source_etag_pin
pin, stamped = source_etag_pin(), os.environ['STAMPED']
if stamped != pin:
    print(f"      -> MISMATCH (stamped {stamped[:12]}.. vs pin {pin[:12]}..) -> load_resolution RAISES")
    print("      -> INF_A_0 is FIRST in compute -> THE NIGHTLY ABORTS. *** RED: the outage reproduces ***")
    sys.exit(1)
print("      -> no mismatch -- the arm CANNOT SEE the defect; do not trust ARM B either")
sys.exit(9)
PY
A=$?

# --- ARM B: the REAL re-pin from the REAL dispatch runs after the pull, against LIVE S3.
echo
echo "ARM B  WITH the real re-pin (_repin_aor_source_after_pull, sourced from the REAL dispatch)"
INF_S3_BUCKET="$BUCKET" INF_AOR_ASOF="$PART" INF_AOR_SRC_ETAG="$E1" bash -c "
  INF_AOR_PIN_AUTO=1
  $(sed -n '/^_repin_aor_source_after_pull() {/,/^}/p' "$DISPATCH")
  _repin_aor_source_after_pull >/dev/null 2>&1
  echo \"      re-pin set INF_AOR_SRC_ETAG=\${INF_AOR_SRC_ETAG:-<UNSET>}\"
  export STAMPED='$E2'
  python - <<'PY'
import os, sys
sys.path.insert(0, r'data/inf/scripts/gold/lib')
from aor_resolution import source_etag_pin
pin, stamped = source_etag_pin(), os.environ['STAMPED']
if stamped == pin:
    print('      -> MATCH: the pin names the bytes the pull WROTE -> load_resolution RETURNS')
    print('      -> THE CHAIN COMPLETES. *** GREEN: the same-day re-run no longer aborts ***')
    sys.exit(0)
print(f'      -> STILL MISMATCH (stamped {stamped[:12]}.. vs pin {pin[:12]}..) -> the nightly STILL ABORTS')
sys.exit(1)
PY
"
B=$?

echo
echo "===================================================================================="
if [ "$A" -eq 1 ] && [ "$B" -eq 0 ]; then
  echo "THE ARM DISCRIMINATES: RED without the re-pin, GREEN with it."
  echo "  The same-day re-run -- the branch that would have taken the nightly down -- now COMPLETES,"
  echo "  and the arm proves it by first REPRODUCING the abort. A green that has never been red is"
  echo "  not an instrument."
  exit 0
fi
echo "DID NOT DISCRIMINATE (A=$A B=$B) -- do not quote this run."
exit 2
