# Deploy Completion Record
**Date opened:** 2026-10-01T18:52:27.861057+00:00
**Status:** OPEN
**Deploy:** MDPF_TAXSMA TX-r-3 activation: mdpf-gold-lambda gains its four Tax settings (Tax ENABLED from its next run); code unchanged at pin 335430e793; never-widen halves CTO @1b43d6f201 (+addendum @5f39857797), COO @07d269eb28; Gateway route live (site Z release 3a7d6a7dc8), controlled read 18:51Z HTTP 200 complete
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | the controlled read through GET /ms/taxsma-workbook (TX-r-3 AC6) | HTTP 200, complete true, 16 account slots; a call with no bearer refused UNAUTHORIZED_CAPABILITY; no row printed | 18:51:01Z, probe org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/probes/tx_r_3_controlled_read.py: NEGATIVE (no bearer) HTTP 401 UNAUTHORIZED_CAPABILITY; CONTROLLED READ HTTP 200, schema_version 0.6.0, sheet Sheet1, used_rows 22, account_slot_count 16, complete true, observed_at 2026-10-01T18:51:02Z, source_modified_at 2026-09-30T18:44:16Z, 21 rows returned (none printed). The identity binding was confirmed by site Z from the host broker record (relay 103944). | CLOSED 20261001T185311Z |
| P1 | verify | a fresh saved plan of mdpf-pipeline | 0/1/0: the function's environment gains the four TAXSMA_ keys; code unchanged | Saved plan 18:54Z: 0 to add, 1 to change, 0 to destroy = aws_lambda_function.mdpf_gold, environment + TAXSMA_CAPABILITY_SECRET_ID (the secret's ARN), TAXSMA_GATEWAY_BASE_URL https://mcp.opalinvest.dev, TAXSMA_PRELUDE_ROLE_ARN_49FINANCIAL (mdpf-49f-taxsma-role), TAXSMA_PRELUDE_ROLE_ARN_COTTONWOOD (mdpf-cot-taxsma-role); code unchanged. | CLOSED 20261001T190406Z |
| D1 | activation | safe-apply mdpf-pipeline (mdpf-gold-lambda) | environment carries MDPF_GOLD_COMMIT and the four TAXSMA_ keys; CodeSha256 unchanged 9YL45zw0..; re-plan No changes | safe-apply 18:55:18Z: 0 added, 1 changed, 0 destroyed. get-function-configuration: CodeSha256 9YL45zw0.. unchanged; environment MDPF_GOLD_COMMIT 335430e793 + the four TAXSMA_ keys; re-plan No changes. | CLOSED 20261001T190406Z |
| V1 | verify | the deployed qa_local dry run after the apply (zero writes) | status green 16 of 16; the Tax prelude runs (not DISABLED) and its result is read: run_result, valuation date, per-firm coverage |  | OPEN |

## Log

- 20261001T185227Z OPENED by 4.0.0_SA_CRO with 4 leg(s)
- 20261001T185311Z LEG R1 closed: 18:51:01Z, probe org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/probes/tx_r_3_controlled_read.py: NEGATIVE (
- 20261001T190406Z LEG P1 closed: Saved plan 18:54Z: 0 to add, 1 to change, 0 to destroy = aws_lambda_function.mdpf_gold, environment + TAXSMA_CAPABILITY_
- 20261001T190406Z LEG D1 closed: safe-apply 18:55:18Z: 0 added, 1 changed, 0 destroyed. get-function-configuration: CodeSha256 9YL45zw0.. unchanged; envi
