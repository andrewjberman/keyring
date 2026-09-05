# ANDREW-DIRECT at the CTO terminal, 2026-09-03 ~13:0xZ -- "recs approved" on /open-calls (2 calls)

**Verbatim (all words):** `recs approved`

**What was in front of him (the /open-calls output of 1.0.0_SA_CTO, 2 calls, both CARRIED):**

- CALL 1: apply the 60-day expiry on ms-heat snapshots in the global_graph bucket -- (a) yes, under its own ledger
  entry, or (b) no, revert the declaration. Declared in Terraform 2026-07-15 by 0.8.0_AE_CloudComp~Z, never applied;
  held under CloudComp's change-management entry (commit c5dea0f11c) with every shared-infra apply scoped away from it.
  **REC (a), once the owner states the snapshots are rebuildable;** (b) if they are not.
- CALL 2: confirm or dispute the DONE WHEN lines of the two retrofitted endpoints -- ADVI_INSURE FWD-1..10
  (`docs/architecture/ADVI_INSURE_PRD.md`) and ADVI_49F FWD-1..6 (`docs/architecture/D2_ADVI_49F_E2E_PRD.md`), his L2
  touch point ("i will confirm CTO's DONE WHEN from their /endpoint --forward"). **REC confirm as written.**

**Reading (scope = the two recs, verbatim, nothing wider):**
1. The lifecycle expiry applies ONCE ITS OWNER STATES IN WRITING THAT THE SNAPSHOTS ARE REBUILDABLE; that statement
   lands in the HOLD ledger entry, the owner applies the rule under that entry through safe-apply, and the acceptance is
   an UNSCOPED re-plan reading 0/0/0. If the owner states they are NOT rebuildable, the declaration is reverted so
   DESIRED matches APPLIED. Either way the act is the owner's (0.8.0_AE_CloudComp / NFRA_GLOBGRPH, module steward
   0.7.0_AE_CloudOps per the D0 rows), gated by the CTO as every apply is.
2. The sixteen DONE WHEN lines of the two endpoints are CONFIRMED AS WRITTEN. Both PRDs carry the confirmation beside
   their ENDPOINT sections; the ids are permanent; a future dispute appends a new id, never edits one.

**Authority chain:** this record; his 2026-09-03 ~05:2xZ word on the L2 touch point
(`ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_COO_COMPLETION_REPORT_CTO_GRADES_TWO_READS.md`); the HOLD entry
`org/critical_paths/change_management/20260903T1120Z_shared-infra-ms-heat-snapshots-expire-60d_hold.md` @c5dea0f11c;
the two endpoint commits @447605c7de / @9669835c7e and the header commit @87fbf61c0b.

**Execution this turn (1.0.0_SA_CTO):** the confirmation written into both PRDs beside their ENDPOINT sections and
committed with this record; the lifecycle ruling routed to its owner with its condition and to 0.0.0_AB_MSTR for relay
to site Z; same-turn broadcast with push state stated as measured.
