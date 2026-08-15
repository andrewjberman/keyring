# ANDREW-DIRECT 2026-08-15 — do NOT first-class the reconstructed/interpolated points

**Channel:** MSTR terminal, 2026-08-15 (~0350Z / ~11:50 PM ET 08-14), in response to MSTR's
explanation of TO `MDPF_EVR.FE-1` and a recommendation to date it to the 08-16 CLEANUP close.

## VERBATIM

> *"i dont want to draw attention to the interpolated points at all, no one cares about that, its
> more problematic to open up the can of worms and seed doubt rather than just another data point
> that is probably within 10bps anyway on a random day no one cares about"*

## What it rules

**`MDPF_EVR.FE-1` is CANCELLED** — the FE first-classing of `point_class: "reconstructed"`
(closed-enum extension + legend entry + distinct styling) is not wanted and is not to be built.
Status `cancelled`, citing this ruling, per the `org/XXX.md` terminal-status vocabulary (the need
went away by ruling; a terminal status without its pointer is rot with a tidier label).

**The reasoning is his and it is the load-bearing half, not the verdict.** He is not saying the
work is low priority — he is saying the deliverable is *net-negative*: a visual treatment that
singles out 7 reconstructed points among 438 measured ones **seeds doubt disproportionate to the
magnitude** (his estimate: within ~10bps, on a day nobody is looking at). Prominence is not a free
good. Making provenance more visible is a real cost when the underlying delta is immaterial.

## Scope — stated narrowly, because the temptation is to widen it

**This ruling addresses the FRONT-END PRESENTATION only.** It does NOT touch, and must not be read
as touching:
- the EVR emitter, its outputs, or the reconstruction itself (his 2026-08-14 "yes to both" scope +
  serve ruling stands, record `@e4251a4567`);
- the SERVER-SIDE provenance lattice — `point_class` remains in the data, correctly labelled;
- the ratified EVR spec honesty conditions, **including `reconstructed-never-measured`** (CRO's
  set, carried 2026-08-14: body labels, calibrate/validate split, 136bp gate-FAIL-not-relax).

## The one open question MSTR surfaced rather than adjudicated

Today the FE renders `reconstructed` (and `carried`) as **estimate-class with a console warn** —
the closed-enum loud-degrade path in `portal/src/lib/pairedProvenanceRead.ts`. That is *already* a
visible distinction from a measured point. So his *"at all"* admits two readings:

1. **CANCEL-ONLY (assumed, and what is being executed):** stop the first-classing; today's
   estimate-class rendering stays as-is. Nothing is built, nothing is changed.
2. **GO FURTHER:** soften today's treatment so reconstructed points render as ordinary.

**Reading 2 is NOT being implemented on inference**, and the reason is specific rather than
procedural: rendering reconstructed data indistinguishably from measured data would collide with
the ratified **`reconstructed-never-measured`** honesty condition. That is a genuine conflict
between two of his own positions, and adjudicating it belongs to him, not to the fabric
(surface-do-not-adjudicate). Surfaced to him at the terminal the same turn; **no work is pending
on the answer** — cancel-only is complete in itself.

## Actions taken

- Recorded verbatim + broadcast to COO and CTO, same turn (record+broadcast law).
- `MDPF_EVR.FE-1` → `cancelled` by its ISSUER (COO), citing this record.
- MSTR's carried "DE FE-1 spawn-or-defer-date" item is **DISCHARGED** — no DE spawn, no defer
  date, nothing hanging. It does not become an 08-16 item.
