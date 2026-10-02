# Deploy Completion Record
**Date opened:** 2026-10-02T09:05:07.399051+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T090943Z
**Deploy:** ETFS_RIVALS FAST: CRO~RV CALL 8 split guard (pin CLOUD 2a9a11a025, plan 0/5/0) + 2026-10-01 rebuild and republish
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds saved plan /c/tmp/rv_apply4.tfplan (5 Lambdas source_code_hash; no policy) | apply output: Apply complete 0 added 5 changed 0 destroyed | ledger committed 60cfc1d14a BEFORE the apply (&&); safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan /c/tmp/rv_apply4.tfplan from /c/tmp/rv-apply detached at 2a9a11a025, 09:06:22Z): Apply complete! Resources: 0 added, 5 changed, 0 destroyed; tagauthz PASSED; tombstone CLEAN | CLOSED 20261002T090659Z |
| D2 | verify | five CodeSha256 after apply differ from the 0d4b3f6e4d set | get-function output | CodeSha256 after (all Successful): etfs-rivalfunds-daily-lambda 02zhwL+K.. etfs-rivalfunds-fetch-holdings-lambda izhloOpa.. rivalfunds-build-canonical-shape-lambda gTzFpzuO.. rivalfunds-build-silver-lambda bbdszizR.. rivalfunds-publish-page-lambda w5yrc9aX.. -- every one differs from the 0d4b3f6e4d set | CLOSED 20261002T090708Z |
| D3 | activation | rebuild + republish 2026-10-01: daily-lambda only publish-page refresh_a1, batch fast-a1-publish-1001d | request id + marker + new holding_contribution revision | daily-lambda only publish-page refresh_a1, date 2026-10-01, batch fast-a1-publish-1001d (09:07-09:08Z), PARTIAL by GQGU freshness as before; marker state/publish_page/date=2026-10-01/fast-a1-publish-1001d.json; holding_contribution rebuilt -> holding_contribution-20261002T090746Z-371779fe0d1c; index 1,578,676 bytes | CLOSED 20261002T090943Z |
| D4 | verify | moved fields: BASG/GQGU/CGIC YTD, 5 refused rows with reasons, the 7 newly priced days | S3 readback | moved fields read back 09:0xZ: YTD BASG +10.15% GQGU +6.35% CGIC +5.87%; exactly 5 refused rows (BIDD KMB IN 01-13 r=0.1995 and 01-14 r=4.9466, GQGU Amphenol 09-02 r=0.4905, TXUE AZN LN 02-02 r=2.0207: corporate_action_suspected; CGIC IBE/D SM 07-07 r=43561: implausible_valuation); the 7 real moves priced with 0 refused days (BASG Datadog +2.09% rank 2, Intuit -1.95%; GQGU Snowflake, Atlassian; CGIC 8283 JP, VAL SJ, IMP SJ); audit table 5 rows, 7 captions, no script | CLOSED 20261002T090943Z |

## Log

- 20261002T090507Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)
- 20261002T090659Z LEG D1 closed: ledger committed 60cfc1d14a BEFORE the apply (&&); safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan /c/tmp/rv_apply4.t
- 20261002T090708Z LEG D2 closed: CodeSha256 after (all Successful): etfs-rivalfunds-daily-lambda 02zhwL+K.. etfs-rivalfunds-fetch-holdings-lambda izhloOp
- 20261002T090943Z LEG D3 closed: daily-lambda only publish-page refresh_a1, date 2026-10-01, batch fast-a1-publish-1001d (09:07-09:08Z), PARTIAL by GQGU 
- 20261002T090943Z LEG D4 closed: moved fields read back 09:0xZ: YTD BASG +10.15% GQGU +6.35% CGIC +5.87%; exactly 5 refused rows (BIDD KMB IN 01-13 r=0.1
- 20261002T090943Z CLOSED -- all 4 legs proven
