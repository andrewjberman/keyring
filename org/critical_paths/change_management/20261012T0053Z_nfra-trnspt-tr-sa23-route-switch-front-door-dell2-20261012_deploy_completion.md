# Deploy Completion Record
**Date opened:** 2026-10-12T00:53:02.723907+00:00
**Status:** OPEN
**Deploy:** NFRA_TRNSPT TR-sa-23: edit commentary.tf line 72 (.api_base -> .portal_base), rebuild transcripts-pull.zip at box/dell2 HEAD (pin c942202bf9), and apply in ONE targeted safe-apply to aws_lambda_function.pull, .mail_pull and .commentary -- code on all three plus the ONE environment value TICKET_API_BASE on .commentary; then ONE invoke of each pull and ONE signed probe post through the front door; NO invoke of the commentary function
**Authored by:** 0.7.0_AE_CloudOps~TR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | precondition reads: three functions CodeSha256 == auyn4IvltKLLl6yw+SsMWGi3VVlYZKnmJKFssjJaVNY=, MemorySize 1024/1024/512, Timeout 300/600/300; the commentary function's WHOLE environment by NAME plus the value of TICKET_API_BASE (expected the runner config's api_base); event source mapping 1 Enabled; commentary invocation count since 2026-10-12T00:00Z; the on-disk dist zip's base64 sha256 | every read printed, with the on-disk zip hash and the environment name set |  | OPEN |
| L2 | verify | rollback artifact: deployed package fetched from get-function, held OUTSIDE the repo, base64 sha256 printed and equal to auyn4Ivl... | the fetched zip's hash printed before the plan |  | OPEN |
| L3 | git | the Terraform edit in this lane: infra/aws/terraform/transcripts/commentary.tf line 72, the one token .api_base -> .portal_base with its comment brought into line, nothing typed; then build.sh | the commit hash, the built zip's hash and member count, the HEAD built from, and an EMPTY diff of the three pinned members against c942202bf9 |  | OPEN |
| L4 | verify | ADDRESS EQUALITY on the BUILT zip: addr_equal.py printing ADDR-EQUAL-OK teams=14/14 mail=7/7 control=discriminates | the ADDR-EQUAL-OK line at rc=0 |  | OPEN |
| L5 | activation | safe-apply in infra/aws/terraform/transcripts targeted at exactly aws_lambda_function.pull, aws_lambda_function.mail_pull, aws_lambda_function.commentary -- plan 0 add / 3 change / 0 destroy; source_code_hash on .pull and .mail_pull, source_code_hash plus the ONE environment value TICKET_API_BASE on .commentary whose new value equals the runner config's portal_base (CTO condition 1) | the safe-apply receipt and the plan's exact changed-attribute set read from the plan JSON |  | OPEN |
| L6 | verify | AFTER reads: all three CodeSha256 == the built zip's hash; MemorySize 1024/1024/512 and Timeout 300/600/300 unchanged; the commentary environment carries the SAME NAMES as L1 and ONLY TICKET_API_BASE differs in value; event source mapping still 1 Enabled; the commentary log shows NO new invocation across the act | the readbacks, the name-set and per-value comparison, and the flat invocation count |  | OPEN |
| L7 | verify | PROOF 7(b) driven: ONE invoke of teams-global-transcripts-pull-lambda and ONE of outlook-global-transcripts-pull-lambda, graded as in TO-APPLY-ca23 step 7; any landing reported with its series and count before the ledger closes | both invoke results graded against the packet |  | OPEN |
| L8 | verify | PROOF 7(c), the probe exactly as the CTO signed it: ONE post with the service bearer to <portal_base>/api/scoped/tickets/PROBE-NOSUCH-0/commentary-draft with ONE EXTRA body key. PASS = 400 application/json naming the unexpected field. 403, 401, HTML or 5xx = a finding and the base is ROLLED BACK. A denied secret read = NOT MADE, no grant sought, and no rollback on that alone. Status and content type read as PARSED values, never a captured output compared whole (CTO condition 3). The bearer is never printed | the parsed status integer, the parsed content type, and whether the body names the unexpected field |  | OPEN |
| L9 | verify | proof instance: python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R23_CHECKS/r23_checks.py sa23 prints R23-SA23-OK | the check line at rc=0 |  | OPEN |
| L10 | git | commit of the proof instance, the applier's report and the session log under 0.7.0_AE_CloudOps~TR2 via safe-commit.sh | commit hashes read with an author filter and the measured push state |  | OPEN |

## Log

- 20261012T005302Z OPENED by 0.7.0_AE_CloudOps~TR2 with 10 leg(s)
