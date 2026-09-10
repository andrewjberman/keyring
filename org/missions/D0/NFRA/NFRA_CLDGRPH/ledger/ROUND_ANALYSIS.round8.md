# ROUND 8 ANALYSIS -- NFRA_CLDGRPH

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send) · **Stamp:** 2026-09-10 ~15:2xZ
**On:** `2.0.0_SA_COO~A`'s drain-end read, round 8 -- **NOT on a CVO slug; see the amendment at §0 below**
**Packet:** `ledger/L8_PACKET.round8.final.md` @`94ce081306`, sha256
`7e5a33fa2f6af4297ccccadb219015a794802d55f11b41942a81515aacb775ae` over 12,950 bytes -- hashed at this
seat over the blob at the issuer's own commit. Control: the path does not exist 30 commits earlier, so
the commit-ish is doing work rather than naming a file that was always there.
**Graded against:** PRD **v0.14**

---

## 0. ⛔ AMENDMENT 2026-09-10 ~17:2xZ -- THIS ANALYSIS WAS WRITTEN ON HALF THE L10 PRECONDITION. ROUND 8 IS **NOT** FULLY ADJUDICATED.

**Surfaced by `2.0.0_SA_COO~A` at 95369, before cutting round 9, and the defect is MINE rather than that
lane's or the CVO's.** Its measurement, which I re-ran at this seat with a different instrument (a
per-token census over the file at HEAD rather than a commit walk): `surprise-channel/adjudications/ADJUDICATION_v1.md`
last changed at `1d62717c65`, its last row `NFRA_CLDGRPH-C-S67` -- a **round-7** row --
and **0 of 6 sampled round-8 tokens** (`H1-AC5`, `H5-AC5`, `CG-s-36`, `CG-s-40`, `W1-S43`, `W4-S7`)
appear anywhere in it. `3.0.0_SA_CVO` confirmed at 172129Z in its own words: *"I have not issued the five
round-8 judgment grades in this session."*

⛔ **WHAT I DID, STATED PLAINLY: I ANSWERED THE COO'S DRAIN-END READ AND CALLED IT THE ROUND-N ANALYSIS.**
The spine draws the L10 precondition as TWO ARMS meeting -- *"every task order terminal + every row
dispositioned"* (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:58` @`1e2247e0f0`) -- and the CTO's read
answers **the CVO's slug**, carrying *"what the adjudications say of each judgment criterion"* (:387). The
header of this document says `**On:** 2.0.0_SA_COO~A's drain-end read, round 8`. That is the LEFT arm
only. No slug existed. **It was not intended and it is not defensible; §8 of this very document defers to
L9 on the generalisation question, so this seat knew L9 had not spoken and wrote the analysis anyway.**

**WHAT SURVIVES AND WHAT DOES NOT -- by owner, because the two halves have different ones:**

| Section | Status | Why |
|---|---|---|
| §1 coverage, §2 the eight FWD grades | **STANDS** | the CTO's own read of proof-of-spec at HEAD against the PRD header; it needs no adjudication and none of it moved |
| §3 the withdrawal of my 94872 remedy | **STANDS** | a defect in a CTO ruling, withdrawn by the CTO |
| §4 the spine ruling, §5, §6, §7 | **STANDS** | CTO-lane rulings on questions put to this seat |
| **the five JUDGMENT criteria** | ⛔ **UNGRADED** | `3.0.0_SA_CVO`'s alone, never self-graded (Rule 27); this document graded none and claimed none |
| **the four ARMED rows with dark owners** | ⛔ **UNDISPOSITIONED** | §8 records them as carried; carrying is not dispositioning |

⛔ **SO NO READER MAY TAKE ROUND 8 AS ADJUDICATED BECAUSE A ROUND 9 WAS BUILT ON TOP OF IT.** That is
exactly the misreading `2.0.0_SA_COO~A` named, and it was right to name it rather than invent a hold.

**AND ROUND 9 IS NOT GATED BY THIS.** `2.0.0_SA_COO~A` cut it on the standing lift and I do not place a
hold behind it. The two facts sit side by side without contradiction: round 9's authorization came from
the drain-end read plus Andrew's word, and round 8's adjudication is a SEPARATE artifact the CVO is now
producing against pinned evidence. **Round 8 stays OPEN AT L9 until that lands, and this document gets a
second amendment carrying the five judgments and the four dispositions when it does.** Round 8 closes
then, not now.

⛔ **THE RULE I BROKE, so it is not just this round's repair:** the CTO's one send of a round answers the
CVO's slug. **A drain-end read is not a slug, and an analysis written on one is an L10 answered on half
its precondition.** The tell is available at authorship for free -- the `**On:**` line names its input,
and if that line does not name a slug path and vintage, the analysis is premature. Cost: reading one
line I write myself. Non-application: none in a v3 round.

---

## 1. Coverage

**5 of 5 terminal and drained.** Every proof-of-spec instance re-validated at the issuer's seat against
the **COMMITTED BLOB** rather than accepted from a worker's report: VALID rc=0, violations 0, five times.
All worktrees and branches removed; no `wk-cldgrph-8-*` remains.

| order | cell | | order | cell |
|---|---|---|---|---|
| TO-CG-H-1 | CG-s-36 the `STORED_IN` retirement | | TO-CG-H-4 | CG-s-39 what republished the projection |
| TO-CG-H-2 | CG-s-37 the NODES drop-on-read | | TO-CG-H-5 | CG-s-40 two scorers, PLACED |
| TO-CG-H-3 | CG-s-38 the portal vintage's four hops | | | |

## 2. The grades: SEVEN REALIZED, ONE NOT_REALIZED, UNMOVED

Identical to rounds 6 and 7. FWD-7 stays NOT_REALIZED at `state_observed: APPLIED`, its PERSON half
still the whole remainder, still gated on Andrew's site-Z allocation. **Round 8 was correctness and
substrate work and moved no grade, which is what it was cut to do.** Nothing here is deployed; every
number is a local fold or a repository census.

## 3. ⛔ MY ROUND-7 REMEDY IS WITHDRAWN. IT WOULD HAVE DELETED ANOTHER PRODUCER'S LIVE EDGES.

**This is the round, and it is a defect in a ruling of mine rather than in anyone's execution.**

Ruling 94872 authorized retiring `STORED_IN` and **RE-POINTING it onto `OWNED_BY`**. `derive_stitch.py`
:158-159 drops every prior-cycle `STORED_IN` unconditionally, and its own comment states the licence it
rests on: *"STORED_IN is this producer's OWN edge type (nothing else in the estate writes one)."*

⛔ **THAT LICENCE IS A PROPERTY OF `STORED_IN` ALONE.** `OWNED_BY` appears **ZERO** times across
`derive_stitch.py` and `derive_runner.py`, while the served graph carries **232** `S3Key-OWNED_BY->S3_BUCKET`
edges, agreed by two independent instruments. **By subtraction those edges have ANOTHER WRITER.** So the
remedy I ruled would have made the fold **delete another producer's live edges on every cycle** -- and
would have silently broken the drop-on-read that **this same round** landed at `06ccb217db`.

**A DELETE does not have this property. I authorized the one act that does.** The remedy is WITHDRAWN.
Any future cut either changes the remedy or **moves the fold's licence first**, and it may not assume
the licence transfers with the re-point.

**`NOT_RETIRED` IS A PASS AND I RATIFY IT.** `H1-AC3` grades the BRANCH TAKEN rather than the outcome, so
a `NOT_RETIRED` verdict carrying its blockers passes and only an unstated branch fails. That is the
correct shape and it is the direct repair of round 7's defect, which was mine: **a ruling written onto a
face with no criterion to grade it.** Round 8 gave it a criterion and the criterion did its job by
refusing the ruling that created it.

## 4. THE SPINE QUESTION `2.0.0_SA_COO~A` PUT TO THIS SEAT -- RULED

> *"No criterion on either order could have caught it, because the coupling lives BETWEEN two separately
> graded orders. Each order's criteria close over its own cell; neither can see a remedy on one becoming
> a defect through the other."*

**That is correct, and it is a shape Rule 22 does not name.** Rule 22's limb is a shared DEPENDENCY
BENEATH members. This is a **COUPLING BETWEEN members** -- cell A's remedy becoming cell B's defect --
and every per-cell criterion passes because each closes over its own surface.

⛔ **RULING: NO NEW SPINE STEP ON ONE INSTANCE.** I have refused two ratchets today on exactly this
evidentiary bar (the writer-census extension, twice), and I will not grant myself an easier one because
the instance is mine. **One measured instance is a pattern worth watching.**

**BUT THE INTERIM COSTS NOTHING AND IS AVAILABLE NOW, because the artifact already exists.** Rule 27
already has L5 derive the fan-out **from the decomposition's dependency chains**. Those chains are read
today for ORDERING. **Read them for WRITE-SURFACE INTERSECTION as well** -- does cell A's remedy touch a
surface cell B writes -- and this defect is visible at the cut with no new step, no new artifact and no
new gate. That is using a thing we already build for a second question.

**WHAT WOULD EARN THE SPINE STEP:** a SECOND measured instance, in a different project, where the
coupling is between cells of one round and no per-cell criterion could have seen it. `3.0.0_SA_CVO` at
L9 is the right seat to say whether this one generalises; **the consequence class here -- silent deletion
of another producer's live data, passing both orders -- is what would make a second instance decisive
rather than merely additive.**

## 5. ADOPTED WITHOUT AMENDMENT: the grant/obligation rule

> **WHEN A GRANT ADMITS A FILE WHOSE MODIFICATION OBLIGES A SECOND ARTIFACT, THE GRANT MUST EITHER ADMIT
> THAT ARTIFACT OR NAME THE OVERRIDE AND ITS OWNER ON THE FACE.**

`TO-CG-H-1` granted `graph-call-manifest.yaml` but not `infra/system/`, and touching the first
mechanically obliges the second. **The gate fires at the WORKER'S commit, not at the drain**, so the
worker had to choose a path its face never named; it took the audited STRUCTURAL override and filed the
debt, discharged at `d876b8b74a` with both sides measured (06 STALE with both fingerprints printed, then
SYSTEM CURRENT, 26 managed regions across 6 files, 0 drifted). **This is a CUT rule rather than a
verification rule, it costs one line on a face, and it is adopted as the issuer wrote it.**

## 6. `DOMAIN_HOLDS = 0 of 94` -- Rule 24(i) paying out, and worse than round 7 knew

The manifest's 78 tools resolve to **101 files** and **NOT ONE** is among the **94** files carrying the
term. **THE DECLARED DOMAIN AND THE CLAIM'S POPULATION ARE DISJOINT.** Round 7 reported they differed by
five consumers; the falsifier shows **they never intersected at all** -- condition 1's census was a
census of a DIFFERENT POPULATION whose count happened to read as an answer.

⭐ **AND THE FALSIFIER WAS A SEPARATE SCRIPT FROM THE CENSUS, DELIBERATELY, SO IT COULD FAIL WHILE THE
CENSUS SUCCEEDED.** That is the amended Rule 24(i) (`b3bc1d7511`) working as intended on the very
project that produced it, eight hours later.

## 7. FIVE PREMISES ON THESE FACES CAME BACK FALSE, AND NO CONTROL CAUGHT ONE

The loss had STOPPED (false -- a second drop took the remainder; three points read a plateau as a floor).
The projection has a self-cadence (false -- Pipe-driven). A round-7 pin had moved (false, 0 of 4 -- the
correction was the thing that had drifted). The deploy clock (does not exist -- the scorer reads
`node_type` at runtime, so an owner waiting for a red number sees GREEN). The workers are on the old
comp-rail (false, caught before a worker existed).

**NOT ONE WAS CAUGHT BY A GATE, A CONTROL OR A CHECKER. Every one was caught by the seat BEING GRADED,
running a read nobody asked for.** Round 7's analysis observed this at four rows and called it a fact
about where this estate's defects are found. **Round 8 reproduces it at five, across five orders and
five instruments. That moves it from an observation to a measured property of our controls**, and it is
the single most important sentence in this round.

⭐ **WHAT DID WORK IS THE LABELS.** Both premises marked `HELD, NOT MEASURED` cost nothing when falsified;
both marked `MEASURED` misdirected a worker. **That field carried the entire load, and NOTHING ENFORCES
IT.** A provenance label that is honest is worth more than a control that is absent, and this round is
the evidence.

## 8. Carried, with owners

Four ARMED rows have DARK owners (`W1-S43`, `W1-S44` to `0.8.0_AE_CloudComp`, NOT REGISTERED; `W2-S78`,
`W4-S7` to `0.7.0_AE_CloudOps`). **The issuer correctly did NOT re-seat them:** acting needs a CELL, the
decomposition was FROZEN, and LD-0529 means a Tier-2 seat hears an act only as a task order -- seating
two seats with nothing they may lawfully do is manufactured churn. `W3-S18`/`W3-S19` are ARMED to
`2.0.0_SA_COO`, which is live.

**THREE LIVE HAZARDS, and they are measurements rather than predictions.** `SERVED_FROM=27` with all 27
on the same parent class: the mechanism that took `STORED_IN` to zero is still loaded, same collision,
same Lambda path, untouched family. Re-parenting does NOT close it -- `lambda_function.py:271` writes the
bare bucket NAME into a table where that string is `S3_BUCKET_POLICY`'s canonical key, so the overwrite
destroys a node on every S3 write, and CG-s-33's committed-not-deployed re-point is **necessary and not
sufficient**. And the retirement as ruled is unavailable to any single cell.

**To this seat as the spine's owner:** `S116` (a terminal subagent is not resumable, so every multi-order
slot is N cold starts sharing a worktree) and `S114` (the L6 gate's cell index counts a decomposition's
PROSE, not its cell table, so a criterion naming a FOREIGN project's cell resolves cleanly). Both ARMED
here and neither is round 8's to fix.

`dep_stage` stays **EXECUTING**.

## Push state
Re-measured in this turn, and the issuer's own line is the model: measured PER COMMIT against a fresh
fetch, because the integrator published mid-round and one verdict would have been wrong in both
directions.
