#!/usr/bin/env bash
# =============================================================================
# test-pre-push-safe-deploy.sh -- proof for NFRA_CTLPLN FWD-5 (contract C-TRUNK-DEPLOY):
# the pre-push deploy gate runs safe-deploy.sh ONLY when the pushed REMOTE ref is
# refs/heads/CLOUD; every other ref prints one SKIP line and deploys nothing.
# =============================================================================
# Author: 2.0.0_SA_COO~C.
#
# TEST DOUBLE, DECLARED. The fixture is a throwaway repo holding a copy of the hook and a stub
# `.tools/safe-deploy.sh` that only records its argv (and exits with STUB_RC). No real push is
# made and nothing deploys. It tests the HOOK's ref routing; it says nothing about safe-deploy.sh.
# The fixture has no halt-gate-check.sh, so the HALTGT checkpoint is skipped here by the hook's
# own `[ -f ]` guard; that block is not edited by FWD-5.
#
# NEGATIVE CONTROL. The same non-trunk case is run against the hook at the workspace's
# origin/CLOUD (pre-FWD-5 bytes). It must CALL the stub; if it does not, the fixture cannot
# tell the two hooks apart and every PASS below is void.
#
# RUN:  bash .tools/git-hooks/test-pre-push-safe-deploy.sh
# =============================================================================
set -u

WS="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$WS" ] || { echo "FAIL: not inside a git repo"; exit 2; }
HOOK="$WS/.tools/git-hooks/pre-push-safe-deploy.sh"
[ -f "$HOOK" ] || { echo "FAIL: hook not found at $HOOK"; exit 2; }

TMP="${TMPDIR:-/tmp}/prepush_fwd5_$$"
FX="$TMP/fixture"
rm -rf "$TMP"; mkdir -p "$FX/.tools/git-hooks" "$FX/data/x/scripts/gold"
cleanup() { cd /; rm -rf "$TMP" 2>/dev/null || :; }
trap cleanup EXIT INT TERM

PASS=0; FAIL=0
ZERO=0000000000000000000000000000000000000000

cd "$FX" || exit 2
git init -q .
git config user.email "fixture@opal.agent"
git config user.name "2.0.0_SA_COO~C"
git config core.autocrlf false

cp "$HOOK" .tools/git-hooks/pre-push-safe-deploy.sh
printf '#!/usr/bin/env bash\necho "$*" >> "%s/calls.log"\nexit "${STUB_RC:-0}"\n' "$TMP" > .tools/safe-deploy.sh

echo "a = 1" > data/x/scripts/gold/a.py
git add -A && git commit -q -m base
BASE="$(git rev-parse HEAD)"
echo "a = 2" > data/x/scripts/gold/a.py
git add -A && git commit -q -m change
TIP="$(git rev-parse HEAD)"

# run_case <name> <hook> <expected_calls> <expected_rc> <stdin> [stderr_must_contain]
run_case() {
    name="$1"; hook="$2"; want_calls="$3"; want_rc="$4"; input="$5"; want_err="${6:-}"
    rm -f "$TMP/calls.log"
    printf '%s\n' "$input" | bash "$hook" origin "https://example.invalid/repo.git" 2> "$TMP/err.txt"
    rc=$?
    calls=0; [ -f "$TMP/calls.log" ] && calls="$(wc -l < "$TMP/calls.log" | tr -d ' ')"
    ok=1
    [ "$calls" = "$want_calls" ] || ok=0
    [ "$rc" = "$want_rc" ] || ok=0
    if [ -n "$want_err" ] && ! grep -qF "$want_err" "$TMP/err.txt"; then ok=0; fi
    if [ "$ok" = 1 ]; then
        PASS=$((PASS+1)); echo "PASS: $name (calls=$calls rc=$rc)"
    else
        FAIL=$((FAIL+1)); echo "FAIL: $name (calls=$calls want $want_calls; rc=$rc want $want_rc)"
        sed 's/^/      stderr: /' "$TMP/err.txt"
    fi
}

H=.tools/git-hooks/pre-push-safe-deploy.sh

run_case "non-trunk branch push deploys nothing" "$H" 0 0 \
    "refs/heads/coo-c-ctlpln-r1 $TIP refs/heads/coo-c-ctlpln-r1 $BASE" \
    "SKIP: no deploy ran for refs/heads/coo-c-ctlpln-r1"
run_case "new non-trunk branch (zero remote sha) deploys nothing" "$H" 0 0 \
    "refs/heads/wk $TIP refs/heads/wk $ZERO" "SKIP: no deploy ran for refs/heads/wk"
run_case "trunk push runs the gate on the range" "$H" 1 0 \
    "refs/heads/CLOUD $TIP refs/heads/CLOUD $BASE"
grep -qF -- "--commit-range $BASE..$TIP" "$TMP/calls.log" 2>/dev/null \
    && { PASS=$((PASS+1)); echo "PASS: trunk push passes --commit-range BASE..TIP"; } \
    || { FAIL=$((FAIL+1)); echo "FAIL: trunk push range not passed: $(cat "$TMP/calls.log" 2>/dev/null)"; }
run_case "keyed on REMOTE ref: work:CLOUD deploys" "$H" 1 0 \
    "refs/heads/work $TIP refs/heads/CLOUD $BASE"
run_case "keyed on REMOTE ref: CLOUD:work deploys nothing" "$H" 0 0 \
    "refs/heads/CLOUD $TIP refs/heads/work $BASE" "SKIP: no deploy ran for refs/heads/work"
run_case "a similar name is not the trunk (CLOUD-x)" "$H" 0 0 \
    "refs/heads/CLOUD-x $TIP refs/heads/CLOUD-x $BASE"
run_case "mixed push: only the trunk line runs the gate" "$H" 1 0 \
    "refs/heads/wk $TIP refs/heads/wk $BASE
refs/heads/CLOUD $TIP refs/heads/CLOUD $BASE"
STUB_RC=1 run_case "trunk gate refusal still blocks the push" "$H" 1 1 \
    "refs/heads/CLOUD $TIP refs/heads/CLOUD $BASE"
run_case "tag push deploys nothing" "$H" 0 0 "refs/tags/v1 $TIP refs/tags/v1 $ZERO"
run_case "trunk delete deploys nothing" "$H" 0 0 "(delete) $ZERO refs/heads/CLOUD $TIP"

# --- real git push to a local bare remote: git itself writes the pre-push stdin ---
git init -q --bare "$TMP/remote.git"
git remote add origin "$TMP/remote.git"
printf '#!/usr/bin/env bash\nexec bash "$(git rev-parse --show-toplevel)/.tools/git-hooks/pre-push-safe-deploy.sh" "$@"\n' > .git/hooks/pre-push
chmod +x .git/hooks/pre-push
git branch -q -f CLOUD "$BASE"
git push -q origin CLOUD >/dev/null 2>&1   # first publish of the trunk (zero remote sha)
# real_push <name> <expected_calls> <refspec> <stderr_must_contain>
real_push() {
    rm -f "$TMP/calls.log"
    git push origin "$3" > /dev/null 2> "$TMP/err.txt"; rc=$?
    calls=0; [ -f "$TMP/calls.log" ] && calls="$(wc -l < "$TMP/calls.log" | tr -d ' ')"
    if [ "$calls" = "$2" ] && [ "$rc" = 0 ] && grep -qF "$4" "$TMP/err.txt"; then
        PASS=$((PASS+1)); echo "PASS: REAL PUSH $1 (calls=$calls rc=$rc)"
    else
        FAIL=$((FAIL+1)); echo "FAIL: REAL PUSH $1 (calls=$calls want $2; rc=$rc)"; sed 's/^/      stderr: /' "$TMP/err.txt"
    fi
}
git branch -q -f wk "$TIP"
real_push "of a work branch deploys nothing" 0 wk "SKIP: no deploy ran for refs/heads/wk"
git branch -q -f CLOUD "$TIP"
real_push "of CLOUD runs the gate once" 1 CLOUD "To "

# --- negative control: the pre-FWD-5 hook must deploy on the non-trunk push ---
# MSYS_NO_PATHCONV: Git Bash mangles a slashed <ref>:<path> argument (CLAUDE.md, Git section).
if MSYS_NO_PATHCONV=1 git -C "$WS" cat-file -e origin/CLOUD:.tools/git-hooks/pre-push-safe-deploy.sh 2>/dev/null; then
    MSYS_NO_PATHCONV=1 git -C "$WS" show origin/CLOUD:.tools/git-hooks/pre-push-safe-deploy.sh > "$TMP/hook_orig.sh"
    # FWD-5 is detected by its refusal text, which every FWD-5 version prints. Per-box B2 (84bbe98f80) rewrote the
    # `!= "refs/heads/CLOUD"` test as a case arm, so the old literal no longer marks it (4.0.0_SA_CRO~A, 2026-10-08).
    if grep -qF 'the deploy gate runs only on a push to refs/heads/CLOUD' "$TMP/hook_orig.sh"; then
        echo "SKIP: negative control -- origin/CLOUD already carries FWD-5; no pre-FWD-5 bytes to contrast"
    else
        cp "$TMP/hook_orig.sh" .tools/git-hooks/hook_orig.sh
        run_case "CONTROL: pre-FWD-5 hook deploys on a non-trunk push" .tools/git-hooks/hook_orig.sh 1 0 \
            "refs/heads/coo-c-ctlpln-r1 $TIP refs/heads/coo-c-ctlpln-r1 $BASE"
    fi
else
    FAIL=$((FAIL+1)); echo "FAIL: negative control -- could not read origin/CLOUD:.tools/git-hooks/pre-push-safe-deploy.sh"
fi

echo "RESULT: $PASS passed, $FAIL failed (of $((PASS+FAIL)))"
[ "$FAIL" = 0 ]
