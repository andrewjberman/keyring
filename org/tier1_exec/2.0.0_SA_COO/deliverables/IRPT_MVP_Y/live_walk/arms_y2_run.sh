#!/usr/bin/env bash
# The two Y2 upload arms still unproved live (P_Y2_UPLOAD_ARMS_ACT_20260927.md), each ONE Cottonwood Overview job on the st13
# resident: leg TW (Target Weight CSV, reference notional 1000) then leg XL (the XLSX template). The CRO trace's "one job per
# remaining arm" (ANALYSIS_END_TO_END_GAP_BRIEF_20261001.md section 8); the session is live since 09:45:44Z (window C).
#
#   bash arms_y2_run.sh --plan     # each leg's solo gate and live_chain plan; no secret read, no login, no POST
#   bash arms_y2_run.sh --leg-tw   # ONE upload (Target Weight) and ONE Overview, to a terminal state
#   bash arms_y2_run.sh --leg-xl   # ONE upload (XLSX) and ONE Overview, to a terminal state
#
# Packet: ../ARMS_Y2/WINDOW_PACKET_ARMS_Y2_20261002.md. Each leg is hop7_run.sh unchanged with this window's folder, base,
# arm environment and ledger; a leg whose evidence exists refuses (hop7_run.sh's own rule). No retry.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
export HOP7_OUT="$HERE/../ARMS_Y2"
AUTH="CRO trace section 8 and CTO batch 61 item 8; Andrew-direct 2026-09-27 124xZ; ledger irpt-arms-y2-20261002"
case "${1:-}" in
  --plan)
    ( export HOP7_BASE=TW_overview_cottonwood HOP7_AUTHORITY="arms Y2 leg TW; $AUTH" \
        WALK_UPLOAD_FILE="$HERE/../aapl-vnq-target-weight.csv" WALK_REFERENCE_NOTIONAL=1000; bash "$HERE/hop7_run.sh" --plan ) || exit $?
    ( export HOP7_BASE=XL_overview_cottonwood HOP7_AUTHORITY="arms Y2 leg XL; $AUTH" \
        WALK_UPLOAD_FILE="$HERE/../aapl-vnq-12.03.xlsx" WALK_FILE_TYPE=xlsx; bash "$HERE/hop7_run.sh" --plan ) || exit $?
    ;;
  --leg-tw)
    export HOP7_BASE=TW_overview_cottonwood HOP7_AUTHORITY="arms Y2 leg TW; $AUTH" \
      WALK_UPLOAD_FILE="$HERE/../aapl-vnq-target-weight.csv" WALK_REFERENCE_NOTIONAL=1000
    exec bash "$HERE/hop7_run.sh"
    ;;
  --leg-xl)
    export HOP7_BASE=XL_overview_cottonwood HOP7_AUTHORITY="arms Y2 leg XL; $AUTH" \
      WALK_UPLOAD_FILE="$HERE/../aapl-vnq-12.03.xlsx" WALK_FILE_TYPE=xlsx
    exec bash "$HERE/hop7_run.sh"
    ;;
  *)
    echo "usage: arms_y2_run.sh --plan | --leg-tw | --leg-xl" >&2
    exit 2
    ;;
esac
