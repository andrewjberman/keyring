# Deploy Completion Record
**Date opened:** 2026-10-11T21:00:40.672846+00:00
**Status:** OPEN
**Deploy:** NFRA_TRNSPT TR-ca-23: rebuild transcripts-pull.zip at box/dell2 HEAD 4fb80c408c (pin 615010e8bf) and apply it CODE-ONLY to aws_lambda_function.pull, .mail_pull and .commentary in ONE targeted safe-apply; then ONE driven invoke of the Teams pull and ONE of the mail pull; NO invoke of the commentary function
**Authored by:** 0.7.0_AE_CloudOps~TR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | precondition reads: three functions CodeSha256 == AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=, MemorySize 1024/1024/512, Timeout 300/600/300, commentary event source mapping 1 Enabled, commentary invocation count since 2026-10-11T00:00Z, on-disk dist zip hash (row D2-S31) | the four reads printed with the on-disk zip hash |  | OPEN |
| L2 | verify | rollback artifact: deployed package fetched from get-function, stored OUTSIDE the repo, base64 sha256 printed and equal to AI4UQD0M... | fetched zip hash printed before the plan (CTO condition 4) |  | OPEN |
| L3 | verify | BUILD + ADDRESS EQUALITY on the BUILT zip (CTO condition 2): build.sh at HEAD, built hash and member count, git diff 615010e8bf..HEAD over the packet's 10 section-1 members EMPTY, addr_equal.py printing ADDR-EQUAL-OK teams=14/14 mail=7/7 control=discriminates | built hash + empty 10-member diff + the ADDR-EQUAL-OK line |  | OPEN |
| L4 | activation | safe-apply in infra/aws/terraform/transcripts targeted at exactly aws_lambda_function.pull, aws_lambda_function.mail_pull, aws_lambda_function.commentary -- plan 0 add / 3 change / 0 destroy, source_code_hash only (CTO condition 1) | safe-apply receipt and the exact plan line |  | OPEN |
| L5 | verify | AFTER reads: all three CodeSha256 == the built zip hash; MemorySize 1024/1024/512 and Timeout 300/600/300 unchanged; commentary event source mapping still 1 Enabled; commentary log shows NO new invocation across the act | the readbacks and the flat invocation count |  | OPEN |
| L6 | verify | PROOF driven: ONE invoke of teams-global-transcripts-pull-lambda (no errorMessage, 4 series, totals carrying read_refused expected 4, run record + listing snapshot exist) and ONE of outlook-global-transcripts-pull-lambda (one MAIL-PULL-FIRE line, window_days=7, list_refusals=0); NO invoke of outlook-global-commentary-draft-lambda; any landing reported with its series and count | both invoke results graded against packet section 4 |  | OPEN |
| L7 | verify | proof instance: python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R23_CHECKS/r23_checks.py ca23 prints R23-CA23-OK | the check line |  | OPEN |
| L8 | git | commit of the proof instance, ledger and lane deliverables under 0.7.0_AE_CloudOps~TR2 via safe-commit.sh | commit hash and measured push state |  | OPEN |

## Log

- 20261011T210040Z OPENED by 0.7.0_AE_CloudOps~TR2 with 8 leg(s)
