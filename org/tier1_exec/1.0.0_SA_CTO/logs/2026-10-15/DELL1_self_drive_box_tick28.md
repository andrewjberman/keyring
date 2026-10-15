# /self-drive dell1 box open calls -- tick 28 (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~01:27Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17). **state: ARMED**
Covers the window since tick 27 (@06ae738014, 00:27Z).

## Measured (01:26Z)

- **Box list:** rows=85, **open=1**: `a196`. It is to be WITHDRAWN as superseded once the amended CN-p-2 row lands.
- **Inbox:** 0 unread. Msg 5968 was acked.

## Andrew-direct (relayed by `2.0.0_SA_COO~D1`, msg 5968)

- "It looks good! ... Only thing is need rollforwards for the the Custom Models. This is good though, let's get that sorted for PROD now".
  Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261015_01xxZ_COO_D1_TREND_LOOKS_GOOD_CUSTOM_ROLLFORWARD_THEN_PROD.md` @9fbada016d.
- **Applied:**
  - CN-p-2 AMENDMENT 2 (Custom carries its last value) was cut @d944c67b7f and drained @0fe75c0756. This is consistent with PRD v2.21 override (c).
  - Plan: ~D1 renders and registers the new row. This seat closes it `--by andrew --ruled-by andrew --decision approved` on his record, and closes `a196` withdrawn.
  - ~D1 then runs the merge-forward and orders DT~H1 to make a chosen-set release on PROD 5d64641891.

## Completion test

Box scope: **NOT DONE**. The stop is Andrew's stand-down. REACHABLE 0. HELD 1 (`a196`, superseded on arrival of the new row).

## ACTS ONLY ANDREW CAN DO (cited)

- None open now. His client-facing word for the amended head is given (record above). Carried: the restart window; the SECCLASS BD Mix push; the gateway session; the ASTN FT hold; ADVI_BILLING's answers; G4.

## Compiler Tools

`open-calls.py list`; `check_inbox`; `git log --since`.

-- 1.0.0_SA_CTO~DELL1
