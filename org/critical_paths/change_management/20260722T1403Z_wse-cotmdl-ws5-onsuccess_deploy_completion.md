# Deploy Completion Record
**Date opened:** 2026-07-22T14:03:40.144490+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260722T143146Z
**Deploy:** WSE_COTMDL WS-5: on_success destination + InvokeFunction grant (bronze->silver automation, CTO GO 140211Z, -target scoped)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | targeted plan PURE ADD | 2 to add 0 to change 0 to destroy | terraform plan -target x2: Plan: 2 to add, 0 to change, 0 to destroy (pure-add, new-territory rule satisfied; the 1-to-change bd49f_reporting_io TAXSMA drift EXCLUDED by targeting, routed to CTO/COO) | CLOSED 20260722T140424Z |
| L2 | activation | safe-apply -target both resources ONE apply | apply rc=0 | safe-apply -chdir=opal-assets -target x2: both resources created. Re-invocation returned 'Apply complete! Resources: 0 added, 0 changed, 0 destroyed' (idempotent). | CLOSED 20260722T141611Z |
| L3 | verify | 0-diff on targeted re-plan, live primitive | No changes + get-role-policy/get-function-event-invoke-config | LIVE PRIMITIVE, not the apply output (CTO cond 4): get-function-event-invoke-config cot-rebalancer-runner -> retry=2 age=21600 OnSuccess.Destination=arn:...:function:opal-assets-silver-blackdiamond. get-role-policy cot-rebalancer-runner-role/cot-rebalancer-runner-invoke-silver-blackdiamond -> Sid InvokeBlackdiamondSilverConverterOnSuccess Allow on that exact ARN. Terraform 0-diff corroborates but is NOT the evidence. | CLOSED 20260722T141612Z |
| L4 | verify | simulate-principal-policy target=allowed, positive control SEPARATE invocation | EvalDecision allowed + control allowed | simulate-principal-policy, ONE --resource-arns per call, controls as SEPARATE invocations (Rule 22a). TARGET lambda:InvokeFunction -> opal-assets-silver-blackdiamond = allowed (was implicitDeny pre-apply). NEGATIVE CONTROL (separate) -> opal-assets-silver-orion = implicitDeny, proving the grant is ARN-scoped least-privilege and NOT a blanket lambda:InvokeFunction, and that the simulator discriminates. | CLOSED 20260722T141612Z |
| L5 | git | commit + tag pushed --follow-tags | hash + tag name | tag opal-assets-v0.31.0 pushed --follow-tags, verified on origin via git ls-remote --tags (ddadf1ab3e86...). TF commit df3197883 on origin/CLOUD. NOTE: I first attempted v0.28.0 by assumption; the tag command rejected it as existing and I then ran the Rule-6 pre-flight (git tag -l \| sort -V) which showed v0.28/0.29/0.30 all taken. | CLOSED 20260722T141739Z |
| L6 | verify | EXERCISE end-to-end: mode==event manifest after invoke, before 05:00Z (parquet-landed is NECESSARY AND NOT SUFFICIENT) | meta/conversions/{run_id}.json mode=event + fact_model_* partition | EXERCISED end-to-end. Invoked opal-assets-silver-blackdiamond with a REAL on_success envelope (condition=Success, responsePayload.as_of=2026-07-22). Manifest blackdiamond/cottonwood/meta/conversions/20260722T143053Z-81076020.json carries mode=='event' -- ASSERTED, not eyeballed. Written 14:30:53Z; prior newest manifest was 05:00:11Z, so the 05:00Z sweep did NOT produce this evidence. All 4 rebalancer tables returned skipped-idempotent (correct: DE hand-ran them). PARQUET-LANDED IS NECESSARY AND NOT SUFFICIENT -- the sweep self-heals a broken destination, so only mode=='event' discriminates. ALSO: import-health probe with a discriminating payload returned ValueError 'destination envelope carries condition=RetriesExhausted -- this branch is for on_success only', an error string that exists ONLY in the new code, proving both that the module imports AND that the new dispatcher is live. | CLOSED 20260722T143145Z |

## Log

- 20260722T140340Z OPENED by 0.7.0_AE_CloudOps with 6 leg(s)
- 20260722T140424Z LEG L1 closed: terraform plan -target x2: Plan: 2 to add, 0 to change, 0 to destroy (pure-add, new-territory rule satisfied; the 1-to-c
- 20260722T141611Z LEG L2 closed: safe-apply -chdir=opal-assets -target x2: both resources created. Re-invocation returned 'Apply complete! Resources: 0 a
- 20260722T141612Z LEG L3 closed: LIVE PRIMITIVE, not the apply output (CTO cond 4): get-function-event-invoke-config cot-rebalancer-runner -> retry=2 age
- 20260722T141612Z LEG L4 closed: simulate-principal-policy, ONE --resource-arns per call, controls as SEPARATE invocations (Rule 22a). TARGET lambda:Invo
- 20260722T141739Z LEG L5 closed: tag opal-assets-v0.31.0 pushed --follow-tags, verified on origin via git ls-remote --tags (ddadf1ab3e86...). TF commit d
- 20260722T143145Z LEG L6 closed: EXERCISED end-to-end. Invoked opal-assets-silver-blackdiamond with a REAL on_success envelope (condition=Success, respon
- 20260722T143146Z CLOSED -- all 6 legs proven
