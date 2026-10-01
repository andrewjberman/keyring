# Window packet -- hop 8, on the st7 resident: leg P (ONE liveness read), leg S (ONE operator sign-in, only if the session is not live), leg J (ONE job attempt)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~10:3xZ.
**Authority:** CTO rulings batch 76 item 5 ("ONE job attempt follows it under a window packet"); Andrew-direct
2026-09-27 (`ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`) for leg J; his standing word of 2026-09-23
item 3 (the host's own session sign-in and maintenance) for legs P and S. **Precondition, met:** st7 is installed
(`ST7/INSTALL_OUTPUT_20261001.txt`: running root `a3b35fd376-st7` since 10:27:05Z, digests equal the signed packet's;
ledger `irpt-resident-st7-20261001` CLOSED). **Ledger:** `irpt-hop8-probe-signin-job-20261001` (legs P1, S1, J1, J2,
J3). **Runner:** `live_walk/hop8_run.sh`; every leg refuses unless the running root is the st7 root.

## The legs

- **Leg P, one GET, no sign-in:** `live_walk/session_probe_host.sh` (sha256 `d3fef0997c999014..`, the script the third
  window ran): the report-template route through the resident's classes, capture removed.
  - `LIVE`: leg J runs. Leg S is not run.
  - `NOT_LIVE:<status>` (the session was displaced): leg S runs.
  - `CHALLENGED`, `RAISED` or `NOT_RUN`: the packet ends. Nothing else is sent.
- **Leg S, ONE operator sign-in, only on `NOT_LIVE`:** `live_walk/leg_s_host.sh` (sha256 `c2ec45793fbfbabe..`, the
  script the second window ran): the canonical wrapper once, as the resident's user with the resident's environment.
  It is the path that signed in at 08:21Z, and here it is the FIRST sign-in on the st7 library (`9511060e..`).
  - `AUTHENTICATED`: one new stored session version; leg J runs, not sooner than 600 seconds after leg S ended. The
    spacing is deliberate: at 08:22Z the lookups of the four minutes after a sign-in were refused, cause unread.
  - `FAILED` or `CHALLENGED`: nothing is written; the receipt carries the st7 reason token; the packet ends; no
    further sign-in from this host for 24 hours (batch 70 item 4: this would be today's second failure).
- **Leg J, one job attempt:** the hop-7 shape unchanged: `svc-irpt-analysis@opalinvest.com`, Cottonwood, ONE K4 POST of
  `aapl-vnq-12.03.csv` (35 bytes, sha256 `bb079cbf..0960ddc`), ONE K5 POST (`overview`, no comparison key), no retry,
  a 60-minute deadline. Evidence base `HOP8/H8_overview_cottonwood`. Write set and vendor calls as
  `HOP7/WINDOW_PACKET_HOP7_SOLO_JOB_20261001.md` lists them, with one difference in st7: the ticker lookup carries no
  cookie.

## What each stop of leg J reads, of the three things that run live for the first time (CTO half of st7, item 2)

| where the attempt stops | which new thing it exercised | what is read |
|---|---|---|
| the upload does not read NORMALIZED | the SESSIONLESS LOOKUP through the resident's own child process, and the REFUSAL CLASS | the journal's `RESOLVE state=RETRY code=PROVIDER_READ_UNAVAILABLE:<CLASS>` lines; the class names the cause (a status, a WAF action, a login page, a lease or child-process code); the seconds since the last sign-in beside it (third-window half, item 10). K5 is not made; no vendor mutation happened |
| the upload reads NORMALIZED | the sessionless lookup SERVED | `RESOLVE state=READY` on the first receive |
| the job reads EVICTED | the st7 SIGN-IN REASON TOKEN and the kept stderr, if the resident's own sign-in then fails | `CAPTURE_FAILED:AUTH_FAILED:<REASON>` and `/opt/investor-reporting-ycharts/last-capture.stderr` (read on the host, masked); reported FIRST (stop 5) |
| the job is refused at the printed-type check | the ROW CENSUS and the KEPT PDF | `IRPT_RESIDENT_TOLERANCE_ROWS pages= table_pages= name_lines= accepted= refused=` and `IRPT_RESIDENT_REFUSED_PDF kept=1 artifact=`; then, BEFORE the PDF is used for anything, one live read of the job's status and sections routes as the service principal, which must show UNAVAILABLE with no document (CTO half of st7, item 1); then the settings-table lines of the kept PDF are read by this seat to a scratch directory outside the repo (the lane's own AAPL and VNQ test upload), which names the reader's repair and gives it its fixture |
| the job reads READY | none of the three refusals; hop 8 PASSED | the receipt's vendor request shapes, `case_trace.py cottonwood <REQ>`; `2.0.0_SA_COO~D` walks the request on the page |

## Stops

1. Both halves at HEAD naming this file's blob, before any leg.
2. Before each leg: the running root is `a3b35fd376-st7`; no non-terminal job; both queues 0/0.
3. Each leg ONCE; the runner refuses a leg whose output file exists. At most ONE sign-in by the operator (leg S).
4. Leg J: ONE login to Opal, EXACTLY one K4 POST and one K5 POST. If the upload does not read NORMALIZED, K5 is not
   made and the attempt is over.
5. The resident's own sign-in, named as in the second and third windows: if the session is displaced after leg P or
   leg S and before the job's first read, the job reads EVICTED and the resident takes its one refresh by itself. It
   cannot be prevented after K5. If it happens it is reported first; whatever its result, no further sign-in is made
   from the host today.
6. A read challenge or a still-calculating portfolio releases the message for redelivery; the job may take several
   receives. At the 60-minute deadline a job still non-terminal is reported to `1.0.0_SA_CTO` before anything is
   posted or redriven.
7. Each output file is read for values before it is committed. A kept PDF is not committed and not uploaded anywhere.
8. Any deviation not named here stops the window for a new half.

## Rollback

None for a vendor call that was made. Opal rows are append-only records of the attempt. A kept refused PDF is an
unreferenced artifact under its family's existing 30-day rule.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~10:3xZ, on this packet's bytes at the commit that carries it. Both host scripts are the bytes two
earlier windows ran today without a deviation; the runner's gates were read in `bash -n` and its plan mode.

## CTO half -- 1.0.0_SA_CTO

SIGNED, 2026-10-01T10:43Z, on the pre-signature blob `4ab72f71b2` (@ffed19c0ae). Leg P is ONE GET; leg S is at most ONE operator
sign-in and runs only on `NOT_LIVE`; leg J is ONE job attempt. Stops 1 to 8 stand as written.

Vendor authority, read by this seat earlier today in the record's own lines: legs P and S are the host's session sign-in and
maintenance (Andrew's standing word of 2026-09-23 item 3); leg J is one attempt inside his word of 2026-09-27. No new vendor use
is created.

Read by this seat before signing:

- The two host scripts at ffed19c0ae hash to `d3fef0997c999014` and `c2ec45793fbfbabe`: the bytes this seat read in full for the
  third and second windows. Neither changed.
- `ST7/INSTALL_OUTPUT_20261001.txt`: the running root is `a3b35fd376-st7`; `resident_worker` `2ba09afaa8a2fc9e`,
  `current_authority` `5291b3be7e0006ad`, `host_capture` `8288e724e843cb89`, `extract` `3f5e2bb0bc2299f6`, the host library
  `9511060e04f45b51`, each equal to the value this seat signed on the st7 packet; queue 0/0. The precondition is met.

The table of what each stop reads carries items 1 and 2 of the st7 half. All five outcomes of leg J and all three of leg S are
covered.

Named by this half in addition:

9. LEG S, IF IT RUNS, IS THE FIRST SIGN-IN ON THE st7 LIBRARY. Its change is record literals only, read line by line by this
   seat. If it fails where the same wrapper authenticated at 08:21Z, the receipt's reason token and step list are reported
   before anything else, and the library's rollback (the `.before-a3b35fd376-st7` file, with the st6 root) is a new half, not
   a reflex.
10. THE 600-SECOND SPACING after a sign-in is accepted as a measurement aid, not as a fix: if the lookup is refused after it,
    the refusal class and the seconds since the sign-in are the finding.
11. Not verified by this seat: `hop8_run.sh` (its gates and plan mode are the COO's read).
