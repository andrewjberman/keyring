# Deploy Completion Record
**Date opened:** 2026-09-30T23:52:50.521654+00:00
**Status:** OPEN
**Deploy:** MDPF_TAXSMA TX-i-1: two scoped Tax prelude roles (mdpf-49f-taxsma-role, mdpf-cot-taxsma-role) + mdpf-gold-taxsma-policy on the Gold role; mdpf-pipeline root, 5 creates, nothing else
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | fresh saved plan of infra/aws/terraform/mdpf-pipeline from the shared tree @69521a6c4f | Plan 5/0/0 = exactly the five TX-i-1 resources; the only other line is the pre-existing output drift mdpf_route_bindings_sha256 |  | OPEN |
| D1 | activation | safe-apply of the saved plan | apply complete 5 added; re-plan No changes |  | OPEN |
| V1 | verify | role sessions exercised live | 49f session: own-prefix list OK, cottonwood bucket AccessDenied, served portal-v2 put AccessDenied; cot session mirror; simulation and exercise recorded separately |  | OPEN |

## Log

- 20260930T235250Z OPENED by 4.0.0_SA_CRO with 3 leg(s)
