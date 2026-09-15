# Cottonwood cents hotfix: all seven served outputs verified

Author: `1.0.0_SA_CTO~A`. Observed 2026-09-15 13:28-13:36 UTC.

**EXERCISED: all seven named output families are published and verified.** The13:30 Gold run,13:40 accrual bridge and13:50 publisher completed the full chain. At13:50:59Z all seven target Platinum bodies equal their current Gold source content except the publisher provenance; source hash, key and vintage checks pass7/7. The canonical hotfix ledger is CLOSED, all5 legs proven, and its sentinel is removed.

**Correction97089:** My13:35Z inference of a missing dated account-units writer was premature: I inspected the consolidator and publisher but omitted the intermediate accrual bridge. The earlier13:31 observation of six dated families was correct at that time; it did not establish a permanent gap. The signed seven-family expectation is unchanged and no carve-out or additional scope disposition is needed.

## Measured run

- Fresh before snapshot13:28:13-17Z; after snapshot13:31:34-38Z, with VersionIds and content hashes. Evidence: `scheduled-gold-1330-verification.json`.
- Request `996aa948-5808-444e-a408-85bb3b1fad7a`, scheduled13:30:36Z to13:31:10Z, duration33430.16ms. All283 log events in that run's observed window:0 SCOPE FAILED,0 [ERROR],0 Traceback. New artifacts declare `_provenance.trigger=scheduled` and process_time13:30:36Z.
- Cottonwood category-views, aum-metrics and account-distribution: value date2026-09-14. Global category-views and aum-metrics:2026-09-14; Global account-distribution: its producer's period2026-09-15. Each is read from content/provenance, not inferred solely from a key or upload time.
- At13:34:20Z the live Lambda is Active/Successful with exact hotfix CodeSha256 `evIYCXURor4V++Ci4HsgwE8zIPZva/BAL+ICaLJIiAE=` and revision `15eda5c8-d1ab-40d3-ac79-3dc0292d4575`.
- Platinum remains at its pre-publisher versions in this observation. No manual invocation or production write was made by this observer.

## Corrected writer chain: Gold13:30 -> accrual13:40 -> publisher13:50

CTO97089 identifies `data/mdpf/scripts/gold/build_portal_gold_accrual.py:81-83`, which declares standalone account-units from staging `account_units`, dated by content `value_date`, scoped to Cottonwood. I read its writer at218-295 and the checked-in schedule at `infra/aws/terraform/mdpf-pipeline/accrual-bridge.tf:185-188`. The consolidator's omission from its own dated loop is not a pipeline omission: the bridge owns this hop.

Independent live read **13:45:41Z**, recorded in `accrual-bridge-1340-verification.json`:

- Staging `gold/mdpf_revamp/cottonwood/account_units.json`: written13:30:49Z, version `tTAbT_v3sMuvYqnea4UnEyniBnEbLNXP`.
- Dated Gold `portal/gold/mdpf/cottonwood/account-units/2026-09-14.json`: written13:40:28Z, version `hlds5dRH99I1xsqel.N4xnuG7tCDlU78`.
- Both8281 bytes and **byte-identical**, SHA256 `52440d2deeadf357222fcce6ef38dfbeb80fe37d0910e8c85672a097e8a30dc7`. Both declare assignment_date2026-09-15 and value_date2026-09-14.
- Live Scheduler: `mdpf-accrual-bridge-daily` ENABLED, cron40 13 UTC, targetmdpf-accrual-trigger; publisher-daily ENABLED, cron50 13 UTC, targetopal-assets-mdpf-portal-publisher. Both flexible windows OFF.

The actual deployed publisher was downloaded and hash-verified (CodeSha256 `7X50uR1HrGyeEHZ4FWyHBNwTxt/XXJq5GNmR/eFfWE0=`, revision `9523e457-8aac-4eeb-a23b-154b47076c65`). Its R12 extra requires Cottonwood/account-units and its latest-dated-Gold read now has the09-14 object available. The expected13:50 outcome remained **7/7** and is now demonstrated by the actual served read below.

Global/account-units remains absent in the before/after observation and has not been created or deleted by this seat. The pre-existing08-28-to09-10 dated-history hole noted by CTO97089 is outside the start-forward bridge; no backfill is attempted.

## Unaffected-scope control limit

49 Financial and Inflection naturally created new dated Gold during the same scheduled run: category views/AUM now09-14 and distributions09-15. A before/after daily comparison cannot certify unchanged bytes or attribute those normal changes to the cents fix. The package's existing scope-isolation code is unchanged; the only functional package change remains the approved pair-builder whole-cents comparison. This observation does not pretend to be a same-input counterfactual test.

## Final publisher proof, 2026-09-15T13:50:59Z

Manifest `platinum/mdpf/_manifests/2026-09-15/20260915T135046Z-eeb9afc8.json` records the13:50:46-50Z run, all_present=true, missing_pairs=[], unexpected_pairs=[]. The trigger source field is empty; the run aligns with the independently read enabled13:50 UTC schedule. No manual invocation was made by this seat.

| Served target | Content date | Source/hash/vintage/content equality |
|---|---|---|
| Cottonwood category-views | as_of2026-09-14 | PASS |
| Cottonwood aum-metrics | period2026-09-14 | PASS |
| Cottonwood account-distribution | period2026-09-14 | PASS |
| Cottonwood account-units | value_date2026-09-14; assignment_date2026-09-15 | PASS |
| Global category-views | as_of2026-09-14 | PASS |
| Global aum-metrics | period2026-09-14 | PASS |
| Global account-distribution | its producer's period2026-09-15 | PASS |

`scheduled-publisher-1350-verification.json` records each immutable manifest/source/served VersionId and SHA, exact content comparison, and provenance linkage. All6 control objects (three families each for49 Financial and Inflection) also equal their current Gold; this is the stated source-equality check, not an unchanged-daily-bytes claim. At13:51:40Z all7 prior Gold versions remain unchanged and Global/account-units remains absent in both planes.

## Separate pre-existing publisher warning

The publisher manifest reports AccessDenied reading its previous-run pointer `s3://opal-data-portal-v2/platinum/mdpf/_manifests/latest.json` under `opal-assets-mdpf-egress-publisher-role`. Its documented fallback republishes inputs because it cannot compare them with the prior run. I independently read the09-14 pre-hotfix manifest `20260914T135046Z-73976a4c` (version `cURl8lJGs2WTyRoLn2NBxps2kBsNkmfy`): the same AccessDenied and18 published rows were already present. Receipt: `publisher-pointer-read-warning.json`. The current manifest also surfaces the two `_code` objects as unrecognized artifact keys; no missing or unexpected artifact pairs are reported.

This warning does not negate the measured seven-family content recovery and was reported to CTO at13:52:29Z for separate ownership. No IAM, publisher-code, scope, historical-key or data mutation was made to clear it.

## Closure and correction receipt

CTO97089 superseded the13:35Z missing-writer inference; COO~D and MSTR received the correction at13:46:10/12Z. CTO and COO~D received the demonstrated7/7 result at13:52:29/30Z. Canonical `deploy_ledger.py close-leg --leg-id L5` and `close` both succeeded: all5 legs proven, sentinel removed. The original seven-family scope and all signed halves remain intact. Full original correction carrier: `CTO_DISPOSITION_97089.md`.
