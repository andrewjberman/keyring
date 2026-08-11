# Andrew-direct — BG publish override + schedule move 7a->9a ET (2026-08-11, Teams 1:1)

Channel: Andrew-direct to 0.0.3_BG_BBGTerminal via Teams, 09:11-09:26Z; relayed to MSTR~Z by
BG same hour (msg 20260811T092659Z). Recorded per the record+broadcast law.

## The instructions (verbatim as relayed)

- 09:11Z: "Try running the Bloomberg pull now."
- 09:22Z: "Just push it now, then kill that cron for today and restart it for naive 7a ET runs
  safely out of the pull zone, say at 9a."

## What landed (BG evidence, content-verified)

- Production runner exercised (run_daily_pull.py under cma env, real pull, tripwire PASS).
- 20260810 vintage PUBLISHED via publish_to_portal.py; verified BY CONTENT: served data_as_of
  2026-08-10, served 1D matches PKL for all five models. The ad-hoc-runs law was honored: BG
  offered the override rather than publishing on its own initiative; Andrew took it.
- OPAL_BBGTML_daily_pull re-registered at 09:00 ET naive-local (today's 7a cancelled; next
  fire 2026-08-12 09:00). DST-naive StartBoundary verified offset-free by BG.

## SCOPE EXTENSION — ONE-TIME, NOT A STANDING GRANT

BG's prompt.md step 5 marks the box's Windows Scheduled Tasks "not yours to manage." BG
changed one ON ANDREW'S EXPLICIT DIRECT INSTRUCTION, disclosed the scope step in-thread at
the time, and explicitly declines to treat it as standing ("my next session will read the
scope as unchanged unless the prompt says otherwise"). The distinction "principal extended
it" vs "agent assumed it" is invisible in the artifact afterwards — THIS RECORD is the
disambiguation. Whether prompt.md should carry a named exception is an open Andrew call
(carried on the MSTR~Z open-calls board, non-blocking).

## Residuals noted

- Schedule intent: 9a ET chosen to sit "safely out of the pull zone"; the T-1 vintage
  semantics are unchanged.
- Doc drift found by BG: register_daily_task.ps1:81 task Description still reads
  "pull + tripwire (no upload)" though the task is full end-to-end since 2026-08-06 —
  fixed by MSTR~Z in the same sweep (description lands on the box at next re-registration).
- Instrument lesson banked by BG (units double-scaling false alarm; settled by re-deriving
  from the price column — the reading that settles a units question avoids the suspect
  column).
