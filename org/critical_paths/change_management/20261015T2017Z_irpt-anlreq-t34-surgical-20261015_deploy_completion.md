# Deploy Completion Record
**Date opened:** 2026-10-15T20:17:08.496052+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-t34 amendment_1 (route B): SURGICAL zip sha256 hUZY39qNcHdJf0fgQRHS4ckuFBT+8rU/K7VhGscaeYc= (the fetched live zip xC1GDXXp with exactly 3 commentary members from pin 5b438cd6c4; 92 members) applied by one targeted safe-apply to teams-global-transcripts-pull-lambda, outlook-global-transcripts-pull-lambda, outlook-global-commentary-draft-lambda; then ONE read-only draft_exists invoke
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | the three proofs (i) three of three byte-equal to the pin, (ii) exactly 3 members differ from live, (iii) clean -I imports, plus addr_equal ADDR-EQUAL-OK | the printed proof lines and the surgical sha |  | OPEN |
| V2 | verify | plan 0/3/0 source_code_hash only; after reads: three CodeSha256 equal the surgical zip, sizes, env values and mapping unchanged | the printed reads |  | OPEN |
| V3 | verify | get_ref non-null then ONE invoke: stage draft_exists, failed empty, the INFO line present | the parsed response and the log line |  | OPEN |
| teams-global-transcripts-pull-lambda | tf-lambda | aws_lambda_function.pull | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| outlook-global-transcripts-pull-lambda | tf-lambda | aws_lambda_function.mail_pull | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| outlook-global-commentary-draft-lambda | tf-lambda | aws_lambda_function.commentary | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261015T201708Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
