# Deploy Completion Record
**Date opened:** 2026-09-04T04:18:30.837931+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260904T045116Z
**Deploy:** NFRA_OPSEC202609.TO-OP-S-10C -- ADOPT opal-session-analytics into Terraform (portal-auth root), ACT ONE of TWO: an INERT import only. Config declared to match the WORLD exactly (nodejs20.x, index.handler, opal-portal-lambda-role, 256MB, 30s, TABLE_NAME/TTL_DAYS, no tags/layers/VPC). Code attributes carry lifecycle ignore_changes BECAUSE Terraform cannot read a function's code back and would otherwise propose replacing a function serving 141,685 invocations/14d. ROLLBACK: terraform state rm aws_lambda_function.session_analytics -- returns the function to unmanaged and changes NOTHING live, the same rollback partner-firms/demo.tf documents for its own adoption. Rollback is FAST: ordinary regional Lambda, no edge replication. ⛔ THIS ENTRY DOES NOT CLOSE THE BUILD-PATH QUESTION -- act one leaves the CODE managed by nothing, and act two's FIRST step is removing that ignore_changes (hazard named by 0.7.0_AE_CloudOps~V, msg 20183)
**Authored by:** 0.7.0_AE_CloudOps~W
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal-auth/session-analytics.tf committed under 0.7.0_AE_CloudOps~W | commit hash | commit ea544ac7e2 on SITEZ, author 0.7.0_AE_CloudOps~W -- portal-auth/session-analytics.tf, 194 insertions across the .tf and this ledger. terraform fmt clean, terraform validate Success. File is ASCII-only: the commit gate refused an earlier attempt on a non-ASCII character and the same rule binds production code, so the .tf was cleaned too. | CLOSED 20260904T045115Z |
| L2 | activation | terraform import aws_lambda_function.session_analytics opal-session-analytics -- state mutation only, no apply | import output | terraform import aws_lambda_function.session_analytics opal-session-analytics -- rc=0 captured directly, not through a pipe. 'Import successful!' NOT AN APPLY: import mutates Terraform state only and issues no mutating AWS call, which is why it can be run against a root carrying three foreign pending changes without landing them. | CLOSED 20260904T045115Z |
| L3 | verify | terraform plan after import MUST show NO changes to the running function; if not clean, STOP and reconcile the DECLARATION to the WORLD, never the reverse | plan output quoted | THE CONTROL FIRED TWICE BEFORE IT PASSED, and each time the DECLARATION moved rather than the world. Attempt 1: plan proposed tags_all += {Environment,ManagedBy,Project,System} (this root sets provider default_tags; the live function has none) plus publish=false. Attempt 2: tags reconciled via tags={} and ignore tags_all, same shape as waf-cloudfront.tf:239-243 in this root; publish remained. Attempt 3: publish added to ignore_changes -- declaring publish=false explicitly did NOT clear it because it is a Terraform-only meta-argument import cannot read, so state holds null and null->false renders as a change. FINAL, TWO-SIDED: HALF 1 aws_lambda_function.session_analytics appears exactly ONCE in the plan, in a 'Refreshing state...' line, and in NO change block -- zero proposed changes to the running function. HALF 2 the three PRE-EXISTING foreign changes remain present and untouched (ip_set v4, ip_set v6, web_acl) -- a clean whole-root plan would have been a FAILURE, meaning this act had swallowed another lane's pending work. Plan: 0 to add, 3 to change, 0 to destroy -- IDENTICAL to the true baseline taken with this file moved aside. 0 forces-replacement, 0 destroyed. | CLOSED 20260904T045115Z |
| L4 | verify | live function UNTOUCHED across the import: CodeSha256, LastModified, Handler, Runtime, MemorySize, Timeout, Environment identical before and after | paired live reads | Live function UNTOUCHED across the import, paired reads before and after: CodeSha256 eQswWf3zdISgafQwQ+GhHgyWNfoxPOSeriqYVxiN9VU= identical; LastModified 2026-01-08T15:31:07.000+0000 identical; Handler index.handler, Runtime nodejs20.x, MemorySize 256, Timeout 30, Environment TABLE_NAME=opal-sessions TTL_DAYS=90 all identical; list-tags returns {} before and after, so the four default_tags were NOT applied. The adoption is provably inert on the live plane. | CLOSED 20260904T045115Z |

## Log

- 20260904T041830Z OPENED by 0.7.0_AE_CloudOps~W with 4 leg(s)
- 20260904T045115Z LEG L1 closed: commit ea544ac7e2 on SITEZ, author 0.7.0_AE_CloudOps~W -- portal-auth/session-analytics.tf, 194 insertions across the .t
- 20260904T045115Z LEG L2 closed: terraform import aws_lambda_function.session_analytics opal-session-analytics -- rc=0 captured directly, not through a p
- 20260904T045115Z LEG L3 closed: THE CONTROL FIRED TWICE BEFORE IT PASSED, and each time the DECLARATION moved rather than the world. Attempt 1: plan pro
- 20260904T045115Z LEG L4 closed: Live function UNTOUCHED across the import, paired reads before and after: CodeSha256 eQswWf3zdISgafQwQ+GhHgyWNfoxPOSeriq
- 20260904T045116Z CLOSED -- all 4 legs proven
