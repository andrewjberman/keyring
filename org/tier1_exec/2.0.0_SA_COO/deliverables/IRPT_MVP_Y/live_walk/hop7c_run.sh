#!/usr/bin/env bash
# Hop 7, third window -- leg P (ONE liveness read of the stored session) then leg J (ONE job attempt) only if P reads LIVE.
#
#   bash hop7c_run.sh --plan     # the solo gate and what each leg would run; no vendor call, no secret read, no POST
#   bash hop7c_run.sh --leg-p    # ONE GET of the report-template route through the resident's session classes
#   bash hop7c_run.sh --leg-j    # ONE upload and ONE Overview; refuses unless leg P's output reads PROBE_VERDICT=LIVE
#
# Packet: ../HOP7C/WINDOW_PACKET_HOP7C_PROBE_THEN_JOB_20261001.md. Each leg is run once: a leg whose output file exists
# refuses. No sign-in is made by either leg's script.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../HOP7C"
ROOT="$HERE/../../../../../.."
AWS="$ROOT/.tools/aws"
P_OUT="$OUT/LEG_P_OUTPUT_20261001.txt"
mkdir -p "$OUT"

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
    echo "  leg P would send: live_walk/session_probe_host.sh sha256 $(sha256sum "$HERE/session_probe_host.sh" | cut -c1-16) (ONE GET, no sign-in)"
    echo "  leg J would run : hop7_run.sh with base H7C_overview_cottonwood (ONE upload, ONE Overview)"
    echo "PLAN ONLY -- nothing fired."
    ;;
  --leg-p)
    [ ! -e "$P_OUT" ] || { echo "REFUSED: $P_OUT exists; leg P was already run." >&2; exit 6; }
    solo_gate || exit 3
    echo "=== leg P fire at $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    python "$HERE/host_read.py" "$HERE/session_probe_host.sh" "2.0.0_SA_COO~Y hop-7 leg P: ONE session liveness read" > "$P_OUT" 2>&1
    echo "host_read rc=$?"
    cat "$P_OUT"
    ;;
  --leg-j)
    grep -q '^PROBE_VERDICT=LIVE[[:space:]]*$' "$P_OUT" || { echo "REFUSED: leg P did not read LIVE; leg J is not run." >&2; exit 7; }
    HOP7_OUT="$OUT" HOP7_BASE=H7C_overview_cottonwood \
      HOP7_AUTHORITY="hop-7 third window leg J; Andrew-direct 2026-09-27 124xZ; ledger irpt-hop7c-probe-then-job-20261001" \
      bash "$HERE/hop7_run.sh"
    ;;
  *)
    echo "usage: hop7c_run.sh --plan | --leg-p | --leg-j" >&2
    exit 2
    ;;
esac
