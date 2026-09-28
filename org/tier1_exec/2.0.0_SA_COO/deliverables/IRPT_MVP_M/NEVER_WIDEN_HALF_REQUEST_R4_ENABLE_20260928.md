# Never-widen half requested -- R4 step 4: ENABLE the scheduled daily Holdings producer (FILLED 2026-09-28, NOT SENT)

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. Filled by `0.9.0_WK_IRPT_BCKEND~42` (TO-IB-mr-2) from
this session's own measurements, 2026-09-28 ~19:1x-19:3xZ. **Precondition 2 did NOT pass: the QA fire failed at all
three firms (surprise row IRPT_BCKEND-W42-S1, BLOCKING/ARMED). This half is filled honestly with that failure, not
sent, and not ready to sign as written** -- the issuer (2.0.0_SA_COO~M) decides whether to re-fire after S1's disarm
or hold the enable.

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
| 1 | Negative arm N1 exercised (R4 condition 3): COT's principal REFUSED on opal-data-bd, 49F's REFUSED on opal-data-cot, each ALLOWED on its own directory | DONE, not re-run. Ledger `irpt-holdings-principals-dispatch-m-20260925` CLOSED @26127abf10 (all 4 legs). Leg N1: 2026-09-28T13:5xZ SSM `da369659-c8ab-4fa3-8ddb-fa2224d8ff35` on the daily-runner host (i-02448edb624a7a7cf), run as each firm principal via `r4_monday_negative_arm.py`: irpt-cot-holdings-role on opal-data-bd REFUSED; irpt-49f-holdings-role on opal-data-cot REFUSED; positive controls irpt-cot-holdings-role on opal-data-cot ALLOWED and irpt-49f-holdings-role on opal-data-bd ALLOWED -- 4 of 4 match (status Success), closed 20260928T135856Z |
| 2 | One QA fire: `aws lambda invoke --function-name irpt-holdings-refresh-lambda --payload '{"qa": true}'` publishes to holdings_qa at all 3 firms, and the served index is untouched | **NOT MET.** One fire this session (2026-09-28 19:30:55Z), the only one: `lambda.invoke(FunctionName='irpt-holdings-refresh-lambda', Payload=b'{"qa": true}')` -> first call `RUNNER_OFFLINE_START_ISSUED` (host was stopped), `ssm.describe_instance_information` Online within 1s, second call `DISPATCHED`. Per firm: 49financial SSM `10a22d91-5462-4da6-b241-841be0796b51` rc=1 Failed (AccessDenied: assumed-role irpt-49f-holdings-role lacks s3:GetObjectVersion on `opal-data-assets/gateway/49financial/bronze/taxsma_workbook_projection/date=2026-09-23/...`); cottonwood SSM `415f085f-24a5-43fa-b565-fa7b341dc927` rc=1 Failed (same shape, irpt-cot-holdings-role on `opal-data-assets/blackdiamond/cottonwood/silver/fact_model_assignment/date=2026-09-28/data.parquet`); inflection SSM `a0f8059e-ac39-4ce7-9bc2-292ef6afd857` rc=1 Failed (`ModuleNotFoundError: No module named 'lib.silver_ids'` -- the re-minted bundle's closure, `.tools/safe_deploy_core.py` `_IRPT_HOLDINGS_CLOSURE`, does not carry `lib/silver_ids.py`). holdings_qa revision published: **none, at any firm** (`holdings_qa/current/manifest.json` is a 404 at all 3 firms, read after the fire). Served index revision before/after: EQUAL at all 3 firms -- 49financial `OqjgF6qs7e5QsF7HScOre54hxJ18Ktgf`=`OqjgF6qs7e5QsF7HScOre54hxJ18Ktgf`; inflection `ipomYxTGLoE0pAgeh.nNtVJ6QUm5ynJG`=`ipomYxTGLoE0pAgeh.nNtVJ6QUm5ynJG`; cottonwood `ykQofbha2WKbcHFKvxMThBs0UNC_g9ji`=`ykQofbha2WKbcHFKvxMThBs0UNC_g9ji` (untouched, as expected of a refused build). Surprise row `IRPT_BCKEND-W42-S1` (BLOCKING, ARMED; disarm owners CTO for the closure gap, COO~M for the IAM grant). Re-minted members-sha256 this fire ran against: `a2866ed29a82318385469985f53fbdebcc59ff4b718c3360a0a6568a2728961f` (40 members/firm; ledger `irpt-holdings-packages-m-20260928` CLOSED, commit `850c6bbc52`) |
| 3 | The first publication's diff against the served revision, by class (`account_mask_publication_diff.py dry --pin-served` and `holdings_publication_diff_classes.py`, the QA candidate at the fire's as_of) | **BLOCKED, cannot run as written**: precondition 2 published no holdings_qa candidate at any firm (no JSON to diff). The nearest available read is the PINNED re-run at the SERVED date on today's code, already on file: `R4_ENABLE_DIFF_20260928/README.md` (2.0.0_SA_COO~M, ~14:0xZ, code de306d972f6/a57537bd8a on CLOUD) -- table below reproduces it. It is NOT a diff of this QA fire's own candidate (none exists); first read (09-22) @707490f568 |
| 4 | INF name census on the QA candidate (0 personal data, or each hit dispositioned) | **BLOCKED, same cause**: no INF holdings_qa candidate was published to census. Last known read, `R4_ENABLE_DIFF_20260926/README.md` Addendum 1 (pinned INF candidate, revision b681cc8d..., business date 2026-09-22): 30,881 SECURITY nodes scanned, 0 email-like tokens, 8 distinct 6+-digit-run texts (security product codes / pre-corporate-action tickers), all dispositioned SAFE. Not re-run on this fire's candidate (none exists); first read @6be843ee44 |

## What the first scheduled publication moves (by class, per firm)

**Source: the pinned re-run at the served date, `R4_ENABLE_DIFF_20260928/README.md` (2.0.0_SA_COO~M, ~14:0xZ, code
d306d972f6 cash-line + a57537bd8a UIC-16 on CLOUD), NOT this fire's own QA candidate -- precondition 2 failed before
any candidate published. as_of: not observable -- every command's log ends inside the builder before the business-date
line prints (49F/COT: AccessDenied inside `retained_capture`/`_read_parquet`; INF: ModuleNotFoundError at import,
before `build_snapshot` runs at all).**

| Class | 49F | INF | COT | Traced to |
|---|---|---|---|---|
| Node set (added / removed) | 0 / 0 | 0 / 0 | 0 / 0 | -- (0 at the first read and the 09-28 pinned re-run) |
| Amounts / percentages | 0 | 0 | 0 | -- (0 at the first read and the 09-28 pinned re-run) |
| Clocks | 0 (pinned to served 09-22) | 0 (pinned to served 09-22) | 0 (pinned to served 09-22) | the new business date itself, only on an UNPINNED live fire (none succeeded this session) |
| ACCOUNT `display.label` | 2,970 | 875 | 755 | own-mask half: CTO @45bafa24a1, CRO @c412578ede; INF/COT rose from the first read (562/595) because UIC-16's full account type now changes labels the old 24-char cut or uppercasing had left alone |
| Classification (asset_class / sub / basis, incl. cash-line) | 123 | 30,881 | 2,577 | batch A (CTO @8214723353); COT-new Part 1 (CTO @ab4a2e41bb, deferred Holdings to THIS half); COT's 2,577 includes the Holdings cash-line rule on BD's own `CASH -- CASH` rows (COT gold half of the cash-line act is HELD, CTO 102293/102323) |
| `company=` + SECURITY display name | 67 | 30,881 | 0 | 49F: CTO R5 decision 4 (cb8cd03113). INF: e0f680f0df, admitted as its own line by CTO 101360 under the census in precondition 4 |

Three lines from the code now on CLOUD (not yet exercised live -- precondition 2 did not reach a publish):
- **Cash-line rule** (`classify_security` on `display.description`, `CASH -- CASH` -> `cash`, d306d972f6): its per-firm
  count is folded into the Classification column above (the diff tool does not break it out separately) and is **NOT
  separately measured from a QA candidate** -- no candidate published this session. The pinned 09-28 README names it
  as included in COT's 2,577; 49F and INF counts are not distinguished from their other classification changes.
- **UIC-16** (the account type in full, a57537bd8a): INF only (labels rose 562 -> 875); 49F keeps its Schwab codes
  unchanged (label count steady at 2,970 across both reads).
- **ETF Part A** (16 keys incl. VNQ -> alternatives; CTO @c516dab84b): a static classifier-table change, not a
  QA-candidate measurement; folded into the Classification column wherever a rebuilt SECURITY node's asset class
  changed.

A later as_of also brings real custody movement (new trades, prices and accounts). That is the producer's ordinary
daily output, not a code change. Not named per firm here because no fire this session reached a live as_of.

## Blast radius and rollback

- **Touches:** the schedule's State; one Holdings revision per firm per weekday in each firm's served table. The code
  the schedule would run: the re-minted standalone packages, members-sha256
  `a2866ed29a82318385469985f53fbdebcc59ff4b718c3360a0a6568a2728961f` (40 members/firm, off the 2026-09-25 mint's
  `83f6a81aab34...`; ledger `irpt-holdings-packages-m-20260928` CLOSED, commit `850c6bbc52`).
- **Does not touch:** the directory, bd-securities, any COT/BD gold output, the portal;
  `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` (the directory chain's
  own bundle, ETag `4155283a1b77394259ff809611f28a8e`, read unchanged this session) -- UIC-16's directory side waits on
  2.0.0_SA_COO~P's next directory package, not this half.
- **Rollback per key:** (a) set the schedule to DISABLED (Terraform); (b) per firm, repoint the served index to the
  prior revision, which is retained with its manifest and version-pinned source objects.

## The ask

**NOT SENT.** Precondition 2 failed at all three firms this session (surprise row `IRPT_BCKEND-W42-S1`); preconditions
3 and 4 could not be run against a QA candidate because none was published. The issuer (`2.0.0_SA_COO~M`) decides
whether to disarm S1 (bundle closure + IAM grant) and re-fire before sending this half, or hold. The CTO said it signs
on arrival with the pinned re-run (msg 101360) -- that re-run is reproduced above, but it is not a QA-fire-live diff and
precondition 2 as the CTO's own condition 3/4 named it is unmet.
