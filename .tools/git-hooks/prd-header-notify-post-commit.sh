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
_log="$_ws/org/mcp/.prd-notify/hook.log"
mkdir -p "$_ws/org/mcp/.prd-notify"
# ONE LINE PER FIRING, before any work: a reoffer with nothing outstanding prints nothing, and an
# empty log then cannot tell "fired, nothing to do" from "never fired" (measured on the first
# commit after install: 0 bytes, and the question could not be answered from the log).
# post-commit mode when the commit touched a PRD (R3, step 4 -> 5) OR a remediation doc on either root
# (R7, step 10 -> loop_target owner); the python decides what, if anything, is notified.
case "$_touched" in
  # L4-R (2026-09-11, 1.0.0_SA_CTO): a SIGN-OFF commit (prd/signoff/<serial>.json) must run post-commit too, or the
  # release branch never fires -- measured on 3.0.0_SA_CVO 0a317a6a73: both projects fully signed, COO delivery never sent.
  *docs/architecture/*_PRD.md*|*/prd/*_PRD.md*|*/prd/signoff/*|*/REMEDIATION_v*|*surprise-channel/remediations/*) _mode=post-commit ;;
  *) _mode=reoffer ;;   # nothing notifiable in this commit -- outstanding rows still RE-OFFER (commit-driven in v1)
esac
printf '%s fired HEAD=%s mode=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$(git -C "$_ws" rev-parse --short=10 HEAD 2>/dev/null)" "$_mode" >> "$_log"
( cd "$_ws" && python "$_ws/.tools/prd-header-notify.py" "$_mode" >> "$_log" 2>&1 ) &
exit 0
