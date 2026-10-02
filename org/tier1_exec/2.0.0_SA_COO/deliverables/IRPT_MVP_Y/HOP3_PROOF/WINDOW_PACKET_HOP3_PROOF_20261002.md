# Window packet -- hop 3's proof on the st10 resident: an upload resolves while another job's generation is in flight; leg P, leg S (only if the session is not live), leg A (ONE Overview job), leg B (ONE upload, no submission, during A)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~06:2xZ.
**Authority:** CTO rulings batch 61 item 8 (after the catalogue: "the resolve concurrency fix (hop 3)") and batch 72 item 12
(its remedy: the upload's ticker lookup is made without the session); Andrew-direct 2026-09-27
(`ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`, "as many analysis attempts as needed") for legs A and B;
his standing word of 2026-09-23 item 3 for legs P and S, with batch 88 item 3's terms for the sign-in. **Ledger:**
`irpt-hop3-proof-20261002` (legs P1, S1, A1, B1, V1). **Runner:** `live_walk/hop3_proof_run.sh` (the hop-8 runner for P, S
and A with this window's folder, the st10 root and base; leg B is new). Every leg refuses unless the running root is
`b1db201025-st10`.

## Why this shape and not "two uploads 10 s apart"

The trace's proof sentence ("two uploads 10 s apart both reach NORMALIZED") does not reproduce the failure. Row S206 found
every exhausted resolve dispatched while other work was in flight on the same principal (3 of 3; the 2 READY bodies had
none); row S215 pinned the condition to a live GENERATION (arm 2 was dispatched into arm 1's job, `irpt-jobs` read
SUBMITTING with `session_refresh` across arm 2's whole resolve window). A resolve takes about a second, so two uploads 10 s apart would usually not overlap at all. Batch 72 item 12's
remedy (st7, `1253002a2f`, still in st10): the lookup carries no session, under the provider lease with its spacing and
deadline. So the proof is: leg B's upload resolves NORMALIZED while leg A's job is non-terminal.

## The legs

- **Leg P, one GET, no sign-in:** `live_walk/session_probe_host.sh` (sha256 `d3fef0997c999014..`, unchanged). `LIVE`: leg A
  runs. `NOT_LIVE:<status>`: leg S runs. `CHALLENGED`, `RAISED`, `NOT_RUN`: the packet ends.
- **Leg S, ONE operator sign-in, only on `NOT_LIVE`:** `live_walk/leg_s_host.sh` (sha256 `c2ec45793fbfbabe..`, unchanged),
  under batch 88 item 3's terms: at most once in 24 hours (the last host sign-in was 2026-10-01T08:21Z). `AUTHENTICATED`:
  leg A runs, not sooner than 600 seconds later. `FAILED` or `CHALLENGED`: the packet ends.
- **Leg A, one Overview job attempt:** `svc-irpt-analysis@opalinvest.com`, Cottonwood, ONE K4 POST of `aapl-vnq-12.03.csv`
  (35 bytes, sha256 `bb079cbf..`), ONE K5 POST, Overview (no comparison keys). No retry; a 60-minute deadline. Base
  `HOP3_PROOF/H3_A_overview_cottonwood`. Run in the background; it returns when the job is terminal.
- **Leg B, one upload, NO submission:** the same principal and file, ONE K4 POST with `WALK_K4_ONLY=1`, so `live_chain.py`
  returns after the resolve and never posts K5. The runner reads leg A's job from `irpt-jobs` first and REFUSES unless it is
  non-terminal (`RECEIVED` .. `CERTIFYING`): the condition under test. Fired once leg A's job reads `SUBMITTING` or later,
  and printed again after the resolve. A 20-minute deadline. Base `HOP3_PROOF/H3_B_upload_cottonwood`.

Vendor calls: leg A as every Overview attempt (two sessionless symbol lookups, one holdings upload, one model portfolio,
its status reads, report validation, ONE report generation, one PDF download); leg B two sessionless symbol lookups only.
The file is the two-ticker test portfolio, not a client's. Nothing of another firm's is read or written.

## What each outcome reads

| outcome | read |
|---|---|
| **leg B reads NORMALIZED while A's job is non-terminal** | hop 3 is closed on served code: the resident journal's `IRPT_RESIDENT_RESOLVE` line for B and A's job state before and after; row S215's remedy is evidenced |
| leg B reads `NEEDS_CORRECTION RESOLVE_RETRY_EXHAUSTED` | the remedy does not hold under a live generation: every `PROVIDER_READ_UNAVAILABLE:<CLASS>` line (st7's classes) is quoted and goes to `1.0.0_SA_CTO` before anything else |
| leg A reads READY | the first live read of st10's items 15 and 16 (CTO batch 106 item 1): the journal's `IRPT_RESIDENT_VENDOR_REQUESTS kept=N`, the job row's `vendor_requests` count against the requests the job made, every receive quoted with its time; `job_status_route_read.py` and `case_trace.py` as for every READY job |
| leg A's job meets a challenged read | item 15's `WAF_READ header=<token>` is quoted; the receive keeps 900 s |
| leg A reads EVICTED or ATTENTION | reported first; leg B is not run if A is already terminal |

## Stops

1. Both halves at HEAD naming this file's blob, before any leg.
2. Before legs P, S and A: the running root is `b1db201025-st10`; no non-terminal job; both queues 0/0. Before leg B: the
   running root, and leg A's job non-terminal.
3. Each leg ONCE (the runner refuses a leg whose output exists). At most ONE operator sign-in.
4. Leg A: ONE login, EXACTLY one K4 and one K5 POST; if its upload does not read NORMALIZED, K5 is not made and leg B is
   not run. Leg B: ONE login, EXACTLY one K4 POST, never a K5.
5. At leg A's 60-minute deadline a job still non-terminal is reported to `1.0.0_SA_CTO` before anything is posted or
   redriven.
6. Each output file is read for values before it is committed. A kept PDF is not committed.
7. Any deviation not named here stops the window for a new half.

Leg A adds one accepted Cottonwood request (18 to 19). E6's measure puts a cold history list near the 15 s timeout at about
22, and CTO batch 111 names a timeout packet at 20; this window does not reach it.

## Rollback

None for a vendor call that was made. Opal rows are append-only records of the attempt; leg B's upload and normalization
rows reference no request.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~06:2xZ, on this packet's bytes at the commit that carries it. The two host scripts are unchanged by
sha256; the runner's plan ran at 06:12Z (root `b1db201025-st10`, no non-terminal job, both queues 0/0; both bodies validated
offline, leg B's with no K5).

## CTO half -- 1.0.0_SA_CTO

(not signed)
