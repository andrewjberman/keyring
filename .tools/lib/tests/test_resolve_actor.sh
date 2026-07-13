#!/usr/bin/env bash
# Exercise resolve-actor.sh. Rule 22a: acceptance rests on the resolver FIRING, not on reading it.
#
# THE TWO ASSERTIONS THAT MATTER:
#   F1 (FALSE-WITNESS control) -- seed .comp-graph/.agent_context with a DIFFERENT serial and set
#      $OPAL_AGENT_SERIAL. The resolver MUST return the ENV serial. If it ever returns the file's,
#      the false witness is back: on a destructive HEAD move it would name the innocent.
#   M4 (MUTANT BAR / demotion test, named in CLAUDE.md) -- with NO env and NO session id, it MUST
#      print UNKNOWN. Never the shared serial. A resolver that "helpfully" falls back to the shared
#      file under demotion has silently reverted the fix while every other test stays green.

set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
. "$HERE/../resolve-actor.sh"
ROOT="$(cd "$HERE/../../.." && pwd)"
PASS=0; FAIL=0

chk() { # name expected actual
    if [ "$2" = "$3" ]; then PASS=$((PASS+1)); printf '  PASS  %-52s -> %s\n' "$1" "$3"
    else FAIL=$((FAIL+1)); printf '  FAIL  %-52s -> %s (want %s)\n' "$1" "$3" "$2"; fi
}

# The shared file is REAL and currently names whoever ran Step E last (me, this session).
SHARED="$(grep -m1 '^SERIAL=' "$ROOT/.comp-graph/.agent_context" 2>/dev/null | sed 's/^SERIAL=//' | tr -d '\r')"
echo "resolve-actor -- EXERCISED"
echo "  (the shared .comp-graph/.agent_context currently says: '${SHARED:-<empty>}' -- this is the"
echo "   value the OLD headmove-guard would have named, regardless of who was acting.)"
echo ""

echo "POSITIVE -- the sound sources:"
OPAL_AGENT_SERIAL="0.9.9_ZZ_TestAgent" CLAUDE_CODE_SESSION_ID="" \
  chk "env \$OPAL_AGENT_SERIAL wins" "0.9.9_ZZ_TestAgent" \
      "$(OPAL_AGENT_SERIAL=0.9.9_ZZ_TestAgent CLAUDE_CODE_SESSION_ID= bash -c ". '$HERE/../resolve-actor.sh'; resolve_actor")"

# per-session file (tier 2): no env, but a real session serial file
TMPSID="test-$$-sid"
mkdir -p "$ROOT/org/mcp/sessions" 2>/dev/null
echo "0.9.9_ZZ_SessionAgent" > "$ROOT/org/mcp/sessions/${TMPSID}.serial"
chk "per-session serial file (tier 2)" "0.9.9_ZZ_SessionAgent" \
    "$(env -u OPAL_AGENT_SERIAL CLAUDE_CODE_SESSION_ID="$TMPSID" CLAUDE_PROJECT_DIR="$ROOT" \
       bash -c ". '$HERE/../resolve-actor.sh'; resolve_actor")"
rm -f "$ROOT/org/mcp/sessions/${TMPSID}.serial"

echo ""
echo "*** F1 -- THE FALSE-WITNESS CONTROL (this is the whole point of the fix) ***"
echo "    .agent_context says '${SHARED:-<empty>}' but the ACTOR is 0.9.9_ZZ_RealActor."
echo "    The OLD headmove-guard named the FILE. The resolver must name the ACTOR."
chk "shared file IGNORED when env names the actor" "0.9.9_ZZ_RealActor" \
    "$(OPAL_AGENT_SERIAL=0.9.9_ZZ_RealActor CLAUDE_PROJECT_DIR="$ROOT" \
       bash -c ". '$HERE/../resolve-actor.sh'; resolve_actor")"

echo ""
echo "*** M4 -- THE MUTANT BAR / DEMOTION TEST (named in CLAUDE.md) ***"
echo "    No env, no session id. MUST be UNKNOWN -- never the shared serial."
echo "    A resolver that falls back to the shared file here has silently reverted the fix."
GOT="$(env -u OPAL_AGENT_SERIAL -u CLAUDE_CODE_SESSION_ID -u GIT_AUTHOR_NAME CLAUDE_PROJECT_DIR="$ROOT" \
       bash -c ". '$HERE/../resolve-actor.sh'; resolve_actor")"
chk "demoted -> UNKNOWN (not the shared serial)" "UNKNOWN" "$GOT"
if [ -n "$SHARED" ] && [ "$GOT" = "$SHARED" ]; then
    echo "  !!!! CRITICAL: the resolver returned the SHARED serial under demotion. FALSE WITNESS IS BACK."
fi

echo ""
echo "================================================================"
echo "PASS: $PASS   FAIL: $FAIL"
[ "$FAIL" -eq 0 ] && { echo "ALL CHECKS PASS -- names the actor, or says UNKNOWN. Never the innocent."; exit 0; }
exit 1
