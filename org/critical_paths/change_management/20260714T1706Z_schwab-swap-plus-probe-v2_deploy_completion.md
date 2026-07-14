# Deploy Completion Record
**Date opened:** 2026-07-14T17:06:16.301736+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260714T171239Z
**Deploy:** Schwab V2-8 swap + bd49f probe-v2 (CTO GO 165829Z; saved plan 0/2/0)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply schwab-swap-plus-probe-v2.tfplan (HALTGT) | apply rc=0, 2 changed | safe-apply schwab-swap-plus-probe-v2.tfplan rc=0: 0 added / 2 changed / 0 destroyed (module.silver_converter[schwab] + module.bd49f_pull lambdas); outputs rendered clean | CLOSED 20260714T171238Z |
| L2 | verify | 0-diff replan + live CodeSha256 x2 == artifact shas + sizing live + import smoke | replan No changes + get-function-configuration x2 + designed loud-refusal | 0-diff replan 'no differences'; live x2 MATCH TF source_code_hash byte-identical (schwab p+a2DLtF... py3.11/3008/600 pandas-pyarrow-layer:1; bd49f 9huT1p5O... py3.12/512/300); schwab import smoke = designed ValueError loud-refusal from schwab_runtime.py:227 (real runtime, imports resolve); probe-v2 invoke rc=200 no FunctionError, verdict ROSTER-LANDED+2-BODIES, ListObjectsV2 3 keys: roster 13924B + template_390224 37055B + template_435407 12223B | CLOSED 20260714T171239Z |
| L3 | git | tag opal-assets-v0.9.0 + push --follow-tags | tag on origin | tag opal-assets-v0.9.0 pushed --follow-tags (CLOUD 635ff2f21..e8de422f6) | CLOSED 20260714T171239Z |

## Log

- 20260714T170616Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260714T171238Z LEG L1 closed: safe-apply schwab-swap-plus-probe-v2.tfplan rc=0: 0 added / 2 changed / 0 destroyed (module.silver_converter[schwab] + m
- 20260714T171239Z LEG L2 closed: 0-diff replan 'no differences'; live x2 MATCH TF source_code_hash byte-identical (schwab p+a2DLtF... py3.11/3008/600 pan
- 20260714T171239Z LEG L3 closed: tag opal-assets-v0.9.0 pushed --follow-tags (CLOUD 635ff2f21..e8de422f6)
- 20260714T171239Z CLOSED -- all 3 legs proven
