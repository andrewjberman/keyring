#!/usr/bin/env bash
# resolve-actor.sh -- THE sound way to answer "which agent is doing this?" in a gate/audit.
# Source it:  . "$(dirname "$0")/lib/resolve-actor.sh"  ;  ACTOR="$(resolve_actor)"
#
# Built 2026-07-13 (1.0.0_SA_CTO) for RV-0047 F-001. One helper, because we currently have three
# different answers to this question across the estate and one of them is a FALSE WITNESS.
#
# ===========================================================================================
# THE DEFECT THIS EXISTS TO KILL (documented in CLAUDE.md/org-XXX and still live at build time):
#   headmove-guard.sh:57-59 resolves the actor for a DESTRUCTIVE HEAD MOVE by grepping ^SERIAL=
#   out of `.comp-graph/.agent_context` -- a SHARED, repo-root file that EVERY agent's startup
#   Step E TRUNCATES AND REWRITES. It therefore names whoever ran Step E most recently.
#
#   Exercised live 2026-07-10 (CVO): the guard named `1.0.0_SA_CTO` while `3.0.0_SA_CVO` was the
#   actor, and `$OPAL_AGENT_SERIAL` held the correct answer, unread. `GIT_AUTHOR_NAME` is UNSET in
#   an agent Bash-tool shell, so the guard has NO BRANCH that can ever name the true actor:
#   file present -> whoever last ran Step E; file absent -> UNKNOWN.
#
#   *** AN ABSENT FIELD IS A GAP. A CONFIDENT WRONG FIELD IS A FALSE WITNESS. ***
#   And this one is ANTI-CORRELATED: it names the most-recently-STARTED agent, who by construction
#   has the fewest local commits worth force-discarding. IT NAMES THE INNOCENT.
#
#   .comp-graph/.agent_context is NEVER an identity source. It answers "what TO", never "who am I".
# ===========================================================================================
#
# SOUND PRECEDENCE (both sources already exist in every agent shell):
#   1. $OPAL_AGENT_SERIAL                                  -- per-PROCESS (.tools/ajb.ps1:286)
#   2. org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial     -- per-SESSION, race-free (org/XXX.md 1b-A.1)
#   3. $GIT_AUTHOR_NAME                                    -- usually unset in an agent shell; last resort
#   4. UNKNOWN                                             -- and it SAYS so. Never a guess.
# Reference impl of the same precedence: org/modules/graph/comp_log_auto.py:62-77
#
# THE MUTANT BAR (M4, the demotion test -- tests/test_resolve_actor.sh):
#   with NO env and NO session-id, this MUST print UNKNOWN -- never the shared serial.
#   If that test ever goes green while reading .agent_context, the fix has been silently reverted.

resolve_actor() {
    # 1. per-process env -- the strongest source, and the one headmove-guard never read.
    if [ -n "${OPAL_AGENT_SERIAL:-}" ]; then
        printf '%s' "$OPAL_AGENT_SERIAL"
        return 0
    fi

    # 2. per-session serial file (survives compaction; unique per session; no cross-agent race).
    if [ -n "${CLAUDE_CODE_SESSION_ID:-}" ]; then
        _ra_root="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}"
        _ra_f="$_ra_root/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"
        if [ -f "$_ra_f" ]; then
            _ra_s="$(tr -d '\r\n' < "$_ra_f" 2>/dev/null)"
            if [ -n "$_ra_s" ]; then
                printf '%s' "$_ra_s"
                return 0
            fi
        fi
    fi

    # 3. git author identity (unset in agent Bash-tool shells; present for a human at a terminal).
    if [ -n "${GIT_AUTHOR_NAME:-}" ]; then
        printf '%s' "$GIT_AUTHOR_NAME"
        return 0
    fi

    # 4. Say you do not know. NEVER fall through to .comp-graph/.agent_context.
    printf 'UNKNOWN'
    return 0
}
