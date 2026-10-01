#!/usr/bin/env bash
# Hop 7 -- ONE Analysis attempt under the durable service identity: one upload (K4), one Overview submission (K5), no retry.
#
#   bash hop7_run.sh --plan     # the solo gate and the plan; no secret read, no login, no POST
#   bash hop7_run.sh            # fire
#
# AUTHORITY: CTO rulings batch 61 @8dcf5bbe7a item 5 and CTO 103571 (the controls are read; S238 disarmed, row S248);
# Andrew-direct 2026-09-27 ~12:4xZ ("yes you can run as many analysis attempts as needed": each attempt ONE upload and
# ONE submission, inside a window packet with both halves). Packet: ../HOP7/WINDOW_PACKET_HOP7_SOLO_JOB_20261001.md.
# The identity is the durable svc-irpt-analysis (nothing minted, nothing deleted). The password goes from Secrets Manager
# into WALK_PW for this process only and is never printed. live_chain.py makes EXACTLY one K4 POST and one K5 POST.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${HOP7_OUT:-$HERE/../HOP7}"          # a later packet's leg J names its own folder and base, so no evidence is overwritten
ROOT="$HERE/../../../../../.."
AWS="$ROOT/.tools/aws"
PLAN=0
[ "${1:-}" = "--plan" ] && PLAN=1

export WALK_EMAIL="svc-irpt-analysis@opalinvest.com"
export WALK_PW_NAME="irpt/svc-irpt-analysis/password"
export WALK_PW_RETAINED=1
export WALK_TENANT=cottonwood
export WALK_AUTHORITY="${HOP7_AUTHORITY:-hop-7 solo job; CTO batch 61 item 5 and 103571; Andrew-direct 2026-09-27 124xZ; ledger irpt-hop7-solo-job-20261001}"
mkdir -p "$OUT"
BASE="${HOP7_BASE:-H7_overview_cottonwood}"
[ ! -e "$OUT/$BASE.json" ] || [ "$PLAN" -eq 1 ] || { echo "REFUSED: $OUT/$BASE.json exists; this attempt was already made. A new attempt names a new base." >&2; exit 6; }

# SOLO GATE: no job in a non-terminal state, and the queue empty. The 8 non-terminal states are durable_job.py's.
solo_gate() {
  local blockers depth
  blockers=$("$AWS" dynamodb scan --table-name irpt-jobs \
    --filter-expression "#s IN (:a,:b,:c,:d,:e,:f,:g,:h)" --expression-attribute-names '{"#s":"state"}' \
    --expression-attribute-values '{":a":{"S":"RECEIVED"},":b":{"S":"CLAIMED"},":c":{"S":"SUBMITTING"},":d":{"S":"SUBMITTED"},":e":{"S":"DOWNLOADING"},":f":{"S":"EXTRACTING"},":g":{"S":"CERTIFYING"},":h":{"S":"UNCERTAIN"}}' \
    --query 'Items[].job.S' --output text)
  depth=$("$AWS" sqs get-queue-attributes --queue-url https://queue.amazonaws.com/313476888478/irpt-generation \
    --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible \
    --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text | tr -s '\t ' '/')
  echo "  SOLO GATE: non-terminal jobs [${blockers}] | queue visible/in-flight $depth"
  [ -z "$(echo "$blockers" | tr -d '[:space:]')" ] || { echo "REFUSED: another job is non-terminal." >&2; return 1; }
  [ "$depth" = "0/0" ] || { echo "REFUSED: the queue is not empty." >&2; return 1; }
}

echo "=== hop 7: ONE attempt, one login, the durable identity ==="
echo "  principal : $WALK_EMAIL"
echo "  pw source : Secrets Manager $WALK_PW_NAME -> WALK_PW in this process only; never printed"
echo "  tenant    : $WALK_TENANT   variant: overview (no comparison key)"
echo "  upload    : aapl-vnq-12.03.csv sha256 $(sha256sum "$HERE/../aapl-vnq-12.03.csv" | cut -c1-16)"
solo_gate || exit 3
if [ "$PLAN" -eq 1 ]; then
  ( export WALK_DEADLINE="$(date -u -d '+60 minutes' +%Y-%m-%dT%H:%M:%S+00:00)"; python "$HERE/live_chain.py" "$OUT/$BASE.plan.json" --dry )
  echo "PLAN ONLY -- nothing fired."
  exit 0
fi

export WALK_DEADLINE="${WALK_DEADLINE:-$(date -u -d '+60 minutes' +%Y-%m-%dT%H:%M:%S+00:00)}"
echo "  deadline  : $WALK_DEADLINE"
WALK_PW="$("$AWS" secretsmanager get-secret-value --secret-id "$WALK_PW_NAME" --query SecretString --output text)"
[ -n "$WALK_PW" ] || { echo "REFUSED: empty secret read." >&2; exit 5; }
export WALK_PW

echo "=== fire at $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
python "$HERE/live_chain.py" "$OUT/$BASE.json" 2>&1 | tee "$OUT/$BASE.log"
unset WALK_PW
[ -s "$OUT/$BASE.json" ] || { echo "STOPPED: no out file; nothing submitted. See $OUT/$BASE.log." >&2; exit 4; }
req=$(python -c "
import json,re,sys
t=open(sys.argv[1],encoding='utf-8').read()
m=re.search(r'REQ-[0-9a-f]+',t)
print(m.group(0) if m else '')
" "$OUT/$BASE.json")
echo "  REQ = ${req:-<none: K5 was not made>}"
if [ -n "$req" ]; then
  python "$HERE/job_terminal_wait.py" "$WALK_TENANT" "$req" --deadline "$WALK_DEADLINE" 2>&1 | tee -a "$OUT/$BASE.log"
fi
echo "=== the attempt is over. No second POST is made by this script. ==="
