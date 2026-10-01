# Deploy Completion Record
**Date opened:** 2026-10-01T01:51:39.074157+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T015711Z
**Deploy:** MDPF_TAXSMA TX-i-3 as built: the capability bearer secret gateway/global/taxsma-workbook-token (no value) + gateway-taxsma-workbook-bearer-read-policy on opal-gateway-role; mdpf-pipeline root, 2 creates, nothing else
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | fresh saved plan of infra/aws/terraform/mdpf-pipeline from the shared tree @9db0981bd6 | Plan 2/0/0 = the secret and the one inline policy | Saved plan 01:5xZ from the shared tree @9db0981bd6 (vendored terraform 1.9.8, shared tree = origin/CLOUD 68e15a70df plus this seat's commits): Plan 2 to add, 0 to change, 0 to destroy = aws_secretsmanager_secret.taxsma_workbook_bearer + aws_iam_role_policy.gateway_taxsma_workbook_bearer_read (role opal-gateway-role). | CLOSED 20261001T015255Z |
| D1 | activation | safe-apply of the saved plan | apply complete 2 added; re-plan No changes | safe-apply 01:52:55Z of the saved plan (vendored terraform 1.9.8; naming plan limb WARN 51 graded, 0 REFUSE; comp-tagauthz PASSED): Apply complete, 2 added 0 changed 0 destroyed -- secret arn ...:secret:gateway/global/taxsma-workbook-token-nPDnbk and opal-gateway-role:gateway-taxsma-workbook-bearer-read-policy. Re-plan 01:5xZ: No changes. | CLOSED 20261001T015711Z |
| V1 | verify | secret has no value; the Gateway role reads exactly it | describe-secret shows no version; from the Gateway host GetSecretValue on the new secret is admitted (no value yet) while a secret the role does not hold is AccessDenied | describe-secret 01:5xZ: 0 versions (no value). EXERCISED from the Gateway host, SSM command f7021757-2156-4989-a468-5aa8e0a592bb, host clock 01:56:15Z, caller arn:aws:sts::313476888478:assumed-role/opal-gateway-role/i-07dccb1615503ac99, output limited to names and error classes: GetSecretValue on gateway/global/taxsma-workbook-token -> ResourceNotFoundException (IAM admitted, no value exists); negative control orion/credentials (not held) -> AccessDeniedException; positive control opal/mcp/ms-ingest-token (held) -> the secret name. The 49financial Tax role's read (ARN pattern, real suffix -nPDnbk matches ??????) is unexercised until TX-r-3. | CLOSED 20261001T015711Z |

## Log

- 20261001T015139Z OPENED by 4.0.0_SA_CRO with 3 leg(s)
- 20261001T015255Z LEG P1 closed: Saved plan 01:5xZ from the shared tree @9db0981bd6 (vendored terraform 1.9.8, shared tree = origin/CLOUD 68e15a70df plus
- 20261001T015711Z LEG D1 closed: safe-apply 01:52:55Z of the saved plan (vendored terraform 1.9.8; naming plan limb WARN 51 graded, 0 REFUSE; comp-tagaut
- 20261001T015711Z LEG V1 closed: describe-secret 01:5xZ: 0 versions (no value). EXERCISED from the Gateway host, SSM command f7021757-2156-4989-a468-5aa8
- 20261001T015711Z CLOSED -- all 3 legs proven
