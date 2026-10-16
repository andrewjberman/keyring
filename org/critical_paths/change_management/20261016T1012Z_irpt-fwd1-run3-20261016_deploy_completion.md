# Deploy Completion Record
**Date opened:** 2026-10-16T10:12:28.614230+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-RUN-FWD1 window 3 (AR-y-371): FWD-1 run 3 on release 33, r35L and the resident r34c: Q the step-0 probe (five candidates as the probe viewer irpt-r3p-iv-20261016@opal.invalid), M mint the synthetic staff user fwd1-staff-r41b@opal.invalid, S submit one Analysis Request through the Ticket Center page (firm 49financial), P poll the chain read-only, R remove both users (ABSENT by GSI and ConsistentRead); NO retry; addendum 3 COO blobs 64884b3338 / 7a4e873515 / e934758e07, CTO half signed for all three
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| Q | verify | probe viewer irpt-r3p-iv-20261016@opal.invalid mint, five door probes, removal ABSENT | probe table, intake listing before and after, viewer ABSENT by GSI and ConsistentRead |  | OPEN |
| M | verify | run user fwd1-staff-r41b@opal.invalid users row (fwd1_mint.py) | row minted, signed-in by the driver |  | OPEN |
| S | verify | one Analysis Request filed through the Ticket Center page by the driver | ticket id, decisions pressed from the decisions file |  | OPEN |
| P | verify | the chain polled read-only (20 minutes) | ticket status, attachments n of 4, report, queues, resident journal, Yahoo count |  | OPEN |
| R | verify | removal of the run user and the probe viewer | four ABSENT lines (GSI and ConsistentRead each) |  | OPEN |

## Log

- 20261016T101228Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 5 leg(s)
