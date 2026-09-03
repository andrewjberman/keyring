# ANDREW-DIRECT 2026-09-02 ~23:5xZ -- R-i approved: the generator's `check` becomes a refusal on the commit gate, BEFORE L3's registration commit

**Channel:** Andrew, directly at the `1.0.0_SA_CTO` terminal, mid-turn during L3 of the NFRA_COMPEFFICACY test run.
**Recorded by:** `1.0.0_SA_CTO`, same turn. Broadcast same turn to `3.0.0_SA_CVO`, `2.0.0_SA_COO`, `0.0.0_AB_MSTR`.

> **NEVER A PARAPHRASE. THE PHRASING *IS* THE RULING.** Verbatim:
>
> *"make sure you handle this, rec approved: [<One call, carried, not blocking: CVO's residual R-i asks that the
> generator's check be wired into the commit gate as a refusal for staged tree/register paths. That is a new refusal
> on an existing gate, so it is yours — REC yes, before L3's commit, so the registration is the first commit the tree
> validates mechanically.>]"*

## What it settles

- **R-i is approved as recommended, INCLUDING ITS TIMING:** the refusal is wired before the L3 registration commit,
  so `org/missions/D11/NFRA/NFRA_COMPEFFICACY/project.json` + its generated index entry are the first commit the tree
  validates mechanically. The registration was NOT yet committed when this word arrived (the commit call had been
  refused by the comp-rail over an unrelated search token in the same command; nothing landed) -- the sequence he
  asked for is honoured exactly, not retro-fitted.
- **The refusal:** any commit whose staged paths include `org/missions/D<n>/**` or `org/projects/*.json` runs
  `.tools/missions-tree-index.py check` and is REFUSED on rc 1 (violations, printed) or rc 2 (the generator could
  not run -- fail closed). rc 0 passes. It is an additional limb on the EXISTING commit path (`safe-commit.sh`'s
  pre-commit gates), not a new gate.
- **Consequence he will see immediately:** with the refusal live, the registration commit is refused on R5 until
  `0.0.0_AB_MSTR` lands `NFRA_COMPEFFICACY` in `DIRECTIVES.yaml` D11 members -- that is the gate doing what it is
  for. MSTR's line therefore lands first (it validates clean on the shared worktree, where the folder and index
  entry already exist uncommitted), then the registration commit passes.

## Not settled by this word

- The staged-vs-worktree grain of `check` (the generator reads the worktree; the step-6 gate's limb 5 reads the
  staged index). Stated in the hook's header as a known bound, not closed here.
- R-ii (six one-root TO readers) and R-iv (the gate reading `row.project_code`) -- still queued at this seat behind
  the test run's steps; not widened by this word.
