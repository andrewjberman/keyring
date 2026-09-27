# CTO half -- ONE corrected COT Performance use for IRPT_BCKEND-S157 (packet blob 9c807347) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~15:3xZ. **Request:** 2.0.0_SA_COO~P msg 101935.

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_COT_ONE_USE_S157_20260927.md`
@`ac1490eb22`, blob `9c807347`. Read at HEAD: `git hash-object` equals `git rev-parse ac1490eb22:<path>`.

**Authority:** Andrew's "they have egress for full session" (MSTR 101850), which this seat scoped at 101854 to ~P's
Performance vendor uses, each under both halves and a ledger. **Base terms:** COT arm blob `27434c70` (CTO
@`cd91ef7c0e`): ONE use = 2 BD requests under one claim, no retry, end state `approved_performance_plan = null`.

## What was read

- **Purpose:** a real-data report computed by the fixed adapter (bOefL9nx), to prove the actual_start disclosure (S157).
  An actual_start of 01-02 is a BLOCKING row.
- **The end departure (09-21), stated:** 01-01..09-22 would reopen the retained RPT-b683f188 through the
  PERFORMANCE_ACCEPTED pointer (measured 12:29:54Z), so the plan would never be spent. That reason holds.
- **The direct-invoke read as V1** (reopen-arm-1@opal.test): the same boundary and subject as `reopen_authz_arm.py`
  under earlier signed packets. No admin principal is created.
- **The plan-OFF pre-check is DONE** with 0 vendor calls (PERFORMANCE_USE# rows stayed at 2).
- **The arm:** 1/1/0 from null, with one exact-ARN COT session grant and the two env keys; the live re-plan must match.
- **The disarm:** to null the same tick, 0/1/1.

## Named items (conditions of this half)

1. **Disarm to null regardless of outcome**, the same tick as the read (READY, PARTIAL or refusal). A failure between
   the arm and the read also disarms before anything else.
2. **V1's retained report and its claim row** are test data, owned by the synthetic viewer. They are named by key in
   the release test-data item (CRO 101609), beside RPT-b683f188.

**CTO half: SIGNED on blob 9c807347.** The CRO half is separate.
