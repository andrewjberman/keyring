#!/usr/bin/env bash
# post-send-commitment.sh -- Claude Code PostToolUse hook for active-commitment
# detection.
#
# CANONICAL SOURCE: org/mcp/hooks/post-send-commitment.sh (version-controlled)
# INSTALL TARGET:   .tools/hooks/post-send-commitment.sh (gitignored, copied via install)
# INSTALL SCRIPT:   .tools/hooks/install-telemetry-hook.sh (idempotent + drift check)
# (Promoted to a tracked canonical 2026-06-23 -- it was previously a gitignored
#  runtime-only file with no version-controlled source; wired into settings.json
#  PostToolUse on every tool, so it must be reviewable + reinstallable. CTO.)
#
# Ported from corporeal mcp_runner/hooks/post_send_message_commitment_detector.sh
# (2026-05-20). Adapted to the ajb_workspace: serial resolved from
# .comp-graph/.agent_context (or OPAL_AGENT_SERIAL); ledger written via
# org/mcp/append-commitment.sh which resolves the tilde-lane-aware inbox dir.
#
# When the tool was a send_message, regex-scans the message body for
# commitment-language patterns. If detected (and not negated), appends a line
# to the sender's .active-commitments ledger so the supervisor /loop body
# Step 0.5 can deterministically execute the committed work on the next tick.
#
# This is the DETERMINISTIC write-source for the ledger -- an external observer
# of agent-emitted send_message calls. Agents do NOT need to remember to call
# append-commitment.sh; the hook fires automatically. Sibling pattern to
# inbox-watch.sh writing .unread-deliveries.
#
# Failures are silent by design -- a hook error must never disrupt the agent.

set -u  # do NOT set -e -- silent-fail by design

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Resolve agent serial (same precedence as post-tool-telemetry.sh).
AGENT="${OPAL_AGENT_SERIAL:-}"
if [ -z "$AGENT" ] && [ -f "$REPO_ROOT/.comp-graph/.agent_context" ]; then
    AGENT=$(grep -m1 '^SERIAL=' "$REPO_ROOT/.comp-graph/.agent_context" 2>/dev/null | cut -d= -f2- | tr -d '\r' || echo "")
fi
if [ -z "$AGENT" ] || [ "$AGENT" = "_unknown" ]; then
    exit 0  # no attributed identity -- nothing to ledger
fi

# Read hook context from stdin. Short-circuit on non-send-message.
HOOK_INPUT="$(cat)"
TOOL=$(printf '%s' "$HOOK_INPUT" | jq -r '.tool_name // ""' 2>/dev/null || echo "")
case "$TOOL" in
    mcp__opal-agent-comms__send_message) : ;;  # proceed
    *) exit 0 ;;
esac

# --- FREEFORM standdown (shared /freeform marker with the comp-rail comp-tool-hud.sh) -----------
# If this session has a LIVE (unexpired) freeform marker, commitment-ledgering is a friction TAX
# -- NOT a safety guard -- so stand down: a freestyling agent's sends are not auto-ledgered during
# the speed push. Mirrors comp-tool-hud.sh's freeform block (same marker, same expiry parse).
# Best-effort: any ambiguity just ledgers as normal (fail-open is correct -- non-critical).
_FF_SID=$(printf '%s' "$HOOK_INPUT" | jq -r '.session_id // ""' 2>/dev/null || echo "")
[ -z "$_FF_SID" ] && _FF_SID="${CLAUDE_CODE_SESSION_ID:-}"
if [ -n "$_FF_SID" ]; then
    _FF="$REPO_ROOT/org/mcp/sessions/${_FF_SID}.freeform"
    if [ -f "$_FF" ]; then
        _FF_EXP=$(tr -dc '0-9' < "$_FF" 2>/dev/null); _FF_NOW=$(date +%s 2>/dev/null | tr -dc '0-9')
        if [ -n "$_FF_EXP" ] && [ -n "$_FF_NOW" ] && [ "$_FF_NOW" -lt "$_FF_EXP" ] 2>/dev/null; then exit 0; fi
    fi
fi

BODY=$(printf '%s' "$HOOK_INPUT" | jq -r '.tool_input.body // ""' 2>/dev/null || echo "")
[ -z "$BODY" ] && exit 0
SUBJECT=$(printf '%s' "$HOOK_INPUT" | jq -r '.tool_input.subject // ""' 2>/dev/null || echo "")
TO_AGENT=$(printf '%s' "$HOOK_INPUT" | jq -r '.tool_input.to_agent // ""' 2>/dev/null || echo "")

# Commitment-language detection. Conservative: missing a commitment is preferred
# over false-firing on past-tense / hypothetical language. Case-insensitive
# fixed-string match (grep -F) -- portable and fast.
LOWER_BODY=$(printf '%s' "$BODY" | tr '[:upper:]' '[:lower:]')
MATCHED=0
for phrase in \
    "next turn" "next cycle" "next wake" "standing by on" "pending dispatch" \
    "drafting next" "queued for" "follow-up to" "follow on to" \
    "i'll draft" "i'll dispatch" "i'll execute" "i'll ship" "i'll route" \
    "i'll reply" "i'll surface" "i'll send" "i'll commit" \
    "i will draft" "i will dispatch" "i will execute" "i will ship" \
    "i will route" "i will reply" "i will surface" \
    "i need to draft" "i need to dispatch" "i plan to" \
    "awaiting your" "awaiting principal" "eta " ; do
    if printf '%s' "$LOWER_BODY" | grep -F -q "$phrase"; then
        MATCHED=1
        break
    fi
done
[ "$MATCHED" -eq 0 ] && exit 0

# Negation avoidance: skip if the body carries a prominent negation.
NEGATED=0
for neg in \
    "won't" "wont " "will not" "not going to" "no commit" \
    "nothing to dispatch" "nothing to ledger" "nothing to surface" \
    "no urgency" "no action required" ; do
    if printf '%s' "$LOWER_BODY" | grep -F -q "$neg"; then
        NEGATED=1
        break
    fi
done
[ "$NEGATED" -eq 1 ] && exit 0

# Build a concise commitment description: prefer subject, strip leading tag
# prefixes ("DISPATCH GO -- ", "ACK 224500Z -- "); fall back to a body slice.
if [ -n "$SUBJECT" ]; then
    DESC=$(printf '%s' "$SUBJECT" | sed -E 's/^[A-Z][A-Z 0-9_]*[—-][ ]*//; s/[|]/_/g')
else
    DESC=$(printf '%s' "$BODY" | head -c 200 | tr '\n' ' ' | sed 's/[|]/_/g')
fi
DESC=$(printf '%s' "$DESC" | head -c 250)
[ -n "$TO_AGENT" ] && DESC="[->$TO_AGENT] $DESC"

# Append via the canonical script (handles inbox resolution + ISO timestamp).
bash "$REPO_ROOT/org/mcp/append-commitment.sh" "$AGENT" "$DESC" >/dev/null 2>&1 || true

exit 0
