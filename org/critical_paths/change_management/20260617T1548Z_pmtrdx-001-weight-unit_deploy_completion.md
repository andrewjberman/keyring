# Deploy Completion Record
**Date opened:** 2026-06-17T15:48:45.053340+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260617T161555Z
**Deploy:** PMTRDX.001 trade-weight unit fix (financial path): PATCH1 producer divide-100 + weight_unit=fraction, PATCH2 excel-gens x100-on-read (broker byte-identical), PATCH3 remediation
**Authored by:** 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| patch1-producer | activation | opal-portfolio-excel-generator | deployed CodeSha256 == new zip sha256 (terraform apply repoint) | APPLIED via safe-apply (portfolio-management, saved plan, 1 change repoint-only). EGRESS-VERIFIED: opal-portfolio-excel-generator CodeSha256=3KhyVvll..=new zip sha; LastModified 2026-06-17T15:55:13Z. weight_unit=fraction + ÷100 live. | CLOSED 20260617T155711Z |
| patch2-excel-gens | activation | trade-workflow-handler + trade-dashboard-api | both deployed CodeSha256 == new zip sha256 | APPLIED via safe-apply (trade-pipeline, saved plan, 2 changes repoint-only). EGRESS-VERIFIED: trade-workflow-handler CodeSha256=jKU+Mk.. + trade-dashboard-api CLpMor.. = new zip shas; LastModified 15:55:57Z. Broker Excel byte-identical (empirical proof 4a4360909). | CLOSED 20260617T155711Z |
| patch3-remediation | verify | DDB PENDING_APPROVAL source=portfolio_export records | COO-gated --apply after clean dry-run (idempotent + scoped) | remediate --apply on 2 records (AMZN TRADE-20260617-144856-MKYYDP + AMD TRADE-20260602-135824-9CHHWS). LIVE-DDB post-verify (not rc): both weight_unit=fraction + securities ÷100'd (AMZN 0.0555/0.0505/-0.005; AMD 0.0212/0.0175/-0.0037); status PENDING_APPROVAL unchanged. Idempotent+scoped. | CLOSED 20260617T161554Z |

## Log

- 20260617T154845Z OPENED by 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent> with 3 leg(s)
- 20260617T155711Z LEG patch1-producer closed: APPLIED via safe-apply (portfolio-management, saved plan, 1 change repoint-only). EGRESS-VERIFIED: opal-portfolio-excel-
- 20260617T155711Z LEG patch2-excel-gens closed: APPLIED via safe-apply (trade-pipeline, saved plan, 2 changes repoint-only). EGRESS-VERIFIED: trade-workflow-handler Cod
- 20260617T161554Z LEG patch3-remediation closed: remediate --apply on 2 records (AMZN TRADE-20260617-144856-MKYYDP + AMD TRADE-20260602-135824-9CHHWS). LIVE-DDB post-ver
- 20260617T161555Z CLOSED -- all 3 legs proven
