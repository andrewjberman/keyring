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

---

# AMENDMENT 1 -- the M9 capture contradiction (2026-07-31, ~0420Z)

**Raised by:** `0.0.0_AB_MSTR~Z` 041708Z, sharpened from base MSTR. **Status:** ACUTE -- the metric is
perishable, its trigger is a normal work event, and until this ruling there was no permitted capturer.

## The contradiction as presented

NFRA_VELOCITY_ESTATE P1 BASELINE s3 assigns M9's capture to `~Z` "at ADVI_PERFORMANCE's decomposition."
Ruling 1 above holds that the fence governs KNOWLEDGE, so a `~Z` rail author who learns ADVI's surface
has breached it. **Capturing a build-cost baseline appears to require touching the surface. So the
assignment names the one fabric whose rail authors must not learn it.**

Four shapes were offered: (a) a non-rail-authoring `~Z` seat, requiring the fence to bind by SEAT;
(b) main-side capture, which contradicts s3 and the standing no-cross-routing order; (c) Andrew
reassigns; (d) something else.

## RULING A1.1 -- IT IS (d), AND THE CONTRADICTION IS AN EQUIVOCATION ON "TOUCHING THE SURFACE"

**A BUILD-COST BASELINE AND A DOMAIN SURFACE ARE DIFFERENT OBJECTS, AND ONLY THE SECOND IS FENCED.**

M9 measures what it COSTS to build ADVI_PERFORMANCE's decomposition before the rails exist -- elapsed
time, step count, rework cycles, human touches. The fence forbids something else entirely: *"no surface
of either used as a vocabulary example, no contract authored to make a rail look expressive."* It
protects the INDEPENDENCE OF A FUTURE TEST -- that *"can the rails type a project nobody shaped them
against?"* stays answerable rather than assumed.

**A number of hours cannot shape a type system.** Knowing a decomposition took 14 hours across 3 rework
cycles tells a rail author nothing about ADVI's grain, paths, contracts, or vocabulary -- and it is
precisely grain/path/contract/vocabulary that the held-out test is for. The premise *"capturing the
baseline requires touching the surface"* conflates **being present at the work** with **carrying the
work's semantic content**. Only the latter is fenced.

So the contradiction dissolves without deciding fabric-vs-seat, without contradicting s3, and without
Andrew reassigning. **The s3 assignment stands. `~Z` captures it.**

## RULING A1.2 -- TWO CONTROLS, BOTH REQUIRED (neither is sufficient alone)

- **CONTROL 1 -- ON THE ARTIFACT.** The M9 capture is a COST MEASUREMENT against a DECLARED SCHEMA
  (elapsed time, step/rework counts, touches, dates). It carries **NO** ADVI identifiers, field names,
  path structures, grains, partition schemes, or contract content. Free-text notes are excluded, not
  merely discouraged -- free text is where surface leaks.
- **CONTROL 2 -- ON THE CAPTURER.** The capturing seat does not author, review, or ratify WS-C1/C2 rail
  vocabulary while the fence stands. **Declared at assignment, never inferred afterward.**

**Why both, when either looks sufficient:** Control 1 stops the ARTIFACT leaking; Control 2 stops the
AGENT leaking what it incidentally saw while timing the work. A schema-clean artifact written by a rail
author still puts the surface in a rail author's head; a non-rail-author writing free-text notes still
puts the surface in a file the rails are built beside. **Each closes exactly the hole the other leaves
open, which is the test for defense in depth rather than belt-and-braces.**

## RULING A1.3 -- THE FENCE BINDS ON THE CAUSAL PATH INTO RAIL AUTHORSHIP. NOT FABRIC. NOT SEAT.

Asked directly whether the fence is a property of the FABRIC or of the SEAT: **neither.**

Ruling 1 already retired FABRIC. **SEAT is closer and still wrong** -- it is a PROXY, and a leaky one:
seats on this device share an inbox fabric, a working tree, and a relay, and tonight alone produced a
dual-seat collision and a context-clear that made a seat unrecognisable to itself. A proxy that has
failed twice in one session is not a unit of account.

**The fence binds on the CAUSAL PATH BY WHICH KNOWLEDGE COULD REACH RAIL AUTHORSHIP.** Control 2 is
stated seat-wise because a seat is the cheapest *administrable* approximation of that path -- but when
the proxy and the principle disagree, **the principle binds.**

**Corollary, and it is the reason A1.1 is safe:** the fence must be verifiable WITHOUT READING THE
FENCED SURFACE. Control 1 delivers exactly that -- CVO checks the captured artifact against a schema,
never against ADVI. **A fence whose enforcement requires the enforcer to breach it is not a fence**, and
any future control on this set must satisfy that same property.

## What this does and does not authorise

- **The protective HOLD at the arch-gates may LIFT** once the capture is specified per Controls 1+2. It
  was the right precaution and it is now discharged by specification rather than by waiting. Given
  perishability, holding longer costs the metric.
- **CVO does NOT assign the seat.** I rule on what the fence permits; WHO captures is CTO/Andrew's. The
  assignment must carry the Control-2 declaration explicitly.
- **No ADVI substance was requested or received in making this ruling**, and none appears in it. It was
  authored without opening either held-out project. Ruling 3 held throughout: the question travelled,
  the answer did not.
- **If the capture as designed CANNOT be schema-constrained** -- if someone shows M9 genuinely requires
  domain content -- then A1.1's premise fails and this returns to me. That is the falsifier, stated so
  this ruling can fail rather than merely be agreed with.

---

# AMENDMENT 2 -- does the fence bar the CLASSIFYING READ? (2026-07-31 ~0630Z)

**Raised by:** base CVO via `0.0.0_AB_MSTR~Z` 062729Z, explicitly deferred to this seat.
**Status:** ACUTE -- `~D` held a withhold on (d)-attribution of the M9 baseline, a perishable metric.

## The question as posed

*Does the held-out fence bar ONLY the WRITTEN ARTIFACT that carries surface, or ALSO the CLASSIFYING
READ that (d)-attribution requires?*

## RULING A2.1 -- THE DICHOTOMY IS FALSE. THE FENCE BARS **CONTACT**, IN ANY MEDIUM.

Ruling 1 settled that the fence governs **KNOWLEDGE**. A read is a knowledge-acquisition act, so a read
breaches exactly as a write does. **The written artifact was never the fence's OBJECT -- it was its most
TRACTABLE CONTROL POINT.** Control 1 constrains the artifact because an artifact is checkable; it does
not follow that the artifact is the protected thing.

MSTR~Z identified the carrier: free text was excluded because *"free text is where surface leaks"* --
**a mechanism about CONTACT, not about WRITING.** It extends. Ruling "artifact only" would license an
agent to tour the held-out surface at will provided they wrote nothing down -- **the fence defeated
while formally intact.**

## RULING A2.2 -- THE DISCRIMINATOR IS *WHOSE SURFACE*

> **A classifying read of the REFERENCE CLASS is PERMITTED. A classifying read of `ADVI_PERFORMANCE`
> or `MDPF_GLOBAL` is BARRED.**

The fence is not a prohibition on reading prose; it is a prohibition on contacting two named projects'
surface. The reference class is unfenced, so the fence is not engaged.

A seat's own fence-clean **self-attestation is necessary and not sufficient** (Ruling 5's amendment: a
corpus must state its members' INDEPENDENCE, not merely name them). **The clearance rests on A2.2, not
on the attestation.**

## RULING A2.3 -- THE MECHANICAL TEST (A1's corollary, operationalised for ACTS)

> **If verifying the RESULT would require the verifier to make the fenced read, the read is BARRED.
> If the result stays checkable by someone who has not made it, the read is PERMITTED.**

Reference-class read -> a verifier re-reads an unfenced class -> **SATISFIED**. ADVI/MDPF read ->
verification requires the verifier to breach -> **VIOLATED**, an independent bar rather than a
restatement. **The two tests agree**, and A1's corollary survives transfer from artifacts to acts:
*a fence must be verifiable without reading the fenced surface*, whatever the medium. This is a
standing self-test; it does not need CVO in the loop per instance.

## Conditions -- DECLARED, never inferred

- **C-1.** The capturing seat DECLARES in the source-declaration that the (d)-attribution read touched
  **only the reference class**, and NAMES that class. Not "fence-clean" in general -- *this read, that
  class.* If false, the clearance is **void ab initio** and the artifact is quarantined, not corrected.
- **C-2.** Amendment 1's Control 2 continues to bind (no WS-C1/C2 rail vocabulary while fenced).
- Control 1 (schema-constrained artifact, free text EXCLUDED) unchanged.

**DISPOSITION: (d)-attribution CLEARED to proceed under C-1 + C-2.**

## Falsifier

**If (d)-attribution cannot be performed against the reference class alone -- if it genuinely requires
reading ADVI/MDPF prose -- then A2.2 does not clear it, C-1 cannot truthfully be declared, and it
returns to CVO.** That is a finding to report, never a step to route around.

*Authored without opening either held-out project; no surface of either appears above. Ruling 3 held
throughout -- the question travelled, the answer did not.*
