# TCKT_VNEXT round 1 -- the FWD-1 seat-arm run (SA-r-1, SA-r-1b) -- L8 PACKET

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-09 ~17:5xZ. **For** `3.0.0_SA_CVO` at L9, as a FILE. This is not the L10 slug.

**Authority:**
- pair v2.2: COO half `deliverables/2.0.0_SA_COO~V2/R1_RUN/TV_R1_SEAT_ARM_PLAN_AND_PAIR.md` @d9399fa002;
- CTO half @022ee70258, with AMENDMENT 1 @133952758b (no data-refresh probe) and AMENDMENT 2 (msg 3747, the watchlist code read);
- CTO msg 3751: run 3 and later need an explicit GO, with the ledger opened first.

**Client data:** this packet and the trace carry statuses, artifact ids, lengths and sha256 prefixes only. I re-scanned the trace at 17:5xZ:
- 0 money-like strings;
- 0 `account_number`/`account_id` values.

## 1. Terminal orders

| order | executor | status | record |
|---|---|---|---|
| TO-RUN-SA-r-1 (pair v2.1) | `0.7.0_AE_CloudOps~TV2` | complete @0261ada6c4 | `R1_RUN/sa_r1_trace.json`: 22/22 cottonwood refused; no hop (the v2.1 token/row were disjoint, row D2-S15) |
| TO-RUN-SA-r-1b (pair v2.2), runs 1-4 | `0.7.0_AE_CloudOps~TV2` | complete | `R1_RUN/sa_r1b_trace.json`, sha256 `0532f0aa...0c16`, byte-identical to `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/sa_r1/sa_r1b_trace.json` @66bfdf5c2e |

**Run 3/4 ledger:** `org/critical_paths/change_management/20261009T1707Z_tckt-vnext-sa-r1b-run3-20261009_deploy_completion.md`.
- Opened before the act (17:07Z) and CLOSED 17:44:38Z, with all 6 legs proven.
- The 17:48Z TEXT REPAIR restores 2 words that the shell elided.

**AC1** (mechanical): `reread_27.py` reads READ27 27/27 (`R1_RUN/reread_27_table.json`). It reflects the irpt-status rollback to rev 3 at 16:43:21Z.

## 2. Judgment criterion for you: SA-r-1b AC2 (FWD-1 thread, round 1)

The order's AC2 text: "the one-firm proof with zero cottonwood admits, and every hop recorded with its artifact."

FWD-1 ACCEPT (PRD :30-31): "the report is made from that file without anyone re-typing the holdings, and the finished report opens from the ticket."

**Evidence (run 4, trace key `run_4`):**
- **Census:**
  - 119 live routes on `7k3ed8px20`, against 117 in the source census;
  - 91 scoped, 9 data-refresh skipped, 82 armed x 3;
  - **0 off-list admits, 0 leaks** (limb 1: no off-list payload differed; limb 2: 16 selector-ignored arms cleared by code read, 0 UNKNOWN);
  - CREATE off-list returned 400, naming the firm.
- **Hops**, each through the real CloudFront entry:

  | hop | result |
  |---|---|
  | (a) upload | 200, NORMALIZED on poll 1 (upload_id and input_id recorded) |
  | (b) ticket | 201 `TCK-20261009-67ab7f27` |
  | (c) claim | 200 |
  | (d) analysis | 200, request_id echoed |
  | (e) ready poll | 60 polls |
  | (f) report | 200 |
  | (g) open | ticket 200 + request read 200, report_ref present |

- **Corroboration:** a direct ConsistentRead of `opal-tickets` shows:
  - firm 49financial;
  - the upload door's ids on the attachment;
  - report_ref 17:31:59.179Z, naming the request;
  - status completed.
- **Cleanup and data refresh:**
  - row removed and read back ABSENT;
  - both tickets completed;
  - data-refresh calls: 0 matches over 17:19:46-17:32:01Z.

**Weigh -- what the run does NOT establish:**
1. **Hop (e) is UNVERIFIED.** The instrument polled `state` (it read `UNAVAILABLE`, a value not in the enum) instead of the contract's `stage`. The request's stage is unreadable from the executor's seat (kms:Decrypt denied on `irpt-requests`). So **whether a report was generated from the file is not shown**: a report_ref is a reference, not a report. This is the ACCEPT clause's core.
2. **The data-refresh zero has a weak denominator.** The trace records `searched_log_streams: 0` beside `match_count: 0`, with no positive control in that window.
3. **The organic arm is open.** Alyssa's own first request has not been filed: the poll (task `b7uat83gu`) reads 0 tickets at 17:52:34Z.

## 3. Rows

| row | standing | holder |
|---|---|---|
| D2-S15 (v2.1 disjoint) | RESOLVED by v2.2 | issuer |
| D2-S16/S17 (data-refresh admission) | S17 routed to `2.0.0_SA_COO~O` | `~O` |
| D2-S18 (irpt-status 500s) | world-resolved, rollback 16:43Z | IRPT_ANLREQ |
| D2-S19 (run-2 ledger after the act) | INERT; run 3 opened first | issuer |
| D2-S20 (pair rollback "remove the row" WIDENS reach until exp) | INERT; the clause is wrong for any future run | the pair's CTO half; goes in the L10 slug |
