# Deploy Completion Record
**Date opened:** 2026-10-20T07:00:18.187037+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T071353Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R37 v2: irpt-ycharts-generate (the upload door) -- served.py O1 owner fallback and ticket_confirmation.py creator stamp; 2 of 107 members move
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | investor-reporting/irpt-ycharts-generate.zip new latest version, sha256 3e50a336, CodeSha256 PlCjNms/RRLRB/c15zW8Sdzl7w3ptodi3o8sSxnWjYA= (rollback: the R0 latest VersionId) | digest, read-back | uploaded VersionId gY39LYe321yWZLPHcyP5CjdB.wawFQEL, sha256 3e50a336..., 639224 bytes, built digest PlCjNms/RRLRB/c15zW8Sdzl7w3ptodi3o8sSxnWjYA= equals the expected; rollback VersionId q.dgcHo9eVEsvflc0BMYEshY.tL2nNbK kept | CLOSED 20261020T071352Z |
| C | tf-lambda | scoped plan 0/1/0 on module.irpt_ycharts_generate.aws_lambda_function.this, ONE safe-apply | plan counts, CodeSha256 | scoped plan 0 add 1 change 0 destroy (last_modified, s3_object_version, source_code_hash only), ONE safe-apply 2026-10-20T07:09:59Z-07:11:01Z from trunk 77968aef12, scoped re-plan No changes | CLOSED 20261020T071352Z |
| V | verify | after-reads G1 to G4 | S1 to S4 lines | G1 CodeSha256 equals PlCjNms/...; G2 2 of 107 differ (served.py, ticket_confirmation.py), none added or removed; G3 envelope equal (401, same body sha256); G4 census changed_members 0; map record merged at 2465dc5f5d3 | CLOSED 20261020T071352Z |

## Log

- 20261020T070018Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
- 20261020T071352Z LEG U closed: uploaded VersionId gY39LYe321yWZLPHcyP5CjdB.wawFQEL, sha256 3e50a336..., 639224 bytes, built digest PlCjNms/RRLRB/c15zW8
- 20261020T071352Z LEG C closed: scoped plan 0 add 1 change 0 destroy (last_modified, s3_object_version, source_code_hash only), ONE safe-apply 2026-10-2
- 20261020T071352Z LEG V closed: G1 CodeSha256 equals PlCjNms/...; G2 2 of 107 differ (served.py, ticket_confirmation.py), none added or removed; G3 enve
- 20261020T071353Z CLOSED -- all 3 legs proven
