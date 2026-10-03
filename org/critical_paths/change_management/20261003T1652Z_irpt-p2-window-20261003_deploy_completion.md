# Deploy Completion Record
**Date opened:** 2026-10-03T16:52:57.507424+00:00
**Status:** OPEN
**Deploy:** P-2 window: every 49F account on method_version 2, summaries, PATH B print/export, PATH A retired for 49F (packet @855fdad77c blob f3532bf5b9; CTO half batch 222 @e67cba94ac; Andrew B2 word @2488be2c68)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | tf-lambda | irpt-49f-reporting-gold-lambda code | CodeSha256 = Mex71Y5g; re-plan 0 |  | OPEN |
| A2 | s3-prefix | account_return_daily backfill 23 chunks over the population | every day's manifest method_version 2 with reported rows; served accounts kept; pre-window VersionIds recorded |  | OPEN |
| A3 | s3-prefix | dim_return_method method_version=2 (--method-row-only --tieout 0.037) | served row hash = contract 73e80ef7 |  | OPEN |
| A4 | tf-lambda | irpt-49f-reporting-publish-lambda code + policy (not the schedule) | CodeSha256 = AH5r60vp; policy read back |  | OPEN |
| A5 | s3-prefix | publish fan-out over every account | account= prefixes = gold union count; series + manifest each; the 6 at method_version 2 |  | OPEN |
| A6 | tf-lambda | reporting-read: code+env, policy, render-grant policy, summary route | CodeSha256 = Wzf2qS5P; route listed; series 200 for an account outside the 6 |  | OPEN |
| A7 | activation | auth-validator-edge new version + distribution association | association on every behavior that carried :21; 401 negative arm before/after; human Auth OK, 0 runtime errors |  | OPEN |
| A8 | tf-lambda | irpt-export-render code | CodeSha256 = WDAv+kWK; PATH A export unchanged |  | OPEN |
| A9 | s3-prefix | summaries pass | summaries = directory clients with a published account (counts printed) |  | OPEN |
| A10 | activation | irpt-49f-reporting-publish-summaries-daily schedule | ENABLED 08:45 America/New_York read back |  | OPEN |
| B1 | git | portal DEV: ~D lands P-6 + P-3 + Download (staged 426761e4) | three readers on DEV read PATH B |  | OPEN |
| B2 | git | portal PROD promote by 0.0.0_AB_MSTR on Andrew's word | origin/PROD contains B1 (is-ancestor + positive control) |  | OPEN |
| B3 | tf-lambda | irpt-performance-adapter code (PATH A retired for 49F) | CodeSha256 = NU6YVERL; 49F PATH A refuses OBJECT_NOT_COVERED; Inflection still composes |  | OPEN |
| V | verify | P-1 walk on PROD + FWD-8 served pair | account outside the 6: tab, print, export, frozen as_of; CVO reads one served pair |  | OPEN |

## Log

- 20261003T165257Z OPENED by 2.0.0_SA_COO~P with 14 leg(s)
