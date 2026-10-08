#!/usr/bin/env bash
# monitor-bound-warn.sh -- PreToolUse ADVISORY hook for the Claude Code `Monitor` tool.
#
# THE PROBLEM: the harness kills every Monitor at 1800 s, but the kill reaches only the
# wrapper shell, never its children. An unbounded child (a `while true` loop, `tail -f`,
# `typeperf` with no sample count) survives the kill and leaks. The rule (watcher skill,
# Traps): a hand-written Monitor command runs as `timeout 1770 bash -c '<cmd>'` or carries
# its own bound.
#
# WHAT IT DOES: classifies `.tool_input.command` and, when it carries an unbounded marker
# and no bound, adds ONE warning line (systemMessage + additionalContext). It NEVER blocks:
# no permissionDecision is ever emitted; the Monitor always runs.
#
#   BOUNDED (silent): a leading `timeout N` with N <= 1770 (after an optional `cd ...;` or
#     `cd ... &&` prefix); a SECONDS deadline (`END=$((SECONDS+N))` ... `$SECONDS`, N <= 1770);
#     `inbox-watch(.sh) <serial> stream`; `agentbus-sqs.sh watch`; `typeperf ... -sc N`
#     (bounds the typeperf only).
#   UNBOUNDED (warn): `while true`, `while :`, `tail -f/-F/--follow`, `typeperf` without
#     `-sc`, `teams-watch.py`, `inotifywait -m`, or a leading `timeout N` with N > 1770 --
#     and no global bound above.
#   Anything else (a one-shot command): silent.
#
# COST: one jq process; the classification is pure bash (no grep/sed/dirname spawns).
# FAIL-OPEN: jq missing, empty stdin, unparsable JSON, or no `.tool_input.command` (a Monitor
# may use `ws` instead) -> exit 0 with no output.

# Hook dir without a dirname spawn. $0 may carry backslashes ($CLAUDE_PROJECT_DIR on Windows
# is C:\...), so strip at the last / OR \.
HOOK_DIR="${0%[\\/]*}"
[ "$HOOK_DIR" = "$0" ] && HOOK_DIR="."
if [ -x "$HOOK_DIR/../jq.exe" ]; then
    JQ="$HOOK_DIR/../jq.exe"
elif command -v jq >/dev/null 2>&1; then
    JQ="jq"
else
    exit 0
fi

# jq reads stdin directly (no cat). Empty stdin -> no output; bad JSON -> non-zero -> pass.
CMD=$("$JQ" -r 'select((.tool_name // "Monitor") == "Monitor") | .tool_input.command // empty | strings' 2>/dev/null) || exit 0
[ -z "$CMD" ] && exit 0

# --- seconds helper: N[smhd] -> seconds in SECS (pure bash) ---------------------------------
to_secs() {
    local n="$1" u="$2"
    n=$((10#$n))
    case "$u" in
        m) SECS=$((n * 60)) ;;
        h) SECS=$((n * 3600)) ;;
        d) SECS=$((n * 86400)) ;;
        *) SECS=$n ;;
    esac
}

# --- strip leading `cd ...;` / `cd ... &&` prefixes (up to 3) -------------------------------
REST="$CMD"
re_cd='^[[:space:]]*cd[[:space:]]+[^;&]*(;|&&)(.*)$'
for _ in 1 2 3; do
    if [[ $REST =~ $re_cd ]]; then REST="${BASH_REMATCH[2]}"; else break; fi
done

# --- global bounds -----------------------------------------------------------------------
BOUNDED=0
HEAD_TOO_LONG=0
# leading timeout, with optional flags (-k 5, -s KILL, --foreground, --signal=TERM ...)
re_to='^[[:space:]]*timeout[[:space:]]+((-[ks][[:space:]]+[^[:space:]]+|--?[a-zA-Z-]+(=[^[:space:]]+)?)[[:space:]]+)*([0-9]+)([smhd]?)([[:space:]]|$)'
if [[ $REST =~ $re_to ]]; then
    to_secs "${BASH_REMATCH[4]}" "${BASH_REMATCH[5]}"
    if [ "$SECS" -le 1770 ]; then BOUNDED=1; else HEAD_TOO_LONG=1; fi
fi
# SECONDS deadline loop (the /git-pull pattern)
re_sec='SECONDS[[:space:]]*\+[[:space:]]*([0-9]+)'
if [ "$BOUNDED" = 0 ] && [[ $CMD =~ $re_sec ]] && [[ $CMD == *'$SECONDS'* ]]; then
    to_secs "${BASH_REMATCH[1]}" ""
    [ "$SECS" -le 1770 ] && BOUNDED=1
fi
re_inbox='inbox-watch(\.sh)?[[:space:]]+[^[:space:]]+[[:space:]]+stream([[:space:]]|$)'
re_abus='agentbus-sqs\.sh[[:space:]]+watch([[:space:]]|$)'
if [ "$BOUNDED" = 0 ] && { [[ $CMD =~ $re_inbox ]] || [[ $CMD =~ $re_abus ]]; }; then
    BOUNDED=1
fi
[ "$BOUNDED" = 1 ] && exit 0

# --- unbounded markers -------------------------------------------------------------------
UNB=$HEAD_TOO_LONG
re_while='(^|[^[:alnum:]_])while[[:space:]]+(true|:)([[:space:];]|$)'
re_tail='(^|[^[:alnum:]_-])tail[^|;&]*[[:space:]](-[a-zA-Z]*[fF][a-zA-Z]*|--follow(=[^[:space:]]*)?)([[:space:]]|$)'
re_tp='(^|[^[:alnum:]_-])typeperf([.]exe)?([[:space:]]|$)'
re_tp_sc='typeperf([.]exe)?[[:space:]][^|;&]*[[:space:]][-/][sS][cC][[:space:]]+[0-9]'
re_inw='(^|[^[:alnum:]_-])inotifywait[^|;&]*[[:space:]](-[a-zA-Z]*m[a-zA-Z]*|--monitor)([[:space:]]|$)'
if [ "$UNB" = 0 ]; then
    if [[ $CMD =~ $re_while ]] || [[ $CMD =~ $re_tail ]] || [[ $CMD =~ $re_inw ]] \
       || [[ $CMD == *teams-watch.py* ]]; then
        UNB=1
    elif [[ $CMD =~ $re_tp ]] && ! [[ $CMD =~ $re_tp_sc ]]; then
        UNB=1
    fi
fi
[ "$UNB" = 0 ] && exit 0

M="WARN: Monitor command has no exit bound -- the harness kill at 1800 s stops only the wrapper, so its children leak. Wrap it: timeout 1770 bash -c '<cmd>' (watcher skill Traps)."
printf '{"systemMessage":"%s","hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":"%s"}}\n' "$M" "$M"
exit 0
