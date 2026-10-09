# CTO RULING -- consolidate IRPT_DASHBD, IRPT_CUSTDY and IRPT_BCKEND ~P's performance scope into ONE project

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~04:3xZ | **Under:** /self-drive, every dell2 project (arming record @35fabf20c8)

**Inputs:**
- Andrew-direct ~04:2xZ, to `4.0.0_SA_CRO~DELL2`, VERBATIM: "I want you to take a look at a few projects that seem like consolidation
  targets. For example, DSHBRD, CUSTDY and IRPT WORKSTREAM ~P, all seem focused around really the same thing."
- The CRO's research: `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261009_CONSOLIDATION_CLIENT_PERFORMANCE_REPORTING.md` @53e1588f09
  (msg 2399).
- Andrew-direct ~04:2xZ to `~D2` @669ab7d677 (msg 2402): Inflection's returns are pulled GROSS from Orion, with its fees as their own figures,
  sliced like 49F's.

## Rulings

1. **CONSOLIDATE. IRPT_DASHBD is the SURVIVOR, re-scoped as the one client-performance product:**
   - the daily return series, the Reporting tab, and the quarterly client statement;
   - Black Diamond switched off per firm.

   IRPT_DASHBD holds the most of the product and has the live issuer (`~D2`).
   - **Absorbs:** IRPT_CUSTDY whole (FWD-1..9; the statement figures and per-firm templates), plus IRPT_BCKEND ~P's performance scope
     (FWD-3, FWD-12 as the guard rail, FWD-13 folded into the one BD comparison, and the statement export cell E-P9).
   - **Stays in IRPT_BCKEND (platform, `~P2`):** auth and routes (FWD-2), directory freshness (FWD-7), holdings (`~M2`, FWD-5), and
     `irpt-export-render` as the shared renderer.
   - **Stays elsewhere:** the Analysis lane, now IRPT_ANLREQ.
2. **WHEN: at each project's next round boundary. Nothing in flight is disturbed.**
   - IB-pr-383 (the 10-12 directory release), release 6 and every signed pair complete under their current projects and halves.
   - IRPT_CUSTDY's held CU-g-2a resumes under the survivor once release 6 and the svc-custody-statement mint land.
   - `~K2` hands its record to `~D2` at its next drain-end. After that, `~D2` is the one issuer.
3. **ONE return method for all three firms:** the flow-adjusted daily TWR (DASHBD's), with the holdings-only figure as its guard rail. That is
   already its role for 49F. It supersedes IRPT_BCKEND FWD-3's holdings-basis figure for Inflection and Cottonwood.
   - Inflection's TWR is taken GROSS from Orion, with fees as their own figures, sliced like 49F's BD (Andrew's word, @669ab7d677).
4. **ONE Black Diamond comparison:** DASHBD FWD-8. IRPT_BCKEND FWD-13 and IRPT_CUSTDY FWD-5 fold into it.
   - **FWD-8's single grade: NOT REALIZED** until Andrew states the tolerance he accepts. Today it is 8,433 of 9,078 within 0.35 pp.
   - This seat's rule: a CVO REALIZED on a sample does not override an open population figure. The CVO may adjudicate otherwise; its verdict
     governs.
5. **Household return:** check once, on one multi-account household, both ways, with the rule stated before the run (the CRO's 2.2). Then keep
   one sentence. This is the merged project's first enrichment after FWD-1.
6. **Registration (L3, this seat):**
   - IRPT_DASHBD's PRD gains a CONSOLIDATION addendum with the absorbed FWDs as new ids, never renumbered.
   - IRPT_CUSTDY closes as `superseded_by: IRPT_DASHBD` at its handover, with its FWDs mapped.
   - IRPT_BCKEND's PRD gains an addendum removing the moved scope.
   - These land at the handover, not before.
7. **Out of this box:** the MDPF_DEMQUE vs MDPF_SECHIST Yahoo-backfill collision (dell1/laptop) goes to MSTR~DELL2 for the owning CTOs.

-- 1.0.0_SA_CTO~DELL2

## CONFIRMED BY ANDREW (2026-10-09 ~04:4xZ)

VERBATIM, via `4.0.0_SA_CRO~DELL2` msg 2451 (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261009_044xZ_CONSOLIDATION_CALLS_GO_WITH_RECS.md` @c41f11fb70): "Go with your recs on both consolidation calls".
- Ruling 1 (one performance-reporting project, IRPT_BCKEND keeps the platform) is confirmed.
- Ruling 3 (Inflection and Cottonwood serve the flow-adjusted daily TWR, superseding IRPT_BCKEND FWD-3's holdings-basis figure for them) is confirmed.
- IRPT_CUSTDY was closed as superseded_by IRPT_DASHBD @d016a98794 after the `~K2` handover @185805a565.
