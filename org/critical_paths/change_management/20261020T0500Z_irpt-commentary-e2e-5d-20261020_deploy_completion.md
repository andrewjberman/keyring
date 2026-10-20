# Deploy Completion Record
**Date opened:** 2026-10-20T05:00:45.466104+00:00
**Status:** CLOSED -- RUN PASSED (P1 READY, R2 sections PASS); five synthetic state objects stay (row IRPT_ANLREQ-D2-S223)
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-5D: allow-listed synthetic principal, three-row bytes, no Keep, commentary_requested omitted; PASS is the sections read
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the allow-listed synthetic user and the advisor (A, A2) | mint ok, advisor ok | A mint ok, A2 advisor ok, L login ok at 2026-10-20T05:01:05Z to 05:01:11Z | CLOSED 20261020T050315Z |
| S | verify | upload, ticket and submit (U, T, S) | answers recorded | U ok tries=2 keep=not-needed (NORMALIZED), T ok, S ok REQ-b838e82f3ab11e8923245cde | CLOSED 20261020T050316Z |
| P | verify | poll P1 only | P1 READY or the stop named | P1 READY at 05:01:55Z; P2-P6 NOT-RUN by design (commentary not requested, no unknown row) | CLOSED 20261020T050316Z |
| R | verify | sections read (R2); route read NOT-RUN by design | sections line | R2 sections status=200 n_sections=3 value=1 builder_only_without_value=0 not_in_this_version=0 PASS; R route NOT-RUN by design | CLOSED 20261020T050316Z |
| D | verify | delete only the recorded keys, each read back ABSENT | deleted n of m | deleted 14 of 20 recorded keys ABSENT (19 distinct; five state objects stay, AccessDenied, row filed); first delete 05:02:04Z after last read 05:02:01Z | CLOSED 20261020T050316Z |

## Log

- 20261020T050045Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261020T050315Z LEG A closed: A mint ok, A2 advisor ok, L login ok at 2026-10-20T05:01:05Z to 05:01:11Z
- 20261020T050316Z LEG S closed: U ok tries=2 keep=not-needed (NORMALIZED), T ok, S ok REQ-b838e82f3ab11e8923245cde
- 20261020T050316Z LEG P closed: P1 READY at 05:01:55Z; P2-P6 NOT-RUN by design (commentary not requested, no unknown row)
- 20261020T050316Z LEG R closed: R2 sections status=200 n_sections=3 value=1 builder_only_without_value=0 not_in_this_version=0 PASS; R route NOT-RUN by 
- 20261020T050316Z LEG D closed: deleted 14 of 20 recorded keys ABSENT (19 distinct; five state objects stay, AccessDenied, row filed); first delete 05:0
- 20261020T050316Z CLOSED -- all 5 legs proven
