# ANDREW-DIRECT 2026-10-10 ~20:5xZ-21:0xZ -- site Z launch roster is three seats

Channel: the `1.0.0_SA_CTO~Z` terminal at site Z, three messages after the device crashed and restarted (boot 20:47Z).
Recorded by `1.0.0_SA_CTO~Z`.

## Verbatim

1. "This device crashed earlier and was unable to restart. I want you to reassess state based on what you can see here.
   I also do not want all these agents started at launch. The only ones that are actually necessary are
   0.0.0_AB_MSTR~Z, 0.0.3_BG_BBGTerminal, and you, 1.0.0_SA_CTO~Z."
2. "what is the actual logic of this startup? that it simply loads the agents that were online at some last marked
   state? that is actually an acceptable approach"
3. "We just need to make sure that state is correct. For example, when I left the office here the other day, I stopped
   loading CTO~O because we don't need to run two different CTOs by default on a single box. However, with this auto
   launcher loader setup, I notice it spawned a CTO~O, which makes me think its loading based off some state that is
   not the most recent"

## Act taken

- `C:\opal-elev\autolaunch-agents.ps1` (the device-local wrapper the elevated log-on task `OPAL_autolaunch_agents`
  runs) cut from 15 serials to `0.0.0_AB_MSTR~Z`, `0.0.3_BG_BBGTerminal`, `1.0.0_SA_CTO~Z`. Previous roster kept at
  `C:\opal-elev\autolaunch-agents.ps1.bak-20261010T2100Z`. Parse check: 0 errors.

## What the launcher actually does (answer to message 2)

It keeps no state. The wrapper holds a STATIC serial list, last rewritten 2026-10-09 ~06:3xZ. The repo engine
`.tools/autolaunch-agents.ps1` launches every listed serial that has no running `claude.exe`. Nothing reads which seats
were live at the last shutdown. `1.0.0_SA_CTO~O` was retired at ~07:4xZ the same day
(`ANDREW_DIRECT_20261009_074xZ_CTO_O_RETIRED_CTO_Z_LEADS_SITEZ_FABRIC.md`), an hour after the list was written, and
nothing carried that retirement into the list. That is why it launched.

## Scope

Site Z launch roster only. The 12 other seats already launched this boot are not covered by this order; stopping them
waits on Andrew's word.
