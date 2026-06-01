# work 1702Z — 0.4.0_DS_ClientPlatform~C — wire wrong-entity gate into pull path

**Tick:** /work 2026-06-01 ~1702Z. **Project:** FIND_INSURE Phase 2A (parallel/secondary).
**Trigger:** CTO [RESOLVE routing] 170359Z — (1) PMA removal STANDS no-revert, (2) confirm the standing gate is wired into the pull path, (3) Eagle = milder over-scope, route disposition via COO.

## Done this tick
1. **Gate WIRED into the enrichment pull path** (96018e109) — CTO #2:
   - Extracted reusable `run_gate()` in `rep_bd_disjoint_gate.py`; `finra_backfill_existing_bronze.py` now auto-runs the wrong-entity gate at the end of every enrichment run.
   - Policy split: in-pipeline = advisory WARN (enrichment succeeded), standalone gate = exit-1 blocking CI check.
   - Effect: the PMA/#79 wrong-entity class auto-flags at PULL-TIME for every IMO — covers the 75 unpulled IMOs when pulled, no manual audit.
   - Verified: `run_gate` importable from backfill path, py_compile clean, standalone exit 0 (PMA=KNOWN, midland=LOW_CONF), 5 tests pass. (Full 24-IMO backfill not re-run — enrichment already done + wiring import/compile-verified.)
2. **Routing crossing RESOLVED**: CTO confirmed PMA off-slot removal is FINAL (his [ALIGN] hold superseded by considered 162809Z position; binding regardless of A/B). No revert; Lincoln #1 stands. Confirmed the timeline: COO 163931Z GO is the latest word, post-dating the CTO 163914Z [ALIGN].
3. **Eagle #31**: kept flagged REVIEW_CONFIRMED_OVERSCOPE in-universe (not off-slot-removed per CTO); disposition routed to COO.

## Gate / verify
- ds-commit-gate clean (2 files); pytest 5 pass; run_gate import + backfill py_compile OK; standalone gate exit 0.

## Commits
- `96018e109` (gate wired into pull path) — pushed origin/CLOUD.

## RAVC2 / confirm
- CTO 170930Z (gate-wired confirm) + COO 170947Z (CC + re-surfaced open asks).

## Open / pending senior decisions (non-blocking; FIND_INSURE parallel/secondary)
- COO: Eagle #31 disposition (re-source-to-RIA vs accept-parent-with-annotation); 'life' _FIRM_STOPWORDS bank-or-GO.
- Andrew: universe-DEFINITION A/B (expand to adjacent-WM vs insurance-IMO-only).

## Queue note
- 5 pending ADVI TOs (DEMOV1/INFDEMO) + 1 in_progress (ADVI_INFDEMO.F4) + 1 dispatched (F11) in the shared ClientPlatform task_orders dir — off the FIND_INSURE-resume priority lane + freshness/ownership uncertain. Not actioned; flag to COO for priority/ownership if FIND_INSURE quiesces.
