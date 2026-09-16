# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 47 (covers ticks 46-47)

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-13T05:15:10Z**
Tick 45's log is `@e2c924a274`, committed `2026-09-13T00:25:30-04:00` (author time, not the filename).
Tick 46 was QUIET and wrote nothing. **Tick 47 ran POSN's L10 and it is the sharpest read of the
night — because what it found is a defect in this seat's own PRD that hid two outcomes for three
rounds.**

---

## 1. THE ROUND-3 SLUG ARRIVED AND THE COVERAGE SUBTRACTION IS **NOT** EMPTY

`REMEDIATION_v3.md` `@c89c0e45a2`. Answer: `ledger/ROUND_ANALYSIS.round3.md` + **PRD v0.5 -> v0.6**,
both `@ae66157381`.

```
15 cut orders · 6 declared · 4 covered · UNCOVERED = { FWD-4, FWD-6 }   <- NOT EMPTY
FWD-1 14 · FWD-2 4 · FWD-3 1 · FWD-4 ZERO · FWD-5 1 · FWD-6 ZERO
```
**NEGATIVE CONTROL: a synthetic outcome id generated AT RUN TIME and verified absent from the corpus
before use — the token deliberately not printed anywhere**, because `Z-S67` measured three hours ago
that a literal control token published in a citable document dies at the first citation. **The lesson
banked this morning was applied the same morning, in the first document that could have repeated it.**

⭐ **`FWD-6` IS THE ASTTAX FRONTEND OUTCOME ANDREW NAMED** — *"the places that show asset classes
agree with each other"*. It has **never had a cell cut for it**. Not deprioritised, not blocked:
never issued, three rounds running. `FWD-4` (one colour per class, everywhere) likewise.

## 2. ⛔ WHY IT WAS INVISIBLE, AND THE LINE IS MINE

PRD v0.5's surface table closes: **"6 of 6 outcomes carried by exactly one row, 0 uncovered."**
**True — and about ASSIGNMENT, not ISSUANCE.** Every outcome has an owning surface row; two have no
cell. **Rule 24's wrong-domain failure in its most dangerous form: the subtraction returned EMPTY, so
it was acted on rather than argued with, and it printed a denominator so it read as MEASURED.**
`2.0.0_SA_COO~Z` and `3.0.0_SA_CVO~Z` both had that same green available. **A surface row owning an
outcome is not a cell serving it.**

## 3. THE ADDENDUM — FOUR ITEMS, ALL DEFECTS IN TEXT THIS SEAT AUTHORED AT L4

1. the coverage gap named by id (Rule 27's addendum trigger, verbatim);
2. the MECE check **qualified** so "0 uncovered" can never again be read as "0 unserved";
3. **`Z-W10-S1`** — s.4's live mechanism corrected: the weight is **not** zeroed in the allocation
   dict, which serves 2.5; the loss sits at the five-class served view and at delta/spread rows that
   carried **no row at all**. Its consumer is `AT3-s-5`, **the bar that gates the retag**, and the
   correction says so *at the point of use*;
4. **`Z-C-S55`** — the surface list discloses the third, non-owned reader (ruled at `Z-S42`), with
   its 189-rows / four-books / **zero-candidate** state **and the condition that ends it**.

⭐ **ITEM 4 AND `FWD-6` ARE ONE DEFECT SEEN FROM TWO SIDES:** S3 is defined as *"the two surfaces"*,
the world has at least three readers, and the outcome that spans them is the one nobody cut a cell
for. **A row scoped to two cannot generate a cell that checks three.**

## 4. ⚠ A CLAIM CORRECTED BEFORE COMMIT — AND ITS SOURCE IS ALSO MY OWN PRD

The analysis first said the bump *"de-currents **both** halves"*, quoting the PRD's own version line:
*"Each bump re-opens the two L4-R sign-offs."* **The gate said otherwise and the gate is right** —
`ratified-text SIGNED current`, `brief STALE`. `RATIFIED_SECTIONS` is `("ENDPOINT","CONTRACTS")`
matched on a heading's **first word**, so **exactly one section here is ratified-text** and s.4
(*"4. Constraints that BIND the decomposition"*) is brief-half. These edits touched no ENDPOINT byte.

**So the cost is half what I claimed: one re-sign by `4.0.0_SA_CRO~Z`; `3.0.0_SA_CVO~Z`'s signature
is untouched and stays valid.** The PRD's false line is corrected in the same commit.
⛔ **AND IT IS THE SAME DEFECT AS ITEM 2 — a line of mine stating a rule STRONGER than the mechanism
behaves, which I then quoted as authority against myself.** That is the shape CLAUDE.md Rule 27
already records against LIMB 6: *"the law read stronger than the tool behaves and three seats
inherited the belief from it in one evening."* **Twice in one document, found only because a gate
disagreed with a sentence I trusted.**

## 5. `Z-S47` `@95ed81b570` -- BOTH POSN ACTS THIS SEAT CARRIED ARE NOW COMPLETE

`Z-W10-S1`'s disarm was *"amending that text is the only disarm"* — done at v0.6, verified at HEAD
rather than from the worktree. `Z-C-S55` was ruled at `Z-S42` and its line landed in the same
addendum. **They waited two ticks for the right carrier and not out of neglect:** Rule 27 freezes the
spec mid-round, the L10 addendum is the carrier the law provides, and the hazard was mitigated
meanwhile by routing the corrected reading to the round owner — **but a message is not a carrier**,
which is exactly why the PRD edit still had to happen.

## 6. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 2 RESERVED · NO PITCH   (all-reserved tell does not fire)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  EXECUTING  REACHABLE  1 OPEN of 47 -- rh-1, the served route
  POSN_ASTTAX  EXECUTING  REACHABLE  4 OPEN of 15 carried unrun; L10 ANSWERED, round 4 owed
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
**ROUND 4 MUST COVER `FWD-4` AND `FWD-6`.** The recut is `2.0.0_SA_COO~Z`'s and nothing here cuts it;
the brief-half re-sign sits in front of it and `4.0.0_SA_CRO~Z` has been told.
Register agrees with the gate: D4 6=6, D5 1=1.
**Push state:** `origin/SITEZ fbd26c5878`, local ahead 1 at the read. `HEAD:portal e85f6eb84f`,
unmoved. No TO cut, no dispatch, no apply, no retag, no deploy, no promote.

## Compiler Tools

A coverage subtraction over the 15 cut orders with a **run-time-generated, absence-verified,
unprinted** control · `prd_signoff_lib.half_of_section` driven over every heading to map sections to
halves, which is what caught the both-halves error · `prd-signoff.py status` read before AND after the
bump · a `RETAG`-count positive control before quoting s.4 · `git show HEAD:` to verify the PRD
correction landed, never the worktree · an edit-scoped non-ASCII guard comparing the glyph set before
and after, after a whole-file guard falsely refused on pre-existing characters · `git status
--porcelain` before the channel append · `date -u` at the write · post-commit HEAD oracle with a
`Z-S99` negative control · `safe-commit.sh -F` with non-shell-written message files · short send
subjects.
