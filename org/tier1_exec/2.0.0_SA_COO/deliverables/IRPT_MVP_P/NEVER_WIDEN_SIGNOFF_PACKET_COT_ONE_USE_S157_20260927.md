# Never-widen sign-off packet -- ONE corrected COT Performance use (IRPT_BCKEND-S157), by direct IAM invoke

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~15:3xZ.
**Ledger (opened before any write):** `irpt-performance-cot-one-use-s157-20260927`.
**Authority:** Andrew-direct, relayed by 0.0.0_AB_MSTR 101850: "they have egress for full session". CTO 101854 ruled that
it reaches P's Performance vendor uses, each under both halves and a ledger.

This packet is the COT one-use arm packet (`NEVER_WIDEN_SIGNOFF_PACKET_COT_ONE_USE_ARM_W8_K12_20260927.md`, blob
27434c70, signed CTO @cd91ef7c0e and CRO @49a2ab81bd) with only the deltas below. It carries:
- ONE use = the BD `performancePeriod` request plus the `performanceSeries` request under ONE claim;
- no retry;
- the end state `approved_performance_plan = null` (no live session grant);
- the audit: BD requests counted from the claim's retained provider evidence (exactly 2), and COT REPORT# +1 at most.

## S157-1 -- why

COT's first retained report RPT-b683f188 states its actual window as 01-02..09-22 over a series that starts 07-21. The
cause is fixed for new reports in adapter bOefL9nx (actual_start = the account's first series point). Replaying the
recorded bytes gives 07-21, but criterion 3 ("window disclosed") has no REAL-DATA report computed by the fixed code.
This use produces one.

## S157-2 -- the plan (built with NO vendor call)

`cot_one_use_plan.py --end-before-holdings 2026-09-21`, receipt `COT_ONE_USE_PLAN_3_S157_20260927.json`:

| field | value |
|---|---|
| account | `acc_81d92b2b7e971a76bac96cea` (vendor 27436081), the same rule pick as plan 1 (rank 40 of 82) |
| window | 2026-01-01..**2026-09-21** |
| expires_at | 1790575200 = 2026-09-28T06:00:00Z |
| sha256 | `63cf95e9defc2385c7314f193cf211ea5a6d25a3426ece07654b7bcf8d31fb44` |

**The end is a DELIBERATE DEPARTURE** from "end = the served holdings as-of" (09-22), stated in the receipt. Measured
12:29:54Z (`COT_S157_PRECHECK_20260927.json`): the 01-01..09-22 window REOPENS retained RPT-b683f188 through the
PERFORMANCE_ACCEPTED pointer, which is keyed by selection and window, so it would never reach the gate and a plan on it
would never be spent. 09-21 has no retained report.

## S157-3 -- the read, by direct IAM invoke (no walk principal)

`cot_direct_read.py <phase> <out> 2026-09-21` invokes irpt-directory-search (the selection) and
irpt-performance-adapter with the edge's trusted header set, as the synthetic internal viewer V1
(reopen-arm-1@opal.test). That is the same boundary and subject as `reopen_authz_arm.py`, used under earlier signed
packets. No admin principal is created. The retained report's owner is V1's principal row.

1. **Plan-OFF pre-check, DONE (15:23:49Z):** `COT_S157_PRECHECK_PLAN3_20260927.json`. The answer was
   UNAVAILABLE/DEPENDENCY_UNAVAILABLE with no report. The adapter logged VendorEgressRefused 'matching current
   server-approved performance use required', and cottonwood PERFORMANCE_USE# rows stayed at 2 (0 vendor calls).
2. **The arm:** dry plan with this tfvars at 15:2xZ reads **1 add / 1 change / 0 destroy**. It adds
   `performance_approved_session[0]` (GetSecretValue on the ONE COT session secret, blackdiamond/cot/session) and adds
   exactly the two env keys `IRPT_PERFORMANCE_APPROVED_PLAN` and `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED`. The code is
   unchanged; the hash reads "known after apply" only through the data read, as on every earlier arm. The live re-plan
   must read exactly this, or it stops. Readback: env plan sha 63cf95e9 and the egress digest equal.
3. **The ONE read:** `read`. The outcome is READY/PARTIAL with a retained report, or a named refusal. No retry.
4. **ONE reopen:** `reopen`, which is the same retained report with no vendor call.
5. **Disarm the same tick:** `approved_performance_plan = null`, re-plan **0/1/1** (the env and the COT session
   policy destroyed).

## S157-4 -- what the read must show (the point of it)

The new report's `dates.actual_start` is the account's first series point (expected 2026-07-21, not 01-02), with the
actual end on or before 09-21 and the series' first date equal to the actual start. If it shows 01-02, the fix is not
working on real data: a BLOCKING row the same tick.

## What the halves sign against

This file's committed blob; blob 27434c70's terms as amended here; plan 63cf95e9 with its stated end departure; the
direct-invoke read as V1; the 1/1/0 arm and the 0/1/1 disarm to null.
