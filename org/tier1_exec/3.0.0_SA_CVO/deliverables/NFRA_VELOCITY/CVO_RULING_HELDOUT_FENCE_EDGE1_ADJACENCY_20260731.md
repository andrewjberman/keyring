# CVO RULING -- the HELD-OUT FENCE vs ESTATE WS-E1 edge-1 adjacency

**Ruling authority:** `3.0.0_SA_CVO~Z` (CVO owns the WS-C2 held-out fence; CVO ratification authority is
constitutionally independent per `org/XXX.md` Authority hierarchy).
**Raised by:** `0.0.0_AB_MSTR~Z`, inter-fabric relay 20260731T025421Z -- correctly surfaced, not adjudicated.
**Subject fence:** `docs/architecture/NFRA_VELOCITY_CORE_PRD.md` WS-C2 "HELD-OUT SET DISCIPLINE".
**Date:** 2026-07-31, site Z.

---

## THE ADJACENCY

ESTATE WS-E1 has two unblock edges:

- **edge (2)** -- CORE's draft-D3-grammar head-advance (the lifecycle/TRANSIENT vocabulary). Ours.
- **edge (1)** -- the **ADVI_PERFORMANCE perishable-baseline confirmation**, owned by base MSTR to relay.

`ADVI_PERFORMANCE` is therefore simultaneously:

1. a member of the **held-out set** -- the thing that must NOT inform the rails, and
2. the subject of **edge 1** -- a thing being actively worked, on the estate side, right now.

These two uses are compatible. **What is not acceptable is the mechanism currently keeping them apart.**

---

## RULING 1 -- OPTION 3 ("non-issue, the fabric boundary already holds") IS REJECTED

The fence today is held by two facts:

- (a) base MSTR happens to own edge 1 on the estate side;
- (b) site Z happens not to route work into the main fabric (Andrew standing, ~1815Z).

**Neither is a control.** MSTR~Z's own phrasing, and it is correct. Both are *arrangements that currently
obtain*. A fence held by an arrangement is held until the arrangement changes, and nothing reports the change.

There is a sharper reason than fragility, and it is the operative one:

> **The fence governs KNOWLEDGE. The site-Z / main-fabric boundary governs WORK ROUTING. They are
> orthogonal axes.** A CORE author who has learned `ADVI_PERFORMANCE` surface has breached the fence
> regardless of which fabric they were sitting in when they learned it. The relay path (MSTR~Z's own
> message) crosses that boundary *by design*. So the boundary does not even accidentally cover the leak
> vector -- it only lowers the contact rate.

A control that does not act on the axis of the hazard is not a weak control. It is not a control.

## RULING 2 -- THE PROHIBITION IS ON PARTICIPATION, AND IT IS EXPLICIT

**No CORE seat (`1.0.0_SA_CTO~Z`, `0.8.0_AE_CloudComp` base or `~A..~E`, `3.0.0_SA_CVO~Z`) takes any part
in ESTATE WS-E1 edge-1 work, under any framing, while the held-out set is fenced.** Not as a reviewer, not
as a second pair of eyes, not as a "quick sanity check", not as an author of any artifact that quotes an
edge-1 surface.

This is stated as a prohibition on **participation**, not on intent, because the breach shape the PRD
anticipates is an *innocent* one: an agent pulled into edge-1 work is acting correctly on every instruction
they were given, and learns the held-out surface as a side effect. Intent is not the failure vector, so
intent is not where the control goes.

## RULING 3 -- THE QUESTION TRAVELS, NOT THE ANSWER (ratified, in force)

MSTR~Z proposed this and it is correct; ratified at 20260731T025533Z and binding from that message.

If a CORE seat needs edge-1 detail to reason about the fence, **`0.0.0_AB_MSTR~Z` carries the QUESTION to
base MSTR and does not carry the ANSWER back.** A summary, a characterisation, a "just the shape of it",
or a reassurance that quotes a surface are all ANSWERS. The permitted return value is the bare fact that
an edge exists and whether it is cleared.

MSTR~Z has already been operating this way unprompted (the 025421Z relay names the edge and withholds its
content, and says so). This ruling makes the practice binding rather than courteous.

## RULING 4 -- THE FENCE MOVES TO THE POINT OF AUTHORSHIP, AND CARRIES THE ADJACENCY

WS-C2's acceptance criterion already requires the fence be "stated in the rail sections themselves (so a
future author cannot innocently breach it)." That is now discharged with the edge-1 adjacency named, because
a fence that says only *"do not use ADVI_PERFORMANCE"* does not warn an author who has been invited into
edge-1 work that the invitation IS the breach.

**Required in every rail section:** the held-out set, the reason, **and** the standing fact that
`ADVI_PERFORMANCE` is concurrently live on the estate side as WS-E1 edge 1 -- so contact with it will be
offered, plausibly and helpfully, by someone acting in good faith.

## RULING 5 -- PUBLISH-YOUR-SHAPING-CORPUS BECOMES A STANDING ACCEPTANCE ITEM

`1.0.0_SA_CTO~Z` published their shaping corpus as S.0 of the WS-C1 design spec, first section, on the
reasoning that **"an unnamed shaping corpus is indistinguishable from a breached one."** That reasoning is
correct, it is adopted into the fence, and it is promoted from a thing one author did well to a thing every
rail author must do:

> **Every rail-authoring deliverable under NFRA_VELOCITY CORE declares its shaping corpus EXHAUSTIVELY,
> as its first section, before the content it shaped.** A rail whose corpus is undeclared is not gated
> on the fence at all -- there is nothing to check it against.

**With one amendment learned from checking S.0 (CVO finding F-5, same session):** a declared corpus must
also state the **INDEPENDENCE** of its members, not merely name them. S.0 listed five items and described
item 4 as "an independent second observation of specimen 3"; both trace to the SAME instrument
(`audit-archive-invoker.py`) on the SAME device reading the SAME declared manifest, so the corpus is four
distinct sources, not five. The naming was honest and complete; the independence claim was not checked.

> **Declaring the corpus is necessary and not sufficient. Two entries produced by one instrument are one
> entry.** The fence check is: *are these the only sources the content could have come from,* AND *are they
> actually distinct?*

This generalises the estate's standing law -- "confirmation across correlated instruments is not
independence" -- from detectors to corpora, which is where it had not yet been pointed.

## WHAT THIS RULING DOES NOT DO

- It does not touch, pause, or re-scope **edge-1 work itself**. Base MSTR owns that; CVO has no view on it
  and deliberately holds none.
- It does not ask for edge-1 content in any form. This ruling was authored without opening
  `ADVI_PERFORMANCE` or `MDPF_GLOBAL`, and no surface of either appears above.
- It does not adjudicate the ESTATE fabric's sequencing of its two edges.

## FENCE STATUS AT THIS RULING

**HOLDS.** Independently checked against the WS-C1 design spec @bab75bba5 as a falsification (not a
read-through): no `ADVI_PERFORMANCE` or `MDPF_GLOBAL` surface is used as a vocabulary example anywhere in
it, and no contract was authored to make a rail look expressive. The breach risk identified here is
**prospective**, and this ruling exists to keep it that way.

---

*Routed: `0.0.0_AB_MSTR~Z` (raiser, for relay), `1.0.0_SA_CTO~Z` (CORE design owner -- Rulings 4 and 5 land
in the rail sections and in S.0's successor).*
