# Deploy Completion Record
**Date opened:** 2026-10-16T16:27:01.161210+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T163334Z
**Deploy:** IRPT_ANLREQ TO-RUN-AR-v32 attempt 2 (AMENDMENT 3+5): mint one staff-only synthetic user, read the Ticket Center page for t55's hop failure on dev server 5174, remove the user
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M | activation | opal-users-v2 USER#fwd1-staff-r41b@opal.invalid PROFILE | MINT-OK READBACK-OK and U1 line | MINT-OK READBACK-OK; U1 line staff-only, entitlement_rows=0 | CLOSED 20261016T163333Z |
| P | verify | localhost:5174 Ticket Center TCK-20261015-944c84f8 | D1-D6 lines, screenshots, P1 P2 P3 | page read: ticket listed on In Progress, words_shown=NO; screenshots taken; P1/S1 FAIL recorded | CLOSED 20261016T163333Z |
| R | activation | same users row removed | ABSENT by GSI and ConsistentRead | removed, ABSENT GSI and ABSENT CONSISTENT, independent read ABSENT | CLOSED 20261016T163334Z |

## Log

- 20261016T162701Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
- 20261016T163333Z LEG M closed: MINT-OK READBACK-OK; U1 line staff-only, entitlement_rows=0
- 20261016T163333Z LEG P closed: page read: ticket listed on In Progress, words_shown=NO; screenshots taken; P1/S1 FAIL recorded
- 20261016T163334Z LEG R closed: removed, ABSENT GSI and ABSENT CONSISTENT, independent read ABSENT
- 20261016T163334Z CLOSED -- all 3 legs proven
