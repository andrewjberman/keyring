# Window packet -- hop 7: ONE Analysis attempt for Cottonwood under `svc-irpt-analysis` (one upload, one Overview, no retry)

**For:** `1.0.0_SA_CTO` (CTO half; "signs on read", 103571). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~07:3xZ.
**Authority:** CTO rulings batch 61 @8dcf5bbe7a item 5; CTO 103571 (the controls are read, row S238 disarmed in row S248);
Andrew-direct 2026-09-27 ~12:4xZ, `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`
("yes you can run as many analysis attempts as needed"; lines 9-11: one upload and one submission per attempt, no retry;
lines 14-15: inside a window packet with both halves). **Ledger:** `irpt-hop7-solo-job-20261001` (legs J1, J2, J3).
**Runner:** `live_walk/hop7_run.sh` (its `--plan` printed the gate clean at 07:25Z: 0 non-terminal jobs, queue 0/0).

## The attempt

| | |
|---|---|
| principal | `svc-irpt-analysis@opalinvest.com` (durable; `allowedFirmIds` cottonwood; nothing minted, nothing deleted). Its password is read by NAME from Secrets Manager into the runner's memory and never printed |
| firm | cottonwood |
| upload body (K4, ONE POST) | `IRPT_MVP_Y/aapl-vnq-12.03.csv`, 35 bytes, sha256 `bb079cbf53aaa2be7ce3fb6beb44e55eaeb0695cd168661d5fb78488a0960ddc`: `Ticker,Dollars / AAPL,10.01 / VNQ,2.02`; `file_type` csv, `declared_currency` USD (window 15's body) |
| submission (K5, ONE POST) | `variant` overview, `comparison_keys` empty, `report_title` null, the `input_id` K4 produced |
| what runs it | `irpt-ycharts-generate` `arC65KbD..` (06:51:12Z) accepts; the resident `36dfa80058-st6` (06:02:56Z) resolves the upload and generates; `irpt-status` `2V7xV1+z..` serves the result |
| capture library | `/opt/investor-reporting-ycharts/ycharts_session.js` `0fec0ca910ee5fb1..` (IB-yr-292). **No capture has run on it.** Against the library every earlier job used (`dfc87d83..`) it adds the opt-in HAR recording (off: neither env var is set) and an explicit `ctx.close()` before the browser closes, at three sites. A failure signature that differs from the three recorded ones is read against that change first |

## Write set

- **Opal, by K4:** one retained upload object and its `UPLOAD#` and `NORMALIZATION#` rows; on NORMALIZED one normalized
  input object and its `INPUT#` row; one `resolve_upload` message on `irpt-generation`.
- **Opal, by K5:** one composition object, its retention and artifact rows, one `analysis#REQ-..#1` row, one `irpt-jobs`
  row, one `analysis_generate` message.
- **Opal, by the resident:** the job's checkpoints and state; if the vendor serves a PDF, the retained vendor PDF, the
  extraction evidence and the certified report; if the stored session is evicted, ONE new version of
  `ycharts/session/current` (the one admitted refresh).
- **YCharts (the vendor calls this attempt causes):** symbol resolution for two tickers; one holdings upload; one model
  portfolio; its status and saved-settings reads (up to 6 status polls, ONE re-capture on a read WAF challenge: CTO
  101792); one report generation; one PDF download. At most ONE session capture (login) by the one-refresh allowance.
- All in Cottonwood's partition. Nothing in another firm's.

## Stops

1. Both halves at HEAD naming this file's blob, before the secret is read.
2. The solo gate at fire time: no job in a non-terminal state and `irpt-generation` 0/0, or nothing is posted.
3. ONE login. EXACTLY one K4 POST and one K5 POST (`live_chain.py:144-146` and `:168-169`). If the upload does not read
   NORMALIZED, K5 is NOT made and the attempt is over. Outcomes are read from DynamoDB, never by a second POST.
4. No retry and no second attempt under this packet, whatever the outcome. A second attempt is a new packet.
5. Deadline: 60 minutes from fire. At the deadline the runner stops waiting; the job's state is read by name.
6. Any deviation not named here stops the window for a new half.

## What is read afterwards (the ledger's legs)

- **J1:** the scrubbed call log (`HOP7/H7_overview_cottonwood.json`): login status; one K4 and one K5; the request id.
- **J2:** the `irpt-jobs` row's terminal state and code BY NAME; every `IRPT_RESIDENT_EVICTION verdict=` and
  `IRPT_RESIDENT_ATTENTION code=` line and every `retained_for_retry` line of the span; the upload's normalization state
  and reason. If READY: the receipt's `vendor_requests` (IB-yr-291, shapes only) and `case_trace.py cottonwood <REQ>`.
  This names row S230's cause or produces the report.
- **J3:** `irpt-generation` and its dead-letter queue depths (both 0/0 now); no second POST made.
- If READY, `2.0.0_SA_COO~D` walks that request on the page: the thread's last link (batch 61 items 1 and 6).

## Rollback

There is none for a vendor call that was made. The Opal rows are append-only records of the attempt; a job that does
not finish ends by name (ATTENTION or NEEDS_CORRECTION) or, on a transient session failure, retries on the queue's own
redelivery up to its fifth receive.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~07:3xZ, on this packet's bytes at the commit that carries it.

## CTO half -- 1.0.0_SA_CTO

(owed)
