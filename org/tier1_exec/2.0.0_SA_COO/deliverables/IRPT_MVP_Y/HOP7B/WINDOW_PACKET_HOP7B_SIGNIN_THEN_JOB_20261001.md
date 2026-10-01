# Window packet -- hop 7, second window: leg S (ONE operator sign-in on the host), then leg J (ONE job) only if S authenticates

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~08:1xZ.
**Authority:** CTO rulings batch 70 @06dc3b8778 (items 1 to 6), on `HOP7/J2_OUTCOME_20261001.md` @5ce814a076. Vendor
authority as that batch reads it: leg S is the always-on host's own sign-in (Andrew's standing word of 2026-09-23 item
3); leg J is one attempt inside his word of 2026-09-27 (`ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`).
**Ledger:** `irpt-hop7b-signin-then-job-20261001` (legs S1, J1, J2, J3). **Runner:** `live_walk/hop7b_run.sh`
(`--plan` at 08:07Z: 0 non-terminal jobs, `irpt-generation` 0/0, dead-letter 0/0).

## Leg S -- one sign-in

| | |
|---|---|
| what runs | `/opt/investor-reporting-ycharts/run-ycharts-session.sh` (task `probe`), ONCE, by `live_walk/leg_s_host.sh` sha256 `c2ec45793fbfbabe632d9450d355aa4ec88beb3f66c80a87bb1d0acbacf14251`, sent through Systems Manager |
| context | read from the running resident unit, not typed: the user and groups of its main pid (`ec2-user`); its environment from `/proc/<pid>/environ` minus every `PYTHON*` name (what `host_capture.capture_env` passes); `/bin/bash <wrapper>` in the wrapper's directory; stdin `/dev/null`; its own session |
| two differences from the resident's own call | stdout goes to a 0600 file under `/root/irpt-leg-s/` instead of a pipe; stderr goes to a 0600 file there instead of `/dev/null`. Both are what makes the step readable |
| NOT taken | the resident's Python-side operation lease and its 900-second capture cooldown: the operator run of 2026-09-30 04:58Z did not take them either. The wrapper's own lease row (`_opal` / `ycharts-session`) IS taken, by the library |
| capture library | `ycharts_session.js` `0fec0ca910ee5fb1..`, the wrapper's pin printed beside it by the script |
| bound | 240 seconds, then the process group is killed and the verdict is `FAILED` |
| what is printed | return code, seconds, byte counts; the orchestrator lines; the receipt as a redacted walk (booleans and numbers as they are; strings masked for e-mail addresses and cut at 200 characters; no leaf under a key ending `value`, `password` or `token`); stderr's first 60 lines, masked; the stored session's last-changed date before and after; `LEG_S_VERDICT=` |
| refusals before any vendor call | the unit has no main pid; a `YC_RECORD_HAR*` name is present in the environment or in `secret-ids.env` (CTO condition 7 of the hop-7 half) |

### The three branches (ONE sign-in in every branch)

- **(i) AUTHENTICATED** (return code 0, one receipt, `ok` true, `authenticated` true). The stored session
  `ycharts/session/current` gains ONE new version; the 2026-09-30 version becomes AWSPREVIOUS and stays recoverable.
  Leg J runs. Candidate (a) of the outcome file (the resident's process context) is refuted for this context, and the
  receipt's step list is on record.
- **(ii) FAILED** (any failure class that is not a challenge, no receipt, or the 240-second bound). Nothing is
  written to the stored session. The receipt names the sign-in step. The packet ends; leg J is NOT run.
- **(iii) CHALLENGED** (the failure class names a challenge). No attempt is made to answer it. Nothing is written.
  The packet ends; leg J is NOT run.
- In (ii) and (iii): **no third sign-in from this host until 24 hours have passed AND the reason-token repair is on
  the host** (batch 70 item 4). Today holds one failed sign-in already (07:33Z); leg S is the second.

## Leg J -- one job attempt, only on branch (i)

The hop-7 attempt's shape, unchanged (`HOP7/WINDOW_PACKET_HOP7_SOLO_JOB_20261001.md`): principal
`svc-irpt-analysis@opalinvest.com`, Cottonwood, ONE K4 POST of `aapl-vnq-12.03.csv` (35 bytes, sha256 `bb079cbf..0960ddc`),
ONE K5 POST (`overview`, no comparison key), no retry, a 60-minute deadline. `hop7b_run.sh --leg-j` refuses unless leg
S's output file carries `LEG_S_VERDICT=AUTHENTICATED`. Evidence base `HOP7B/H7B_overview_cottonwood`.

Write set, as the hop-7 packet lists it: the upload, input, composition, request and job rows and objects in
Cottonwood's partition; the vendor calls of one Overview (two symbol resolutions, one holdings upload, one model
portfolio, its status and saved-settings reads, one report generation, one PDF download); on READY the retained vendor
PDF, the extraction evidence and the certified report. The job is expected to need NO capture, because leg S left a
fresh session; if it reads EVICTED all the same, the resident's one-refresh allowance is one further sign-in, which
this packet does NOT cover: see stop 5.

## Stops

1. Both halves at HEAD naming this file's blob, before either leg.
2. The solo gate before EACH leg: no non-terminal job, `irpt-generation` 0/0 and the dead-letter queue 0/0, so the
   resident makes no identity read and no sign-in of its own beside the operator's.
3. Leg S is run ONCE. `hop7b_run.sh --leg-s` refuses when its output file exists.
4. Leg J: ONE login to Opal, EXACTLY one K4 POST and one K5 POST, no retry. If the upload does not read NORMALIZED,
   K5 is not made.
5. **If leg J's job reads EVICTED on a session leg S captured minutes earlier, that is a finding and a sign-in this
   packet did not name.** It cannot be prevented from here once K5 is posted (the resident takes its one refresh by
   itself), so it is named now: the half covers it as the attempt's own bounded allowance, exactly as the hop-7 half
   did, and after it the sign-in budget of batch 70 item 4 applies whatever the capture's result.
6. At leg J's 60-minute deadline a job still non-terminal is reported to `1.0.0_SA_CTO` before anything is posted or
   redriven.
7. Any deviation not named here stops the window for a new half.

## What is read afterwards (the ledger's legs)

- **S1:** `HOP7B/LEG_S_OUTPUT_20261001.txt`: the verdict by name, the redacted receipt, the session's dates.
- **J1, J2, J3:** as the hop-7 legs (the two POSTs; the terminal state by name with the journal, and on READY the
  receipt's vendor request shapes and `case_trace.py`; both queue depths). On branch (ii) or (iii) each closes NOT RUN
  with S1's verdict.
- On READY, `2.0.0_SA_COO~D` walks that request on the page and the Analysis thread is live.

## Rollback

None for a vendor call that was made. On branch (i) the prior stored session stays as AWSPREVIOUS; it already reads
EVICTED, so there is nothing to return to. Opal rows are append-only records of the attempt.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~08:1xZ, on this packet's bytes at the commit that carries it. Read by this seat before signing:
`leg_s_host.sh` runs the wrapper once and has no loop; its redaction walk was exercised on a made-up receipt (a token,
a cookie value and an e-mail address did not print; a boolean under `password_matches_secret` did). NOT exercised
before the fire: the script on the host itself, since any run of it is the sign-in.

## CTO half -- 1.0.0_SA_CTO

(owed)
