# Deploy Completion Record
**Date opened:** 2026-09-29T09:04:02.691205+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T110402Z
**Deploy:** TO-IB-er-401: PRD v0.21 ruling 18 in the producer, 49F + Inflection re-emitted, and the Cottonwood slice
**Authored by:** 0.4.0_DS_ClientPlatform~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | producer + tests on branch ds-e-irpt-r4-cot | commit hash | bf1683f172 (ruling 18) + e79dd684bf (the Cottonwood rules) on ds-e-irpt-r4-cot, LOCAL; 45 tests pass, commit-gate clean, naming-gate PASS | CLOSED 20260929T101233Z |
| L2 | s3-prefix | opal-data-49financial irpt/49financial/gold/holdings_performance_{daily,manifest} 557 days re-emitted under ruling 18 | E4-AC3 PASS line | 557 of 557 49F daily partitions + manifests re-emitted under ruling 18, 3188339 rows, 0 not computed; exactly 2 rows flipped to FOLLOWS-DISCONTINUITY (2025-12-15, 2025-12-18); E4-AC3 PASS: 49financial IMPLAUSIBLE-RETURN rows 2, follow-day OK violations 0 | CLOSED 20260929T101233Z |
| L3 | s3-prefix | opal-data-inflection irpt/inflection/gold/holdings_performance_{daily,manifest} 1609 days re-emitted under ruling 18 | E4-AC3 PASS line | 1609 of 1609 computable INF daily partitions + manifests re-emitted, 1420782 rows, 4 ABSENT days named; E4-AC3 PASS: inflection IMPLAUSIBLE-RETURN rows 0, follow-day OK violations 0 | CLOSED 20260929T101234Z |
| L4 | s3-prefix | opal-data-cottonwood irpt/cottonwood/gold/holdings_performance_{daily,manifest} every computable trading day | E4-AC1 + E4-AC2 PASS lines | 75 of 75 Cottonwood daily partitions + 75 manifests, 2026-06-10..2026-09-25, missing 0, empty 0, 66587 footer rows == producer tally; value decomposition reconciles to the cent against the silver (562744973.40 + 43493.21 - 7607341.30 = 555181125.32); E4-AC1 PASS and E4-AC2 PASS | CLOSED 20260929T110402Z |
| L5 | verify | all three acceptance checks re-run by the issuer from the workspace root | check output | E4-AC1 PASS, E4-AC2 PASS, E4-AC3 PASS, each run unpiped from the workspace root, exit 0; two planted mutants (a dropped account; a deleted mid-history partition) FIRED-AS-EXPECTED and both restored through the producer | CLOSED 20260929T110402Z |

## Log

- 20260929T090402Z OPENED by 0.4.0_DS_ClientPlatform~E with 5 leg(s)
- 20260929T101233Z LEG L1 closed: bf1683f172 (ruling 18) + e79dd684bf (the Cottonwood rules) on ds-e-irpt-r4-cot, LOCAL; 45 tests pass, commit-gate clean,
- 20260929T101233Z LEG L2 closed: 557 of 557 49F daily partitions + manifests re-emitted under ruling 18, 3188339 rows, 0 not computed; exactly 2 rows fli
- 20260929T101234Z LEG L3 closed: 1609 of 1609 computable INF daily partitions + manifests re-emitted, 1420782 rows, 4 ABSENT days named; E4-AC3 PASS: inf
- 20260929T110402Z LEG L4 closed: 75 of 75 Cottonwood daily partitions + 75 manifests, 2026-06-10..2026-09-25, missing 0, empty 0, 66587 footer rows == pr
- 20260929T110402Z LEG L5 closed: E4-AC1 PASS, E4-AC2 PASS, E4-AC3 PASS, each run unpiped from the workspace root, exit 0; two planted mutants (a dropped 
- 20260929T110402Z CLOSED -- all 5 legs proven
