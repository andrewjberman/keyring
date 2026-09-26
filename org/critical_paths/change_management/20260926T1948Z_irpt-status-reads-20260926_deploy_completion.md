# Deploy Completion Record
**Date opened:** 2026-09-26T19:48:33.031592+00:00
**Status:** OPEN
**Deploy:** IRPT hops 8-9: irpt-status packages interactive_access.py (A) and irpt-status-role gains s3:GetObjectVersion on its four families (B); ~Y HOPS_8_10 @acd17573d7, CTO 101466
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | irpt-status artifact + apply | census vs deployed pfAr3uZE (exactly +interactive_access.py); safe-apply; readback CodeSha256; 0-diff replan | source map 69037884e9 (irpt-p-publish-20260923): irpt-status staged_from + files gain _scope/interactive_access.py @19d8f3038c sha256 bba07a3f4eeb947b.. (the bytes generate serves; ~Y's pin 9a3ec2a11f47 has the same sha); artifact bMMJ/bQ+5RKoYSCgAIkRwEVcMpK6kxNWt3TFdZX6wyI= 301192 bytes, S3 version 7xPCOM83IW1fRmcGpm_.t0AWyWPjG5XR; census vs live pfAr3uZE: 42 -> 43, only +interactive_access.py, 0 members differ; builder import-closure OK (32 .py); plan 0/2/0 (this code change + B1's policy); safe-apply 19:56:53Z; readback CodeSha256 bMMJ.. Active/Successful; invoke {} -> 200 CONTRACT_VERSION before and after; replan -detailed-exitcode 0 No changes | CLOSED 20260926T200145Z |
| B1 | activation | irpt-status-role policy (ops root) | plan names only the one statement's actions; safe-apply; readback policy; 0-diff replan | backend aede6418c6 (~Y's P_STATUS_READ_GRANT applied unchanged): ops/iam.tf statement ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly actions [s3:GetObject] -> [s3:GetObject, s3:GetObjectVersion], same four families and resources; plan showed only that Action change on aws_iam_role_policy.irpt_status; applied 19:56:53Z in the same safe-apply as A1; readback get-role-policy irpt-status-role/irpt-status-policy Action [s3:GetObjectVersion, s3:GetObject]; replan No changes; iam_hop8_pairs.py simulate: irpt-status-role 10 of 10 met (hop8-9 8/8 allowed incl. GetObjectVersion on both families; control-negative PutObject/DeleteObject 2/2 denied) | CLOSED 20260926T200145Z |
| V1 | verify | ~Y's proofs on the served code | status_read_proof.py no overlay 4/4 Opal owner-reads; iam_hop8_pairs.py simulate 10/10 |  | OPEN |

## Log

- 20260926T194833Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T200145Z LEG A1 closed: source map 69037884e9 (irpt-p-publish-20260923): irpt-status staged_from + files gain _scope/interactive_access.py @19d8
- 20260926T200145Z LEG B1 closed: backend aede6418c6 (~Y's P_STATUS_READ_GRANT applied unchanged): ops/iam.tf statement ReadRetainedAnalysisFamiliesUnderT
