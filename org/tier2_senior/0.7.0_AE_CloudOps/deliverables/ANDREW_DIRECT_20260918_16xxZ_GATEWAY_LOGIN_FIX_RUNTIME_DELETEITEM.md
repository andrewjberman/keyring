# ANDREW-DIRECT 2026-09-18 ~16:1xZ -- Gateway login outage: apply the IAM fix (runtime DeleteItem on RUNTIME#*)

**Recorded by:** `0.7.0_AE_CloudOps` | **Channel:** direct session prompt (this seat's own terminal) | **Andrew's words, verbatim:**

> "Go ahead with the fix"

**What the word answers.** This seat's report to Andrew (same session, ~15:5xZ) named two remedy branches for
the Gateway login outage and recommended branch 1:

1. **IAM (recommended):** add `dynamodb:DeleteItem` to the `AccessStateRuntimeWritesRuntimeKeysOnly` statement of
   `aws_iam_role_policy.gw_access_state_runtime` (`infra/aws/terraform/opal-gateway/schwab_access_state.tf`), under
   the SAME `dynamodb:LeadingKeys = RUNTIME#*` condition. One line of Terraform, `safe-apply`, no code deploy, no
   restart, reversible by removing the action.
2. **Code:** convert `oauth_as.py:649` / `:772` to a conditional `UpdateItem` marking `consumed_at`; tests, a release
   through OG-r-1's route, and a restart.

The report ended: *"Say 'apply 1' and I do it now under a ledger entry via safe-apply."* Andrew's reply is the
sentence above. It is read as authorizing **branch 1**, the branch the report recommended and the only one the
sentence "the fix" resolves to in that context.

**Scope, held narrow.** The word covers ONE act: the IAM policy change on the Gateway instance role's runtime grant,
applied through `.tools/safe-apply.sh` under a change-management ledger entry. It does NOT cover: the code branch,
attaching an Elastic IP, any change to `oauth_as.py`, any change to NFRA_OPLGTW's task orders, decomposition or PRD
(the record contradiction with `OGI1-AC5` / `NFRA_OPLGTW_DECOMP.md:183` / `probes/og_i1.py:415` is the CTO's addendum
to cut), or any other Gateway surface.

**Why this needed his word at all.** The change contradicts a ratified acceptance criterion of a complete cell
(`OGI1-AC5`: "no DeleteItem") of a project mid-round with a frozen spec. The contract itself
(`org/standards/NFRA_OPLGTW_CONTRACT.json` v1.1 `state_store.key_namespaces.RUNTIME` = "runtime conditional writes
and expiring records") does not forbid the delete; the ban was introduced at the decomposition grain. A seat does
not widen or narrow an access-control value on its own; Andrew is the sovereign over that value.

**Root cause the fix addresses** (measured this session, host journal via SSM + DynamoDB scan + TF + deployed bytes):
`/callback` returns 503 after every successful Entra sign-in because `oauth_as.take_pending()` calls
`access_state.delete_runtime()` -> `dynamodb:DeleteItem`, which the runtime grant does not hold
(`AccessDeniedException`, journal 14:55:37Z and 15:16:07Z). Login has been impossible since the OG-r-1 deploy of the
durable-OAuth build at 05:58:16Z 2026-09-18. The OG-i-4 stop/start (14:53Z) did not cause it.

**Ledger:** slug `nfra-oplgtw-gw-runtime-deleteitem`, `org/critical_paths/change_management/` (opened before the
act, closed after the exercised verification).
