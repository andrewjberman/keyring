#!/usr/bin/env bash
# presence-stamp.sh -- the UserPromptSubmit presence stamp (report 2 call 5; Andrew-direct 2026-09-24 ~15:3xZ,
# org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_153xZ_REPORT2_ALL_SEVEN_RECS_APPROVED.md item 5).
#
# Writes ONE epoch-seconds timestamp to <main-checkout>/org/mcp/presence/<device>.last each time a prompt is submitted in any
# session on this device. A live /drive-mode FAST lease extends while that stamp is under 30 minutes old. It is a
# timestamp write only: no monitor, no alert, no network.
#
# CONTRACT (the lease reader in .tools/drive-mode.py reads exactly this):
#   path     the MAIN checkout's org/mcp/presence/<device>.last (a linked worktree stamps the main checkout, so a
#            device has one stamp); gitignored, device-local
#   device   `.tools/agentbus-sqs.sh device` (laptop | sitez), the fabric's one device resolver
#   content  one line, epoch seconds (`date -u +%s`). NEVER an ISO date: the reader strips non-digits and parses
#            what is left as epoch, so 2026-09-24T15:46:19Z would read as a far-future stamp and hold a lease open
#   absent   an unresolved device writes nothing; the lease then reads no presence and runs its stated length
#
# HARNESS CONTRACT: prints NOTHING on stdout (a UserPromptSubmit hook's stdout is injected into the prompt) and
# exits 0 on every path (a blocking exit would stop the prompt). stderr is left visible on purpose.
root="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
common="$(git -C "$root" rev-parse --path-format=absolute --git-common-dir 2>/dev/null)"
[ -n "$common" ] && root="$(dirname "$common")"
dev="$(bash "$root/.tools/agentbus-sqs.sh" device | sed -n 's/^device: //p')"
case "$dev" in
  laptop|sitez)
    mkdir -p "$root/org/mcp/presence" && date -u +%s > "$root/org/mcp/presence/$dev.last" ;;
esac
exit 0
