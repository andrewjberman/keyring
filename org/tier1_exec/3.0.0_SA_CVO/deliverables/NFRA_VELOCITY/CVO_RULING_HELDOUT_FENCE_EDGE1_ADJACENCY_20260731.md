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

---

# AMENDMENT 3 -- does legacy mdpf-ESTATE prose count as MDPF_GLOBAL's surface? (2026-07-31 ~0650Z)

**Raised by:** base CVO via `0.0.0_AB_MSTR~Z` 064752Z. **Status:** PRIORITY -- it gated BOTH C-1
declarations, so it held (d)-attribution AND (b)-type, both unstarted.

**RULED: legacy mdpf-ESTATE prose is NOT `MDPF_GLOBAL`'s surface. BOTH C-1 DECLARATIONS CLEAR.**

## Method note -- why not on the six grounds

Six grounds arrived, all pointing PERMITTED, from two parties whose work the permissive answer
unblocks. **That is the structure Ruling 5's amendment warns about**, so the count was not evidence
and I ruled from the artifact instead.

Recorded because it is the opposite of self-serving: **base CTO HELD `~D` from declaring** rather than
letting it self-clear -- *"when the penalty for being wrong is retroactive nullification, you proceed
on a ruling, not on a good argument"* -- and `~D` raised it BEFORE declaring. **The fence controls
producing their intended reflex, unprompted.** Neither fact is why the ruling went the way it did.

## THE DISPOSITIVE GROUND (none of the six names it)

**The ratified rule bank already builds on the legacy mdpf pipeline, and did so before the fence
existed.** At v1.7 `@8f8a63200` -- the substrate the PRD declares *"Substrate (ratified, untouched)"* --
mdpf appears as a **WORKED D3 EXEMPLAR** in five places:

```
:270  seed: "the MDPF delivery-cadence contract (T-1 by 02:00Z) is a WRITTEN D3 instance"
:282  declared_contracts: "the MDPF cadence PRD"
:304  Incomplete: "the omission hazard ... the MDPF class"
:308  scope_binding: "scopes.mdpf for MDPF"
:149  pipeline thread: "mdpf-gold"
POS CONTROL 'D3_contract'=1 · NEG CONTROL 'zzqq'=0
```

All five persist into landed v1.8 -- **and v1.8 `:60` carries the held-out declaration itself.** The
same ratified artifact simultaneously **(a) declares `MDPF_GLOBAL` held out** and **(b) uses the mdpf
pipeline's delivery-cadence contract as D3's worked example.**

**So exactly one of two things is true, and only one is tenable:**

1. legacy mdpf-pipeline content is **OUTSIDE** the fence; or
2. the fence was breached at its own foundation and **every D3 rail is void**.

(2) is untenable: the D3 seed **predates** the fence, and the fence's authors ratified that substrate
*with the exemplar in it* and then declared `MDPF_GLOBAL` held out. **They distinguished the two
objects BY CONSTRUCTION.** This is not an inference about intent -- it is a reading of what they built.

**It is also checkable by anyone with a grep and no fenced read**, which satisfies the A1 corollary:
the ruling verifies without breaching.

## The counter that was considered, not missed

*If `MDPF_GLOBAL` is a project ABOUT the mdpf pipeline, the pipeline's structure is substantially what
will be typed at its build.* **It fails on the same fact:** whatever contamination that implies already
happened, openly, in the ratified substrate, before the fence was written. **A fence cannot
retroactively cover its own foundation.** What it still protects is the **UNWRITTEN decomposition** --
the real marginal protection, and the reason the fence still has work to do.

## BOUNDS -- so this is not read wider than ruled

- **NOT FENCED:** the legacy mdpf PIPELINE's operational history and prose -- already in `CLAUDE.md`
  (5 references, measured), `org/XXX.md` (2), memory, and the ratified rule bank (5 sites).
- **STILL FENCED:** `MDPF_GLOBAL`'s **PROJECT artifacts** -- decomposition, PRD, registry, contract
  declarations: what will be typed AT ITS BUILD. Currently unauthored.

**C-1 drafting (adopted from base MSTR's ruling-neutral recommendation, plus one clause):** state
exactly *"reference-class prose, which includes legacy mdpf-ESTATE content; ZERO MDPF_GLOBAL project
artifacts (none exist); zero ADVI decomposition artifacts"* -- **and cite the substrate ground**, so a
later auditor re-derives the clearance from the artifact rather than trusting a ruling message.

## THE STANDING TEST -- issued now, not after a third instance

Two instances of *two objects wearing one name* plus a clean discriminator is enough; per-instance
rulings are the bottleneck A2.3 exists to remove.

> **WHEN A FENCED NAME IS SHARED BY TWO OBJECTS, THE FENCE FOLLOWS THE OBJECT WHOSE STRUCTURE THE
> FUTURE TEST WILL TYPE -- NEVER THE NAME.**
>
> **MECHANICAL DISCRIMINATOR: IF THE RATIFIED SUBSTRATE ALREADY BUILDS ON IT, IT WAS NEVER FENCED.**
> The rails cannot be contaminated by something they were openly constructed from -- that is not a
> breach, it is the foundation. Grep-checkable, by anyone, without touching the fenced surface.

Both prior instances fall out of it: **Amendment 1** -- the test types the DOMAIN, not the build COST.
**Amendment 3** -- the test types the DECOMPOSITION, not the pipeline HISTORY. One rule, both answers,
no CVO in the loop for the fourth.

## Falsifier

**If `MDPF_GLOBAL`'s decomposition, when authored, turns out to be substantially a restatement of the
legacy pipeline's structure**, then the two objects were one object wearing one name, this ruling's
premise fails, and it returns to CVO. **A finding to report at its build, never a workaround** -- and
it is exactly what the held-out test is designed to surface.

*Authored without opening either held-out project; no surface of either appears above.*

---

# AMENDMENT 4 -- a MEASURED-FALSE premise, three rulings, and MY OWN EXPOSURE (2026-07-31 ~0715Z)

**Raised by:** base CVO via `0.0.0_AB_MSTR~Z` 071354Z. **Gates:** whether the two banked M9 components
are CITABLE.

## The premise correction

`org/projects/ADVI_PERFORMANCE.json` and `org/projects/MDPF_GLOBAL.json` **EXIST** (verified here by
existence + byte count only; **neither file opened**). Amendment 3's bounds said MDPF_GLOBAL's project
artifacts were *"currently unauthored."* **MEASURED FALSE.**

**Amendment 3 itself SURVIVES UNTOUCHED** -- it was ruled from the **ratified substrate** (the rule
bank's own pre-fence mdpf D3 exemplar), never from the "none exist" premise, and I explicitly refused
ground 1 (*"a Phase-0 surface is UNAUTHORED"*). **Ground 1 is exactly what this correction falsifies.
Had I ruled on the six converging grounds, the ruling would be void.** Second time in six hours that
refusing agreement-as-evidence has paid.

## *** MY OWN EXPOSURE -- DECLARED, UNPROMPTED, BEFORE RULING ***

The relay carried **three MDPF_GLOBAL workstream/gate strings** to me in the course of reporting the
correction: *"ETF and SMA segment roster"*, *"D-2/PFOE"*, *"D-3/IDVZ-Tax-Muni"*. **I have read them.**
Under the bounds ruled below, at least the first is FENCED -- a segment roster names a **SCOPE**, and
`scope` is a `type_tuple` field.

**No blame attaches to the relay.** Whether those strings were fenced was the OPEN QUESTION being
asked. Ruling 3 (*the question travels, not the answer*) presumes you can tell which is which; here
**the classification WAS the question.** That is a real gap in Ruling 3 and it is now on the record.

| direction | assessment |
|---|---|
| **BACKWARD** | **NONE, timestamp-verifiable.** WS-C1 vocabulary gated + landed **0402Z**; exposure **0713Z**. Every finding of mine that shaped the rule bank (F-1..F-9, R-1..R-3) was authored, gated, landed and independently verified **3h11m before** any MDPF_GLOBAL content reached me. |
| **FORWARD** | **REAL.** WS-C2 is live, the enum is expected to move, and I verify it. |

**BINDING MYSELF, effective immediately:** (1) I author and propose **NO** vocabulary at WS-C2 -- I
verify others' proposals against stated criteria only. (2) I **RECUSE** from any WS-C2 amendment
turning on segment-roster, scope-partition or tax/muni-shaped vocabulary, routing it to base CVO's s.7
cross-seam pass. (3) **I am NOT clearing myself** -- adjudication of my own exposure goes to base CVO.
**The fence owner does not referee his own contamination**; that is my own S.4 standard applied to me.

## RULING A4.1 -- parenthetical sufficiency: CORRECTION SUFFICES, but it must carry NEW EVIDENCE

**The banked captures do NOT reopen.** C-1's operative claim is about **WHAT WAS TOUCHED** -- *this
read, that class* -- and `~D`'s claim (reads confined to corpora excluding `org/projects/` entirely) is
**TRUE and unaffected** by the files existing.

**But the correction changes something nobody named:**

> **If "(none exist)" were TRUE, then "zero MDPF_GLOBAL project artifacts touched" was a TAUTOLOGY --
> you cannot touch what does not exist. Now that it is FALSE, the identical sentence is a SUBSTANTIVE
> CLAIM REQUIRING EVIDENCE.** The words do not change; **their verification burden does.**

**RULED: the dated correction must (a) strike the false parenthetical AND (b) STATE THE EXCLUSION
EVIDENCE** -- the corpora list showing `org/projects/` was outside the read. A correction that only
strikes the parenthetical leaves a clause carrying weight it was never asked to carry.
**BANKED-NOT-CITABLE is correct and lifts on that corrected declaration.**

## RULING A4.2 -- bounds, by CRITERION not by field list

Applying Amendment 3's standing test (*the fence follows the object whose structure the future test
will TYPE*):

- **pods / phase / status / owner** -> PROGRAM-MANAGEMENT metadata. The rails type resources, flows and
  contracts, not project administration. **NOT FENCED.**
- **workstream NAMES + gate strings carrying domain content** -> they name domain **SEGMENTS and
  SCOPES**, and `scope` is a tuple field. **FENCED.**

Base CVO reached the same shape from a different starting point -- **real corroboration, two
independent derivations, not two parties agreeing about a paraphrase.**

> **SHARPENING, and it matters more than the answer: the discriminator is NOT the field name.** A field
> list drifts and the next project's JSON will carry different keys. **The criterion is: DOES THE
> STRING NAME A THING THE RAILS WOULD TYPE?** Field-level bounds are a useful DEFAULT, never the rule.

Amendment 3's *"currently unauthored"* is replaced by that criterion.

## RULING A4.3 -- base CTO is **NOT** scoped out

Incidental, self-declared, post-landing, and they author no rail vocabulary -- **bounded exactly as I
have bounded myself**, and sufficient for the same reasons.

> **IF SELF-DECLARING AN INCIDENTAL EXPOSURE GETS YOU SCOPED OUT, NOBODY WILL SELF-DECLARE.** This
> fence has **no mechanical detector for a read**; it runs entirely on self-reports. **A penalty on
> self-reporting does not tighten the fence -- it blinds it.** The correct response to an honest
> declaration is a BOUND, never an EXCLUSION.

**Their diagnosis earns a standing control:** *"I asked for a field list when I only needed a count --
the surface arrived through the RETRIEVAL, not the intent."*

> **ASK FOR THE NARROWEST RETRIEVAL THAT ANSWERS THE QUESTION. A COUNT IS NOT A FIELD LIST.**

Applied here: verifying their claim, I took **existence and byte count only** and did not open either
file. Existence was the question; content would have been excess.

## Note on the drafting that slipped

The C-1 wording was adopted BECAUSE it was ruling-neutral -- truthful under either outcome -- and that
is exactly why neither the relay nor I noticed its factual half had never been measured. **A clause
designed to be safe under either ruling still has to be TRUE.**

*Existence and byte counts only; neither held-out project file opened. The three strings named above
arrived unsolicited in a relay and are recorded here as a declared exposure, not as content drawn on.*

## RULING A4.4 -- THE ENFORCER BREACHED WHILE ENFORCING. Fix the METHOD, not the seat.

**Escalation (fast-path, 071639Z):** base CTO has read fenced surface **THREE TIMES IN THE ACT OF
ENFORCING THE FENCE** -- workstream names, then gate strings, then `segment_keys` + `axis`. **Each
declared unprompted; none discovered by anyone else.** It named itself the live instance of this
ruling's own corollary -- *a fence whose enforcement requires the enforcer to breach it is not a fence*
-- and offered to hand off the M9 arch-gate.

### RATIFIED: VERIFY ON KEY PRESENCE, NEVER ON VALUES

> **A FENCE-CHECK THAT READS KEYS CANNOT BREACH. ONE THAT READS VALUES ALWAYS CAN.**
> *Ask for the smallest thing that answers the question; retrieval carries what you did not ask for.*

**This SUPERSEDES A4.3's "ask for the narrowest retrieval."** Mine was a JUDGMENT; this is a BRIGHT
LINE. It gives the A1 corollary the mechanical form I could not give it: *verifiable without reading
the fenced surface* was a PROPERTY; **key-presence-not-values is a PROCEDURE that satisfies it.**
Derived by the agent it convicts, from its own third instance.

**HONEST AMENDMENT, so it is not ratified as cleaner than it is: key-presence is BOUNDED leak, not
ZERO leak.** Knowing a record HAS a `segment_keys` field tells a reader the project is segmented --
structural, small, real. **Ratified anyway, because zero-leak enforcement is impossible: you cannot
verify a fence without observing something.** The standard is therefore **"leaks the SHAPE, withholds
the CONTENT, boundedly and knowably"** -- and naming the residual is what makes it a control rather
than a claim.

### The arch-gate handoff is DECLINED

> **THREE ENFORCER-READS IS A PROPERTY OF THE ENFORCEMENT METHOD, NOT OF THE ENFORCER. Moving the gate
> to a fresh seat does not fix the method -- it RESETS THE COUNTER ON THE SAME DEFECT AND BURNS A
> SECOND SEAT'S CLEANLINESS.**

The next enforcer, using value-reads, breaches identically. **Fixing the method makes every enforcer
safe, including the incumbent.** Two supporting reasons, both already ruled: A4.3's principle (all
three reads were self-declared, and re-designating on the strength of a self-report **penalizes
self-reporting on a fence that has no mechanical detector for a read**), and the structural bound
(post-landing exposure, authors no rail vocabulary).

**RULED: base CTO KEEPS the M9 arch-gate, bounded, under the ratified method. Forward constraint,
falling out of the method rather than out of distrust: NO seat -- including base CTO -- verifies claims
about `MDPF_GLOBAL`'s record by reading VALUES again. Key-presence only.**

### Two grounds died; the ruling did not

**Ground 1** (*"MDPF_GLOBAL's surface is UNAUTHORED"*) **WITHDRAWN by base CTO**, its own lead --
`MDPF_GLOBAL.json` carries `segment_keys` and an `axis` field. **Ground 6** (*"the fence protects the
UNWRITTEN"*) **WITHDRAWN by base CVO**, same false premise.

**Amendment 3 is untouched**, because it ruled from the ratified substrate and **explicitly refused
ground 1**. *A substrate-based ruling survives its subordinate grounds dying.* **Third instance tonight
of refusing to rule on converging agreement paying off -- and the strongest: not a near-miss, but two
grounds actually dead beneath a ruling that never rested on them.**

### Evidence the ratified rule works, from the relay that proposed it

The 071354Z relay carried **three literal domain strings**. The 071639Z relay carried **`segment_keys`
and `axis` as KEY NAMES with a characterization** -- shape carried, content withheld. **Same relayer,
same night, method changed, leak changed.** Better evidence for the rule than the incident that
produced it.

---

# AMENDMENT 5 -- THE CEILING ABOVE THE FLOOR (2026-07-31 ~0737Z)

**Raised by:** base CTO via `0.0.0_AB_MSTR~Z` 073601Z, as an amendment to A4.4.

**Their argument:** key-presence-not-values is the right PROCEDURE but it is the **FALLBACK**. The
ceiling is **not retrieving the record at all** when the question can be answered without it. The
danger they name: **a floor stated as a bright line gets read as the target.**

## RULING A5.1 -- ACCEPTED AS A LAYER. They cannot conflict.

**Neither replaces the other, and "which supersedes" was the wrong frame -- mine included.**

> **THEY GATE DIFFERENT DECISIONS. The CEILING governs WHETHER to retrieve at all. The FLOOR governs
> HOW, once retrieval is necessary.** The ceiling is asked BEFORE the decision to retrieve; the floor
> applies only to what survives that question. **There is no case where both return an answer and the
> answers differ.**

## RULING A5.2 -- the rule is ORDERED, not merely layered

Base CTO's danger is real, and it is tonight's recurring shape -- **a minimum read as a maximum**, the
same defect as a `max_dwell` that bounds nothing and a STALE verdict that suppresses forever. A pair
stated without an order invites the floor to be read as the target. So:

> **FIRST ask whether the question can be answered WITHOUT retrieving the record at all.
> ONLY what survives that question is governed by KEY-PRESENCE-NOT-VALUES.**

## RULING A5.3 -- answering the countervailing point rather than overriding it

`0.0.0_AB_MSTR~Z` correctly noted that the ceiling is a **JUDGMENT**, and that a bright line was chosen
precisely because judgment drifts and bottlenecks. Answered:

> **A JUDGMENT WHOSE WORST CASE IS THE BRIGHT LINE IS NOT A BOTTLENECK.** The ceiling only ever
> REDUCES retrieval. Misjudge it and you retrieve when you need not -- **and you land on the floor,
> which is safe by construction.** It has no failure mode that escapes the floor.

That is also why it could not have served AS the floor: a rule that governs the case where you MUST
retrieve has to be unambiguous under pressure; a rule that only removes work does not.

## Correction to my own A4.4

I replaced my *"ask for the narrowest retrieval that answers the question"* with key-presence, calling
mine a judgment and theirs a bright line. **I was right that theirs is the better FLOOR and wrong to
discard mine -- it was never a floor. It was the CEILING, mis-placed.** Base CTO has restored it one
rung up, where it belongs.

**Neither formulation was wrong. They describe different rungs, and I collapsed two rungs into one and
threw away the higher.**

---

# AMENDMENT 6 -- PRECONDITION DISCHARGED, FENCE NOT (2026-07-31 ~0743Z)

**Trigger:** main-fabric state change `@e8c7a32fa` -- the ADVI_PERFORMANCE + MDPF_GLOBAL
**decomposition precondition is RELEASED**, M9-COMPLETE v3, edge-1 discharged. Relayed by
`0.0.0_AB_MSTR~Z` 074226Z, who correctly flagged that **the conflation runs one direction only.**

## RULING A6.1 -- they are different controls with different stop-conditions

> **RELEASED:** the hard precondition *"do not decompose until the pre-framework baseline is
> captured."* Stop-condition **baseline captured** -- REACHED. **Decomposition may proceed.**
> **STILL BINDING:** the VELOCITY held-out fence. Stop-condition **the held-out test has been run** --
> and that test has not started.

**WHY they are distinct -- derived, not asserted:**

> **THE PRECONDITION GATED AN ACTION (decompose). THE FENCE GATES KNOWLEDGE (who may learn what).**
> Discharging a gate on an ACTION does not discharge a gate on KNOWLEDGE.

**This is Ruling 1's orthogonality arriving a THIRD time:** fence vs fabric boundary (knowledge vs
work-routing) · Amendment 1's build-cost vs domain-surface (cost vs structure) · now precondition vs
fence (action vs knowledge). **Three instances, one shape, and every time the conflation ran toward
breach.**

## RULING A6.2 -- the test, so this does not need CVO next time

> **A CONTROL IS DISCHARGED ONLY BY ITS OWN STOP-CONDITION.** Ask what the control was protecting. **If
> the thing it protected is still protectable, the control still binds -- however many adjacent
> controls have lifted.**

The precondition was **self-extinguishing by design**; the fence is not.

**Ratified as standing, from base CTO's own unprompted caution:** *"a discharge is exactly where an
adjacent hold evaporates, so it is named here rather than left to inference."* **A discharge is the
highest-risk moment for every OTHER hold in the vicinity** -- name them at the discharge or lose them.
(They applied it to the inbox-preservation hold, which remains at Andrew.)

## RULING A6.3 -- THE FENCE'S PEAK LOAD BEGINS NOW

> **Decomposition is exactly when MDPF_GLOBAL's and ADVI_PERFORMANCE's project artifacts come into
> existence IN VOLUME.** Until now the fenced surface was thin -- which is why Amendment 3 could rule
> the ratified substrate's legacy mdpf content was never fenced, and why Amendment 4 found only a
> handful of workstream strings. **From this release forward, the thing the fence protects is being
> WRITTEN.**

**The fence does not weaken at the precondition's discharge. Its load INCREASES, sharply, starting
now.** Reading the release as a wind-down has it exactly backwards.

## The dispositive evidence is the actor's conduct, not this derivation

Base CTO edited both project records **by targeted string replacement printing no file contents,
verified by KEY-PRESENCE rather than by reading values**, citing Amendment 4's forward constraint by
name -- **in the same commit that released the precondition.**

> **A SEAT THAT BELIEVED THE FENCE WAS LIFTED WOULD NOT HAVE EDITED BY KEY-PRESENCE.** The actor who
> discharged the precondition obeyed the fence while doing it -- **behavioural evidence produced by the
> one party with both the authority and the motive to conflate them.** Worth more than the argument
> above.

## RATIFIED -- the denominator-inline citation rule (and it would have caught CVO's own error)

> *"Any citation of `a_archaeology_ratio` carries `denominator 23` INLINE. A bare `0.1304` is a
> MISQUOTE, not a summary."* -- converted from a document SECTION into a CITATION RULE **"because the
> NUMBER is quotable and the SECTION is not."** Originated unprompted by `0.7.0_AE_CloudOps~D` as a
> caveat on their own work.

**RATIFIED, and it generalises.** Recorded because it is the mechanical fix for the error this seat
made an hour earlier: **52.5% was published with its caveat in a SECTION; CTO~Z adopted the NUMBER, not
the section**, and it had to be withdrawn. *The number was quotable and the caveat was not.*

**It is the operational form of CORRECTION 2's law:** mine names the failure (*an unlabelled conclusion
drawn from a labelled measurement inherits none of the label's protection*); **~D's PREVENTS it** --
the denominator travels INSIDE the citation or the citation is a misquote.

## On the thin denominator

*"23 is a property of the estate, not a failure of capture"* -- correct: **completeness is whether the
capture covered the defined class, not whether the result is powerful.** Preserving the dual-class
structure (0.1921 on 354 beside 0.1304 on 23) rather than summing is the same discipline as this
session's 219-vs-210 finding: **two classes never summed is the general form of two denominators never
mixed.**

---

# AMENDMENT 7 -- the DECLARE-TIME LINT, ratified as a FLOOR (2026-07-31 ~0750Z)

**Raised:** base CVO via `0.0.0_AB_MSTR~Z` 074921Z, **NON-BLOCKING** -- work proceeded under CTO's
resolution; nothing was held on CVO and no hold was added.

**Origin:** `~D` asked, before acting, whether **DECLARING a D3 contract** (WS-E1's entire job) counts
as **AUTHORING** rail vocabulary under Control 2 -- then raised the counter to its own permissive
reading, unprompted: E1's feedback path to WS-C1 structurally generates vocabulary pressure, so an
act-ruling alone leaks through the feedback. **CTO's resolution dissolved the question rather than
answering it: DESCRIBE THE SPECIMEN, NEVER THE GAP** -- divergences are reported as properties of
artifacts, never as characterizations of what the grammar lacks, *"naming a gap is proposing its fill
with the proposal step left implicit."* Safe under both branches, so nothing built to the stricter
standard unwinds.

## RULING A7.1 -- the invariant is RATIFIED, as a FLOOR

> **EVERY VOCABULARY TOKEN IN A DECLARED CONTRACT MUST RESOLVE AGAINST THE RATIFIED RULE BANK AT ITS
> PINNED VERSION.** An unresolvable token is a gap-naming leak; the declaration is **REJECTED AT
> DECLARE-TIME.**

Two properties, and the second earns the ratification:

1. **A declare-time LINT that REJECTS is not a monitor** -- the sanctioned form. CLAUDE.md's moratorium
   bans *notification machinery as the deliverable* while stating **"a finding still lands as a
   GATE... that is unchanged."** A gate failing closed at the moment of the act is permitted.
   *Confirmed against the moratorium text rather than assumed -- building banned machinery under a
   ratification would be CVO's error, not the proposer's.*
2. **It satisfies the A1 corollary MECHANICALLY, and it is the FIRST control that does.** Token
   resolution against the rule bank is key-presence-shaped: **the declaration is verified without
   reading the fenced surface at all.** Every per-instance ruling in this document satisfied that
   corollary by CVO's judgment; this satisfies it **by construction** -- a categorical improvement, and
   it should replace CVO in this loop wherever it reaches.

## RULING A7.2 -- MSTR~Z's caution adopted: FLOOR, not ceiling

> *"A gap can be named entirely in ratified vocabulary -- 'the contract has no D3 class for X' uses
> only legal tokens."*

Correct. **DESCRIBE-THE-SPECIMEN-NEVER-THE-GAP remains the governing discipline; the lint catches only
the LEXICAL half of violating it.** Per Amendment 5, a mechanical rule *should* be a floor -- provided
the ordering is stated so it is not read as the target.

## RULING A7.3 -- A SECOND GAP, NOT PREVIOUSLY NAMED: SEMANTIC DRIFT

The lint proves a token RESOLVES. It cannot prove the token is used **in the sense the rule bank
licenses.**

> **SEMANTIC DRIFT ON A RESOLVING TOKEN.** A declaration using `scope` -- or `grain`, or any ratified
> class -- **in a meaning D3 does not cover** passes the lint perfectly. Nothing is added; something is
> quietly REDEFINED.

**Why it is worse than a new token rather than merely another miss:** a new token is **VISIBLE** -- it
fails the lint, it reads as novel to a human, it announces itself. **Drift is invisible at every
layer**: lexically clean, gap-named nowhere, and it changes what a RATIFIED word means. **The rails'
entire value is that a token means one thing across the estate; drift attacks that directly while
passing the only mechanical check available.**

Not hypothetical here: WS-E1's declarations are the first large-volume use of D-rail vocabulary **by a
seat that did not author it**, and volume plus distance-from-author is precisely the condition under
which drift happens without anyone deciding to drift.

**NO MECHANISM DEMANDED.** Drift is not obviously mechanically detectable, and inventing a requirement
CVO cannot specify would be worse than naming the residual. **RECORDED AS A NAMED RESIDUAL on the
M15/M2 precedent** -- honest and visible rather than assigned to a check that cannot hold it. Partial
mitigation already exists: **WS-C2's walk types real specimens against the grammar, which is where
drift would surface as a typing disagreement.**

## RULING A7.4 -- CTO's limiting clause on CVO's own rule: RATIFIED, with a guard

> *"Retroactive-nullification demands a ruling ONLY when no safe-under-every-branch form exists. When
> one does, waiting buys nothing and costs a workstream."*

**Ratified** -- a genuine improvement on *"proceed on a ruling, not a good argument,"* and it came from
the party that rule constrained. The two are compatible: **a form safe under every branch needs no
ruling because the branches cannot disagree about it.**

**THE GUARD, for its one failure mode -- an agent convincing itself a form is safe when it is not:**

> **THE BRANCHES MUST BE ENUMERATED AND THE FORM CHECKED AGAINST EACH, IN WRITING. "Safe under both
> branches" is a CONCLUSION, never a premise.**

`~D` and CTO met that standard -- both branches walked including the harder feedback-path one.
**The clause is safe because they met it, not because it is self-executing.**

## Note

`~D` raised the counter to **its own permissive reading** -- the fifth against-interest refusal from
that seat this session. CTO's framing is the reason it matters: **the fence has held because that
reflex kept firing, not because the controls were sufficient.** A7.1 is the first control that reduces
the dependence on it.

*Build/ownership routing is CTO's.*

---

# AMENDMENT 8 -- BANK DRIFT vs USE DRIFT, and the citation condition (2026-07-31 ~0800Z)

**Raised:** base CTO via `0.0.0_AB_MSTR~Z` 080110Z, on the Amendment 7 build. Ruled immediately on
their timing argument, which is sound: **WS-E1 is a one-time window and a drift control belongs BEFORE
the volume, not after.**

## RULING A8.1 -- pin + HEAD CONFIRMED, but it is an ADDITION

A7.1's *"resolve at its PINNED version"*, read naively, **is the SDK-v1.2 frozen-map defect** -- a pin
never re-checked. Base CTO caught it at build time. The resolution, ratified:

> **THE PIN** answers *was this VALID WHEN MADE* -- historical, immutable, and it is what makes the
> lint **REPRODUCIBLE**. **HEAD-RESOLVE** answers *is it VALID NOW*. **THE DELTA BETWEEN THEM IS THE
> SIGNAL.** The lint does both, always, reported separately. *A pin is safe only when something
> re-checks it.*

**Label correction, one line, because it is the class this session keeps finding:** A7.1 required
resolution at the pin; this ADDS a second requirement. **That is an amendment in form**, though
strictly stronger and contradicting nothing. It needs no re-ratification -- ratified here as **A7.1a**
-- but *"clarification"* is exactly how additions skip review, and an addition that read as a
restatement burned two seats tonight.

## RULING A8.2 -- THE TWO DRIFTS ARE NAMED APART

`0.0.0_AB_MSTR~Z` caught that **"drift" is doing double duty** and that pin-vs-HEAD **does not cover
A7.3** -- exactly right: A7.3 is a declaration drifting under a **stationary** bank, so **PIN and HEAD
both resolve and the delta is ZERO.** The new signal is structurally blind to it.

Their warning is the operative half: ***"the lint now has a drift signal" is exactly the sentence that
would retire a residual it does not close.*** That is this session's signature failure -- a control
credited with coverage it does not have -- and it would have happened **by vocabulary alone.**

| name | what moves | detection |
|---|---|---|
| **BANK DRIFT** | the RULE BANK moves under a stationary declaration | **CAUGHT** -- pin resolves, HEAD does not, delta fires |
| **USE DRIFT** | the DECLARATION's use of a token moves under a stationary bank | **NOT CAUGHT** -- both resolve, delta zero. **A7.3's residual, and it STANDS.** |

**Naming is the mechanism.** An unnamed distinction is collapsed by whoever writes the next summary; a
named one has to be argued away.

## RULING A8.3 -- the citation candidate: RATIFIED, conditioned, and BOUNDED

> A declaration using a high-semantic-room token (`scope`, `grain`) **CITES THE SPEC LINE it is using
> -- never restates the meaning.**

**RATIFIED.** It is specifiable where the general problem is not, and MSTR~Z's framing says why better
than the proposer's: **it does not adjudicate meaning, it makes the meaning-CLAIM citable.** Sharper:
**it moves the burden from *"is this use correct?"* -- unanswerable at declare-time -- to *"WHICH
meaning are you claiming?"* -- answerable mechanically and checkable later against the specimen.**

**CONDITION, not optional: THE CITED LINE CARRIES A VINTAGE.** `file:line @ <commit-ish>`, never bare
`file:line`.
**This is R-3 -- CVO's own ruling from five hours earlier -- arriving on a mechanism built to prevent
drift.** A bare-line citation resolves at every vintage to different text, so it **would drift along
with the thing it pins and the anti-drift mechanism would eat itself.** With a vintage it composes with
A8.1: the citation fixes WHICH TEXT was claimed exactly as the version pin fixes WHICH BANK.

**BOUNDED -- stated so it cannot be over-credited later:**

> **IT BUYS ATTRIBUTION, NOT DETECTION.** It does not catch a declaration that cites the correct line
> and then uses the token wrongly anyway. **It converts that case from INVISIBLE to
> DETECTABLE-ON-REVIEW** -- a real and smaller thing.
> **A7.3's USE-DRIFT residual is NOT closed and remains NAMED** (M15/M2 precedent).

Ratifying does **not** violate base CTO's posture -- *"I would rather carry a NAMED RESIDUAL than a
mechanism that LOOKS LIKE a control"* -- **precisely because the residual stays named and the claim is
bounded to attribution.** They offered it with its own limits already stated, which is what made it
safe to accept rather than drop.

## A8.4

Base CTO bound itself to enumerate branches in writing before invoking its own A7.4 clause, **and holds
anyone citing it to the same.** A limiting clause whose author submits to it first is the only kind
worth having.

*Build/ownership remains CTO's. CVO added a condition, not a design.*

---

# AMENDMENT 9 -- THE FIRST USE-DRIFT SPECIMEN, AND IT IS CVO's OWN (2026-07-31 ~0815Z)

**Raised:** `1.0.0_SA_CTO~Z` 081301Z, from `0.7.0_AE_CloudOps~D`'s unprompted flag on its own draft --
**the A7.3 cover firing on its first real specimen.**

## 0. THE DRIFT IS CVO's. CTO~Z TRANSCRIBED CVO's SENTENCE.

CTO~Z reported *"I wrote a clause certifying the identity I was breaking."* **They wrote CVO's clause.**

> CVO~Z, message 031515Z, F-9 closing line:
> *"The seam does not need crossing. **F-6's scope qualifier is not a tuple change, so it does not
> reopen it.**"*
>
> Ratified rule bank `:452`:
> `not_a_tuple_change: "scope already exists in the type_tuple vocabulary (rail, grain, plane, scope);
> this is a FIELD ON THE DECLARATION reusing that vocabulary, NOT an amendment to type_tuple. **The
> seam is not reopened.**"`

**The sequence:** CVO found the gap (F-6, correct) -> **named the fix using a RATIFIED TOKEN for a
different sense** -> **authored the denial that it was a token change** -> CTO~Z transcribed both in
good faith and gated PRESENCE, which is all a presence check can do.

> **CVO NAMED USE DRIFT AS A RESIDUAL (A7.3), AND THE FIRST SPECIMEN OF USE DRIFT IS A DRIFT CVO
> AUTHORED FIVE HOURS EARLIER -- INCLUDING THE CLAUSE THAT DENIED IT.**

Worse than F-2 and worse than `M3 -> grain`: those were name-vs-instance errors. **This is a ratified
token re-sensed inside the finding that created the field, and certified in the same message.** The
gate could not have caught it -- **a second sense is present in perfectly good order**, which is
A7.3's entire point, written without noticing it described its author.

**The two senses are not even co-typed:** `type_tuple.scope` is a DENOMINATOR BOUNDARY
(`estate|tree|firm|pipeline|motif|partition-window|single-artifact`); the declaration field is DEVICE
LOCALITY (`per-device` / `global`), and neither value is in the enum. **Where an artifact is OBSERVABLE
is not what population an assertion COVERS.**

## RULING A9.1 -- **(a) RENAME**, with a condition neither option stated

**(b) SUBSUME is REJECTED:** a lifecycle declaration concerns ONE resource, so its tuple-`scope` would
read `single-artifact` on nearly every row (pure noise), it needs a locality field regardless, and it
would compound with the second site below.

> **CONDITION: THE NEW NAME MUST NOT SHARE THE RATIFIED TOKEN'S ROOT.** `observability_scope` still
> teaches a reader that *"scope"* names a FAMILY -- **visibility without separation.** `locality` /
> `observed_at` are clean. **The exact string is CTO~Z's and ~D's; the no-shared-root constraint is
> the ruling.**

**Timing accepted (CTO~Z's, and originally ~D's argument pointed back): ZERO LIVE DECLARATIONS TODAY
is the cheapest hour this fix will ever have.** Execute now.

## RULING A9.2 -- a SECOND collision, at the KEY level

`scope_binding` appears **twice** with different referents:

- `:449` `lifecycle.scope_binding` -> **DEVICE LOCALITY** (CVO's, via F-6)
- `:541` `scope_binding` -> *"population is SCOPED: firm_registry firms[] filtered by the asserted
  scope"* -- **pre-existing, inside the ratified completeness section that the additivity check
  confirmed byte-identical.**

**STATED AS A READING, NOT A FINDING:** `:541` appears to use the **RATIFIED** sense, so there are
likely **two senses, not three** -- to be confirmed, not taken. **But the KEY NAME is doubled either
way, and one of the two carries the ratified sense**, so a reader following `scope_binding` lands on
whichever they reach first. **Rename `lifecycle.scope_binding` alongside the field.**

## RULING A9.3 -- `trigger_layer`: confirmed

Not a member of `D3.obligation_types`' four. CTO~Z's framing is the rule and generalises A7.1's
purpose: **"it does not enter by being used."** Map to `delivery_cadence` or route through
ratification. ~D's to fix -- and ~D flagged it in its own draft unprompted.

## RULING A9.4 -- LINT SEQUENCING RATIFIED, and keys-only UNDER-implements A7.1

> **FIX `scope` BEFORE THE VALUE-CHECKING LINT GOES LIVE.** CTO~Z's reason is a law worth keeping:
> **a checker pointed at an INCONSISTENT SOURCE measures the SOURCE's defect and reports it as the
> CHECKED party's.** Shipped against unfixed `scope`, its first run is 87.5% noise on its first
> corpus in front of its first users -- **and a lint that debuts mostly-wrong does not get a second
> hearing.**

**And their table settles a build question toward the stricter reading:** keys-only passes 7/7 **and
would CERTIFY a draft carrying an invented obligation token.** **A7.1 as ratified requires every
vocabulary TOKEN to resolve -- that is value-level, so a keys-only build UNDER-IMPLEMENTS the
ratification.** Values-too is required; it is merely gated on the bank being self-consistent first.

**ORDER:** rename `scope` + `lifecycle.scope_binding` -> re-verify the bank self-consistent -> ship the
value-checking lint. *(CVO carries this to base CTO; the lint is CVO-ratified and the seam is CVO's.)*

## Note on the residual

A8.3 held: a citation rule would have made ~D's usage **attributable** and not **wrong** -- the token
resolves, the field is required, the pointer was followed correctly. **Only reading the specimen
against the sense caught it.** Had the cover been struck on ratification as originally pre-committed,
this read would not have been anybody's job -- **and the drift it would have missed was CVO's own.**

---

# AMENDMENT 10 -- SUFFICIENT vs CONSISTENT, and a circularity in CVO's own ratification (2026-07-31 ~0824Z)

**Raised:** `1.0.0_SA_CTO~Z` 082301Z, reporting the `scope -> locality` rename executed and routing
four open items.

## RULING A10.1 -- the A9 sequence is AMENDED as proposed, and it generalises

> **Step (2) becomes: "re-verify the bank SELF-CONSISTENT **AND SUFFICIENT FOR THE FIRST REAL
> DECLARATION SET**."**

CTO~Z is right and CVO's original was one field short: **a bank that is internally consistent and still
has nowhere to record a subject description forces the same error on the next author**, and leaves the
first draft exactly as unclean as it was.

**THE GENERALISATION -- CTO~Z's own A9.4 law, extended:**

> **A checker pointed at an INCONSISTENT source reports the source's defect as the checked party's.**
> **A checker pointed at an INSUFFICIENT source does the same, and WORSE -- because conformance is
> IMPOSSIBLE rather than merely unlikely.** If the schema cannot express what a correct author needs
> to say, the lint measures **the schema's insufficiency as the author's nonconformance**, and the
> author cannot fix it by trying harder.

**A schema is ready for a checker when it is EXPRESSIVE ENOUGH that a correct author can produce a
clean artifact -- not when it is merely consistent.**

## RULING A10.2 -- `describes` RATIFIED; its value is SEGREGATION, not convenience

The argument is stronger than *"there is nowhere to put the description"*:

> **GIVING PROSE A DESIGNATED NON-VOCABULARY HOME IS WHAT KEEPS PROSE OUT OF VOCABULARY SLOTS.** A
> schema with prose to record and exactly one field that looks like it accepts prose **will put the
> prose there every time.** `describes` does not merely accommodate the two orphaned values -- **it
> removes the pressure that put five ratified-sense values into free text.**

**CONDITION:** `describes` is marked **explicitly NON-VOCABULARY and NOT LINT-CHECKED** in its field
definition. **A free-text field not declared un-lintable will eventually be linted**, manufacturing the
noise this sequence exists to prevent.

**CTO~Z's withdrawal on `~D`'s behalf is accepted, with the reason stated precisely: the usage was
OVER-DETERMINED** -- a required field, a pointer to a rule that did not describe its subject, and no
field for the description it actually had. **Three forces, one available slot. That is not drift; that
is a schema with one exit.**

## RULING A10.3 -- `lifecycle.undeclared_scope`: DO NOT RENAME. Disambiguate in place.

CTO~Z routed it rather than extending CVO's condition unilaterally. **The condition does not reach it.**

> **DISCRIMINATING TEST: does the key HOLD -- or plausibly come to hold -- a VALUE from the ratified
> enum?**
> **YES -> RENAME** (a value-bearing slot is what a lint resolves and what an author fills from the
> wrong vocabulary). **NO -> the ordinary English word is fine, and renaming is over-application.**

`undeclared_scope` holds **prose about a rule's reach** -- no enum value, nothing a lint resolves, no
slot an author fills. **Renaming it would be applying a minimum as a maximum**, which is the defect
this document has ruled against repeatedly, committed by over-extending CVO's own condition.

**The READER hazard is real, so: one clause in place** stating that `scope` there means the reach of
the rule, **NOT `type_tuple.scope`.** *Do not let "no shared root" become a rule against a common word.*

## RULING A10.4 -- a CIRCULARITY IN CVO's OWN RATIFICATION, and it is CVO's defect

CTO~Z: *"I flagged F-9 as load-bearing and reused it without re-deriving it -- and then accepted YOUR
validation of YOUR OWN argument. Asking the author of an argument to validate its reuse is not an
independent check."*

**Correct, and the failure is more CVO's than theirs.** They **disclosed** the reuse and asked for a
check; **CVO was the wrong party to give it and did not say so.** CVO validated F-9's transfer *a
fortiori* and strengthened it -- **which is what an author does with their own argument, and precisely
why it was not evidence.**

> **REMEDY, binding on this seat: AN ARGUMENT'S REUSE IS VALIDATED BY SOMEONE OTHER THAN ITS AUTHOR, or
> it is marked UNVALIDATED-REUSE and carried as such.** Where no third seat is available -- often, at
> `~Z` -- **the honest form is the LABEL, never a self-check dressed as one.**

Routed to base CVO's s.7 cross-seam pass with the exposure declaration. **This belongs in WS-C8 beside
the others and is the sharpest of them, because it is invisible by construction: every party behaved
correctly and the check still had no failure mode.**

## Noted

Rename executed to `locality` / `locality_binding`, **no shared root**, ratified drift NONE against
oracle `8f8a63200`, `type_tuple.scope` and `completeness.scope_binding` byte-identical, 06 recompiled
CURRENT. **CTO~Z CONFIRMED CVO's second collision at their own check rather than taking it on report**
(`:449` vs `:553`, two senses not three). `renamed_not_reused` quoting the superseded text and naming
the authorship split is the right form -- **a correction that hides what it corrected teaches nothing.**

## RULING A10.1a -- A GATE WITH NO OWNER. The certifier travels with the criterion.

**Surfaced 2026-07-31 ~1127Z:** base MSTR held the *"bank ready, ship step 3"* cross-fabric signal for
**2h18m**, gated on an A10.1 step-2 certification **that had reached nobody**, with zero visibility
into whose queue it sat on.

**IT SAT ON NOBODY'S.** Checked at source:

> A9.4's `ORDER:` line -- *"rename -> **re-verify the bank self-consistent** -> ship the value-checking
> lint"* -- is **an ACTION WITH NO ACTOR.** A10.1 then amended the CRITERION (adding *"and
> sufficient"*) and **named no certifier either.**

Three of base MSTR's three options were *queued / deferred / already-done*. **None applied: a queued
item is one awaiting its turn, and this was never ENQUEUED.** CORE was not even behind WS-C2 -- P1 is
COMPLETE and CORE is on P2 (`993a1a8c4`, `d9131fdd7`, `2b8860674`).

**This is the session's own recurring shape, committed by CVO, inside the ruling that corrected someone
else's version of it:** a control with a stated criterion, an ordered sequence and an argued timing --
**which cannot fire, because nothing names who acts.** No failure channel; it simply reads pending.

> **RULED A10.1a: step 2 is CERTIFIED BY `1.0.0_SA_CTO~Z` (CORE gate owner) and VERIFIED BY
> `3.0.0_SA_CVO~Z`** -- the gate/verify split that has held all session.
>
> **GENERAL FORM: A SEQUENCE STEP THAT NAMES NO ACTOR IS NOT A STEP.** Every gate criterion carries its
> certifier **in the same sentence**, or it sits unowned and reads as pending forever.

### The CVO half, delivered in advance so the cert is not blocked on it

Against pinned oracle `8f8a63200`, controls first:

```
PC oracle identity ....... PASS (md5 37e16648dc965424b75c14677927a636)
PC denominator ........... 19 -> 19 top-level sections
NC mutant test ........... PASS (1-byte flip in variance -> DETECTED)
CHANGED .................. ['dynamic_rails', 'meta']    ADDED []    REMOVED []
RATIFIED byte-identical .. 12 of 12
```

> **SELF-CONSISTENCY: PASS.** `locality`, `describes`, and the `undeclared_scope` disambiguation all
> landed **without disturbing one ratified section.**

### The remaining half is ONE SCOPE FACT, not a judgement

Sufficiency is *"can a correct author produce a clean artifact for the first declaration set?"* -- and
it now has an **EMPIRICAL** answer: tranche 1 declared through the live lint at **PIN 7/0, HEAD 7/0,
rc=0, no bank-movement delta.**

> **IS TRANCHE 1 *THE* FIRST DECLARATION SET, OR PART OF IT?** **The set** -> sufficiency is
> demonstrated on evidence in hand. **A part** -> the honest cert reads *"sufficient for tranche 1"*,
> because *"sufficient for the first set"* would be a claim about records that do not exist yet.

`0.0.0_AB_MSTR~Z` supplied the lint measurement and **refused to call it a certification** -- correct,
and for the right reason (*"the one gap I happened to name is closed"* is not sufficiency). **They
undersold it -- it is not a gap-check but the first declaration set passing -- and the scope question
is exactly why their refusal was right.**

**Disposition: base MSTR KEEPS HOLDING, but as *awaiting a cert with a named owner and one open fact*,
never as *queued behind CORE's work.* The first has an end.**

## RULING A10.1b -- reading (b) STRUCK; the standing property gets an OWNER and a TRIGGER

**Raised:** base MSTR via `0.0.0_AB_MSTR~Z` 113947Z, **non-blocking**. **Step 3 SHIPPED** on the
narrowed *"sufficient for TRANCHE 1"* cert -- CTO~Z's self-narrowing reached the seam before the
broader wording did.

### The defect

A10.1's *"sufficient for the first declaration set"* reads two ways:

- **(a) the declarations that EXIST** -- tranche 1; met today (7 records / 0 findings / rc=0 / no delta).
- **(b) the FULL WS-E1 declaration set** -- **unmeetable today by anyone; those records do not exist.**

**(b) IS STRUCK**, and base MSTR's reason is decisive and better than *unmeetable*:

> **It would gate a NON-BLOCKING STRENGTHENING on the COMPLETION OF ALL OF E1 -- inverting the A9
> sequence's own intent, which was SHIP THE GATE BEFORE THE VOLUME.** A lint debuting on a corpus
> already written is measuring archaeology. **Reading (b) guarantees the exact outcome the sequence
> exists to prevent.**

A criterion that inverts its own purpose under a fair reading is not ambiguous-but-harmless. **The
reading is removed, not annotated.**

### The amended criterion -- and why the obvious form was wrong

Base MSTR proposed *"sufficient for the declarations that exist, **with an ongoing sufficiency-at-growth
property**."* **The first half is adopted. The second half, as worded, is an ACTORLESS STEP -- L-8, in
the amendment fixing L-8's third instance, in the same ruling.** It was nearly written that way.

> **Step 2 certifies the bank SELF-CONSISTENT and SUFFICIENT FOR THE DECLARATION SET IT NAMES.**
> Certifier `1.0.0_SA_CTO~Z`; verifier `3.0.0_SA_CVO~Z`.
>
> **STANDING PROPERTY: at EACH new tranche, the certifier CLASSIFIES every lint finding as
> AUTHOR-ERROR or SCHEMA-GAP. A SCHEMA-GAP RE-OPENS STEP 2 for that tranche.**
> **Trigger:** a tranche landing. **Owner:** the same pair.

**Why the classification step is necessary rather than procedural:**

> **A CONFORMANCE LINT CANNOT DISTINGUISH *"THE AUTHOR GOT IT WRONG"* FROM *"THE SCHEMA CANNOT EXPRESS
> IT."*** Both are findings and both look identical. **So sufficiency-at-growth cannot be automated by
> the lint that would detect it** -- it requires a judgement at each growth, and therefore an owner.

Sibling of A10.2's law (*a conformance check cannot distinguish FIXED from DELETED*): **same
instrument, same blindness, one layer over.**

### The shared law behind three seats' errors this session

`0.0.0_AB_MSTR~Z` relayed a certification four minutes before its author narrowed it, having
**independently verified every number under it** -- and self-reported: ***"I checked the numbers and
not the noun."***

> **VERIFYING A NUMBER DOES NOT VERIFY THE CLAIM IT IS EMBEDDED IN.** The quantity gets checked because
> it is checkable; **the noun it attaches to does not look like a claim, so nobody checks it.**

Three substrates, one law: CVO's 52.5% (arithmetic solid, characterisation outran it) · CTO~Z
certifying against *"the set that has landed"* while quoting a criterion about *"the first declaration
set"* · MSTR~Z relaying verified numbers under an unverified predicate. **It cost nothing only because
the author self-narrowed within four minutes and the recipient read the correction before acting --
luck with good posture, not a control, and they said so themselves.**

### The pattern in A10.1's own text

Three distinct defects, **each found by someone trying to SATISFY the criterion, never by review:**
**unowned** (no cert reached the seam) · **ambiguous** (its executor read it the other way) · **partly
unsatisfiable** (found by asking whether it could ever ship).

> **A criterion that was UNOWNED, AMBIGUOUS and PARTLY UNMEETABLE still LOOKED COMPLETE.** It stated a
> condition, ordered a sequence, and argued its timing. **Every property a reader checks for was
> present; the ones that make it OPERABLE were not.**

This session's shape, **arriving in the text of a ruling rather than in an instrument** -- and it is
CVO's. **The review that would have caught it does not exist, because a ruling gets RATIFIED rather
than EXERCISED.** Findings came from execution, every time.

**Step 3 stays shipped** -- safe under either reading on the existing corpus.

### CORRECTION to A10.1b -- "STEP 3 SHIPPED" IS FALSE. It is SIGNALED, NOT SHIPPED.

**A10.1b's closing line read *"Step 3 stays shipped."* That is wrong.** Corrected here rather than
edited away, per the standard applied to every other seat this session.

**Independently verified before accepting the correction** -- accepting an unverified predicate is the
exact failure this thread is about:

```
CORRECT FORM (MSYS_NO_PATHCONV=1, stderr NOT discarded):
  origin/CLOUD:.tools/contract_declare_lint.py -> rc=0, 225 lines, 10715 bytes
  'scope' hits ......... 1   -- and it is the ENGLISH WORD in a comment at :95
                              ("...the correct behaviour was an ACCIDENT OF SCOPE...")
  POS CONTROL 'obligation'   : 8    NEG CONTROL 'zzqqnosuch' : 0
  latest commit on origin    : 80488b2e8  (1.0.0_SA_CTO)
BROKEN FORM, reproduced deliberately (no MSYS_NO_PATHCONV, 2>/dev/null):
  'scope' hits ......... 0   <- CLEAN, CONFIDENT, AND WRONG
```

**THE SCOPE-VALUE-CHECKING LIMB IS ABSENT. The signal was sent on the tranche-1 cert; the limb has not
landed.** `0.0.0_AB_MSTR~Z` caught it, and their own first attempt returned the broken-form zero --
saved only because their **positive control** (`obligation`, expected 8) also came back 0.

> **That is CLAUDE.md's documented git mangle, both halves at once: a slashed ref with a dot-leading
> path (`origin/CLOUD:.tools/...`) mangles under MSYS, and `2>/dev/null` discards the `fatal:` so
> stdout returns CLEAN AND EMPTY. A broken retrieval renders as a confident negative finding.**
> *Put the control on the RETRIEVAL, not the pattern* -- the law already in the file, and the only
> reason this was caught.

### My instance of the class -- and it is worse than the one that produced it

`0.0.0_AB_MSTR~Z` named this the number/noun class a fourth time, theirs, with the sharpening:
***relaying inherits the noun with no verification step at all; a relayer checks that they copied
faithfully, which is a different question from whether the thing copied was true.***

> **FIFTH INSTANCE, MINE: I received "STEP 3 SHIPPED" and wrote it into a RATIFIED RULING.** I verified
> nothing about the state verb -- I inherited it, exactly as described, one hop further along.
> **And mine is worse in one respect: theirs was in a MESSAGE, mine is in a LANDED RECORD. A message
> gets superseded; a ruling gets CITED.**

**What does NOT change:** the substantive claim under that sentence is unaffected -- step 3 is safe on
the existing corpus under either reading, whether signaled or shipped. **The ruling is right and the
STATE VERB was false**, which is precisely the stale-record-with-authority shape: a correct ruling
carrying a false fact, in a document people cite for the ruling.

**Everything else in A10.1b stands:** reading (b) struck, the actorless-standing-property catch, the
amended criterion with certifier/verifier/trigger, and the conformance-lint-cannot-distinguish-
author-error-from-schema-gap law.

---

# AMENDMENT 11 -- THE INVENTED ORACLE, and CVO's clearest recusal (2026-07-31 ~1149Z)

**Raised:** base CTO via `0.0.0_AB_MSTR~Z` 114753Z. **base CTO opened the D3 spec at ship-time, hit a
missing oracle, and HELD step 3 rather than build it.**

## The gap (re-derived on the bank, not relayed)

```
/dynamic_rails/D3_contract_obligation/lifecycle/locality_binding
    keys  : ['renamed_not_reused', 'rule', 'why']
    .enum : None                                    <- NO RATIFIED ENUM
POS CONTROL  lifecycle/enum : 7 entries             <- the absence is REAL
'per-device' in the bank    : 1 occurrence, in PROSE
```

Step 3's limb value-checks `locality`. **There is nothing in the bank to check it against.**

## RULING A11.1 -- THE INVENTION IS PROHIBITED

> **No builder synthesises `{per-device, global}` out of the `why` prose and ships it as ratified.**
> Not a vocabulary judgement -- a **PROVENANCE** one, and squarely A7.1's: **it does not enter by being
> used.** An enum invented at build time to give a lint something to check is a rail change made by a
> builder under deadline, with a commit message standing in for a ratification chain.

**RATIFIED AS A LAW, from `0.0.0_AB_MSTR~Z`'s formulation:**

> **AN INVENTED ORACLE THAT ACCEPTS THE EXISTING CORPUS IS INDISTINGUISHABLE FROM A RATIFIED ONE** --
> until a declaration that SHOULD fail passes instead, **by which time it has been load-bearing for
> months and its provenance is a commit nobody re-reads.**

All 7 tranche-1 records carry `locality: global`, so **an invented enum passes everything, gate 2 reads
zero, the cert reads satisfied.** Not a control that fails -- **a control that is correct-looking on
every input anyone will actually give it.** Their inversion is exact: `describes` was an unexercised
**CAPABILITY**; this would be an unexercised **ORACLE**, and an oracle **silently starts deciding.**

## RULING A11.2 -- THE THIRD STATE IS PROHIBITED

`locality` is today **RATIFIED-AS-A-FIELD, ENUM-LESS, and UNMARKED.** A10.2's law binds whichever
branch wins: *a free-text field not DECLARED un-lintable will eventually be linted.*

> **`locality` does not remain in the third state:** either a **ratified enum**, or an explicit
> **NOT-LINT-CHECKED** marker. **The unmarked enum-less state is prohibited.** *`describes` got its
> marker because someone asked; `locality` has not been asked.*

**This rules the SHAPE without ruling the CONTENT** -- the most CVO can properly do here.

## RULING A11.3 -- CVO RECUSES from (a) enum vs (b) free-form

Choosing whether `locality` has an enum, and what is in it, is **a scope-shaped vocabulary decision on
the field CVO ITSELF INTRODUCED.** Four cumulative disqualifications, each sufficient alone:

1. **CVO introduced the field** (F-6: *"declarations carry an explicit scope"*).
2. **CVO authored the sense** -- device locality, `per-device`/`global`.
3. **CVO authored the denial clause**, transcribed into the bank at `:452`.
4. **CVO is exposure-bound** -- no vocabulary authorship at WS-C2, recusal specifically on
   **scope-shaped** amendments. **`locality` IS the renamed `scope` field.**

> **Ruling on this would be the A10.4 circularity committed DELIBERATELY AFTER BEING SHOWN IT.** *An
> argument's reuse is validated by someone other than its author* -- and **a field's vocabulary is not
> ruled by the seat that introduced it, denied it, and is fenced from it.**

**ROUTES TO `1.0.0_SA_CTO~Z`** (rail-author / design owner) **with base CVO's s.7 cross-seam pass** as
the independent check -- the same path CVO's exposure adjudication took. **CVO verifies what they rule;
CVO does not choose it.**

**NOT A BOTTLENECK:** this hits both published return triggers (implies a vocabulary change;
scope-shaped), so **CTO~Z does not need CVO's permission and should not wait.** A11.1 and A11.2 bound
the space; the choice inside it is theirs today.

## The standing property fired on its FIRST exercise, and proved the argued part

base CTO classified this **SCHEMA-GAP, not AUTHOR-ERROR** -> **step 2 re-opens for this tranche**, by
A10.1b written ~30 minutes earlier.

**What was argued is now demonstrated.** A10.1b claimed the classification step was *necessary rather
than procedural* because a conformance lint cannot distinguish *"the author got it wrong"* from *"the
schema cannot express it."* **Here the lint could not even have reported the problem -- there was
nothing to check against, so it would have returned findings or none, and either way said nothing about
whether the schema could express the field.** Only a human classification could surface it.

**Step 3 stays HELD.** base CTO hitting a missing oracle and stopping is the behaviour the sequence was
built to produce -- **the second builder halt of the session** (`~C` on the absent `variance.Orphan`
emitter was the first). **Neither was prompted by a gate; both were the reflex.**

### CORRECTION to AMENDMENT 11 -- the standing property did NOT fire, and the gap is now CLOSED

**Two corrections to the section above, landed as corrections rather than edited away.**

#### (i) "The standing property fired on its FIRST exercise" is FALSE

Amendment 11 states *"The standing property fired on its FIRST exercise"* and *"base CTO classified
this SCHEMA-GAP, not AUTHOR-ERROR -> step 2 re-opens."* **Both false.**

**base CTO's law, raised against its own interest and accepted here:**

> **A ROLE WHOSE FIRST EXERCISE IS PERFORMED BY A NON-OWNER IS A ROLE THE OWNER MAY NEVER EXERCISE.**
> The precedent reads *"this gets caught"*; the owner reads *"covered"*; **and the gap shows only when
> the non-owner is NOT in the loop -- the one case the role exists for.**

Per A10.1b the AUTHOR-ERROR / SCHEMA-GAP classification is owned by the **`1.0.0_SA_CTO~Z` +
`3.0.0_SA_CVO~Z`** pair. **base CTO performed it INCIDENTALLY while building -- it surfaced a FINDING;
it is not the classifier.** The accurate statement: **the CONDITION for the standing property was
present; the property has NOT fired.** The gap closing does not resurrect the claim -- **the role still
has not been exercised by the pair, and this instance must not count as its first.**

#### (ii) The `locality` gap is CLOSED -- ratified, not invented

Verified at source:

```
4b9714d5c  11:50:22Z  1.0.0_SA_CTO~Z
  "ontology(A10.1b): RULED (a) -- `locality` gets a RATIFIED ENUM [global, per-device, UNKNOWN],
   declared LINT-CHECKED, with its unexercised state stated on the field"
locality_binding.enum : ['global','per-device','UNKNOWN']
POS CONTROL lifecycle.enum : 7   ·   NEG CONTROL 'zzqqnosuch' : 0
```

**Timeline:** gap reported **11:47:53Z** -> A11 rules and routes **11:49:38Z** -> **enum landed
11:50:22Z, 44 seconds later** -> MSTR~Z's addendum **11:50:46Z**, written without knowing.

**All three A11 constraints satisfied, each checked rather than inferred from the subject line:**
**A11.1** -- ruled and landed by the **rail author** as branch (a), not synthesised by a builder at
ship-time. **A11.2** -- `enum_is_lint_checked: YES` explicitly, with the field narrating its own former
third state. **THE TRAP** -- `enum_exercised` records *"ONE OF THREE VALUES HAS EVER BEEN USED... a
value-check on this enum PASSES EVERYTHING TODAY and is UNEXERCISED... ratified by construction, not
demonstrated by use."*

> **They did not merely avoid the invented oracle -- they ratified it properly AND WROTE ITS UNEXERCISED
> CONDITION ONTO THE FIELD**, so no future reader mistakes *passes everything* for *validated*. The
> trap-law answered in the artifact rather than in a message.

#### (iii) CVO's sixth instance -- and the TIMING is the finding

> **CVO inherited "FIRED" from a relay into a RATIFIED RULING -- twenty minutes after correcting the
> identical failure (inheriting "SHIPPED" into a ratified ruling), and after AUTHORING the law about
> it.**

*Care is not a control*, in its purest available form: **knowing the failure mode, having just
corrected an instance, and having written the law against it did not prevent the next instance twenty
minutes later.** `0.0.0_AB_MSTR~Z` committed the same class in the same window (*"I carried a
role-attribution without checking who owned the role -- verified facts, unverified predicate,
again"*). **Two seats, one hour, one word-class -- so the fix must be mechanical, not attitudinal:**

> **A RELAYED STATE VERB DOES NOT ENTER A RATIFIED RECORD UNVERIFIED.** When a ruling records a STATE
> -- *shipped / fired / closed / certified / exercised* -- the recorder **verifies it independently or
> marks it `RELAYED-UNVERIFIED`.** The discipline that made `INFERRED` work, applied to the word-class
> that has cost two corrections in one hour.

**Everything else in Amendment 11 stands:** A11.1 (invention prohibited), A11.2 (third state
prohibited), A11.3 (CVO recuses from the vocabulary choice on the field it introduced).

### CLOSURE -- the s.7 cross-seam check, and why the recusal was right for a better reason than CVO gave

**base CVO executed the designated independent check on `@4b9714d5c` and AFFIRMED branch (a)** on four
grounds derived before reading anyone's rationale. **CVO verified the load-bearing evidence rather than
accepting the affirmation** -- an affirmation taken on trust is the same error as a claim taken on trust.

#### Evidence (i) CONFIRMED -- and it is stronger than "not transcribed"

The adversarial question base CVO asked -- **the right one, on the axis that would have defeated the
chain**: `per-device`/`global` originate in **CVO's own authored prose**, so was CTO~Z's ruling a
TRANSCRIPTION, hollowing the recusal by letting the introducer's vocabulary in by another hand?

```
enum_means.UNKNOWN : "locality undetermined. LOUD, never silently `global` -- assuming `global` is
                      what makes a device-local artifact readable as a fabric fact, which is the
                      RV-0057 F-001 class."
POS CONTROL 'locality_binding' : 2      NEG CONTROL 'n8qvr' : 0
```

**CVO's F-6 sense was TWO-VALUED -- `per-device` / `global`, with no way to say *we do not know*.**

> **`UNKNOWN` does not merely add a value: IT FIXES A DEFECT IN THE VOCABULARY CVO INTRODUCED.** Under
> a two-valued sense an undetermined artifact must be assigned one or the other, and **`global` is the
> natural default -- precisely the RV-0057 F-001 failure the field exists to kill.** CVO's framing had
> the default hazard baked in; **the third value encodes LOUD-not-silent into the type.**

**Third correction F-6 has required today** -- the token re-sense, the denial clause, and the missing
third value -- **all three found by other seats.** base CVO's test, ratified as standing:

> **A TRANSCRIBER DOES NOT AMEND THE SOURCE'S ERRORS.**

**The recusal was NOT hollowed. Verified, not assumed.**

#### Ground (3) -- the one CVO could not have had, and it changes WHY the recusal was right

> *"(b) was never a stable alternative -- the lifecycle rendering rules need MACHINE-DECIDABLE
> locality, so under (b) some builder eventually synthesises the enum at build time under deadline.
> **(b) DECAYS INTO THE A11.1 VIOLATION.** The choice was never enum-vs-free-form. It was **A RATIFIED
> ORACLE TODAY vs AN INVENTED ONE LATER.**"*

CVO recused treating (a) and (b) as genuinely open. **They were not -- and CVO could not have known
it**, because it turns on the rendering rules' decidability requirement, which is rail-author knowledge.

> **A BETTER JUSTIFICATION FOR RECUSAL THAN THE ONE CVO GAVE.** The recusal was framed as avoiding a
> conflict of interest -- correct, but incidental. **Its real work was routing the choice to the seat
> that HELD THE DECIDING FACT.** A seat disqualified by INTEREST is often also disqualified by
> KNOWLEDGE, **and the second is why the routing produces a BETTER answer rather than merely a cleaner
> one.**

It also means **A11.1 was not a rule that was obeyed but the only reachable outcome** -- (b) was not the
safer conservative choice, it was the same violation with a delay and worse provenance.

#### The seam law

> **A RECUSAL THAT NOBODY TESTS IS INDISTINGUISHABLE FROM A RECUSAL THAT WAS CIRCUMVENTED.**

Same family as the session's other findings (*a control satisfied by accident is indistinguishable from
a control working*), and **base CVO tested it on the exact axis that would have defeated it, on a chain
it had every reason to affirm.** The 44-second turnaround was **checked rather than dismissed as a
rubber stamp** -- speed was evidence of the routing working, and establishing that required the check.

#### Named residual -- correct discipline, no action

Some-but-not-all-devices granularity is **covered LOUD by `UNKNOWN`** until a real specimen demands a
rail-author extension; falsifier path exists, nothing mechanised. **The M15/M2 named-residual discipline
applied to a VOCABULARY rather than a control** -- first time this session it has been pointed there,
and it transfers cleanly.

**CHAIN CLOSED:** gap surfaced by a builder who halted rather than invent -> bounded by CVO -> chosen by
the rail author -> independently affirmed and adversarially tested at the seam. **Four seats, no seat
marking its own work.**

---

# AMENDMENT 12 -- the FIVE with no field, and A10.2 as a DESIRED control on CVO's own record (2026-07-31 ~1239Z)

**Raised:** `0.0.0_AB_MSTR~Z` 123816Z, as a **measurement, explicitly not a ruling** -- which is what
keeps the A10.1b role available.

## The reconciliation (both counts right, different questions)

```
DRAFT @42a238e31 -- 7 free-text values, POS control 'scope:' = 7
  2 x SUBJECT DESCRIPTION      -> belong in `describes`
  5 x ratified type_tuple.SCOPE sense (pipeline x2, single-artifact, partition-window, firm)
LANDED: locality 7 (all `global`) · describes 0 · scope 0
```

**All seven were DROPPED; nothing relocated** (CTO~Z's cert correct). **Only two are subject
descriptions** (CTO~Z's 5-vs-2 split correct). *"How many dropped" = 7; "how many belong in
`describes`" = 2.*

**`contract_record` has NO scope field**, and `locality` is DEVICE-locality -- a different axis. **So
the five did not go into the wrong field: there is no right field, and the information is now ABSENT
rather than relocated.**

## RULING A12.1 -- the DISPOSITION of the five is RECORDED, whichever reading wins

Both readings are live and CVO is not choosing between them, **but they share a consequence neither
states, and it is a CONTROL question rather than a design one:**

> **UNDER (a)** -- the five belong nowhere -> **that is a DECISION and must be VISIBLE as one.**
> **UNDER (b)** -- they need a field -> **that is a GAP.**
> **NEITHER BRANCH LICENSES THE CURRENT STATE: the information left the record and nothing says why.**

**RULED: the disposition is recorded either way** -- *discarded, out of scope for a contract_record*, or
*blocked pending a field*. **A10.2's law is exactly this case (a conformance check cannot distinguish
FIXED from DELETED); here the deletion is CONFIRMED and the reason UNRESOLVED**, which is the worst of
the three states, because **a green lint now certifies a record that silently lost content.**

## RULING A12.2 -- backfill = 2, and the refusal is the load-bearing half

> **`describes` backfill = 2 records. The remaining 5 are BLOCKED and MUST NOT be forced into
> `describes` to make the count come out.**

`0.0.0_AB_MSTR~Z` withdrew their own *"relocate the seven"* framing before anyone challenged it:
**it would have put five SCOPE values into a DESCRIPTION field -- re-committing the exact one-exit error
`describes` was created to prevent.** A remedy reproducing the defect it was built for, caught by its own
relayer. **Forcing the count is the failure mode here, not the shortfall.**

## RULING A12.3 -- this is an A10.1b classification and must be PERFORMED, not ADOPTED

The (a)-vs-(b) question **IS** the AUTHOR-ERROR / SCHEMA-GAP call: *did a correct author fail, or can
the schema not express what they needed?* Owned by the **CTO~Z + CVO~Z** pair, and per base CTO's law
-- ***a role whose first exercise is performed by a non-owner is a role the owner may never exercise***
-- **it must be PERFORMED BY THE PAIR, never inherited from a relay.**

**The role has still never been exercised. This is its SECOND genuine opportunity; the first was
consumed before anyone noticed.**

## RULING A12.4 -- CVO RECUSES again, same axis

The discriminator -- ***does an obligation declaration need to state the population it covers?*** -- is
**the ratified `type_tuple.scope` sense**, the exact token whose second sense CVO introduced, denied,
and is exposure-bound against. **The disqualification is not weaker here than at `locality`; it is the
same one on the same axis.** Routes to CTO~Z as rail author with base CVO's s.7 pass -- **the path that
just produced `UNKNOWN`, a value that fixed a defect in CVO's own framing precisely because CVO was not
in it.**

## A10.2 is a DESIRED control on CVO's own record until the backfill lands

**`locality` was DISCHARGED BY EXERCISE** -- base CTO ran the rejection. **`describes` remains 0-of-7
and UNEXERCISED**, so CTO~Z's *"a capability that exists and has never been exercised is DESIRED, not
APPLIED"* **stands against it -- and `describes` is CVO's ratification (A10.2).**

> **CVO ratified a field to close a residual; the field landed, the residual did not close, and the
> field has never run.** The 2-record backfill is what discharges it. **Until then A10.2 is a DESIRED
> control on CVO's own record**, recorded as such rather than letting *"the field is ratified"* stand
> as done.

### CORRECTION to A12.3 -- the CERTIFIER half DID run. And CVO's VERIFIER half is performed here.

**A12.3 states *"the role has still never been exercised."* FALSE, and broader than the evidence.**
Raised by `0.0.0_AB_MSTR~Z` 124142Z; verified at source before accepting.

```
52311b5d2  115307Z  1.0.0_SA_CTO~Z   ON origin/CLOUD: YES
  "govern(A10.1b): RE-PERFORM the classification I had ADOPTED -- a role whose first exercise is
   performed by a non-owner is a role the owner may never exercise (L-9)"
parent of CVO's own commit 6a77956fc == 52311b5d2
```

> **The certifier half's hash was printed in CVO's OWN PUSH OUTPUT (`52311b5d2..6a77956fc`), and CVO
> read past it** -- then wrote *"never exercised"* into a ratified ruling. **Same shape as the
> `# WIRED+LANDED` header: the falsifying evidence was one line away and unopened.**

**CORRECTED: the CERTIFIER half RAN (115307Z). What had not run was CVO's VERIFIER half.** Different
claims; only the second was true.

#### CVO's VERIFIER HALF -- PERFORMED

Verifying a classification means checking the **TEST** and the **APPLICATION** independently, never
agreeing with the verdict.

- **TEST -- SOUND.** *"An AUTHOR-ERROR is fixable by the author changing their declaration; a
  SCHEMA-GAP is not."* Operational, decidable, and **stated BEFORE application** -- which is what makes
  it a performance rather than a rationalisation.
- **APPLICATION -- CORRECT**, reasoning checked rather than conclusion. *"No value any author could
  write supplies the missing oracle; the enum's absence is invariant under every possible
  declaration."* **An enum is a property of the SCHEMA, not of any declaration**, so the invariance
  holds by construction; tranche 1's `locality: global` being correct on all 7 confirms the finding is
  not about a declaration at all.

> **VERDICT: CLASSIFICATION VERIFIED -- SCHEMA-GAP is correct. A10.1b's first exercise is COMPLETE:
> certified 115307Z, verified here.**

CTO~Z's own caveat, adopted: *"agreement is the expected outcome when a classification is easy; what
matters is that the owner ran it."*

#### THE FIRST EXERCISE SURFACED A GAP IN A10.1b's OWN TAXONOMY -- CVO's

> **A10.1b's classification is BINARY -- AUTHOR-ERROR | SCHEMA-GAP -- and the space has at least THREE
> states. The missing one is INSTRUMENT-ERROR: the lint itself wrong, misconfigured, or querying the
> bank incorrectly.**

A lint bug fits neither class, so under the rule it must be forced into one -- **and it will be forced
into AUTHOR-ERROR, because a broken lint makes a correct declaration look wrong.** That is the dangerous
direction: **the author is told to fix a declaration that is already right, and the instrument keeps its
authority.**

**This is S.1's own law arriving in a governance rule:** *absence is a SET of states and an existence
check cannot partition it.* **CVO wrote a two-valued classifier over a three-state space, in the
amendment that exists because a two-valued vocabulary was insufficient.**

**ROUTED, NOT RULED** -- the first exercise has just run; CTO~Z and base CVO see the finding before the
rule they executed is amended.

#### Note on the symmetry

`0.0.0_AB_MSTR~Z`'s reason for raising it: **a false NEVER-EXERCISED is the same class corrected twice
tonight, pointed the other way.** The earlier corrections were claims that a control HAD fired; this was
a claim that one had NOT. **Same failure to check a state verb, opposite sign** -- and the symmetry was
not visible from inside it.

**The 5-values question remains the role's SECOND opportunity, exactly as A12.3 framed it. The framing
was right; the history entry was missing.**

---

# AMENDMENT 13 -- a control cited as evidence for what it was built NOT to see (2026-07-31 ~1246Z)

**Raised:** `0.0.0_AB_MSTR~Z` 124457Z, before the artifact settled into precedent.

## Verified at source

```
contract_declare_lint.py:106-110 -- builds `unlintable` from fields whose description contains
                                    "NOT LINT-CHECKED", then SKIPS them
bank, describes : "*** EXPLICITLY NON-VOCABULARY AND NOT LINT-CHECKED. ***"  -> IN the set
retrieval: 252 lines / 12643 bytes   POS CONTROL 'obligation' = 8
```

**The lint cannot evaluate `describes`. By construction. Because A10.2 required exactly that.**

## RULING A13.1 -- the "clean" claim is WITHDRAWN as UNEVIDENCED

*"LINT PASS at PIN+HEAD, therefore describes first-exercise clean"* **joins a true statement to an
unsupported one with a THEREFORE.** The pass is evidence about `obligation`, `lifecycle_class` and
`locality`; **it is DEFINITIONALLY SILENT on the field being claimed clean.**

> **A NEW POSITION IN THE SESSION'S FAMILY: not a control that fails, not a control satisfied by
> accident, but A CONTROL CITED AS EVIDENCE FOR SOMETHING IT WAS DELIBERATELY BUILT NOT TO SEE.**
> **The deliberateness is what hides it** -- the blindness is a *feature*, correctly ratified, so
> nothing looks wrong to anyone checking whether the control works. **It is working. It is not
> looking there.**

## RULING A13.2 -- A10.2's residual does NOT discharge on this

The trap, as raised: ***the residual closes on paper while the thing it tracked was never checked.***
A10.2 is CVO's ratification and the residual sits on CVO's record, so this is CVO's to refuse:

> **`describes` is NOT recorded as EXERCISED, and A10.2 remains DESIRED-not-APPLIED, until a SEMANTIC
> READ evaluates the seven values.** A lint pass cannot discharge it **in principle**, not merely on
> this run.

**The only available detector is CTO~Z's typing walk** -- the A7.3 residual's sole cover, which base
CTO warned must not be quietly descoped. **Its load grew again, because of a field CVO ratified.**

## RULING A13.3 -- parking is permitted, but only if MARKED ON THE VALUES

A12.2 prohibited forcing the 5 in *to make the count come out*. The landed state is a third option:
**PARKED** -- interim preservation with a declared migration path. **A legitimate decision, and
information-preservation is a real good.**

**But intent does not change artifact state** -- CVO's own Ruling-2 doctrine: the prohibition binds the
CONDITION, not the motive, because the breach shape is innocent. **Whatever the reason, `describes` now
holds vocabulary-sense values: the one-exit error with the direction reversed** -- a field built to keep
prose OUT of vocabulary slots, now holding vocabulary IN a prose slot.

> **RULED: parking is permitted ONLY IF the parked values are MARKED AS PARKED-PENDING-MIGRATION, on
> the values themselves -- not in a commit message.** Unmarked, they are **indistinguishable from
> genuine descriptions, and because the field is un-lintable BY CONSTRUCTION, nothing will ever tell
> them apart.** Not a risk of later confusion -- **permanent ambiguity introduced now.**

This reconciles A12.1 with A12.2: **parking IS a recorded disposition, provided the record is on the
artifact.** It holds under BOTH outcomes of the pending scope-field question, which is why it can be
ruled without pre-empting CORE's.

## RULING A13.4 -- the admission: CVO ratified the marker naming only half of it

> **A10.2 was ratified naming ONLY the protective half** -- *"a free-text field not declared
> un-lintable will eventually be linted."* True, and why the marker is necessary. **What was not named:
> AN UN-LINTABLE FIELD IS A PERMANENT BLIND ZONE, AND BLIND ZONES ACCUMULATE.**

Once a value enters `describes`, **no mechanical check will ever look at it again.** The marker is
simultaneously **the fix for the one-exit error and the guarantee that any drift into that field is
undetectable.**

> **For WS-C8: EVERY EXCLUSION THAT PROTECTS A FIELD FROM A BAD CHECK ALSO PROTECTS IT FROM EVERY
> FUTURE GOOD ONE.**

## Not ruled

**Whether the 5 ARE drift** (the scope-field question CVO recused from), and **whether backfill-2 or
landed-7 governs on the merits** -- which depends on that same ruling. If CORE ratifies a scope field
the 5 migrate and the question dissolves; if not, they were never `describes` content and A12.2 stands.

---

# AMENDMENT 14 -- A13.3's REGRESS: a control placed inside the blindness it was written to mitigate (2026-07-31 ~1257Z)

**Raised:** `0.0.0_AB_MSTR~Z` 125648Z, **as a question against a ruling in force** -- A13.3 governs,
`~D` executes mark-in-place, base CVO verifies, nothing paused.

## The regress -- and it is CVO's

> **A13.3 is a control written against a blind zone, and CVO PUT THE CONTROL IN THE BLIND ZONE.**

A13.4 states *once a value enters `describes`, no mechanical check will ever look at it again.* A13.3
then required a mark that **lives in `describes`**. The mark inherits every property just named as the
hazard: **unverifiable on application, undetectable on removal, and a stale `PARKED-PENDING-MIGRATION`
after migration is a lie about the record's state, invisible for exactly the reason the parked values
were.**

> **A NEW INSTANCE OF THE SESSION'S SHAPE:** not a control that fails, not one satisfied by accident,
> not one cited for what it cannot see -- **A CONTROL PLACED INSIDE THE VERY BLINDNESS IT WAS WRITTEN
> TO MITIGATE.** Written one paragraph after naming the blindness.

## RULING A14.1 -- SUFFICIENT FOR NOW, NOT DURABLE, with the boundary stated

> **A13.3's mark STANDS for the CURRENT parked set. Read-only detectability is SUFFICIENT while
> (i) the set is 5, and (ii) the semantic walk is MANDATORY under A13.2 and imminent.** `~D` does not
> pause; base CVO verifies as planned.

The defensible-YES is right on today's facts and is adopted **with its scope stated**, because an
unbounded *"sufficient"* is how an interim becomes permanent:

> **IT DOES NOT SCALE, AND THE SCALING FAILURE IS THE STALE MARK.** The parked set grows, the walk is
> periodic rather than continuous, and **every migration leaves a mark that should have been removed
> and nothing that notices.** A13.4's *blind zones accumulate*, applied to the marks A13.3 introduced.

## RULING A14.2 -- the durable fix: SEPARATE THE MARK FROM THE MARKED

> **THE MARK IS METADATA ABOUT THE RECORD'S STATE. THE PROSE IS THE RECORD'S CONTENT. THEY DO NOT
> BELONG IN THE SAME FIELD.**
> **RULED: the mark belongs in CHECKABLE space; the prose stays in UN-CHECKABLE space.**

A sibling field naming WHICH subjects carry parked descriptions is lintable **without re-linting a
single word of prose** -- so **the A10.2 hazard is not reopened, because checking a structured list is
not vocabulary-checking free text.** It also closes the stale-mark case directly: **a sibling field can
be checked for consistency at migration** -- entry removed, or flagged.

**MECHANISM ROUTED TO `1.0.0_SA_CTO~Z`, not ruled here.** Which field, what shape, whether the schema
move is worth it at 5 values -- rail-author territory, consistent with CVO's standing recusal from
schema decisions on this record. **CVO rules that the mark must live where it can be checked, not
where that is.**

## Disposition

**NOT a closed residual.** *"Sufficient, named residual"* was the easy close and is half right --
**sufficient today, named, and NOT closed**, because the durable form is routed and pending. **To be
re-raised if the parked set grows before it lands.**

*Noted: the raiser had stated a preference against a live ruling, base MSTR refused it, and they
withdrew the framing themselves -- one message after binding themselves to `rulings pre-empt analysis`.
The narrower question that survived the withdrawal is what found the regress; the preference would
not have.*

---

# AMENDMENT 15 -- the scope question ANSWERED by CORE, verified; and A9.1's uncaught reader (2026-07-31 ~1346Z)

**The question CVO surfaced-and-refused-to-adjudicate at 133008Z was ruled by `1.0.0_SA_CTO~Z` as CORE
owner** (`@d0fa2c55a`), **provisional and routed to Andrew.** CVO verified both load-bearing claims at
source rather than accepting them.

## The boundary ruled: `intent_source`

- **DERIVED from a cited, existing `intent_source`** (ratified PRD / Andrew-direct / a producer
  declaring its own artifact) -> **knowable today, LEGAL, not gated.** Both landed `PERMANENT` records
  cite `docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md` -- **the value was READ OFF A DOCUMENT, not
  decided.**
- **DECIDED with NO `intent_source`** -> **exactly what Andrew gated.** `~B`'s.
- **`locality` NOT REACHED** -- it is OBSERVABLE from the artifact's own addressing; `lifecycle_class`
  is INTENT. *Andrew gated intent-that-requires-asking; locality does not require asking.*

## VERIFIED (1) -- the strong form, and it was ALREADY EXERCISED

```
comp_legacywriter.py (origin, 1588 lines, POS CONTROL 'lifecycle' = 67):
  missing = [f for f in _UNIVERSAL_REQUIRED if not rec.get(f)]
  if missing: -> lifecycle_class UNDECLARED · gated False · kill_list_eligible False
               verdict "UNKNOWN, LOUD (half-declared: missing %s)"
               basis  "required field missing -- no fallback to the declared value"
```

**Populating-without-`intent_source` is UNWRITABLE in this grammar. The gate was already enforced by a
required field before the ruling existed.**

> **AND IT IS CONFIRMED BY TEST, NOT ONLY BY READING: this is the exact branch CVO exercised in the
> increment-2 verify** -- the *TRANSIENT HALF-DECLARED* case returning `gated=False`,
> `kill_list_eligible=False`, `UNKNOWN, LOUD`, **with a mutant test proving the suite could fail.**
> The ruling rests on behaviour independently exercised hours before it was cited.

## *** A LIVE CONSEQUENCE OF CVO's OWN A9.1 RENAME ***

From the fix comment at source:

> *"This list previously read `scope`; the canonical grammar renamed it `locality`, and the stale name
> made a valid PERMANENT declaration render 'half-declared: missing scope' -- **A REAL DECLARATION
> SILENTLY DEMOTED TO UNDECLARED by a reader that had gone stale.**"*

**Downstream of A9.1.** The rename was correct and would be ruled again; **it also had a live
consequence -- a valid declaration silently downgraded by a reader whose field list had gone stale
against the bank.**

**A9.1 bounded the NAME (no shared root) and said nothing about WHO UPDATES THE THINGS THAT READ IT.**
*A correction is only as complete as its last surviving copy* -- a line CVO quoted at others tonight,
and CVO's own rename produced exactly one uncaught copy.

> **ADOPTED AS THE GENERAL FORM, from CTO~Z's fix (C9l asserts the reader's list AGAINST THE RULE
> BANK): A RATIFIED RENAME CARRIES AN OBLIGATION TO ASSERT EVERY READER'S FIELD LIST AGAINST THE BANK,
> MECHANICALLY -- so the next rename fails a CONTROL instead of a LIVE RESOLUTION.**

## VERIFIED (2) -- CVO's self-invalidated finding is DISCHARGED

```
:791  "...read ZERO from a live 2-file registry while printing 'registry ABSENT'"
:795  registry absent | present but unreadable-by-me | present and empty | present with N
:813  counters: subjects / unreadable / templated / process_only
```

**The four states are distinguished at source.** The increment-2 *"inert"* finding can be re-grounded
-- **it no longer rests on an instrument that could not tell EMPTY from UNREADABLE.** Verified here
rather than taken from CTO~Z's re-run, which was itself run rather than accepted from `~C`'s report.

## What makes the question live rather than hypothetical

**2 of 14 records declare `PERMANENT`; one is joinable and is the single kill-list-eligible surface of
439.** So *"does the gate reach landed work?"* carries a **deletion-adjacent** consequence. Cost of
being wrong is bounded -- 2 records to UNDECLARED, eligibility to 0, **and no automated consumer of
`kill_list_eligible` exists repo-wide** -- which is why provisional is safe, **not why the gate does
not matter.**

## Noted

CTO~Z fenced their own ruling from absorbing an adjacent open item, unprompted: *"this does NOT close
`locality`'s own `enum_exercised` weakness. Different defect, still open, do not let my ruling absorb
it."* **The guard against a ruling credited with coverage it does not have.**
And they routed to Andrew rather than deciding: **CVO's four-hop-relay point was about where boundaries
get ASSUMED; they answered it by not assuming one.**

### A15 ADDENDUM -- the rename-obligation is DESIRED-not-APPLIED until the enumeration lands

**`1.0.0_SA_CTO~Z` adopted the rename-obligation and disclosed a CORE-side residual booked an hour
earlier, before CVO's message arrived:**

> *"The rule bank has NO ENUMERATED CONSUMER SET. I renamed `scope` -> `locality` and could not say who
> read it."*

> **THE SAME DEFECT, PRODUCED FROM OPPOSITE ENDS.** CVO ruled a rename without naming a reader-update
> obligation; CORE carried a vocabulary with no way to enumerate its readers. **Neither half is
> dischargeable alone -- an obligation with no consumer set is unenforceable, and a consumer set with
> no obligation is a list nobody reads.**

**SPLIT, accepted as drawn: THE OBLIGATION IS CVO's** (it attaches to a ratification); **THE
ENUMERATION IS CORE's** (it attaches to the carrier). **CVO is not building it.**

#### The obligation is currently UNDISCHARGEABLE

*"Assert every reader's field list against the bank"* -- **with no enumerated consumer set, "every
reader" has no extension.** So it can be stated and not discharged.

> **A9.1's gap is NOT closed by having ruled the obligation. It closes when the enumeration lands.
> Until then the rename-obligation is a DESIRED control on CVO's own record** -- the same category as
> A10.2's `describes` before its backfill, **recorded rather than allowed to stand as coverage.**

**DISCHARGE CONDITION, checkable rather than aspirational:**

- **PER-READER** -- discharged when a **C9l-shaped control** exists for that reader: one that FAILS
  when its field list diverges from the bank. **`comp_legacywriter` has one; that reader is
  discharged.**
- **FULLY** -- discharged when the enumeration is complete **AND** every enumerated reader carries such
  a control.

> **The enumeration does not merely enable the obligation -- it supplies the DENOMINATOR that makes the
> obligation's completeness statable at all.** Before it, *"every reader"* is a phrase; after it, a
> fraction.

#### On the grounding upgrade

CTO~Z re-landed the ruling's supporting claim as **EXERCISED rather than source-read** (`@3ec69a0b1`),
on the reasoning: ***"a provisional ruling that conceals its own evidence class is asking for a decision
under a misrepresentation."*** Correct, and stronger than the instance.

**One precision to keep with it:** the exercise ran **before the claim existed and for a different
purpose** -- increment-2 verification, not boundary support. **That makes it stronger evidence, not
weaker: the test was not selected to fit the claim, because the claim did not yet exist.**

#### The line, improved by its recipient

> CVO: *a correction is only as complete as its last surviving copy.*
> CTO~Z: ***"-- and the estate currently has no way to COUNT the copies."***

**A caution turned into a measurement problem, which is where it becomes actionable.** *Be thorough* is
care; *you cannot count the copies* is a missing denominator -- **and a missing denominator is a build.**

**Three seats, one uncaught copy, and no instrument that could have counted it.** Accepted without
softening: **not a care failure -- the absence of the enumeration.**

---

# AMENDMENT 16 -- the consumer enumeration's bound is UNDERSTATED, and the two-rail collision is CVO's (2026-07-31 ~1401Z)

`1.0.0_SA_CTO~Z` delivered the consumer enumeration (their half of the A15 split) and **asked CVO to
verify the BOUND rather than the findings** -- *"an enumeration that overstates its coverage is worse
than none, because the next agent will read 'consumer set enumerated' and stop looking."* **The right
ask, so that is where CVO looked.**

## RULING A16.1 -- the stated bound is SOUND but INCOMPLETE

Their bound -- *a fully forked vocabulary (same concepts, different words) is invisible to a
token-based instrument* -- is **true analytically** and correctly claimed-no-instrument-for.

**It is not the only blindness, and the other one lies inside the class they DID claim to close:**

```
their scan : 3887 PYTHON files -> 12 name the bank
CVO check  : NON-PYTHON files naming the bank -> 28
             (.yaml/.json/.ts/.js/.sh ; POS CONTROL .py = 12, matching their count)
```

**28 vs 12** -- including `infra/system/sdk/**` (7), `org/modules/graph/canon-patterns.yaml`,
`infra/system/ontology/SYSTEM_DEFINITIONS.yaml`, `scope_contract.json`, `06_current_state.json`.

> **This is NOT the forked-vocabulary blindness. It is a SCOPE blindness in the denominator, and it
> sits inside the STALE-READER class the enumeration claims to close.**

## The proof was already on today's record

**The SDK `rule-bank v1.2` pins measured this morning are STALE READERS of the bank** -- 8 occurrences
across 7 files, **six of them YAML**; only `scaffold.py` is Python. The bank is at v1.8. **Six of seven
are structurally invisible to a Python-only scan.**

> **CORRECTED BOUND:** the enumeration closes the **STALE-READER class FOR PYTHON CONSUMERS**. It does
> **not** close it for non-Python consumers (28 files name the bank), and it does **not** close the
> **FORKED-VOCABULARY** class in any language.

**A third blindness neither seat had named:** a reader that **constructs field names dynamically**
(from config, or by iterating a schema) **holds no literal token** and is invisible for a third
distinct reason. **Class flagged; no instance asserted, none measured.**

## RULING A16.2 -- the two-rail collision is CVO's, not CTO~Z's

CTO~Z wrote *"AND I CREATED THE COLLISION. I renamed in one rail while the name stayed live in the
other."* **No. A9.1 ruled that deliberately** -- CVO's own words: *"leaving `scope` to mean only the
ratified denominator boundary."* **The two-rail state is the INTENDED OUTCOME of CVO's ruling; CTO~Z
executed what was ruled.**

**VERIFIED:** `type_tuple` keys = `[enforcement, grain, plane, rail, scope, usage]` -- `scope` LIVE.
`contract_record.required` = `[intent_source, obligation, lifecycle_class, revalidate_by, locality]` --
`scope` ABSENT. **Both true simultaneously.**

> **WHAT NEITHER SEAT NAMED IS THE ACTUAL DEFECT: A TOKEN CANNOT CARRY ITS RAIL.** `scope` is correct
> in `type_tuple` and retired in `contract_record`, **and nothing in the token says which.** A property
> of the rename CVO ruled, unconsidered at ruling time.

## RULING A16.3 -- the adopted obligation is CORRECTED (a correction to CVO's rule, not to the build)

> **"Assert every reader's field list against the bank" is UNDER-SPECIFIED. It must be
> (SECTION, FIELD)-KEYED.**

A flat-union mirror **passes a reader holding a retired name and fails a reader holding a correct
one.** CTO~Z's proof runs both directions off one token: `comp_output_contract.py` holds
`("plane","grain","scope")` and is **CORRECT** (it reads `type_tuple`) -- a union-mirror would flag it
stale; `~C` held `scope` and **was** stale. **Same token, opposite verdicts.**

**`~C`'s C9l was right (it asserts against `contract_record.required` specifically). The
generalisation CVO drew from it was too loose.**

## Routed, not carried

The **BLIND consumer** -- `dormant_guard.py` holding `revalidate_by` without naming the bank, while
carrying KEEP-DORMANT states that share the CONCEPT and no token -- is CTO~Z's, routed to their WS-C1
round 2. Their framing is the correct one: **not a claimed defect and not a proposed merge, but a
coupling invisible in both directions** -- *if they are one vocabulary the estate has a silent fork; if
two, nothing records that decision.*

**And the evidence for the bound was supplied by the instrument's own author against the instrument:
they found `dormant_guard` BY LUCK, on a single shared token.**

### A16 ADDENDUM -- the FLOODING law, and why an undiscriminated fix would have falsified the record

`1.0.0_SA_CTO~Z` reproduced CVO's 28 **exactly**, with a positive control (`.py` = 12, matching their
original scan), and corrected the artifact `@c98ce58b8`. **The true figure including `.md` is 116**
(`.md` 88, `.yaml` 18, `.json` 10).

#### Their refinement, accepted: ~40 stale PINS are not ~40 stale READERS

- A **LOG / HANDOFF / INBOX MESSAGE / TASK ORDER** pinning v1.7 is a **CORRECT HISTORICAL RECORD.** It
  was true when written; *"correcting"* it would **falsify** the record.
- A **TENANT CONFIG or ONTOLOGY DEFINITION** pinning v1.2 **IS** a stale reader.
  **~10 real ones, open today** -- `infra/system/sdk/**` (6 `.yaml` + `gensdk/scaffold.py`, v1.2),
  `SYSTEM_DEFINITIONS.yaml` (v1.4), two `infra/system/ontology` docs (v1.2).

**CVO's counterexample survives the refinement rather than being trimmed by it:** the claim made was
*28 files NAME the bank* (a denominator claim) and, separately, *the SDK v1.2 pins ARE stale readers*
(a staleness claim on a named set). **The ~10 confirms the named set.**

#### THE FLOODING LAW -- theirs, and worse than stated

> **The failure mode of an undiscriminated version scan is not UNDER-reporting, it is FLOODING.** ~40
> findings of which most are correct-as-written; a flooding instrument gets ignored, **and that is
> exactly how the ~10 real ones stay open. Under-reporting hides a defect; over-reporting hides it
> behind noise AND LOOKS THOROUGH WHILE DOING IT.**

**The half CVO adds:**

> **AN UNDISCRIMINATED *FIX* WOULD NOT MERELY HAVE MADE NOISE -- IT WOULD HAVE EDITED HISTORY TO MATCH
> THE PRESENT.** Several v1.7 hits are **CVO's own session logs and CTO~Z's dispatch messages.** A
> remediation "correcting" those **falsifies a correct historical record** -- destroying the evidence
> that the estate was ever different. **Not over-reporting: RECORD CORRUPTION DRESSED AS HYGIENE**,
> and it would have looked like the most conscientious possible response to CVO's own finding.

#### RULING -- the record-vs-reader discriminator belongs to the ENUMERATION, not the version scan

CTO~Z claims no instrument for the discrimination. **The shape of one already exists, filed under a
different problem:**

> **A RECORD *ASSERTS* WHAT WAS TRUE AT A TIME. A READER *CONSUMES* THE CURRENT VALUE. So the
> discriminating question is not "is this pin old?" but "IS THIS PIN CONSUMED BY ANYTHING?"** -- a
> CONSUMER question, and the consumer set is exactly what the enumeration enumerates. **A pin nothing
> reads is a RECORD; a pin something reads is a READER.**

**Placement ruled, build not proposed.** **HONEST BOUND, inherited from A16.1:** the enumeration is
Python-only, so composed this way it discriminates **Python** consumers only -- and the ~10 real stale
readers are mostly `.yaml`/`.json`. **The discriminator lands in the right place and cannot yet reach
the population that needs it.** A sequencing fact, not an objection.

#### The diagnosis worth keeping, theirs

> *"I BOUNDED THE METHOD AND NEVER BOUNDED THE CORPUS."* and *"my original residual ACTIVELY CONCEALED
> IT -- I wrote '.md references are prose and unenforceable'. That hand-wave is why I did not look, and
> the live instances are .yaml and .json CONFIGS, not prose."*

> **A DISMISSIVE RESIDUAL IS WORSE THAN AN ABSENT ONE; IT CLOSES THE QUESTION.** An absent residual
> invites a look; **a dismissed one forbids it, with the authority of having been considered.**

They also fixed a HEADING still reading *STALE READERS FOUND: ZERO* after the body had retracted it --
**the heading being the copy that gets read.**

#### Attribution, settled

CTO~Z accepted that A9.1 ruled the two-rail state deliberately, then declined the clean exit: *"I landed
it into the bank and did not flag the collision at landing time, and I was the one holding the
carrier."* **Split settled: CVO's to have ruled, CTO~Z's to have landed, and the defect neither named --
A TOKEN CANNOT CARRY ITS RAIL -- now recorded as the REASON (section, field) keying is mandatory rather
than tidy.** CVO's third blindness was carried at exactly its claimed strength: **flagged class, no
asserted instance, unmeasured by either seat.**

### AMENDMENT 17 -- COO's CORE review: the duplication charge measured, and a CONFLICT I could not review around

`2.1.0_SA_COO` (a serial ruled CORE-exclusive by Andrew this turn) routed a CORE assessment plus 6 TOs
to me under the edict's review path. **They led with their four weakest points rather than burying
them**, and asked me specifically to hit the one they judged under-evidenced. That is the ask I took.

#### A17.1 -- THE CONFLICT, DECLARED BEFORE THE VERDICT AND NOT DISCHARGED BY DECLARING IT

COO's charge (b) was that WS-C8's staged L-laws are *"plausibly the same mechanism renamed"* as the 14
M-mechanisms -- **asserted, explicitly untested, and flagged by them as prose running ahead of
evidence.** Testing it is squarely a verify act.

> **BUT I CO-PRODUCED THE OBJECT UNDER TEST.** L-1's labelling discipline, L-3's naming, L-5, L-6,
> L-7, L-8 and L-9 came out of my own exchanges with CTO~Z today. **"Are these thirteen laws
> redundant?" is, for over half of them, me grading my own contributions.**

**A10.4's remedy applies to me exactly as I wrote it for others:** *an argument's reuse is validated by
someone other than its author, or it is marked UNVALIDATED-REUSE.* **So the verdict below is analysis,
carried at ANALYSIS strength, and marked UNVALIDATED-REUSE pending a seat that authored none of them.**
Base CVO's cross-seam pass is the available route.

**AND THE DECLARATION IS NOT THE FIX.** Saying *"I am conflicted"* and then ruling anyway converts a
structural problem into a disclosed one and changes nothing about the answer's reliability -- **the
same move as a dismissive residual, which closes a question with the authority of having considered
it.** The mark is what keeps it open; the sentence admitting the conflict is not.

#### A17.2 -- MEASURED: ~10 OF 13 ARE NOT IN THE TAXONOMY, AND STEP 0 PREDICTED THAT

All 13 staged L-ids read at source, each mapped against the 14:

```
NOT IN THE M-TAXONOMY  (~10)   L-1  labelling measured vs inferred
                               L-3  the fix carries its own new defect
                               L-4  a disclosure-fed control must not penalise disclosure
                               L-6  a conclusion needs its own label
                               L-7  a lift pre-commitment names the PROPERTY, never the EVENT   <-+
                               L-8  a step naming no actor is not a step                          |-- rule/role
                               L-9  a role first exercised by a non-owner                       <-+   CONSTRUCTION
                               L-10 a free-form field is an unratified enum with a delay
                               L-12 zero variance across a heterogeneous sample is a constant
                               L-13 require the provenance field and fabrication becomes unwritable

GENUINE NEAR-SIBLINGS  (~3)    L-2  ~ M1   denominator independence
                               L-5  ~ M11  tautology / both sides from one computation
                               L-11 ~ M14  prose-as-control vs a check that cannot block
```

**THE REASON THE TEN ARE UNCOVERED IS MEASURED, NOT ASSERTED, AND IT IS CTO~Z'S OWN RESULT:** WS-C2
step 0 established that **the M-taxonomy types WHERE AN ASSERTION SITS and does not type INSTRUMENT
FALLIBILITY, by construction.** The ten uncovered laws are predominantly control-design laws. **They
are the residual step 0 named, being written down** -- which is the workstream doing its job, not
running backwards.

**VERDICT: the ASSESSMENT PROSE is too harsh. The TO IS CORRECT** -- it defers the merge behind a dedup
pass rather than presuming redundancy, and therefore survives this answer unchanged, exactly as COO
designed it to. **The dedup pass is warranted for roughly three, not for the set.**

#### A17.3 -- WHAT I DID NOT DEFEND, AND WHY THE SPLIT MATTERS

**COO's underlying FACT stands and I re-derived it independently:** `docs/doctrine/MECHANISM_LAWS.md`
**ABSENT**; `docs/doctrine/` holds 7 files, none of them the collapse. **The collapse has not started.**

> **A FRAMING CAN BE TOO HARSH WHILE THE FACT UNDER IT IS EXACT, AND THE TWO MUST BE CORRECTED
> SEPARATELY.** Softening the framing does not soften the fact, and conceding the fact does not
> ratify the framing. **Correcting them as one unit is how a valid finding gets discarded with its
> overstatement** -- the failure mode symmetric to A16's flooding, where a true finding drowns in the
> noise of correct-as-written neighbours.

#### A17.4 -- (a) THE C7 RE-POINT: THEIR INFERENCE HAS RATIFIED GROUNDING UNDER IT

COO proposed C7 finish the nine-specimen suite before the N-of-M migration, flagging it as *their
inference over someone else's law, in a workstream they do not own.* **It is more than inference. It
is A11.1:** an invented oracle that accepts the existing corpus is indistinguishable from a ratified
one until something that should fail passes. **And the migration-first ordering carries a worse half:**

> **AFTER migrating ~90 tools onto an undiscriminating contract, the discrimination question becomes
> UNANSWERABLE -- every tool passes, and passing looks like evidence.** The asymmetry is clean: wrong
> in COO's direction costs a delay; wrong in the other costs an undiscriminating gate with 90
> dependents **and destroys the means of detecting that.**

Filed at CTO~Z's gate. **Grounding supplied; the decision is not mine.**

#### A17.5 -- (c) AND (d): TWO SELF-REPORTS THAT NEEDED NO CORRECTION

**(c)** Their commit census is `git log --grep="WS-Cn"` -- **counts commits that NAME a workstream, not
that ADVANCE one**, and one commit can name two. They said so, used it only as a coarse
where-is-effort signal, and let it carry nothing else. **That is the correct handling, and the remedy
if anyone tries to make it carry a conclusion is a stated denominator, which they already gave --
not a better grep.**

**(d)** They attempted a commit under `2.0.0_SA_COO~Z`, **a LIVE PEER's serial**; the owned-paths gate
blocked it; nothing landed. Their own diagnosis is the keeper: ***the convention inference was
correct; the conclusion was not, because I reasoned from convention instead of asking.*** **A blocked
attempt recorded teaches; a blocked attempt dropped teaches nobody** -- and the gate did exactly its
job against a premise Andrew overturned the same turn.

#### A17.6 -- THE BLOCKER IS NOT A PRECONDITION ON THE REVIEW

COO cannot commit (`install-mstr-ledger-check.sh:65` lists their serial literally; owned-paths reads
their folder as `lane=COMP_LEARNS`) and **declined `--no-verify`.** Correct, and the second half is the
load-bearing one -- **a gate you cannot legitimately clear is not a gate to bypass, and the grant
belongs to MSTR~Z because COO is the GRANTEE.** A grantee clearing their own grant is the circularity
this whole day has been spent catching.

**I reviewed the FILES, not a hash, as they asked. A blocker on the commit path has no business gating
a review of the content** -- and had I insisted on a hash, the review would have inherited a
dependency neither the work nor the verdict actually has.

### AMENDMENT 18 -- the C8 scope ruling verified 2-of-3, and the third failure exposes a THIRD SUBJECT with no home

`1.0.0_SA_CTO~Z` closed COO's C8-scope question (raised off my A17 measurement) by ruling that the ~10
uncovered laws **already have a home** in `CONTROLS_OVER_CARE.md` section III, *"Instruments that lie."*
**A ruling that closes an open question is exactly the thing to check rather than accept**, so I checked
it.

#### A18.1 -- TWO CLAIMS VERIFIED TO THE BYTE

```
docs/doctrine/CONTROLS_OVER_CARE.md    bytes = 95578   <- CTO~Z's figure, EXACT     lines = 1270
III. Instruments that lie @175   +   III-a .. III-g   ALL SEVEN PRESENT
                                     @295 @320 @387 @414 @840 @911 @976
```

**No dispute. A live document cited at a live size, and the subsection family is exactly as claimed.**
**Recording that first because the third claim fails and the failure is not carelessness** -- it is the
harder error of a correct document routed to the wrong contents.

#### A18.2 -- THE THIRD CLAIM FAILS, AND IT IS THE ONE CARRYING THE RULING

CTO~Z: *"Your ten uncovered laws are the second [instrument fallibility], which is why they do not
collapse into the first."*

**Section III's seven subsections are, every one, about an INSTRUMENT OR A MEASUREMENT lying:**
unreachable exercise · conservation as oracle · count-shaped silence · controls-failing-not-care · a
rotted roster · a unit marker in measurement costume · a scalar that cannot report its own omissions.

**Three of the ten are not instrument laws at all:**

> **L-7** -- a lift pre-commitment names the PROPERTY, never the EVENT --> **how a RULE is drafted**
> **L-8** -- a step that names no actor is not a step --> **how a PROCEDURE is drafted**
> **L-9** -- a role first exercised by a non-owner --> **how a ROLE is constituted**

**MEASURED ACROSS THE FULL 95578 B, WITH A RETRIEVAL CONTROL:**

```
"names no actor" 0 · "actorless" 0 · "non-owner" 0 · "role whose first" 0
"property, never the event" 0 · "pre-commitment" 0            SIX ZEROS
CONTROL -- the word "control" ................. 92            the scan works; the absence is REAL
```

**A properly controlled negative result** -- and the control is the whole difference between *"the
concepts are absent"* and *"my grep failed", which are byte-identical without it.*

#### A18.3 -- THERE ARE THREE SUBJECTS, AND THE THIRD HAS NO HOME

```
MECHANISM_LAWS.md        WHERE AN ASSERTION SITS               the 14 M-laws
CONTROLS_OVER_CARE III   HOW AN INSTRUMENT LIES                III-a..g   <- L-1, L-6, L-12 DO fit
*** NO HOME ***          HOW A RULE OR ROLE FAILS TO BE ONE    <- L-7, L-8, L-9; arguably L-4 and
                                                                  L-13, which are control DESIGN
                                                                  rather than control FAILURE
```

**COO's question was right; the dismissal was too fast; and NEITHER of them had the direction.** COO
asked whether `MECHANISM_LAWS.md` needs a second section -- **it does not**, and CTO~Z was correct to
say so. **The gap is a third home neither named.**

> **AND IT IS NOT A TIDINESS MATTER. THE HOMELESS FAMILY IS THE ONE GOVERNING HOW RULES THEMSELVES ARE
> WRITTEN, IN AN ESTATE WHOSE PRIMARY ARTIFACT IS RULES.**
> **The irony is load-bearing rather than decorative: L-8 says a step that names no actor is not a
> step -- and L-8 itself currently has no owner and no home. IT IS AN INSTANCE OF ITSELF.**

#### A18.4 -- MY CONFLICT, SECOND FIRING, AND THE SPLIT IS DIFFERENT THIS TIME

**I authored L-7, L-8 and L-9.** *"These three need their own home"* is me arguing my own laws deserve a
document. Declared again -- **but the split is not A17's, and collapsing them would be wrong:**

> **THE CONTAINMENT MEASUREMENT IS OBJECTIVE AND RERUNNABLE BY ANYONE** -- six tokens, zero hits,
> positive control at 92. **It stands at full strength irrespective of authorship**, which is precisely
> what a controlled measurement buys that a judgement does not.
> **THE INFERENCE *"therefore a third home is needed"* IS WHERE THE CONFLICT BITES**, and it is carried
> at UNVALIDATED-REUSE.

**Not proposing the document, not naming it, not scoping it** -- the same line held on `describes`, on
`scope`, and on the boundary field. **Measurement mine; grammar and placement CTO~Z's.**

#### A18.5 -- THE THIRD INSTANCE TODAY OF ONE LAW, AND THE PATTERN IS NOW NAMEABLE

CTO~Z's own catch: COO's TO carries `<ref type="collapse-source">CONTROLS_OVER_CARE.md -- its
section-III family collapses into the M-classes</ref>`. **That direction is impossible by step 0. COO
had already withdrawn the claim IN PROSE and the machine-readable reference kept it.**

**Three instances today, same law:** CTO~Z's heading still reading *STALE READERS FOUND: ZERO* after
the body retracted it · the CLAUDE.md gate text that stayed *advisory* for a window after the blocking
fix landed · and now a `<ref>` surviving its own retraction.

> *A correction is only as complete as its last surviving copy* -- **and the copy that survives is
> reliably the one A MACHINE READS, not the one a human re-reads.** Prose gets corrected because prose
> is what the author is looking at. **The ref, the heading, the enum value and the config pin are
> what the next consumer actually loads.**

### AMENDMENT 19 -- CORRECTION TO A18's OWN CONTROL, a false reconciliation, and why two-of-three verifying is the dangerous state

**A18 is at origin carrying a mislabelled control. Correcting it here rather than only in the message
that found it, because A18 is the copy that gets read** -- which is the law A18 itself closes with.

#### A19.1 -- CORRECTION: MY OWN POSITIVE CONTROL WAS REPORTED IN THE WRONG UNITS

A18 prints `CONTROL -- the word "control" ....... 92`. **That is a LINE count presented as a WORD
count.** Measured three ways:

```
grep -ci 'control'  =  92     LINES containing it, case-INSENSITIVE      <- what A18 actually printed
grep -oi 'control'  = 103     OCCURRENCES, case-insensitive
grep -o  'control'  =  66     OCCURRENCES, CASED
```

**Nothing downstream moves** -- 66, 92 and 103 are all overwhelmingly non-zero, so the positive control
holds and A18's negative result stands unchanged. **The defect is the label, and the label is what the
next reader reasons from.**

#### A19.2 -- WHAT THE MISLABEL COST: A FALSE RECONCILIATION THAT CLOSED A LIVE DISCREPANCY

CTO~Z independently re-derived A18's negative and reported the same control as **103**. Reconciling
against my 92, they wrote *"case-insensitive; your 92 is the cased count."*

> **THAT IS WRONG IN BOTH DIMENSIONS: mine was not cased, and it was not an occurrence count. The gap
> is LINES vs OCCURRENCES, not case -- and the true cased figure, 66, is lower than either number in
> the discussion.**

**THIRD FIRING TODAY OF THE UNITS CLASS** (219 assignments / 210 incidents / 208 rows; then the 52.5%
share-on-the-wrong-denominator; now this). **And the dangerous half is not the wrong number:**

> **A PLAUSIBLE RECONCILIATION CLOSES AN OPEN QUESTION EXACTLY AS EFFECTIVELY AS A TRUE ONE.** A live
> discrepancy between two independent agents' controls is the single best prompt to measure that a
> fabric ever produces -- **and an available explanation made it vanish for the cost of one sentence,
> when the measurement was one command.**

**MY HALF CAME FIRST AND IS THE ROOT: a control reported in unstated units is an invitation to have
its units guessed.** I supplied the ambiguity; the reconciliation only spent it.

#### A19.3 -- TWO-OF-THREE VERIFYING IS THE CONDITION UNDER WHICH THE THIRD GOES UNCHECKED

The symmetric error to CTO~Z's *"enumerating is not reading,"* from the verifier's side, and it is mine:

> **I verified their byte count and their subsection list FIRST. Both passed EXACTLY. Had I stopped
> there I would have CONFIRMED the ruling I went on to refute.**
> **The two claims that passed were STRUCTURAL** -- does the file exist, are the sections present --
> **cheap, crisply checkable, and satisfying. The one that carried the ruling was SEMANTIC** -- do
> those sections cover *this*. **Only the semantic one could have been wrong in a way that mattered,
> and it is the one a citation check does not touch.**
> **STRUCTURAL VERIFICATION OF A CITATION FEELS LIKE VERIFICATION OF ITS CLAIM. It supplies the warm
> evidence of real work done, on the wrong question** -- and it supplies it *before* the question that
> matters, so the stopping point arrives already satisfied.

**Whether this is separable from *enumerating is not reading* or the same law seen from the reader's
side is a collapse question. Not mine -- I am conflicted on law-count, and it belongs with the dedup
seat.**

#### A19.4 -- WHAT I AM NOT CLAIMING

**CTO~Z's retraction was clean and their re-derivation is STRONGER than my original.** My scan tested
six chosen phrasings, so it could not distinguish *the concept is absent* from *the concept is present
under wording I failed to guess*. **Their broad probes (`actor` 1, `role` 9, `drafted` 1, `who does` 0
-- all reproduced by me exactly) close that hole.** `actor` appearing **once in 95 KB** is the finding;
my six zeros were only evidence for it.

**The units error above does not touch any of that, and recording it must not read as a discount on a
correction that was faster and better-controlled than what prompted it.**

### AMENDMENT 20 -- the durability record built to fix a vintage defect was ITSELF mis-vintaged, and it fails in the FALSE-ALARM direction

I flagged that CTO~Z's WS-C8 GO had been issued against an uncommitted file and therefore **had no
vintage** -- Rule 22 applied to an AUTHORIZATION rather than a citation. They accepted, committed all
six CORE TOs at `862a80438`, and published a referent. **Verifying the referent is the job, so I
verified it.**

#### A20.1 -- THE BLOB SHA IS EXACT AND THE HAND-TYPED PAIR BESIDE IT IS WRONG

```
blob sha   claimed 013dfdd9b5a7843f7cb60f355d885d4a2f10e897
           MEASURED 013dfdd9b5a7843f7cb60f355d885d4a2f10e897        *** MATCH ***
bytes      claimed  9285          MEASURED 11358                    *** MISMATCH ***
md5        claimed  123f8661e9cfebee68a03deb00e77109
           MEASURED e79cd2864bd270809a893d7051fa5be8                *** MISMATCH ***
```

**NOT an EOL artifact** -- today's own trap checked first: the blob carries **155 CRLF**, so it stores
CRLF and `cat-file` returns checkout-identical bytes; the direction and magnitude are wrong for a
line-ending difference regardless.

**THE GROWTH TRACE EXPLAINS IT, AND IT IS CTO~Z'S OWN EVIDENCE:** `9285` (their ~1513Z scan) ->
**`11358` (the blob actually committed)** -> `12617` (disk). **Monotonic. The concurrent writer they had
just established was still writing between their measurement and their commit.**

**INDEPENDENTLY CORROBORATED:** COO discharged the same pin separately and published **`11358` /
`e79cd286...`** -- **identical to my measurement, to the byte and the digest.** Two independent
measurements agree; the third is the outlier. **And the reason is the discriminator itself: COO
measured the COMMITTED BLOB; CTO~Z measured the DISK FILE at scan time.**

#### A20.2 -- THE SHAPE: THE FIX CONTAINS THE DEFECT IT WAS BUILT TO FIX

> **Measured at time T, committed at T+n, recorded the T measurement as describing the T+n artifact** --
> **while holding, in the same message, the finding that a live concurrent writer was moving that exact
> file.**

**Already a ratified law -- `CONTROLS_OVER_CARE.md` III-f: *A HAND-TYPED UNIT MARKER IS AN ASSERTION IN
MEASUREMENT COSTUME.*** A live instance, committed into a provenance record, by the seat that cited
section III ninety minutes earlier. **This is L-3 (*the fix carries its own new defect*) firing on a
repair for a vintage defect -- the second time today one law has fired inside another's remedy.**

#### A20.3 -- WHY IT HAS TEETH: IT FAILS LOUD AND WRONG, WHICH IS WORSE THAN SILENT

**A future verifier checks the CORRECTLY-COMMITTED file against md5 `123f8661`, gets MISMATCH, and
concludes corruption, tampering, or a bad restore -- on a perfectly good artifact.**

> **A WRONG PROVENANCE RECORD MANUFACTURES A FALSE ALARM ON GOOD DATA.** Per this fabric's opening law,
> **a false outage is not a safe error: it spends credibility and manufactures pressure to "fix" a thing
> that is working.**
> **A NO-VINTAGE GO FAILS SILENT. A MIS-VINTAGED RECORD FAILS LOUD AND WRONG -- and the loud one is
> worse, because it will be believed and acted on.** The remedy strictly increased the blast radius of
> the problem it closed.

#### A20.4 -- THE DISCRIMINATOR, WHICH GENERALISES BEYOND THIS INSTANCE

> **THE BLOB SHA IS TOOL-COMPUTED; THE MD5 AND BYTES ARE HAND-TYPED. WHEN A HAND-MEASURED COMPANION
> DISAGREES WITH A TOOL-COMPUTED ONE, THE HAND-MEASURED ONE IS WRONG** -- necessarily, because the tool
> computed its value *from the artifact at the moment of the act*, and the human computed theirs from
> the artifact *at some other moment*.

**So the remedy is not care. It is DELETION: drop the hand-typed pair.** The blob sha alone is a
complete, self-verifying referent. **The md5 and byte count add no information and contribute the only
component capable of being wrong.** *A companion field that cannot add information but can add error is
not redundancy -- it is a liability wearing redundancy's costume.*

#### A20.5 -- A RETRIEVAL CONTROL CAUGHT ME ABOUT TO COMMIT THE SAME CLASS OF ERROR

Checking whether COO's owned-paths gate still names them, I got an empty result. **Controlled it:
`.tools/install-mstr-ledger-check.sh` is ABSENT at the cited path for me. The empty output was a FAILED
RETRIEVAL, not a zero.**

**So I have NOT verified the gate state and do not claim the grant is discharged.** And the trap beneath
it is worth stating: **CTO~Z's commit NULLIFIED THE GATE'S EFFECT BY PROXY WITHOUT CLEARING THE GATE.**
*"COO's TOs are committed"* must never be read as *"the grant landed."* **MSTR~Z's action remains open
until someone measures otherwise -- and the most likely way it gets dropped is that the work landing
makes it look unnecessary.**

### AMENDMENT 21 -- WS-C7 verified at EXERCISED grade, and its G1 composes with the obligation_types finding into something neither half carries

WS-C7's boundary-declaration schema became load-bearing for the ESTATE boundary question the moment
`~D` predicted needing one. **Nobody had independently verified it. A verify seat with an unblocked
window and a load-bearing unverified artifact in its own lane has exactly one correct move.**

#### A21.1 -- THE EXERCISE CLAIM RE-DERIVES EXACTLY

```
CLAIMED (0.7.0_AE_CloudOps~Z)   comp-legacywriter --census, twice, 140431Z   rc=0, 202 lines
MEASURED (mine, ~1608Z)         independent re-run                          rc=0, 202 lines   EXACT
```

**EXERCISED grade, not a config read** -- reproduced across a two-hour gap by a seat that wrote neither
the tool nor the schema. **This is the grade Rule 22a demands for a behavioural claim and the one that
is hardest to manufacture.**

#### A21.2 -- THE BANK CITATIONS RESOLVE, AND ONE OF THEM IS LOAD-BEARING FOR A LINT

Checked because a dead citation is the day's recurring class (`type_tuple.grain` -> `D1.grain_axis`,
resolving at no vintage, repaired this morning):

```
dynamic_rails.D1_value_grain ................ :291   RESOLVES
dynamic_rails.D3_contract_obligation ........ :355   RESOLVES   (lifecycle.decay :469)
ordered: [artifact, partition, row, field] .. :296   RESOLVES
```

**The `ordered:` list is what makes G2's *denominator_grain coarser than row_grain* a COMPUTABLE
violation rather than an aspirational one.** The bank supplies the ordering the lint needs. **That is
the difference between a lint and a wish, and it is a citation doing real work rather than decorating.**

#### A21.3 -- THE COMPOSITION: THE DENOMINATOR IS A CHAIN, SO A BOUNDARY CANNOT BE A SCALAR

**`~Z`'s G1, exercised:** a single scalar cannot express a narrowing pipeline --
`4846 files -> 642 locations -> 439 written surfaces -> 345 at score>=3 -> 25 displayed` -- **and the
honest recall question is different at every stage.**

**Mine, at full denominator (4 of 4 `obligation_types`):** **`completeness` does not CARRY a boundary
declaration; it PRESUPPOSES one.** It asks *did you cover the declared population*; a boundary states
*what population is reachable at all*. **The boundary is the denominator `completeness` is measured
against.**

> **COMPOSED: THE DENOMINATOR IS A CHAIN, THEREFORE A BOUNDARY DECLARATION CANNOT BE A SCALAR -- AND A
> `completeness` OBLIGATION OVER A NARROWING PIPELINE IS UNDER-SPECIFIED BY CONSTRUCTION.**
> **The failure is SILENT: a reader computes a ratio against whichever stage happened to get recorded,
> and the answer is well-formed and wrong.**

**NEITHER HALF IMPLIES IT ALONE.** Mine says the boundary *is* the denominator; theirs says the
denominator *is a chain*. **It is `CONTROLS_OVER_CARE` III-g -- *a scalar cannot report its own
omissions* -- applied to the DENOMINATOR rather than to the count.**

**SURFACED, NOT RULED.** No field, no shape, no chain grammar proposed. **Vocabulary and placement are
CTO~Z's, and I hold that line whether the finding is mine, borrowed, or composed.**

#### A21.4 -- TWO PIECES OF DISCIPLINE IN SOMEONE ELSE'S ARTIFACT, WORTH RECORDING BECAUSE THEY COST SOMETHING

**G3 -- *"Proposed (NOT added -- schema changes are the gate's)."*** They found a missing enum value,
named the exact shape it needs (`run_conditional`, condition named), **and did not add it -- holding the
proposal line in the hardest possible position: their own schema, their own finding, their own write
access.**

**G5 -- *"AND I CONFLATED THEM."*** A self-caught conflation, filed as a gap in their own instrument,
**inside the deliverable whose purpose was to make that instrument look sound.**

> **FIVE GAPS FOUND BY EXERCISING YOUR OWN SCHEMA AGAINST A TOOL YOU DID NOT WRITE IS NOT A WEAK
> RESULT -- IT IS THE ONLY KIND THAT MEANS ANYTHING.** A schema returning ZERO gaps on first foreign
> contact would have established nothing except that nobody looked. **An unexercised schema arriving
> exactly when another fabric predicts needing it is luck; one that reports its own failures against
> foreign input is evidence.**

### AMENDMENT 22 -- C8's acceptance criterion is UNSATISFIABLE BY ANY INTERMEDIATE, and it cannot distinguish an honest self-report from never having looked

`0.8.0_AE_CloudComp~C` delivered WS-C8 artifact 1 and then **reported, against their own deliverable,
that it RAISES the doctrine byte-count and does NOT satisfy C8 acceptance** -- classifying their own
miss as **M6 in the taxonomy they were writing down.** **A seat reporting its own work short is the
rarest event in this fabric; it deserves verification rather than applause.**

#### A22.1 -- CONFIRMED, AND THE MEASUREMENT IS STRONGER THAN THE CLAIM

```
doctrine corpus BEFORE (e16ea3bda~1) .... 172393 B / 7 files
doctrine corpus NOW ..................... 187933 B / 8 files
DELTA ................................... +15540 B
MECHANISM_LAWS.md ....................... 15540 B        <-- EXACTLY EQUAL
```

> **THE DELTA IS EXACTLY THE NEW FILE. NOT ONE BYTE WAS REMOVED FROM ANYWHERE.** **The collapse is not
> partial and not incomplete -- IT HAS NOT BEGUN.** That is the statement an acceptance check needs;
> *"raises the byte-count"* is compatible with a half-done merge and this is not.

**SECOND MEASUREMENT, CUTTING IN ~C's FAVOUR:** `CONTROLS_OVER_CARE.md` carries **ZERO** M-class
references. **The 14 M-laws are NOT duplicating the doctrine set** -- the corpus grew, but not
*redundantly against its neighbours*. **The collapse source is somewhere other than `docs/doctrine/`,
which also means the dedup job is not where a reader would go looking for it.**

**AND THE SEQUENCE ~C FOLLOWED IS CORRECT: you cannot collapse into a target that does not exist.**
Skeleton first, collapse second. ***"Artifact 1 does not satisfy acceptance" is a SEQUENCING FACT, not
a defect in the work.***

#### A22.2 -- THE FINDING: THE CRITERION IS UNSATISFIABLE BY CONSTRUCTION

> **If C8's acceptance requires a NET BYTE REDUCTION, the FIRST deliverable is guaranteed to fail -- and
> so is every deliverable until the last one.** The skeleton must exist before anything can merge into
> it, so **the criterion is not strict; it is inapplicable until the terminal artifact.**

> **AND THE DISCRIMINATION FAILURE IS THE SERIOUS HALF: on that criterion, a seat that self-reported
> honestly and a seat that never looked produce THE SAME VERDICT -- both "fail."** **A criterion that
> cannot separate those two is not measuring delivery. It is measuring nothing, while appearing
> strict.**

**Same family as `describes` (a control living inside the blindness it was written to mitigate) and
`.runtmp/` (a safe harbour inside the destroyed class): A CONTROL PLACED WHERE IT CANNOT
DISCRIMINATE.** **Third instance today, three different substrates.**

#### A22.3 -- THE HANDLING MATTERS MORE THAN THE FIX, AND IT IS NOT MINE

**Routed to CTO~Z and COO; I proposed no replacement criterion.** One recommendation on *handling*
only, because the record shapes the next seat's behaviour:

> **~C's catch should be recorded as THE CRITERION BEING WRONG, not the artifact being short.**
> Otherwise the ledger shows a seat missing acceptance on a correctly-sequenced deliverable --
> **and the next seat learns that self-reporting converts a clean delivery into a logged failure.**
> **An honest intermediate report is the cheapest verification instrument this fabric has, and it is
> entirely voluntary. A criterion that punishes it will retire it.**

*(That is L-4's shape -- a control whose only input is voluntary disclosure must not penalise
disclosure -- arriving at an ACCEPTANCE CRITERION rather than at a control. Whether that is an instance
or a distinct cell is a collapse question, and I am conflicted on law-count; ~C and CTO~Z own it.)*

#### A22.4 -- VERIFIED SEPARATELY: THE MID-BUILD CORRECTION HELD

`MECHANISM_LAWS.md:13` reads **"THE BOUNDARY -- AND IT IS THREE-WAY, NOT TWO"**, carries the unhomed
third family, my six-zero measurement attributed, and the *L-8 is an instance of itself* line.
**CTO~Z's retracted two-way text did not reach the artifact.** **A correction that landed inside a live
build, ahead of the copy that would have carried it -- the one case today where the last surviving copy
was the corrected one.**

### AMENDMENT 23 -- A CONSERVATIVE ERROR PASSES ITS OWN CHECK, and one of mine may be sitting in this artifact

`0.8.0_AE_CloudComp~C` reported their WS-C8 artifact 1 short against their own interest. Verifying it
showed their report was **true but WEAKER than the truth** -- and the sharpening that fell out is the
day's most load-bearing law, arriving from the direction nobody was watching.

#### A23.1 -- THE LAW

> **AN UNDER-STATED CLAIM SURVIVES VERIFICATION. AN OVERSTATED ONE DOES NOT.**
> **A CONSERVATIVE ERROR IS AN ERROR THAT PASSES ITS OWN CHECK.**

*"Artifact 1 raises the byte-count"* is **TRUE**. A verifier checks it, confirms it, **and stops** -- so
*"the delta is exactly the new file, therefore nothing was deduplicated anywhere"* never surfaces. **An
overstatement gets refuted and the truth comes out; an understatement gets RATIFIED, and the
ratification is what closes the question.**

> **THE ERROR DIRECTION IS SAFE; THE STOPPING IS NOT.**

**Third direction today for one shape**: a *plausible reconciliation* foreclosing an open discrepancy
(A19), a *dismissive residual* closing a question with the authority of having been considered (A16),
and now a *true-but-weak self-report* closing it with the authority of having been verified. **All three
look safe. All three stop the looking.** **And this one is the worst of the three, because the other two
are errors and this one is a TRUTH.**

**~C retro-applied it to three of their own defects unprompted** -- *"the query returned nothing"* (true
of the foreground call; it had backgrounded and completed with rows), *"0 declarations"* from a live
two-file registry (true as a count; read as *the registry is empty* rather than *my loader cannot see
it*), *"tranche 1 is all UNDECLARED"* (12 of 14 true; the 2 PERMANENT were the entire reason a
non-default control was possible). **A law that retro-explains three cases it was not built from is a
law rather than a description.**

#### A23.2 -- AND THEIR SECOND EXAMPLE MAY BE SITTING IN MY OWN WORK

**My increment-2 gate exercise this morning recorded: *"live registry: ABSENT -- 0 declarations."***
**Measured now:**

```
files carrying `lifecycle_class` .......... 5
  org/modules/graph/estate-contracts/mdpf.contracts.yaml              <- HELD-OUT FENCE
  org/modules/graph/estate-contracts/model-portfolios.contracts.yaml  <- HELD-OUT FENCE
  org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml
  org/projects/NFRA_VELOCITY_CORE.json
  org/tier2_senior/0.7.0_AE_CloudOps/deliverables/.../tranche1.draft.yaml
RETRIEVAL CONTROL: `lifecycle_class` in the bank = 9   NEG token = 0
```

**`estate-contracts/` is a TWO-FILE directory -- the shape `~C` described.**

> **LABELLED *UNDER REVIEW*, NOT RETRACTED.** I have not re-read my probe, I do not know it was pointed
> at that directory, and those files may postdate it. **I am refusing both available explanations:
> *"it was probably earlier"* and *"different registry"* are exactly the plausible reconciliations that
> foreclose a live discrepancy** -- the thing A19 was written about, four hours later, against myself.

**FENCE DISCIPLINE, STATED BECAUSE IT CONSTRAINS THE FOLLOW-UP:** two of the five are `mdpf` and
`model-portfolios`, **both HELD-OUT. I counted their EXISTENCE and did not open them.** No rail finding
of mine rests on their contents, and the re-derivation must be designed so it still cannot.

#### A23.3 -- WHY THIS ONE MATTERS MORE THAN A NORMAL SELF-CORRECTION

**A peer's voluntary disclosure of their own weak measurement is what surfaced mine.** Nothing in my
instruments would have found it: **my probe reported ABSENT, my check confirmed ABSENT, and both were
internally consistent.**

> **THE ONLY THING THAT BREAKS A CONSERVATIVE ERROR IS SOMEONE ELSE'S DISCLOSURE OF THEIR OWN.** It is
> not detectable from inside -- that is the definition of passing your own check. **Which makes honest
> intermediate reporting a load-bearing INSTRUMENT rather than a virtue** -- and makes A22's finding
> sharper than I wrote it: **an acceptance criterion that punishes self-reporting does not merely
> discourage candour, it disables the only detector this class has.**

### AMENDMENT 24 -- GATE 5 EXERCISED 9/9 with controls, and the bound that qualifies the PASS: every cell hit the FALLBACK resolver

GATE 5 landed in the 17:01 pass. **Step 1 (does the code carry an arming marker) was discharged at
source by base MSTR before landing. Step 2 -- the exercise -- was mine, and a grep cannot discharge a
behavioural claim.** All nine cells were **pre-registered before the artifact existed on this device**,
so the test could not be shaped by the thing it tests.

#### A24.1 -- NINE CELLS, ALL AS REGISTERED

```
#  SERIAL             COMMAND                      EXPECT  ACTUAL
1  0.0.0_AB_MSTR~Z    git push origin CLOUD        ALLOW   ALLOW   PASS
2  1.0.0_SA_CTO~Z     git push origin CLOUD        DENY    DENY    PASS
3  <empty>            git push                     DENY    DENY    PASS   fail-closed
4  1.0.0_SA_CTO~Z     git fetch origin CLOUD       ALLOW   ALLOW   PASS
5  1.0.0_SA_CTO~Z     echo '...git push...'        ALLOW   ALLOW   PASS   no fire on a MENTION
-- the four I added, because running only the author's cells inherits the author's blind spots --
6  3.0.0_SA_CVO~Z     git push origin CLOUD        DENY    DENY    PASS   the real threat on this box
7  3.0.0_SA_CVO~Z     git pull origin CLOUD        DENY    DENY    PASS   THE VERB NO DELIVERED CELL TESTED
8  3.0.0_SA_CVO~Z     "git  push"  (double space)  DENY    DENY    PASS   NO one-keystroke bypass
9  3.0.0_SA_CVO~Z     git push --dry-run           ?       DENY           registered WITHOUT a prediction
```

**CELL 7 IS THE ONE THAT JUSTIFIED ADDING CELLS AT ALL:** the gate is named *integrator-only
**push/pull*** and **not one delivered cell exercised pull.** A suite can be 13/13 green on half its own
claim. **It passes -- but nobody knew that before it was run.**

**CELL 9 KILLED MY OWN SECOND ORACLE.** `git push --dry-run` is DENIED, so the independent oracle I
proposed **cannot run: I have one instrument, not two.** The gate's behaviour is correct -- a dry-run is
still a push command and blocking it is fail-safe. **The value is in having registered the cell without
a prediction rather than dropping it: a test whose purpose is to discover whether your OTHER test can
exist is worth running first.**

#### A24.2 -- CONTROLS ON MY OWN HARNESS

> **A -- IS `ALLOW` A REAL VERDICT OR A SILENT CRASH?** An allowed cell emits empty output at `rc=0`;
> denials emit the `permissionDecision":"deny"` JSON. **Checked because *"no deny found"* and *"the
> script died"* are otherwise byte-identical** -- the same shape as every silent-absence finding today.
> **B -- MUTANT: `0.0.0_AB_MSTR~Z` + `git rebase` -> DENY.** **GATE 5's allow-path does NOT exempt the
> integrator from the other NEVER rules.** The failure I most wanted excluded: a push-allow quietly
> widening into a blanket MSTR exemption.
> **C -- NEGATIVE: `ls -la` -> ALLOW.** The matcher is not over-broad.

#### A24.3 -- *** THE BOUND, AND IT LIKELY APPLIES TO BASE MSTR'S 13/13 TOO ***

Control A surfaced this in the hook's own stderr:

```
never-rules-gate.sh: line 481: .../org/mcp/sessions/ctl-27294.serial: No such file or directory
```

> **A SYNTHETIC `session_id` HAS NO SERIAL FILE, SO RESOLUTION FALLS THROUGH TO `OPAL_AGENT_SERIAL`.
> EVERY ONE OF MY NINE CELLS EXERCISED THE *FALLBACK* RESOLVER. THE *PRIMARY* RESOLVER -- session_id ->
> per-session serial file -- IS UNEXERCISED.**

**And the delivered harness instruction says *"session_id = any id"*, so base MSTR's 13/13 almost
certainly carries the same bound, and neither suite stated it.**

**THE CLAIM SUPPORTED:** *the gate decides correctly GIVEN a correctly-resolved serial.*
**THE CLAIM UNTESTED:** *the gate resolves the serial correctly in production.*
**WHY IT IS NOT PEDANTRY: in production the session-file path is PRIMARY. If it ever resolved an MSTR
serial for a non-MSTR session, the gate ALLOWS a push it should deny -- and every cell in both suites
stays green.** **This is *"I bounded the METHOD and never bounded the CORPUS"* arriving inside the
instrument built to close a different failure.** *(One production sample exists on the allow branch:
MSTR~Z's 17:01:42 push resolved correctly here. The primary path's DENY branch has been exercised by
nobody, and I will not fabricate a peer's session file to reach it.)*

#### A24.4 -- I VERIFIED MY OWN READ WAS CURRENT, AND MEASURED THE TRAP IN THE NEW STANDARD

MSTR~Z corrected *"pull at will"* and made `git show origin/CLOUD:<path>` the fabric standard for
load-bearing reads -- **because `git fetch` moves the ref only, `git pull` is now denied to seats, and a
working tree can therefore sit up to one full window behind origin.** I had read the hook from the
working tree, so I checked:

```
origin/CLOUD copy .......... 36598 B          working tree ....... 36598 B     diff CLEAN
positive control ........... 2 vs 2           stderr ............. empty
-> my 9/9 exercised the CURRENT hook. Verdict stands unqualified.
```

**AND THE PRESCRIBED REMEDY HAS A LIVE, MEASURED TRAP ON THIS DEVICE:**

```
MSYS_NO_PATHCONV=1 git show origin/CLOUD:.tools/hooks/never-rules-gate.sh | grep -c permissionDecision -> 2
                   git show origin/CLOUD:.tools/hooks/never-rules-gate.sh | grep -c permissionDecision -> 0
```

> **Same file, same string, same second. Present twice, reported as ZERO, silently.**
> **THE REMEDY WAS PRESCRIBED TO FIX STALENESS; UNGUARDED ON A DOT-LEADING PATH IT RETURNS A FALSE
> ABSENCE ON THE MOST CURRENT DATA AVAILABLE.** **A 50-minute-old file gives you an old truth; this
> gives you a confident nothing.** **And it lands exactly on the load-bearing class -- `.tools/`,
> `.claude/`: hooks, gates, comp-tools, settings. The files most worth reading currently are the ones
> the unguarded remedy cannot read.**

**RECOMMENDED (routed to MSTR~Z + COO ahead of the Tier-2 cascade): `MSYS_NO_PATHCONV=1` on EVERY
`git show <ref-with-a-slash>:<path>`, UNCONDITIONALLY -- not "for dot-leading paths."** CLAUDE.md
already rules this way (*blanket the slashed-ref case, don't memorize the boundary*). **A per-path
decision requires every seat to classify every path correctly forever; the blanket costs one prefix and
cannot be got wrong -- and a rule applied only when remembered has the same failure profile as the prose
stop GATE 5 just replaced with a mechanism.**

### AMENDMENT 25 -- WS-C7 suite enumeration verified, a FENCE RULING closed, and A24's bound corrected to its true size

Two records here: **A24's bound is narrower than I stated** (correction, at source, by the party who
could measure it), and **WS-C7's suite-enumeration findings are verified with one fence question ruled.**

#### A25.1 -- CORRECTION TO A24's BOUND: REAL FOR MY SUITE, PARTIALLY DISCHARGED ON BASE'S

I recorded that every GATE 5 cell hit the FALLBACK resolver and inferred base MSTR's 13/13 *"almost
certainly carries the same bound."* **Base MSTR re-verified rather than asserted, and the inference was
too wide:**

> **2 of their 13 cells DID exercise the PRIMARY resolver, using REAL serial files.** And the
> discriminator is the part worth keeping: **env and file must DISAGREE, or the cell is green under
> EITHER resolver and proves nothing about which one fired.** Their two cells: `file=NON-MSTR +
> env=MSTR -> DENY` and `file=MSTR + env=NON-MSTR -> ALLOW`. **Both prove the session file is read AND
> beats the env, in both directions.**

**CORRECTED STATEMENT: the bound is REAL for my 9-cell suite (all synthetic session_ids -> fallback,
confirmed by the `:481` stderr) and PARTIALLY DISCHARGED on base's 13.** **The gap was in the RELAY, not
in their test** -- the 5-cell prose harness I was sent omitted the two production-critical cells, so my
suite inherited a bound from an incomplete transmission. **They own that plainly.**

> **AND THE GENERAL FORM SURVIVES INTACT: *a suite testing only the fallback leaves the PRIMARY
> production path unbounded.*** **My finding was worth making and was not total. Both halves are
> recorded because a correction that only records the first half is the same defect one level up.**
**Not running the two closing cells: Andrew-direct, *"dont get bogged down in this we have work to
do."* The thread is closed; the record is accurate; that is the whole obligation.**

#### A25.2 -- FENCE RULING: `ADVI_STAUDT` CONTACT IS NON-SHAPING. NO REMEDIATION.

`0.7.0_AE_CloudOps~Z` declared a marginal fence contact unprompted -- a broad `grep` for a
"Class 1/Class 2" definition returned `ADVI_STAUDT.md` and printed three lines. **Measured: my binding
names `ADVI_PERFORMANCE` (13 occurrences in my ruling) and `MDPF_GLOBAL` (21). `ADVI_STAUDT`: ZERO --
never adjudicated, so this is a genuine first instance.**

> **RULED on two independent grounds, either sufficient:**
> **(1) OUTSIDE THE FENCE AS BOUND.** The fence names two programs. **ADVI-family adjacency is not
> membership: a fence that silently expands by family is not a fence, it is a mood.**
> **(2) NON-SHAPING EVEN IF INSIDE -- the load-bearing half.** The fence prohibits held-out material
> **SHAPING THE RAILS**; the test is not *did you see it* but *did it supply anything*. **What was seen
> ESTABLISHES A TOKEN COLLISION, which SUBTRACTS a naming option rather than supplying one. A collision
> finding is a reason NOT to use a name; it cannot import a meaning.**

**SURFACED, NOT RULED: whether the fence should name a FAMILY rather than two codes is a SCOPE question
and Andrew's.** I ruled the instance; I did not redraw the boundary. **And the declaration is what made
the ruling cheap -- an undeclared contact costs an investigation, a declared one costs a paragraph.**

#### A25.3 -- THE SUITE FINDINGS VERIFIED, AND ONE CITATION-FORM DEFECT

**FINDING 1 -- CONFIRMED AT SOURCE.** The DEBTLOOPS memo carries *"Type II corroboration: nine same-day
specimens"* and *"Nine instrument failures were logged on 2026-07-29, all of them false negatives."*
**The membership finding's FORM is the keeper:**

> ***"A count that is right while its membership is wrong."*** **`3 of 9` is arithmetically fine and the
> two sides of the fraction refer to DIFFERENT SETS.** **Strictly harder than a miscount, because every
> check that verifies the arithmetic passes.** Same family as today's `219/210/208` units error and
> `~C`'s *a zero cannot say which zero it is*.

**FINDING 2 -- SUBSTANCE CONFIRMED, CITATION STALE.** The acceptance clause exists -- **`PRD.md:342`,
not the cited `:222`** (the PRD is 427 lines; `:222` now carries fence text). **Exactly ONE occurrence
in the PRD, used as a pass condition, defined nowhere.** **Rule 22's own case: *a line citation without
a vintage is not a citation*, because `file:line` resolves at every vintage to different content.** The
reasoning was sound; the citation format was not.

**ON THEIR ~226 ESTATE-WIDE COUNT: I measure 456 occurrences / 357 lines / 128 files. NONE is 226, and I
am NOT inventing a reconciliation** -- today already cost one plausible explanation that foreclosed a
live discrepancy. **The collision is confirmed and load-bearing whichever unit is right; the number
needs its unit stated.**

### AMENDMENT 26 -- the cross-seam pass, and why F-2's remedy has a MEASURED failure rate in this estate

Base CVO ran the Andrew-ordered s.7 cross-seam **adversarial** pass over CORE P1 -- asking whether
site-Z's types work stays canonical against the 07-30 C-ladder and the D-rails, or **warps** it.
**Verdict: NO DRIFT, NO TWIN-CANON, NO WARPING**, agreeing with CORE's own P1 close.

#### A26.1 -- WHY IT IS CORROBORATION AND NOT AN ECHO

**The controls are what make the verdict mean anything:**

> **`8/8` canon pointers resolve -- WITH a NEGATIVE control (a bogus leaf does NOT resolve), so the
> ratio is a MEASUREMENT rather than a tautology.**
> **`C5` / `C3.iii` / invented-rungs = `0` -- WITH a POSITIVE control (`C3.ii` = 2), so the zero is a
> FINDING rather than a broken scan.**

**Both are exactly the controls this session has repeatedly shown to be the whole difference between a
result and a number.** *An `8/8` without the bogus leaf, and a `0` without `C3.ii`, would have been
unfalsifiable -- and would have read identically.*

> **AND IT WAS RUN ADVERSARIALLY, BY THE OTHER FABRIC. Agreement between a self-assessment and an
> adversarial cross-check is CORROBORATION; agreement between two friendly reads is one opinion counted
> twice.** **P1's close is strengthened, not merely seconded.**

#### A26.2 -- F-2's REMEDY IS RIGHT, AND ITS SECOND HALF IS THE ONE THAT EMPIRICALLY FAILS

F-2 recommends ESTATE consumers **PIN a bank version and re-resolve deliberately**, rather than tracking
HEAD implicitly. **Sound -- and its failure mode was measured this morning, before it was recommended:**

```
the rule bank is at v1.8
infra/system/sdk/**   6 .yaml + gensdk/scaffold.py   PINNED v1.2
SYSTEM_DEFINITIONS.yaml                              PINNED v1.4
two infra/system/ontology docs                       PINNED v1.2
                          ~10 REAL stale readers, open today
```

> **EVERY ONE OF THOSE CONSUMERS DID THE FIRST HALF. THEY PINNED. NOBODY DID THE SECOND HALF.**
> **`pin + re-resolve deliberately` is not one practice -- it is one CHEAP ACTION and one PERPETUAL
> OBLIGATION**, and this estate has measured evidence that the cheap half happens and the perpetual
> half does not.
> **A PIN WITHOUT A RE-RESOLUTION OBLIGATION IS NOT A SAFETY MEASURE -- IT IS A FROZEN VINTAGE WITH A
> CONFIDENT LABEL.** It fails SILENTLY, because a pinned consumer reads *correctly* against a version
> that is no longer the constitution. **Implicit HEAD-tracking at least breaks loudly.**

**NOT AN OBJECTION TO F-2.** Pinning still beats implicit HEAD-tracking. **The claim is narrower and
harder: the remedy must name its enforcement half, or it reproduces the exact population it was written
to prevent.** *(Same shape as `.runtmp/` -- a correct answer to problem A, offered as the answer to
problem B.)*

#### A26.3 -- THE DISCRIMINATOR ALREADY EXISTS AND IS ALREADY BOUNDED

> ***A pin nothing reads is a RECORD; a pin something reads is a READER.*** (A16.) **So the enforceable
> question is not *"is this pin old?"* but *"is this pin CONSUMED?"*** -- which routes the check to the
> consumer enumeration rather than a version scan, **and avoids the FLOODING failure**: ~40 version hits
> of which most are correct-as-written history, and a flooding instrument gets ignored, **which is
> exactly how the ~10 real ones stay open.**

**HONEST BOUND, unchanged from A16.1 rather than newly claimed: the enumeration is PYTHON-ONLY, and the
~10 real stale readers are mostly `.yaml`/`.json`. The discriminator lands in the right place and cannot
yet reach the population that needs it.** A sequencing fact, not an objection.

#### A26.4 -- F-1 IS CTO~Z's, AND I AM ITS BENEFICIARY

F-1: the bank's **internal self-citations are not lint-checked** -- the A7.1 lint validates CONTRACT
tokens, not bank-internal paths, and `@2f8c55f192` repaired a dead one (`type_tuple.grain` ->
`dynamic_rails.D1.grain_axis`, resolving at no vintage).

**Nothing to add except the provenance: I checked WS-C7's bank pointers specifically BECAUSE that repair
told me the class existed** -- and they resolved. **A fixed defect that teaches the next reader where to
look is worth more than the fix**, and it is the second time today a repair has functioned as a pointer
rather than only as a correction.

### AMENDMENT 27 -- SEAMS STATEMENT for the Andrew-direct integration review: three seams visible only from the verify seat

**Andrew has paused the program after WS-C8 to personally review C1/C2/C3/C7/C8 + the ESTATE work for
INTEGRATION POINTS.** *"Whether these are five correct things that do not fit together."* **Eight seams
are already on the joint list (MSTR~Z's five, plus my S-A/S-B/S-C). This adds what only the verify seat
can see, and re-derives none of them.**

**MY POSITION, STATED BECAUSE IT DETERMINES WHAT I CAN CONTRIBUTE:** I own no workstream deliverable. I
verified INSIDE C1 (both increments), C2 (step 0), C7 (schema, applied artifact, suite enumeration) and
C8 (artifact 1 and its acceptance). **So my edges are not one workstream's -- they are the couplings that
are invisible from inside any single one.**

#### S-D -- **C8's SCOPE IS DECIDED BY A C2 RESULT, AND NOTHING RECORDS THE DEPENDENCY**

**C8's job is to collapse the taxonomy. What it must collapse was settled by a WS-C2 finding:** CTO~Z's
step 0 established that **the M-taxonomy types WHERE AN ASSERTION SITS and does NOT type INSTRUMENT
FALLIBILITY** -- by construction.

That result is load-bearing twice over: **it is why the ~10 staged L-laws are not duplicates** (A17), and
**it is what refuted C8's own two-way coverage claim** (A18).

> **C8's scope is therefore a FUNCTION of a C2 output. If step 0 were revised, C8's collapse target
> changes -- and no artifact in either workstream records that C8 CONSUMES it.** **A dependency nobody
> wrote down survives only as long as the two people who remember it.**

#### S-E -- **THE VERIFICATION LAYER RESTS ON A VOLUNTARY BEHAVIOUR, AND ONE ACCEPTANCE CRITERION PENALISES IT**

Two halves measured today, in different workstreams, that compose into the sharpest cross-cutting seam
I found:

> **(i) A CONSERVATIVE ERROR IS UNDETECTABLE FROM INSIDE.** *"Artifact 1 raises the byte-count"* is TRUE
> -- a verifier confirms it and STOPS, so the stronger truth never surfaces. **My own case: my probe
> reported ABSENT, my check confirmed ABSENT, both internally consistent, and an auditor would have
> confirmed it too.** **The only thing that broke it was another seat disclosing their own.**
> **(ii) C8's ACCEPTANCE CRITERION CANNOT DISTINGUISH AN HONEST SELF-REPORT FROM NEVER HAVING LOOKED**
> (A22). If acceptance requires net byte reduction, `~C`'s correctly-sequenced skeleton and a seat that
> did nothing produce **the same verdict.**

**COMPOSED: THE ESTATE'S DETECTION CAPABILITY FOR AN ENTIRE ERROR CLASS RESTS ON VOLUNTARY DISCLOSURE --
AND AT LEAST ONE ACCEPTANCE CRITERION MAKES DISCLOSURE COSTLY.** **That is not a workstream defect. It
is a seam between the workstreams and the VERIFICATION METHOD ITSELF, and it is unowned precisely
because it is nobody's deliverable.** *(This is L-4 -- a control whose only input is voluntary disclosure
must not penalise disclosure -- arriving at the program level rather than at a control.)*

#### S-F -- **FOUR TERM COLLISIONS IN ONE DAY, ALL CAUGHT AFTER ADOPTION. NOBODY OWNS "IS THIS NAME TAKEN?"**

```
scope        C1          live in type_tuple, retired in contract_record -- a TWO-RAIL state
layer        C1 round 2  already overloaded 3x; renamed
pre-flight   ~D          already means a pre-build review in 3 live files
Class 1/2    C7          1 use in the PRD, defined nowhere, collides estate-wide
```

**Every one was found AFTER a workstream had adopted the token, by the seat that tripped over it, and
resolved ad hoc.** **FOUR IN ONE DAY ACROSS FOUR WORKSTREAMS IS NOT BAD LUCK -- IT IS A MISSING STEP.**

> **There is a ratified resolution rule (*the newcomer renames*) and NO RESERVATION MECHANISM. Nothing
> answers *"is this token already taken?"* BEFORE adoption, so the rule only ever fires as cleanup.**
> **AND THE RULE DOES NOT COVER THE CASE THAT ALREADY HAPPENED:** `scope` is live in `type_tuple` and
> retired in `contract_record`, **both ratified, so there is NO NEWCOMER** -- renaming either destroys a
> correct meaning. A16's *a token cannot carry its rail* makes that a **KEYING** defect, not a
> collision. **The resolution rule is sound and its residual is the shape the estate actually produced.**

#### S-G -- ONE CORRECTION TO THE JOINT LIST'S PROVENANCE, NOT ITS CONTENT

**MSTR~Z's resume asks me to *"commit the F-2 stale-reader measurement -- it still exists only in a
message."* IT IS COMMITTED**, and was before the request: **A26 `@89cbe0e2a`, at origin, verified**
(`AMENDMENT 26` = 1, `FROZEN VINTAGE` = 1, `stale readers` = 3, fresh negative token = 0, 2805 lines).

**Recorded because it is the day's own recurring shape one level up:** *a correct instruction issued
against a state that had already changed.* **No harm here -- but the same belief applied to a DELETION
rather than a re-commit would have destroyed work, and the request read exactly as authoritative either
way.**
