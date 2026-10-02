#!/usr/bin/env bash
# W26 -- Andrew's three-variant automated-submission proof. ONE login, THREE bodies, SERIALIZED, no retry.
#
#   bash w26_run_arms.sh --plan            # print what would run + the solo gate; no login, no POST
#   EPOCH=<epoch> bash w26_run_arms.sh     # fire, once the principal exists
#   EPOCH=<epoch> bash w26_run_arms.sh --from 2   # resume at arm 2 (a resumed arm is still ONE body)
#
# AUTHORITY: Andrew-direct 2026-09-30 ~04:4xZ ("prove an automated ycharts submission for each of the three
# variants right now ad hoc and see if we even get a generated export") and ~04:3xZ ("the owner of YCharts is
# COO~Y"). Packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W26_20260930.md, halves at CTO + CRO.
#
# WHY THIS FILE EXISTS BEFORE THE LAST HALF LANDS: the window is capped and Andrew's word does not extend to a
# second one. Everything decidable in advance is decided here so the only act left at fire time is to paste the
# epoch. Written after w25_s218_read.sh refused on an MSYS path mangle -- that lesson is baked in below.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../W26"
ROOT="$HERE/../../../../../.."
AWS="$ROOT/.tools/aws"
PLAN=0
FROM=1
while [ $# -gt 0 ]; do
  case "$1" in
    --plan) PLAN=1 ;;
    --from) shift; FROM="$1" ;;
  esac
  shift
done

EPOCH="${EPOCH:-}"
if [ -z "$EPOCH" ] && [ "$PLAN" -eq 0 ]; then
  echo "REFUSED: EPOCH is unset. It comes from the principal create; this script never invents one." >&2
  exit 2
fi
EPOCH_SHOWN="${EPOCH:-<epoch-at-create>}"

# NO LEADING SLASH on the parameter name. MSYS converts a leading-slash argv into a Windows path, which is what
# refused W25's first attempt at 03:33:05Z (row IRPT_BCKEND-S215's trap, one layer out).
export WALK_PW_NAME="irpt/ui-walk-principal/${EPOCH_SHOWN}/password"
export WALK_EMAIL="irpt-uiwalk-${EPOCH_SHOWN}@opal.test"
export WALK_TENANT=cottonwood
export WALK_DEADLINE="${WALK_DEADLINE:-<cap-iso-at-open>}"
export WALK_AUTHORITY="W26 packet blob a4ba10a9d4 (CTO half @1574863a17 re-affirmed 'Proceed'; CRO half re-affirm pending at authoring); Andrew-direct 2026-09-30 ~04:4xZ three variants + ~04:3xZ YCharts owner; MSTR runs credoff on Andrew's word ~05:5xZ"
# WALK_PW_RETAINED intentionally NOT exported: 0.0.0_AB_MSTR credoffs on the login line, before K4.

mkdir -p "$OUT"

# arm | variant | out basename | extra env
ARMS=(
  "1|OVERVIEW|Y1_overview_cottonwood|"
  "2|COMPARISON|Y2_comparison_cottonwood|WALK_COMPARISON_KEYS=opal_long_term"
  "3|MULTI|Y3_multi_cottonwood|WALK_COMPARISON_KEYS=opal_short_term,opal_intermediate_term"
)

# THE SOLO GATE (packet W26-5, enumeration W26-6 derived from durable_job.py:16). Queue depth is CONTEXT, never
# the gate: a permanently stranded message poisons a depth proxy forever. The two stranded ids are excluded by
# EXACT id, per the CTO's condition 9.
STRANDED="REQ-86f1ce7062356bc5c109ce12 REQ-3a1b73a8dead02a17a09043b"
solo_gate() {
  local blockers
  blockers=$("$AWS" dynamodb scan --table-name irpt-jobs \
    --filter-expression "#s IN (:a,:b,:c,:d,:e,:f,:g,:h)" \
    --expression-attribute-names '{"#s":"state"}' \
    --expression-attribute-values '{":a":{"S":"RECEIVED"},":b":{"S":"CLAIMED"},":c":{"S":"SUBMITTING"},":d":{"S":"SUBMITTED"},":e":{"S":"DOWNLOADING"},":f":{"S":"EXTRACTING"},":g":{"S":"CERTIFYING"},":h":{"S":"UNCERTAIN"}}' \
    --query 'Items[].job.S' --output text)
  local remainder=""
  for j in $blockers; do
    local excluded=0
    for s in $STRANDED; do [ "$j" = "$s" ] && excluded=1; done
    [ -n "${THIS_ARM_REQ:-}" ] && [ "$j" = "${THIS_ARM_REQ}" ] && excluded=1
    [ "$excluded" -eq 0 ] && remainder="$remainder $j"
  done
  local depth
  depth=$("$AWS" sqs get-queue-attributes --queue-url https://queue.amazonaws.com/313476888478/irpt-generation \
    --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible \
    --query 'Attributes' --output text | tr '\t' '/')
  echo "  SOLO GATE: non-terminal jobs [$blockers] minus stranded -> remainder [${remainder# }]"
  echo "  CONTEXT (not the gate): irpt-generation depth $depth"
  if [ -n "${remainder# }" ]; then
    echo "REFUSED: another job is non-terminal. The arm WAITS; it is not run alongside (row S206)." >&2
    return 1
  fi
  return 0
}

echo "=== W26: three variants, one login, serialized ==="
echo "  principal : $WALK_EMAIL"
echo "  pw param  : $WALK_PW_NAME   (no leading slash, deliberately)"
echo "  deadline  : $WALK_DEADLINE"
echo "  retained  : ${WALK_PW_RETAINED:-<unset -- MSTR credoffs on the login line>}"
echo
solo_gate || exit 3
echo

if [ "$PLAN" -eq 1 ]; then
  for a in "${ARMS[@]}"; do
    IFS='|' read -r n variant base extra <<< "$a"
    echo "  arm $n  $variant  -> $OUT/$base.json   ${extra:-<no comparison keys>}"
  done
  echo
  echo "PLAN ONLY -- nothing fired. Fill EPOCH and WALK_DEADLINE at open and re-run."
  exit 0
fi

for a in "${ARMS[@]}"; do
  IFS='|' read -r n variant base extra <<< "$a"
  [ "$n" -lt "$FROM" ] && { echo "  arm $n ($variant): SKIPPED by --from $FROM"; continue; }
  echo "=== arm $n: $variant at $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  # Re-read the gate before EVERY K5, never inherited from the arm before.
  solo_gate || exit 3
  ( [ -n "$extra" ] && export $extra
    python "$HERE/run_upload.py" "$OUT/$base.json" "$HERE/live_chain.py" ) 2>&1 | tee "$OUT/$base.log"

  if [ ! -s "$OUT/$base.json" ]; then
    echo "STOPPED at arm $n: the walk wrote no out file, so nothing was submitted. See $OUT/$base.log." >&2
    exit 4
  fi

  # The out path arrives as ARGV: a unix path inside a python -c SOURCE BODY is not converted and Windows python
  # cannot open it (row IRPT_BCKEND-S215, measured live in W24 and again in W25).
  req=$(python -c "
import json,re,sys
t=open(sys.argv[1],encoding='utf-8').read()
m=re.search(r'REQ-[0-9a-f]+',t)
print(m.group(0) if m else '')
" "$OUT/$base.json")
  echo "  arm $n REQ = ${req:-<none found>}"
  if [ -n "$req" ]; then
    THIS_ARM_REQ="$req"
    # SERIALIZE ON THE JOBS TERMINAL (CTO's W24 condition 1). live_chain returns at K5 acceptance, which is not
    # an outcome; an arm that does not wait here reintroduces the concurrency S206 measured.
    python "$HERE/job_terminal_wait.py" "$WALK_TENANT" "$req" 2>&1 | tee -a "$OUT/$base.log"
    unset THIS_ARM_REQ
  fi
  echo "  arm $n done. A FAILED arm does NOT stop the rest -- three independent results are the point."
done

echo
echo "=== all arms attempted. Now read, per packet W26-2: ==="
echo "  1. terminal irpt-jobs state BY NAME for each REQ"
echo "  2. the ORIGINAL_VENDOR_PDF object + certified report for any READY arm"
echo "  3. resident_journal.py over the span (eviction / attention lines)"
echo "  4. DLQ against its baseline of 1 -- growth is a BLOCKING row the same tick"
echo "  5. tell 0.0.0_AB_MSTR the terminal states so K1 is deleted ONLY when all three are terminal (W26-3)"
