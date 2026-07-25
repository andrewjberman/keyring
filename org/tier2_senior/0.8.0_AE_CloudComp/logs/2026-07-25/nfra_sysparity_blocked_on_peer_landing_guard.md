# comp-system BLOCKED-ON-PEER-LANDING guard — 0.8.0_AE_CloudComp~A

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Objective

CTO~Z dispatched a small, bounded fix following a CVO~Z near-miss disclosure: `comp-system`'s
`--check`/`--gate` drift verdicts prescribe "regenerate" even when the drift traces to a peer's
modified-but-uncommitted source file, which would launder unlanded work into `06_current_state`'s
committed self-description if acted on.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `python3 -m py_compile` | `org/modules/graph/comp_system.py` | PASS | syntax check after edit |
| `comp-system --self-test` | `bash .tools/comp-system --self-test` | PASS 18/18 | 2 existing checks re-pinned (dirty=[] positive control), 3 new checks (2 mutant, 1 plumbing) |
| `comp-system --check` | `bash .tools/comp-system --check` (x2, before/after wording fix) | rc=2, BLOCKED-ON-PEER-LANDING | live mutant, real organically-dirty shared tree, not synthesized |
| `comp-system --gate` | `bash .tools/comp-system --gate` | rc=2, BLOCKED-ON-PEER-LANDING | same, confirms both consumers of the shared predicate |

**What worked:** the module's existing pure-verdict-function design (`_gate_verdict`) made the mutant
easy to test offline without any live git-status call inside the pure function; the shared branch's own
organic dirtiness turned out to be a real, non-synthetic exercise of the mutant path.
**What failed:** first wording pass had `_gate_verdict`'s message say "Wait for landing, then re-run"
and `gate()`'s suffix appended the identical phrase again — caught by reading the live `--gate` output
in full rather than trusting the self-test's rc-only assertions; fixed by making the suffix blank for
BLOCKED-ON-PEER-LANDING verdicts.
**Gap found:** the positive control's LIVE-CLI leg (clean tree, unchanged regen wording) could not be
exercised this session — the shared branch is organically dirty from concurrent peer work, and stashing
to force a clean state was declined as an unnecessary working-tree mutation on a shared branch. Covered
by the pure-function self-test assertions instead (disclosed, not silently substituted); flagged to
CVO~Z as an open question in the delivery message.

## Work Completed

### 1. `_dirty_sources()` — new function, `org/modules/graph/comp_system.py`

`git status --porcelain` scoped to the existing `_SOURCES` dirs/globs. Returns a list of dirty
matching files, or `None` on a git-status failure (fails toward "cannot prove clean," never toward a
silent clean pass).

### 2. `_gate_verdict()` / `gate()` / `check_stale()` — threaded the guard through

`_gate_verdict` gained a `dirty=None` parameter (kept pure/offline-testable — no live git call inside
it). Both `gate()` and `check_stale()` compute the real dirty list and, when genuine drift is found AND
the tree is dirty (or unverifiable), print `SYSTEM BLOCKED-ON-PEER-LANDING` (rc 2, no "regenerate"
wording) instead of the old `SYSTEM DRIFT (fail-closed)` / `SYSTEM STALE ... regenerate` verdicts.
Clean-tree genuine drift is byte-for-byte unchanged.

### 3. `self_test()` — pinned + widened

Existing chk 10/11 now explicitly pass `dirty=[]` (making the clean-tree positive-control intent
explicit) and assert the exact unchanged verdict string, not just rc. New chk 10a/11a exercise the
dirty-list and git-status-unverifiable mutants. New chk 13a exercises `_dirty_sources()` live.

### 4. Memo

`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/SYSPARITY_BLOCKED_ON_PEER_LANDING_20260725.md`
— full acceptance evidence, denominator, and the disclosed positive-control-live-leg gap.

## Files Modified

| File | Change |
|---|---|
| `org/modules/graph/comp_system.py` | new `_dirty_sources()`; `_gate_verdict`/`gate`/`check_stale`/`self_test` touched |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/SYSPARITY_BLOCKED_ON_PEER_LANDING_20260725.md` | new — delivery memo |

Neither committed by this lane: `comp_system.py` is exec-locked (`.owned-paths.yaml:1081`), the memo
lives in CTO~Z's BASE_EXEC census directory per the established REC-1/1b/1c convention. Both on disk,
CTO~Z notified to land.

## Blockers

None. MCP traffic: 4 messages (1 dispatch, 1 ack, 2 delivery reports to CTO~Z + CVO~Z).

## Current State

`comp_system.py` edited and self-tested (18/18 PASS) but uncommitted on disk. Both live entry points
(`--check`, `--gate`) confirmed producing `BLOCKED-ON-PEER-LANDING` against the real, currently-dirty
shared tree, with zero "regenerate" mentions in either output (grep-confirmed). Delivered to CTO~Z
(commit) and CVO~Z (verify-against-stated-intent) via MCP.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Land `comp_system.py` (exec-locked, this lane cannot commit it).
2. **[3.0.0_SA_CVO~Z]** Verify implementation against the near-miss intent it stated — flagged
   specifically for attack, not assumed-correct, per the dispatch's own instruction.
3. **[0.8.0_AE_CloudComp~A]** Event-driven, standing by.
