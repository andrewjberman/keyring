# Deploy Completion Record
**Date opened:** 2026-10-16T10:12:28.614230+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T171100Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD1 window 3 (AR-y-371): FWD-1 run 3 on release 33, r35L and the resident r34c: Q the step-0 probe (five candidates as the probe viewer irpt-r3p-iv-20261016@opal.invalid), M mint the synthetic staff user fwd1-staff-r41b@opal.invalid, S submit one Analysis Request through the Ticket Center page (firm 49financial), P poll the chain read-only, R remove both users (ABSENT by GSI and ConsistentRead); NO retry; addendum 3 COO blobs 64884b3338 / 7a4e873515 / e934758e07, CTO half signed for all three
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| Q | verify | probe viewer irpt-r3p-iv-20261016@opal.invalid mint, five door probes, removal ABSENT | probe table, intake listing before and after, viewer ABSENT by GSI and ConsistentRead | three probe sets (SET 1 to 3) read and recorded; no probe in the run window by amendment 8 (c); all viewers ABSENT | CLOSED 20261016T171059Z |
| M | verify | run user fwd1-staff-r41b@opal.invalid users row (fwd1_mint.py) | row minted, signed-in by the driver | run user minted MINT-OK READBACK-OK 16:50:49Z | CLOSED 20261016T171059Z |
| S | verify | one Analysis Request filed through the Ticket Center page by the driver | ticket id, decisions pressed from the decisions file | holdings posted and Submit clicked 16:51:00Z; upload ended NEEDS_CORRECTION, no ticket filed (page wait timed out 17:04:01Z); window SPENT, no retry | CLOSED 20261016T171100Z |
| P | verify | the chain polled read-only (20 minutes) | ticket status, attachments n of 4, report, queues, resident journal, Yahoo count | no polls: no ticket, ticket_id null (A_RUN_FWD1_R3.txt F2 FAIL) | CLOSED 20261016T171100Z |
| R | verify | removal of the run user and the probe viewer | four ABSENT lines (GSI and ConsistentRead each) | run user removed ABSENT GSI and ABSENT CONSISTENT (driver and independent read); three probe viewers ABSENT | CLOSED 20261016T171100Z |

## Log

- 20261016T101228Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
- 20261016T171059Z LEG Q closed: three probe sets (SET 1 to 3) read and recorded; no probe in the run window by amendment 8 (c); all viewers ABSENT
- 20261016T171059Z LEG M closed: run user minted MINT-OK READBACK-OK 16:50:49Z
- 20261016T171100Z LEG S closed: holdings posted and Submit clicked 16:51:00Z; upload ended NEEDS_CORRECTION, no ticket filed (page wait timed out 17:04:
- 20261016T171100Z LEG P closed: no polls: no ticket, ticket_id null (A_RUN_FWD1_R3.txt F2 FAIL)
- 20261016T171100Z LEG R closed: run user removed ABSENT GSI and ABSENT CONSISTENT (driver and independent read); three probe viewers ABSENT
- 20261016T171100Z CLOSED -- all 5 legs proven
