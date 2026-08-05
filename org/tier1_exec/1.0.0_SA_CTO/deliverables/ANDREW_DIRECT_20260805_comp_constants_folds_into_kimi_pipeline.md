# ANDREW-DIRECT — comp-constants folds into the daily Kimi pipeline

**Recorded:** 2026-08-05, CTO base terminal, immediately on receipt (record+broadcast law).
**Trigger:** the `0.4.0_DS_ClientPlatform` comp-constants surface brief @b3e9a5368, which he
requested and had delivered to this seat.

## VERBATIM

> "I like the idea of comp-constants, I would just fold it into the daily kimi pipeline, essentially
> using that pipeline as a mechanism to update all key semantic/hand-drawn surfaces."

## Scope, RECORDED not adjudicated

Three things are unambiguous on the face of it: **(1)** comp-constants is **KEPT** — he likes the
idea, so this is not a removal ruling and the brief's own position (the detection is load-bearing) is
preserved; **(2)** the **daily Kimi pipeline is the update MECHANISM**; **(3)** the scope is **not
just comp-constants** — *"all key semantic/hand-drawn surfaces."* The enumeration of that class is
**not stated** and is **not invented here.**

## Why this answers the actual defect — the fit is exact

The brief's core finding was that comp-constants **cannot distinguish a RATIFIED divergence from
DRIFT**, so it blocked the commit implementing his own rep-10 ruling. Its own BL-1 header named that
exact limitation two weeks ago and marked the fix "(not built)."

**The Kimi loop is already a ratification mechanism with him in it** — pipeline SUGGESTS, Andrew
RATIFIES, CVO LANDS. So his instruction routes the question the gate cannot answer (*is this
divergence ratified?*) to the loop that structurally can. That is a better fit than any of the five
options the brief listed, and none of them proposed it.

**It also dissolves the lane deadlock as a side effect** — the brief's structural finding was that
DS must change constants but is refused on the config lane, making every change a two-agent
transaction. Under this design **DS never updates the canonical at all**: the pipeline proposes, he
ratifies, CVO lands. The deadlock stops existing rather than being adjudicated.

## THE ONE CONSEQUENCE THAT NEEDS HIS EYE — it changes what the gate IS

**A daily ratification cycle cannot service a synchronous commit gate.** comp-constants blocks
in-process inside `commit-gate.sh` on every `.py` commit. If the canonical only moves through a
9a-ET loop, then a seat implementing a ratified change at 14:00Z is blocked until the next morning —
a ~19h stall on correct work, which is the same failure the brief documents, slowed down.

So the fold implies one of two shapes, and **it is a real fork, not a detail**:

| | |
|---|---|
| **(A) Gate becomes a DETECTOR** | It stops blocking on divergence and instead FEEDS the daily loop. Detection preserved, blocking dropped. |
| **(B) Gate keeps blocking + a same-day path** | Divergence still blocks, but a ratified change can clear it inside the working session rather than waiting for the loop. |

**(A) is the honest reading of "fold it into the pipeline"** and is the cheaper build. **(B) preserves
the stop-the-line property** that caught DS's genuinely incomplete fix today — the one where the
roster is ALIASED across `INFLECTION_REP_IDS`, `INFLECTION_EXTENDED` and the `PARTNER_REP_IDS` dict,
and a name-keyed search missed two of three. **Under (A) that fix would have landed incomplete and
been caught the next morning, after the commit.**

Not adjudicated here. Surfaced because the choice determines whether "stop the line" survives.

## THE RECURSION, and it is not a quibble

*"All key semantic/hand-drawn surfaces"* requires a list of hand-drawn surfaces —
**and that list is itself a hand-drawn surface.** Enumerate it by hand and the class reproduces one
level up: the register goes stale silently, in the direction that reads clean, exactly like the 34
constants under it.

Per `docs/doctrine/DERIVED_UNIVERSE.md` (landed today), the register must be **derived** — e.g. every
surface carrying a declared `canonical:`/`derived-from:` marker — **and assert on changes to the
derived set**, not enumerated in a config someone maintains.

## Constraints that ride this, unchanged

- **Detection is load-bearing and must survive** — including the aliasing case. The brief argued its
  own opposing side on this and it is the reason the brief is trustworthy.
- **Not an alarm.** A gate-in-flow redesign; the standing notification moratorium does not bite, and
  nothing here authorises building one.
- **Coupling to price:** comp-constants would depend on the Kimi pipeline's health. That pipeline had
  its **first scheduled fire today** (13:04:53Z). Making a live blocking surface depend on a
  one-day-old producer is a real dependency, and its failure mode needs stating before the fold, not
  after.
- **~30 of 34 constants are unassessed** (brief §8). Some may have no upstream authority to point at,
  so "derivation-backed canonical" may not be reachable for all of them. Unknown, not assumed.

## Routing

`1.0.0_SA_CTO~B` (Kimi pipeline owner) · `3.0.0_SA_CVO` (owns the daily loop; lands ratified semantic
changes) · `0.4.0_DS_ClientPlatform` (brief author, gated surface) · `2.0.0_SA_COO` (decomposition) ·
CC `0.0.0_AB_MSTR`.
