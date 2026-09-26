# Deploy Completion Record
**Date opened:** 2026-09-26T09:35:35.772120+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP rs-2: the redeploy -- opal-amgt-scoped-api carries rs-1's per-case currency rule (render_pack._case_currency / _model_case_line). Under BOTH never-widen halves: COO @4256b6ba46 (3 stop limbs) + CTO @8e2a4a808f (adds limbs 4 and 5). Prior artifact VersionId VgRYuqQ6UE3y8_4C6l1Rq8wWaXIf4j6K = the rollback; deployed CodeSha256 BEFORE = 982nlz5TEI32UQZSqFqbtVwu7/qgVLPn89tMF6kmYvo=.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | closure diff at --build-only against the DEPLOYED build input (s3 VersionId VgRYuqQ6UE3y8_4C6l1Rq8wWaXIf4j6K, content-sha256 982nlz5TEI32UQZSqFqbtVwu7/qgVLPn89tMF6kmYvo= == live CodeSha256), all FIVE stop limbs graded CLEAR BEFORE any upload | file-by-file closure diff printed + a per-limb verdict for limbs 1-5 |  | OPEN |
| L2 | verify | CTO limb 5 BASELINE: the served /print pdf OUTPUT captured BEFORE the apply, content-stream digest (raw sha moves per request on /CreationDate, so the content stream is the oracle) | pre-apply pdf content-stream digest recorded |  | OPEN |
| L3 | s3-prefix | ONE artifact write s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip -- act A of both halves; rollback = prior VersionId VgRYuqQ6UE3y8_4C6l1Rq8wWaXIf4j6K, preserved by bucket versioning, never a delete | head-object new VersionId + uploaded content-sha256 metadata == locally computed sha256 |  | OPEN |
| L4 | activation | ONE safe-apply on infra/aws/terraform/harvest/ moving ONLY opal-amgt-scoped-api's code -- act B; a plan touching a second resource is a REFUSAL | plan 0 add 1 change 0 destroy in-place + apply complete + 0-diff replan |  | OPEN |
| L5 | verify | AC1 -- the deployed code MOVED and the update is Successful | rs-2.AC1.py exit=0, CodeSha256 differs from 982nlz5TEI32UQZSqFqbtVwu7/qgVLPn89tMF6kmYvo=, LastUpdateStatus=Successful |  | OPEN |
| L6 | verify | AC2 -- served /print?format=rich over the LIVE research library with the CASES axis, read fresh; a name with no identity is reported+held+routed, never counted as an export failure | rs-2.AC2.sh exit=0: served over N of N, OK N NOT_OK 0 CAPTURE_FAILED 0, cases missing=0 extra=0 |  | OPEN |
| L7 | verify | CTO limb 5 AFTER: the served /print pdf output re-captured post-apply and graded on OUTPUT, not on the diff | post-apply pdf content-stream digest == L2 baseline digest |  | OPEN |

## Log

- 20260926T093535Z OPENED by 0.7.0_AE_CloudOps~A with 7 leg(s)
