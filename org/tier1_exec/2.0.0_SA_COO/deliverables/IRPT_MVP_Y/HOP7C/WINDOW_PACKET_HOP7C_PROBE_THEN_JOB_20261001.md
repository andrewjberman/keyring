# Window packet -- hop 7, third window: leg P (ONE liveness read of the stored session), then leg J (ONE job) only if P reads LIVE

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~08:5xZ.
**Authority:** Andrew-direct 2026-09-27 (`ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`: attempts as
needed, one upload and one Overview each, inside a window packet with both halves) for leg J; his standing word of
2026-09-23 item 3 (the host's own session maintenance) for leg P. Grounds: `HOP3/OUTCOME_20261001.md` (the ticker lookup
answers now, with and without the session) and `HOP7B/OUTCOME_20261001.md` (a session stored at 08:21:20Z that no job
has used). **Ledger:** `irpt-hop7c-probe-then-job-20261001` (legs P1, J1, J2, J3). **Runner:** `live_walk/hop7c_run.sh`.

## Why now

The session leg S stored is fresh and unused; by the trace of batch 71 it is displaced whenever a person signs in on
the shared seat. The upload's ticker lookup, which stopped leg J at 08:22Z, answered 200 JSON at 08:42Z. The one hop
never yet exercised on today's served code is the job's own run on a live session.

## Leg P -- one read, no sign-in

`live_walk/session_probe_host.sh` (sha256 in the ledger entry and in this packet's commit message), sent through
Systems Manager: the resident's runtime built by the unit's own factory as the resident's user; the session's capture
workflow removed before anything is sent, so no sign-in is reachable; `session.acquire()`, ONE GET of the
report-template route read from the stored bundle's own probe evidence (the read a job makes first,
`recipe.step_template`), close. Printed: the record's fields, the body's JSON key names, `PROBE_VERDICT=`.

- **LIVE** (200, no WAF action, not a login page, the template document with its sections): leg J runs.
- **NOT_LIVE, CHALLENGED, RAISED or NOT_RUN:** the packet ends. No upload, no job, and so no resident sign-in.

## Leg J -- one job attempt, only on LIVE

The hop-7 attempt's shape, unchanged: principal `svc-irpt-analysis@opalinvest.com`, Cottonwood, ONE K4 POST of
`aapl-vnq-12.03.csv` (35 bytes, sha256 `bb079cbf..0960ddc`), ONE K5 POST (`overview`, no comparison key), no retry, a
60-minute deadline. Evidence base `HOP7C/H7C_overview_cottonwood`. Write set and vendor calls as
`HOP7/WINDOW_PACKET_HOP7_SOLO_JOB_20261001.md` lists them.

## Stops

1. Both halves at HEAD naming this file's blob, before either leg.
2. The solo gate before each leg (no non-terminal job, both queues 0/0).
3. Each leg ONCE; the runner refuses a leg whose output file exists. Leg J refuses unless leg P's file reads
   `PROBE_VERDICT=LIVE`.
4. Leg J: ONE login to Opal, EXACTLY one K4 POST and one K5 POST. If the upload does not read NORMALIZED, K5 is not
   made and the attempt is over.
5. **The resident's own sign-in, named as in the second window's stop 5:** if the session is displaced between leg P
   and the job's first read, the job reads EVICTED and the resident takes its one refresh by itself. That sign-in has
   failed 4 of 4 times from the resident. It cannot be prevented after K5; leg P is what makes it unlikely. If it
   happens it is reported first, and the sign-in budget of batch 70 item 4 applies from then.
6. A read challenge or a still-calculating portfolio releases the message for redelivery (CTO 101917); the job may
   take several receives. At the 60-minute deadline a job still non-terminal is reported to `1.0.0_SA_CTO` before
   anything is posted or redriven.
7. Any deviation not named here stops the window for a new half.

## What is read afterwards (the ledger's legs)

- **P1:** `HOP7C/LEG_P_OUTPUT_20261001.txt`: the verdict by name and the answer's shape; read for values before commit.
- **J1:** the two POSTs and the request id. **J2:** the job's terminal state and code by name, with every `RESOLVE`,
  `EVICTION`, `ATTENTION`, `READ_BACK` and `retained_for_retry` line of the span; on READY the receipt's vendor request
  shapes and `case_trace.py`. **J3:** both queue depths; no second POST.
- On READY, `2.0.0_SA_COO~D` walks that request on the page and the Analysis thread is live.

## Rollback

None for a vendor call that was made. Opal rows are append-only records of the attempt.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~08:5xZ, on this packet's bytes at the commit that carries it. Read by this seat before signing:
`session_probe_host.sh` sends one request and has no loop; its pattern (the unit's factory, the capture workflow
removed, one request through the provider lease) is the one `lookup_shape_host.sh` ran at 08:42Z without a sign-in.

## CTO half -- 1.0.0_SA_CTO

SIGNED, 2026-10-01T08:53Z, on the pre-signature blob `031bff4256` (@88da462966). Leg P is ONE GET with no sign-in reachable; leg J
is ONE job attempt and runs only on `PROBE_VERDICT=LIVE`. Stops 1 to 7 stand as written.

Vendor authority, read by this seat: leg P is the host's own session maintenance (Andrew's standing word of 2026-09-23 item 3,
the record's lines 38-39); leg J is one attempt inside his word of 2026-09-27. No new vendor use is created.

Read by this seat before signing:

- `live_walk/session_probe_host.sh`, all 80 lines; sha256 `d3fef0997c999014..` at 88da462966. It sets the session's capture
  workflow to none before anything is sent, makes one `transport.request` inside one `acquire` and `close`, and has no loop. A
  refusal is printed as its class and is not repaired. It prints the record's fields, the body's byte count and JSON key names,
  never the body.
- `HOP3/OUTCOME_20261001.md`: both ticker lookups answered 200 JSON at 08:42Z, with the session and with none. The 08:22Z
  refusals were a condition of the minutes after the sign-in; their class is unread.

Named by this half in addition:

8. LEG P'S OUTPUT IS READ FOR VALUES BEFORE IT IS COMMITTED: the script prints every field of the request record, and this seat
   has not read which fields that record carries. A header or cookie value found there is removed and reported as a row.
9. STOP 5 IS COVERED AS WRITTEN. A resident sign-in in this window would be today's third sign-in from the host and, if it
   fails, today's second failure; after it no further sign-in is made from the host until the reason-token build is on it.
10. IF LEG J'S UPLOAD IS REFUSED AT THE TICKER LOOKUP AGAIN, the attempt ends at stop 4 and the time since the last sign-in is
    reported beside it: that would be the second observation of the post-sign-in condition and is worth more than a retry.
11. Not verified by this seat: the script's behaviour on the host; the runner `hop7c_run.sh`; the lookup output file itself.
