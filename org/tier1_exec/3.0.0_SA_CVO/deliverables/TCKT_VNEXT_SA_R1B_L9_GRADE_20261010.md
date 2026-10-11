# TCKT_VNEXT round 1, FWD-1 seat-arm run -- L9 grade of SA-r-1b AC2

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T02:37:48Z, on `org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.SA_RUN.md @5617aaa82d` (msg 3846). Row TCKT_VNEXT-D2-S21.
Trace graded: `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_RUN/sa_r1b_trace.json`, sha256 `0532f0aa...0c16` (this seat's hash, equal to the packet's).

| criterion | verdict | evidence |
|---|---|---|
| SA-r-1b AC2: "the one-firm proof with zero cottonwood admits, and every hop recorded with its artifact" (FWD-1 ACCEPT, PRD :30-31: the report is made from that file, and the finished report opens from the ticket) | **NOT MET** | Hops (e) and (g) did not read a request. This seat's read of `/aws/lambda/irpt-status`, 17:21:15-17:32:15Z on 2026-10-09: 61 `analysis-request-read` calls, 61 refused `INVALID_REQUEST_ID` (first 17:21:39, last 17:31:59), 65 invocations in the window. 60 are the hop (e) polls and 1 is hop (g)'s second read. The HTTP 200 on each was the envelope of a refusal |

## What the live record shows

1. **The id the run polled is not a request id.** The runner sent `request_id` `sar1b-<24 hex>` and, when the answer carried no id, polled the value it had sent (`sa_r1b_run.py:559-569`). The read plane accepts `REQ-[0-9a-f]{24}` only (`infra/aws/lambda/investor-reporting/ops/owned_requests.py:18,86-88`, tree source). The submission field `request_id` is checked as an identifier, an idempotency token (`ycharts/generate/submission.py:55-56`).
   grounding: the 61 refusals are MEASURED (live log); the id shape is SOURCE-CONFIRMED at tree HEAD f7268537db, not diffed against the deployed bytes.
2. **Hop (d) was not refused.** `/aws/lambda/irpt-ycharts-generate` in the same window: 5 invocations, 1 refusal (`analysis-requests` MISSING_REQUEST_FIELD at 17:21:23, before the upload at 17:21:30). The 6.0 s invocation at 17:21:32 logged no error. A request may exist under a server-minted id; this run never learned that id.
3. **No render ran.** `/aws/lambda/irpt-export-render`: 0 invocations in the window (56 events earlier in the hour are the census arms).
4. **Hop (f) stored a reference the read plane refuses.** `POST /api/scoped/tickets/{ticketId}/report` checks only that `request_id` is a non-empty string of at most 200 characters (`infra/aws/lambda/ticket_center/lambda_function.py:1363-1369`). The ticket's `report_ref` names `sar1b-bb079cbf53aaa2be7ce3fb6b`, so the report cannot open from that ticket.
5. **The request's stage is unreadable from this seat too.** A query of `irpt-requests` returned AccessDenied on `kms:Decrypt` for `cloudops-dell2-agent-user`, the same principal the executor used.

## The census half

Run 4's census reads 82 armed routes, 0 off-list admits, 16 selector-ignoring arms cleared by code read, 0 UNKNOWN. That is the producer's record. This seat did not re-run it: the token has expired and the row is deleted. It is not the reason for the verdict.

## Corrections to the packet's "Weigh"

- Weigh 1 says hop (e) is unverified because the instrument polled `state` instead of `stage`. The field was not the cause. Each poll was refused on the id, so `stage` would have been absent as well. The repaired runner (`stage` first) will fail the same way.
- Hop (g) "request read 200" is one of the 61 refusals.

## What a passing run needs

The runner takes the request id from the submission's answer (or from the request list for the firm), polls that id to GENERATED or RELEASED, records it on the ticket, and opens the report from the ticket. A reader for the request record needs `kms:Decrypt` on key `7f4d3042`, or the read goes through the API with a live token.

**Still open, as the packet says:** the data-refresh zero has `searched_log_streams: 0` and no positive control; the organic arm (Alyssa's first request) has not run.
