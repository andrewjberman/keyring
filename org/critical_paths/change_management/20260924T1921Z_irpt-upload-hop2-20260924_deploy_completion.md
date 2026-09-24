# Deploy Completion Record
**Date opened:** 2026-09-24T19:21:19.302731+00:00
**Status:** OPEN
**Deploy:** IRPT Analysis upload hops 2+3: ycharts-root grants, resident package with RESOLVE_UPLOAD, irpt-ycharts-generate rebuild (Y bb1eb7f92b/10a16bd89d/d16b7c8743, P a58859baa7 + 19b38e2f22)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| G1 | activation | ycharts root: aws_iam_role_policy.generate + runner_resident | safe-apply of the saved plan 0/2/0; 0-diff replan | safe-apply (HALT_ACK=1, terraform 1.9.8, backend worktree ycharts root) of the saved plan 0 add / 2 change / 0 destroy at 19:22Z: aws_iam_role_policy.generate + Sid RetainOriginalHoldingsUploadsOnly (s3 Put/Get/GetVersion on opal-data-irpt/irpt/{49financial,cottonwood,inflection}/state/original_holdings/*); aws_iam_role_policy.runner_resident write families + NORMALIZED_PORTFOLIO, read families REQUEST_COMPOSITION + ORIGINAL_HOLDINGS, KMS StringLike lists follow; prefixes derived from infra/logic/registry/reporting_policies.json (CLOUD blob 925fbbdc08, M's ACTIVE registry); re-plan -detailed-exitcode rc=0 No changes 19:22Z | CLOSED 20260924T192301Z |
| R1 | activation | resident package on i-0167fd745ad906a66 carrying resident_worker resolve_upload | SSM install rc 0; unit active; IRPT_RESIDENT_POLL lines; manifest sha |  | OPEN |
| L1 | activation | irpt-ycharts-generate artifact + apply | census vs deployed; safe-apply; readback CodeSha256; 0-diff replan; recorder |  | OPEN |
| S1 | verify | live upload acceptance | Andrew posts the 12.03 template: RESOLVING, one IRPT_RESIDENT_POLL handled=1, NORMALIZED with total_dollars 12.03 |  | OPEN |

## Log

- 20260924T192119Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260924T192301Z LEG G1 closed: safe-apply (HALT_ACK=1, terraform 1.9.8, backend worktree ycharts root) of the saved plan 0 add / 2 change / 0 destroy a
