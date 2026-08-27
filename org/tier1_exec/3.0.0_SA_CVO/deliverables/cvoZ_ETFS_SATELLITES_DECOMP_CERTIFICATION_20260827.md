# ETFS_SATELLITES STAGE-3 DECOMP — CERTIFICATION

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
