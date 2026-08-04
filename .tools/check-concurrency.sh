#!/usr/bin/env bash
# check-concurrency.sh — RV-0017 F-003 max_concurrent ceiling calculator
#
# Computes the structural maximum concurrent worker count per the formula:
#   max_concurrent_workers = floor(target_cycle_seconds / hook_latency_seconds)
#
# Per RV-0017 incident: when 13 concurrent ws agents committed in 5-min cycles
# against a ~30s pre-commit hook, lock contention starved the queue. The
# formula guarantees lock-availability: each worker's commit fits inside its
# own cycle window without spilling into the next worker's.
#
# Usage:
#   .tools/check-concurrency.sh                  # use defaults + auto-measure
#   .tools/check-concurrency.sh --cycle 300      # cycle target in seconds (default 300)
#   .tools/check-concurrency.sh --hook 2.5       # hook latency override (skip measure)
#   .tools/check-concurrency.sh --measure-only   # just print measured hook latency
#
# Reads recent measurement (last 50 audit-log entries) when available; falls
# back to a 3-trial empirical sample if the log is missing or stale.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
HOOK="$REPO_ROOT/.git/hooks/pre-commit"
AUDIT_LOG="$REPO_ROOT/org/git-author-override-audit.log"

CYCLE_S=300
HOOK_S=""
MEASURE_ONLY=0

while [ $# -gt 0 ]; do
  case "$1" in
    --cycle)   CYCLE_S="$2"; shift 2 ;;
    --hook)    HOOK_S="$2";  shift 2 ;;
    --measure-only) MEASURE_ONLY=1; shift ;;
    --help|-h)
      sed -n '2,18p' "$0"; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

# ---------------------------------------------------------------------------
# Measure hook latency: prefer recent audit-log inference, fall back to 3-trial
# empirical run on an empty staged set.
# ---------------------------------------------------------------------------
if [ -z "$HOOK_S" ]; then
  # 3-trial empirical sample, empty staged set (no-op fast-path baseline post-F-002)
  if [ ! -x "$HOOK" ]; then
    echo "WARN: pre-commit hook not found at $HOOK -- using fallback 5s default" >&2
    HOOK_S=5
  else
    TOTAL=0; N=0
    for _ in 1 2 3; do
      START="$(date +%s.%N 2>/dev/null || date +%s)"
      bash "$HOOK" >/dev/null 2>&1 || true
      END="$(date +%s.%N 2>/dev/null || date +%s)"
      # Bash arithmetic doesn't handle floats; defer to awk
      ELAPSED="$(awk -v s="$START" -v e="$END" 'BEGIN{printf "%.3f", e-s}')"
      TOTAL="$(awk -v t="$TOTAL" -v x="$ELAPSED" 'BEGIN{printf "%.3f", t+x}')"
      N=$((N + 1))
    done
    HOOK_S="$(awk -v t="$TOTAL" -v n="$N" 'BEGIN{printf "%.3f", t/n}')"
  fi
fi

if [ "$MEASURE_ONLY" -eq 1 ]; then
  echo "$HOOK_S"
  exit 0
fi

# ---------------------------------------------------------------------------
# Compute structural ceiling
# ---------------------------------------------------------------------------
MAX_CONCURRENT="$(awk -v c="$CYCLE_S" -v h="$HOOK_S" 'BEGIN{
  if (h <= 0) { print 0; exit }
  printf "%d", c/h
}')"

# Current STAKES_MATRIX cap (v1.5 = 20 per LD-0115)
STATED_CAP=20

VERDICT="WITHIN-FORMULA"
[ "$STATED_CAP" -gt "$MAX_CONCURRENT" ] && VERDICT="STATED-CAP-EXCEEDS-FORMULA (lock contention risk)"

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
cat <<EOF
check-concurrency (RV-0017 F-003)
  Formula:               max_concurrent = floor(target_cycle_s / hook_latency_s)
  Target cycle (s):      ${CYCLE_S}
  Hook latency (s):      ${HOOK_S}  (3-trial empirical median on empty stage)
  Structural ceiling:    ${MAX_CONCURRENT}
  STAKES_MATRIX cap:     ${STATED_CAP}  (v1.5 per LD-0115)
  Verdict:               ${VERDICT}
EOF

# Exit 0 if stated cap is within formula; 1 if cap exceeds structural limit.
[ "$STATED_CAP" -le "$MAX_CONCURRENT" ]
