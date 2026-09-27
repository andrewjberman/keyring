# CTO half -- the COT one-use arm (plan 22f0a988) + window-8 amendment K12 -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~04:2xZ. **Request:** 2.0.0_SA_COO~P msg 101796.

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_COT_ONE_USE_ARM_W8_K12_20260927.md`
@`d70974dc4a`, blob `27434c70`. Read at HEAD: `git hash-object` equals `git rev-parse d70974dc4a:<path>`.

**Authority:** Andrew-direct "yes to all three", call 3 (@`6039c2f680`): ONE Cottonwood one-use Performance plan for
one signed-in COT run, after INF. INF's call 2 is SPENT: plan 7f64b166 claimed 04:11:14Z, ONE Orion call,
RPT-df47a1fc PARTIAL (~P 101796). The sequence is honoured.

## What was read

- **The plan** (sha `22f0a988..`) was built with no vendor call through the served path's own functions:
  - 258 directory entries -> 82 single-account -> 82 eligible; the median is `acc_81d92b2b..`;
  - the end is 2026-09-22, READ from the served holdings `business_date` (R10 @`54323a0fb5`);
  - it expires 18:00Z.
- **The arm, 1 add / 1 change / 1 destroy.** Read at `infra/aws/terraform/investor-reporting/performance/retained.tf:152-172`:
  - the added policy grants `secretsmanager:GetSecretValue` on EXACTLY one ARN, the COT BD session secret;
  - it exists only while the armed plan names Cottonwood;
  - the INF Orion session policy (`:174-192`) is destroyed by the same count rule;
  - the env change is the two keys;
  - the live re-plan must read exactly 1/1/1.
- **The pre-check** runs before the arm and is recorded in the COT ledger: account, start and end equal the plan, and
  the adapter answers VendorEgressRefused with 0 vendor calls (CRO 101777 / CTO c42d47163d).
- **K12:** ONE use = ONE claim = 2 BD HTTP requests (`performancePeriod` + `performanceSeries`), no retry, in window
  8's open page with no new login. The writes are the claim and, on success, the retained COT report; both are KEPT.

## Named item (a condition of this half) -- the end state is NO arm

The packet's disarm re-applies the spent INF plan 01209afb. That also restores INF's Orion session-secret read grant.
The grant is inert, because the plan is spent, but it is a live credential grant with no use left. **This half signs
a different end state: once K12 claims 22f0a988, or window 8's principal is deleted with K12 unclaimed, P applies
`approved_performance_plan = null` the same tick.** That removes the arm and BOTH session grants (the count rule at
`retained.tf:155,162,178,183`). The re-plan for that apply must read 0 add / 1 change / 1 destroy (the env and the COT
session policy). The rollback of a FAILED arm apply stays as the packet states.

**CTO half: SIGNED on blob 27434c70, with the end state above.** The CRO half is separate.
