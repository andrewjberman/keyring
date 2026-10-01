# Deploy Completion Record
**Date opened:** 2026-10-01T17:19:46.989378+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T201926Z
**Deploy:** ETFS_RIVALS round-4 live join (RIV-d-5): etfs-rivalfunds in-place deploy (5 Lambda source_code_hash), 305 GQGU archive days as issuer bronze + silver, per-source identity floors, G1/G5/G6 replay, page, read
**Authored by:** 0.9.0_WK_ETFS_RIVALS~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas source_code_hash in place; no create/destroy/policy change) | apply output: Apply complete, 0 added 0 destroyed, plan = 5 aws_lambda_function in place | safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T17:45Z): Apply complete! Resources: 0 added, 5 changed, 0 destroyed. Plan = 5 aws_lambda_function in place (source_code_hash + last_modified), no policy or non-rivalfunds change (evidence/apply_plan_r4.txt); comp-tagauthz and tombstone gates clean; code pin b366ed9d7e (CLOUD eb3f0cce93 + ledger + floors commits); CodeSha256 after: daily RLPWZacm..., fetch-holdings xI022e4Y..., canonical-shape WAUfqC0Q..., silver /EmLoqqu..., publish-page F+ayajON... (evidence/lambda_after_apply_r4.txt; each package carries the floors and rivalfunds/adapters/gqgu.py) | CLOSED 20261001T174722Z |
| L2 | s3-prefix | issuer-site bronze + silver for GQGU (305 archived days landed with land_bronze fund=GQGU, silver by marker, 0 gqgu objects before) | S3 listing counts + silver marker | S3 listing after the act: issuer-site/etfs/bronze/holdings/ 654 -> 1264 objects (+610: 305 gqgu captures + 305 sidecars, bronze date 2026-09-29, evidence/gqgu_bronze_landed.json); issuer-site/etfs/silver/holdings/ 327 -> 632 (+305 gqgu-* objects, one per report date 2025-07-14..2026-09-28); 0 gqgu objects before (listing at 17:47Z); silver by fetch_holdings marker: 7 build-silver runs OK (b4d9f071 509fc331 7bfc28ed 22d6b98a 7f8df94a 30b0ecb7 d0567989); no S3 delete issued | CLOSED 20261001T201925Z |
| L3 | git | guardrails_config.json min_resolved_fraction per-source floors (issuer, bloomberg, home_producer), one commit | commit hash | git b366ed9d7e: guardrails_config.json min_resolved_fraction issuer 0.23 bloomberg 0.99 home_producer 0.0 (PROVISIONAL), committed before the apply and carried by all five deployed packages | CLOSED 20261001T174722Z |
| L4 | activation | replay G1 G2 G5 G6 over the served-delta window then publish the page (NEW revisions only) | Lambda request ids + S3 object counts by prefix | G1/G5/G6 newest objects written for 307 report dates 2025-07-14..2026-09-30 (canonical_shape 853->1160, trade_schedule 850->1158 incl. earlier counts, flow_reconciliation +307, all NEW revisions, none overwritten): GQGU dates by marker batches d5-gqgu-00..02 and d5-gqgu-s-00..02 (canonical-shape runs a15b8fc7 2292a214 836e425a aadadb30 c60b90fc e97fc93b) and explicit replay windows d5-replay-c3-00..02 (2fc36e1d a6a4ea13 821386a3) + d5-replay-last-00 (d75f494e); marker chain d5-gqgu-03 timed out x3 (1984c6f7, not the record, row Z-W4-S9); page published date=2026-10-01 marker d5-publish-r4 (daily-lambda request 48814ee7), manifest 12 of 13 updated | CLOSED 20261001T201925Z |
| L5 | verify | d-5.AC1 AC2 AC3 against the served bucket; d5_live.json written | AC RESULT lines | d-5.AC1 RESULT: FAIL 2 failures (clause 1: GQGU not-updated by report_date_freshness, lag 2, row Z-W4-S10; clause 2: the check reads min_resolved_fraction at the config's top level, row Z-W4-S11; clause 3 OK, no identity_coverage failure); d-5.AC2 RESULT: PASS 0 failures; d-5.AC3 RESULT: PASS 0 failures; d5_live.json written. The deploy itself is whole: nothing stranded | CLOSED 20261001T201926Z |

## Log

- 20261001T171946Z OPENED by 0.9.0_WK_ETFS_RIVALS~4 with 5 leg(s)
- 20261001T174722Z LEG L1 closed: safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T17:45Z): Apply complete! Resources: 0 added, 5 changed, 0
- 20261001T174722Z LEG L3 closed: git b366ed9d7e: guardrails_config.json min_resolved_fraction issuer 0.23 bloomberg 0.99 home_producer 0.0 (PROVISIONAL),
- 20261001T201925Z LEG L2 closed: S3 listing after the act: issuer-site/etfs/bronze/holdings/ 654 -> 1264 objects (+610: 305 gqgu captures + 305 sidecars,
- 20261001T201925Z LEG L4 closed: G1/G5/G6 newest objects written for 307 report dates 2025-07-14..2026-09-30 (canonical_shape 853->1160, trade_schedule 8
- 20261001T201926Z LEG L5 closed: d-5.AC1 RESULT: FAIL 2 failures (clause 1: GQGU not-updated by report_date_freshness, lag 2, row Z-W4-S10; clause 2: the
- 20261001T201926Z CLOSED -- all 5 legs proven
