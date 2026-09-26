# Deploy Completion Record
**Date opened:** 2026-09-25T23:06:15.022309+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T035152Z
**Deploy:** Re-arm the INF one-use on a SINGLE-ACCOUNT client (Andrew-direct 23:0xZ 'go'): plan 01209afb.. replaces the unreachable 0279 plan b0b85aa9 (its Martin entry holds 2 accounts); env-only apply from a clean pre-(B) checkout
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | irpt-performance-adapter environment | IRPT_PERFORMANCE_APPROVED_PLAN sha256 == 01209afb..; IRPT_PERF_VENDOR_EGRESS_AUTHORIZED == that sha; CodeSha256 unchanged (jbojcl..); no other env key moved | env-only apply from a clean detached checkout at 83e8b9577a (no deploy (B) Terraform): 0 added / 1 changed / 0 destroyed; live IRPT_PERFORMANCE_APPROVED_PLAN sha256 01209afbd7.. and IRPT_PERF_VENDOR_EGRESS_AUTHORIZED 01209afbd7..; CodeSha256 jbojclF39H.. unchanged, LastUpdateStatus Successful; the plan's only other difference from b0b85aa9 is the account (a single-account directory entry) and expires_at 2026-09-26T12:00Z | CLOSED 20260925T231230Z |
| N1 | verify | negative arm | no PERFORMANCE_USE row for the new plan before Andrew's run; a request for any other account is refused before a vendor call (the plan gate) | 0 INF PERFORMANCE_* rows before the run (no USE/ACCEPTED for either plan); the 22:23-22:27Z requests on multi-account selections were refused SelectionUnsupported before any vendor call, and the gate refuses any account other than the plan's | CLOSED 20260925T231230Z |
| S1 | verify | Andrew's signed-in run | PERFORMANCE_USE#01209afb.. + PERFORMANCE_ACCEPTED# rows and a retained REPORT# row for the account | OUTCOME FAILED, act terminal: the run was the bounded walk principal by API (CTO 101109), 03:20:31Z. PERFORMANCE_USE#01209afb.. CLAIMED (plan spent; the gate refuses any second use). PERFORMANCE_ACCEPTED# ABSENT and no INF REPORT#: Orion answered HTTP 404 'Object does not exist' (replayed once under CTO 101098 egress, ledger irpt-orion-scope-diagnostic-20260926). Row IRPT_BCKEND-S143 (ARMED, owner P) carries the grammar fix. The env arm is inert and nothing is half-landed. | CLOSED 20260926T035152Z |

## Log

- 20260925T230615Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260925T231230Z LEG A1 closed: env-only apply from a clean detached checkout at 83e8b9577a (no deploy (B) Terraform): 0 added / 1 changed / 0 destroyed
- 20260925T231230Z LEG N1 closed: 0 INF PERFORMANCE_* rows before the run (no USE/ACCEPTED for either plan); the 22:23-22:27Z requests on multi-account se
- 20260926T035152Z LEG S1 closed: OUTCOME FAILED, act terminal: the run was the bounded walk principal by API (CTO 101109), 03:20:31Z. PERFORMANCE_USE#012
- 20260926T035152Z CLOSED -- all 3 legs proven
