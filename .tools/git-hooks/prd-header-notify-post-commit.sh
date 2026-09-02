#!/bin/sh
# prd-header-notify-post-commit.sh -- R3 of the canonical loop (step 4 -> 5), release condition 7.
# When a commit lands a docs/architecture/*_PRD.md whose PRD_HEADER is NEW or whose prd_version
# BUMPED, deliver its identity to 2.0.0_SA_COO through the broker and re-offer until READ-acked.
#   - post-commit surface: NON-BLOCKING by construction. The commit is made; this only NOTIFIES.
#     BACKGROUNDED so a slow broker never holds the committing seat's terminal.
#   - fires only when the commit touched a PRD path (the python does the filtering); an unrelated
#     commit costs one `git diff-tree`.
#   - it is a NOTIFIER: never cuts a TO, never starts a decomp (CVO~A @0d272d257c R3 boundary).
#   - identity: codex-send.py refuses unless OPAL_AGENT_SERIAL names a LIVE seat; a hook inherits the
#     committing seat's env, so the notification is FROM the seat that landed the PRD.
# Andrew-direct 2026-09-02 memo: "COO has a monitor ... once it's committed, it's sent to COO
# immediately". Loop-internal notifier only; the moratorium width is recorded in the design.
_ws="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
[ -n "$_ws" ] || exit 0
_touched="$(git -C "$_ws" diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null)"
case "$_touched" in
  *docs/architecture/*_PRD.md*)
    ( cd "$_ws" && python "$_ws/.tools/prd-header-notify.py" post-commit >> "$_ws/org/mcp/.prd-notify/hook.log" 2>&1 ) &
    ;;
  *)
    # No PRD in this commit -- still let outstanding notifications RE-OFFER (commit-driven in v1).
    ( cd "$_ws" && python "$_ws/.tools/prd-header-notify.py" reoffer >> "$_ws/org/mcp/.prd-notify/hook.log" 2>&1 ) &
    ;;
esac
exit 0
