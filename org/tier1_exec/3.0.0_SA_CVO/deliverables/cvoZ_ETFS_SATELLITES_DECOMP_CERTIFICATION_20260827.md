# ETFS_SATELLITES STAGE-3 DECOMP — CERTIFICATION

> ## ⛔ READ THIS BLOCK FIRST — BINDING STATE AS OF 2026-08-28 ~00:2xZ
>
> **This file is CHRONOLOGICAL. A CORRECTION at §622 retracts a finding — and a PRECISION AMENDMENT
> at §690 retracts a sentence INSIDE that correction.** ⛔ **The misattribution in the correction
> travelled into a task order's acceptance criterion before it was caught; do not cite §622-689
> without §690.**
>
> | claim | binding state | where |
> |---|---|---|
> | *"vacuous corpus / the anchoring is unsupported"* | ⛔ **RETRACTED, FALSE ON BOTH LIMBS.** Bare substring admits **27**, not 9; `Core \| Satellite 98` **is** in the corpus | §622 |
> | *"the **anchor** excludes eighteen rows"* | ⛔ **RETRACTED.** The **LITERAL TOKEN `Opal`** does. Per-limb: drop `$` → **+0**, drop `^` → **+0**, drop the token → **+18** | §690 |
> | both anchors | **UNEXERCISED by this corpus** — which is a finding, not a pass. Synthetic negatives are required for each | §690 |
> | the membership predicate | **VALIDATED against the real mutant.** `satellites_registry.py:213` was anchored deliberately and documents why | §622 |
> | the classification | **RULED**, not open — Andrew ~16:1xZ, `SAT-b-2`, IS-A vs HOLDS-A | §622 |
> | `F3` / fixture obligation | **STANDS.** Discharged in spec by `T5DS-AC4`'s three rows (1 real + 2 synthetic), `1.0.0_SA_CTO~Z` amend | §622 |
> | this certification's **verdict** | **UNCHANGED** — a finding inside it was retracted; the verdict was not | — |
>
> ⭐ **The corpus exercises the TOKEN and neither ANCHOR. That single sentence is the whole binding
> result, and it is the one that took three attempts to state correctly.**


**Certifier:** `3.0.0_SA_CVO~Z` · 2026-08-27 ~16:4xZ
**Artifact:** `workflows/atom_decomposition/runs/etfs-satellites/20260827T160438Z/DECOMP.md`
**Read at:** `origin/SITEZ @ f58160dd8e` (remote, not a working-tree copy)
**Author:** `2.0.0_SA_COO~Z` · **Issuer:** `1.0.0_SA_CTO~Z` · **Directive:** D4 (SITEZ)

---

## VERDICT — **CERTIFIED WITH FINDINGS**

**The cells are sound and TO-minting may proceed.** Every denominator I could test
independently reproduced EXACTLY, both mid-flight corrections are correct, and the Rule 24
record as corrected is right. Four findings follow. **Two are P1 and must land in the TO cut**;
they are gaps in the decomp, not errors in it, and none invalidates a cell.

⛔ **THIS VERDICT IS ABOUT THE DECOMP, NOT THE BUILD.** It certifies that the cells are
well-formed, MECE over their declared surfaces, and carry oracles that can fail. It says nothing
about whether the build will be correct.

### Vintage guard — how the moving-artifact hazard was closed

`2.0.0_SA_COO~Z` (9253) and `0.0.0_AB_MSTR~Z` (9255) both warned this artifact moved twice today
and that certifying v1 would certify a wrong member set and a withdrawn taxonomy verdict.
**Verified rather than accepted**, with a negative control so the test could say no:

```
git merge-base --is-ancestor a1c38e8c53 origin/SITEZ   -> ancestor      (Rule 24 (iv) withdrawal)
git merge-base --is-ancestor 8e188d4f42 origin/SITEZ   -> ancestor      (member set NINE)
git merge-base --is-ancestor 506a1626f0 origin/SITEZ   -> NOT ancestor  <- CONTROL: my own
                                                          unpushed commit. The test can say no.
git merge-base --is-ancestor f58160dd8e HEAD           -> YES
```
Both corrections are on the remote and in my history. **I could not have picked up v1.**

---

## 1. WHAT REPRODUCED — independent measurement, not assent

Instrument: `s3://opal-data-assets/blackdiamond/cottonwood/bronze/rebalancer_models/2026-08-27/page_000.json`,
pulled to scratch and byte-verified (34,454 B on S3, 34,454 B local — `rc=0` is not evidence of bytes).

| decomp claim | measured | verdict |
|---|---|---|
| DENOMINATOR 65 rows, `pageCount=1`, `totalResultCount=65`, FULL COVERAGE | 65 / 1 / 65 | **EXACT** |
| NINE canonical members: 15 30 40 50 60 70 80 90 98 | the same nine, no more, no fewer | **EXACT** |
| `Opal Satellite 90` has 0 accounts; `98` has 11 (`SAT-b-5`) | 0 and 11 | **EXACT** |
| `Core \| Satellite 98` (9 acct) sits beside `Opal Satellite 98` (11 acct) (`SAT-b-4`) | 9 and 11 | **EXACT** |
| the five blends are real roster books | all 5 present, all `accountCount=1` | **EXACT** |
| `Opal Ultra Short Term` is a real model, not a satellite | present on roster | **EXACT** |
| NEGATIVE CONTROL — `Opal Satellite 99` / `25` absent | both absent | **control passes** |

**Both corrections are RIGHT and I am recording that as a finding of its own**, because the
retraction chain is the part most likely to be misread later: the Rule 24 (iv) withdrawal is
correct (one remedy — build the mode — moves the state axis to parity, so (iv) is satisfied; and
if "not built yet" counted, every enum would fail (iv) on extension), and the IS-A vs HOLDS-A
membership rule is correct and strictly better than the v1 heuristic.

---

## 2. FINDINGS

### ⛔ F1 — P1. `SAT-inv-2` AND THE CORRECTED `SAT-b-2` ARE JOINTLY UNSATISFIABLE ON THE NAMED ARTIFACT.

- `SAT-inv-2` binds membership to *"a DECLARED PREDICATE **OVER THE ROSTER**, NEVER A HAND LIST."*
- `SAT-b-2` as corrected rules the criterion is **IS-A vs HOLDS-A** — structural, sovereign.
- **MEASURED: the roster page cannot express that criterion.** It is FLAT. All 21 fields
  enumerated; **none** carries composition, children, hierarchy, or constituents.

I swept every field for one that separates the 9 members from the 5 blends, then **corrected my own
sweep**: `id`, `lastUpdate`, `name`, `rowNumber` are unique per row, so they are disjoint between
*any* two disjoint row sets **by construction** — that is identity, not class information, and my
first pass wrongly reported them as discriminators. Excluding them, what remains is:

```
accountCount / rebalanceAssignmentCount   all 5 blends = 1, members = {0,3,4,11,18,39,65,81,83}
                                          -> separates TODAY, and it is EXACTLY the bespoke/
                                             one-account heuristic Andrew disowned. A blend that
                                             gains a second account defeats it silently.
displayName                               a NAME field -- the route SAT-b-2 explicitly disowns.
```

>> **SO THE ONLY ROSTER-EVALUABLE PREDICATES ARE THE TWO THE CELL RULES OUT.** The correction fixed
   the ANSWER and weakened the MECHANISM: v1 had a computable predicate that was wrong; v2 has a
   correct criterion that is not yet a predicate, and nine names in its place — which is what
   `SAT-inv-2` calls a hand list. <<

**THE REMEDY IS CHEAP AND THE DECOMP ALREADY NAMES IT.** The structural signal lives in
`rebalancer_model_detail` — `SAT-a-1`'s own source — as `hierarchy.children[]`: a book that
HOLDS-A satellite carries that satellite as a child; a satellite carries its underlying books.
**Ask: point `SAT-b-2`'s oracle at the DETAIL, and widen `SAT-inv-2` from "over the roster" to
"over the roster + detail."** Owner: `2.0.0_SA_COO~Z` (author) with `1.0.0_SA_CTO~Z` (issuer).
⚠ I did **not** verify that `hierarchy.children[]` in fact separates the two sets — that is a
detail-file read I have not run. **It is a CANDIDATE, marked INFERRED, not a measured remedy.**

### ⛔ F2 — P1. `modesFor(firm)` IS A SCHEMA-AUTHORING ACT AND HAS NO FOUR-POSTULATE RECORD.

Rule 24: *"Outcome arrays, typed-result sets and predicates ARE schemas."* `SAT-c-2` introduces
`modesFor(firm)` — a predicate returning a SET of modes per firm. **§2's four-postulate record
covers only `PositioningMode`.** The decomp's own (iii) verdict *names* firm gating as
*"a SEPARATE axis (`SAT-c-2`, `modesFor(firm)`)"* — **it identifies the axis and then never tests
it.** Separating the axes was the right call; the second axis inherited no record from it.

**This is the axis carrying the actual client-facing exposure.** A wrong `PositioningMode` renders
the wrong pill; a wrong `modesFor` shows one firm's books to another. Ask: a four-postulate record
for `modesFor` before `SAT-c-1`/`SAT-c-2` are cut into TOs. Owner: `1.0.0_SA_CTO~Z` (issuer).

### ⛔ F3 — P1, AND THE SHARPEST. A JOIN-KEY FORMAT MISMATCH ON EXACTLY ONE MEMBER.

```
name = "Opal Satellite 60"   displayName = "Opal - Satellite 60"    <== DIFFERS (a dash)
the other eight members       displayName == name                     exactly
```

`SAT-a-2` states the detail files carry **DISPLAY** names and the portal alias map resolves them.
So the roster→detail join crosses a format boundary that **holds for 8 of 9 members and breaks for
1** — and it breaks on the member with the **second-highest account count (81)**.

**THIS IS THE GRAIN-MISMATCHED-JOIN-KEY CLASS AND ITS FAILURE MODE IS SILENCE:** the join returns
empty, and empty reads as *"satellite 60 has no weights"* rather than as *"the key did not match."*
Corroborating that it is a property of the roster and not a typo: `Opal UST/ Sat 70` carries
`displayName = "Opal UST/ Satellite 70"` — the same divergence on a blend. And **only 25 of 65 rows
carry `displayName` at all**, so a null branch exists beside the mismatch branch.

**`SAT-a-2`'S ORACLE IS CORRECT AND ALREADY CATCHES THIS** — *"with the UNRESOLVED count printed —
a silent drop is the defect, not a tidy result."* Good design. **What is missing is the FIXTURE.**
Ask: `SAT-a-2`'s fixture must contain member 60 by name. **It is the natural mutant for the
resolution path exactly as `SAT-b-4` uses the `98` pair for the membership path** — and the decomp
already demonstrates it knows to do this, one cell over.

### F4 — P2. `SAT-b-4`'s "19 excluded rows" DOES NOT REPRODUCE UNDER ANY FRAME I CAN NAME.

```
name starts "Core"                              16
name matches "Core | Satellite *"               15
contains "Satellite" and NOT canonical-9        18
contains Satellite|Sat token and NOT canonical-9  21
NOT starting "Opal" and contains Satellite/Sat  17
```

**I am NOT correcting 19 to any of these.** Correcting a count across an undeclared frame
reproduces the frame error — the same trap that produced "23 Opal-named rows," which is right
under *contains* `Opal` (23) and wrong under *starts with* `Opal` (22). **Both numbers are
frame-dependent and the decomp declares neither frame.** Ask: declare the frame, then state the
number. The full 30-row artifact is printed in the appendix so the next reader recomputes rather
than trusts.

⚠ **A live reason the frame matters:** `Core / Satellite Equity` uses a **slash**, not a pipe. Any
predicate written against `Core | Satellite` misses it.

### F5 — housekeeping, no action. §4's routing line has been overtaken.

§4 reads *"there is no CVO seat on this fabric at authoring time."* **True at authoring, false now.**
Already acted on by `1.0.0_SA_CTO~Z`, who declined an Andrew-approved alternate-certifier rec on
exactly this ground (9246) — the correct direction to err. Noted only because a stale line inside a
correct artifact carries that artifact's authority, which is the decomp's own §0.1 lesson applied to
the decomp itself.

---

## 3. WHAT I DID NOT DO

- **No TO minted, no cell edited, no artifact of the author's touched.** Verifier-not-fixer.
- **Did not re-run the author's own reads as corroboration.** Re-running an instrument a second
  time is repetition, not corroboration (Rule 22). The roster pull is a **different act** from the
  author's — I fetched the artifact and swept **all 21 fields**, which is not what the author ran.
- **Did not verify F1's proposed remedy.** `hierarchy.children[]` is a named candidate, INFERRED.
- **Did not open `org/surprise_channel/ETFS_SATELLITES/`.** No surprise item has been surfaced yet;
  the channel opens on first item, per `2.0.0_SA_COO~Z` (9253) and the COO ruling that executing
  seats do not write that tree.

## 4. APPENDIX — the 30 roster rows carrying `Satellite` or a `Sat` token

A denominator is an artifact, not a summary. `accountCount` in brackets.

```
MEMBER (9)   Opal Satellite 15 [3]   30 [4]   40 [18]   50 [83]   60 [81]
                              70 [39]  80 [65]  90 [0]   98 [11]
BLEND  (5)   Blended Opal / Satellite 50 [1] · Opal - Cash + Satellite 50 [1]
             Opal Sat 50+ 15% cash [1] · Opal UST/ Sat 70 [1] · Opal UST/Sat 80 33/67 [1]
OTHER (16)   Core / Satellite Equity [1] · Core | Satellite 30 [5] 40 [9] 50 [22] 60 [15]
             70 [13] 80 [9] 90 [0] 98 [9] · Core | Satellite CA Tax-Free 70 [2] 80 [3]
             Core | Satellite Tax-Free 30 [1] 40 [1] 50 [2] 60 [0] 70 [3]
```

-- `3.0.0_SA_CVO~Z`

---

# AMENDMENT 1 — 2026-08-27 ~16:5xZ. F1's REMEDY IS FALSIFIED; THE FINDING IS SHARPENED.

**Trigger:** `1.0.0_SA_CTO~Z` (9274) and `2.0.0_SA_COO~Z` (9275) both measured the one thing this
certification marked **INFERRED** — the `hierarchy.children[]` candidate — and it does not work.
**Recorded here rather than only in a message: a finding whose remedy has been falsified must not
be readable in its original form.**

## The measurement — ACCEPTED, NOT RE-DERIVED

`1.0.0_SA_CTO~Z`'s is the load-bearing one:

```
84 detail files, SYNCED WHOLE (not sampled)   -> the zero is over a denominator
121 child nodes, MAX DEPTH REACHED = 1        -> the zero covers the whole tree, not the depth
                                                 the walker happened to reach
child ids matching the 9 canonical satellites -> 0
POSITIVE CONTROL: 18 distinct child ids, 18 of 18 resolve to top-level models in the same feed
hierarchy.components[]                        -> list[0] on every model read
```

⭐ **The positive control is what makes the zero admissible.** It shows the matcher resolves every
child it sees and simply never resolves one to a satellite. Without it, the zero is
indistinguishable from a broken matcher.

⚠ **TWO SEATS, ONE RUNG — recorded so the agreement is not over-read.** `2.0.0_SA_COO~Z` reached the
same verdict on 4 specimens **by the same method** (a `children[]` walk). That is REPETITION of an
instrument, not corroboration by a second one. The finding rests on the 84-file run with its control;
the 4-specimen run adds confidence in that rung and no coverage of any other.

## What it actually showed — this reframes F1 rather than just closing a path

`Opal Sat 50+ 15% cash` composes `Opal Intermediate-Term` 0.5 / `Opal Short-Term` 0.15 /
`Opal Ultra Short-Term Income` 0.35 — **it never references `Opal Satellite 50`.**

>> **THE BLENDS HOLD THE SATELLITES' INGREDIENTS, NOT THE SATELLITES.** So Andrew's criterion is
   correct and describes a business fact **this feed does not encode**. IS-A vs HOLDS-A is not
   evaluable against rebalancer **at any depth** — not on the roster (§2 F1, mine), not on the
   detail (theirs). That is stronger than "F1 stands." <<

## CERTIFIER RULING — option (a), and it is NOT a compromise

**Ship the DECLARED NINE as data, labelled a declared set with a named owner, and amend `SAT-inv-2`
to say so on its face.**

⛔ **The reasoning is not "we tried and failed." It is A VALUE MUST CARRY ITS CLAIM, and `held` is a
legal claim value.** The membership set is `held` — sovereign-declared. **The defect was never that
the set is a list; it is that `SAT-inv-2` CLAIMS "a declared predicate over the roster" while the
mechanism IS a list.** That is a value carrying a false claim, fixed by correcting the claim, not by
manufacturing a predicate to make the claim true. **A fake predicate would be strictly worse than an
honest list — a `measured` label over a `held` value.**

**`SAT-inv-2`'s PURPOSE SURVIVES INTACT; only its wording bites.** Its stated rationale is *"a hand
list inherits someone else's omission,"* and its specimen is `Opal Satellite 98` missing from the
**partner's** table. **An Opal-declared, Opal-owned list is a different object from an inherited
one.** The invariant was written against *inheriting* a list, not against *holding* one.

### The review trigger — and it must NOT be a monitor

A declared list goes stale the day an `Opal Satellite 55` is created, so the trigger is the
load-bearing half. ⛔ **The alarm/monitor moratorium binds: no checker is proposed here.** The
trigger goes **inside `SAT-b-2`'s existing oracle**, which already runs — print the roster rows
matching the canonical `Opal Satellite <N>` form beside the declared nine, and **fail on any
symmetric difference in either direction.**

>> **WHY THIS IS NOT THE DISOWNED HEURISTIC RETURNING.** As a MEMBERSHIP PREDICATE the name form is
   wrong and Andrew ruled it so. As a DRIFT DETECTOR it decides only *"a human must look at this
   row"* — it never decides membership. **Same expression, different job, different correctness
   bar:** a false positive costs one question, where under the old use it silently admitted a book. <<

**Test the direction that ADDS rows too** — a new canonical row absent from the declared nine is the
case that matters, and an undercount announces itself while an overcount never does.

### Routed, not chased

`hierarchy.components[]` empty on every model read goes to the membership TO's owner as a question.
**UNUSED and UNPOPULATED are byte-identical from an empty array and take different remedies.**
Neither `1.0.0_SA_CTO~Z` nor this seat asserts a structural source exists elsewhere — one feed, one
date, and both have said so.

## EFFECT ON THE VERDICT

**CERTIFIED WITH FINDINGS STANDS.** No cell is invalidated; F1 was already P1 and its remedy path
narrowed. ⛔ **SHARPENED: `SAT-b-2` + `SAT-inv-2` are now BLOCKING FOR TO-MINT ON THE MEMBERSHIP
SURFACE SPECIFICALLY** — a TO cut against inv-2's current wording would instruct a builder to derive
something underivable. **The other five surfaces are unaffected and can be cut.**

## A NOTE ON THE MARKING THAT CAUSED THIS

The remedy was marked INFERRED because I had not run it. **That marking is why two seats measured it
instead of a TO being cut against it.** A remedy shipped inside a finding is still a claim, and it
inherits the finding's authority unless it is labelled out of it.

-- `3.0.0_SA_CVO~Z`

---

## AMENDMENT 2 — 2026-08-27 ~17:1xZ. **THE TO-MINT BLOCK IS DISCHARGED.** And Amendment 1's row was the split carrier.

Written by the SUCCESSOR `3.0.0_SA_CVO~Z` (launched ~16:55Z). The predecessor closed at 16:52Z.

### 1. THE ROW THAT WAS WRONG WAS MINE

Amendment 1's table carries **`F1 — RULED + REMEDY LANDED`**, evidenced as *"`SAT-inv-2` AMENDED at
`2758833b9f`"*. **That is TRUE OF s.3a AND FALSE OF THE NORMATIVE LINE.** `2758833b9f` was a **pure
append at `:170+`; it never touched `:118`**, where `SAT-inv-2` still carried the v1 wording
*"membership derives from a declared predicate over the roster."*

**No seat misreported anything.** COO~Z's commit subject said *"fix ... s.3a"* — accurate. COO~Z's
`/log` said *"SAT-inv-2 IS AMENDED"* — true of s.3a. Amendment 1 said *"AMENDED at `2758833b9f`"* —
true of s.3a. **Three accurate reports over one unmoved normative line.** The defect is the SPLIT
CARRIER: *an amendment written as an APPEND leaves the original in force, and every report about the
append is true while the artifact still instructs the opposite.*

⛔ **AND THE ROW WAS THE ONE AN ISSUER WOULD READ AS A DISCHARGE.** `1.0.0_SA_CTO~Z` — the seat that
cuts the membership TO — did **not** take it on trust; they opened `:118` before cutting (msg
20260827T170708Z). **That is the only reason a TO instructing a builder to derive an underivable
predicate was never minted.** The block was never lifted by anyone; this deliverable merely read as
though it had been. Recorded plainly because a certification deliverable is exactly where a false
discharge hardens.

### 2. THE DISCHARGE — RULED ON A READ OF THE NORMATIVE LINE, NOT ON A REPORT

`2.0.0_SA_COO~Z` landed the fix at **`936b9ae1e9`** and deliberately did **not** assert the condition
was met, inviting the read instead. Correct, and the read was done:

```
git show 936b9ae1e9:<DECOMP.md> | sed -n '113,146p'
  :118  **`SAT-inv-2` — MEMBERSHIP IS A DECLARED REGISTRY: an explicit, owned, versioned list
        of the nine members with a named maintainer — NOT an inferred predicate, and NOT an
        unowned hand list.**   <== AMENDED IN PLACE. The v1 wording is quoted beneath it and
                                   marked FALSIFIED AND MUST NOT BE BUILT AGAINST.
push state: 936b9ae1e9 is ON origin/SITEZ (ls-remote read: it IS the head)
```

⛔ **`SAT-b-2` + `SAT-inv-2` ARE NO LONGER BLOCKING FOR TO-MINT. THE MEMBERSHIP SURFACE IS CUTTABLE.**

The line now carries, in the block a builder actually opens: the amended invariant; an explicit stop
on the v1 wording; the derivation pointer to s.3a.2; **the price** (a declared registry does not
self-update — a tenth satellite is a REGISTRY EDIT and a missed edit is a SILENT absence); and the
**two-part remedy stated as composing, not competing** — registry owns the DECISION, `SAT-b-2`'s
symmetric-difference oracle catches the DRIFT at build time. A successor reading `:118` alone can no
longer inherit half a remedy.

### 3. THE UNFILLED MAINTAINER SLOT IS ACCEPTED, AND IT IS NOT A GATE

Both `1.0.0_SA_CTO~Z` and this seat asked that the maintainer be NAMED in the line. `2.0.0_SA_COO~Z`
deliberately left it unfilled, marked it an **OPEN CALL AT ANDREW in the line itself**, and said so
up front rather than letting a certifier find it. **This seat accepts that reasoning and adopts it.**

Membership here is a **PRODUCT FACT Andrew himself ruled** — he set the nine and personally disowned
both heuristic routes. **An owner assigned by inference IS the unowned-list failure this invariant
exists to refuse, merely with a name on it.** Filling the slot to satisfy the form would have made the
artifact look complete and be wrong in precisely the way the invariant names.

**A TO may be cut and BUILT against `SAT-inv-2` now.** The constraint is a SHIPPING condition — the
registry ships with its maintainer named — not a mint condition. **This is not a gate and must not be
relayed as one.**

### 4. SPLIT-CARRIER SWEEP — RUN, BECAUSE IT IS THE LESSON OF THIS VERY ITEM

Swept the estate for the falsified v1 wording surviving anywhere as if live (positive control: the
same sweep for the AMENDED wording returns 8 carriers, so the instrument finds what exists).

**No live carrier instructs a builder with the v1 wording.** Every surviving occurrence is one of:
inbox correspondence (correctly frozen history), the decomp's own quotations at `:121` / `:236`
(explicitly marked falsified), or **this deliverable at `:236` and the predecessor's session log at
`:111`** — where the v1 wording is quoted *as the thing being critiqued* by the F1 ruling.

⚠ **Those two are now HISTORICAL, not descriptive.** `:236`'s sentence — *"`SAT-inv-2` CLAIMS 'a
declared predicate over the roster' while the mechanism IS a list"* — was true when written and no
longer describes the artifact. **It is left in place rather than rewritten**: it is the reasoning that
produced the ruling, and a global substitution over one's own retraction is its own failure class.
This paragraph is the pointer that keeps it readable as history.

### 5. F-ROW STATUS AS OF THIS AMENDMENT

| finding | status | owner |
|---|---|---|
| F1 | **CLOSED. Remedy landed ON THE NORMATIVE LINE @`936b9ae1e9`; block DISCHARGED** | — |
| F2 | LIVE, P1 — four-postulate record for `modesFor(firm)`, correctly deferred behind `SAT-c-1` | `1.0.0_SA_CTO~Z` |
| F3 | LIVE, P1 — `Opal Satellite 60` named as the resolution-path mutant; **FIXTURE still owed** | DE via the TO cut |
| F4 | CLOSED (scope column withdrawn, not restated) | — |
| F5 | CLOSED | — |

**Everything else in this deliverable stands.** No cell verdict is disturbed by this amendment.

— `3.0.0_SA_CVO~Z`

---

## AMENDMENT 3 — 2026-08-27 ~17:4xZ. **F2 IS CERTIFIED AND DISCHARGED.** Plus a caution for TO-4's builder that the record does not carry, and a confirmed new `SAT-b-1` finding.

`1.0.0_SA_CTO~Z` submitted
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_SAT_C2_MODESFOR_FIRM_FOUR_POSTULATE_RECORD_20260827.md`
(@`d5b1139e9f`) for certification — **the issuer authoring it is not the issuer certifying it**, which
is the point of routing F2 rather than absorbing it.

### 1. VERDICT: **CERTIFIED. F2 (P1) DISCHARGED.**

**The two load-bearing code claims were re-read at this seat, at the record's own cited vintage**
(`portal` `origin/DEV` = `4ac152f8`, which I confirmed matches the citation — the local portal tree is
`eaa094e6`, and the record was right to read from the remote rather than the working tree):

```
AuthContext.tsx  else { claims = { firmId: null, ... } }   on !meResponse.ok   -- CONFIRMED
firmAccess.ts    isPathAllowedForFirm:
                   if (FIRM_EXEMPT_PATHS.has(path)) return true      <- a THIRD arm (see §2)
                   if (!firmId) return false                          <- deny arm 1
                   if (firmId === INTERNAL_FIRM_ID) return true
                   return FIRM_ALLOWED_PATHS[firmId]?.has(path) ?? false   <- deny arm 2
```

**Postulate (i)'s CE failure is CORRECT AND MATERIAL.** `firmId: null` is set when `/auth/me`
**fails** — an authenticated session whose firm is **UNKNOWN, not absent**. `null` is not a firm, so
*"every other firm"* does not cover it, and the domain is `firms ∪ {null}` with an uncovered member.
**The remedy — a TOTAL mapping with `null` → the two-pill set, failing closed — is right, and it is
the same distinction D1's `ND-e-1` protects one project over.** An identity outage must never hand
out a third firm's view.

**Postulates (ii), (iii), (iv) PASS as recorded.** (iv) is the one usually asserted rather than
demonstrated, and this record does demonstrate it: three remedies with **disjoint** effects
(onboarding a firm moves that firm's image; building the satellites mode moves `cottonwood` +
`opal-capital`; fixing the identity service moves `null` and nothing else moves it). The token census
carries its denominator (407 `.ts`/`.tsx`), is word-boundary and case-insensitive, and both proposed
names sit at **0** prior occurrence.

⭐ **STRENGTHENING, IN THE RECORD'S FAVOUR:** it cites `?? false` as the deny-default. There are in
fact **TWO** deny arms — `if (!firmId) return false` fires first and is the one that actually catches
`null`. The record's conclusion is right and its citation was narrower than the code.

⭐ **AND §1.4's SELF-DISCLOSURE IS THE PART TO KEEP.** The author scored the wrong directory first
(`head -1` selected `portal/etl/pages/positioning`, 1 file, 0 hits) and **got a clean zero from the
wrong plane** — then caught it, re-measured the right directory, and ran a positive control (105
files under `portal/src` DO contain `firm`) proving the zero is a true absence. **Disclosed rather
than quietly corrected.** That is the standard.

### 2. ⛔ A CAUTION THE RECORD DOES NOT CARRY — FOR TO-4's BUILDER, NOT AGAINST THE RECORD

The record holds `isPathAllowedForFirm` up as **"the model to copy."** For the deny-default, it is.
But that function has a **THIRD arm the record does not name**, and it returns `true` **before any
firm check runs**:

```
if (FIRM_EXEMPT_PATHS.has(path)) return true      <- FAILS OPEN, by design
```

**I measured what is in it: `FIRM_EXEMPT_PATHS` holds exactly one member, `/change-password`, and it
does NOT contain `/positioning`.** So the exemption does not touch the surface TO-4 gates, and the
record's characterisation is safe **for this surface**. ⚠ **But a builder told "copy
`isPathAllowedForFirm`" who copies the function's SHAPE imports a fail-open arm into a firm gate.**
The arm exists for a documented reason (a redirect loop on the change-password page) that has no
analogue in mode selection.

**Recommendation to `1.0.0_SA_CTO~Z`, not a gate:** in TO-4, name **which arm** is the model — the
deny-default — rather than the function. **This does not disturb the F2 discharge.**

### 3. `SAT-b-1` — CTO~Z's NEW FINDING, SHARPEST LIMB CONFIRMED AT THIS SEAT

`SAT-b-1` names six declarations and claims a partial add *"fails at the one that was missed."*
`1.0.0_SA_CTO~Z` measured **eight** mode-keyed sites of which only **three** fail loudly. **I did not
re-derive all eight — that is carried as their measurement — but I did read the limb the whole
finding turns on:**

```
origin/DEV:src/pages/Positioning/shared/bookSet.ts:353
  export const POSITIONING_MODES: readonly PositioningMode[] = ['models', 'etfs'] as const
```

**CONFIRMED: an array literal typed as a subset of the union, NOT an exhaustive `Record`.** Adding
`'satellites'` to `PositioningMode` produces **no TypeScript error here** — clean `tsc`, pill absent.

⭐ **AND IT IS DOING DOUBLE DUTY, WHICH THE FINDING DOES NOT YET SAY.** The same array is passed at
`Positioning.tsx:97` as the **validation set for the persisted mode toggle**, and the comment at
`:90-93` states the intent explicitly: *"a mode that stops existing cannot be restored from storage."*
**So one missing array entry silently breaks BOTH the pill list AND persistence validation** — and
the second failure is invisible even to someone who notices the missing pill.

**Endorsed into this certification as a sharpening of `SAT-b-1`'s oracle.** The cell edit is
`2.0.0_SA_COO~Z`'s call as author; `1.0.0_SA_CTO~Z` correctly did not edit another seat's artifact and
put it in TO-3's acceptance criteria instead.

### 4. F-ROW STATUS

| finding | status | owner |
|---|---|---|
| F1 | CLOSED (Amendment 2) | — |
| F2 | **CLOSED — record CERTIFIED @`d5b1139e9f`** | — |
| F3 | **LIVE, P1** — `Opal Satellite 60` named; FIXTURE still owed, carried in `ETFS_SATELLITES.TO-1` | DS lane |
| F4, F5 | CLOSED | — |
| **new: `SAT-b-1` oracle understates its own failure set** | **LIVE, P2** — 8 sites, 3 loud; `:353` doubles as the persistence validator | `2.0.0_SA_COO~Z` (author) |

— `3.0.0_SA_CVO~Z`

---

## AMENDMENT 4 — 2026-08-27 ~19:0xZ. **SCOPE FENCE against the ANDREW-DIRECT ~18:5xZ**, plus the measurement that settles the FACTUAL half of his fork.

Andrew ruled (recorded verbatim by `1.0.0_SA_CTO~Z` @`dc18f5a855`): *"we have to sort out
multi-tenant functionality for the 'Positioning' page … the patterns that govern these things need to
be deeply analyzed and an implementation spec designed and rigorously validated for potential
breakages."*

That is a **NEW PROJECT under Rule 27**, not an amendment to `ETFS_SATELLITES`. **This amendment adds
no verdict and re-opens nothing.** It exists because the new project's spec will reach for the
nearest certified artifacts, and **two of them are mine.**

### 1. ⛔ THE `modesFor` RECORD IS SCOPED TO A **PRESENTATION** DOMAIN AND DOES NOT TRANSFER

I certified `ctoZ_SAT_C2_MODESFOR_FIRM_FOUR_POSTULATE_RECORD_20260827.md` (Amendment 3). Its own
declared-domain line reads:

> **DECLARED DOMAIN:** *the viewer-firm identities this application can **present** a Positioning page to*

⛔ **RULE 24 POSTULATES ARE SCORED AGAINST THE DECLARED DOMAIN AND NOWHERE ELSE.** That record is
valid for **which firms may SEE which pills** — and it is **not** evidence about which firms may
RECEIVE which data. **If Andrew's *"nobody else"* means a data-access boundary, the domain changes,
and the record must be RE-AUTHORED against the new domain, not re-cited.** A four-postulate record
carried across a domain change is the untestable-criterion shape this project already refuses.

### 2. THIS CERTIFICATION MAKES **NO** AUTHORIZATION CLAIM — MEASURED, NOT ASSERTED

Sweep of this deliverable for `authoriz*` / `access boundary` / `served-artifact`: **zero matches**
before this amendment. **Nothing in it supports either reading of "nobody else", and nothing in it
supports a PROD promote.** `1.0.0_SA_CTO~Z` flagged the promote tension without treating it as a
ruling; **this seat adds only that no certification of mine is available as support for one.**

### 3. `SAT-c-3`'s GROUND IS **MEASURED AT THE CLIENT PLANE** — AND I DID NOT INSPECT IT WHEN I CERTIFIED IT

`SAT-c-3` declares the built gate a VISIBILITY gate rather than an authorization boundary, resting on
*"the underlying models payload is **already served to this viewer**; satellites are arithmetic over
it."* ⚠ **I certified the decomp containing that cell and did not inspect its ground.** I was drafting
this amendment to record the premise as *asserted, not measured* — **and that would have been wrong,
because `0.4.0_DE_ClientPlatform~Y` measured it at source (portal `797c4f8d`) before I committed:**

```
1  /positioning ALLOWLISTED FOR ALL FOUR PARTNER FIRMS (49financial · inflection · cottonwood ·
   demo, + opal-capital internal). Denominator 4 of 4.       [independently matches my own read]
2  SATELLITES IS ARITHMETIC OVER THE ALREADY-FETCHED MODELS PAYLOAD -- satelliteAdapter consumes
   the same positioningData the page already holds; Positioning.tsx adds NO query for satellites.
3  THEREFORE THE GATE REMOVES THE PILL AND THE MODE, NOT THE BYTES.
```

>> **SO `SAT-c-3`'s GROUND HOLDS, AND THE FORK'S FACTUAL HALF IS SETTLED AT THE CLIENT PLANE: a
   non-Cottonwood viewer's browser ALREADY HOLDS the constituent data. If *"nobody else"* is a
   UI-VISIBILITY statement, the shipped gate satisfies it today. If it is a DATA-ACCESS boundary, the
   shipped gate CANNOT satisfy it and CANNOT BE MADE TO client-side — the work moves server-side and
   becomes a security review.** <<

⛔ **WHAT REMAINS UNMEASURED IS THE *EDGE* PLANE, AND THE MEASURING SEAT FENCED IT THEMSELVES.**
`getPositioningData` carries a comment reading *"DEMO: Using public endpoint (no auth)"*, and
`0.4.0_DE_ClientPlatform~Y` **explicitly refused to relay it as measured** — recording only what they
did read at source, that `apiRequest` attaches a bearer whenever a token exists, so the **client**
always sends one. ⭐ **Whether the served route REQUIRES it at the edge is a serving-plane fact nobody
has measured, and a comment is a claim about a vintage, not about the running system.** **If the fork
settles as ACCESS, that edge posture is the first thing needing measurement — and it needs measuring
rather than reading.**

⛔ **I am not taking that measurement**: it is a serving-plane act outside this seat, and the standing
refusal holds — **nobody goes credential-hunting; if a bearer legitimately exists for this purpose,
the seat that holds it says so.**

### 4. ⭐ ONE ARTIFACT ALREADY CARRIES THE RESERVED QUESTION

`modeAccess.ts` states **on its own face** that the gate is a visibility gate and not an authorization
boundary, **with the reason** (*a client-side decision cannot be an authorization boundary, because
the bundle ships to the viewer; authorization lives at the API boundary*) **and with what would be
required if the intent were the other reading** — instructing a successor **not to "strengthen" the
file into a boundary but to MOVE the decision.** **A file that tells the next author which of two
designs it is NOT, and where the other one would live, is the shape that survives a scope change.**

### 5. WHAT IS UNCHANGED

**Every verdict in this certification stands.** Round 1 is certified and closed; F1/F2/F4/F5 closed,
F3's fixture owed at the DS lane, the `SAT-b-1` oracle finding LIVE with `2.0.0_SA_COO~Z`. ⛔ **The
sovereign question — visibility or access — is Andrew's. `1.0.0_SA_CTO~Z` put it to him correctly,
`0.4.0_DE_ClientPlatform~Y` supplied its facts without adjudicating it, and this seat is not
answering it in either direction.**

— `3.0.0_SA_CVO~Z`

---

## AMENDMENT 5 — 2026-08-27 ~19:5xZ. **THE FORK AMENDMENT 4 DECLINED TO ANSWER IS ANSWERED: (b) ACCESS.** One line, because a certification that says "this is open" when it is closed is the same stale-carrier shape.

Andrew-direct ~1946Z, *"recs approved"*, recorded by `1.0.0_SA_CTO~Z` @`5f60dd944a`. **CALL 1 —
*"nobody else": visibility or access?* — settled as ACCESS.**

### What this closes in this certification

Amendment 4 stated: *"the sovereign question — visibility or access — is Andrew's … this seat is not
answering it in either direction."* **That was correct then and is now resolved.** The consequence
Amendment 4 predicted is the operative one:

>> **THE `modesFor` FOUR-POSTULATE RECORD MUST BE RE-AUTHORED AGAINST AN ACCESS DOMAIN FOR R5, NEVER
   RE-CITED.** Its declared domain is *"the viewer-firm identities this application can **PRESENT** a
   Positioning page to."* **The fork settled the way that voids the transfer**, and Rule 24 postulates
   are scored against the declared domain and nowhere else. A record still declaring "present" would
   **pass its own test and answer the wrong question.** <<

### `SAT-c-3` is NOT falsified, and the distinction is exact

`0.4.0_DE_ClientPlatform~Y` drew it at source and this seat adopts it rather than re-deriving:

| | |
|---|---|
| **STILL TRUE** | the gate **is** a visibility gate, is **not** an authorization boundary, and **cannot be made into one** — a property of running client-side, not a design choice |
| **NOW WRONG** | reading it as the **whole** control. **Necessary and not sufficient**: it hides the pill and refuses the persisted-toggle tamper, and it does **not** withhold the bytes |

**So `SAT-c-3` remains accurate about what was built. What it lost is an implicit adequacy claim it
never stated.** ⭐ **Nothing `0.4.0_DE_ClientPlatform~Y` built is invalidated** — it is one layer of a
two-layer control.

### ⭐ AND THE CARRIER SHAPE THEY NAMED IS WORTH KEEPING

`modeAccess.ts` reserved the other reading as a **conditional** — *"IF this is ever meant to be an
authorization boundary…"* — written as a precaution against drift, and then answered.

>> **A COUNTERFACTUAL CONDITIONAL ABOUT A SETTLED QUESTION IS A STALE CARRIER: every word in it stays
   true, and the reader draws the wrong conclusion because the world moved underneath it.** Worse
   here than usual, because R5's implementer opens that file **first** — `1.0.0_SA_CTO~Z`'s R4 names
   it as the artifact that *"may save the spec a step"* — **so the stale reading would have been found
   by exactly the person it would mislead.** <<

**Verdict unchanged: CERTIFIED WITH FINDINGS.** Round 1 remains certified and closed; the
`ETFS_SATELLITES` PROD promote is held by Andrew's ruling flowing through `1.0.0_SA_CTO~Z`'s
pre-stated consequence, **not by anything in this certification** — which carries no support for a
promote in either direction.

— `3.0.0_SA_CVO~Z`

---

# ⛔ CORRECTION — 2026-08-27 ~23:5xZ — MY "VACUOUS CORPUS / THE ANCHORING IS UNSUPPORTED" FINDING IS FALSE. I VARIED THE NOTATION AND HELD THE DISCRIMINATOR CONSTANT.

**Falsified by `2.0.0_SA_COO~Z` (msg 11132). I re-measured at this seat before accepting it, on the
fixture, and they are right.** The finding was **message-only and had no durable carrier** — this
section is that carrier, written because a message-borne false claim cannot be corrected by another
message alone.

## WHAT I CLAIMED

> *On the 65-row roster the anchored regex and a bare substring check admit the IDENTICAL 9 rows, so
> the measurement cannot support the anchoring; and the adversarial case Andrew named is ABSENT from
> the fixture.*

## WHAT IS TRUE — `tests/fixtures/satellites/roster_2026-08-27.json`, 65 rows, `pageCount=1`

```
ANCHORED    ^Opal Satellite (\d+)$        ->  9
MY CONTROL  "opal satellite" substring    ->  9     ADMITS BEYOND ANCHORED:  0
TRULY BARE  "satellite" substring         -> 27     ADMITS BEYOND ANCHORED: 18
TRULY BARE  /sat/i                        -> 30
'Core | Satellite 98' in corpus: True     'Opal Satellite 98' in corpus: True
```

**BOTH LIMBS FALSE.** The bare substring admits **27, not 9** — the anchor excludes eighteen rows
including the entire `Core | Satellite *` family. And the adversarial case is **present**:
`Core | Satellite 98` sits in the corpus beside `Opal Satellite 98`, which is `SAT-b-4`'s named pair.

## ⛔ THE MECHANISM, AND IT IS THE PRECISE ONE

> ### MY "BARE SUBSTRING" CONTROL CONTAINED THE WORD `Opal` — THE ANCHOR UNDER TEST.

**I varied the NOTATION (regex vs. substring) and held the DISCRIMINATOR (the token `Opal`)
constant.** Both arms were anchored. A control built that way **cannot** separate the hypotheses, so
its agreement was guaranteed before I ran it — and I read that guaranteed agreement as *evidence that
anchoring does no work*. ⛔ **The measured discriminating power of my control was ZERO rows, and zero
discriminating power is exactly what "the two instruments agree" looks like from inside.**

⛔ **AND THE ABSENCE CLAIM WAS MANUFACTURED BY THE SAME STRING.** I concluded *"the adversarial case
is absent from the fixture"* from a search whose pattern **structurally excluded** the adversarial
case. *A search for `opal satellite` cannot find `Core | Satellite 98`, and its silence is not the
corpus's.*

## WHAT THE PREDICATE ACTUALLY IS — and it was never unvalidated

`satellites_registry.py:213-218` carries `CANONICAL_NAME_FORM = re.compile(r"^Opal Satellite (\d+)$")`
under a comment naming this exact pair:
> *"⛔ READ THE ANCHORS. `^...$` is load-bearing twice over: `Core | Satellite 98` does not match …
> `Opal Satellite 50 Tax-Free`, were it ever minted, would not match either, so it surfaces as DRIFT
> for a human rather than being silently absorbed as a member."*

**The author anchored it deliberately, against the real mutant, and documented why.** My finding
implied the anchoring was unjustified decoration. **It is the load-bearing part of the predicate**,
and `2.0.0_SA_COO~Z` further established the classification is not open at all — Andrew ruled it at
~16:1xZ (`SAT-b-2`, IS-A vs HOLDS-A), *seven hours before any of us began asking.*

## WHAT MOVES

**`F3` and the "fixture still owed" line stand** — a fixture obligation is untouched by this. **What
is withdrawn is any suggestion that the membership predicate is unvalidated, that the corpus lacks a
negative case, or that the classification is an open sovereign question.** All three were mine and
all three were wrong. **The verdict of this certification does not change; a finding inside it is
retracted.**

⚠ **Third instance tonight of one class: a control that shares the property under test.** Banked at
`[[a-control-that-shares-the-property-under-test]]`. *Twice I caught it myself; this time a peer did.*

---

## ⛔ PRECISION AMENDMENT TO THE CORRECTION ABOVE — 2026-08-28 ~00:0xZ — "THE ANCHOR EXCLUDES 18 ROWS" IS ITSELF A MISATTRIBUTION. THE TOKEN DOES. BOTH ANCHORS MEASURE +0.

**The correction above is right that my original finding was false. Its ATTRIBUTION is wrong, and
the wrong attribution is what travelled.** Raised by `0.4.0_DS_ClientPlatform~Z` (11185), who then
self-corrected the same misattribution (11194); independently measured here by one-limb ablation.

```
ABLATION -- drop EXACTLY ONE component, hold the rest (65-row roster)
  FULL          ^Opal Satellite (\d+)$      ->  9
  drop  $       ^Opal Satellite (\d+)       ->  9    extra admits: +0   UNEXERCISED
  drop  ^        Opal Satellite (\d+)$      ->  9    extra admits: +0   UNEXERCISED
  drop  `Opal`  ^Satellite (\d+)$           ->  0    disagreement: 9    <- THE TOKEN CARRIES IT
  bare  /satellite/i                        -> 27    extra admits: +18  <- Core | Satellite 98 lives HERE
POSITIVE CONTROL (2 synthetic rows appended, engine demonstrably fires):
  + "Opal Satellite 50 Aggressive"  -> exercises the TRAILING $   (+1)
  + "Legacy Opal Satellite 50"      -> exercises the LEADING  ^   (+1)
```

> ### THE 18 ROWS BELONG TO THE LITERAL TOKEN `Opal`, NOT TO EITHER ANCHOR. `Core | Satellite 98` DOES NOT CONTAIN `Opal Satellite` AT ALL, SO NO ANCHOR EVER GETS A CHANCE TO ACT ON IT.

⛔ **MY ERROR HERE IS THE SAME CLASS AS THE ONE I WAS CORRECTING, ONE LEVEL UP.** My original control
varied four things at once (token, both anchors, the digit requirement) and I attributed the whole
delta to one of them. **A COMPOSITE COMPARISON CANNOT ATTRIBUTE** — it can only tell you *something*
in the bundle matters. *I diagnosed "varied the notation, held the discriminator" correctly and then
committed its sibling in the same breath.*

## ⛔ AND THE OVER-BROAD RETRACTION REACHED A SPEC IN TWENTY MINUTES

`1.0.0_SA_CTO~Z` (11188, 11203) traced it: my withdrawal was **broader than my error**, and
`TO-5-DS`'s `AC4` was issued saying *"DO NOT CONSTRUCT A FIXTURE."* **Correct for the token limb.
Fatal for the anchors** — a predicate with `$` deleted scores 9/9 and passes `AC4` on the `SAT-b-4`
pair, so the criterion cannot fail in the direction the `$` exists to defend.

> **The false finding cost a broadcast. The over-broad retraction of it nearly cost a shipped gate.**
> ⚠ **Four seats reviewed the retraction and agreed with it. Nobody audited its SCOPE** — *a
> withdrawal reads as humility, and humility is not audited.*

**WHAT STANDS UNCHANGED:** the anchoring is not decoration; `satellites_registry.py:213` was written
against a real mutant; the classification is ruled, not open. **WHAT IS ADDED:** the corpus exercises
the **token** and neither **anchor**, so `AC4` needs the real pair **plus** synthetic rows —
`1.0.0_SA_CTO~Z`'s amendment (11203) carries the three-row form, including the MUST-ADMIT
`Opal Satellite 55` that no real row can ever supply.

⭐ **Banked: a composite comparison cannot attribute — [[a-composite-comparison-cannot-attribute]].**
