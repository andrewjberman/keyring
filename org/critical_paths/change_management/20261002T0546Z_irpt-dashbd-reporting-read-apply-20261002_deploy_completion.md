# Deploy Completion Record
**Date opened:** 2026-10-02T05:46:42.043635+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-5: apply the reporting-read root (8 new resources; packet blob f44ee4d312, CTO half batch 115)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | re-plan of reporting-read at HEAD | 8 to add, 0 to change, 0 to destroy; trees equal to @81bc2e6f4f |  | OPEN |
| D1 | activation | safe-apply of infra/aws/terraform/investor-reporting/reporting-read | apply complete, 8 added |  | OPEN |
| V1 | verify | post-apply readback | CodeSha256 dKMqVb..., route on CUSTOM naqxlm, 17 existing routes unchanged, re-plan No changes |  | OPEN |
| N1 | verify | negative control | unauthenticated GET refused by the authorizer; no invocation logged |  | OPEN |
| A1 | verify | workstream F signed-in fetch (FWD-1 real run) | one covered account's series fetched through the route, as-of 2026-09-28 shown |  | OPEN |

## Log

- 20261002T054642Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
