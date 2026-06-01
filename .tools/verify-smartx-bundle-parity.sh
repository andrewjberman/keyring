#!/usr/bin/env bash
# =============================================================================
# verify-smartx-bundle-parity.sh -- smartx daily-DAG canonical<->bundle drift guard
# =============================================================================
# BMKAUD §3c INTERIM GUARD (COO/CTO 2026-06-01). Catches the "edits don't reach
# prod" failure class that caused the 202606 premature-June incident: the smartx
# daily pipeline runs the scripts BAKED INTO THE DOCKER BUNDLE
# (infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/), NOT the canonical
# edit copies (data/smartx/scripts/). When a fix lands in canonical but the bundle
# is not re-synced + the image not rebuilt, prod silently runs stale code.
#
# This guard DIFFS each daily-DAG-invoked script (canonical vs bundle) and FAILS
# (exit 1) on any divergence -- so the drift is caught at push/CI time, by design,
# not by luck. Run it pre-deploy + in CI before a smartx-exporter image build.
#
# SCOPE: only the scripts the daily DAG (run_smartx_pipeline.py) actually invokes
# or imports -- those MUST be byte-identical bundle<->canonical. Non-DAG scripts
# (analysis/adhoc) may legitimately diverge and are reported as INFO, not failure.
#
# Rule 16 compliant: uses only Git Bash 3.6.7 default utilities (diff, grep, awk,
# sed, basename). No pgrep/pkill/flock/etc.
# =============================================================================
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CANON_DIR="$ROOT/data/smartx/scripts"
BUNDLE_DIR="$ROOT/infra/aws/ec2/smartx-exporter/smartx-workspace/scripts"
DAG_ENTRY="$BUNDLE_DIR/run_smartx_pipeline.py"

if [ ! -d "$CANON_DIR" ] || [ ! -d "$BUNDLE_DIR" ]; then
  echo "ERROR: missing dir (canon=$CANON_DIR bundle=$BUNDLE_DIR)"; exit 2
fi
if [ ! -f "$DAG_ENTRY" ]; then
  echo "ERROR: DAG entry not found: $DAG_ENTRY"; exit 2
fi

# DAG-critical set = scripts run_smartx_pipeline.py invokes/imports, UNION an
# explicit floor (so a refactor of the entry script can't silently shrink scope).
EXPLICIT_FLOOR="run_smartx_pipeline.py pipeline_monitor.py compute_account_distribution.py consolidate_smartx_to_parquet.py organize_smartx_csvs.py aggregate_smartx_by_transaction_dates.py generate_smartx_timeseries_and_metrics.py"
DERIVED="$(grep -oE "[a-zA-Z0-9_]+\.py" "$DAG_ENTRY" 2>/dev/null | sort -u)"

# Build the unique DAG-critical list (only files that exist in the bundle).
DAG_SET="$(printf '%s\n%s\n' "$EXPLICIT_FLOOR" "$DERIVED" | tr ' ' '\n' | sed '/^$/d' | sort -u)"

drift=0; checked=0; missing=0
echo "smartx-bundle-parity: canonical=$CANON_DIR"
echo "                      bundle=$BUNDLE_DIR"
echo "--- DAG-critical scripts (must be byte-identical) ---"
for b in $DAG_SET; do
  [ -f "$BUNDLE_DIR/$b" ] || continue          # not a bundle script (e.g. a stdlib mention)
  if [ ! -f "$CANON_DIR/$b" ]; then
    echo "  MISSING-CANONICAL: $b (in bundle, absent in data/smartx/scripts) -- investigate"
    missing=$((missing+1)); continue
  fi
  checked=$((checked+1))
  if diff -q "$CANON_DIR/$b" "$BUNDLE_DIR/$b" >/dev/null 2>&1; then
    echo "  IN-SYNC: $b"
  else
    echo "  *** DRIFT ***: $b  (canonical != bundle -- a fix edited in data/smartx did NOT reach the deployed bundle; re-sync + rebuild the image)"
    drift=$((drift+1))
  fi
done

echo "--- summary: $checked checked, $drift drift, $missing missing-canonical ---"
if [ "$drift" -gt 0 ] || [ "$missing" -gt 0 ]; then
  echo "FAIL: smartx daily-DAG bundle is OUT OF SYNC with canonical. Re-sync the"
  echo "      divergent file(s) into smartx-workspace/scripts/ + rebuild+push the"
  echo "      smartx-exporter Docker image (build-and-deploy.sh) before the next run."
  exit 1
fi
echo "PASS: all daily-DAG scripts are bundle==canonical."
exit 0
