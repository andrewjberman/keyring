# D5-FIX.ORPHAN-PM — verify-before-delete + characterize (product-confirm gated)
**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, TRACE
**serial:** 0.4.0_DE_ClientPlatform
**window:** ~2006Z -> 2022Z 2026-06-12

## Summary

COO GO'd D5-FIX.ORPHAN-PM (delete the 19-file dead PortfolioManagement subtree my AC6 census
found), then AMENDED it (CVO product-confirm gate): a "dead refactor subtree" is ambiguous —
abandoned vs paused-WIP — so do the full verify-before-delete + CHARACTERIZE + STAGE-not-commit +
RAVC2 a recommendation for Andrew. Did exactly that. Verdict: ABANDONED, overwhelming evidence,
safe to delete. Deletion STAGED-NOT-COMMITTED (0 files deleted). RAVC2 sent COO + CC CVO.

## Work done

- **Per-file verify-before-delete (19/19):** static import + barrel re-export + dynamic/React.lazy
  + bare-string(registry) scan from every file OUTSIDE the 19-set. ALL 19 = 0 live inbound, 0
  pulled. 4 bare-name mentions in live files verified benign (a same-named AI `PortfolioSnapshot`
  interface + 3 comments).
- **Deletion-safety (ISOLATED):** first tsc in the MAIN tree showed a `PortfolioSummary` error —
  traced to CONTAMINATION from a concurrent eslint-cleanup agent's uncommitted `portfolio.ts`
  edit, NOT my deletion. Re-ran in an ephemeral worktree off clean origin/DEV (67bd09f2):
  baseline `tsc -b --force --noEmit` EXIT 0; after deleting all 19 -> tsc EXIT 0 AND `vite build`
  EXIT 0 (built 17.18s). Live PM page (487L) compiles+bundles green without the subtree.
- **D8:** comp-transform schema-check PortfolioManagement = PASS; comp-blast TradeTable = no graph
  nodes (graph-blind, consistent with orphan). No SEV1, no benchmark-adjacent surface.
- **Characterization = ABANDONED (high conf):** pivot commit `2a58b3a0` (Mar-23 "DEBT_1STRUN --
  extract shared utils, remove dead code") created the live `summaryStats.ts` (which "replaces
  duplicated logic in usePortfolioManagementState") + rewired live hooks, orphaning the old
  subtree without finishing its removal; 0 feature commits to the 19 since (~2.7mo; only mechanical
  color/lint sweeps); Apr-13 feature work built on the live path, not the dead `TradeTable.tsx`
  (frozen Feb-27). No paused-WIP markers (no flag, no half-wired route).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-transform schema-check | PortfolioManagement | PASS | all rendered fields match response types |
| comp-blast | TradeTable | N/A (graph-blind) | "No nodes matching" — PM components have 0 graph edges, consistent with orphan; file-level census per D8 Layer-2 |

What worked: ephemeral-worktree isolation was decisive — the main-tree tsc error was concurrent-
agent contamination, not my change; only a clean-baseline test gave a true signal. What failed:
`tsc -b --noEmit` (non-force) returns CACHED EXIT 0 and masks real errors — must use `--force` for
a true read. Gap: PM components are graph-blind (Rule-20 comp-kuzu can't see them); verify-before-
delete relies on file-level import-graph + tsc/build, not the graph.

## Files Modified

None committed. Deletion STAGED-NOT-COMMITTED per the CVO product-confirm gate. Main portal tree:
all 19 targets present, 0 deletions by me. Scratch (read-only): .runtmp/d5_de/verify_pm.py.

## Blockers

GATED (not blocked): the 19-file deletion awaits Andrew product-confirm (CVO gate 9d024bce5, COO
amendment 200834Z). Analysis itself is complete; only the irreversible commit waits on the human.

## Current State

- D5-FIX.ORPHAN-PM analysis COMPLETE. Recommendation ABANDONED/safe-to-delete sent to COO
  (RAVC2 20260612T202206Z) + CC CVO. 0 files deleted; deletion verified-safe + ready to apply on GO.
- On product-confirm GO: apply the 19-file deletion in the normal DEV path AFTER the concurrent
  eslint-cleanup fix-TO lands (avoid commit entanglement) + VALGATE; NOT promoted to PROD.
- The 19 paths are enumerated in the RAVC2 + .runtmp/d5_de/verify_pm.py CANDS list.
- Concurrent: another agent is mid-flight on the eslint-cleanup fix-TO (10 modified files incl.
  portfolio.ts, useOptimizationAutoSave.ts) — their uncommitted portfolio.ts edit currently fails
  tsc in the shared tree (flagged to COO as a heads-up; their VALGATE will catch it).

## Next Steps

- [2.0.0_SA_COO] route my ABANDONED recommendation to Andrew for product-confirm; on GO, signal me.
- [0.4.0_DE_ClientPlatform] on product-confirm GO: apply the 19-file deletion (DEV path + VALGATE,
  after the eslint-cleanup lands). Then next D5 fix-TOs (DC-01..07 dead modules, ROUTE-01) as COO
  routes them. Also banked: getPlatinumClientDetailStatic schema drift T1b (bundle next portal pass).
