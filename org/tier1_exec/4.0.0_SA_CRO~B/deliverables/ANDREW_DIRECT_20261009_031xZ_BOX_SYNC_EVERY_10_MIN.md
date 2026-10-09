# ANDREW_DIRECT 2026-10-09 ~03:1xZ -- box-sync every 10 minutes, the integrator first in each cycle

**Channel:** laptop terminal, in the 4.0.0_SA_CRO~B session. **Recorded by:** 4.0.0_SA_CRO~B, same turn.

## Andrew's words, verbatim

> "Ok how do you suggest we handle it?"

(answering the measured lag: a box's work reaches another box in ~25 minutes typical, ~55 worst, through three hops on 30-minute
clocks -- the box pushes its branch at its slot, the laptop folds every box into CLOUD at :00/:30, the other box takes CLOUD at
its slot)

> "Sure I lik eit"

## The recommendation he approved

Same three hops every 10 minutes, ordered: laptop integrates (then its own box pass) at :00/:10/:20..., site Z at :02/:12...,
dell1 at :04/:14..., dell2 at :06/:16.... Worst case under ~20 minutes, usually under 10. Integrate never touches a working
tree; a box pass fast-forwards and refuses rather than overwrite a seat's uncommitted edit. Not taken: several CLOUD writers
(law-locked single writer, push races) or a box-to-box mesh (pairwise conflicts). The `/govern` ticks stay 30 minutes on their
own minutes and also pull (record `ANDREW_DIRECT_20261009_030xZ_GOVERN_TICK_RUNS_BOX_SYNC.md`).

Change: `.tools/box-sync-schedule.ps1` slot table and trigger (`$Every = 10`); each box's MSTR re-runs `-Install`.
