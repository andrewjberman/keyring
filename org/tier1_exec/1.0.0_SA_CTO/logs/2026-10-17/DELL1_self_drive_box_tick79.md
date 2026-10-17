# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 79 (covers ticks 77a to 78a, about 16:19Z to 17:18Z)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **Portal PROD-into-DEV fold-back (MSTR 7658, 7659; H2 7665; R1 7666).**
  - dell2's reconcile is CLOSED. origin/DEV..origin/PROD read 2 commits: our 14:44Z release merges 40845c7e and 99d2b2a7.
  - RULED: ~H2 folds them back, with the tree equal to DEV, through R1's amendment of bq-2. This is the standing step after every
    chosen-set promote.
  - The register refused it (dev-overlap 106 of 107). My measure after a fetch: PROD..DEV is 106, and the only branch-only commit is the
    fold merge ac8b722a; TREE-EQUALS-DEV.
  - RULED: a named waiver of exactly those 106, @160cf257d5. Approval row f936 APPROVED.
- **MDPF orion reader (D1 7668).** The 10-16 burst did not recur, and the reader is not yet named. The default stands: keep logging, re-read
  after 16:30Z on 10-18, and remove the logging by 10-19 18:39Z.
- **HARVST ce-4 (W1 7676).** The gold continuation and dossier rebuild of 31 securities.
  - COO half 5b486cda @2fe63a70d6 read: add-only, N = 2 writers, both branches stated.
  - CTO half SIGNED @eae892eec0. It adds C-9: site Z is told first, and a site Z rebuild in flight on any of the 31 is a STOP.
  - The delete rollback is not pre-approved, since it is Andrew's act.

## Completion test

NOT DONE. This is the standing box drive, which ends on Andrew's word.

## Acts only Andrew can do (each with its citation)

1. ADVI_COTBOOKS: confirm the 6 DONE WHEN lines (row 0cf5). Canonical loop L2.
2. SOC2_MSLOGS round 2: run the 8-day re-derive with his MFA session (row 89c9). The access group holds Andrew_Berman alone (TO-R2-r2 :29).
3. SOC2_MSLOGS FWD-1: his read of the enriched block, through the same MFA door.
4. EWS delivery channel. Nothing sends until he names one.
5. FWD-10's portal source line to PROD, a client-facing push (CLAUDE.md PUSHES).

## Compiler Tools

| tool | result | note |
|---|---|---|
| git rev-list / git diff --quiet (portal, after fetch) | PASS | the overlap set and tree equality, measured by me before the waiver |
| open-calls.py close --decision approved | PASS | f936 |
| sha256sum on the COO halves | PASS | ce-4 binding |

What worked: measuring the overlap myself rather than taking the count. Gap: the portal tooling has no fold-back verb. R1 files it as a
surprise row.

-- 1.0.0_SA_CTO~DELL1
