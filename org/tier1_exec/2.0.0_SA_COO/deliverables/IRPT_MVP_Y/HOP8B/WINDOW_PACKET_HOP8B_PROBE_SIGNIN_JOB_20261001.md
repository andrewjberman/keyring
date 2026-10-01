# Window packet -- second hop-8 window, on the st8 resident: leg P (ONE liveness read), leg S (ONE operator sign-in, only if the session is not live), leg J (ONE job attempt)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~12:0xZ.
**Authority:** CTO rulings batch 76 item 5 and batch 83 ("the window packet for the one attempt follows"); Andrew-direct
2026-09-27 (`ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`) for leg J; his standing word of 2026-09-23
item 3 for legs P and S. **Precondition, met:** st8 is installed (`ST8/INSTALL_OUTPUT_20261001.txt`: running root
`9ac9b56d3c-st8` since 11:58:05Z; `resident_worker` `8ba63ba0fc0bff78`, `extract` `c4c4908338fdce62`, the library
unchanged; ledger `irpt-resident-st8-20261001` CLOSED). **Ledger:** `irpt-hop8b-probe-signin-job-20261001` (legs P1,
S1, J1, J2, J3). **Runner:** `live_walk/hop8b_run.sh`, which is `hop8_run.sh` with this window's folder, root and
base; every leg refuses unless the running root is the st8 root.

## The legs -- as the first hop-8 window, whose packet is `HOP8/WINDOW_PACKET_HOP8_PROBE_SIGNIN_JOB_20261001.md`

- **Leg P, one GET, no sign-in:** `live_walk/session_probe_host.sh` (sha256 `d3fef0997c999014..`, unchanged).
  `LIVE`: leg J runs. `NOT_LIVE:<status>`: leg S runs. `CHALLENGED`, `RAISED`, `NOT_RUN`: the packet ends.
- **Leg S, ONE operator sign-in, only on `NOT_LIVE`:** `live_walk/leg_s_host.sh` (sha256 `c2ec45793fbfbabe..`,
  unchanged). `AUTHENTICATED`: leg J runs, not sooner than 600 seconds after leg S ended. `FAILED` or `CHALLENGED`:
  the receipt carries the reason token; the packet ends; no further sign-in from the host for 24 hours.
- **Leg J, one job attempt:** `svc-irpt-analysis@opalinvest.com`, Cottonwood, ONE K4 POST of `aapl-vnq-12.03.csv`
  (35 bytes, sha256 `bb079cbf..0960ddc`), ONE K5 POST (`overview`, no comparison key), no retry, a 60-minute deadline.
  Evidence base `HOP8B/H8B_overview_cottonwood`.

## What each stop of leg J reads

| where the attempt stops | what is read |
|---|---|
| the upload does not read NORMALIZED | the `RESOLVE state=RETRY code=PROVIDER_READ_UNAVAILABLE:<CLASS>` lines and the seconds since the last sign-in. K5 is not made |
| the job reads EVICTED | reported FIRST; if the resident's own sign-in then fails, `CAPTURE_FAILED:AUTH_FAILED:<REASON>` and `last-capture.stderr` |
| the job is refused at the printed-type check | `TOLERANCE_TYPE`, `TOLERANCE_ROWS` (with `cut=`) and `REFUSED_PDF kept=1`; the live status read first (`job_status_route_read.py`), then the kept PDF's table lines |
| **the printed-type check passes** | the line `IRPT_RESIDENT_TOLERANCE_TYPE type=Static as_of=Custom name=cut` (or `name=whole`), QUOTED in the outcome: it is the first live use of the repair (st8 half, item 2). Then the job certifies and publishes, or stops by name at a later step, which is read from the journal and the job row |
| the job reads READY | the receipt's vendor request shapes; `job_status_route_read.py` on the request (expected: a served document); `case_trace.py cottonwood <REQ>`, whose own name match on the retained PDF is the OLD exact rule and may read a mismatch on a cut name: that would be the trace tool's defect, named, not the job's; `2.0.0_SA_COO~D` walks the request on the page (hop 10 on a service-principal request) |

A known 15 minutes: twice today the first receive's second status poll drew a 202 read challenge and the message was
released; the second receive finished the job. The same is expected here and is not a failure (stop 6).

## Stops

1. Both halves at HEAD naming this file's blob, before any leg.
2. Before each leg: the running root is `9ac9b56d3c-st8`; no non-terminal job; both queues 0/0.
3. Each leg ONCE; the runner refuses a leg whose output file exists. At most ONE sign-in by the operator (leg S).
4. Leg J: ONE login to Opal, EXACTLY one K4 POST and one K5 POST. If the upload does not read NORMALIZED, K5 is not
   made and the attempt is over.
5. If the session is displaced after leg P or leg S and before the job's first read, the job reads EVICTED and the
   resident takes its one refresh by itself. It is reported first; whatever its result, no further sign-in is made
   from the host today.
6. A read challenge or a still-calculating portfolio releases the message for redelivery. At the 60-minute deadline a
   job still non-terminal is reported to `1.0.0_SA_CTO` before anything is posted or redriven.
7. Each output file is read for values before it is committed. A kept PDF is not committed and not uploaded anywhere.
8. Any deviation not named here stops the window for a new half.

## Rollback

None for a vendor call that was made. Opal rows are append-only records of the attempt. A READY report is the firm's
own test upload (AAPL and VNQ, 12.03 dollars), as the five earlier READY reports are.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~12:0xZ, on this packet's bytes at the commit that carries it. The two host scripts are the bytes
the earlier windows ran; the runner differs from the first hop-8 window's only in taking its folder, root, base and
ledger from the wrapper.

## CTO half -- 1.0.0_SA_CTO

(owed)
