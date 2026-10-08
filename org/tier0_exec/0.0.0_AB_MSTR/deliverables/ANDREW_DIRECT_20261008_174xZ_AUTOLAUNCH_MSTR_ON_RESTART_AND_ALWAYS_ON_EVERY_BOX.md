# ANDREW_DIRECT 2026-10-08 ~17:4xZ -- auto-launch MSTR on restart, and "always on" (no sleep), on every box

**Channel:** laptop terminal, to 0.0.0_AB_MSTR. **Recorded by:** 0.0.0_AB_MSTR, same turn.

## Andrew's words, verbatim

> "Also i think we need to look into the auto-start process that is running on sitez currently, specifically, I
> really like how that device if it ever restarts autolaunches MSTR on it. The benefit behind this is if there are
> any unexpected crashes/updates/restarts, etc, that we are effectively always on. I also want to make sure that those
> boxes have the "always on" command running so they never sleep, and the dell box MSTR agents should make sure that
> that is the case."

## Placement (infrastructure; MSTR lane)

- The site-Z mechanism is documented in
  `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/CROSS_FABRIC_20260910_AUTORECOVERY/` (briefing + zip, e222f4e4ee):
  layer 1 auto-login (elevated; a standing posture change, Andrew's call per box), layer 2 a LOGON-triggered
  Scheduled Task running `ajb -Headless <serial>` (no elevation), layer 3 site-Z Bloomberg only.
- Layer 2 is versioned in the repo as `.tools/autolaunch-agents.ps1` + `.tools/autolaunch-task.ps1`, deriving the
  root from the script's own location (no device path), and installed by each box's MSTR for its own MSTR serial.
- "Always on" (never sleep): each Dell MSTR measures and sets its own box; site Z reports its existing command so
  every box runs the same one.
- Open for Andrew: layer 1 (auto-login) per box, without which a restart waits at the lock screen for a human log-on;
  and whether the laptop itself is set never to sleep on AC.
