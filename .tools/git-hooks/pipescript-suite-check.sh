#!/usr/bin/env bash
# =============================================================================
# pipescript-suite-check.sh -- pre-commit stage 7: the comp-pipescript suite gate.
#
# Dial F9 (DIAL_RECORD_comp-pipescript_20260804.md @7900435cb): a gate no runner
# is wired to decays silently -- the 4-file suite sat RED ~4 weeks unobserved,
# every failure dating to a real estate change nobody replayed the suite
# against. This stage runs the suite iff a staged path can BREAK it: it
# observes on the CAUSE, not a clock. Unrelated commits: ZERO suite
# invocations (no python spawn, no pytest -- the predicate is pure bash).
#
# TO: ADHOC.comp-pipescript-suite-commit-gate-f9 (2.0.0_SA_COO -> 0.8.0_AE_CloudComp~D)
# Shape borrowed from rcg-sweep-check.sh: the SCOPED-STAGE wiring ONLY -- the
# cheap predicate runs first and every non-matching commit exits silently.
# (NOT borrowed: rcg's author-identity keying, which is specific to the RCG
# sweep-executor ruling.)
#
# ---------------------------------------------------------------------------
# THE WATCH LIST -- SINGLE DERIVATION POINT (TO scope 4 / dial F9).
# Both the trigger predicate AND the suite invocation derive from the two
# blocks below. No other file carries this list: the orchestrator stanza's
# missing-script backstop keys on ONE sentinel path (pipeline_cli.py) and
# names this file as canonical.
#
# Membership source-confirmed 2026-08-04 by 0.8.0_AE_CloudComp~D:
#   The dial suite (P6, 41 tests green @a35ac7af8) is
#     test_multi_pipeline.py (21) + test_pipeline_gaps.py (16)
#     + test_pipescript_deployed_bd_hold.py (2) + test_pipescript_io_discrimination.py (2)
#   -- NOT test_sovereign_held_no_drift as the TO's candidate list guessed;
#   arithmetic + imports settle it (21+16+2+2=41, both extra files exercise
#   extract_pipeline). test_sovereign_held_no_drift.py (5) is ADDED on top:
#   comp-pydeps confirms it INVOKEs pipeline_cli, and it is the suite member
#   that catches predicate-import drift in the engine. Gate suite = 5 files,
#   46 tests at authoring.
#   Engine paths = pipeline_cli.py + its direct engine imports
#   (extract_pipeline.py, sovereign_held.py) + the INVOKE consumer
#   .tools/safe_deploy_core.py (deploy gating) + the .tools/comp-pipescript shim.
#   Deliberately NOT watched: the no-drift census's wider tool set
#   (trace_graph, comp-secrets, ...) -- their lanes carry their own tests, and
#   taxing every tool commit with this suite breaks the zero-cost-to-unrelated
#   property the TO names as load-bearing.
#
# TEST GLOBS are patterns so sibling-TO fixtures (F1, and any later
# test_pipescript_*.py) auto-enroll with ZERO edits to this gate (TO scope 4).
# ---------------------------------------------------------------------------
#
# Bypass (audited, never silent -- rcg-sweep pattern):
#     PIPESCRIPT_SUITE_SKIP="<reason>" git commit ...
# permits the commit and appends a SKIPPED-BYPASS line to the audit log.
#
# Audit: org/pipescript-suite-gate-audit.log -- one line per FIRE (PERMITTED /
# DENIED / SKIPPED-BYPASS). Non-watched commits write nothing (log stays
# signal). The PERMITTED lines are the "observed green on a wired runner"
# record the dial's F9 finding asked for; each carries the suite denominator
# so a silently shrinking suite is visible in the log.
#
# rc: 0 permit | 1 DENY (suite red, or cannot evaluate -- fail closed).
# Rule 16: Git Bash 3.6.7 default utilities only. ASCII only.
# Author: 0.8.0_AE_CloudComp~D, 2026-08-04.
# =============================================================================

ROOT="${PRECOMP_REPO_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null)}"
if [ -z "$ROOT" ]; then exit 0; fi

# --- Watched non-test paths (exact, repo-relative) ---------------------------
WATCH_EXACT="
org/modules/graph/pipeline_cli.py
org/modules/graph/extract_pipeline.py
org/modules/graph/sovereign_held.py
.tools/safe_deploy_core.py
.tools/comp-pipescript
.tools/comp-find
.tools/comp-read
"

# --- Suite files (repo-relative patterns; trigger AND invocation) ------------
# test_extract_column_gaps_bd_hold.py enrolled 2026-08-04 (dial F10, TO
# ADHOC.graph-tests-hygiene-f10): it oracles extract_pipeline's held-path guard
# mechanism and predates the pipescript glob -- the F9 rot class survives
# wherever the glob cannot see, so membership is extended HERE, the one
# derivation point, never a second list.
# F11 family enrolled 2026-08-04 (TO ADHOC.graph-tests-hygiene-f11-family): the three
# repaired held-guard mechanism oracles join the suite; their engines (comp-secrets,
# freshness_manifest_gen, platinum_cli) delegate to the same sovereign_held predicate the
# pipescript engine uses, so they redden on the same cause class. test_incrparity_cli_bd_hold
# is RETIRED (guard deleted @f9ddda52f), not enrolled.
WATCH_GLOBS="
org/modules/graph/tests/test_multi_pipeline.py
org/modules/graph/tests/test_pipeline_gaps.py
org/modules/graph/tests/test_pipescript_*.py
org/modules/graph/tests/test_sovereign_held_no_drift.py
org/modules/graph/tests/test_extract_column_gaps_bd_hold.py
org/modules/graph/tests/test_comp_secrets_bd_hold.py
org/modules/graph/tests/test_freshness_manifest_gen_bd_hold.py
org/modules/graph/tests/test_platinum_held_path_guard.py
org/modules/graph/tests/test_script_io_ast.py
org/modules/graph/tests/test_comp_read.py
org/modules/graph/tests/test_comp_find.py
"
# test_script_io_ast.py added 2026-08-05 (3.0.0_SA_CVO~B): it is the battery for the R-1/R-2
# generalist I/O engine that `comp-pipescript io` now falls back to (@e07b9a29a), so a change that
# breaks it breaks a live pipescript answer path. Adding ONLY this file, deliberately: measured the
# same day, 80 of the 90 test files in org/modules/graph/tests/ sit OUTSIDE this allowlist (the gate
# runs 10). Widening it wholesale would immediately pull in test_adapter_audit.py, which fails
# COLLECTION because its target module org/modules/graph/adapter_audit_cli.py does not exist -- so
# every comp-pipescript commit would start blocking on an unrelated pre-existing break. That is a
# scoping call for the gate's owner, not a side effect of registering one new battery. The 80/10
# gap is routed as its own finding.
#
# test_comp_read.py + test_comp_find.py added 2026-08-06 (3.0.0_SA_CVO~B), NFRA_SCRIPTGEN Part B,
# WITH their engines .tools/comp-read + .tools/comp-find enrolled in WATCH_EXACT above. BOTH HALVES
# ARE REQUIRED AND THE SECOND IS THE LOAD-BEARING ONE: a suite file listed here but whose engine is
# not watched runs only when SOMEONE ELSE'S commit happens to trigger the gate -- which is the F9
# decay class ("a gate no runner is wired to decays silently") reproduced inside the gate built to
# kill it. Enrolled EXPLICITLY rather than by naming the files test_pipescript_*.py: that glob would
# auto-register them with zero edits here and MISNAME them as pipescript suite members, buying a
# free registration with a permanent lie about what the battery covers.
#
# SCOPE NOTE, stated so a later reader does not infer more than is true: this gate is comp-pipescript's,
# and comp-find/comp-read are NOT pipescript engines. What is being borrowed is the RUNNER, because it
# is the one wired commit-time runner in this tree. If a comp-tool suite gate is ever stood up, these
# four lines move there; they are not an argument that these tools belong to pipescript.

STAGED="${PIPESCRIPT_SUITE_STAGED_FILES:-$(git diff --cached --name-only 2>/dev/null || true)}"
if [ -z "$STAGED" ]; then exit 0; fi

# --- Trigger predicate: any staged path in WATCH_EXACT or matching a glob ----
TRIGGERS=""
while IFS= read -r p; do
    if [ -z "$p" ]; then continue; fi
    hit=0
    for w in $WATCH_EXACT; do
        if [ "$p" = "$w" ]; then hit=1; break; fi
    done
    if [ "$hit" -eq 0 ]; then
        for g in $WATCH_GLOBS; do
            case "$p" in
                $g) hit=1; break ;;
            esac
        done
    fi
    if [ "$hit" -eq 1 ]; then TRIGGERS="$TRIGGERS $p"; fi
done <<EOF_STAGED
$STAGED
EOF_STAGED

# Unrelated commit: silent, zero-cost exit. No python was spawned above.
if [ -z "$TRIGGERS" ]; then exit 0; fi

AUDIT="$ROOT/org/pipescript-suite-gate-audit.log"
ISO="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown)"
AUTHOR="$(git var GIT_AUTHOR_IDENT 2>/dev/null | sed 's/ <.*//' || echo unknown)"

_audit() {  # $1 verdict  $2 detail
    printf '%s  %-15s  author=%s  %s\n' "$ISO" "$1" "$AUTHOR" "$2" \
        >> "$AUDIT" 2>/dev/null || true
}

# --- Audited bypass (never silent) -------------------------------------------
if [ -n "${PIPESCRIPT_SUITE_SKIP:-}" ]; then
    _audit "SKIPPED-BYPASS" "reason=${PIPESCRIPT_SUITE_SKIP} trigger=${TRIGGERS# }"
    echo "WARN: comp-pipescript suite gate BYPASSED (audited to org/pipescript-suite-gate-audit.log): ${PIPESCRIPT_SUITE_SKIP}" >&2
    exit 0
fi

# --- Fail closed if we cannot evaluate ----------------------------------------
if ! command -v python >/dev/null 2>&1; then
    echo "BLOCKED: comp-pipescript suite gate (dial F9) -- 'python' is not on PATH; the gate cannot evaluate, which is a DENY." >&2
    _audit "DENIED" "python-missing trigger=${TRIGGERS# }"
    exit 1
fi

# --- Expand the suite from the SAME globs (single derivation point) ----------
SUITE_FILES=""
N_FILES=0
for g in $WATCH_GLOBS; do
    for f in "$ROOT"/$g; do
        case "$f" in *"*"*) continue ;; esac   # unmatched glob stays literal: skip
        if [ -f "$f" ]; then
            case " $SUITE_FILES " in
                *" $f "*) ;;                    # dedup (globs may overlap)
                *) SUITE_FILES="$SUITE_FILES $f"; N_FILES=$((N_FILES+1)) ;;
            esac
        fi
    done
done

if [ "$N_FILES" -eq 0 ]; then
    echo "BLOCKED: comp-pipescript suite gate (dial F9) -- watched paths staged but ZERO suite files resolve on disk. A gate with no suite is the decay this gate exists to kill." >&2
    _audit "DENIED" "zero-suite-files trigger=${TRIGGERS# }"
    exit 1
fi

# --- Run the suite -------------------------------------------------------------
# STRUCTURAL FALSE RED, measured 2026-09-10 by 0.0.0_AB_MSTR and confirmed at 1.0.0_SA_CTO (95122):
# "$ROOT/.git" is a DIRECTORY only in the MAIN tree. In a LINKED WORKTREE .git is an 86-byte POINTER
# FILE, so `>"$OUT"` dies with "Not a directory", the whole `if` takes the failure branch, and the gate
# reports the suite RED with an EMPTY failing-test list -- pytest's verdict never entered it. The suite
# was never actually red. Rule 14b directs every seat into a linked worktree while other seats are live,
# so the BROKEN shape was the NORMAL one, and a gate that cries wolf teaches seats to bypass it.
# rev-parse --absolute-git-dir resolves to a real writable directory in BOTH shapes (main tree ->
# <root>/.git; linked worktree -> <root>/.git/worktrees/<name>), measured on both before this change.
# The fallback keeps a broken resolution from re-creating the same false red by another route.
GITDIR="$(git -C "$ROOT" rev-parse --absolute-git-dir 2>/dev/null)"
[ -n "$GITDIR" ] && [ -d "$GITDIR" ] || GITDIR="${TMPDIR:-/tmp}"
OUT="$GITDIR/pipescript-suite-last-run.out"
echo "[pipescript-suite-gate] watched path staged -- running the comp-pipescript suite ($N_FILES files) ..." >&2
if (cd "$ROOT" && python -m pytest $SUITE_FILES -q --color=no >"$OUT" 2>&1); then
    SUMMARY="$(tail -1 "$OUT" | tr -d '\r' | sed 's/\x1b\[[0-9;]*m//g')"
    echo "[pipescript-suite-gate] OK: $SUMMARY" >&2
    _audit "PERMITTED" "files=$N_FILES result='$SUMMARY' trigger=${TRIGGERS# }"
    exit 0
else
    echo "" >&2
    echo "BLOCKED: comp-pipescript suite gate (dial F9) -- the suite is RED and a path that can break it is staged." >&2
    echo "  staged trigger path(s):${TRIGGERS}" >&2
    echo "  failing tests:" >&2
    grep -E "^(FAILED|ERROR)" "$OUT" | sed 's/^/    /' >&2 || tail -15 "$OUT" | sed 's/^/    /' >&2
    echo "  full output: $OUT" >&2
    echo "  Fix the suite (or the change), or bypass AUDITED with PIPESCRIPT_SUITE_SKIP=\"<reason>\"." >&2
    _audit "DENIED" "files=$N_FILES trigger=${TRIGGERS# } out=$OUT"
    exit 1
fi
