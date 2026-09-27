# Never-widen sign-off packet -- the INF Orion one-use arm, and window-7 amendment 3 (~D's ONE INF Performance read)

**Author:** `2.0.0_SA_COO~P`, 2026-09-27 ~03:0xZ. **Authority:** Andrew-direct "yes to all three", call 2 (record
`ANDREW_DIRECT_20260927_025xZ_YES_TO_ALL_THREE_P_OPEN_CALLS.md` @6039c2f680): ONE new Orion one-use Performance call
on a single-account-household INF client, YTD, used in one signed-in window. **Halves asked:** `1.0.0_SA_CTO` and
`4.0.0_SA_CRO`. **Ledger:** `irpt-performance-inf-one-use-3-20260927`.

## 1. The plan (built with NO vendor call)

`inf_one_use_plan.py --tree <backend worktree>`: the worktree's `orion_selected` / `orion_account_mapping` /
`orion_live` blobs equal the served a7e9f51c77. The stated rule is: not terminated, a single-account Orion household
(S143), in accounts_v2 at the 2026-09-23 cutoff, active, not sweep/sleeve, opened before the window, and the 75th
percentile of value.

| field | value |
|---|---|
| account | `acc_5510a3054a409d548a12c57d` (the rule's pick; the same client as the spent plan 01209afb, INF REPORT# = 0, so nothing is retained for it) |
| window | 2026-01-01..2026-09-25 (the trading frontier: 09-27 is a Sunday) |
| expires_at | 1790510400 = 2026-09-27T12:00:00Z |
| mapping_revision | 3ab7f2bd.. (the served mapping at cutoff 2026-09-23) |
| plan sha256 | `f0de098fddaca8b44ae7aec55f65cf762194e24998f6ad020aa43dd54144619d` |

## 2. The arm (a served move)

Apply `infra/aws/terraform/investor-reporting/performance` with `-var-file` = this plan. The plan read 0/1/0 on
`module.irpt_performance_adapter.aws_lambda_function.this`, environment only:
- `IRPT_PERFORMANCE_APPROVED_PLAN`: 01209afb (SPENT) -> f0de098f;
- `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED`: its digest.

**No code change.** `performance_approved_inf_session[0]` (the Orion session read) is unchanged: firm_id stays
inflection.

- **Rollback:** re-apply with the spent plan's value (the live env today), which restores an exhausted arm; or
  `approved_performance_plan = null`, which removes the arm and its session grant.
- **Spend:** the adapter's one-use gate claims `PERFORMANCE_USE#f0de098f..` on the FIRST matching read, and every
  later read of that plan is refused.

## 3. Window-7 amendment 3 -- K11: ~D's ONE INF Performance read in the open page

- **The act:** in window 7's already-logged-in page (principal irpt-uiwalk-1790477665), ~D selects the plan's ONE
  INF account and opens Performance with the page's YTD preset ending 2026-09-25, if the page allows it. Otherwise
  ~D reads the window the plan names.
- **Two requests:** the page's `POST /selections` (K3) and ONE `GET .../performance/{accountSetId}`. Both are in
  window 7's admitted route classes.
- **Vendor call, named:** exactly ONE Orion Performance request from the adapter, spending plan f0de098f.
- **Writes:** the PERFORMANCE_USE# claim row, and on success the retained INF report (REPORT#, ARTIFACT#,
  RETENTION# rows + blobs in the human-read path); both KEPT.
- **Outcomes, each recorded as the result:**
  - READY / PARTIAL: the first INF signed-in journey, criterion 1.
  - A named refusal: recorded. **No retry:** the plan is spent at the claim.
- **Order:** after the arm's readback, and inside window 7's life. It needs no new login and no new credential.
- **K9 carries:** a second read of the same account and window reopens the retained report (no vendor call).

## 4. What the halves sign against

This file's committed blob: the plan in section 1 (sha f0de098f), the env-only arm in section 2 with its rollback,
and K11 as window 7's amendment 3 (ONE read, ONE Orion call, no retry).
