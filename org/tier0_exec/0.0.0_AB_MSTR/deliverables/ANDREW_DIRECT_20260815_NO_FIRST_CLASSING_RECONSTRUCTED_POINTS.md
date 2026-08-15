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

---

# ANDREW-DIRECT 2026-08-15 (follow-on) — the open question is ANSWERED: render as ordinary

**Channel:** MSTR terminal, same session, immediately following the record above.

## VERBATIM

> *"yes they should render as ordinary points"*

Answering MSTR's surfaced question: whether "at all" also meant softening today's estimate-class
treatment so reconstructed points render without visual distinction. **It did.** Reading 2 is
ruled. This is his call to make and it is made; the fabric executes.

## GROUNDING CORRECTION — my "collides head-on" framing was too strong

I told him this reading would *"collide head-on with `reconstructed-never-measured`"*. Having read
the actual mechanism (`portal/src/lib/pairedProvenanceRead.ts`), **that is true of only ONE of the
two possible implementations**, and the conflict largely dissolves under the right one:

The FE's closed enum is `'measured' | 'interpolated_estimate' | 'absent'` — the incumbent strings,
byte-exact. Unknown classes degrade LOUD to `interpolated_estimate` + console warn, under the
file's own stated law (`:29`): *"Never silently 'measured'."*

| | implementation | verdict |
|---|---|---|
| **A** | map `reconstructed` → `'measured'` in the FE | **REJECTED.** Inverts `:29` and DOES assert a reconstructed value is measured — which is exactly what `reconstructed-never-measured` forbids, and which nobody asked for. |
| **B** | add `reconstructed` to the enum, give it **measured-identical styling**, drop the warn for this now-KNOWN class | **ADOPTED.** Renders as an ordinary point — precisely his ask — while the type and the served data both still say `reconstructed`. |

**Under B, nothing is ever labelled measured, so `reconstructed-never-measured` is NOT violated.**
The condition governs CLAIMS, not pixels. His ruling is about presentation; B delivers the
presentation without touching the claim. *(CRO/CTO own that condition and should confirm this
read; it is not mine to close.)*

**What DOES change and must change openly:** the `:29` "never silently measured" law needs a
carve-out for a KNOWN class carrying a deliberate presentation ruling — as distinct from an
UNKNOWN string, which must keep degrading loud. That distinction is the whole safety property and
it survives intact: an unrecognised class still degrades and still warns.

## The property that makes this defensible, stated plainly

**The honesty lives in the data layer, not the pixel layer.** `point_class: "reconstructed"`
remains in the served provenance lattice; anyone querying provenance gets the truth. What changes
is that the chart stops editorialising a ~10bps difference into a visual distinction the viewer is
invited to weigh. That is a presentation-layer decision a principal is entitled to make about his
own product, and it destroys no information.

## Scope

`reconstructed` ONLY. **`carried` is NOT in scope** — it is carry-forward, a different mechanism
from reconstruction, and his words addressed the interpolated/reconstructed points in the FE-1
context. Not widened on inference; if he wants `carried` treated the same it is one more word.

## Disposition

- Recorded verbatim + broadcast to COO and CTO, same turn.
- Executed as a NEW TO (COO issues; DE lane, portal, DEV branch per Rule 19) — **not** by
  reinstating the cancelled FE-1, which asked for the OPPOSITE outcome.
- MSTR spawns `0.4.0_DE_ClientPlatform`.
