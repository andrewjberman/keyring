#!/bin/sh
# =============================================================================
# test-closeout-comp-state.sh -- the MUTANT-KILL BAR for the R4-A trigger binding
# (closeout -> comp-state), NFRA_VELOCITY_ESTATE WS-E6 item 2.
# =============================================================================
# Author: 0.7.0_AE_CloudOps~E. TO: NFRA_VELOCITY_ESTATE.WS-E6.harness-r4-trigger-binding.
#
# WHY THIS EXISTS. The binding itself already shipped (NFRA_MSBEFF.R4-A, 2026-07-23) and is
# wired into .git/hooks/post-commit (LD-0343, 2026-07-29). It fires: 10 owned findings sat in
# org/critical_paths/.open_findings/ when this was written. What it had NEVER had is a control.
# A binding observed firing once, by an author watching for it, is a demonstration -- not a
# test. The question that decides whether the binding is real: if its detection silently
# stopped holding tomorrow, would anything print? Until this file existed the answer was no.
#
# WHAT IS SCORED. The stderr breadcrumb -- FIRE-vs-SILENT and the derived project CODES.
# Never rc: harness rc is corrupted on this box unless the /c mount is live, and the hook
# exits 0 on every path by construction anyway (it must never block a commit), so rc could
# not discriminate even on a healthy box.
#
# SCOPE BOUND, stated so a green run is not over-read: this exercises the DETECTION FAST PATH
# (the part that decides whether to fire and for which projects). The detached subshell that
# actually runs comp-state and writes the finding file is NOT exercised here -- the fixture
# has no .tools/comp-state. A PASS below says the trigger fires at the right moment for the
# right projects. It says NOTHING about the sweep's own correctness.
#
# THE MUTANTS ARE PERSISTED, NOT PERFORMED. Each mutant is applied here, at run time, to a
# COPY of the hook -- the real hook is never modified. An unpersisted mutant proves a guard
# could fail once, in a session, and then stops existing; these re-run forever.
#
# RUN:  sh .tools/git-hooks/test-closeout-comp-state.sh
# =============================================================================
set -u

WS="$(git rev-parse --show-toplevel 2>/dev/null)"
[ -n "$WS" ] || { echo "FAIL: not inside a git repo"; exit 2; }
HOOK="$WS/.tools/git-hooks/closeout-comp-state-post-commit.sh"
[ -f "$HOOK" ] || { echo "FAIL: hook not found at $HOOK"; exit 2; }

TMP="${TMPDIR:-/tmp}/r4a_mutantbar_$$"
FX="$TMP/fixture"
rm -rf "$TMP"; mkdir -p "$FX/org/projects"
cleanup() { cd /; rm -rf "$TMP" 2>/dev/null || :; }
trap cleanup EXIT INT TERM

PASS=0; FAIL=0

# --- fixture repo -----------------------------------------------------------
cd "$FX" || exit 2
git init -q .
git config user.email "fixture@opal.agent"
git config user.name "0.7.0_AE_CloudOps~E"
printf '# REGISTRY\n' > org/projects/REGISTRY.md
printf '{"status": "active"}\n' > org/projects/FIXTURE_ALPHA.json
printf 'unrelated\n' > notes.txt
git add -A >/dev/null 2>&1
printf 'seed\n' > .msg; git commit -q -F .msg >/dev/null 2>&1

_commit() { git add -A >/dev/null 2>&1; printf '%s\n' "$1" > .msg; git commit -q -F .msg >/dev/null 2>&1; }

# Run a hook (real or mutant) against the fixture HEAD; echo "FIRE <codes>" or "SILENT".
_probe() {
    _out="$(cd "$FX" && sh "$1" 2>&1 1>/dev/null)"
    if printf '%s' "$_out" | grep -q 'closeout detected'; then
        # The hook interpolates $codes NEWLINE-separated, so the breadcrumb spans lines
        # whenever there is more than one code. FLATTEN FIRST: a line-scoped sed here
        # reports an empty code list for exactly the multi-code case worth measuring.
        printf 'FIRE %s' "$(printf '%s' "$_out" | tr '\n' ' ' \
            | sed -n 's/.*closeout detected (\(.*\)) -- comp-state.*/\1/p' \
            | tr -s ' ' | sed 's/^ *//; s/ *$//')"
    else
        printf 'SILENT'
    fi
}

_assert() { # label, expected, actual
    if [ "$2" = "$3" ]; then
        PASS=$((PASS+1)); printf '  ok    %-52s %s\n' "$1" "$3"
    else
        FAIL=$((FAIL+1)); printf '  FAIL  %-52s expected[%s] got[%s]\n' "$1" "$2" "$3"
    fi
}

echo "=================================================================="
echo "R4-A MUTANT-KILL BAR  (closeout -> comp-state)"
echo "=================================================================="
echo ""
echo "-- GREEN: the binding discriminates the moment of work --"

# 1. POSITIVE CONTROL. If this is RED every mutant below is meaningless.
printf '{"status": "complete", "completed": "2026-07-31"}\n' > org/projects/FIXTURE_ALPHA.json
_commit "closeout: FIXTURE_ALPHA -> complete"
_assert "1 POSITIVE CONTROL a true closeout FIRES" "FIRE FIXTURE_ALPHA" "$(_probe "$HOOK")"

# 2. An ordinary commit must NOT fire. This is the "no latency tax on unrelated work"
#    half of the design; without it the hook would train agents to skim past it.
printf 'edit\n' >> notes.txt
_commit "unrelated edit"
_assert "2 an unrelated commit stays SILENT" "SILENT" "$(_probe "$HOOK")"

# 3. A project JSON that moved but did NOT close must NOT fire. Touching is not closing.
printf '{"status": "active", "phase": "moved along"}\n' > org/projects/FIXTURE_ALPHA.json
_commit "project touched, still active"
_assert "3 a touched-but-ACTIVE project stays SILENT" "SILENT" "$(_probe "$HOOK")"

echo ""
echo "-- RED: each guard is proven able to FAIL (mutants on a COPY) --"

# MUTANT A: delete the codes-empty guard (`[ -n "$codes" ] || exit 0`). A commit that clears
# the path filter but yields NO closing project must now fire with an EMPTY code list -- i.e.
# announce a closeout for nothing. This is the guard that stops a contentless finding.
grep -v '^\[ -n "\$codes" \] || exit 0$' "$HOOK" > "$TMP/mutantA.sh"
printf '{"status": "active", "phase": "mutant A probe"}\n' > org/projects/FIXTURE_ALPHA.json
_commit "project touched, still active (mutant A probe)"
_mA="$(_probe "$TMP/mutantA.sh")"
if [ "$_mA" = "SILENT" ]; then
    FAIL=$((FAIL+1)); printf '  FAIL  %-52s mutant stayed SILENT -- guard untested\n' "M-A codes-empty guard removed -> must FIRE"
else
    PASS=$((PASS+1)); printf '  ok    %-52s went RED as required [%s]\n' "M-A codes-empty guard removed -> must FIRE" "$_mA"
fi

# MUTANT C: delete the PATH filter (line 31) and re-run an unrelated commit. It must stay
# SILENT. This is a NEGATIVE mutant and it is deliberate: it establishes that line 31 is a
# FAST PATH, not the correctness guard -- the codes-derivation below it is already sufficient
# to reject an unrelated commit. Measured here rather than assumed, because a reader who
# mistakes the fast path for the safety will "harden" the wrong line and leave M-A's real
# guard untouched. Removing a performance guard must not change a verdict; if this ever goes
# FIRE, the two guards have stopped being independent and the hook needs re-reading.
grep -v "^echo \"\$changed\" | grep -qE '\^org/projects/" "$HOOK" > "$TMP/mutantC.sh"
printf 'edit again\n' >> notes.txt
_commit "unrelated edit (mutant C probe)"
_mC="$(_probe "$TMP/mutantC.sh")"
_assert "M-C path guard removed -> still SILENT (fast path)" "SILENT" "$_mC"

# MUTANT B: neuter the closure-status filter so ANY status counts as a closure. The
# touched-but-ACTIVE case must now fire. This is the guard that separates "a project file
# changed" from "a project CLOSED" -- the whole precision of the trigger.
sed "s/^CLOSURE_RE=.*/CLOSURE_RE='\"status\"'/" "$HOOK" > "$TMP/mutantB.sh"
printf '{"status": "active", "phase": "still active"}\n' > org/projects/FIXTURE_ALPHA.json
_commit "project touched, still active (mutant B probe)"
_mB="$(_probe "$TMP/mutantB.sh")"
if [ "$_mB" = "SILENT" ]; then
    FAIL=$((FAIL+1)); printf '  FAIL  %-52s mutant stayed SILENT -- guard untested\n' "M-B closure filter neutered -> must FIRE"
else
    PASS=$((PASS+1)); printf '  ok    %-52s went RED as required [%s]\n' "M-B closure filter neutered -> must FIRE" "$_mB"
fi

echo ""
echo "-- KNOWN NEGATIVE: the REGISTRY path OVER-FIRES (open defect, pinned) --"
# Reproduces the live shape of 8ca69b870b: ONE project closed; the REGISTRY diff MENTIONED
# others. The hook derives codes with \b[A-Z][A-Z0-9]+_[A-Z0-9_]+\b over the changed rows,
# which cannot tell a CLOSING project from a project merely NAMED on a reflowed line, and
# happily lifts non-project tokens. MEASURED: 0 of 294 org/projects/*.json end in _PRD, yet
# _PRD tokens become "projects" here; live, 8ca69b870b yielded 7 codes for 1 real closure and
# materialized owned findings against projects whose owner had not closed them.
#
# THIS ASSERTION PINS THE DEFECT, IT DOES NOT BLESS IT. If the derivation is fixed, this test
# FAILS -- deliberately. A fix is good news that must be recorded, not silently absorbed; the
# failure message says exactly what to do.
{
  printf '# REGISTRY\n'
  printf '| FIXTURE_BETA | complete | see FIXTURE_BETA_PRD for detail |\n'
  printf '| FIXTURE_GAMMA | active | untouched neighbour row reflowed |\n'
} > org/projects/REGISTRY.md
_commit "registry row move naming neighbours"
_kn="$(_probe "$HOOK")"
_expect_known="FIRE FIXTURE_BETA FIXTURE_BETA_PRD FIXTURE_GAMMA"
if [ "$_kn" = "$_expect_known" ]; then
    PASS=$((PASS+1))
    printf '  ok    %-52s defect present as recorded\n' "KN over-fire: 1 closure -> 3 codes"
    printf '        [%s]\n' "$_kn"
else
    FAIL=$((FAIL+1))
    printf '  FAIL  %-52s\n' "KN over-fire changed"
    printf '        recorded[%s]\n' "$_expect_known"
    printf '        actual  [%s]\n' "$_kn"
    printf '        If the derivation was FIXED, that is good news: update this expectation\n'
    printf '        and strike the known-negative note in the header. If it WIDENED, the\n'
    printf '        trigger is manufacturing more owned items pointing at nothing.\n'
fi

echo ""
echo "=================================================================="
printf 'RESULT: %d passed, %d failed\n' "$PASS" "$FAIL"
echo "Scored on printed OUTPUT above, not on this exit code."
echo "=================================================================="
[ "$FAIL" -eq 0 ] || exit 1
exit 0
