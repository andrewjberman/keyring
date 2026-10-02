# MDPF_TAXSMA -- FAST pin grades (`3.0.0_SA_CVO`, 2026-10-01 ~06:3xZ)

**Asked by:** `1.0.0_SA_CTO` 103508. **Implementing seat:** `4.0.0_SA_CRO`. **Pins named by:**
`org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md` (as of 03:5xZ). **Lease:** FAST `MDPF_TAXSMA` read live until
06:20:24Z at 05:51Z (`drive-mode.py status`). **Graded at:** CLOUD HEAD (local), portal DEV `54bd4224`. Read-only:
two `get-function-configuration`, one `get-function` (the gold zip), two test runs.

| pin | claim | read | grade |
|---|---|---|---|
| TX-k-1, the gold package, deployed 02:17Z | built from `e8994f23af`; Tax code present; Tax DISABLED | live `mdpf-gold-lambda` CodeSha256 `7hI4flW5RZfisph6h7/HSsIWxwSMBFcdXMPMhjF9P/U=`, LastModified 02:17:00Z, equal to STATUS; the zip downloaded from Lambda hashes to the same value; 40 file members, 26 `.py`, six of them `taxsma_*.py`; 19 of 26 `.py` members are byte-equal (line endings normalised) to a file of the same name under `data/mdpf` or `lib` at `e8994f23af`, 0 differ, 7 have their source outside those two trees and were not compared; the function has 1 environment key and 0 carrying TAX | PASS on deployed bytes |
| TX-u-1 / TX-u-2, the publisher, deployed 02:21Z | switch OFF | live `opal-assets-mdpf-portal-publisher` CodeSha256 `pj+Jat96t5dijB+0SQF918S1pi3AZBs1eQNvMXLYEJA=`, LastModified 02:21:34Z, equal to STATUS; `TAXSMA_ROLLOUT_SWITCH` reads `OFF` (the one TAX key of 9) | PASS on the applied plane; the zip was not downloaded |
| TX-r-1, the Tax-off release is a zero business delta | 16 of 16 bodies process-time only | not re-run; the served arm is ledger leg V2 at the 13:50Z publisher run, which has not happened | NOT_EVALUATED until leg V2 |
| E2c `1e5e13d223`, E2d `46d04eb7b6`, E2e `dfe374adfb` (candidates, not deployed) | 223, 226 and 227 tests | all three are ancestors of HEAD; `py -3.12 -m pytest data/mdpf/tests/taxsma`: 227 passed in one process at HEAD | PASS on a test run; the offline real-data runs (Global 2,091,754,766.55; Cottonwood SMA 6,049,368.78) were not re-run |
| TX-c-1 / TX-c-3, portal `370d2fe8` | accessor and caption | ancestor of portal DEV HEAD; `bun test src/api/endpoints/__tests__`: 10 pass, 0 fail | PASS on a test run; no signed-in render exists (nothing serves Tax) |
| TX-i-1, TX-i-2, TX-i-3 (IAM applies) | applied, simulated | not re-read | NOT_EVALUATED |

## Observations (not grades)

- **O-T1.** STATUS says "39 modules" for the gold package; the zip holds 40 file members, 26 of them Python. The two
  counts measure different things; the STATUS line should name its unit.
- **O-T2.** The E2e defect (the prelude's default valuation date) is stated as present in the deployed code. This
  seat's scan of the six bundled `taxsma_*.py` files found neither `expected_last_trading_day` nor
  `prev_trading_day`, so the default lives in another member and the claim was not confirmed on deployed bytes. It is
  harmless while Tax is DISABLED; it is a stop for activation (STATUS next-proof 5 already says the rebuild is
  required first).
- **O-T3.** The lease read 06:20:24Z as its end at 05:51Z. Past that instant the project reads FULL unless
  re-armed; a FAST item landed after it would be outside the lease.

## Not verified by this seat

Leg V2; the two prelude roles in use; the Gateway route; the first-day and weekend parked rules; push state beyond
local CLOUD.

-- 3.0.0_SA_CVO

## Pre-read for TX-r-1 leg V2, 14:0xZ -- the 13:50Z publisher run (the leg is the lane's and is still OPEN)

Ledger `mdpf_taxsma-tx-r-1`, leg V2: "both served category-views keys content-equal to before on every field other
than generation time (DELTA=0, comparison printed)". This seat's read, before the lane's proof exists:

- The run happened on the deployed code: publisher `CodeSha256` `pj+Jat96..` (the built zip's, LastModified
  02:21:34Z), `TAXSMA_ROLLOUT_SWITCH` OFF; request 1c6abe65 at 13:50:49Z published 18 objects, 0 failed, roster
  complete.
- Four category-views keys were written (49financial, cottonwood, global, inflection), each compared here with its
  prior S3 version (2026-09-30 13:50Z): top-level keys equal 4 of 4; leaf paths and types equal 4 of 4 (121 or 122
  leaves each); the token "tax" occurs 5 times in each object in both versions, so no node appeared or vanished.
- Leaf VALUES differ on 17 to 23 leaves per object: `as_of` (2026-09-30 today by the run's log; the prior value
  was not printed), the provenance fields, and AUM figures.

**So the leg as worded cannot read DELTA=0 across two as-of days:** generation time is not the only field a day
changes. What this read supports is the weaker and true statement (same shape, same node set, Tax absent as before).
A DELTA=0 on values needs the same gold input published by the old and the new code. NOT a grade: the lane's proof
is graded when it lands.

-- 3.0.0_SA_CVO

## Grade of the lane's leg V2 read, 14:5xZ (`TX_R_1_LEG_V2_READ_20261001.md` @3d07a6b2ff, merged e7110efff5)

The lane gives no verdict and puts the leg to `1.0.0_SA_CTO`. This seat grades the READ, not the leg.

| the read's claim | this seat's own read | grade |
|---|---|---|
| 1. the prior frontier date is restated every day, on the old code too | SERVED plane, which the lane says it did not read per date: the last three S3 versions of `platinum/mdpf/<scope>/aggregate-aua-timeseries.json` for the four scopes, every list series compared date by date. Old-code pair (publishes of 09-30 against 09-29): exactly one restated date, 2026-09-28, the earlier document's frontier, 4 of 4 scopes | PASS, on a plane the lane did not use |
| the release-crossing pair | publishes of 10-01 against 09-30: Inflection and Cottonwood restate 2026-09-29 only; 49 Financial and Global restate 2026-09-28 and 2026-09-29. Top-level keys added 0 and removed 0, series count equal, in 8 of 8 pairs | PASS: the four differences are where the read says |
| 2. the second date at 49 Financial and Global is the input's own restatement | the lane's probe `tx_r_1_v2_input_restatement.py` run at this seat (read-only): partitions 2026-09-30 against 2026-10-01 of the SmartX model table differ at 2026-09-28 in 1 of 8 models (+74.47) and at 2026-09-29 in 3 of 8 (+88.42, +514.07, +1,035.28, sum +1,637.77); control day 2026-09-25 in 0 of 8 | PASS on a re-run of the lane's instrument; the figures are the read's |
| 3. Cottonwood's shape grows every day and its tax-named paths name a strategy | not re-read; this seat's date-aligned series for Cottonwood number 21 in both versions and none names tax | NOT_EVALUATED |
| no Tax key and no top-level key appeared | 8 of 8 pairs above; and the four category-views objects in the pre-read | PASS |

**The leg was ruled CLOSED at 14:23Z (RULINGS batch 91), before this grade was written.** Item 2 of that ruling
names one limit: "no per-date served value was read by anyone". The first two rows above are that read, taken
at 14:4xZ on the served objects' S3 versions; it agrees with the ruling. A corroboration for the record, not sent.

**What this supports:** the four probe failures are the probe's expectation, as the lane says. The release changed
no shape and no key on the served plane, and the value movements are the pipeline's daily restatement plus one
vendor restatement. **What it does not decide:** whether leg V2, worded as DELTA=0, closes; that is the CTO's.

-- 3.0.0_SA_CVO

## Grade on the served plane, 02:xZ 2026-10-02 -- TX-r-3 activation and portal v2.1.192

Pins: `0f1a67e196`, `335430e793`/`78a7b473f8`, `b1db201025`/`f618ff75a8`, `1f30c98185`, `ba19b35fd8`, `ed0410908b`;
portal `d79b9934` / PROD `f2731ad3`. Every row is this seat's own read; the lane's ledgers only named the objects.

| claim | this seat's read | grade |
|---|---|---|
| mdpf-gold-lambda runs the stdlib Gateway call of `0f1a67e196` | deployed zip downloaded: sha256 equals `CodeSha256` `BZAtvS5m..` (LastModified 22:05:17Z); manifest `source_vintage` `e20899bce7`; 40 of 40 members equal `git show e20899bce7:<path>`; 32 of 40 equal `0f1a67e196`, including all 6 `taxsma_*` modules (the 8 that differ are the later Cottonwood act's). `taxsma_snapshot.py` equals `0f1a67e196` (positive control) and differs from `335430e793` (negative control); imports `urllib.request`, not `httpx` | PASS. The Tax code is what runs; "runs pin 0f1a67e196" is superseded by the later act, not false |
| the four Tax settings are live | function configuration: `TAXSMA_CAPABILITY_SECRET_ID`, `TAXSMA_GATEWAY_BASE_URL`, `TAXSMA_PRELUDE_ROLE_ARN_49FINANCIAL`, `TAXSMA_PRELUDE_ROLE_ARN_COTTONWOOD`, 4 of 4; Active, LastUpdateStatus Successful | PASS |
| publisher switch ON | `opal-assets-mdpf-portal-publisher`: `TAXSMA_ROLLOUT_SWITCH`=ON, `CodeSha256` `pj+Jat96..`; run manifests 13:50Z OFF, 19:28Z ON, 22:09Z ON | PASS |
| Tax is served, valued 2026-09-30 | 4 S3 versions per scope (13:50, 19:28, 21:56, 22:10Z). 49financial total 1,738,331,604.42 to 1,757,099,818.07, the difference equal to `tax_additive_aum` 18,768,213.65 to the cent; SMA 20,777,095.77 to 39,545,309.42. Global 2,060,678,513.01 to 2,085,492,328.94 (+24,813,815.93 = 49financial Tax + Cottonwood Tax); a new fee-basis component `taxsma`, the 3 firm components unchanged, so Cottonwood Tax is not counted twice. Cottonwood total 541,313,055.76 in 4 of 4 versions, SMA 0.00 to 6,045,602.28. Inflection Tax null in 4 of 4. Coverage 11 of 11, 13 of 13, 2 of 2, all CURRENT; Tax values unchanged in the 2 later versions | PASS |
| not stale | `period` 2026-09-30 in 16 of 16 versions; `prev_trading_day(2026-10-01)` = 2026-09-30 (`lib/trading_calendar.py`); next production run 2026-10-02 13:30Z | PASS |
| first-day rule | `tax_additive_aua` non-null on 1 of 478 dates (49financial) and 1 of 487 (Global), 2026-09-30 only; `tax_coverage` on 2026-09-29 reads `BEFORE_FIRST_OBSERVATION`; on 2026-09-30 49financial `measured_aua` 14,318,213.65 + 4,450,000.00 workbook-stated = 18,768,213.65; base + Tax = aggregate on 09-30 | PASS |
| portal v2.1.192 on PROD with the colour change | tag `portal-v2.1.192` at `f2731ad3`; CI run 36918344456 "Deploy to Production" success at that head (20:02Z); `modelPortfolioColors.ts` and its test equal between `d79b9934` and `f2731ad3`, differ from rollback base `ba8e971f`. PROD has since moved to v2.1.193 `b3a1d8a6` (site Z's AMGT release, CI 36956494108 success 02:37Z); `f2731ad3` is its ancestor and the colour file is equal there | PASS |
| ledgers closed | 4 of 4 completion records CLOSED (first-day, activation, urllib, serve-today); shared-tree `.open_deploys` 0 Tax SMA files; 14 worktrees read, one copy on `coo-y-r30` at a head 0 commits ahead of its merge-base, which predates the close and merges as a no-op | PASS |
| lane tests | `data/mdpf/tests/taxsma` at HEAD, `data/mdpf/` clean: 235 passed | PASS on a test run |

**Record drift, not a grade.** `MDPF_TAXSMA.TO-TX-r-2` and `TO-TX-r-3` read `<status>staged` at HEAD although both acts
are served and closed; the project gate therefore reads 6 of 27 orders open, which is what holds the 13 prepared
remediation rows. The flips are the issuer's.

**Limits.** The page was not viewed (Andrew's look on PROD is the only visual record). The custodian sources, the
workbook and the Gateway route were not re-read, so the 4,450,000.00 workbook-stated part is taken as served. The 2
business-active accounts outside the expected set (13 against 11 for 49financial) are not graded.

-- 3.0.0_SA_CVO

## Grade on the served plane, 02:xZ 2026-10-02 -- Cottonwood custom models and SMA sleeves (4.0.0_SA_CRO)

Pins `85dd7adc26`, `8c842b4d44`, `e20899bce7`, `f3044f1e84`; ledger opened `1b0216ee37`, closed `df83ad7236`; halves COO
`32c62ba1b9`, CTO `3338690683`.

| claim | this seat's read | grade |
|---|---|---|
| mdpf-gold-lambda runs `e20899bce7` and nothing else moved | `CodeSha256` `BZAt..` = artifact metadata, version 22:03:41Z; `MDPF_GOLD_COMMIT` `e20899bce7`; the four Tax settings present. 40 of 40 git-sourced members equal `git show e20899bce7:<path>`; prior zip 40 of 40 equal `0f1a67e196`; deployed against prior: the 8 named code members and the manifest differ. Control: the deployed slice differs from the `0f1a67e196` slice | PASS |
| Cottonwood Custom 24,020,674.01, SMA 7,816,204.10, total unchanged | served `category-views`, 22:10Z against 21:56Z: Custom 0 to 24,020,674.01 (seven non-null members, each as claimed); SMA 6,045,602.28 to 7,816,204.10 (DIVZ 1,364,744.83 + PFDE 405,856.99); Client down 25,791,275.83 = Custom + the SMA gain; totals unchanged | PASS |
| Cottonwood series | total unchanged on 487 of 487 dates; the model gain equals the Custom sum on 40 of 40 moved dates (the request's 40); account_count 361 to 378 | PASS |
| Global +24,020,674.01; SMA and Client fixed | total 2,085,492,328.94 to 2,109,513,002.95; Custom 42,899,101.50 to 66,919,775.51; SMA and Client unchanged; non_model unchanged on 487 of 487 dates. 52 dates move: on 40 the move equals Cottonwood's Custom sum to the cent, on 12 it equals the last Custom sum carried forward (provenance `carried_at_declared_cadence`) | PASS |
| blast radius 9 of 16 documents | 10 of 16 served documents move: the request's 9 plus global `account-distribution`, which is the restage branch the request names (active accounts 8,377 to 8,394, seven custom rows). 49 Financial and Inflection gain only nine null Custom members; no dollar node moves. The 21:56Z version equals the 19:28Z version in content, 18 of 18 | PASS |
| COO condition 1: runner copies held or joined to the rollback | the latest versions of the four `opal-data-mdpf/code/scripts/` copies are the ledger's recorded prior versions, byte-equal to `0f1a67e196`: nothing uploaded | PASS |
| COO condition 2 / CTO half: delete-marks only on Andrew's word | word recorded (`ANDREW_DIRECT_20261001_215xZ_COTTONWOOD_CUSTOM_SERVE_NOW_DELETE_MARKS.md`, "Now. Go now"); 2 of 10 version stacks read: marker 22:07Z, prior version intact, new version 22:08:51Z | PASS |
| ledger closed | the completion record reads CLOSED 6 of 6. But `.open_deploys/mdpf-gold-cottonwood-custom-sma-20261001.json` at CLOUD HEAD (read at `3a360e8f33`) is `status: OPEN` with 0 of 6 proofs, past its 3.0-hour window (opened 22:02:01Z); its deletion exists only as an uncommitted ` D` in the laptop shared tree | FAIL on the record only; the act is complete. Row `MDPF_TAXSMA-S15` |

**Unnamed, not graded.** Global `aum-metrics` `account_count` rose 8,242 to 8,263 (+21) while Cottonwood and Global's
distribution rose 17; neither half names a Global count, and Global's count was already not the sum of the three
partners (8,242 against 8,053).

**Limits.** The page was not walked; the dim parquet was not read; 2 of 10 marker stacks were read; 49 Financial and
Inflection gold were not read. as_of 2026-09-30 (Wednesday) is T-1 for the 10-01 runs.

-- 3.0.0_SA_CVO

## Grade, 02:xZ 2026-10-02 -- MDPF_HEALGAP cell 1, the Cottonwood catch-up (2.0.0_SA_COO~M)

Ledger `healgap-cottonwood-catchup-m-20261001`: legs D1 and S `65197e3d01`, leg D2 `35053e1cb9`.

| claim | this seat's read | grade |
|---|---|---|
| D1: the first run catches up 5 dates | manifest `2026-09-30/20261001T191940Z` catchup: planned 5, built 5 (rc 0), failed 0, skipped 39 | PASS |
| S: the five read at the half's values; nothing else moves | served Cottonwood series 13:50Z against 19:28Z: model_aua moved on exactly 5 of 487 dates (08-18, 08-20, 08-21, 09-23, 09-24), each from absent to measured and equal to the half's value to the cent, 5 of 5. Global moved on 6 dates: the five (carried to measured) and 09-30, whose +24,813,815.93 equals the new Tax member exactly | PASS |
| the five survive the 22:08Z run | current version: the five still measured; value minus the Custom sum equals the half's value, 5 of 5 | PASS |
| D2: the second run plans nothing | manifest `20261001T220850Z`: planned 0, built 0, failed 0; unvalued dates 44 to 39 | PASS |
| ledger closed | CLOSED 4 of 4 at HEAD; the JSON removed in `35053e1cb9`. 4 of 14 worktrees still carry it (coo-p-pr275, coo-y-r30, coo_m_r30, wk-taxsma-cro), all at heads that predate the close (`is-ancestor`) | PASS |

**Limits.** The `value_date` of each rewritten parquet was not re-read. The 2026-10-02 13:30Z run (hookup leg V2) has
not happened.

-- 3.0.0_SA_CVO
