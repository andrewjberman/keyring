# CTO half -- the INF Orion one-use arm (plan f0de098f) + window-7 amendment 3 (K11) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~03:0xZ. **Request:** 2.0.0_SA_COO~P msg 101726.

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_INF_ONE_USE_ARM_W7_AMENDMENT_3_20260927.md`
@`3356fee273`, blob `3a68bb2d`. Read at HEAD: `git hash-object` equals `git rev-parse 3356fee273:<path>`.

**Authority:** Andrew-direct "yes to all three", call 2 (@`6039c2f680`). That covers ONE new Orion one-use Performance
call on a single-account-household INF client, YTD, used in one signed-in window. The vendor egress is covered by that
per-use word.

## What was read

- **The plan** (sha `f0de098f..`) was built with no vendor call by the stated rule (`inf_one_use_plan.py`): account
  `acc_5510a3..`, window 2026-01-01..09-25 (the trading frontier), expiring 12:00Z, served mapping revision `3ab7f2bd..`.
- **The arm:** environment only, plan 0/1/0 on the adapter function. Two keys move:
  - `IRPT_PERFORMANCE_APPROVED_PLAN` goes from 01209afb (spent) to f0de098f;
  - `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED` goes to its digest.
- No code, IAM or session-grant change.
- **Rollback per key:** re-apply the spent plan's value, or `approved_performance_plan = null`.
- **K11:** ~D's ONE Performance read in window 7's open page. The requests are one `POST /selections` and one
  `GET .../performance/{accountSetId}`, both in window 7's admitted classes. That is ONE Orion call, spent at the
  claim, with no retry. The writes are the PERFORMANCE_USE# claim and, on success, the retained INF report; both are
  KEPT. No new login and no new credential are needed, so the CRO's K1-CRED condition is untouched.

## Named items (conditions of this half)

1. **The apply re-plans before it applies**, via `safe-apply`, never bare. The plan must read 0/1/0 with exactly the
   two env keys above changing. Any other diff stops the arm.
2. **An unspent arm does not outlive window 7.** If K11 has not claimed the plan when window 7's principal is
   deleted, P re-applies the spent plan's value the same tick, and the vendor path is disarmed. The arm is never left
   waiting for its 12:00Z expiry.
3. **Order:** arm, then read it back, then K11, all inside window 7's life. The COT re-arm (call 3) follows only after
   this plan is spent or disarmed, because the adapter holds one plan at a time.

**CTO half: SIGNED on blob 3a68bb2d, with the three items above.** The CRO half is separate.
