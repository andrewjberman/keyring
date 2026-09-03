# Deploy Completion Record
**Date opened:** 2026-09-03T21:05:29.869637+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-29 -- opal-data-security's two service grants get the source conditions C-16 already claims: aws:SourceAccount added to the ALB grant (CloudFront already had it), and aws:SourceArn added to NEITHER because no instrument establishes that either principal sends one. The remediation half of row Z-S60
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | s3.tf ALB grant gains aws:SourceAccount, committed under 0.7.0_AE_CloudOps~S, with the UNSCOPED baseline quoted and the PRE-APPLY DENOMINATOR captured BEFORE the edit | commit hash + baseline + both prefix counts |  | OPEN |
| L2 | activation | safe-apply -- 0 to add, 1 to change (aws_s3_bucket_policy.data_security IN-PLACE), 0 to destroy, 0 forces-replacement, and ZERO other resources in the changed list -- ROLLBACK: the PRIOR POLICY DOCUMENT captured verbatim before the edit, 874 bytes sha256 f7d19e28aae82709, restorable by put-bucket-policy or by reverting the one condition line and re-applying | apply output + enumerated changed list |  | OPEN |
| L3 | verify | S29-AC1 -- get-bucket-policy AFTER with both service statements quoted in full, showing aws:SourceAccount present on EACH. Denominator 2 of 2 grants. BEFORE quoted from the face: CloudFront present, ALB absent | pasted policy |  | OPEN |
| L4 | verify | S29-AC3 THE CONTROL THAT MUST BE ABLE TO FAIL -- both live legs still delivering AFTER the apply, at least one object with LastModified STRICTLY AFTER the apply timestamp, against the pre-apply denominator. THE ALB LEG DOES NOT GET AN UNCOMPUTABLE BRANCH: it was measured delivering continuously, so a stop there is a regression THIS task order caused, and it is the leg whose grant just gained an untested condition. The CloudFront leg MAY file UNCOMPUTABLE if genuinely idle, with its pre-apply rate as evidence | list-object-versions per prefix with the apply timestamp |  | OPEN |
| L5 | verify | S29-AC4 -- nothing else on the bucket moved: UNSCOPED re-plan after, plus a re-read confirming encryption still AES256 and NOT the project CMK, versioning still Enabled, four public-access blocks still true, waf-logs lifecycle unchanged | plan + pasted reads |  | OPEN |
| L6 | verify | S29-AC5 -- ledger CLOSED on the artifact with the prior policy named as rollback; push state MEASURED by ls-remote + is-ancestor | ledger + ls-remote |  | OPEN |

## Log

- 20260903T210529Z OPENED by 0.7.0_AE_CloudOps~S with 6 leg(s)
