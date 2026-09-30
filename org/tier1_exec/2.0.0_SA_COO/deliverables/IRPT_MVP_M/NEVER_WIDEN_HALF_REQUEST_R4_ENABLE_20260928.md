# Never-widen half requested -- R4 step 4: ENABLE the scheduled daily Holdings producer (FILLED 2026-09-28, NOT SENT)

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. Filled by `0.9.0_WK_IRPT_BCKEND~42` (TO-IB-mr-2) from
this session's own measurements, 2026-09-28 ~23:3xZ (re-fire after amendments 1-3: the read-version grant on the
READ statements, the closure re-trace + 49F memory cut, and the own-prefix read-version grant on `PublishOwnHoldings`).
**Precondition 2 now PASSES: one QA fire reached Success at all three firms** (superseding the two prior failed
fires recorded in surprise rows `IRPT_BCKEND-W42-S1` and the amendment-2 own-prefix/49F-OOM failure, both disarmed
by the grants and the memory fix below). This half is filled from the Success fire's own measurements.

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
| 2 | One QA fire: `aws lambda invoke --function-name irpt-holdings-refresh-lambda --payload '{"qa": true}'` publishes to holdings_qa at all 3 firms, and the served index is untouched | **MET.** One fire this session (runner already Online, one call): `lambda.invoke(FunctionName='irpt-holdings-refresh-lambda', Payload=b'{"qa": true}')` at 2026-09-28T23:32:43Z -> `{"status": "DISPATCHED", "results": [{"firm": "49financial", "dispatched": "f61bb631-bfc0-4d3a-ad39-9d3b278ea1b9"}, {"firm": "cottonwood", "dispatched": "3f2dca9e-7010-4c13-be0a-1bf43add329b"}, {"firm": "inflection", "dispatched": "58cbeda0-790a-41c8-a33f-34295e5672a9"}]}`. All three terminal **Success**, rc=0 (`ssm.get_command_invocation`): 49financial `f61bb631-bfc0-4d3a-ad39-9d3b278ea1b9` (exec 23:32:43Z-23:37:41Z), cottonwood `3f2dca9e-7010-4c13-be0a-1bf43add329b` (23:32:43Z-23:35:59Z), inflection `58cbeda0-790a-41c8-a33f-34295e5672a9` (23:32:43Z-23:35:07Z), all business_date=2026-09-25. holdings_qa revisions published: 49financial `b028497055376448e709387ec4cf85c7041657dbed638c48031a8a503ea516cf` (152,280 nodes, reconcile 1826940340.65/1826940340.65 True), cottonwood `06cf166246cbbaeb9cb2550332f8400d188f8b418666f5cdd143006ab4155755` (17,633 nodes, reconcile 553689995.59/553689995.59 True), inflection `16b173132b6dc87196e4c3932599b1d986cdcf89bcf64df090c06d0824c8b4f1` (32,405 nodes, reconcile 208110999.41/208110999.41 True). Served index revision (`irpt/<firm>/platinum/holdings/current/manifest.json`) VersionId before=after, read by `s3api head-object` immediately before dispatch and again after all 3 commands ended: 49financial `OqjgF6qs7e5QsF7HScOre54hxJ18Ktgf`=`OqjgF6qs7e5QsF7HScOre54hxJ18Ktgf`; cottonwood `ykQofbha2WKbcHFKvxMThBs0UNC_g9ji`=`ykQofbha2WKbcHFKvxMThBs0UNC_g9ji`; inflection `ipomYxTGLoE0pAgeh.nNtVJ6QUm5ynJG`=`ipomYxTGLoE0pAgeh.nNtVJ6QUm5ynJG` -- untouched. Re-minted members-sha256 this fire ran against: `94f2e3433d9ecc018027418ebb057c4ce6bfd2bb5baa45b8edb697f036421e5e` (41 members/firm; ledger `irpt-holdings-packages-m-20260928c` CLOSED, commit `71d1099644`, post the 49F peak-RSS fix `c81280bd75`). Surprise rows `IRPT_BCKEND-W42-S1`/amendment-2's two failures are superseded by this Success fire; the causing grants and fix are: read-version grant on the READS statements (ledger `irpt-holdings-principals-versionread-m-20260928` CLOSED), own-prefix read-version grant on `PublishOwnHoldings` (ledger `irpt-holdings-principals-ownread-m-20260928` CLOSED, this session), and the 49F peak-RSS cut (`c81280bd75`, `R19_49F_MEMORY_PROFILE_20260928.json`) |
| 3 | The first publication's diff against the served revision, by class (`account_mask_publication_diff.py dry --pin-served` and `holdings_publication_diff_classes.py`, the QA candidate at the fire's as_of) | **MET, two readings.** (a) The PINNED re-run at the SERVED date on today's code, already on file: `R4_ENABLE_DIFF_20260928/README.md` (2.0.0_SA_COO~M, ~14:0xZ, code d306d972f6 cash-line + a57537bd8a UIC-16 on CLOUD) -- 0 node/amount/clock changes, isolating the CODE'S effect alone (table reproduced below, first column). (b) THIS fire's own QA candidate at its real as_of (2026-09-25, 3 trading days past the served 2026-09-22), assembled from the holdings_qa manifest+header+gold parquet (bypassing `HoldingsPublication.load()`'s bounded-response refusal, same technique as `account_mask_publication_diff.py._served`) and run through `holdings_publication_diff_classes.py --firm <f> --candidate <assembled.json> --out R4_ENABLE_DIFF_20260928/QA_<firm>.json` for each firm -- node/amount/clock changes are REAL custody movement across the 3-day gap, not a code artifact (second column) |
| 4 | INF name census on the QA candidate (0 personal data, or each hit dispositioned) | **MET.** Re-run on THIS fire's INF candidate (revision `16b173132b...`, business date 2026-09-25, 29,932 SECURITY nodes scanned across `display.label`, `display.description` and the `company=` capability fact, 2,426 distinct name texts): **0 email-like tokens**; **7 distinct 6+-digit-run texts, 7 occurrences** (one fewer than the prior pinned read's 8 -- `TEVA-OLD09152026` no longer present at this business date, rolled off): `NHX203903 -- NH Portfolio 2039 (Fidelity Index)`, `NHB203907 -- NH Portfolio 2039 (Fidelity Blend)`, `NH2036000 -- NH Portfolio 2036 (Fidelity Fund Port)` (New Hampshire 529 product codes), `AZN-OLD02022026`, `TTE-OLD12092025`, `THMR-OLD04152026`, `OGI-OLD04032025` (pre-corporate-action tickers, MMDDYYYY suffix). **Disposition: SAFE, no mask or drop** -- each hit names a listed/registered security, none carries a client identifier. Prior read: `R4_ENABLE_DIFF_20260926/README.md` Addendum 1 |

## What the first scheduled publication moves (by class, per firm)

**Two sources, kept separate.** (A) The pinned re-run at the SERVED date (2026-09-22, `R4_ENABLE_DIFF_20260928/README.md`,
2.0.0_SA_COO~M ~14:0xZ, code d306d972f6 cash-line + a57537bd8a UIC-16 on CLOUD) isolates the CODE's own effect: same
business date in and out, so the only changes are what the code now does differently. (B) THIS Success fire's own QA
candidate (as_of 2026-09-25, 3 trading days past served) in `R4_ENABLE_DIFF_20260928/QA_<firm>.json`, which additionally
carries 3 days of REAL custody movement (new trades, prices, accounts) -- not a code artifact.

| Class | 49F (A / B) | INF (A / B) | COT (A / B) | Traced to |
|---|---|---|---|---|
| Node set (added / removed) | 0/0 / 2,463 added+1,880 removed | 0/0 / 1,644 added+2,567 removed | 0/0 / 979 added+95 removed | (A) code-only 0; (B) real 3-day custody churn, not code |
| Amounts / percentages | 0 / 147,410 amount + 147,161 pct | 0 / 28,458 amount + 12,628 pct | 0 / 16,180 amount + 16,241 pct | (A) code-only 0; (B) real custody movement over the 3-day gap |
| Clocks | 0 (pinned) / 149,817 | 0 (pinned) / 30,761 | 0 (pinned) / 16,654 | (A) pinned to served 09-22; (B) the new business_date=2026-09-25 field on every node, expected of any live fire |
| ACCOUNT `display.label` | 2,970 / 2,970 | 875 / 875 | 755 / 754 | own-mask half: CTO @45bafa24a1, CRO @c412578ede; INF/COT rose from the first read (562/595) because UIC-16's full account type now changes labels the old 24-char cut or uppercasing had left alone. (A)=(B) at 49F/INF exactly; COT off by 1 (a 3-day account-population change, not code) |
| Classification (asset_class / sub / basis, incl. cash-line) | 123 / 135,231 | 30,881 / 29,903 | 2,577 / 12,495 | batch A (CTO @8214723353); COT-new Part 1 (CTO @ab4a2e41bb, deferred Holdings to THIS half); COT's cash-line rule (`classify_security` on `display.description`) hits **981 SECURITY nodes** at COT in this fire's own candidate (asset_class=cash, basis=NAME_PATTERN), **0 at 49F and 0 at INF** -- measured directly on the candidate, not folded/estimated (COT gold half of the cash-line act is HELD, CTO 102293/102323). (B)'s much larger counts vs (A) are the current diff tool's coarser grain (whole `classification` dict compared as one unit, so any capability_facts/valuation_facts churn from the 3-day gap also counts here) plus the real custody movement itself, not evidence of a wider code change |
| `company=` + SECURITY display name | 67 (A) | 30,881 (A) | 0 (A) | 49F: CTO R5 decision 4 (cb8cd03113). INF: e0f680f0df, admitted as its own line by CTO 101360 under the census in precondition 4. Not separately broken out in (B); folded into Classification/display_other there |

Three lines from the code now on CLOUD, now exercised live in this fire:
- **Cash-line rule** (`classify_security` on `display.description`, `CASH -- CASH` -> `cash`, d306d972f6): measured
  directly on this fire's own candidate -- **COT 981** SECURITY nodes (asset_class=cash, basis=NAME_PATTERN, e.g.
  `display.label` `CASH -- CASH`), **49F 0**, **INF 0** (the rule only ever fires on Black Diamond's own cash line,
  which only COT's custodian carries).
- **UIC-16** (the account type in full, a57537bd8a): INF only (labels 875, matching the pinned read exactly, up from
  562 at the first 09-26 read); 49F keeps its Schwab codes unchanged (label count steady at 2,970 across the pinned
  read, the first read and this fire).
- **ETF Part A** (16 keys incl. VNQ -> alternatives; CTO @c516dab84b): a static classifier-table change, not
  separately broken out by this diff tool; folded into the Classification column wherever a rebuilt SECURITY node's
  asset class changed, at both (A) and (B).

A later as_of also brings real custody movement (new trades, prices and accounts): THIS fire's own candidate already
shows it (column B above, 2026-09-25 vs the served 2026-09-22), and it recurs every scheduled weekday fire -- it is the
producer's ordinary daily output, not a code change.

## Blast radius and rollback

- **Touches:** the schedule's State; one Holdings revision per firm per weekday in each firm's served table. The code
  the schedule would run: the re-minted standalone packages, members-sha256
  `94f2e3433d9ecc018027418ebb057c4ce6bfd2bb5baa45b8edb697f036421e5e` (41 members/firm, off the 2026-09-25 mint's
  `83f6a81aab34...`; ledger `irpt-holdings-packages-m-20260928c` CLOSED, commit `71d1099644`, the mint run after the 49F
  peak-RSS fix `c81280bd75`).
- **Does not touch:** the directory, bd-securities, any COT/BD gold output, the portal;
  `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` (the directory chain's
  own bundle, ETag `4155283a1b77394259ff809611f28a8e`, read unchanged this session) -- UIC-16's directory side waits on
  2.0.0_SA_COO~P's next directory package, not this half.
- **Rollback per key:** (a) set the schedule to DISABLED (Terraform); (b) per firm, repoint the served index to the
  prior revision, which is retained with its manifest and version-pinned source objects; (c) IAM: revert the two
  one-line grants (READS statements' and `PublishOwnHoldings`'s `s3:GetObjectVersion`) and safe-apply under a new
  ledger leg, plan 0/3/0 back, per `SIGNOFF_HOLDINGS_READ_VERSIONS_20260928.md` and
  `SIGNOFF_HOLDINGS_OWN_READ_VERSIONS_20260928.md`.

## The ask

**SENT 2026-09-29 ~00:1xZ by the issuer, 2.0.0_SA_COO~M, to 1.0.0_SA_CTO and 4.0.0_SA_CRO** (drain of
TO-IB-m19-2 @6ceb8c3e5a; the issuer re-ran AC1-AC3 from the worker's tree before the drain). Sign or refuse the
enable. All four preconditions now MET on this Success fire (2026-09-28 ~23:3xZ, command ids
`f61bb631-bfc0-4d3a-ad39-9d3b278ea1b9` / `3f2dca9e-7010-4c13-be0a-1bf43add329b` / `58cbeda0-790a-41c8-a33f-34295e5672a9`,
all rc=0, all business_date=2026-09-25). The issuer (`2.0.0_SA_COO~M`) sends this half to `1.0.0_SA_CTO` and
`4.0.0_SA_CRO` at the drain, per the order's own Step 3 instruction ("Do NOT send it. The issuer sends it ... at the
drain.").
