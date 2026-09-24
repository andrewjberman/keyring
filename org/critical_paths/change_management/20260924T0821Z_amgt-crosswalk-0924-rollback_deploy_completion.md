# Deploy Completion Record
**Date opened:** 2026-09-24T08:21:20.106620+00:00
**Status:** OPEN
**Deploy:** AMGT crosswalk/v1/2026-09-24.json RESTORE to the signed bytes after the 08:02:55Z induction fire replaced it (523207 b, sha 9bd953b9, MEASURED 194 -> 231910 b, records 116). Rollback leg of the EXISTING never-widen pair COO 4c7d0b2e7c / CTO 429efcdf30; no new pair. R-37.
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | served object restored | head-object size 523207 AND document-sha256 9bd953b9 |  | OPEN |
| R2 | verify | served identity restored | direct invoke ASML_US_Equity MEASURED/absent/SERVED and AAPL_US_Equity derived 10 SERVED |  | OPEN |
| R3 | verify | untouched control holds | direct invoke CAT_US_Equity MEASURED derived 12 |  | OPEN |

## Log

- 20260924T082120Z OPENED by 1.0.0_SA_CTO~Z with 3 leg(s)
