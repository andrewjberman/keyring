# Deploy Completion Record
**Date opened:** 2026-10-02T20:22:33.198185+00:00
**Status:** OPEN
**Deploy:** IB-pr-221: Inflection's Performance served from its holdings gold + 49F fee_basis GROSS (packet blob 87d1cd8418; COO half signed; CTO half batch 185 @0c714c37eb)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 80.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | verify | pre-conditions (a)-(d) at the hour + both artifacts' map hash = S3 content-sha256 | PASS + equal | ~20:2xZ: (a) stale_gap_days_precondition.py PRE-CONDITION PASS, 0 objects under the three gap days, control intact; (b) PRD v0.23 ruling 23; (c) re-planned in P2/P3 below; (d) rebuild at emission 1.2 (10-01, ledger closed); map artifact_sha256 = S3 content-sha256: producer kKgvbKtG (OJ.bVNs_0q) yes, adapter /K1eLPu (7GwiGHEPjUOS) yes | CLOSED 20261002T202737Z |
| S0 | git | remove the DEPLOY-SERVE-HELD line from holdings_performance.py with SERVE-RELEASE-ACK | commit hash | commit 718716fb60 (SERVE-RELEASE-ACK): the DEPLOY-SERVE-HELD line removed; the file now equals the de3d423dce blob the producer artifact packages | CLOSED 20261002T202918Z |
| P2 | activation | targeted safe-apply irpt-holdings-performance-lambda (49F) to kKgvbKtG; condition 3 dry run before/after | CodeSha + same rows/census | pre-condition (c): full plan 7 to add, 1 to change, 0 to destroy (= P2 + P3); targeted plan 0/1/0 (s3_object_version ifXqxmjU -> OJ.bVNs_0q, source_code_hash gLRGHIyi -> kKgvbKtG); safe-apply 20:54Z Apply complete 0/1/0; read-back CodeSha256 kKgvbKtG, Active, Successful; condition 3: dry run 2026-10-01 source schwab_08335338 before and after: both rows=7570, census {OK 6678, NO-PRIOR-HOLDINGS 883, NON-POSITIVE-BASE 6, ALL-HOLDINGS-EXCLUDED 3}, identical | CLOSED 20261002T205818Z |
| P3 | activation | targeted safe-apply the 7 Inflection resources; condition 4 one dry-run invoke | created + census equals the rebuild | plan 7 to add, 0 change, 0 destroy (schedule cron(0 14 ? * MON-FRI *) UTC, input source orion); safe-apply ~21:0xZ Apply complete 7/0/0 (log group, 2 roles, 2 policies, irpt-inf-holdings-performance-lambda, schedule irpt-inf-holdings-performance-daily); re-plan No changes; condition 4: one dry-run invoke {source: orion, date: 2026-09-30, dry_run: true}: rows=966 census {OK 792, NON-POSITIVE-BASE 174} = the rebuild's manifest for 2026-09-30 (rows 966, status_census OK 792, NON-POSITIVE-BASE 174) | CLOSED 20261002T210857Z |
| G1 | activation | commit the held retained.tf grant + targeted apply; condition 5 IAM simulation, Cottonwood denied | allowed x2 + denied | commit 2b3048bd22 (the held retained.tf half; audited lane override IRPT_BCKEND_FAST_Y_TFPOLICY, logged 21:13:02Z, authority the CTO half batch 185); full plan 0/2/0 (G1 + F1); targeted plan 0/1/0 adding ReadINFHoldingsGoldPartitionInventory + ReadINFHoldingsGoldPartitions only; safe-apply ~21:2xZ Apply complete 0/1/0; condition 5 simulate-principal-policy irpt-performance-adapter-role: GetObject on Inflection holdings_performance_daily date=2026-09-30 allowed, ListBucket with s3:prefix irpt/inflection/gold/holdings_performance_daily/ allowed, GetObject on the Cottonwood gold implicitDeny (negative control) | CLOSED 20261002T212638Z |
| F1 | activation | targeted safe-apply the adapter to /K1eLPu; condition 6 probes, deployed-bytes read, 49F GROSS, 10 min clean log | all four | full plan 0/2/0 (G1+F1); targeted plan 0/1/0 s3_object_version wjneBb9_ -> 7GwiGHEPjUOS, source_code_hash cdbFZDJA -> /K1eLPu; safe-apply Apply complete 0/1/0, live CodeSha256 /K1eLPu 21:39:28Z Active Successful; re-plan No changes. Condition 6: (1) probes before/after equal: empty headers CONTRACT_VERSION, cottonwood non-existent user NOT_AUTHORIZED, no FunctionError; (2) section-3 read on the DEPLOYED bytes (get-function zip = /K1eLPu): Inflection 226 YTD SERVED 0.024030831373 = independent chain, 184 partitions; (3) 49F account 0010023253 YTD 0.028511355170711017 on old and deployed bytes, fee_basis NET -> GROSS; (4) adapter log 21:39:28-21:49:28Z: 9 events, the two probe invokes only, 0 Traceback/TypeError/ImportModuleError/timeout; the one 'Error' match is probe 2's AuthzError EMPTY_GRANT -> NOT_AUTHORIZED by design | CLOSED 20261002T221038Z |
| A1 | verify | the Inflection function's first scheduled fire (Mon 2026-10-05 14:00 UTC) read from its own log | census + rows landed |  | OPEN |

## Log

- 20261002T202233Z OPENED by 2.0.0_SA_COO~P with 7 leg(s)
- 20261002T202737Z LEG C1 closed: ~20:2xZ: (a) stale_gap_days_precondition.py PRE-CONDITION PASS, 0 objects under the three gap days, control intact; (b) 
- 20261002T202918Z LEG S0 closed: commit 718716fb60 (SERVE-RELEASE-ACK): the DEPLOY-SERVE-HELD line removed; the file now equals the de3d423dce blob the p
- 20261002T205818Z LEG P2 closed: pre-condition (c): full plan 7 to add, 1 to change, 0 to destroy (= P2 + P3); targeted plan 0/1/0 (s3_object_version ifX
- 20261002T210857Z LEG P3 closed: plan 7 to add, 0 change, 0 destroy (schedule cron(0 14 ? * MON-FRI *) UTC, input source orion); safe-apply ~21:0xZ Apply
- 20261002T212638Z LEG G1 closed: commit 2b3048bd22 (the held retained.tf half; audited lane override IRPT_BCKEND_FAST_Y_TFPOLICY, logged 21:13:02Z, autho
- 20261002T221038Z LEG F1 closed: full plan 0/2/0 (G1+F1); targeted plan 0/1/0 s3_object_version wjneBb9_ -> 7GwiGHEPjUOS, source_code_hash cdbFZDJA -> /K
