# Deploy Completion Record
**Date opened:** 2026-09-22T10:01:27.022030+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260922T101314Z
**Deploy:** AMGT-rk-97: opal-amgt-scoped-api memory 512 -> 1769 (print render CPU)
**Authored by:** 0.9.0_WK_AMGT_RESAPP~97
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | AC6: text_identical 5 of 5 differ []; other_route_equal 5 of 5 regressed []; medians_not_lower []; post cfg MemorySize 1769 CodeSha256 r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w= (equal to pre-act) State Active LastUpdateStatus Successful | CLOSED 20260922T101314Z |

## Log

- 20260922T100127Z OPENED by 0.9.0_WK_AMGT_RESAPP~97 with 1 leg(s)
- 20260922T101314Z LEG opal-amgt-scoped-api closed: AC6: text_identical 5 of 5 differ []; other_route_equal 5 of 5 regressed []; medians_not_lower []; post cfg MemorySize 1
- 20260922T101314Z CLOSED -- all 1 legs proven
