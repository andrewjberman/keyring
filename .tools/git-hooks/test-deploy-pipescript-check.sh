#!/bin/sh
# =============================================================================
# test-deploy-pipescript-check.sh -- the MUTANT-KILL BAR for the R4-B trigger binding
# (deploy -> comp-pipescript deployed), NFRA_VELOCITY_ESTATE WS-E6 item 2.
# =============================================================================
# Author: 0.7.0_AE_CloudOps~E. TO: NFRA_VELOCITY_ESTATE.WS-E6.harness-r4-trigger-binding.
#
# WHY THIS ONE NEEDED A CONTROL MORE THAN R4-A DID. Measured 2026-07-31:
#   354 deploy-completion ledgers exist; only 6 name a gold/silver/bronze script.
#   ALL SIX PREDATE THE HOOK'S INSTALL (newest 2026-07-24; installed 2026-07-29T00:59:18Z).
#   All 9 post-install ledger commits named ZERO scripts.
# So R4-B'S FIRING PATH HAS NEVER RUN LIVE. Every post-install invocation correctly exited at
# the scripts-empty guard -- silent BY DESIGN, not by defect. But a hook that has only ever
# taken its silent path is indistinguishable from a hook that is broken, and no amount of
# waiting distinguishes them: the discriminating evidence does not arrive on its own. This
# file is the only thing that can tell those two states apart, so it is the evidence.
#
# NOT MANUFACTURED. A real ledger was NOT authored to force a live fire (COO 20260731T150921Z,
# explicit: a manufactured trigger is a manufactured verdict). The fixture below is an
# ISOLATED throwaway repo; the real estate is never committed to.
#
# TEST DOUBLE, DECLARED. The fixture supplies a stub `.tools/comp-pipescript` whose output the
# test controls. That is deliberate and its limit is exact: it drives THE HOOK through its
# branches. It tests the HOOK's parsing and finding-emission. IT SAYS NOTHING ABOUT
# comp-pipescript's own correctness, and no result here may be quoted as if it did.
#
# WHAT IS SCORED. The breadcrumb (fire vs silent) AND the FINDING FILE -- which for this hook
# is the authoritative product: the heavy block runs detached with `>/dev/null 2>&1 &`, so its
# own MATCH/STALE prints are discarded by construction. Never rc: the hook exits 0 on every
# path so it can never block a commit.
#
# RUN:  sh .tools/git-hooks/test-deploy-pipescript-check.sh
# =============================================================================
set -u

WS="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$WS" ] || { echo "FAIL: not inside a git repo"; exit 2; }
HOOK="$WS/.tools/git-hooks/deploy-pipescript-check-post-commit.sh"
[ -f "$HOOK" ] || { echo "FAIL: hook not found at $HOOK"; exit 2; }

TMP="${TMPDIR:-/tmp}/r4b_mutantbar_$$"
FX="$TMP/fixture"
LEDGER_DIR="org/critical_paths/change_management"
FIND_DIR="org/critical_paths/.open_findings"
rm -rf "$TMP"; mkdir -p "$FX/$LEDGER_DIR" "$FX/.tools"
cleanup() { cd /; rm -rf "$TMP" 2>/dev/null || :; }
trap cleanup EXIT INT TERM

PASS=0; FAIL=0

cd "$FX" || exit 2
git init -q .
git config user.email "fixture@opal.agent"
git config user.name "0.7.0_AE_CloudOps~E"

# --- the test double --------------------------------------------------------
# The hook runs `cd "$WS" && timeout 90 .tools/comp-pipescript deployed <script>`, so CWD is
# the fixture root and this stub simply replays whatever the current case staged.
printf '#!/bin/sh\ncat ./.stub_output 2>/dev/null\n' > .tools/comp-pipescript
chmod +x .tools/comp-pipescript
printf 'placeholder\n' > .stub_output
printf 'seed\n' > notes.txt
git add -A >/dev/null 2>&1
printf 'seed\n' > .msg; git commit -q -F .msg >/dev/null 2>&1

_commit() { git add -A >/dev/null 2>&1; printf '%s\n' "$1" > .msg; git commit -q -F .msg >/dev/null 2>&1; }
_findings_count() { ls "$FX/$FIND_DIR"/deploy_stale_*.json 2>/dev/null | grep -c . ; }

# Run a hook build; return "FIRE"/"SILENT" and wait (bounded) for the async finding write.
_probe() {
    _before="$(_findings_count)"
    _out="$(cd "$FX" && sh "$1" 2>&1 1>/dev/null)"
    if printf '%s' "$_out" | grep -q 'deploy-check'; then _fire="FIRE"; else _fire="SILENT"; fi
    # The heavy block is detached. Poll for a NEW finding rather than sleeping a fixed guess;
    # bounded so a hook that never writes cannot hang the suite. Rule 16: no flock/pgrep.
    # 3s ceiling: the stub returns instantly, so a real write lands in well under a second.
    # A no-finding case necessarily burns the whole window (absence is only provable by
    # waiting), so this bound is what keeps the suite's total runtime sane.
    _i=0
    while [ "$_i" -lt 12 ]; do
        [ "$(_findings_count)" -gt "$_before" ] && break
        sleep 0.25; _i=$((_i+1))
    done
    if [ "$(_findings_count)" -gt "$_before" ]; then _fnd="FINDING"; else _fnd="no-finding"; fi
    printf '%s/%s' "$_fire" "$_fnd"
}

_assert() {
    if [ "$2" = "$3" ]; then PASS=$((PASS+1)); printf '  ok    %-50s %s\n' "$1" "$3"
    else FAIL=$((FAIL+1)); printf '  FAIL  %-50s expected[%s] got[%s]\n' "$1" "$2" "$3"; fi
}

# Assert a mutation actually applied. A sed that silently fails to match produces a "mutant"
# byte-identical to the hook, and every verdict drawn from it is meaningless.
_mutated() {
    if cmp -s "$HOOK" "$1"; then
        FAIL=$((FAIL+1)); printf '  FAIL  %-50s MUTATION DID NOT APPLY (file identical to hook)\n' "$2"; return 1
    fi
    return 0
}

_ledger() { # filename, body
    printf '%s\n' "$2" > "$LEDGER_DIR/$1"
}

echo "=================================================================="
echo "R4-B MUTANT-KILL BAR  (deploy -> comp-pipescript deployed)"
echo "=================================================================="
echo ""
echo "-- GREEN: the binding discriminates the moment of work --"

# 1. POSITIVE CONTROL: a ledger naming a script, and the deployed-check reports STALE.
printf 'Summary: 0 MATCH, 1 STALE, 0 MISSING_ON_S3\n' > .stub_output
_ledger "20260731T1200Z_fixture-stale_deploy_completion.md" \
    "deploy completion. script: data/inf/scripts/gold/D_99_fixture.py"
_commit "ledger closed naming a STALE script"
_assert "1 POSITIVE CONTROL ledger+STALE -> finding" "FIRE/FINDING" "$(_probe "$HOOK")"

# 2. THE DOCUMENTED FALSE-FLAG TRAP. A CLEAN result still contains the words STALE and
#    MISSING_ON_S3 in its summary ("1 MATCH, 0 STALE, 0 MISSING_ON_S3"). A naive substring
#    grep flags EVERY script. The hook parses the COUNTS instead; this proves it.
printf 'Summary: 1 MATCH, 0 STALE, 0 MISSING_ON_S3\n' > .stub_output
_ledger "20260731T1300Z_fixture-clean_deploy_completion.md" \
    "deploy completion. script: data/inf/scripts/gold/D_98_fixture.py"
_commit "ledger closed, script is a clean MATCH"
_assert "2 clean MATCH -> fires but NO finding" "FIRE/no-finding" "$(_probe "$HOOK")"

# 3. A ledger that names NO script is a serve-only/infra deploy -> nothing to verify.
#    This is the path EVERY live post-install invocation has actually taken.
_ledger "20260731T1400Z_fixture-infra_deploy_completion.md" \
    "deploy completion. terraform only, no gold scripts touched."
_commit "ledger closed naming no scripts"
_assert "3 ledger naming no scripts stays SILENT" "SILENT/no-finding" "$(_probe "$HOOK")"

# 4. An ordinary commit must not fire.
printf 'edit\n' >> notes.txt
_commit "unrelated edit"
_assert "4 unrelated commit stays SILENT" "SILENT/no-finding" "$(_probe "$HOOK")"

# 5. MISSING_ON_S3 is the second failure mode and must also raise a finding.
printf 'Summary: 0 MATCH, 0 STALE, 1 MISSING_ON_S3\n' > .stub_output
_ledger "20260731T1500Z_fixture-missing_deploy_completion.md" \
    "deploy completion. script: data/inf/scripts/gold/D_97_fixture.py"
_commit "ledger closed, script MISSING on S3"
_assert "5 MISSING_ON_S3 -> finding" "FIRE/FINDING" "$(_probe "$HOOK")"

echo ""
echo "-- RED: each guard is proven able to fail (mutants on a COPY) --"

# MUTANT A: replace the COUNT parse with the naive substring grep the hook's own comment warns
# about. Case 2 (a clean MATCH) must now raise a FALSE finding. This is the sharpest mutant
# here: it reproduces the exact documented trap, and if it does not fire, assertion 2 is
# decorative.
sed 's/elif \[ "\$stale_n" -gt 0 \] || \[ "\$miss_n" -gt 0 \]; then bad=1; else bad=0; fi/elif echo "\$out" | grep -qE "STALE|MISSING_ON_S3"; then bad=1; else bad=0; fi/' \
    "$HOOK" > "$TMP/mutantA.sh"
if _mutated "$TMP/mutantA.sh" "M-A naive substring parse -> false FINDING"; then
    printf 'Summary: 1 MATCH, 0 STALE, 0 MISSING_ON_S3\n' > .stub_output
    _ledger "20260731T1600Z_fixture-cleanB_deploy_completion.md" \
        "deploy completion. script: data/inf/scripts/gold/D_96_fixture.py"
    _commit "clean MATCH (mutant A probe)"
    _mA="$(_probe "$TMP/mutantA.sh")"
    if [ "$_mA" = "FIRE/FINDING" ]; then
        PASS=$((PASS+1)); printf '  ok    %-50s went RED as required [%s]\n' "M-A naive substring parse -> false FINDING" "$_mA"
    else
        FAIL=$((FAIL+1)); printf '  FAIL  %-50s expected FIRE/FINDING got [%s]\n' "M-A naive substring parse -> false FINDING" "$_mA"
    fi
fi

# MUTANT B: remove the scripts-empty guard. A serve-only ledger must now fire. This is the
# guard that every live invocation to date has relied on, so it is the one most in need of
# proof: it is the ONLY reason R4-B has been silent, and silence was all we had.
grep -v '^\[ -n "\$scripts" \] || exit 0$' "$HOOK" > "$TMP/mutantB.sh"
if _mutated "$TMP/mutantB.sh" "M-B scripts-empty guard removed -> must FIRE"; then
    _ledger "20260731T1700Z_fixture-infraB_deploy_completion.md" \
        "deploy completion. terraform only, no gold scripts touched."
    _commit "serve-only ledger (mutant B probe)"
    _mB="$(_probe "$TMP/mutantB.sh")"
    case "$_mB" in
        FIRE/*) PASS=$((PASS+1)); printf '  ok    %-50s went RED as required [%s]\n' "M-B scripts-empty guard removed -> must FIRE" "$_mB" ;;
        *) FAIL=$((FAIL+1)); printf '  FAIL  %-50s stayed SILENT -- guard untested\n' "M-B scripts-empty guard removed -> must FIRE" ;;
    esac
fi

echo ""
echo "=================================================================="
printf 'RESULT: %d passed, %d failed\n' "$PASS" "$FAIL"
echo "Scored on printed OUTPUT above, not on this exit code."
echo "NOTE: exercises the HOOK against a comp-pipescript TEST DOUBLE."
echo "      Says nothing about comp-pipescript's own correctness."
echo "=================================================================="
[ "$FAIL" -eq 0 ] || exit 1
exit 0
