# Deploy Completion Record
**Date opened:** 2026-09-11T01:03:19.410256+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T013010Z
**Deploy:** IRPT_BCKEND IB-s-13 -- the shared irpt-common layer: build, upload, publish and attach to irpt-performance-adapter (surprise row IRPT_BCKEND-W4-S3)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-1-4 commit of the layer source, the performance root layers.tf and env pins, and the CI map registrations | commit hash | commits a12b0df4e7 (layer source + roots + CI maps + both ledgers opened), a290b61eed (the build made reproducible: bin/ launchers and their RECORD line dropped) and 8e5d8cadad (the AST closure extended to module-level IMPORTS plus a clean-namespace exec check) on wk-irpt_bckend-1-4 -- LOCAL; a worker never pushes | CLOSED 20260911T012936Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-layers/irpt-common.zip | head-object ContentLength + content-sha256 equal to the built zip | s3://opal-313476888478-lambda-layers/irpt-common.zip -- head-object read back ContentLength=621748 and Metadata content-sha256=JWKuEDIoIPgt1zaYmymEhmHS9HZtG2XCwEc7LXKagf4=, both equal to the built zip (154 members); two consecutive builds of the same inputs are byte-identical, so the digest is re-derivable from the manifest | CLOSED 20260911T012936Z |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/performance (aws_lambda_layer_version.irpt_common + the attach on module.irpt_performance_adapter) | safe-apply output | safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/performance apply, three runs: (1) 'Apply complete! Resources: 1 added, 1 changed, 0 destroyed.' publishing irpt-common:1 and attaching it; (2) '0 added, 1 changed, 0 destroyed' taking the rebuilt adapter zip that resolves the contract from the layer; (3) '1 added, 1 changed, 1 destroyed' publishing irpt-common:2 after the import-closure fix -- the destroyed resource is version 1, created minutes earlier by this same cell and consumed by nothing else. NO existing bucket, table, route, behavior or other Lambda was touched in any of the three. | CLOSED 20260911T013010Z |
| L4 | verify | get-function-configuration irpt-performance-adapter shows a Layers[].Arn containing irpt-common, an invoke returns contract_validated true, and the root re-plans 0-diff | verbatim CLI output | get-function-configuration irpt-performance-adapter: Layers[0].Arn = arn:aws:lambda:us-east-1:313476888478:layer:irpt-common:2, Env carries IRPT_BD_HELPERS_PATH=/opt/python/bd_helpers.py and IRPT_CONTRACTS_DIR=/opt/python/irpt_contracts, State=Active. TWO invokes of the DEPLOYED function over its offline fixtures, one per provider: Orion F-INF and Black Diamond F-49F BOTH return contract_validated=true, and the BD response no longer carries the period_range_labels PARTIAL absence -- the bounded helpers load from the layer. The single-provider invoke that preceded this read GREEN on a layer that was broken for the other provider; both are read now. | CLOSED 20260911T013010Z |

## Log

- 20260911T010319Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
- 20260911T012936Z LEG L1 closed: commits a12b0df4e7 (layer source + roots + CI maps + both ledgers opened), a290b61eed (the build made reproducible: bin/
- 20260911T012936Z LEG L2 closed: s3://opal-313476888478-lambda-layers/irpt-common.zip -- head-object read back ContentLength=621748 and Metadata content-
- 20260911T013010Z LEG L3 closed: safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/performance apply, three runs: (1) 'Apply complete! Resource
- 20260911T013010Z LEG L4 closed: get-function-configuration irpt-performance-adapter: Layers[0].Arn = arn:aws:lambda:us-east-1:313476888478:layer:irpt-co
- 20260911T013010Z CLOSED -- all 4 legs proven
