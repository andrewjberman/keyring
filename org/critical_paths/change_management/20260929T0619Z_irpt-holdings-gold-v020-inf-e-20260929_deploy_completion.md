# Deploy Completion Record
**Date opened:** 2026-09-29T06:19:10.931045+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T071955Z
**Deploy:** TO-IB-er-301: producer to PRD v0.20 (rulings 13-17), re-emit all 557 49F holdings-gold days, mint the Inflection slice 2020-04-27..2026-09-25
**Authored by:** 0.4.0_DS_ClientPlatform~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | producer + sources.json + tests on branch ds-e-irpt-r3-holdings | commit hash | f302ab14cd on ds-e-irpt-r3-holdings (local; branch not pushed -- CLOUD is pushed by 0.0.0_AB_MSTR only); 24 tests pass, commit-gate clean, naming-gate PASS 1 graded 0 REFUSE | CLOSED 20260929T071927Z |
| L2 | s3-prefix | opal-data-49financial irpt/49financial/gold/holdings_performance_{daily,manifest} 557 days re-emitted under v0.20 | E3-AC4 PASS line | 557 of 557 49F daily partitions + 557 manifests re-emitted, 2024-07-09..2026-09-25, missing 0, empty 0, 3188339 footer rows == producer tally; E3-AC4 PASS: OK rows \|r\|>=1 0 (base 2846), \|r\|>0.5 4 (base 4061), days without leveraged 0, manifests complete 557/557 | CLOSED 20260929T071927Z |
| L3 | s3-prefix | opal-data-inflection irpt/inflection/gold/holdings_performance_{daily,manifest} every computable trading day | E3-AC1 + E3-AC2 PASS lines | 1609 of 1609 computable INF daily partitions + 1609 manifests, 2020-04-27..2026-09-25, missing 0, empty 0, 1420782 footer rows == producer tally; 4 non-computable days all ABSENT and named; E3-AC1 PASS (960/960, missing 0, dup 0, complete true) and E3-AC2 PASS (missing gold 0) | CLOSED 20260929T071928Z |
| L4 | verify | all three acceptance checks re-run by the issuer from the workspace root | check output | E3-AC4 PASS, E3-AC1 PASS, E3-AC2 PASS, each run unpiped from the workspace root, exit 0; two planted mutants FIRED-AS-EXPECTED and both restored through the producer | CLOSED 20260929T071928Z |

## Log

- 20260929T061910Z OPENED by 0.4.0_DS_ClientPlatform~E with 4 leg(s)
- 20260929T071927Z LEG L1 closed: f302ab14cd on ds-e-irpt-r3-holdings (local; branch not pushed -- CLOUD is pushed by 0.0.0_AB_MSTR only); 24 tests pass, 
- 20260929T071927Z LEG L2 closed: 557 of 557 49F daily partitions + 557 manifests re-emitted, 2024-07-09..2026-09-25, missing 0, empty 0, 3188339 footer r
- 20260929T071928Z LEG L3 closed: 1609 of 1609 computable INF daily partitions + 1609 manifests, 2020-04-27..2026-09-25, missing 0, empty 0, 1420782 foote
- 20260929T071928Z LEG L4 closed: E3-AC4 PASS, E3-AC1 PASS, E3-AC2 PASS, each run unpiped from the workspace root, exit 0; two planted mutants FIRED-AS-EX
- 20260929T071955Z CLOSED -- all 4 legs proven
