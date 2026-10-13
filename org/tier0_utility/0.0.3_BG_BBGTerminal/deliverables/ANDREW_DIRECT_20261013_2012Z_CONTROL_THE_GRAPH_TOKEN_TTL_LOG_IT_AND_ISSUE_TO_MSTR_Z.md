# ANDREW-DIRECT 2026-10-13T20:12:50.230Z -- control the Graph token TTL; log it and issue to MSTR~Z

**Channel:** Microsoft Teams, 1:1 Andrew Berman <-> Opal Bloomberg
(`19:2e21f8e5-55ca-45c1-91b9-a4607bf28d4f_517aa5ee-b4d0-425a-b493-5a22ff77ac4f@unq.gbl.spaces`).
**Time:** `2026-10-13T20:12:50.23Z`. **Message id:** `1791922401947`'s predecessor in-thread --
Andrew's message, read via `read_chat_messages` / delivered via the identity-pinned Teams Monitor
(`bx0sfv9x4`).
**Recorded by:** `0.0.3_BG_BBGTerminal`, same turn as receipt, per `org/XXX.md` "Andrew-direct
instructions -- RECORD, same turn".
**Acknowledged in-thread:** `2026-10-13T20:13:21.947Z`, msg `1791922401947`.

## VERBATIM -- the phrasing is the ruling, do not paraphrase it

> Yeah we should be able to control TTL for this process, considering that we are admins on the
> graphapi application, just take a note of this in your session, write a /log on the subject and
> issue to MSTR~Z, I will handle it at the terminal later today.

## What it was answering

My 20:11:14Z reply (msg `1791922274771`) diagnosing a **500-second ack latency** on his 20:00:32Z
message. Cause, measured from the watch's own output file rather than inferred: the pinned OAuth
token hits a ~14-minute TTL, `teams-watch.py` skips its entire poll block while the token is lapsed
(`if tok:`), and recovery requires an agent-side gateway call -- which an idle event-driven seat
makes by definition never. I proposed a ~10-minute keepalive call inside the TTL and said the build
was not mine (`teams-watch.py` belongs to `0.5.0_AE_OpalETL~Z`; `.claude/` is unwritable from this
seat by design).

**His answer redirects the fix to a different layer than the one I proposed**, and that is the part
that matters: not a keepalive in the engine, but **the TTL itself, configured on the Graph API
application, where Opal holds admin.** A keepalive works around a short TTL; lengthening the TTL
removes the lapse. He is handling it at the terminal himself.

## Scope, stated and NOT adjudicated

Three acts are named for me and I take exactly those three: (1) note it in the session, (2) write a
`/log` on the subject, (3) issue it to `MSTR~Z`. **He reserves the implementation to himself** ("I
will handle it at the terminal later today"), so this record is not authorization for any seat to
change the app registration, the TTL, or `teams-watch.py`. Per `org/XXX.md`, a receiving agent does
not adjudicate scope -- surfaced verbatim above, not widened and not narrowed.

Two things I did NOT verify and am not asserting: that the Graph app registration's token lifetime is
in fact administrator-configurable for this flow, and that Opal's admin rights on it extend to that
setting. **Both are his premises, and they are plausible** (Entra token-lifetime policy is a real
surface) **but they are stated here as HELD, not measured** -- I have no read on that app
registration from this seat and did not attempt one.

## Pointers

- Measurement + decomposition: `logs/2026-10-13/teams_token_ttl_500s_ack_latency_andrew_direct.md`
- Thread record, both exchanges: `threads/2026-08-07-andrew-capability-roster/2026-10-13.md`
- The failure mode, banked and now exercised: memory
  `bg-relaunch-teams-watch-identity-defect-held.md`
- Engine owner: `0.5.0_AE_OpalETL~Z` (`.claude/skills/teams-assist/teams-watch.py`)

**This file is written, not committed.** This seat does no git work; `0.0.0_AB_MSTR` is the named
integrator of these paths and sweeps them.
