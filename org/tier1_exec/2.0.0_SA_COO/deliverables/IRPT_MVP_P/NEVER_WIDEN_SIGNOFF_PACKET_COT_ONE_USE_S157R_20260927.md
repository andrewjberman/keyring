# Never-widen sign-off packet -- the S157 COT use AGAIN, on the refreshed session (a new signed use)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~20:3xZ.
**Ledger (opened before any write):** `irpt-performance-cot-one-use-s157r-20260927`.
**Why now:** CTO 102044 item 2: "re-arm S157 as a new signed use when you choose". 0.6.2_AE_PartnerETL~S 102034 /
TO-IB-s158 complete (@fe23038617): `blackdiamond/cot/session` AWSCURRENT is **9da4e781**, created
2026-09-27T18:42:27.771Z by document Success cf7fdead.

This packet is the S157 packet (`NEVER_WIDEN_SIGNOFF_PACKET_COT_ONE_USE_S157_20260927.md`, blob 9c807347, both halves)
with ONLY the deltas below. Every other term reads as S157's, including:
- ONE use = `performancePeriod` + `performanceSeries` under ONE claim, with no retry;
- the direct IAM invoke as V1 (reopen-arm-1@opal.test);
- the audit: BD requests counted from the claim's retained provider evidence (exactly 2), and COT REPORT# +1 at most;
- disarm in the same tick to `approved_performance_plan = null`;
- S157-4's test: the new report's `actual_start` is the account's first series point (expected 2026-07-21), and 01-02
  there is a BLOCKING row.

## S157R-1 -- what happened to the first use

Plan 63cf95e9's claim was spent at 15:41:03Z. The provider refused with BDRequestFailed (HTTPError), because the
session secret dated from 09-16. No report was retained; the plan was disarmed to null (ledger CLOSED 15:45:05Z).
Row S158 found the cause (the refresh document had failed since 09-24) and TO-IB-s158 fixed it. A spent claim is
never reused, so this is a NEW plan.

## S157R-2 -- plan 4 (built with NO vendor call)

`cot_one_use_plan.py --end-before-holdings 2026-09-21`, receipt `COT_ONE_USE_PLAN_4_S157R_20260927.json`:

| field | value |
|---|---|
| account | `acc_81d92b2b7e971a76bac96cea`, the same rule pick (rank 40 of 82 eligible) |
| window | 2026-01-01..**2026-09-21**, the same stated departure as plan 3 |
| expires_at | 1790560800 = 2026-09-28T02:00:00Z, before MSTR's 03:00Z freeze |
| sha256 | `b20d69b2f3e3784ebb698b0146574c8bba10db22e7a7114dba38330bea5d73c7` |

**The departure still holds, re-measured:**
- The default rule re-read at 20:1xZ gives end 09-22 (the served holdings as-of did not move with today's chain run),
  and 01-01..09-22 reopens retained RPT-b683f188.
- 01-01..09-21 has no retained report, because the first use retained none.

## S157R-3 -- measured before the arm

1. **Plan-OFF pre-check** (20:21:36Z, `COT_S157R_PRECHECK_PLAN4_20260927.json`): UNAVAILABLE/DEPENDENCY_UNAVAILABLE,
   no report. The adapter logged VendorEgressRefused (3 lines in the 5-minute read), so 0 vendor calls.
2. **Adapter:** live CodeSha `bOefL9nx..` with plan and egress env both null. The S3 artifact
   `investor-reporting/irpt-performance-adapter.zip` (version 8uohgNwE.) carries content-sha256 `bOefL9nx..`, so the
   arm's "known after apply" code read moves NO code.
3. **Dry plan with plan 4's tfvars** (performance root, backend worktree): **1 add / 1 change / 0 destroy**. It adds
   `performance_approved_session[0]` and exactly the two env keys `IRPT_PERFORMANCE_APPROVED_PLAN` and
   `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED` (b20d69b2..). The live re-plan must read exactly this, or it stops.

## S157R-4 -- order and timing

Arm -> ONE read -> ONE reopen -> disarm, all in one tick, and all before 02:00Z (the plan's expiry) and clear of the
03:00Z freeze. This act uses no walk principal and does not overlap window 18's K7 (a 49F read on the internal engine).

## What the halves sign against

This file's committed blob; blob 9c807347's terms as amended here; plan b20d69b2 with its re-measured end departure;
the 1/1/0 arm with the no-code-move read; and the disarm to null in the same tick.
