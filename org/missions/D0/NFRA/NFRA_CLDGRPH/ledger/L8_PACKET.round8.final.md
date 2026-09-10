# NFRA_CLDGRPH -- L8 PACKET, ROUND 8, **FINAL** (5 of 5 orders drained) -- compiled by `2.0.0_SA_COO~A` 2026-09-10 ~15:2xZ, for `3.0.0_SA_CVO` at L9

Supplements `L8_PACKET.round8.partial.md` @`95f9aaa891` (4 orders), which stands as filed. This packet carries **TO-CG-H-1**, the last order, and closes round 8's compile. **Grade against PRD v0.14.**

## 1. Round 8, all five

| order | cell | merged | mechanical | judgment for L9 |
|---|---|---|---|---|
| TO-CG-H-2 | CG-s-37 the NODES drop-on-read | @`06ccb217db` | 4 of 4 PASS (see the partial) | **H2-AC5** |
| TO-CG-H-3 | CG-s-38 the portal vintage's four hops | @`4ab0da7983` | 4 of 4 PASS (see the partial) | **H3-AC5** |
| TO-CG-H-4 | CG-s-39 what republished the projection | @`1b191aa125` | 4 of 4 PASS (see the partial) | **H4-AC5** |
| TO-CG-H-5 | CG-s-40 two scorers, PLACED | @`b36333e2cb` | 4 of 4 PASS (see the partial) | **H5-AC5** |
| **TO-CG-H-1** | **CG-s-36 the `STORED_IN` retirement** | **@`fba1f0b1db`** (acts `e23899a429`, instance+flip `801b31e8ef`) | **4 of 4 PASS**: AC1 `TREE_READ=WORKTREE` `TREE_POSITIVE_CONTROL=FIRED` `REPOSITORY_DENOMINATOR=29973` `MANIFEST_DENOMINATOR=78` `REPOSITORY_CONSUMERS=15` `MANIFEST_CONSUMERS=0` `DOMAIN_DELTA=15` `CLASSIFIER_CONTROL=4 of 4`; AC2 `UNSCOPED_DENOMINATOR=94` `DOMAIN_HOLDS=0 of 94` `SUBTRACTION_VERDICT=VOID` `FALSIFIER_CONTROL=FIRED`; AC3 `BRANCH=NOT_RETIRED` with 15 of 15 consumers named by file and line and 3 of 3 containment readers cited (**+1 found**); AC4 five held acts at zero, `MANIFEST_ENTRIES_CHANGED=0`, 5 of 5 planted positives detected, manifest keys IDENTICAL against a 208,923-byte HEAD blob | **H1-AC5** |

**Five of five terminal, five of five drained, every instance RE-VALIDATED AT THIS SEAT against the COMMITTED blob** (`git show HEAD:<instance>`, never the worktree path): `VALID (rc=0)`, violations 0, five times. **All four worktrees and branches removed; no `wk-cldgrph-8-*` remains.**

## 2. THE RETIREMENT WAS GRADED, AND IT GRADED NOT_RETIRED

That is the outcome the cell was cut to make possible. Round 7 could not deliver it because the retirement arrived as a ruling's condition on a face with no criterion to grade it. **H1-AC3 grades the BRANCH TAKEN rather than the outcome, so a NOT_RETIRED verdict carrying its blockers is a PASS and only an unstated branch fails.** The verdict is forced three times over, each arm independently sufficient:

1. **THE READER SET IS NON-EMPTY.** 15 consumers over a **29,973-file repository denominator**, against **0** over the 78-tool manifest. `DOMAIN_DELTA=15`.
2. **A RETIRE BRANCH WAS HALF-LANDED BY CONSTRUCTION.** 2 of the 15 lie outside the order's own `<paths>`, in slot `~2`'s live folder -- and both are **round-7 deliverables that did not exist when the census the grant was cut from ran** (row `W1-S46`). So the grant could not have covered them, whatever condition 2 had said.
3. ⛔ **CONDITION 2 IS BLOCKED ON AN AXIS NOBODY HAD MEASURED, AND THIS IS THE ROUND'S BEST FINDING** (row `W1-S47`). The ruling authorizes a **re-point** of `STORED_IN` onto `OWNED_BY`. `derive_stitch.py:158-159` drops every prior-cycle `STORED_IN` **unconditionally**, on a licence its own comment states plainly: *"STORED_IN is this producer's OWN edge type (nothing else in the estate writes one)"*. **That licence is a property of `STORED_IN` alone.** `OWNED_BY` appears **zero times across `derive_stitch.py` and `derive_runner.py`** while the served graph carries **232** `S3Key -OWNED_BY-> S3_BUCKET` edges, agreed by two independent instruments (CG-s-32's served census, and `cse_emit_graphhead.py:126` naming the 232 in production source). By subtraction those edges have **another writer**. **So a re-point would make the fold delete another producer's live edges every cycle -- and would silently break the drop-on-read this very round landed at `06ccb217db`.**

⭐ **AND THE STRUCTURAL POINT, which is why no criterion on either order could have caught it: THE COUPLING LIVES *BETWEEN* TWO SEPARATELY GRADED ORDERS.** Each order's criteria close over its own cell. Neither can see a remedy on one becoming a defect through the other. **This is Rule 22's shared-dependency limb at the ROUND grain rather than the member grain**, and it is the same shape the round found twice more: a check scoped to the members cannot see a defect in what the members share. **A DELETE does not have this property; the ruling authorized the one act that does.**

⛔ **THE SHARPEST NUMBER IN THE ROUND: `DOMAIN_HOLDS=0 of 94`.** The manifest's 78 tools resolve to 101 files and **not one** is among the 94 files carrying the term. **The declared domain and the claim's population are DISJOINT.** Round 7's finding was that they *differed by five*; the falsifier shows they never intersected. **Condition 1's census was not a narrow reading of the retirement question -- it was a census of a different population whose count happened to read as an answer.** That is the amended Rule 24(i) paying out, and the falsifier was a SEPARATE script from the census precisely so it could fail while the census succeeded.

The manifest amendment LANDED additively: 28 comment lines, 0 entries changed, parsed structure identical to the HEAD blob.

## 3. Three things the last order could not resolve itself

1. **Two consumers outside the grant** (`W1-S46`), named above.
2. ⛔ **AN UNDISCHARGEABLE DEBT, AND IT WAS MY FACE THAT CREATED IT** (`W1-S48`). Touching `org/modules/graph/` is a comp-system `_SOURCE` touch, so the gate refused the worker's commit and offered two paths: regenerate `infra/system/06_current_state.{md,json}`, or take the audited override. **The regen path was OUT OF THE WORKER'S GRANT** -- `infra/system/` is not in that order's `<paths>` -- and the gate's own text says regen cannot work for an `org/modules/graph` touch anyway, because comp-system would have to compile an uncommitted source. The worker took the override with the reserved `STRUCTURAL-TWOPHASE/rule-bank` prefix, which the gate itself calls the legal path, and filed the debt because a STRUCTURAL override left undischarged **is** a discipline event. **DISCHARGED AT THE DRAIN @`d876b8b74a`**, measured both sides: `06 STALE: source drift, fingerprint 8a433f14.../260 -> b49c62e1.../260` before, `SYSTEM CURRENT (26 managed regions across 6 files, 0 drifted)` after. **The generalisation is the row's and I adopt it: when a grant admits a file whose modification mechanically obliges a second artifact, the grant must either admit that artifact or name the override and its owner ON THE FACE.** My BOUNDS foresaw the comp-system pass and told the worker to report the touch, which is why the discharge happened at all -- but it did not foresee that **the gate fires at the worker's commit, not at the drain**, so the worker had to choose between two paths the face never named.
3. **A self-correction the worker recorded rather than left standing:** its act commit's *message body* quoted sweep figures from the run before it (29,971/92) while its committed captures carry the final run's (29,973/94). The captures are authoritative; the denominators moved because the cell was adding untracked files to the corpus it was sweeping, and **every graded value was invariant across all runs**.

## 4. FIVE PREMISES I PUT ON THESE FACES CAME BACK FALSE

Enumerated in the partial packet's section 3 and unchanged by this order. Summarised here so the L9 grades the whole round from one place: *the loss STOPPED* (false, `STORED_IN` is 0, row `W3-S18`); *the projection has a self-cadence* (falsified, it is Pipe-driven); *one round-7 pin has moved* (false, 0 of 4, row `W2-S76`); *the deploy clock* (does not exist; the owner will see green, row `W4-S7`); and *the workers are on the old comp-rail* (false, caught before a worker existed, row `S115`).

⭐ **NOT ONE WAS CAUGHT BY A GATE, A CONTROL OR A CHECKER. Every one was caught by the seat being graded, running a read nobody asked for.** Round 7 observed this at four rows and called it a fact about where this estate's defects are found. Round 8 reproduces it at five, from five different orders and five different instruments, which moves it from an observation to a measured property of the controls.

**What did work is the LABELS.** Both premises marked `HELD, NOT MEASURED` cost nothing when falsified -- one of them was falsified *because* the face told the worker to falsify rather than confirm it. Both marked `MEASURED` misdirected a worker. `measured / inferred / held / absent` is carrying the entire load, and it is worth noting that it is a discipline rather than a mechanism: nothing enforces it.

## 5. The rows, and the four with a dark owner

The partial packet's section 5 table stands. **This order adds three, all OBSERVATION/ARMED to `2.0.0_SA_COO~A`:** `W1-S46` (the two out-of-grant consumers), `W1-S47` (the re-point would break the fold), `W1-S48` (the undischargeable debt -- **now discharged**, and the row's generalisation stands).

⛔ **UNCHANGED AND STILL OWED: four ARMED rows have a DARK owner** -- `W1-S43`, `W1-S44` (`0.8.0_AE_CloudComp`, NOT REGISTERED) and `W2-S78`, `W4-S7` (`0.7.0_AE_CloudOps` base dark; only `~W` is live). Liveness **read at close, not assumed**. I did not re-seat them and the reason is stated in the partial: acting on any needs a CELL, the decomposition was frozen while H-1 was in flight, and a Tier-2 seat hears an act only as a task order. **They ride the drain-end read.**

**Channel at close: 281 rows, 281 distinct.** 17 filed this round. **4 of the 5 drains conflicted on the append-only channel** (S36's normal path), each resolved as *base + ours-tail + theirs-tail* under a guard that refuses if either side is not a pure append, verified on the written bytes: 0 markers, 0 duplicates, 0 lost, union counts printed (272, 275, 278, 281).

## 6. What the L9 is asked for

1. **Five judgment criteria:** `H1-AC5`, `H2-AC5`, `H3-AC5`, `H4-AC5`, `H5-AC5`. All RECORDED as `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO`; **no verdict is taken anywhere in the instances or in either packet.**
2. **The disposition of the four ARMED rows with dark owners**, and of `W3-S18`/`W3-S19` which the base COO owns.
3. **A reading I am asking for and will not offer:** whether five false premises from one issuer in one round, every one caught downstream and none by a control, is a cut-discipline failure at this seat or a controls failure in the estate. **I have an interest in the second answer.**
4. **One question the retirement raises above this project:** `W1-S47` shows a ruled remedy that would have broken a control landed in the same round, and no criterion on either order could have seen it because the coupling sits between them. Whether that is a gap the spine should close at L5 -- an explicit cross-cell coupling read at the decomposition -- is a judgment above this seat.

## 7. What round 8 hands forward, with the two LIVE HAZARDS first

- ⛔ **`SERVED_FROM=27`, all 27 on the same parent class. The mechanism that took `STORED_IN` to zero is still loaded.** Same collision, same Lambda path, untouched family. Not a prediction.
- ⛔ **Re-parenting does not close it.** `lambda_function.py:271` writes the bare bucket NAME into a table where that string is `S3_BUCKET_POLICY`'s canonical key; the overwrite destroys a node on every S3 write. `CG-s-33`'s committed-not-deployed re-point is **necessary and not sufficient**.
- ⛔ **And the retirement is not merely deferred: AS RULED it is unavailable to any single cell**, because the re-point breaks the fold. A future cut must either change the remedy or move the fold's licence first.
- The node drop still has no edge-side counterpart, and the producer's `0-dangling` check cannot see the gap (`W1-S44`).
- A dated snapshot key reads immutable and is a mutable pointer on an unversioned bucket (`W1-S43`).
- The four-way canonical-shape disagreement, with the ratified canon declaring the edge in the **opposite direction** and its own 2026-07-18 instruction to trace consumers first, unrun for eight weeks until `H5-AC1` ran it.
- Hop 1's committed producer exists on both routes but not in a production HOME.
- The deferred SERVED re-take of `F11-AC3` and `G2-AC2`, still Andrew-gated; **section 2 of the partial is what makes it readable when it comes.**

**Push state: MEASURED at this compile against a FRESH fetch, PER COMMIT rather than as one verdict, because the integrator published mid-round and a single answer would have been wrong in both directions.** `origin/CLOUD` `634255bcc3`. **ON ORIGIN:** `217a87a817`, `2fd5cae09f`, `06ccb217db`, `4ab0da7983`, `1b191aa125`, `b36333e2cb`, `95f9aaa891`. **LOCAL:** `fba1f0b1db` (the H-1 drain merge) and `d876b8b74a` (the comp-system discharge). A negative control was run: a known-local object reads LOCAL on the same instrument. Andrew holds the push and this claim ages the moment the integrator runs again.
