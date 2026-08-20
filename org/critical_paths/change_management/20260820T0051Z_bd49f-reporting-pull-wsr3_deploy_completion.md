# Deploy Completion Record
**Date opened:** 2026-08-20T00:51:26.357081+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260820T010550Z
**Deploy:** OPAL_TAXSMA_PT2 WS-R3: deploy the producer registry-read (committed-not-deployed ~29d) + the taxsma_registry.py packaging fix
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | WS-R3 source @7d97a8bed2 + files-list fix @4c22b8951a | both on CLOUD, source_dir clean | WS-R3 source @7d97a8bed2 (0.5.0_AE_OpalETL~A 2026-07-21) already on CLOUD; files-list fix @4c22b8951a then corrected to full source_dir parity in the follow-up commit. source_dir clean at build time (commit-before-apply, Rule 2). | CLOSED 20260820T010549Z |
| L2 | activation | artifact opal-assets/opal-assets-bd49f-reporting-pull.zip rebuilt WITH taxsma_registry.py | package member list read from the built zip, 2 members | build-and-upload REFUSED the first attempt -- ADHC_DRIFTD.002 parity: taxsma_newacc/resolver/seed on disk but not in files[]. Contract is SOURCE_DIR PARITY, not import-closure-minimal; corrected to all 5 non-test modules (dry_test.py exempt by the gate's own *_test.py rule). Rebuilt: artifact = 5 members incl. taxsma_registry.py; built lambda_function.py carries taxsma_registry x3 / list_active x1 / WS-R3 x1. | CLOSED 20260820T010549Z |
| L3 | verify | CTO plan-gate GO on the staged plan (declared condition on this artifact, COO cond a) | CTO word citing the plan shape | CTO PLAN-GATE GO 010213Z on the enumerated plan exactly (declared condition 'CTO plan-gate before apply (COO cond a)' in the source-map note -- honoured, not inferred). Presented: plan JSON enumeration (source_code_hash + s3_object_version only; no env/IAM/sizing/schedule) + arms-nothing verified on live primitives with denominators (135 rules / 17 schedules naming it = NONE; get-policy ResourceNotFoundException; 0 event-source-mappings). Riders: expect==plan strictly, L6 verbatim in the close. | CLOSED 20260820T010549Z |
| L4 | verify | targeted safe-apply matches the staged plan exactly | apply counts == plan counts | safe-apply (HALTGT passed): 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' == the gated plan EXACTLY. No deviation, so rider 1 (STOP-not-adapt) was not triggered. | CLOSED 20260820T010550Z |
| L5 | verify | 0-diff on-target re-plan | No changes | 0-diff on-target re-plan: 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260820T010550Z |
| L6 | verify | DEPLOYED BYTES carry WS-R3 AND the taxsma_registry member | package downloaded post-apply: taxsma_registry present as a member AND list_active reachable -- the landmine proven closed on the executing plane, not the built one | ACCEPTANCE, on the EXECUTING plane -- deployed package DOWNLOADED and read post-apply, verbatim: live State=Active CodeSha256=jqtTQyhZn9RMTmdn9RgjYKqOBbOVqhd88iDNHrc2/cg= LastModified=2026-08-20T01:03:35.000+0000. DEPLOYED PACKAGE MEMBERS (denominator 5): lambda_function.py / taxsma_newacc.py / taxsma_registry.py / taxsma_resolver.py / taxsma_seed.py. MARKER COUNTS in the DEPLOYED lambda_function.py: taxsma_registry=3, list_active=1, WS-R3=1 (all were 0 on the pre-apply artifact). taxsma_registry.py IS A MEMBER OF THE DEPLOYED PACKAGE: True. list_active DEFINED in the deployed taxsma_registry.py: True. So the 29-day committed-not-deployed gap is closed on the plane that runs, and the ImportError landmine is closed there too -- not merely at the built artifact. | CLOSED 20260820T010550Z |

## Log

- 20260820T005126Z OPENED by 0.7.0_AE_CloudOps with 6 leg(s)
- 20260820T010549Z LEG L1 closed: WS-R3 source @7d97a8bed2 (0.5.0_AE_OpalETL~A 2026-07-21) already on CLOUD; files-list fix @4c22b8951a then corrected to 
- 20260820T010549Z LEG L2 closed: build-and-upload REFUSED the first attempt -- ADHC_DRIFTD.002 parity: taxsma_newacc/resolver/seed on disk but not in fil
- 20260820T010549Z LEG L3 closed: CTO PLAN-GATE GO 010213Z on the enumerated plan exactly (declared condition 'CTO plan-gate before apply (COO cond a)' in
- 20260820T010550Z LEG L4 closed: safe-apply (HALTGT passed): 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' == the gated plan EXACTLY. No d
- 20260820T010550Z LEG L5 closed: 0-diff on-target re-plan: 'No changes. Your infrastructure matches the configuration.'
- 20260820T010550Z LEG L6 closed: ACCEPTANCE, on the EXECUTING plane -- deployed package DOWNLOADED and read post-apply, verbatim: live State=Active CodeS
- 20260820T010550Z CLOSED -- all 6 legs proven
