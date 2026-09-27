# ANDREW-DIRECT 2026-09-27 ~02:0xZ -- yes to ONE YCharts wrapper run (S151)

**Channel:** the 1.0.0_SA_CTO terminal. **Recorded by:** 1.0.0_SA_CTO, the same turn.

## Verbatim

> "yes on the YCharts wrapper run, one run"

## The call it answers

S151 (IRPT_BCKEND, ARMED, owner 2.0.0_SA_COO~Y). Window 6's receive 1 (00:12:08Z) failed in the resident's YCharts
session capture, and the cause is unmeasured: the static causes were ruled out read-only @`27cbee90e4`. The next
Analysis window is blocked on it (STATUS~P @`b561fb334f`). The diagnostic run is a live YCharts headless session
capture. That is vendor egress which the arm's "API calls" did not plainly cover, so it was put to Andrew
(tick log @`6e795f1658`).

## What it authorizes, exactly

- **ONE** run of the session-capture wrapper, by 2.0.0_SA_COO~Y, to measure receive 1's failure cause.
- **No vendor write:** no upload, submission or settings change at YCharts.
- **No retry loop.** A second run needs a new word.
- **Ledgered:** the run gets its own entry in `org/critical_paths/change_management/`, opened before the run and closed
  with the result. It is carried to S151's disarm.
- **Credentials:** never printed or logged; any HAR is scrubbed.

## What it does not authorize

Any further YCharts call, a live Analysis window, or any served-output move. Those keep their own mechanisms.
