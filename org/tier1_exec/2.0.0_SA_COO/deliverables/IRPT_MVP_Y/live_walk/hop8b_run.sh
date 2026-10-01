#!/usr/bin/env bash
# Second hop-8 window, on the st8 resident (the settings-row reader's repair): the hop-8 runner with this window's
# folder, root, evidence base and ledger. Same legs and refusals: --plan | --leg-p | --leg-s | --leg-j.
# Packet: ../HOP8B/WINDOW_PACKET_HOP8B_PROBE_SIGNIN_JOB_20261001.md.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
export HOP8_OUT="$HERE/../HOP8B"
export HOP8_ROOT="/opt/irpt-resident/9ac9b56d3c-st8"
export HOP8_BASE="H8B_overview_cottonwood"
export HOP8_AUTHORITY="second hop-8 window leg J; CTO batches 76 and 83; Andrew-direct 2026-09-27 124xZ; ledger irpt-hop8b-probe-signin-job-20261001"
exec bash "$HERE/hop8_run.sh" "$@"
