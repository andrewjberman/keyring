# POSN_ASTTAX — ROUND 3 ANALYSIS (L10)

**From** `1.0.0_SA_CTO~Z`, L2/L4 owner, answering `3.0.0_SA_CVO~Z`'s round-3 slug
`surprise-channel/remediations/REMEDIATION_v3.md` `@c89c0e45a2`.
**2026-09-13T05:0xZ** · `HEAD:portal e85f6eb84f`, unmoved. No retag, no deploy, no promote.

> **VERDICT: PRD ADDENDUM REQUIRED — v0.5 -> v0.6.** Two of six declared outcomes have been served by
> **zero cut orders across three rounds**, which is Rule 27's addendum trigger verbatim. Three
> further corrections ride the same bump, and **all four are defects in text this seat authored.**

---

## 1. COVERAGE — the subtraction, and it is NOT empty

```
DENOMINATOR       15 cut task orders under POSN_ASTTAX
DECLARED          6  (FWD-1..FWD-6, PRD v0.5 header endpoint_outcomes)
COVERED           4
UNCOVERED = declared MINUS covered = { FWD-4, FWD-6 }     <- NOT EMPTY

  FWD-1  14 orders   FWD-2  4   FWD-3  1   FWD-4  0   FWD-5  1   FWD-6  0
```
**NEGATIVE CONTROL:** a synthetic outcome id generated at run time and verified absent from the
corpus *before* use; it returned 0 orders, so the reader discriminates. **The token is deliberately
not printed here** — an analysis exists to be quoted into orders, and a literal control token
published in one dies at the first citation (`AMGT_RESAPP-Z-S67` `@8af6dbbe88`, measured on this
seat's own round-8 analysis three hours ago).

- **`FWD-4`** — *"Each class has one color, the same everywhere."*
- **`FWD-6`** — *"The places that show asset classes agree with each other."*

⭐ **`FWD-6` IS THE ASTTAX FRONTEND OUTCOME ANDREW NAMED.** His 03:21:46Z direction: *"I expect
frontend for both RESAPP and ASTTAX to be done too."* ASTTAX's frontend outcome is FWD-6, mapped to
surface **S3**, the views that render — and **it has never had a cell cut for it.** Not deprioritised,
not blocked: never issued, three rounds running.

## 2. ⛔ THE PRD'S OWN MECE CHECK SAYS "0 UNCOVERED" AND IT IS ABOUT A DIFFERENT POPULATION

PRD v0.5's surface table closes with, verbatim: **"6 of 6 outcomes carried by exactly one row, 0
uncovered."**

**That sentence is TRUE and it is not about issuance.** Its domain is *outcomes ASSIGNED to a surface
row* — S1 carries FWD-1/2/5, S2 carries FWD-3/4, S3 carries FWD-6. Every outcome does have an owner.
**The claim a reader takes from it is that every outcome is SERVED, and that is a different
population**: FWD-4 and FWD-6 are assigned and unserved.

⛔ **This is Rule 24's wrong-domain failure in its most dangerous form — the subtraction returned
EMPTY, so it was acted on rather than argued with, and it printed a denominator so it read as
MEASURED.** `2.0.0_SA_COO~Z` and `3.0.0_SA_CVO~Z` both had the same green available to them.
**The line is this seat's, written at L4, and it is the reason two outcomes went three rounds
unnoticed.** A surface row owning an outcome is not a cell serving it, and the PRD must say so.

## 3. THE OTHER TWO CORRECTIONS, BOTH SCHEDULED TO THIS MOMENT AND BOTH NOW DUE

**(a) `Z-W10-S1` — s.4's live-mechanism sentence is half false at HEAD.** The PRD reads *"It renders
`Commodities`/`Structured` as the literal string `'Unknown'` **and silently zeroes the weight**."*
The label half is correct. **The weight half is not:** `AT2-s-1` added an `else` to all three
`asset_class` chains, so at the order's own base commit a Commodities holding served allocation
**2.5, not 0.000**. The real loss sits at the five-class served view and at the delta and spread rows,
which carried **no row at all** rather than a zero.
⚠ **Its consumer is why this could not keep waiting:** the next cell to read that sentence is
`AT3-s-5`, **the bar that GATES the retag.** A bar built on *"confirm the weight zeroes in the
allocation dict"* returns the same answer before and after a retag. The corrected reading already
went to the round owner (22254) so the bar is safe whenever it is cut; **the addendum is what stops
the wrong sentence being read again.**

**(b) `Z-C-S55` — the surface list is incomplete, ruled at `Z-S42` `@9d7b09987f`.** A third producer
outside the two-sibling set copies gold holding class values. Out of POSN's write scope, in its
disclosure scope, carrying its measured state (189 rows, four books, **zero candidate members**) and
**the condition that ends that state.** The slug has already adopted this — *"The additional ETF
publisher receives disclosure only, with its pinned zero-candidate state and expiry"* — so the PRD is
now the last place the fabric's own position is not written down.

⭐ **AND (b) AND FWD-6 ARE ONE DEFECT SEEN FROM TWO SIDES.** S3 is defined as *"The two surfaces"*;
the world has at least three readers; and the outcome that spans them — *"the places that show asset
classes agree with each other"* — is the one nobody cut a cell for. **A surface row scoped to two
cannot generate a cell that checks three.**

## 4. THE SLUG'S OWN SHAPE, GRADED

Four orders (`S2-1`, `S3-1`, `T6-1`, `T7-1`) are carried **unrun** and their status is deliberately
not made terminal. ⚠ **A future reader will see a round-3 slug cut over four non-terminal orders and
should not read it as the L10 rule being broken:** it is Andrew-direct LD-0562, 04:08:22Z, *"all recs
approved"*, card 1 — the carry-forward is his ruling and it is what let round 3 close at all. Twenty-
seven remediation records, 9 completed and 18 open. The slug states plainly that no FWD is claimed
REALIZED and that the deployment gap and the missing frontend/sibling implementation are distinct
from measurement. **Both readings agree with this seat's.**

## 5. STATE — 0 of 6 REALIZED

Every bar re-read from the PRD this tick. The distance is not uniform and the difference matters:
- **FWD-4, FWD-6** — no cell has ever been cut. Distance: an order, then the work, then the bar.
- **FWD-1, FWD-2, FWD-5** — cells exist and ran; the retag that would exercise them is **NO-GO**, and
  the generator carrying the repairs is **undeployed** (deploy approved 04:08Z *conditional on the
  two-seat never-widen sign-off*, which has not landed and whose writer count this seat has measured
  at **at least three**, not two — `Z-S43` `@a12a092051`).
- **FWD-3** — one order; order and colour are defined but not shown to agree across surfaces, which
  is FWD-6's job and FWD-6 has no cell.

## 6. WHAT THE ADDENDUM DOES, AND WHAT IT COSTS

**PRD v0.5 -> v0.6**, four changes, all in text this seat wrote: the coverage gap named with FWD-4 and
FWD-6 called out by id; the MECE check qualified so "0 uncovered" can never again be read as "0
unserved"; s.4's weight mechanism corrected with what it used to say; and the third surface disclosed
with its measured zero and expiry.

⛔ **THE COST IS REAL AND IS ON THE CRITICAL PATH, SO IT IS STATED RATHER THAN DISCOVERED.**
`to-pipeline-gate.py` LIMB 6 refuses a **newly-added** task order against a half that is not SIGNED at
current bytes, and **round 4 must add cells for FWD-4 and FWD-6 — so a re-sign sits directly in front
of the work Andrew asked for.**

> ⚠ **CORRECTED BEFORE COMMIT, AND THE SOURCE OF THE ERROR IS THIS SEAT'S OWN PRD.** This paragraph
> first said the bump *"de-currents **both** halves"*, quoting the PRD's version line — *"Each bump
> re-opens the two L4-R sign-offs."* **THE GATE SAYS OTHERWISE AND THE GATE IS RIGHT.** Measured
> after the edit: `ratified-text SIGNED current`, `brief STALE`. A bump re-opens only the half whose
> SECTION BYTES moved; `RATIFIED_SECTIONS` is `("ENDPOINT", "CONTRACTS")` matched on a heading's
> FIRST WORD, so in this document **exactly one section — `ENDPOINT` — is ratified-text**, and s.4
> ("4. Constraints that BIND the decomposition") is brief-half. These edits touched no ENDPOINT byte.
> ⭐ **So the cost is HALF what this analysis first claimed: one re-sign by `4.0.0_SA_CRO~Z`, and
> `3.0.0_SA_CVO~Z`'s signature is untouched and stays valid.** The PRD's false line is corrected in
> the same commit — **and it is the same defect as item 2 above: a line of mine stating a rule
> stronger than the mechanism behaves, which I then quoted as authority.**
⭐ **This is nonetheless the cheapest moment it will ever be:** `3.0.0_SA_CVO~Z` cut this slug minutes
ago and `4.0.0_SA_CRO~Z` is live, both holding the project in context. Deferring costs the same two
reads later **plus** a fourth round cut against a spec that three seats now know is wrong.

---

## 7. CLARIFICATION 05:2xZ -- WHAT "ROUND 4 MUST COVER FWD-4 AND FWD-6" MEANS, asked and answered

`2.0.0_SA_COO~Z` asked before cutting (22280) whether a **measure-and-price** reading satisfies s.6 --
cells that read portal source, enumerate rendering surfaces and price the change, **writing no byte
under `portal/`** -- and said it would cut wider if that reads narrower than intended. **It reads
narrower, and asking before cutting was the right instinct.**

⛔ **THE DISCRIMINATOR IS NOT THIS SEAT'S PREFERENCE. IT IS A LIVE PRECEDENT IN THE SIBLING PROJECT,
CUT UNDER THE SAME FREEZE, ON THE SAME NIGHT, CITING THIS SEAT'S OWN ROUND-8 ANALYSIS.**
`AMGT_RESAPP.TO-AMGT-rh-1` grants **write paths inside the submodule** --
`portal/src/pages/SecurityAnalysis/` and `portal/src/api/endpoints/amgt-lead-panel.ts` -- while its
own text reads *"NO PROMOTE. NO GITLINK MOVE. NO REMOTE PUSH. NO DEV OR PROD MERGE... A local dev
server is not a publish. **Commit yes, promote no.**"* Its `AC5` mechanically verifies the
superproject gitlink still reads `e85f6eb84f` and calls a moved gitlink a hard stop.

**So the boundary the fabric is already operating is:**
```
write portal source          YES     commit inside the submodule   YES
MOVE THE SUPERPROJECT GITLINK NO     promote / push / DEV / PROD    NO
```
**Those last two are exactly the acts the relay names** (22187: *"Do not read any part of this
direction as a licence to promote, push DEV/PROD, or move the gitlink"*). **Writing source is not
among them, and never was.**

⭐ **AND HIS OWN FRAMING SETTLES IT:** *"the work should be COMPLETE AND WAITING AT THE PROMOTE LINE,
so that the day he gives the word, the only thing between the build and a person is the promote
itself."* **A frontend that has been measured and priced leaves a great deal more than a promote
between the build and a person.** `FWD-4` and `FWD-6` are EXERCISED bars; measurement cannot approach
them, and a round that covered them with pricing cells would be covering without serving -- **the
exact failure s.2 of this analysis exists to name.**

⚠ **THIS IS A READING OF WHAT THE FREEZE COVERS, NOT A LIFT OF IT, AND NOTHING HERE ANSWERS THE CARD
`2.0.0_SA_COO~Z` put to Andrew at 05:14Z.** That card asks whether *"frontend ... done"* opens the
promote; it does not, it stands, and it is his. This clarification only says that the freeze was never
on writes -- evidenced by a committed sibling order, not inferred from his sentence.

### 7a. AMENDED 05:3xZ -- "COMMIT INSIDE THE SUBMODULE: YES" WAS INCOMPLETE, AND THE GAP IS SILENT

`2.0.0_SA_COO~ZZZ` answered the sequencing point (22289, row `AMGT_RESAPP-Z-S70` @`cede63a639`) and
supplied a coordinate not guessable from outside that project. **Reproduced here independently, in
the main tree's `portal` clone, with this seat's own controls:**

```
a845a8be75  (AMGT round 8's portal repairs)
  git branch -a --contains ................ 0        <- reads exactly like work never done
  git for-each-ref --contains ............. refs/drains/rg-2-portal   (one ref, no branch)
  is-ancestor of refs/remotes/origin/DEV .. NO
POSITIVE CONTROL, same run: for-each-ref --contains on local HEAD 30ca034bba -> 10 refs;
  is-ancestor origin/DEV origin/DEV -> YES.   The zeros are REAL zeros, not a broken predicate.
e85f6eb84f (the frozen gitlink) on 5 refs · rev-list e85f6eb84f..a845a8be75 = 14 commits
```

⛔ **SO s.7's `commit inside the submodule -- YES` IS INCOMPLETE AS THIS SEAT WROTE IT.** It said that
a commit is permitted; it did not say **where that commit must be reachable from**, and a sibling
project's fourteen commits of portal repair are currently on **no branch at all**. A lane that later
merges portal work *from branches* and pushes DEV produces a DEV **missing those repairs -- with no
conflict, no refusal, and no gitlink disagreement to notice**, because the gitlink never pointed at
them either.

**THE COMPANION INSTRUCTION, which s.7 should have carried and now does:**
1. **A portal commit must be reachable from a ref a peer's merge will actually traverse** -- a branch,
   or a drain ref the merging lane is told about BY NAME. A `refs/drains/*` ref keeps objects alive
   and `gc` honours it; **it does not make the work discoverable.**
2. ⛔ **`git branch --contains` RETURNING 0 IS NOT EVIDENCE THE WORK WAS NEVER DONE** -- on this
   submodule right now it is the *expected* reading for real, committed, fourteen-commit work. Use
   `git for-each-ref --contains` beside it, always, and print both.
3. **The gitlink moves ONCE, at promote, after both lanes' portal commits are merged inside the
   submodule** -- never once per project. `2.0.0_SA_COO~ZZZ`'s asymmetry is the reason and it is
   correct: if only ONE side moves it the superproject **fast-forwards that field with no conflict
   and replaces the other lane's pointer silently**; if BOTH move it, git raises a submodule conflict
   and somebody looks. **The dangerous branch is the quiet one.**

⭐ **AND THE SEQUENCING QUESTION ITSELF DISSOLVES:** while neither lane moves the gitlink there is no
contention on the shared value at all, because disjoint paths inside the submodule do not write it.
**The risk was never concurrent writing; it is a later merge that cannot see one lane's work.**

⛔ **ONE NEW COORDINATION POINT, RAISED BECAUSE IT IS CREATED BY THIS ANSWER:** with round 9 live in
`portal/src/pages/SecurityAnalysis/` and round 4 heading for the Positioning and Philosophy/CMA
surfaces, **two projects will be writing inside ONE submodule with ONE HEAD.** The `<paths>` are
disjoint; the submodule HEAD is not. That is the two COO lanes' to sequence, and it is named here
rather than discovered at a conflicted drain.

## 7b. AMENDMENT 05:4xZ -- s.7a NAMES A PROPERTY AND NEVER NAMES ITS CARRIER, AND THAT IS THIS SEAT'S OMISSION

s.7a requires that a portal commit be **reachable from a ref a peer's merge will TRAVERSE.** It does
not say ANYWHERE RECORDS WHICH REFS THOSE ARE. The omission is invisible while one lane writes and
becomes load-bearing the moment two do, which is now: Andrew answered the 05:14Z card at 05:31Z --
VERBATIM *"Yes the frontend being done is defined as built and committed behind the freeze"* -- so
BOTH projects have a live reason to write inside one submodule.

> **A PER-LANE REF SPLIT IS PERFECTLY SAFE TODAY AND LOSES WORK AT PROMOTE.** The promote is performed
> LATER, by a DIFFERENT actor, who has no way to discover a ref nobody wrote down. **The failure lands
> on the step furthest in time from the decision that caused it**, and by then the lane that knew is
> gone. There is no conflict to catch it: merging a gitlink never moves what it points at.

**SO, BINDING ON THIS SEAT FIRST: THE SET OF PORTAL REFS CARRYING WORK NOT YET IN THE GITLINK IS
RECORDED ON A DURABLE CARRIER THE PROMOTE WILL READ** -- each project's `ledger/`, one line per ref,
written WHEN THE FIRST PORTAL COMMIT LANDS rather than at the end. A ref agreed in a broker message
and nowhere else is the class this fabric spent 2026-09-13 retiring: **a ruling that exists only in
mail.**

| choice | contention | the risk it moves |
|---|---|---|
| ONE SHARED REF | two lanes on one ref is shared mutable state; non-fast-forward and force-update, and this estate has measured an append-only shared file silently reverting a peer's write with no error | contention is live NOW, and is at least LOUD |
| PER-LANE REFS | none | the ENTIRE risk moves to the promote DISCOVERING both, and that risk is SILENT |

**Either is defensible; NEITHER is safe without the ref set being written down.** Which ref is the two
COO lanes' choice and this analysis does not make it -- `refs/drains/rg-2-portal` is the incumbent and
incumbency is a real argument.

WARN: **AND THE INSTRUMENT LIES IN THE REASSURING DIRECTION.** `git branch --contains` returning **0**
is the EXPECTED reading for real committed work on this submodule, not evidence of a problem. Print
`git for-each-ref --contains` beside it, or a 0 is read as *fine* or *broken* according to what the
reader already believed.

NOTE: s.7b adds no permission and lifts nothing. The freeze stands: **no promote, no DEV/PROD push, no
gitlink move.** It constrains only how a permitted source write is RECORDED.
## 7c. PRECONDITION 05:4xZ -- THE SHARED SUBMODULE CHECKOUT IS 14 COMMITS BEHIND THE POINTER, AND s.7a's ONE PERMITTED MOVE IS THE ACT THAT WOULD REWIND IT

Measured by `0.0.0_AB_MSTR~Z` with a firing negative control, the direction unambiguous in both
directions rather than asserted from one:

```
gitlink recorded by the superproject ... e85f6eb84f
shared submodule ACTUAL checkout ....... 30ca034bba, branch DEV, dated 2026-09-02
is-ancestor 30ca034bba -> e85f6eb84f ... TRUE      reverse ... FALSE   <- control fires
missing from the checkout .............. 14 commits, the IRPT_FNTEND frontend, ~140 files
corroboration, DIFFERENT instrument .... ls-tree -r FILE COUNT: 1201 at the pin, 1079 at the
                                         submodule HEAD -- 122 fewer (2.0.0_SA_COO~Z, reached
                                         while censusing readers, not while looking for this)
```

**RULING: NO PORTAL-SOURCE CELL IS CUT AGAINST THE SHARED CHECKOUT UNTIL IT IS ALIGNED TO THE
RECORDED POINTER.** This binds the CUT, not a conversation, so it does not depend on anyone
remembering a thread.

⛔ **A CELL WRITTEN AGAINST THAT TREE IS WRITTEN AGAINST A SEPTEMBER 2 PORTAL.** Components, routes
and a rendering package that ARE in the recorded pointer are ABSENT from the tree a worker opens.
Work may duplicate them, conflict with them, or silently assume their absence -- and **a cell whose
premise is a stale tree can grade REALIZED against a surface that is not the served one**, which is
the failure s.7 exists to prevent from the other direction.

⭐ **AND IT IS THE MIRROR OF s.7a's OWN HAZARD, WHICH IS WHY IT BELONGS HERE AND NOT IN A MESSAGE.**
s.7a warns that one lane's portal commits can go MISSING at a merge with no conflict. This is the
same quiet mechanism pointed the other way: **a gitlink move from this checkout would REWIND fourteen
commits of another fabric's SHIPPED frontend**, and `git diff --submodule=log` prints that word
itself. **The act s.7a permits exactly once -- the gitlink move at promote -- is the act that would
do it. s.7a's "moves ONCE at promote" is safe only if the thing it moves TO is not behind.**

**TWO OPERATIONAL POINTS THAT TRAVEL INTO THE CELL TEXT, because a worker never reads this ledger:**
1. ⚠ **WORKER CLONES ARE SEPARATE.** Each `wk-*/portal` carries its own checkout and aligning the
   shared tree aligns nothing else. **A task order granting portal paths states that the worker
   verifies its OWN clone against the recorded pointer before writing** -- a `<paths>`-adjacent
   precondition, not a courtesy.
2. ⚠ **`git status` PRINTS THIS AS A BARE `M portal` AND SAYS NOTHING ABOUT DIRECTION**, which is why
   it sat unremarked while it was harmless. **Any check prints the is-ancestor test BOTH WAYS**; a
   one-direction read cannot distinguish behind from ahead.

NOTE: aligning the working copy is **not a fenced portal act** -- no promote, no push, no DEV/PROD
merge, and **it does not move the gitlink**; it moves the WORKING COPY to the commit the superproject
already records. It is an INTEGRATOR act. Nothing was at risk when found: nothing staged, gitlink
`e85f6eb84f` unmoved on every tick including after the cross-fabric merge, submodule worktree clean.
**A do-it-in-the-right-order finding, caught in the one window where the order was still free.**
---

**PRD ACTION: ADDENDUM, v0.5 -> v0.6, landed in the same commit as this analysis.**
**Round 4 must cover FWD-4 and FWD-6.** The recut is `2.0.0_SA_COO~Z`'s and this analysis does not
cut it. No TO cut, no dispatch, no apply, no retag, no deploy, no promote.
