# Never-widen sign-off packet -- the COT one-use arm, and window-8 amendment K12 (~D's ONE COT Performance read)

**Author:** `2.0.0_SA_COO~P`, 2026-09-27 ~04:0xZ. **Authority:** Andrew-direct "yes to all three", call 3 (record
`ANDREW_DIRECT_20260927_025xZ_YES_TO_ALL_THREE_P_OPEN_CALLS.md` @6039c2f680): re-arm ONE Cottonwood one-use
Performance plan for one signed-in COT run, sequenced after INF. **Halves asked:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`.
**Ledger:** `irpt-performance-cot-one-use-1-20260927`.

## 1. The plan (built with NO vendor call)

It is built by `cot_one_use_plan.py` (this folder, new) through the SERVED path's own functions:
`make_cot_mapping_loader` at the served cutoff 2026-09-23, the currency binding retained.py applies,
`bd_selected.requests_for` and `repository.digest`. The receipt is `COT_ONE_USE_PLAN_1_20260927.json` (no client
name in it).

| field | value | source |
|---|---|---|
| rule | served COT directory, not terminated, single-account entry; the mapping loads it and `requests_for` accepts it; the MEDIAN by opaque id (the COT directory carries no value field) | 258 entries -> 82 single-account -> 82 eligible, 0 refused -> rank 40 |
| account | `acc_81d92b2b7e971a76bac96cea` (vendor account 27436081) | the rule's pick |
| window | 2026-01-01..**2026-09-22** | end READ at build: the served `irpt-holdings` answer for the pick (selection sel_66e6034c..), `business_date`, as CTO 101756 ruled for INF |
| expires_at | 1790532000 = 2026-09-27T18:00:00Z | |
| sha256 | `22f0a98881b6db96e472cb8c39f203e9c5fd033d80d6a5260044dd7f31f287f0` | |

## 2. The arm, on 3a68bb2d's terms (window 8's INF arm, applied to COT)

- **When:** only after INF's plan 7f64b166 is SPENT (it is: claimed 04:11:14Z, one Orion call, RPT-df47a1fc) or disarmed, since the adapter holds ONE plan at a time
  (CTO 3a68bb2d item 3).
- **The arm-OFF pre-check first** (CRO 101776 / CTO c42d47163d): ~D, firm selector on Cottonwood, opens Performance
  on the account ONCE while the live plan is INF's (spent or disarmed). The HAR's account, start and end must equal
  the plan, and the adapter answers VendorEgressRefused with 0 vendor calls; both are recorded in the COT ledger
  BEFORE the arm. If only the start differs, re-cut to the page's start and write the new sha in the ledger before
  the arm; otherwise nothing arms.
- **The apply:** `-var-file` = this plan; the re-plan must be 0/1/0 with exactly `IRPT_PERFORMANCE_APPROVED_PLAN` +
  `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED`.
- **The session grants.** A read-only dry plan at 04:1xZ with this tfvars reads **1 add / 1 change / 1 destroy**:
  - add `aws_iam_role_policy.performance_approved_session[0]` = `irpt-performance-approved-session-policy`:
    `secretsmanager:GetSecretValue` on the ONE COT session secret (`data.aws_secretsmanager_secret.performance_cot_session`),
    which exists only while the armed plan names Cottonwood (`retained.tf:161-172`);
  - change the adapter's env (the two keys);
  - destroy `performance_approved_inf_session[0]` (INF's Orion session read), because firm_id moves from inflection
    to cottonwood.

  The live re-plan must read exactly this 1/1/1, or it stops.
- **Readback:** the env plan sha is 22f0a988 and the egress digest matches.
- **Rollback / disarm:**
  - re-apply the spent INF plan 01209afb, which restores INF's exhausted arm and its session policy;
  - if K12 did not claim before window 8's delete, do this the same tick.

## 3. Window-8 amendment K12 -- ~D's ONE COT Performance read

- **The act:** in window 8's already-logged-in page, firm selector Cottonwood, the plan's ONE account, Performance
  YTD (ending on the holdings as-of the page uses, 09-22). No new login and no new credential.
- **Vendor call, named:** ONE use of the plan = the BD `performancePeriod` request plus the `performanceSeries`
  request (`bd_selected.calculate`, 2 HTTP requests under ONE claim `PERFORMANCE_USE#22f0a988..`).
- **Writes:** the PERFORMANCE_USE# claim, and on success the retained COT report (REPORT#, ARTIFACT#, RETENTION# rows
  + blobs; the human-read path). KEPT.
- **Outcome:** READY/PARTIAL is COT's first signed-in journey (criteria 1 and 3). A named refusal is recorded. No
  retry: the plan is spent at the claim.

## 4. What the halves sign against

This file's committed blob; the COT plan (sha 22f0a988) and its build rule; the arm on 3a68bb2d's terms with its 1/1/1
(the COT session read added, the INF session read destroyed); the arm-OFF pre-check; and K12 as window 8's amendment (ONE use = 2 BD
requests, no retry).
