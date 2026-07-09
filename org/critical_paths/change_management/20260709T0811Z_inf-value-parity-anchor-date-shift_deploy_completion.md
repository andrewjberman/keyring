# Deploy Completion Record
**Date opened:** 2026-07-09T08:11:39.988951+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T081938Z
**Deploy:** inf value-parity anchor-date shift: bundle canonical _orion_vendor_asof + VP_ANCHOR_DATE_SHIFT -- kills the hourly phantom $1.44M false-positive (CTO pre-apply GO 062304Z, DS~A paired)
**Authored by:** 0.8.0_AE_CloudComp
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit + push value_parity_reader.py + inf_value_parity.tf | hash pushed to origin/CLOUD | c9e42d485 pushed to origin/CLOUD (verified via git merge-base --is-ancestor, not the push message) | CLOSED 20260709T081147Z |
| L2 | activation | safe-apply(HALTGT) inf-value-parity: lambda code + VP_ANCHOR_DATE_SHIFT env | apply complete, resources changed as planned | safe-apply(HALTGT) of saved plan .build/inf-vp.tfplan: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' -- aws_lambda_function.inf_value_parity modified (source_code_hash + VP_ANCHOR_DATE_SHIFT env) | CLOSED 20260709T081425Z |
| L3 | verify | 0-diff re-plan on inf-value-parity after apply | terraform plan = No changes | terraform plan -detailed-exitcode after apply = exit 0, 'No changes. Your infrastructure matches the configuration.' | CLOSED 20260709T081442Z |
| L4 | verify | (a) dry-run invoke -> fired=False exit=0 | live invoke payload showing fired=False | LIVE dry-run invoke of deployed opal-inf-value-parity (StatusCode 200, FunctionError none): {"firm":"inf","fired":false,"published":false,"exit_code":0,"disposition":"FRESH"} -- detail: 'served 202246989.07 matches inf current_value.sum[2026-07-08] (served as_of=2026-07-07) 202246989.07 to the cent (diff 0.0000)'. fired=False exit=0 CONFIRMED. | CLOSED 20260709T081700Z |
| L5 | verify | (b) FIRM-SCOPING: cot-value-parity + 49f-value-parity terraform plan = ZERO diff | both plans 'No changes' | FIRM-SCOPING PROVEN, but NOT by the declared 'both plans ZERO diff' criterion -- that criterion is UNACHIEVABLE for two reasons, NEITHER a firm-scoping failure, both surfaced + escalated: (1) cot-value-parity archives the SAME shared source_dir infra/aws/compdiff, so editing the shared value_parity_reader.py NECESSARILY moves cot's source_code_hash -- cot plan = '0 to add, 1 to change, 0 to destroy', the change being source_code_hash ONLY, environment block UNCHANGED; (2) 49f-value-parity is NOT DEPLOYED AT ALL -- plan = '8 to add, 0 to change', and the live primitive  returns ResourceNotFoundException. ACTUAL firm-scoping evidence, live + exercised: (a) VP_ANCHOR_DATE_SHIFT appears ONLY in inf_value_parity.tf (grep across all 3 value_parity .tf); (b) LIVE cot lambda env: VP_ANCHOR_DATE_SHIFT ABSENT (VP_FIRM=cot); (c) cot AND 49f built zips contain ZERO _orion_vendor_asof.py (9 files each vs inf's 10); (d) unit-exercised passthrough: shift unset -> _resolve_anchor_date returns as_of byte-identical. cot/49f behavior is therefore provably unchanged. | CLOSED 20260709T081745Z |
| L6 | verify | (c) IMPORT-WORKS: built inf-value-parity.zip physically CONTAINS _orion_vendor_asof.py | unzip -l listing of the built artifact | unzip -l .build/inf-value-parity.zip lists _orion_vendor_asof.py (6358 bytes, 10 files vs cot/49f 9 files). DEPLOY-SHA PARITY: live CodeSha256 gwq1R5iTBgyyAI602vBBySZLUn4OpFMNz4og7epW13k= == sha256(built zip) exactly, so the DEPLOYED code is that zip. IMPORT proven by EXERCISE, not inspection: the dry-run label reads sum[2026-07-08] (served as_of=2026-07-07), which only renders if _resolve_anchor_date imported the module and inverted the shift -- had it been absent, the guarded shift would have raised RuntimeError. | CLOSED 20260709T081700Z |
| L7 | verify | (d) BEHAVIORAL: next real hourly EventBridge invoke shows fired=False in CloudWatch | CloudWatch log line from a scheduled (non-manual) invoke | BEHAVIORAL, on a REAL SCHEDULED EventBridge invoke (not a manual call). CloudWatch /aws/lambda/opal-inf-value-parity, hourly cadence :16. BEFORE (scheduled 2026-07-09T07:16:36Z): '=== value-parity [PUBLISH] firm=inf fired=True published=True exit=1 ===' + 'served 202246989.07 does NOT match inf current_value.sum[2026-07-07] 203686267.57 (diverges by 1439278.50)'. AFTER (scheduled 2026-07-09T08:16:24Z, [PUBLISH] mode): '=== value-parity [PUBLISH] firm=inf fired=False published=False exit=0 ===' + 'served 202246989.07 matches inf current_value.sum[2026-07-08] (served as_of=2026-07-07) 202246989.07 to the cent (diff 0.0000)'. Provenance: the deployed handler prints [PUBLISH] ONLY when the event lacks dry_run; my sole manual invoke was the [dry-run] at 08:16:10Z, so the 08:16:24Z [PUBLISH] is the EventBridge scheduled fire. Rule opal-inf-value-parity-hourly = rate(1 hour), ENABLED. Hourly false-positive (firing since 2026-07-06T17:16:36Z) is CONFIRMED DEAD; SNS no longer published. | CLOSED 20260709T081937Z |

## Log

- 20260709T081139Z OPENED by 0.8.0_AE_CloudComp with 7 leg(s)
- 20260709T081147Z LEG L1 closed: c9e42d485 pushed to origin/CLOUD (verified via git merge-base --is-ancestor, not the push message)
- 20260709T081425Z LEG L2 closed: safe-apply(HALTGT) of saved plan .build/inf-vp.tfplan: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' -- a
- 20260709T081442Z LEG L3 closed: terraform plan -detailed-exitcode after apply = exit 0, 'No changes. Your infrastructure matches the configuration.'
- 20260709T081700Z LEG L4 closed: LIVE dry-run invoke of deployed opal-inf-value-parity (StatusCode 200, FunctionError none): {"firm":"inf","fired":false,
- 20260709T081700Z LEG L6 closed: unzip -l .build/inf-value-parity.zip lists _orion_vendor_asof.py (6358 bytes, 10 files vs cot/49f 9 files). DEPLOY-SHA P
- 20260709T081745Z LEG L5 closed: FIRM-SCOPING PROVEN, but NOT by the declared 'both plans ZERO diff' criterion -- that criterion is UNACHIEVABLE for two 
- 20260709T081937Z LEG L7 closed: BEHAVIORAL, on a REAL SCHEDULED EventBridge invoke (not a manual call). CloudWatch /aws/lambda/opal-inf-value-parity, ho
- 20260709T081938Z CLOSED -- all 7 legs proven
