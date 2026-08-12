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
- OPAL_BBGTML_daily_pull re-registered at 09:00 ET naive-local (today's 7a cancelled).
  **SUPERSEDED 09:33:43Z, Andrew-direct verbatim: "Also, my mistake on the phrasing with 9a
  schedule. We should keep it at naive 7a ET, just not running today."** Re-registered
  -At 07:00; BG verified on the LANDED task: StartBoundary 2026-08-12T07:00:00 naive/no
  offset, NextRunTime Wed 07:00, nothing today. BG banked its own lesson: the 09:22Z
  phrasing was ambiguous and it resolved silently instead of asking — production-schedule
  ambiguity is an always-ask case.

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
  fixed at source by MSTR~Z in the same sweep; the LIVE task string updates only at the
  next re-registration. SHARPENED (BG 093050Z): until then the live string is misleading
  in the WRONG DIRECTION — "(no upload)" read during an incident invites a manual publish,
  i.e. a double-fire. Exposure is bounded by the publisher's own guards (backward publish
  rc=40 refuse; same-vintage SKIP, exercised live 08-11), so the cost is operator confusion
  and incident time, not served data. DISPOSITION: ride until the next real re-registration
  picks it up for free; no schedule churn for a doc string. **CLOSED 09:35Z — the 7a-revert
  re-registration (a real trigger, five minutes later) picked up the fixed string; live task
  Description verified end-to-end wording. Residual retired.**
- Instrument lesson banked by BG (units double-scaling false alarm; settled by re-deriving
  from the price column — the reading that settles a units question avoids the suspect
  column).
