# Deploy Completion Record
**Date opened:** 2026-10-15T20:03:26.843160+00:00
**Status:** CLOSED -- REFUSED BY GATE, nothing created -- closed 20261015T200747Z
**Deploy:** IRPT_ANLREQ TO-APPLY-t34 (round 44, AR-t-34): rebuild the transcripts zip from pin 5b438cd6c4 and apply it by one targeted safe-apply to teams-global-transcripts-pull-lambda, outlook-global-transcripts-pull-lambda, outlook-global-commentary-draft-lambda (code only, from xC1GDXXp); then ONE read-only draft_exists invoke of the commentary function
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | preconditions, rollback artifact, build, member diff exactly three, address equality, zip import | the printed reads and check lines |  | OPEN |
| V2 | verify | after reads: three CodeSha256 equal the built zip, sizes, env values and mapping unchanged | the printed reads |  | OPEN |
| V3 | verify | get_ref non-null then ONE invoke: stage draft_exists, failed empty, the INFO line present | the parsed response and the log line |  | OPEN |
| teams-global-transcripts-pull-lambda | tf-lambda | aws_lambda_function.pull | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| outlook-global-transcripts-pull-lambda | tf-lambda | aws_lambda_function.mail_pull | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| outlook-global-commentary-draft-lambda | tf-lambda | aws_lambda_function.commentary | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261015T200326Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
- 20261015T200747Z CLOSED -- REFUSED BY GATE before apply, world untouched: STOP at step 3 of TO-APPLY-t34: the built zip (pin 5b438cd6c4, base64 sha256 H0Jkkn4G..., 100 members) differs from the fetched live zip (xC1GDXXp..., 92 members) in 17 members and holds 8 more, not exactly the 3 commentary members the CTO condition requires; the 14 other changed and 8 added members are named in deliverables/A_T34_STOP_MEMBER_DIFF.txt. NOTHING WAS APPLIED, PLANNED OR INVOKED: no A
