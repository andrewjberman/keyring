# All 14 READY-served requests read READY in irpt-jobs; 45 of 51 accepted requests store no ticket_id -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-11
**Task Order:** IRPT_ANLREQ.TO-READS-Y6.job-rows-and-ticket-id-count-laptop
**Status:** COMPLETE

---

## Objective

Read the job row state of the 14 requests the Y5 snapshot served as READY, so the dell2 applier of release 6 can pick one, and count how many accepted requests store no `ticket_id` (CTO msg 4955). Read-only; nothing written to AWS.

## What was done

- Acked crossbox XB-20261011T160627Z-53a9 on the laptop; sent the ack line and the step-1 report to dell2 over agentbus (MessageId d1456b6e-75be-4fff-be46-bd6f43800598, not yet acked by dell2).
- Step 1: `y6_scripts/reads6.py jobs`, 14 `get_item` reads on `irpt-jobs` (ConsistentRead, state only), tenant cottonwood: 14 of 14 read, 14 READY, 0 NO_ROW, 0 denied. First READY id `REQ-01c903660d7ab222cd08b2ff`.
- Step 3: `reads6.py count`, one consistent scan of `irpt-requests`: 1904 items, 51 accepted, 0 unreadable. With ticket_id 6 (49financial), without 45 (49financial 5, cottonwood 39, inflection 1).
- The scan holds one more accepted request than the Y5 snapshot (51 against 50; 1904 items against 1894); it is in the count and not in the 14.
- Result: `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y6_job_rows_and_ticket_id_count.json`; checker prints `READS6-OK`.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| reads6_check | python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r9/reads6_check.py | PASS | READS6-OK |
| comp-iam | none | SKIPPED | read-only order; the laptop identity read both tables without a denial |

**What worked:** the Y5 snapshot held the id and tenant for each READY request, so no id was retyped.
**What failed:** nothing.
**Gap found:** none.
