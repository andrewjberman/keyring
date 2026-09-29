# Deploy Completion Record
**Date opened:** 2026-09-29T07:35:33.862065+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T081615Z
**Deploy:** TO-IB-er-302: FWD-13 comparison points for 49F -- one row per landed Black Diamond reporting_performance file, both bases stated
**Authored by:** 0.4.0_DS_ClientPlatform~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | holdings_comparison.py + its tests + the sources.json comparison block | commit hash | 6851215833 on ds-e-irpt-r3-holdings (local); 39 tests pass, commit-gate clean, naming-gate PASS 0 graded on the new file | CLOSED 20260929T081614Z |
| L2 | s3-prefix | opal-data-49financial irpt/49financial/gold/holdings_performance_comparison one partition per as-of date | E3-AC3 PASS line | 2 partitions landed: date=2026-06-30 footer 1 row, date=2026-08-28 footer 5317 rows; 5318 rows against 5318 bronze files, 5318 distinct source_key, 0 duplicated, 0 rows carrying neither figures nor a reason | CLOSED 20260929T081614Z |
| L3 | verify | E3-AC3 re-run by the issuer from the workspace root | check output | E3-AC3 PASS, run unpiped from the workspace root, exit 0; two planted mutants (duplicate row; figure dropped with no reason) FIRED-AS-EXPECTED and both restored through the producer | CLOSED 20260929T081615Z |

## Log

- 20260929T073533Z OPENED by 0.4.0_DS_ClientPlatform~E with 3 leg(s)
- 20260929T081614Z LEG L1 closed: 6851215833 on ds-e-irpt-r3-holdings (local); 39 tests pass, commit-gate clean, naming-gate PASS 0 graded on the new file
- 20260929T081614Z LEG L2 closed: 2 partitions landed: date=2026-06-30 footer 1 row, date=2026-08-28 footer 5317 rows; 5318 rows against 5318 bronze files
- 20260929T081615Z LEG L3 closed: E3-AC3 PASS, run unpiped from the workspace root, exit 0; two planted mutants (duplicate row; figure dropped with no rea
- 20260929T081615Z CLOSED -- all 3 legs proven
