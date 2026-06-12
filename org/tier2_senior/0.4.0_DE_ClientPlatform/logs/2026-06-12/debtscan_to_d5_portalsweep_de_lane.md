# TO-D5 PORTALSWEEP — DE lane (component/data-channel/type-contract sweep)
**archetype:** EXPLORE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**serial:** 0.4.0_DE_ClientPlatform
**window:** session start (~1929Z) -> 1957Z 2026-06-12

## Summary

Spawned, armed /watcher (Monitor task b5af638uk live), registered LIVE, checked in with COO.
Executed the DE lane of NFRA_DEBTSCAN.TO-D5 PORTALSWEEP (joint with DT, Andrew-named both) —
read-only AC4 (dead data channels) / AC5 (unused imports) / AC6 (dead exports/components) sweep
of the whole portal (443 ts/tsx files; Phase-1 AdvisorIntelligence+ModelPortfolios deep, Phase-2
mechanical census global). Merged §4 into DT's joint ledger, committed, handed DT the joint RAVC2.

## Work done

- **Coordination:** confirmed AC2/AC5 split with DT (DT owns broad ESLint AC2; DE owns the
  unused-imports census AC5). DT authored ledger; I added §4 and co-signed.
- **AC5:** ESLint `unused-imports` (scoped to real `portal/src/`, `.runtmp/` worktrees excluded)
  = **0 unused imports**; 5 unused-VARS only (already DT's ESLINT-02). Clean on imports.
- **AC4 dead data channels:** file-level import-graph detector found **7 whole-file dead modules**
  DT's export-grep didn't surface (orphaned ENTIRE files): `endpoints/benchmarks.ts` (dead shadow
  of `@/api/portal-proxy`), `endpoints/market-update.ts`, `endpoint-mapping.ts`(286L),
  `sentiment-backend.ts`, `client/axios.ts`, `lib/rsiCalculator.ts`, `lib/colorTokens.ts`
  (also out-of-pattern: `getSentimentColor` re-defined 3x locally). `comp-cache collisions` = 5
  shared keys, all type-consistent = **0 real RQ collisions**.
- **AC6 dead exports/components:** 72 orphan files (no importer by path). Clusters: ORPHAN-PM(19,
  HIGH — dead refactor sub-tree under the live PortfolioManagement page), ORPHAN-AI(11, Phase 1),
  ORPHAN-MISC(8, incl. dead 1185L Attribution `HoldingsTab`), ORPHAN-UI(3), ORPHAN-BARREL(3),
  ORPHAN-CATALYST(21, ADVISORY/vendored — not actionable).
- **Precision contributions to DT:** ROUTE-02 (getAccountDistribution) RESOLVED as FALSE ALARM
  (live path is `/api/general/`, the `/api/private/` was a commented-out line + doc text;
  channel is live at `ModelPortfolios.tsx:432`). ROUTE-01 (searchSecurities) DE-confirmed 0
  callers -> dead-code/dormant, recommended MEDIUM not HIGH.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-cache collisions | portal RQ keys | PASS | 5 shared keys all type-consistent = 0 real collisions |

What worked: comp-cache cleanly separated safe shared keys from corruption (none found).
What failed: none. Gap found: none new — the file-level orphan census is grep/AST not a comp-*
tool (portal dead-component census is not graph-indexed; D8 Layer-2 file-level lesson applies).
Other AC4/5/6 work is read-only census (ESLint + custom import-graph), not a cloud/infra/data
change — Rule-20 graph checks ride the eventual fix-TOs, not this read-only sweep.

## Files Modified

| File | Change |
|---|---|
| org/modules/graph/debtscan/2026-06-12_D5_portalsweep_dt_de.md | §4 DE findings (AC4/5/6) merged + co-sign header/footer — commit 872c6ad19 |

Scratch (read-only, .runtmp/d5_de/, not committed): eslint_full.json, dead_files.py (import-graph
orphan detector), dead_exports2.py (export census).

## Blockers

None. DE lane complete; awaiting DT's joint RAVC2 send (DT leads, I'm aligned).

## Current State

- TO-D5 DE lane DONE. Joint ledger `org/modules/graph/debtscan/2026-06-12_D5_portalsweep_dt_de.md`
  has DT §§1-3,5-8 + DE §4 (commit 872c6ad19 on CLOUD). DT base ledger was c2539b2bb.
- Zero mutations to `portal/src/` — read-only sweep. All fixes = separate TOs after CVO §3
  precision-gate adjudication.
- Detector note: file-level orphan resolver uses APPEND-suffix (not `Path.with_suffix`, which
  clobbers dotted names like `*.context.ts` -> caused a transient contexts/ FP, fixed).
- Highest-value removal candidate flagged: ORPHAN-PM (19 dead files under the live PM page).

## Next Steps

- [0.4.0_DT_ClientPlatform] merge DE §4d rows into §7 + send joint RAVC2 to COO CC CVO.
- [3.0.0_SA_CVO] §3 precision-gate adjudication before any orphan cluster is promoted to a fix-TO.
- [0.4.0_DE_ClientPlatform] standing by for fix-TOs (ORPHAN-PM removal is the lead candidate) +
  next allocation pass. Also pending from prior session: getPlatinumClientDetailStatic schema
  drift (T1b, medium, bundle with next portal pass).
