#!/usr/bin/env bash
# Hop 8 window, on the st7 resident -- leg P (ONE liveness read), leg S (ONE operator sign-in, only if P reads the
# session NOT_LIVE), leg J (ONE job attempt, only on a live session).
#
#   bash hop8_run.sh --plan     # the running root, the solo gate and what each leg would run; no vendor call
#   bash hop8_run.sh --leg-p    # ONE GET of the report-template route through the resident's session classes
#   bash hop8_run.sh --leg-s    # ONE operator sign-in; refuses unless leg P's output reads PROBE_VERDICT=NOT_LIVE:
#   bash hop8_run.sh --leg-j    # ONE upload and ONE Overview; refuses unless P reads LIVE, or S reads AUTHENTICATED
#                               # and at least 600 seconds have passed since leg S ended
#
# Packet: ../HOP8/WINDOW_PACKET_HOP8_PROBE_SIGNIN_JOB_20261001.md. Each leg is run once: a leg whose output file exists
# refuses. Every leg refuses unless the resident's running root is the st7 root the packet names.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="${HOP8_OUT:-$HERE/../HOP8}"                 # a later window names its own folder, root, base and ledger
ROOT="$HERE/../../../../../.."
AWS="$ROOT/.tools/aws"
P_OUT="$OUT/LEG_P_OUTPUT_20261001.txt"
S_OUT="$OUT/LEG_S_OUTPUT_20261001.txt"
WANT_ROOT="${HOP8_ROOT:-/opt/irpt-resident/a3b35fd376-st7}"
BASE="${HOP8_BASE:-H8_overview_cottonwood}"
AUTHORITY="${HOP8_AUTHORITY:-hop-8 window leg J; CTO batch 76 item 5; Andrew-direct 2026-09-27 124xZ; ledger irpt-hop8-probe-signin-job-20261001}"
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

# The running root, read on the host (no vendor call). Every leg runs on st7 or not at all.
root_gate() {
  local probe running
  probe="$(mktemp)"
  printf '%s\n' 'readlink /proc/$(systemctl show irpt-analysis-resident.service -p MainPID --value)/cwd' > "$probe"
  running=$(python "$HERE/host_read.py" "$probe" "2.0.0_SA_COO~Y read-only: the running resident root" 2>&1 | grep -E '^/opt/irpt-resident/' | tr -d '\r' | head -n 1)
  rm -f "$probe"
  echo "  ROOT GATE: running root [$running]"
  [ "$running" = "$WANT_ROOT" ] || { echo "REFUSED: the resident is not running $WANT_ROOT." >&2; return 1; }
}

case "${1:-}" in
  --plan)
    root_gate || exit 4
    solo_gate || exit 3
    echo "  leg P would send: live_walk/session_probe_host.sh sha256 $(sha256sum "$HERE/session_probe_host.sh" | cut -c1-16) (ONE GET, no sign-in)"
    echo "  leg S would send: live_walk/leg_s_host.sh sha256 $(sha256sum "$HERE/leg_s_host.sh" | cut -c1-16) (ONE sign-in; only if P reads NOT_LIVE)"
    echo "  leg J would run : hop7_run.sh with base $BASE (ONE upload, ONE Overview)"
    echo "PLAN ONLY -- nothing fired."
    ;;
  --leg-p)
    [ ! -e "$P_OUT" ] || { echo "REFUSED: $P_OUT exists; leg P was already run." >&2; exit 6; }
    root_gate || exit 4
    solo_gate || exit 3
    echo "=== leg P fire at $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    python "$HERE/host_read.py" "$HERE/session_probe_host.sh" "2.0.0_SA_COO~Y hop-8 leg P: ONE session liveness read" > "$P_OUT" 2>&1
    echo "host_read rc=$?"
    cat "$P_OUT"
    ;;
  --leg-s)
    [ ! -e "$S_OUT" ] || { echo "REFUSED: $S_OUT exists; leg S was already run. No second sign-in under this packet." >&2; exit 6; }
    grep -q '^PROBE_VERDICT=NOT_LIVE:' "$P_OUT" || { echo "REFUSED: leg P did not read NOT_LIVE; leg S is not run." >&2; exit 7; }
    root_gate || exit 4
    solo_gate || exit 3
    echo "=== leg S fire at $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    python "$HERE/host_read.py" "$HERE/leg_s_host.sh" "2.0.0_SA_COO~Y hop-8 leg S: ONE operator sign-in" > "$S_OUT" 2>&1
    echo "host_read rc=$?"
    cat "$S_OUT"
    ;;
  --leg-j)
    if grep -q '^PROBE_VERDICT=LIVE[[:space:]]*$' "$P_OUT"; then
      echo "  leg J on: leg P read LIVE"
    elif grep -q '^LEG_S_VERDICT=AUTHENTICATED[[:space:]]*$' "$S_OUT" 2>/dev/null; then
      AGE=$(( $(date +%s) - $(stat -c %Y "$S_OUT") ))
      echo "  leg J on: leg S read AUTHENTICATED, $AGE seconds ago"
      [ "$AGE" -ge 600 ] || { echo "REFUSED: fewer than 600 seconds since the sign-in; the packet spaces the job from it." >&2; exit 8; }
    else
      echo "REFUSED: no live session by leg P or leg S; leg J is not run." >&2; exit 7
    fi
    root_gate || exit 4
    HOP7_OUT="$OUT" HOP7_BASE="$BASE" HOP7_AUTHORITY="$AUTHORITY" bash "$HERE/hop7_run.sh"
    ;;
  *)
    echo "usage: hop8_run.sh --plan | --leg-p | --leg-s | --leg-j" >&2
    exit 2
    ;;
esac
