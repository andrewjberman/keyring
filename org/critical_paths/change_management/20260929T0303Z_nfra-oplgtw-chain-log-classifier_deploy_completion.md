# Deploy Completion Record
**Date opened:** 2026-09-29T03:03:56.525728+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T031500Z
**Deploy:** OG-m-3: 49F gold dispatcher grades the chain log's terminal line (not SSM stdout) -- code + ReadTheChainLog + CHAIN_LOG_* env
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~15 <0.9.0_WK_NFRA_OPLGTW~15@opal.agent>
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| iam | verify | aws_iam_role_policy.advi_49f_gold_dispatch | get-role-policy read | get-role-policy read 2026-09-29T03:1xZ: 7 statements = 2a's set plus ReadTheChainLog (s3:GetObject on arn:aws:s3:::opal-data-49financial/gold/advi/_logs/chain_*); marker statement GetObject+GetObjectVersion unchanged; no ListBucket; dc.AC2 s3 read grants exact 2 of 2 extra 0; re-plan (with aws_ssm_document target) No changes | CLOSED 20260929T031459Z |
| advi-49f-gold-dispatch | tf-lambda | module.advi_49f_gold_dispatch (yang-lambda) | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | live CodeSha256 TjIWGFWkbUswLkA+mUac9NS+LRZ1q7o6lR1iQLb0kI4= = artifact content-sha256, moved off KqlIoAJs...; zip member lambda_function.py = HEAD bytes; env CHAIN_LOG_BUCKET=opal-data-49financial, CHAIN_LOG_PREFIX=gold/advi/_logs/chain_ = locals plus the 3 prior vars; apply 0 added 2 changed 0 destroyed | CLOSED 20260929T031459Z |

## Log

- 20260929T030356Z OPENED by 0.9.0_WK_NFRA_OPLGTW~15 <0.9.0_WK_NFRA_OPLGTW~15@opal.agent> with 2 leg(s)
- 20260929T031459Z LEG iam closed: get-role-policy read 2026-09-29T03:1xZ: 7 statements = 2a's set plus ReadTheChainLog (s3:GetObject on arn:aws:s3:::opal-
- 20260929T031459Z LEG advi-49f-gold-dispatch closed: live CodeSha256 TjIWGFWkbUswLkA+mUac9NS+LRZ1q7o6lR1iQLb0kI4= = artifact content-sha256, moved off KqlIoAJs...; zip membe
- 20260929T031500Z CLOSED -- all 2 legs proven
