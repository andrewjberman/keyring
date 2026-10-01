# Deploy Completion Record
**Date opened:** 2026-10-01T21:51:55.887030+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T221248Z
**Deploy:** ETFS_RIVALS RIV-d-5 addendum 1: five Lambdas in place to the q-1 G2 fix (rows Z-W4-S12/S13), G2 holdings_coverage replay, page republish
**Authored by:** 0.9.0_WK_ETFS_RIVALS~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas source_code_hash in place; no create/destroy/policy) | apply output: Apply complete 0 added 5 changed 0 destroyed | safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T21:54Z): Apply complete! Resources: 0 added, 5 changed, 0 destroyed; plan = 5 aws_lambda_function in place (source_code_hash + last_modified) only (evidence/apply_plan_a1.txt); tagauthz and tombstone gates clean; code pin 35d94bd5e3 (CLOUD 25f4ac5418 + ledger commit); CodeSha256 after: daily C/lTSdk7.. fetch-holdings sLwaf78F.. canonical-shape DSDRr5th.. silver bDpv4Qks.. publish-page rphyMKON.. (evidence/lambda_after_apply_a1.txt) | CLOSED 20261001T215632Z |
| A2 | activation | G2 holdings_coverage replay over 2025-07-14..2026-09-30 (GQGU +307 rows, others byte-equal) | Lambda request ids + per-fund G2 rows | daily-lambda build-coverage only, replay 2025-07-14..2026-09-30, batch d5-g2-a1-full, request e83248aa-b484-401c-a48d-a8cdbfed971e (354.5 s, status OK, written_new 307 days); read back all 502 coverage objects: rows per fund equal the addendum table (GQGU 307, BASG 645, BIDD 471, CGIC 502, ETFT 208, IDVZ 28, INEQ 502, PCLG 240, PFOE 27, SCHY 502, TSEL 438, TXUE 420, WCMG 111; 0 mismatches); 305 GQGU rows name a gqgu- capture, 0 BASG rows name one (evidence/g2_readback_a1.txt) | CLOSED 20261001T220325Z |
| A3 | activation | republish page 2026-10-01 (new object) | publish marker + request id | daily-lambda publish-page only, date 2026-10-01, batch d5-publish-a1, request 8a6012e1-a017-40d4-a673-5fc06dec76e4 (8.4 s): marker state/publish_page/date=2026-10-01/d5-publish-a1.json; page index.html + manifest.json new revision; GQGU block data-calendar status ok, 20 days, issuer badge; funds_updated 12 of 13 | CLOSED 20261001T221248Z |
| A4 | verify | d-5.AC1 AC2 AC3 re-run; d5_live.json addendum1 | AC RESULT lines | d-5.AC1 RESULT: PASS 0 failures; d-5.AC2 RESULT: PASS 0 failures (382 s); d-5.AC3 RESULT: PASS 0 failures; d5_live.json addendum1 written (evidence/d-5.AC*.a1.output.txt) | CLOSED 20261001T221248Z |

## Log

- 20261001T215155Z OPENED by 0.9.0_WK_ETFS_RIVALS~4 with 4 leg(s)
- 20261001T215632Z LEG A1 closed: safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T21:54Z): Apply complete! Resources: 0 added, 5 changed, 0
- 20261001T220325Z LEG A2 closed: daily-lambda build-coverage only, replay 2025-07-14..2026-09-30, batch d5-g2-a1-full, request e83248aa-b484-401c-a48d-a8
- 20261001T221248Z LEG A3 closed: daily-lambda publish-page only, date 2026-10-01, batch d5-publish-a1, request 8a6012e1-a017-40d4-a673-5fc06dec76e4 (8.4 
- 20261001T221248Z LEG A4 closed: d-5.AC1 RESULT: PASS 0 failures; d-5.AC2 RESULT: PASS 0 failures (382 s); d-5.AC3 RESULT: PASS 0 failures; d5_live.json 
- 20261001T221248Z CLOSED -- all 4 legs proven
