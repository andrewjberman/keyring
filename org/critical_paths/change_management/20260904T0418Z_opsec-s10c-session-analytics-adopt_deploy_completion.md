# Deploy Completion Record
**Date opened:** 2026-09-04T04:18:30.837931+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-10C -- ADOPT opal-session-analytics into Terraform (portal-auth root), ACT ONE of TWO: an INERT import only. Config declared to match the WORLD exactly (nodejs20.x, index.handler, opal-portal-lambda-role, 256MB, 30s, TABLE_NAME/TTL_DAYS, no tags/layers/VPC). Code attributes carry lifecycle ignore_changes BECAUSE Terraform cannot read a function's code back and would otherwise propose replacing a function serving 141,685 invocations/14d. ROLLBACK: terraform state rm aws_lambda_function.session_analytics -- returns the function to unmanaged and changes NOTHING live, the same rollback partner-firms/demo.tf documents for its own adoption. Rollback is FAST: ordinary regional Lambda, no edge replication. ⛔ THIS ENTRY DOES NOT CLOSE THE BUILD-PATH QUESTION -- act one leaves the CODE managed by nothing, and act two's FIRST step is removing that ignore_changes (hazard named by 0.7.0_AE_CloudOps~V, msg 20183)
**Authored by:** 0.7.0_AE_CloudOps~W
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal-auth/session-analytics.tf committed under 0.7.0_AE_CloudOps~W | commit hash |  | OPEN |
| L2 | activation | terraform import aws_lambda_function.session_analytics opal-session-analytics -- state mutation only, no apply | import output |  | OPEN |
| L3 | verify | terraform plan after import MUST show NO changes to the running function; if not clean, STOP and reconcile the DECLARATION to the WORLD, never the reverse | plan output quoted |  | OPEN |
| L4 | verify | live function UNTOUCHED across the import: CodeSha256, LastModified, Handler, Runtime, MemorySize, Timeout, Environment identical before and after | paired live reads |  | OPEN |

## Log

- 20260904T041830Z OPENED by 0.7.0_AE_CloudOps~W with 4 leg(s)
