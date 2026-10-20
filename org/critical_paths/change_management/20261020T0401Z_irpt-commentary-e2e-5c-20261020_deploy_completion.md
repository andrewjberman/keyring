# Deploy Completion Record
**Date opened:** 2026-10-20T04:01:42.068256+00:00
**Status:** CLOSED -- STOPPED AT P1 (NOT_READY_IN_BUDGET; RecipeRefused); three synthetic state objects stay (rows IRPT_ANLREQ-D2-S221 and S222)
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-5C: three-row bytes, no unknown row, no Keep, commentary_requested omitted; PASS is the sections read
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic user and advisor (A, A2) | mint ok, advisor ok | A mint ok, A2 advisor ok, L login ok at 2026-10-20T04:02:02Z to 04:02:07Z | CLOSED 20261020T043420Z |
| S | verify | upload, ticket and submit (U, T, S) | answers recorded | U ok tries=2 keep=not-needed (NORMALIZED 04:02:22Z), T ok, S ok REQ-948597d16f8e5da8f6d64677 at 04:02:32Z | CLOSED 20261020T043420Z |
| P | verify | poll P1 only | P1 READY or the stop named | STOPPED AT P1: job not READY in the 30 minute budget (ended 04:32:35Z); resident retained_for_retry class=RecipeRefused x3; P2-P6 NOT-RUN by design | CLOSED 20261020T043420Z |
| R | verify | sections read (R2); route read NOT-RUN by design | sections line | NOT-RUN: stopped at P1 (R2 not reached; R NOT-RUN by design) | CLOSED 20261020T043420Z |
| D | verify | delete only the recorded keys, each read back ABSENT | deleted n of m | deleted 12 of 16 recorded keys ABSENT (15 distinct; three state objects stay, AccessDenied, rows S221 and S222); first delete 04:32:39Z at or after last read 04:32:39Z | CLOSED 20261020T043420Z |

## Log

- 20261020T040142Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261020T043420Z LEG A closed: A mint ok, A2 advisor ok, L login ok at 2026-10-20T04:02:02Z to 04:02:07Z
- 20261020T043420Z LEG S closed: U ok tries=2 keep=not-needed (NORMALIZED 04:02:22Z), T ok, S ok REQ-948597d16f8e5da8f6d64677 at 04:02:32Z
- 20261020T043420Z LEG P closed: STOPPED AT P1: job not READY in the 30 minute budget (ended 04:32:35Z); resident retained_for_retry class=RecipeRefused 
- 20261020T043420Z LEG R closed: NOT-RUN: stopped at P1 (R2 not reached; R NOT-RUN by design)
- 20261020T043420Z LEG D closed: deleted 12 of 16 recorded keys ABSENT (15 distinct; three state objects stay, AccessDenied, rows S221 and S222); first d
- 20261020T043420Z CLOSED -- all 5 legs proven
