#!/usr/bin/env bash
# Hop 7, second window -- leg S (ONE operator sign-in on the host) then leg J (ONE job attempt) only if S authenticates.
#
#   bash hop7b_run.sh --plan     # the solo gate and what each leg would run; no vendor call, no secret read, no POST
#   bash hop7b_run.sh --leg-s    # ONE run of the canonical sign-in wrapper on the host, in the resident's context
#   bash hop7b_run.sh --leg-j    # ONE upload and ONE Overview; refuses unless leg S's output reads AUTHENTICATED
#
# AUTHORITY: CTO rulings batch 70 (2026-10-01). Packet: ../HOP7B/WINDOW_PACKET_HOP7B_SIGNIN_THEN_JOB_20261001.md.
# Each leg is run once. A leg whose output file exists refuses: there is no second sign-in and no second attempt here.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../HOP7B"
ROOT="$HERE/../../../../../.."
AWS="$ROOT/.tools/aws"
S_OUT="$OUT/LEG_S_OUTPUT_20261001.txt"
mkdir -p "$OUT"

# SOLO GATE (the hop-7 packet's, applied before BOTH legs): no job in a non-terminal state and both queues empty, so
# the resident makes no identity read or sign-in of its own beside the operator's.
solo_gate() {
  local blockers depth dlq
  blockers=$("$AWS" dynamodb scan --table-name irpt-jobs \
    --filter-expression "#s IN (:a,:b,:c,:d,:e,:f,:g,:h)" --expression-attribute-names '{"#s":"state"}' \
    --expression-attribute-values '{":a":{"S":"RECEIVED"},":b":{"S":"CLAIMED"},":c":{"S":"SUBMITTING"},":d":{"S":"SUBMITTED"},":e":{"S":"DOWNLOADING"},":f":{"S":"EXTRACTING"},":g":{"S":"CERTIFYING"},":h":{"S":"UNCERTAIN"}}' \
    --query 'Items[].job.S' --output text)
  depth=$("$AWS" sqs get-queue-attributes --queue-url https://queue.amazonaws.com/313476888478/irpt-generation \
    --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible \
    --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text | tr -s '\t ' '/')
  dlq=$("$AWS" sqs get-queue-attributes --queue-url https://queue.amazonaws.com/313476888478/irpt-generation-dlq \
    --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible \
    --query 'Attributes.[ApproximateNumberOfMessages,ApproximateNumberOfMessagesNotVisible]' --output text | tr -s '\t ' '/')
  echo "  SOLO GATE: non-terminal jobs [${blockers}] | irpt-generation $depth | dead-letter $dlq"
  [ -z "$(echo "$blockers" | tr -d '[:space:]')" ] || { echo "REFUSED: another job is non-terminal." >&2; return 1; }
  [ "$depth" = "0/0" ] || { echo "REFUSED: the queue is not empty." >&2; return 1; }
  [ "$dlq" = "0/0" ] || { echo "REFUSED: the dead-letter queue is not empty." >&2; return 1; }
}

case "${1:-}" in
  --plan)
    solo_gate || exit 3
    echo "  leg S would send: live_walk/leg_s_host.sh sha256 $(sha256sum "$HERE/leg_s_host.sh" | cut -c1-16) (ONE sign-in)"
    echo "  leg J would run : hop7_run.sh with base H7B_overview_cottonwood (ONE upload, ONE Overview)"
    echo "PLAN ONLY -- nothing fired."
    ;;
  --leg-s)
    [ ! -e "$S_OUT" ] || { echo "REFUSED: $S_OUT exists; leg S was already run. No second sign-in under this packet." >&2; exit 6; }
    solo_gate || exit 3
    echo "=== leg S fire at $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    python "$HERE/host_read.py" "$HERE/leg_s_host.sh" "2.0.0_SA_COO~Y hop-7 leg S: ONE operator sign-in, CTO batch 70" > "$S_OUT" 2>&1
    echo "host_read rc=$?"
    cat "$S_OUT"
    ;;
  --leg-j)
    grep -q '^LEG_S_VERDICT=AUTHENTICATED[[:space:]]*$' "$S_OUT" || { echo "REFUSED: leg S did not read AUTHENTICATED; leg J is not run." >&2; exit 7; }
    HOP7_OUT="$OUT" HOP7_BASE=H7B_overview_cottonwood \
      HOP7_AUTHORITY="hop-7 leg J; CTO batch 70; Andrew-direct 2026-09-27 124xZ; ledger irpt-hop7b-signin-then-job-20261001" \
      bash "$HERE/hop7_run.sh"
    ;;
  *)
    echo "usage: hop7b_run.sh --plan | --leg-s | --leg-j" >&2
    exit 2
    ;;
esac
