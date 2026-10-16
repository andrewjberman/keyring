# Deploy Completion Record
**Date opened:** 2026-10-16T07:53:23.936651+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-t54 (AR-tf-76): FWD-4 commentary hop, three artifacts one at a time at HEAD 8da0127c5b: G the inline policy of irpt-commentary-draft-store-role gains S6 and S7; D the draft-store zip (commentary_draft_store.py changed, durable_job.py added; BUILD_ONLY twice, digest recorded before deploy); C the SURGICAL commentary zip (lambda_handler.py replaced); P the driven proof on the synthetic row REQ-d47252fe74634d0c5cdd8067, restored; COO packet blob 8dcbccc512, CTO half msg 9181
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G | verify | irpt-commentary-draft-store-role inline policy S6 and S7 (draft-store root, one resource in place) | simulate battery, plan 0/1/0, safe-apply, re-plan No changes, Sids S1 to S7 | validate Success; unscoped plan read 2 changes (the policy and the Lambda whose 3 attributes are only known-after-apply because the S3 artifact data source is read during apply); SCOPED plan -target the policy: 0 add 1 change 0 destroy, attribute policy only, equal to the simulated document; simulate battery 10 rows + 2 controls OK; safe-apply 0 added 1 changed 0 destroyed; re-plan No changes; Sids S6 S7 S1 to S5 read live | CLOSED 20261016T082516Z |
| P | verify | driven proof on synthetic row REQ-d47252fe74634d0c5cdd8067 plus two negative arms, restored | the answers, the row before and after, the restore read ABSENT |  | OPEN |
| irpt-commentary-draft-store-lambda | tf-lambda | module.irpt_commentary_draft_store.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| outlook-global-commentary-draft-lambda | tf-lambda | aws_lambda_function.commentary | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261016T075323Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261016T082516Z LEG G closed: validate Success; unscoped plan read 2 changes (the policy and the Lambda whose 3 attributes are only known-after-apply 
