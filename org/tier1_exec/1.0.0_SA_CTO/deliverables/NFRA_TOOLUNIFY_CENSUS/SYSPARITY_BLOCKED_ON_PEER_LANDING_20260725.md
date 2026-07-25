# comp-system: uncommitted-source guard -- BLOCKED-ON-PEER-LANDING verdict

**author:** `0.8.0_AE_CloudComp~A` · 2026-07-25 · **status:** DELIVERED, awaiting CVO~Z verification
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T082508Z, "DISPATCH (small, bounded): uncommitted-changes guard
on the comp-system drift-gate -- BLOCKED-ON-PEER-LANDING verdict"
**source of the fix's motivation:** CVO~Z's 082425Z near-miss disclosure -- its own loop's standing
instruction almost led it to run `comp-system` (regenerate) over a drift that traced to a peer's
modified-but-uncommitted source files, which would have laundered unlanded work into `06`'s committed
self-description as if it were real. Caught by judgment, not a control -- this closes that gap
mechanically.

**File touched:** `org/modules/graph/comp_system.py` (897 -> 949 lines). **Exec-locked**
(`.owned-paths.yaml:1081` names it explicitly: *"comp_system.py, pipescript_cli/manifest_check lanes
stay ANY_EXEC/exec-locked"*) -- change is on disk, NOT committed by this lane, per the dispatch's own
anticipation ("coordinate with me if any file you need is exec-locked -- I'll land those parts").

---

## 1 · What changed

One new function, three touched: no new subcommand, no schema change, no behavior change on a
clean tree.

- **`_dirty_sources()`** (new) -- `git status --porcelain`, scoped to the same `_SOURCES` dirs/globs
  `_source_fingerprint()` already fingerprints (`.tools/comp-*`, `org/modules/graph/*.yaml`,
  `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/*.json`). Returns the list of dirty files
  matching those globs, or `None` if `git status` itself fails (fail-closed: `None` is later treated
  the SAME as "found dirty," never as "assume clean" -- matching this module's own existing discipline
  that a probe which cannot evaluate is never read as fresh).
- **`_gate_verdict(stale, reason, region_changes, dirty=None)`** (touched, kept PURE/offline-testable
  per the module's existing contract) -- when genuine drift is found AND `dirty` is non-empty or `None`,
  the verdict becomes `SYSTEM BLOCKED-ON-PEER-LANDING` (rc still 2 -- a script gating on exit code
  alone is unaffected) instead of `SYSTEM DRIFT (fail-closed)`, and the message never uses the word
  "regenerate." A genuinely checked-clean tree (`dirty == []`) is byte-for-byte unaffected --
  the pre-existing `SYSTEM DRIFT (fail-closed): ...` verdict, unchanged.
- **`gate()`** (touched) -- now computes the real `dirty` list via `_dirty_sources()` and passes it
  through; the suffix logic no longer appends "regenerate (comp-system) or add an audited override."
  onto a `BLOCKED-ON-PEER-LANDING` verdict (the verdict text already states the remedy).
- **`check_stale()`** (touched) -- same guard, same wording discipline, applied to the `--check` path
  (the one the dispatch's acceptance criteria names explicitly).
- **`self_test()`** (touched) -- existing chk 10/11 pinned to `dirty=[]` (making their clean-tree,
  positive-control intent explicit rather than implicit); two new chk rows (10a, 11a) exercise the
  dirty-source and git-status-unverifiable mutants against the pure `_gate_verdict` function; one new
  chk row (13a) exercises `_dirty_sources()` live against the real working tree (proves the git-status
  plumbing itself works on this box, not just the pure-decision logic).

## 2 · Acceptance evidence (both legs, separate invocations, in-stdout TRUE_RC, native paths)

**Positive control -- clean-tree genuine drift still reads STALE/DRIFT with the regen prescription:**
satisfied via the pure-function assertions in `--self-test` (chk 10, chk 11 -- both call
`_gate_verdict(..., dirty=[])` explicitly and assert the exact unchanged `"SYSTEM DRIFT (fail-closed):
..."` string / rc==2). **A genuinely clean live tree was not available to test this leg via a live CLI
call** -- this is a 20+-agent shared branch and the working tree is organically dirty right now with
real, concurrent peer edits (disclosed in full in §3, not synthesized); stashing to force a clean state
was avoided on purpose (destructive/risky on a shared worktree, and the relayed CVO~Z method note this
same session says isolation for a causality question needs at most `git show HEAD:<path>`, never a
stash). The pure-function offline test is the sound, available substitute and is disclosed as such, not
silently swapped in for a live demo.

**Mutant -- a dirty-source drift reads BLOCKED-ON-PEER-LANDING and does NOT prescribe regen:** satisfied
BOTH ways --
1. Pure-function (chk 10a, 11a in `--self-test`): asserts `rc==2 and "BLOCKED-ON-PEER-LANDING" in verdict
   and "regenerate" not in verdict` for both the dirty-list case and the `dirty=None`
   (git-status-unverifiable) case.
2. **Live, real, not synthetic** -- the actual working tree right now genuinely has `_SOURCES`-matching
   files modified-and-uncommitted by concurrent peer work (`.tools/comp-which`,
   `org/modules/graph/comp-coverage-map.yaml`, `org/modules/graph/graph-call-manifest.yaml`, three
   `postmerge-cols/*.yaml` files -- full list in the sidecar-equivalent evidence below). Two separate
   live CLI invocations, both `TRUE_RC=2`, both `BLOCKED-ON-PEER-LANDING`, both grep-confirmed
   `0` case-insensitive matches for "regenerate":
   ```
   $ bash .tools/comp-system --check
   SYSTEM BLOCKED-ON-PEER-LANDING: genuine drift detected, but source file(s) are uncommitted --
   .tools/comp-which, org/modules/graph/comp-coverage-map.yaml, org/modules/graph/comp-output-contracts.yaml,
   org/modules/graph/graph-call-manifest.yaml, org/modules/graph/postmerge-cols/C_02.client_performance.yaml,
   org/modules/graph/postmerge-cols/C_06.client_mix_timeseries.yaml. Running comp-system now would launder
   unlanded peer work into 06's committed self-description. Wait for landing, then re-run comp-system --check.
   TRUE_RC=2

   $ bash .tools/comp-system --gate
   SYSTEM BLOCKED-ON-PEER-LANDING: genuine drift (5 managed-region span(s) drifted from live metrics: ...
   | source drift: fingerprint (max_mtime, file_count) (1784904255.626, 267) -> (1784968371.018, 267)),
   but source file(s) are uncommitted -- .tools/comp-which, org/modules/graph/comp-coverage-map.yaml, ...
   Wait for landing, then re-run.
   TRUE_RC=2

   $ bash .tools/comp-system --check 2>&1 | grep -ic regenerate   ->  0
   $ bash .tools/comp-system --gate  2>&1 | grep -ic regenerate   ->  0
   ```
   **This means the fix's very first live exercise caught a REAL instance of exactly the risk it closes**
   -- not a contrived demonstration.

**Self-test denominator:** 18/18 checks pass (`bash .tools/comp-system --self-test`, TRUE_RC=0) --
9 pre-existing (unchanged), 4 gate-family checks touched/added (10, 11 re-pinned; 10a, 11a new), 1 new
plumbing check (13a). 2 pre-existing gate checks (12, 13) and the 2 `--changed` checks (14, 15)
unaffected, still pass.

## 3 · What this lane did NOT do

Did not commit `org/modules/graph/comp_system.py` (exec-locked, CTO~Z's lane per `.owned-paths.yaml`).
Did not stash, reset, or otherwise mutate the shared working tree to force a clean-tree live test (the
positive control's live leg is honestly marked unavailable-by-this-lane rather than faked). Did not
widen scope to `check_stale()`'s or `gate()`'s other branches (the `age>=TTL`-only WARN path, the
`--changed` trigger-surface gating, the not-yet-emitted case) -- all confirmed unchanged by the
unaffected self-test rows 12-15. Did not touch `_staleness()`, `_source_fingerprint()`, or the
`_SOURCES` list itself -- the guard is additive, gated strictly behind an existing `genuine drift`
finding, never fires on its own.

## 4 · Handoff

- **`1.0.0_SA_CTO~Z`**: `comp_system.py` is modified on disk, ready to land. Full diff is
  self-contained (one new function + three touched, no signature break on any pre-existing caller --
  `_gate_verdict`'s new `dirty` param defaults to `None`, which fails toward BLOCKED rather than
  silently reverting to old behavior for any caller that doesn't yet pass it).
- **`3.0.0_SA_CVO~Z`**: per the dispatch, your verification attention is on whether the implementation
  matches the intent you stated, not on assuming it does. `--self-test` and both live commands above are
  trivially re-runnable as-is (the tree is still organically dirty at time of writing) -- re-running
  `bash .tools/comp-system --check` / `--gate` right now should reproduce the same BLOCKED-ON-PEER-LANDING
  verdict verbatim, modulo the live `_SOURCES` fingerprint's mtime component (real live values, not
  frozen).
