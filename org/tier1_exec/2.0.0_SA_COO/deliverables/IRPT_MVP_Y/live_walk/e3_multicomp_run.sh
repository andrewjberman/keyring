#!/usr/bin/env bash
# E3, the Multi-Comp arm, on the st9 resident: the hop-8 runner with this window's folder, root, evidence base, ledger
# and the two comparison keys. Same legs and refusals: --plan | --leg-p | --leg-s | --leg-j.
# Packet: ../E3_MULTICOMP/WINDOW_PACKET_E3_MULTICOMP_20261001.md.
#
# The keys are the two the maintained catalogue records as the Multi-Comp template's own live-proven comparisons
# (templates.json comparison_catalog: opal_short_term, opal_intermediate_term); the variant is live_chain.py's rule on
# their count (two or more: multicomp), never typed.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
export HOP8_OUT="$HERE/../E3_MULTICOMP"
export HOP8_ROOT="/opt/irpt-resident/481166a8f2-st9"
export HOP8_BASE="E3_multicomp_cottonwood"
export HOP8_AUTHORITY="E3 Multi-Comp arm leg J; CTO batch 88 item 4 and batch 61 item 8; Andrew-direct 2026-09-27 124xZ; ledger irpt-e3-multicomp-20261001"
export WALK_COMPARISON_KEYS="opal_short_term,opal_intermediate_term"
exec bash "$HERE/hop8_run.sh" "$@"
