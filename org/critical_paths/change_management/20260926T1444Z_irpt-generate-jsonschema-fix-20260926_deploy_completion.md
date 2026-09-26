# Deploy Completion Record
**Date opened:** 2026-09-26T14:44:01.549770+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T145409Z
**Deploy:** irpt-ycharts-generate: irpt-common layer (jsonschema/referencing/rpds) + whole-row re-pin at 19d8f3038c incl. the IAM-only import census (CTO 101229; K5 ModuleNotFoundError jsonschema)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | checker + served function | (1) package_import_check FAILS on IJD6bd1I naming jsonschema; (2) passes on the new zip + irpt-common; (3) import census on the deployed function: 0 failed modules; CodeSha256 == artifact; invoke {} CONTRACT_VERSION before and after; replan No changes | (1) NEGATIVE CONTROL: package_import_check.py on IJD6bd1I without a layer -> rc 1, UNRESOLVED jsonschema <- composition_admission.py [module level], parse.py and referencing <- composition_admission.py [module level] (Y's generate_package_closure --layer measured the same: exit 1 without, 0 with layer 5). (2) new zip 85TXFzzv.. + irpt-common:5: package_import_check rc 0 (60 .py, 4 named nested allowances: controller/operation_lease resident-host-only, pdfminer/pdfplumber guarded by backend_state); generate_package_closure --layer rc 0 (closure 40, 0 third-party absent). grant.py staged after both checks named it (served.render_ports_from_env). (3) DEPLOYED import census {irpt_import_census:true} -> {modules: 59, failed: {}}. CodeSha256 85TXFzzv.. == artifact, layers [irpt-common:5], Active/Successful; invoke {} CONTRACT_VERSION before and after; replan detailed-exitcode 0. | CLOSED 20260926T145408Z |
| irpt-ycharts-generate | tf-lambda | module.irpt_ycharts_generate.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | plan 0/1/0: layers [] -> [irpt-common:5] (data source by name resolved v5), source_code_hash IJD6bd1I -> 85TXFzzv, s3_object_version only; safe-apply 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.'; backend TF 08d9f2f0b1; publish map 0af4314fe7 + grant row + artifact record | CLOSED 20260926T145408Z |

## Log

- 20260926T144401Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260926T145408Z LEG V1 closed: (1) NEGATIVE CONTROL: package_import_check.py on IJD6bd1I without a layer -> rc 1, UNRESOLVED jsonschema <- composition_
- 20260926T145408Z LEG irpt-ycharts-generate closed: plan 0/1/0: layers [] -> [irpt-common:5] (data source by name resolved v5), source_code_hash IJD6bd1I -> 85TXFzzv, s3_ob
- 20260926T145409Z CLOSED -- all 2 legs proven
