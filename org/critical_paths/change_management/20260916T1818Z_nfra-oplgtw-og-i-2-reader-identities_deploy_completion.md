# Deploy Completion Record
**Date opened:** 2026-09-16T18:18:21.199253+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-i-2: Schwab reader identities -- data role opal-mcp-emp-menachem-schwab-read, catalog role opal-mcp-schwab-catalog-read, one assume statement on opal-gateway-role, ExternalIds secret and account_ref key secret with Gateway read resource policies
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | infra/aws/terraform/opal-gateway/schwab_reader_iam.tf committed on wk-nfra_oplgtw-1-1c BEFORE the apply, with this entry and its OPEN sentinel | commit hash |  | OPEN |
| L2 | activation | terraform apply of infra/aws/terraform/opal-gateway through .tools/safe-apply.sh creating exactly the ten OG-i-2 resources, 0 to change, 0 to destroy, judged by the in-run guard | safe-apply rc 0 and the Apply complete line |  | OPEN |
| L3 | verify | source bucket opal-data-assets policy sha256 read immediately before and immediately after the apply are equal (no bucket policy change) | pre and post read times and sha256 |  | OPEN |
| L4 | activation | the alias-key secret opal/mcp/opal-gateway-schwab-account-ref-key receives its FIRST value out-of-band in the OG-z-3 JSON shape, value never recorded | version id and read-back shape |  | OPEN |

## Log

- 20260916T181821Z OPENED by 0.9.0_WK_NFRA_OPLGTW~1 with 4 leg(s)
