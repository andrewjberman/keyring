# Deploy Completion Record
**Date opened:** 2026-08-20T00:51:26.357081+00:00
**Status:** OPEN
**Deploy:** OPAL_TAXSMA_PT2 WS-R3: deploy the producer registry-read (committed-not-deployed ~29d) + the taxsma_registry.py packaging fix
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | WS-R3 source @7d97a8bed2 + files-list fix @4c22b8951a | both on CLOUD, source_dir clean |  | OPEN |
| L2 | activation | artifact opal-assets/opal-assets-bd49f-reporting-pull.zip rebuilt WITH taxsma_registry.py | package member list read from the built zip, 2 members |  | OPEN |
| L3 | verify | CTO plan-gate GO on the staged plan (declared condition on this artifact, COO cond a) | CTO word citing the plan shape |  | OPEN |
| L4 | verify | targeted safe-apply matches the staged plan exactly | apply counts == plan counts |  | OPEN |
| L5 | verify | 0-diff on-target re-plan | No changes |  | OPEN |
| L6 | verify | DEPLOYED BYTES carry WS-R3 AND the taxsma_registry member | package downloaded post-apply: taxsma_registry present as a member AND list_active reachable -- the landmine proven closed on the executing plane, not the built one |  | OPEN |

## Log

- 20260820T005126Z OPENED by 0.7.0_AE_CloudOps with 6 leg(s)
