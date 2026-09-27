# Deploy Completion Record
**Date opened:** 2026-09-27T21:37:21.557169+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter role: render-grant kms:Decrypt under the S3 Bucket Key (bucket-ARN context, core key only); backend <kms commit>; CTO 102135; policy only 0/1/0; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | performance root safe-apply | both halves at HEAD naming the packet blob; plan 0/1/0 this policy only; safe-apply; live policy readback equal; simulator positive + negative arms; replan 0 | Both halves at HEAD naming blob f7aa7b3c (@03de7272cd): CRO @b994f81153 102149 (no ask), CTO @11eedb85ae 102153 (named item: live get-role-policy readback beside the planned statement). safe-apply kmsfix.tfplan (performance root, backend c8572cb1bd, null plan tfvars): Apply complete 0 added / 1 changed / 0 destroyed at 21:50:13Z. LIVE get-role-policy DecryptRenderGrantsViaS3Only: Resource [arn:aws:kms:us-east-1:313476888478:key/7f4d3042-10d8-49a7-b55e-3c963cea8111], Condition StringEquals {kms:EncryptionContext:aws:s3:arn: arn:aws:s3:::opal-data-ycharts, kms:ViaService: s3.us-east-1.amazonaws.com}; PLANNED identical -> EQUAL. Live role simulator: kms:Decrypt with the bucket context allowed; s3:GetObject of narrative_packet.json in the same folder implicitDeny (negative arm). Re-plan: no changes (detailed-exitcode 0). Adapter code unchanged bOefL9nx, no plan. | CLOSED 20260927T215158Z |
| A1 | verify | next K8 window | the render's Performance read as RENDER_DELEGATE succeeds (no AccessDenied); READY %PDF |  | OPEN |

## Log

- 20260927T213721Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260927T215158Z LEG D1 closed: Both halves at HEAD naming blob f7aa7b3c (@03de7272cd): CRO @b994f81153 102149 (no ask), CTO @11eedb85ae 102153 (named i
