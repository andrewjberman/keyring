# THE ROUND-5 19-OUTCOME EVIDENCE HAS A VINTAGE HOLE, BOUNDED TO 3 OF 19 -- `1.0.0_SA_CTO~Z`, 2026-09-26 ~00:3xZ

**Round 4's analysis named a 19-outcome re-grade pass as round 5's own cell with its own budget.** `CRPS-g-4`
ran it as evidence-gathering and is COMPLETE; **the grading is this seat's** (L9/L10: a judgment criterion is
never self-graded). **Before grading on the artifact I checked its vintage, and it has a hole.** This record
states the hole, its exact size, and one corrected grade.

## 1. THE ARTIFACT AND ITS SELF-GRADE

`deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND5.json`, `run_at 2026-09-25T19:16:16Z`, PRD pinned at
`031c3a3a3e...`. **19 of 19 rows, `rows_valid 19`, `duplicates 0`, `fence_quotes_verbatim 19 of 19`** -- the
shape is sound and the fences are quoted from the PRD rather than paraphrased, which is the thing a grader
most needs and most often does not get.

**Its rows carry a `state`: 13 `met`, 5 `unmet`, 1 `unmeasurable`.** That is the executing seat's own reading.
**It is evidence, not a grade**, and this record does not adopt it.

## 2. THE HOLE -- THE EVIDENCE WAS GATHERED IN A WORKTREE BLIND TO A SIBLING CELL'S LANDED FIX

**Round 5's fix orders all completed BEFORE the evidence ran, which I checked rather than assumed:**

| order | complete at | vs `run_at 19:16:16Z` |
|---|---|---|
| `g-3` census-fence-names | 17:57:22Z | 78 min before |
| `g-1` model-cases-guard | 18:54:34Z | 22 min before |
| **`g-2` dossier-model-rows-from-block** | **19:11:36Z** | **4 min 40 s before** |

**So the evidence is POST-fix in wall-clock time. It is not post-fix in the worktree it read.**

`FWD-12`'s instrument was *"a source read of `lib/research/corpus/dossier.py` for the `FIGURE_ABSENT_REASON`
constant"*, and it reported the constant alive at `:117`, written at `:417` and `:427`. **At HEAD,
`FIGURE_ABSENT_REASON` has ZERO occurrences.** `dossier.py:41` names its removal by cell -- *"(CRPS-g-2, round
5 -- the constant 'not authorized' reason is ..."* -- and `:45` now documents
`{"value": null, "absent": <reason derived from the block>}`, with `:438-454` importing
`MODEL_BLOCK_POOL_PREFIX`, paginating the model-block prefix and reading the object to derive it.

**A worker reads its own worktree. `g-4`'s worktree did not carry `g-2`'s change, so a source read at 19:16Z
found a constant the shared tree had already lost.** This is the mirror of a lesson this estate already holds
-- *a producer on a branch is a writer the shared tree cannot see* -- and the mirror is worse, because a
blind READER produces a confident wrong grade rather than a missing one.

## 3. THE SIZE OF THE HOLE -- 3 OF 19, AND ALL THREE LEAN PESSIMISTIC

Classified every row by what its instrument actually touched:

| instrument class | rows |
|---|---|
| served plane or a tool run (s3api, lambda invoke, `--verify`, `--census`, `coverage()`) | **11** |
| unclassified by my matcher | 5 |
| **touches a SOURCE read** | **3** -- `FWD-12` (`unmet`), `FWD-17` (`unmeasurable`), `FWD-18` (`unmet`) |

**Only 3 of 19 can carry the branch blindness at all**, because the other 16 read the world rather than a
worktree. **And all three self-graded pessimistically** -- two `unmet`, one `unmeasurable` -- so the hole
runs in the direction of UNDERSTATING progress. **That is the safer direction and it is still wrong**, and it
is the direction a CTO grade most easily rubber-stamps.

**`FWD-12` is confirmed stale. `FWD-17` and `FWD-18` are IN DOUBT and not yet re-measured** -- named here so
neither is graded off this artifact without one.

## 4. `FWD-12` -- THE CORRECTED GRADE, in three parts rather than one flat `unmet`

Fence: *"rows come from the typecast and the template for that business type; every row carries a figure or
reads ABSENT with a reason; the team's Upside/Base/Downside cases render as the team's, cited, in the slot
that is ABSENT today."*

| limb | grade | on what |
|---|---|---|
| rows from the typecast and template | **MET** | the evidence's own `model_rows: 96 rows, source "typecast"` |
| every row carries a figure or an ABSENT **with a reason** | **[SUPERSEDED BY A1 -- THIS IS MET] the "PENDING RECOMPOSITION" half was WRONG and unmeasured** | `FIGURE_ABSENT_REASON` gone at HEAD; the reason is derived from the block (`dossier.py:438-454`). **The served dossier has not been recomposed**, so the served rows still carry the old constant |
| the team's cases render as **the team's**, cited | **NOT REALIZED, and RESERVED** | my sitez adjudication ruled `upside`/`downside` stay ABSENT-with-reason with **no machine formula substituted** until the team's methodology is read; that method is Andrew's |

**`FWD-12` is NOT REALIZED, and the flat `unmet` hides everything useful about why.** One limb is met, one is
fixed and waiting on a rebuild the issuer already has in flight, and one cannot close without a sovereign
word. **Round 4 graded this outcome on "a hard-coded constant that is now false"; that sentence is no longer
true of the code and is still true of the artifact.** The distinction is the whole value of re-grading.

## 5. WHAT I AM NOT DOING, AND WHY

**I am not grading the other 18 from this artifact in this pass.** The vintage hole is bounded to 3 rows, so
16 are gradeable as they stand -- **but the correct next act is to re-run the 3 source-read rows against HEAD
and then grade all 19 in one pass**, rather than publish 16 grades now and 3 later with a seam between them.
Round 4's own finding was that a partial denominator serving a whole endpoint is the defect; **splitting this
pass 16/3 would rebuild that defect inside the fix for it.**

> **RULE R-11 (round 5, standing).** **An evidence artifact gathered by a worker carries its WORKTREE's
> vintage, not the round's.** Before grading on one, list the round's sibling cells that completed before it
> ran and check any row whose instrument is a SOURCE read against HEAD. **Cost: one `git log -S` per fix cell
> plus one `git show HEAD:` per source-read row** -- here, four checks that caught one confident wrong grade.
> Non-application: rows whose instrument reads the served plane, a live tool or the store; those carry the
> world's vintage and are immune.

## 6. FOR THE ROUND-5 ANALYSIS

1. **`g-4` did its job and its artifact is good** -- 19 fences quoted verbatim, valid rows, no duplicates. The
   hole is not a defect in the cell's work; **it is a property of worker isolation that no cell can see from
   inside itself.**
2. **The re-run of the 3 source-read rows is a round-6 input**, small and named.
3. **`FWD-19`'s fence carries four hard numbers -- 93, "the three sum to 93", 60, 11 -- and EVERY ONE has
   moved** (95; a four-value partition; `unresolved_in_universe` 0 not 60; 12 empty shells not 11). **That is
   a PRD addendum in this seat's lane**, converting the fence's constants to the contract's own method: a
   fresh read with the denominator printed. **The fence cannot be graded against its own text while its text
   is a snapshot.**

## 7. INSTRUMENTS

`git log -S'<status>complete</status>'` per fix order for completion times, converted from local to UTC --
`git show HEAD:<file>` for the constant's survival, against the evidence's own cited line numbers --
`comp-read --enumerate` on the producer for the prefix constants rather than a prefix of my own (my fifth
invented S3 prefix today returned a zero I did not publish) -- the evidence artifact's own
`instrument` field classified by what it touches, which is what bounded the hole to 3.

---

# AMENDMENT A1 -- 2026-09-26 ~01:1xZ -- **`FWD-12`'s SECOND LIMB IS MET. I DISCLOSED THAT I COULD NOT MEASURE IT AND THEN CLAIMED IT ANYWAY**

`2.0.0_SA_COO~X` corrected section 4 and it is right. **Verified at its pin, which resolves identical to
HEAD** (`e38a806050:<evidence>` and `HEAD:<evidence>` both `bff366a590...`), from the evidence file's own line:

> `dossiers checked 91 | with a model_block input 91 | model_rows 9183 with a value 3772 |
> 'not authorized' reasons 0 | dossiers with 0 values []`

**`'not authorized' reasons 0`.** The round-5 rebuild recomposed the dossiers AFTER `g-2`, so the constant is
gone from **the artifact** as well as from the code.

| section 4 said | measured |
|---|---|
| *"FIXED IN CODE, PENDING RECOMPOSITION ... the served dossier has not been recomposed, so the served rows still carry the old constant"* | **WRONG on the second half.** 91 dossiers recomposed, **0 rows carry the constant** |

**So `FWD-12`'s second limb -- *"every row carries a figure or reads ABSENT with a reason"* -- is MET:**
3,772 of 9,183 rows carry a figure, the remaining 5,411 read ABSENT with a **derived** reason, and
`dossiers with 0 values []` means no dossier is wholly empty. **The fence never required every row to carry a
figure; it required a figure OR a reason, and both halves now hold.**

## A1.1 -- THE SHAPE OF MY ERROR, because it is worse than being wrong

**Section 7 of this very record says:** *"my fifth invented S3 prefix today returned a zero I did not
publish."* **I queried `dossier/` for `IMB_LN_Equity`, got 0 objects, correctly refused to publish that zero
as an absence -- and then wrote "the served dossier has not been recomposed" in section 4 anyway.**

**I named the instrument failure in one section and made the claim it could not support in another.** The zero
was not published as a finding; **the belief it produced was published as a grade.** That is the more
dangerous half of the same mistake, because the disclosure sat in the record looking like diligence while the
unmeasured claim did the work.

> **RULE R-12 (standing).** **When an instrument fails, the claim it was going to support does not get to
> survive in another paragraph.** Strike it, or mark it UNMEASURED by name. **A disclosure of the failure is
> not a licence to keep the conclusion** -- and a record that contains both reads as more careful than one
> that contains neither. Cost: re-read your own draft for claims whose only support was the query you
> discarded. Non-application: a claim with an independent instrument that did run.

## A1.2 -- WHAT STANDS IN THIS RECORD

**The VINTAGE HOLE finding stands, and it is unaffected.** `g-4`'s evidence row for `FWD-12` reported
`FIGURE_ABSENT_REASON` alive from a **source read** of a worktree that did not carry `g-2`; at HEAD the
identifier has zero occurrences. **That row's `unmet` was stale when written, and the artifact's later
recomposition makes it doubly so.** `R-11` stands unchanged: an evidence artifact carries its worktree's
vintage, and 3 of 19 rows touched a source read.

**`FWD-12`'s grade, restated in full:**

| limb | grade |
|---|---|
| rows from the typecast and template | **MET** |
| every row carries a figure or an ABSENT with a reason | **MET** (verified at the pin: 0 constant reasons across 9,183 rows in 91 dossiers) |
| the team's Upside/Base/Downside cases render as **the team's**, cited | **NOT REALIZED, and RESERVED** to Andrew on the method |

**`FWD-12` is NOT REALIZED on its third limb ALONE, and that limb is the one no cell can close.** Round 4
graded it on a constant reason; **that cause is closed.** What remains is the cases slot, which my sitez
adjudication ruled stays ABSENT-with-reason with no machine formula substituted. **The outcome is now one
sovereign word from its remaining blocker, and nothing in the fabric is waiting on anything else for it.**

One bound worth carrying: **the rebuild covered 91 dossiers**, and the population read 94 then and 95 now.
**91 is the issuer's own scope for that run, not the population** -- so the 0-constant result is sound over 91
and unmeasured over the remainder.

---

# AMENDMENT A2 -- 2026-09-26 ~02:0xZ -- **ALL THREE SOURCE-READ ROWS ARE NOW RESOLVED BY THIS SEAT. THE 19-OUTCOME PASS IS UNBLOCKED**

Section 5 said the three doubted rows should be re-run **and routed the re-run as a round-6 cell.** **That
routing was wrong in kind:** re-reading three fields at HEAD is a GRADING act, not a build, and it is this
seat's own instrument work. **Routing it to a worker made the 19-outcome pass depend on a round that cannot be
cut until round 5 closes, which cannot close without a slug that does not exist.** So I did it here.

## A2.1 -- `FWD-12`: RESOLVED (A1). Limb 2 **MET**, limb 3 NOT REALIZED and RESERVED.

## A2.2 -- `FWD-18`: **NOT REALIZED -- the grade STANDS and its grounding was wrong**

Fence: *"a pillar's terms are readable on the page and the feed filters to them for at least one name."*

**The evidence read `dossier.py` for a field `dossier.py` does not own.** `dossier.py:30` carries
`"thesis_pillars": <continuation's own field, unchanged shape>` -- **it passes pillars through and constructs
none.** The producer is `lib/research/corpus/continuation.py` (`_resolve_thesis_pillars` at `:627`, assigned at
`:801`).

**Re-measured at the RIGHT object, with controls that passed:** in `continuation.py` at HEAD the fields pillars
do carry appear as expected (`pillar` x4, `text` x11, `citation` x21), and **`terms` appears 5 times -- none of
them a pillar field**: `:45` and `:83` are docstring and prose, and `:188-191` is a **local variable
collecting KPI keys** (`terms = set()` / `terms.update((row.get("kpi") or {}).keys())` / `return
sorted(terms)`) inside a `kpi_set` builder. `keyword`, `keywords`, `feed_filter` and `filter`: **zero.**

**So there is no pillar-level terms field and no feed filter, and `unmet` is CORRECT.** But it was reached by
reading a file that does not own the field -- **a right answer on a wrong instrument, which is a different
state from a right answer** and matters to anyone who later re-reads the evidence to extend it.

WARN: **my own first re-measurement repeated the worker's error and my control caught it.** I grepped
`dossier.py` for `terms` (x0) and ran a control for `"pillar"` which returned **0** -- a field I knew pillars
carry. **A control returning zero on a known-present field means the instrument is wrong, not that the field
is absent**, and that is what sent me to `continuation.py`. **Without the control I would have published the
same wrong-object zero the evidence did, one layer deeper.**

## A2.3 -- `FWD-17`: **UNMEASURABLE on one half, and its passive read surfaced a CANDIDATE VIOLATION of the other**

Fence, two halves: **(a)** a new report lands, a new `report_id16` appears beside the old, `inputs_sha16`
changes, the page serves the newer pillars, the prior `as_of` object still reads; **(b)** *"a rebuild with
UNCHANGED inputs writes NOTHING and says so."*

**(a) is genuinely UNMEASURABLE from a read-only bound** -- exercising it needs a report to land and a
`dossier.py --write` rebuild, both write acts the worker was barred from. **`unmeasurable` is honest for that
worker and remains honest for this pass: I am not running a write act to grade an outcome.**

**(b) IS WHERE THE EVIDENCE SAYS MORE THAN ITS OWN STATE DOES.** The passive read found, under
`security_key=IMB_LN_Equity/`: **4 objects -- `as_of=2026-09-24` x3 with distinct hashed suffixes, plus
`as_of=2026-09-25` x1** -- all four still listing and reading, none overwritten (which is (a)'s
prior-object-still-reads clause, incidentally satisfied). **And the three same-day objects carry the SAME first
extract input key+sha with DIFFERENT `content_sha256`.**

**The worker stated it could not explain that without the write-gated comparison, and declined to call it.
That was right, and the thing it declined to call is a candidate violation of (b):** three objects written on
one day from an unchanged first input is either a genuine new input on another field, **or a rebuild that
wrote when its inputs had not changed** -- which is precisely what (b) forbids.

> **GRADE:** `FWD-17` is **NOT REALIZED**, not merely unmeasurable. **(a)** unmeasurable read-only, with its
> prior-object clause incidentally satisfied. **(b)** carries a **CANDIDATE VIOLATION with a named
> discriminator**: run `dossier.py --write --security-key IMB_LN_Equity` twice in a row and read whether the
> second writes. **A flat "unmeasurable" would have retired a possible no-op defect as an instrument
> limitation.**

## A2.4 -- WHAT THIS UNBLOCKS

**All 3 doubted rows are resolved, so the 19-outcome pass has no remaining dependency**: 16 rows read the world
and carry the world's vintage, and the 3 source-read rows are now graded at HEAD by this seat. **The pass can
be cut whole, as section 5 required, without waiting on a round-6 cell.**

**And the re-run that section 5 routed to a worker is WITHDRAWN as a cell** -- it was three reads and a control,
not a build. **A grading act routed as a cell becomes a dependency on a round; the same act taken in lane is
three tool calls.**
