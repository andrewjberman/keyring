# Never-widen half requested -- R4 step 4: ENABLE the scheduled daily Holdings producer (DRAFT, filled Monday)

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **DRAFT, pre-staged 2026-09-26 ~19:3xZ.** Every `{{slot}}`
is filled from Monday's runs before this is sent. Nothing here is a measurement until its slot is filled.

Required by: CTO R4 sign-off (SIGNOFF_HOLDINGS_PRINCIPALS_DISPATCH_20260925.md @6c5c27a666), condition 4, "The enable
(R4 step 4) comes as its own half, naming the served daily move at 3 firms and the rollback per key". Also CTO msg
101343: the first publication's per-firm structural diff against the served revision, by class, each class traced to
its half, with any uncovered class named. And CTO msg 101360: the INF name census on that line.

## The act

Flip the EventBridge Scheduler schedule `irpt-holdings-snapshot` from DISABLED to ENABLED
(`cron(15 10 ? * MON-FRI *)` America/New_York, target `irpt-holdings-refresh-lambda`), in Terraform, through safe-apply,
under its own ledger. From then on, each weekday fire sends one SSM command per firm to the daily runner. Each firm
builds under its own principal and publishes one Holdings revision to the SERVED table. `latest` moves only on a
validated publication.

## Preconditions (each filled with its evidence)

| # | Precondition | Evidence |
|---|---|---|
| 1 | Negative arm N1 exercised (R4 condition 3): COT's principal REFUSED on opal-data-bd, 49F's REFUSED on opal-data-cot, each ALLOWED on its own directory | `r4_monday_negative_arm.py --read {{cid}}`: {{N1 4 of 4 lines}}; ledger irpt-holdings-principals-dispatch-m-20260925 leg N1 closed {{time}} |
| 2 | One QA fire: `aws lambda invoke --function-name irpt-holdings-refresh-lambda --payload '{"qa": true}'` (the QA mode added at 1eec202d22, ledger irpt-holdings-dispatch-qa-m-20260926 CLOSED) publishes to holdings_qa at all 3 firms, and the served index is untouched | per firm: SSM {{cid}} rc {{rc}}; holdings_qa revision {{rev}}; served index revision before/after {{same}} |
| 3 | The first publication's diff against the served revision, by class (`account_mask_publication_diff.py dry --pin-served` and `holdings_publication_diff_classes.py`, the QA candidate at the fire's as_of {{as_of}}) | table below; first read @707490f568 |
| 4 | INF name census on the QA candidate (0 personal data, or each hit dispositioned) | {{count}}; first read @6be843ee44: 0 email-like, 8 security identifiers |

## What the first scheduled publication moves (by class, per firm)

As of the first read (served 09-22, pinned) and Monday's re-run at {{as_of}}:

| Class | 49F | INF | COT | Traced to |
|---|---|---|---|---|
| Node set (added / removed) | {{0 / 0}} | {{0 / 0}} | {{0 / 0}} | -- (0 at the first read) |
| Amounts / percentages | {{0}} | {{0}} | {{0}} | -- (0 at the first read) |
| Clocks | {{n}} | {{n}} | {{n}} | the new business date itself (a later as_of than the served 09-22) |
| ACCOUNT `display.label` | {{2,970}} | {{562}} | {{595}} | own-mask half: CTO @45bafa24a1, CRO @c412578ede |
| Classification (asset_class / sub / basis) | {{64/108/109}} | {{1,464/1,414/1,696}} | {{323/1,175/1,693}} | batch A (CTO @8214723353); COT-new Part 1 (CTO @ab4a2e41bb, which deferred Holdings to THIS half); Part 2 if written first (@ab4a2e41bb) |
| `company=` + SECURITY display name | {{67}} | {{30,881}} | 0 | 49F: CTO R5 decision 4 (cb8cd03113). INF: e0f680f0df, admitted as its own line by CTO 101360 under the census in precondition 4 |

A later as_of also brings real custody movement (new trades, prices and accounts). That is the producer's ordinary daily
output, not a code change. It is named per firm as {{accounts / nodes / $}} against the served revision.

## Blast radius and rollback

- **Touches:** the schedule's State; one Holdings revision per firm per weekday in each firm's served table.
- **Does not touch:** the directory, bd-securities, any COT/BD gold output, the portal.
- **Rollback per key:** (a) set the schedule to DISABLED (Terraform); (b) per firm, repoint the served index to the
  prior revision, which is retained with its manifest and version-pinned source objects.

## The ask

Sign or refuse. The CTO has said it signs on arrival with Monday's pinned re-run (msg 101360). 4.0.0_SA_CRO reads the
same diff.
