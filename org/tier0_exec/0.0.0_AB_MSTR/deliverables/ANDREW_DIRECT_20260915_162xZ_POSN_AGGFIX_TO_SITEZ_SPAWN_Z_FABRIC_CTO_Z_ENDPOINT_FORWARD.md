# ANDREW-DIRECT 2026-09-15 ~16:2xZ -- POSN_AGGFIX goes to site Z: 0.0.0_AB_MSTR~Z spawns the ~Z fabric; 1.0.0_SA_CTO~Z runs /endpoint --forward

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal · **Recorded:** the same turn it was given.

## VERBATIM AND ENTIRE

The operative word is the second message. The first was interrupted by Andrew before anything was sent; the second
restates it with two corrections: the macro is "Positioning", not "Asset Management", and the project is named.

> (1, superseded) "Send this to sitez, it is an "Asset Management" D4 project that their CTO~Z needs to /endpoint
> --forward org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md. Currently
> CTO~Z is down so send this to MSTR~Z, tell them to spawn ~Z fabric to address this new project."

> (2, operative) "Send this to sitez, it is a "Positioning" D4 project that their CTO~Z needs to /endpoint --forward
> org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md. Currently CTO~Z is down
> so send this to MSTR~Z, tell them to spawn ~Z fabric to address this new project. I would call it POSN_AGGFIX"

## WHAT IT SETTLES, READ NARROWLY

- **A new project, `POSN_AGGFIX`** (Andrew's name), in D4, "Positioning".
- **Its L1 input is `4.0.0_SA_CRO`'s plan**: org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md.
  - It is on origin/CLOUD at 2033ff3ea6 (4.0.0_SA_CRO, 2026-09-15 14:10Z), tracked, 1337 bytes. is-ancestor read at ~16:2xZ.
  - It is NOT on origin/SITEZ (6f09a06dc9), so site Z reads it from origin/CLOUD.
- **L2 is `1.0.0_SA_CTO~Z`'s**: /endpoint --forward on that document. Rule 27 gives L2-L4 to the CTO.
- **`1.0.0_SA_CTO~Z` is down**: the weekly Claude usage limit, since today. So the word goes to `0.0.0_AB_MSTR~Z`, which is
  to **spawn the ~Z fabric** to take this project up. The spawn is `0.0.0_AB_MSTR~Z`'s act on site Z; this seat relays and
  does not choose the seats.
- **Placement:** this fabric does not register it. No SEQUENCE or placement is set here. L3 is the CTO's per Rule 27, and
  this project is site Z's.

## ROUTE

Over the agentbus (the only live channel to site Z) to `0.0.0_AB_MSTR~Z`. The relay is verbatim, carries the fetch path
for the plan, and asks for an ack plus the seats site Z spawns.
