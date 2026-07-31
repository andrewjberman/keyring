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
