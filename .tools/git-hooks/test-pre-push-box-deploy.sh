#!/usr/bin/env bash
# =============================================================================
# test-pre-push-box-deploy.sh -- proof for per-box branch build item B2 (1.0.0_SA_CTO
# PER_BOX_BRANCH_BUILD_PLACEMENT_20261008.md): a deploy fires only on the AUTHORING box, for its own work.
#   push of box/<this box>   -> one gate run over merge-base(origin/CLOUD, tip)..tip
#   push of box/<other box>  -> SKIP
#   box push, box name unknown -> BLOCKED
#   CLOUD push that brings in a box branch (integration) -> SKIP
#   integration push that also carries commits from no box branch -> BLOCKED
#   CLOUD push that brings in no box branch (a box not yet switched) -> today's gate, REMOTE..LOCAL
# =============================================================================
# Author: 4.0.0_SA_CRO~A. Ledger gate added on 1.0.0_SA_CTO's ruling msg 107341 (a script deploys only when an OPEN
# change-management ledger names it; others are HELD and the push goes through). Companion to test-pre-push-safe-deploy.sh (FWD-5, 2.0.0_SA_COO~C), which still
# covers the trunk routing; this file covers only the per-box rules.
#
# TEST DOUBLE, DECLARED. A throwaway repo holds a copy of the hook and a stub `.tools/safe-deploy.sh` that records its
# argv. No real push is made, nothing deploys, and the fixture has no agentbus script, so the box name comes only from
# AGENTBUS_DEVICE as each case sets it.

WS="$(git rev-parse --show-toplevel 2>/dev/null)"
HOOK="${HOOK_UNDER_TEST:-$WS/.tools/git-hooks/pre-push-safe-deploy.sh}"   # HOOK_UNDER_TEST: negative control on other bytes
[ -f "$HOOK" ] || { echo "FAIL: hook not found at $HOOK"; exit 2; }

TMP="${TMPDIR:-/tmp}/prepush_box_$$"
FX="$TMP/fixture"
rm -rf "$TMP"; mkdir -p "$FX/.tools/git-hooks" "$FX/data/x/scripts/gold"
cleanup() { cd /; rm -rf "$TMP" 2>/dev/null || :; }
trap cleanup EXIT INT TERM
PASS=0; FAIL=0

cd "$FX" || exit 2
git init -q .
git config user.email "fixture@opal.agent"
git config user.name "4.0.0_SA_CRO~A"
git config core.autocrlf false
cp "$HOOK" .tools/git-hooks/pre-push-safe-deploy.sh
cp "$WS/.tools/deploy-ledger-names.py" .tools/deploy-ledger-names.py
# TEST DOUBLE for crossbox-deploy-check.py --list-deployable: prints STUB_DEPLOYABLE and records the range it was asked for
cat > .tools/stub-lister.py <<'EOF_L'
import os, sys
a = sys.argv
if '--commit-range' in a:
    open(os.environ['STUB_RANGE_FILE'], 'w').write(a[a.index('--commit-range') + 1])
if os.environ.get('STUB_LISTER_BROKEN') == '1':
    sys.exit(1)
paths = [x for x in os.environ.get('STUB_DEPLOYABLE', '').split() if x]
for x in paths:
    print('DEPLOYABLE ' + x)
print('DEPLOYABLE-COUNT n=%d' % len(paths))
EOF_L
mkdir -p org/critical_paths/.open_deploys
printf '{"slug": "led-1", "status": "OPEN", "legs": [{"target": "deploy data/x/scripts/gold/sitez.py"}]}' > org/critical_paths/.open_deploys/led-1.json
printf '{"slug": "gated-1", "status": "HELD-SOVEREIGN-GATED", "legs": [{"target": "deploy data/x/scripts/gold/other.py"}]}' > org/critical_paths/.open_deploys/gated-1.json
export PREPUSH_DEPLOY_LISTER="$FX/.tools/stub-lister.py" STUB_RANGE_FILE="$TMP/range.txt"
printf '#!/usr/bin/env bash\necho "$*" >> "%s/calls.log"\nexit "${STUB_RC:-0}"\n' "$TMP" > .tools/safe-deploy.sh
c() { echo "$2" > "data/x/scripts/gold/$1.py"; git add -A; git commit -q -m "$1"; git rev-parse HEAD; }

B="$(c base 1)"                                   # the trunk at the start
git checkout -q -b d1 "$B"; D1="$(c dell1 1)"     # dell1's own commit
git checkout -q -b s "$B";  S1="$(c sitez 1)"     # site Z's own commit, pushed earlier as box/sitez
git checkout -q -b t "$B"; git merge -q --no-ff --no-edit "$D1"; C1="$(git rev-parse HEAD)"   # integrator: dell1 into CLOUD
git checkout -q s; git merge -q --no-ff --no-edit "$C1"; M="$(git rev-parse HEAD)"           # site Z takes the trunk
S2="$(c sitez 2)"                                 # site Z's next own commit
git update-ref refs/remotes/origin/CLOUD "$C1"
git update-ref refs/remotes/origin/box/dell1 "$D1"
git update-ref refs/remotes/origin/box/sitez "$S2"
git checkout -q t; git merge -q --no-ff --no-edit "$S2"; I="$(git rev-parse HEAD)"           # integrator: sitez into CLOUD
L1="$(c laptop 1)"                                # an integrator-box commit that came through no box branch
git checkout -q -b u "$C1"; L2="$(c laptop 2)"    # a not-yet-switched box's own commit on the trunk

run_case() {   # name want_calls want_rc stdin [stderr_must_contain]
    rm -f "$TMP/calls.log"
    printf '%s\n' "$3" | bash .tools/git-hooks/pre-push-safe-deploy.sh origin "https://example.invalid/r.git" 2> "$TMP/err.txt"; rc=$?
    calls=0; [ -f "$TMP/calls.log" ] && calls="$(wc -l < "$TMP/calls.log" | tr -d ' ')"
    ok=1; [ "$calls" = "$1" ] || ok=0; [ "$rc" = "$2" ] || ok=0
    if [ -n "${4:-}" ] && ! grep -qF "$4" "$TMP/err.txt"; then ok=0; fi
    if [ "$ok" = 1 ]; then PASS=$((PASS+1)); echo "PASS: $NAME (calls=$calls rc=$rc)"
    else FAIL=$((FAIL+1)); echo "FAIL: $NAME (calls=$calls want $1; rc=$rc want $2)"; sed 's/^/      stderr: /' "$TMP/err.txt"; fi
}

A_LOG="$FX/org/safe-deploy-bypass-audit.log"
NAME="own box push: the LEDGERED script deploys, the unledgered one is HELD (CTO 107341)"
STUB_DEPLOYABLE="data/x/scripts/gold/sitez.py data/x/scripts/gold/dell9.py" AGENTBUS_DEVICE=sitez run_case 1 0 "refs/heads/s $S2 refs/heads/box/sitez $S1" "HELD-DEPLOY data/x/scripts/gold/dell9.py"
if grep -qF "data/x/scripts/gold/sitez.py" "$TMP/calls.log" && ! grep -qF "dell9.py" "$TMP/calls.log" && grep -qF "path=data/x/scripts/gold/dell9.py" "$A_LOG"; then
  PASS=$((PASS+1)); echo "PASS: only the ledgered path reached safe-deploy, and a HELD-DEPLOY row names the other"
else FAIL=$((FAIL+1)); echo "FAIL: deploy call: $(cat "$TMP/calls.log" 2>/dev/null); audit: $(cat "$A_LOG" 2>/dev/null)"; fi
if [ "$(cat "$TMP/range.txt" 2>/dev/null)" = "$C1..$S2" ]; then
  PASS=$((PASS+1)); echo "PASS: the deploy-scope list is read over merge-base(origin/CLOUD)..tip, so dell1's work taken from the trunk is excluded"
else FAIL=$((FAIL+1)); echo "FAIL: lister range $(cat "$TMP/range.txt" 2>/dev/null) (want $C1..$S2)"; fi
NAME="a script named only by a HELD-SOVEREIGN-GATED entry is held, not deployed"
STUB_DEPLOYABLE="data/x/scripts/gold/other.py" AGENTBUS_DEVICE=sitez run_case 0 0 "refs/heads/s $S2 refs/heads/box/sitez $S1" "HELD-DEPLOY data/x/scripts/gold/other.py"
NAME="an unreadable deploy-scope list deploys NOTHING, logs it, and the push goes through"
STUB_LISTER_BROKEN=1 AGENTBUS_DEVICE=sitez run_case 0 0 "refs/heads/s $S2 refs/heads/box/sitez $S1" "could not be read"
if grep -qF "reason=deploy-list-unreadable" "$A_LOG"; then PASS=$((PASS+1)); echo "PASS: the unreadable list wrote a HELD-DEPLOY row"; else FAIL=$((FAIL+1)); echo "FAIL: no unreadable row"; fi
NAME="no deploy-scope file in the box's diff deploys nothing"
STUB_DEPLOYABLE="" AGENTBUS_DEVICE=sitez run_case 0 0 "refs/heads/s $S2 refs/heads/box/sitez $S1" "nothing to deploy"
NAME="another box's branch deploys nothing"; AGENTBUS_DEVICE=dell1 run_case 0 0 "refs/heads/s $S2 refs/heads/box/sitez $S1" "is not this box (dell1)"
NAME="box push with the box name unknown is BLOCKED"; _saved_dev="${AGENTBUS_DEVICE-}"; unset AGENTBUS_DEVICE
run_case 0 1 "refs/heads/s $S2 refs/heads/box/sitez $S1" "BLOCKED"
if [ -n "$_saved_dev" ]; then export AGENTBUS_DEVICE="$_saved_dev"; fi
NAME="integration push of CLOUD deploys nothing"; AGENTBUS_DEVICE=laptop run_case 0 0 "refs/heads/t $I refs/heads/CLOUD $C1" "an integration push (box/sitez)"
NAME="integration push carrying a non-box commit is BLOCKED"; AGENTBUS_DEVICE=laptop run_case 0 1 "refs/heads/t $L1 refs/heads/CLOUD $C1" "came through no box branch"
NAME="not-yet-switched CLOUD push keeps today's gate"; AGENTBUS_DEVICE=dell2 run_case 1 0 "refs/heads/u $L2 refs/heads/CLOUD $C1"
grep -qF -- "--commit-range $C1..$L2" "$TMP/calls.log" 2>/dev/null \
  && { PASS=$((PASS+1)); echo "PASS: not-yet-switched CLOUD push range is REMOTE..LOCAL"; } \
  || { FAIL=$((FAIL+1)); echo "FAIL: not-yet-switched range: $(cat "$TMP/calls.log" 2>/dev/null)"; }
NAME="own box push: a safe-deploy refusal of a ledgered script still blocks the push"; STUB_DEPLOYABLE="data/x/scripts/gold/sitez.py" STUB_RC=1 AGENTBUS_DEVICE=sitez run_case 1 1 "refs/heads/s $S2 refs/heads/box/sitez $S1"

echo "RESULT: $PASS passed, $FAIL failed (of $((PASS+FAIL)))"
[ "$FAIL" = 0 ]
