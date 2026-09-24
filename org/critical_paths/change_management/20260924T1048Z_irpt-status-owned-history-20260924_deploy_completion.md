# Deploy Completion Record
**Date opened:** 2026-09-24T10:48:18.789444+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T105602Z
**Deploy:** irpt-status: installed owned-history handler status_installed.lambda_handler + the two table env keys + GetObject on the four retained families (CTO batch 28 (ii) / 100523)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply 0 added 2 changed 0 destroyed (safe-apply, status-owned-history.tfplan, 10:53:17Z); replan rc=0 No changes; get-function-configuration CodeSha256 5E8T+/LV4p22RfqWCyacy13I7+2QPxGIs2nuE1oVQBs= == uploaded sha (S3 version Hm2q90mPbHJRrkzE857zlUaRh5V4bujV), handler status_installed.lambda_handler, State Active / Successful, IRPT_REQUESTS_TABLE irpt-requests, IRPT_JOBS_TABLE irpt-jobs; get-role-policy: ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly GetObject x 12 ARNs; verify-on-served: invoke {} -> 200 CONTRACT_VERSION (cold compose 4609 ms, request 00b5e214-0a28-4a2d-abdd-195b54418361), unsigned history GET -> 200 NOT_AUTHORIZED with operation analysis-request-history resolved from the function's own route table (request 328500fb-0bda-47f6-9330-b5a6f75873d7); recorder 9cd8ee37ac | CLOSED 20260924T105602Z |

## Log

- 20260924T104818Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260924T105602Z LEG irpt-status closed: TF apply 0 added 2 changed 0 destroyed (safe-apply, status-owned-history.tfplan, 10:53:17Z); replan rc=0 No changes; get
- 20260924T105602Z CLOSED -- all 1 legs proven
