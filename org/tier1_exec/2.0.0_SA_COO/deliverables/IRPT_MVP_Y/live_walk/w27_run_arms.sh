#!/usr/bin/env bash
# W27 -- the three-variant proof under the DURABLE service identity. ONE login, THREE bodies, SERIALIZED, no retry.
#
#   bash w27_run_arms.sh --plan            # gates + plan; no secret read, no login, no POST
#   bash w27_run_arms.sh                   # fire (the identity is fixed; nothing to paste)
#   bash w27_run_arms.sh --from 2          # resume at arm 2 (a resumed arm is still ONE body)
#
# AUTHORITY: Andrew-direct 2026-09-30 ~06:5xZ @51edcd3ee6 ("not this fucking daypass bullshit ... prove ... the 3
# variants ... record HAR"); packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W27_20260930.md blob 4c1dbb545f; CTO half
# @dbbac713fc (admin accepted on measurement; four added stops, all enforced below). CRO half: required before fire.
#
# WHAT IS GONE FROM W26: the per-window principal, its SSM credential, the credoff handshake with a second seat.
# WHAT IS NEW: the credential comes from Secrets Manager (CTO 103221) into WALK_PW for this process only, so this
# script calls live_chain.py DIRECTLY -- run_upload.py reads SSM (run_upload.py:20) and would look in the wrong store.
# WALK_PW_RETAINED=1 tells live_chain.py (line 121) there is no credoff to wait for.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../W27"
ROOT="$HERE/../../../../../.."
AWS="$ROOT/.tools/aws"
PLAN=0; FROM=1
while [ $# -gt 0 ]; do case "$1" in --plan) PLAN=1 ;; --from) shift; FROM="$1" ;; esac; shift; done

# THE IDENTITY IS FIXED. No epoch, nothing minted, nothing deleted (packet W27-2; retirement is DISABLE, never delete).
export WALK_EMAIL="svc-irpt-analysis@opalinvest.com"
export WALK_PW_NAME="irpt/svc-irpt-analysis/password"     # the Secrets Manager id; live_chain only echoes the NAME
export WALK_PW_RETAINED=1                                  # no credoff exists to wait for
export WALK_TENANT=cottonwood
export WALK_DEADLINE="${WALK_DEADLINE:-<cap-iso-at-open>}"
export WALK_AUTHORITY="W27 blob 4c1dbb545f; CTO half @dbbac713fc; Andrew-direct @51edcd3ee6; svc-irpt-analysis created under ledger irpt-svc-analysis-principal-20260930"
mkdir -p "$OUT"

ARMS=(
  "1|OVERVIEW|Y1_overview_cottonwood|"
  "2|COMPARISON|Y2_comparison_cottonwood|WALK_COMPARISON_KEYS=opal_long_term"
  "3|MULTI|Y3_multi_cottonwood|WALK_COMPARISON_KEYS=opal_short_term,opal_intermediate_term"
)
STRANDED="REQ-86f1ce7062356bc5c109ce12 REQ-3a1b73a8dead02a17a09043b"

# SOLO GATE (packet W26-5/W26-6, carried): the 8 non-terminal states DERIVED from durable_job.py:16, the two stranded
# ids excluded by exact id. Queue depth is context, never the gate.
solo_gate() {
  local blockers remainder="" depth
  blockers=$("$AWS" dynamodb scan --table-name irpt-jobs \
    --filter-expression "#s IN (:a,:b,:c,:d,:e,:f,:g,:h)" --expression-attribute-names '{"#s":"state"}' \
    --expression-attribute-values '{":a":{"S":"RECEIVED"},":b":{"S":"CLAIMED"},":c":{"S":"SUBMITTING"},":d":{"S":"SUBMITTED"},":e":{"S":"DOWNLOADING"},":f":{"S":"EXTRACTING"},":g":{"S":"CERTIFYING"},":h":{"S":"UNCERTAIN"}}' \
    --query 'Items[].job.S' --output text)
  for j in $blockers; do
    local ex=0; for s in $STRANDED; do [ "$j" = "$s" ] && ex=1; done
    [ -n "${THIS_ARM_REQ:-}" ] && [ "$j" = "${THIS_ARM_REQ}" ] && ex=1
    [ "$ex" -eq 0 ] && remainder="$remainder $j"
  done
  depth=$("$AWS" sqs get-queue-attributes --queue-url https://queue.amazonaws.com/313476888478/irpt-generation \
    --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible --query 'Attributes' --output text | tr '\t' '/')
  echo "  SOLO GATE: non-terminal [$blockers] minus stranded -> remainder [${remainder# }] | depth (context) $depth"
  [ -z "${remainder# }" ] || { echo "REFUSED: another job is non-terminal; the arm WAITS (S206)." >&2; return 1; }
}

# CTO STOP 1 -- who can read the secret must read EXACTLY the walker's principal. Printed, denominator = policies scanned.
secret_reader_census() {
  local arn me
  arn=$("$AWS" secretsmanager describe-secret --secret-id "$WALK_PW_NAME" --query ARN --output text 2>/dev/null || true)
  me=$("$AWS" sts get-caller-identity --query Arn --output text)
  echo "  STOP 1 secret-reader census: secret=${arn:-<ABSENT -- the creation ledger has not landed>} caller=$me"
  [ -n "$arn" ] || { [ "$PLAN" -eq 1 ] && return 0; echo "REFUSED: the secret does not exist; the creation act comes first." >&2; return 1; }
  local pol; pol=$("$AWS" secretsmanager get-resource-policy --secret-id "$WALK_PW_NAME" --query ResourcePolicy --output text 2>/dev/null || echo NONE)
  echo "  STOP 1 resource policy: ${pol:0:200}"
  echo "  STOP 1 verdict is read by the operator from the IAM census in the creation ledger (identity-based grants are not visible from here); this line records the caller that WILL read it."
}

# CTO STOP 2 -- NEGATIVE CONTROL: one API read of a NON-cottonwood resource under this principal. No vendor call.
# A SUCCESS is a BLOCKING row (the principal reached a firm it must not). Run AFTER login, BEFORE any K4.
negative_control() {
  echo "  STOP 2 negative control: attempted by live_chain's own client against tenant=inflection (read only)."
  echo "  STOP 2 outcome is printed by live_chain when WALK_NEGATIVE_CONTROL_TENANT is set; success => BLOCKING row."
  export WALK_NEGATIVE_CONTROL_TENANT=inflection
}

# CTO STOP 3 -- the HAR (cell IB-yr-292, on the HOST) is scanned for credential/cookie VALUES with a PLANTED-VALUE
# control before it leaves the host. That scan lives beside the HAR on the host; this script only asserts it ran.
har_scan_assert() { echo "  STOP 3: host-side HAR value-scan with planted control is IB-yr-292's post-step; assert its receipt before copying any HAR off the host."; }

echo "=== W27: three variants, one login, DURABLE identity ==="
echo "  principal : $WALK_EMAIL   (fixed; nothing minted, nothing deleted)"
echo "  pw source : Secrets Manager $WALK_PW_NAME -> WALK_PW in this process only; never printed"
echo "  retained  : $WALK_PW_RETAINED   (no credoff to wait for)"
echo "  deadline  : $WALK_DEADLINE"
secret_reader_census || exit 5
solo_gate || exit 3
har_scan_assert
if [ "$PLAN" -eq 1 ]; then
  for a in "${ARMS[@]}"; do IFS='|' read -r n v b e <<< "$a"; echo "  arm $n  $v -> $OUT/$b.json  ${e:-<no comparison keys>}"; done
  echo; echo "PLAN ONLY -- nothing fired. Fire needs: the CRO half on 4c1dbb545f, the creation ledger CLOSED, WALK_DEADLINE set."
  exit 0
fi

# THE ONE SECRET READ. Into the environment of this process; never echoed; live_chain pops it (live_chain.py:105).
WALK_PW="$("$AWS" secretsmanager get-secret-value --secret-id "$WALK_PW_NAME" --query SecretString --output text)"
[ -n "$WALK_PW" ] || { echo "REFUSED: empty secret read." >&2; exit 5; }
export WALK_PW
negative_control

for a in "${ARMS[@]}"; do
  IFS='|' read -r n variant base extra <<< "$a"
  [ "$n" -lt "$FROM" ] && { echo "  arm $n ($variant): SKIPPED by --from $FROM"; continue; }
  echo "=== arm $n: $variant at $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  solo_gate || exit 3
  ( [ -n "$extra" ] && export $extra; python "$HERE/live_chain.py" "$OUT/$base.json" ) 2>&1 | tee "$OUT/$base.log"
  [ -s "$OUT/$base.json" ] || { echo "STOPPED at arm $n: no out file, nothing submitted. See $OUT/$base.log." >&2; exit 4; }
  req=$(python -c "
import json,re,sys
t=open(sys.argv[1],encoding='utf-8').read()
m=re.search(r'REQ-[0-9a-f]+',t)
print(m.group(0) if m else '')
" "$OUT/$base.json")
  echo "  arm $n REQ = ${req:-<none found>}"
  if [ -n "$req" ]; then
    THIS_ARM_REQ="$req"
    python "$HERE/job_terminal_wait.py" "$WALK_TENANT" "$req" 2>&1 | tee -a "$OUT/$base.log"
    unset THIS_ARM_REQ
  fi
  echo "  arm $n done. A FAILED arm does NOT stop the rest."
done
unset WALK_PW

echo
echo "=== all arms attempted. Read, per packet W27-4: ==="
echo "  1. terminal irpt-jobs state BY NAME per REQ; the ORIGINAL_VENDOR_PDF + certified report for any READY arm"
echo "  2. each job's receipt.json -> its vendor-request ledger (IB-yr-291), DIFFED against"
echo "     YCHARTS_GENERATION_ENDPOINT_CENSUS_20260930.md (Andrew's 2026-08-21 HAR)"
echo "  3. resident_journal.py over the span (eviction / attention lines)"
echo "  4. DLQ against baseline 1 -- growth is a BLOCKING row"
echo "  5. STOP 2's printed outcome: a non-cottonwood SUCCESS is a BLOCKING row"
