# Deploy Completion Record
**Date opened:** 2026-10-02T10:47:33.479457+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 62 AMGT-al-1 (URGENT, demo risk, due 12:15Z): raise opal-amgt-scoped-api memory_size 1769 -> 3538 MB in infra/aws/terraform/harvest/scoped-amgt-api.tf, then ONE code-free safe-apply. Escalate to 10240 under THIS SAME entry if AC1 C1 still misses 20 s, and stop at 10240. NO never-widen pair: CTO round-61 addendum ruling 5 @f1d5dac151 classes track A as config only, in its own words 'no served value moves, so no never-widen pair', with rollback the memory back to 1769 -- verified by reading the ruling, not taken from the order. Live base at open: MemorySize 1769, Timeout 29, CodeSha256 E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY= (ak-2's, unmoved)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | the memory_size raise in infra/aws/terraform/harvest/scoped-amgt-api.tf and ONE safe-apply of a saved plan, escalating to 10240 under this same entry if needed | the plan read BEFORE applying shows ONE in-place update of the function with ONLY memory_size changing: any source_code_hash, IAM, route, gateway, alias or destroy change is a STOP; prior and new MemorySize read back from LIVE state, not from the apply rc; the forbidden classes graded at the resource-block grain with a positive control |  | OPEN |
| L2 | verify | AC1 round62/checks/timeline_day.py --what post --target-ms 20000 at the TO's literal invocation | C0 PASS MemorySize moved off 1769; C1 PASS 3 of 3 concurrent BA_US_Equity /timeline/day/2026-09-08 invokes each COLD (REPORT carries Init Duration) and each status 200 with Duration under 20,000 ms; C2 PASS the AMD timeline control's body sha256 equals its pre value, which is what shows a memory change moved no served output; THE BA DAY ROUTE ANSWERS COLD UNDER TARGET: YES and exit=0. A failing C2 is the ROLLBACK trigger: memory_size back to 1769 through one safe-apply |  | OPEN |

## Log

- 20261002T104733Z OPENED by 0.7.0_AE_CloudOps~A with 2 leg(s)
