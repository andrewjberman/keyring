# /self-drive laptop directives -- ticks 29-30 (2026-09-29 12:57Z-13:27Z)

**archetype:** COORDINATE

Arming record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_230xZ_SELF_DRIVE_LAPTOP_FABRIC.md`
@`9549fd3b32`; cron `f02c52db`. **state: ARMED**

## Served this interval

- **Resident st4 LIVE** at 12:31Z (`4af16f7879`; root fe64236bbb-st4, worker 5288ff5a; 0 restarts).
- **HoldingsSnapshot CATEGORY contract** and **S132 edge-role public keys**: both ledgers CLOSED (`a951227bc7`), each
  on the CRO's signed-in page read.
- **Window 22 OPEN** (`062c9e8dea`): the first Analysis on st4, five bodies, one principal.

## Acts

- **W22 half SIGNED** `3b209c072c`. The unpinned adapter is sound: the ycharts tree has 0 performance-Lambda callers,
  with a positive control. Conditions: Y3 reads the NEEDS_CORRECTION row; any DLQ growth is BLOCKING. The DLQ holds 1
  pre-existing message, per the CRO.
- **AD-10 half SIGNED** `ee4bc93257`. Portal PROD's `directory-browse.ts:15` throws on an unlisted key, and the
  directory runner fires on weekdays (`schedule.tf:75,394`). Condition: the step-3 bundle deploy waits for a read of
  the served portal PROD bundle admitting `account_masks`.
- **Portal DEV 18899c96 APPROVED**: a wire type only; the header sha256 equals the schema at `bb145ff1fe`. It is now on
  origin DEV (`c90ab2e921`).
- **AD-10 step 1 half SIGNED** `797a4c8c0a`: the contract copy into directory-search + generate, applied after W22.
  The CRO signed too (`3efef80e48`).

## State

54 open TOs across 9 laptop directives. COO AT CAP (~D, ~M, ~P); MDPF_CANON and ADVI_FIRMBKTS NEEDS-SLOT. Inbox 0.
Pending on others: W22 terminal states; 49F r3 re-switch halves on TBy0pL; INF adapter switch (pr-221 code drained
`b917320dca`, apply owes every-period-cold census); R4's first scheduled Holdings fire at 14:15Z.

## At Andrew (acts only)

- The word for the portal PROD hotfix of 6c163889 + 27eae57a. It now also gates AD-10 steps 2-4.

## Compiler Tools

- None new.
