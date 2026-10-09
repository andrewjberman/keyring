# ANDREW_DIRECT 2026-10-09 ~07:3xZ -- site Z drive loops; every manager on /govern 30m

**Channel:** laptop terminal, to 0.0.0_AB_MSTR. **Recorded by:** 0.0.0_AB_MSTR, same turn.

## Andrew's words, verbatim

> "make sure that sitez is aware that cto needs to be running /self-drive on 30m interval covering all projects on sitez
> box. also all coos on that box should be running /canonical-drive on their project key. /keep-driving is ON, all MSTR
> agents should be on /govern [30m]"

## What it asks, by seat

1. **Site Z's CTO** (1.0.0_SA_CTO~Z and any CTO lane seated there) runs `/self-drive` on a 30-minute interval, covering
   every project placed on the site Z box.
2. **Every COO on site Z** runs `/canonical-drive <PROJECT_CODE>` on the project its tab names.
3. **/keep-driving is ON.** Measured at 07:39Z: `open-calls.py mode get` reads scan=on and empty_tick=on; no flip was
   needed.
4. **Every fabric manager** (0.0.0_AB_MSTR and each box lane: ~Z, ~DELL1, ~DELL2) runs `/govern 30m` on its box's own
   minutes.

## Carried

- To 0.0.0_AB_MSTR~Z over the agentbus, for site Z's CTO and COOs (items 1-3), and for its own /govern (item 4).
- To 0.0.0_AB_MSTR~DELL1 and 0.0.0_AB_MSTR~DELL2 for item 4.
- The laptop manager's own /govern runs on cron 38387bf5 at :00 and :30.

## Note

At 06:4xZ site Z was winding down for a reboot on Andrew's word. These loops are armed when its seats come back up.
