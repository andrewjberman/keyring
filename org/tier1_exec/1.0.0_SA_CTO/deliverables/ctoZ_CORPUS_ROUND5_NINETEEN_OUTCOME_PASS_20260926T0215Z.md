# AMGT_CORPUS -- the 19-outcome endpoint coverage pass, `1.0.0_SA_CTO~Z`, 2026-09-26 ~02:1xZ

**What this is and is NOT.** This is the CTO's own L2 coverage read of the round-5 endpoint against
`FWD_EVIDENCE_ROUND5.json`. **It is NOT the L10 ROUND ANALYSIS**, which answers a CVO slug that does not
exist -- CORPUS's newest adjudication is `ADJUDICATION_v7`, round FOUR's. The precedent is the RESAPP
20-of-20 pass (`ctoZ_ENDPOINT_COVERAGE_AUDIT_AMGT_RESAPP_20260925T0355Z.md`): the seat that owns the
endpoint may read coverage against it at any time; grading the round still waits on the slug.

**Inputs.** `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/FWD_EVIDENCE_ROUND5.json`,
`run_at 2026-09-25T19:16:16Z`, PRD pinned `031c3a3a3e`. 19 rows, `rows_valid 19`, duplicates 0,
`fence_quotes_verbatim 19 of 19`. Its states are the executing seat's reading; L9/L10 says a judgment
criterion is never self-graded, so this pass adopts none of them and re-derives all 19.

**Predecessor:** `ctoZ_CORPUS_ROUND5_EVIDENCE_VINTAGE_20260926T0030Z.md` @`3c70a79176` (+A1 `3bb9d60b53`,
+A2 `4bd5738990`), which bounded the worktree-vintage hole to 3 of 19 and resolved all three in lane.
Section 5 of that record required the pass be cut WHOLE rather than split 16/3. This is that whole pass.

---

## 1. THE RESULT

**10 REALIZED, 9 NOT REALIZED, 0 unmeasurable.** Against the artifact's self-grade of 13 met / 5 unmet /
1 unmeasurable: **3 rows demoted from met, 1 row promoted out of unmeasurable to a decided NOT REALIZED,
5 unmet confirmed, 10 met confirmed.**

| grade | outcomes |
|---|---|
| **REALIZED (10)** | FWD-1, FWD-2, FWD-3, FWD-4, FWD-5, FWD-6, FWD-7, FWD-8, FWD-13, FWD-16 |
| **NOT REALIZED (9)** | FWD-9, FWD-10, FWD-11, FWD-12, FWD-14, FWD-15, FWD-17, FWD-18, FWD-19 |

---

## 2. THE HEADLINE -- THE ARTIFACT ERRED IN BOTH DIRECTIONS, AND DISCLOSED BOTH IN THE SAME FIELD

The predecessor record found 3 rows self-graded PESSIMISTICALLY because a worker's worktree was blind to a
sibling cell's landed fix -- and noted that the hole therefore **understated** progress, "the safer
direction, still wrong". **That framing was half the picture.** This pass found the mirror: **3 rows
self-graded OPTIMISTICALLY because the instrument could not reach the fence's render clause.**

| direction | rows | mechanism | effect |
|---|---|---|---|
| PESSIMISTIC | FWD-12, FWD-17, FWD-18 | worker worktree blind to g-2's landed fix (source reads) | understated |
| OPTIMISTIC | FWD-10, FWD-11, FWD-15 | s3api data read standing in for a fence that says *renders* | overstated |

**6 of 19 rows carry an instrument-boundary error, and the artifact's own `notes` field states the boundary
in every one of the six.** The pessimistic three named their source read; the optimistic three wrote, in
their own words, *"a separate project's surface this worker did not exercise"*, *"a page-layout claim on
AMGT_RESAPP's render, not exercised by this read"*, and *"whether the header posture line and Posture tab
are byte-unchanged by their presence is AMGT_RESAPP's render, not exercised by this read."*

**Each of those three then carries `state: met`.** That is R-12's exact shape -- the instrument failure
disclosed in one field while the conclusion it was going to support survives in another -- and R-12 was
banked two hours ago against MY OWN record. **It generalises off its author on first reuse.**

> **R-12 restated, wider:** a disclosed instrument boundary and a `state` field that ignores it are one
> defect, not a disclosure plus a grade. **The `state` field is the only thing a consumer reads.**
> A caveat in a sibling field is invisible to every fold, census and rollup downstream.

---

## 3. THE STRUCTURAL FINDING -- 3 OF 19 CORPUS OUTCOMES ARE FENCED ON A DIFFERENT PROJECT'S RENDER

FWD-10, FWD-11 and FWD-15 are fenced on typography, placement and interaction:

- FWD-10: *"renders the pack's pillars as **bold lead plus paragraph, each openable** to the report and the
  passage it came from, and each **marked as the team's**"*
- FWD-11: *"the passage renders labelled as the team's, **BESIDE the filing roster, with the roster
  unchanged**"*
- FWD-15: *"both render cited on **the header posture line and the Posture tab**, and the machine verdict is
  **byte-unchanged** by their presence"*

**None of the three can be closed from inside AMGT_CORPUS.** The pillars, the management passage and the
posture fields are all present, cited and correct in the served substrate -- CORPUS built its half. The
bold lead, the roster adjacency, the Posture tab and the byte-unchanged verdict are AMGT_RESAPP's page.

**This is the CORPUS/RESAPP seam, and the endpoint does not acknowledge it.** Three outcomes are written as
if one project owned both planes. It is also, precisely, the goal's first clause -- the *"visually polished
Security Analysis application"* -- so the seam is not incidental to the goal; it is the goal's own surface.

**Denominator, subtracted not listed.** 6 of 19 fences contain the word *render*. Of those 6: 3 carry an
undischarged UI clause (10, 11, 15); FWD-12 is NOT REALIZED on other grounds; **FWD-13 and FWD-16 use
"renders" of the DATA plane** -- FWD-13's negative control *"renders ABSENT"*, FWD-16's PDF pack *"renders
pillars ... from the PDF"* with the docx path as control -- both fully exercised by the read. My first
matcher called all 5 met-rows disclosures; printing the matched substring per row showed **2 of 5 were
matcher artifacts, 40%**. A caveat is a promise to measure, so it was measured.

---

## 4. FWD-9 -- THE CENSUS IS THE DEFECT, NOT THE CODE

Self-graded unmet on `code-census rc 1`: `files_scanned 37, write_like_calls 43, library_write_calls 4
(induction_run.py:462,464,688,690 ... reaches_library True, origins ['unknown'])`.

**I read all four sites.** `:462`/`:464` and `:688`/`:690` are `os.makedirs(deliverables_dir)` and
`open(os.path.join(deliverables_dir, ...), "w")`. Both sites resolve `deliverables_dir = deliverables_dir
or DELIVERABLES_DIR`, and `induction_run.py:117` defines

```
DELIVERABLES_DIR = os.path.join(
    "org", "missions", "D5", "AMGT", "AMGT_CORPUS", "deliverables", "0.9.0_WK_AMGT_CORPUS~2"
)
```

a repo-relative literal. The library root comes from `library.library_root()`, the synced drive. **The two
are disjoint by construction, so at HEAD with default arguments no flagged call reaches the library root.**

**The census is not lying and it is not right.** Both sites accept `deliverables_dir` as a PARAMETER, so
the AST genuinely cannot resolve the path -- which is what `origins ['unknown']` says. The defect is that
**an UNRESOLVED origin is folded into `reaches_library True`**, so a third state is reported as the unsafe
one. The instrument's own positive control works (`positive_control flagged 1`, two temp-dir plants outside
the repo), so this is not a broken census; it is a census with two values where it needs three.

**FWD-9 is NOT REALIZED, on its own terms:** the fence demands *"a census ... prints zero write, move,
delete or open-for-write calls against any path under the library root"*, and this census prints 4. But the
remedy is a census state, not a code change -- **R-10's shape: a field recording a state also records its
refusal.** Naming the cause matters because "the ingestion writes to the library" and "the AST cannot
resolve a keyword argument" have nothing in common except a number.

---

## 5. FWD-19 -- AND THE CORRECTION I ALMOST PUBLISHED ABOUT MY OWN ADDENDUM

**What I was about to write:** that my FWD-19 addendum (`ff7999d770`, committed `2026-09-26T01:33:19Z`,
**6h17m after the 19:16:16Z run**) had aged the artifact's fence quote out from under it -- a second
vintage hole whose author was the grader, and a new rule about amendments invalidating verbatim quotes.

**The measurement says no.** `git diff --shortstat 031c3a3a3e ff7999d770` on the PRD reads **`1 file
changed, 25 insertions(+)`** -- **zero deletions.** The addendum was APPENDED beside the fence; the
original bytes are unchanged. **FWD-19's `fence_quote` is still verbatim at HEAD, and so are all 19.**
One `git log` on the PRD since the run returned exactly one commit, whose changed lines name only FWD-19,
so the bound is 1 of 19 and the content of that 1 is intact.

**That is R-11 firing on my own act for the third time today** -- read the bytes before asserting a
mismatch. The wrong finding would have been confident, specific, and carried a new standing rule.

**What survives is weaker and real.** Because the addendum only appends, the superseded constants still
stand in the fence text above it: a grader reading FWD-19 linearly meets *"all 93"*, *"the 60
today-unresolved"* and *"the 11 that can never carry prose"* before reaching the note that every one is a
reading. My own banked lesson says a supersession marker sits ON the superseded bytes; mine sits directly
beneath them, inside the same block, which is the acceptable case -- but it is adjacency, not replacement.

**FWD-19 graded, three limbs:**

| limb | grade |
|---|---|
| the partition sums to the folder count | **MET** -- `dossier_served 82 + served_as_empty_shell 12 + resolved_no_prose 0 + unresolved_with_reason 0 = 94 = folders`, and CRPS-g-3 @`bae7f689bc` emits the fence's own three names with the fold stated |
| *"the 60 today-unresolved folders are inducted by a SCRIPTED producer and re-ingested"* | **NOT EXERCISED** -- see below |
| *"the 11 that can never carry prose ... are NAMED with their reason"* | **NOT MEASURED BY THIS ARTIFACT** -- the census prints the count 12; `--folder-by-index 0` proves a name+reason is retrievable per folder, which is not the same as the census naming them |

**Limb 2 is the one worth stating carefully.** `unresolved_in_universe` reads **0** today where the fence
says 60. A zero population does not satisfy a clause that demands an ACT be exercised on that population --
that is 22a's `ABSENT != EXERCISED-AGAINST`. **The discriminator is HOW the 60 reached 0:** by induction
plus re-ingest (limb 2 exercised, MET) or by re-mints and registrations of the identity layer (limb 2 never
ran). This session's own record points at the second -- the folder count moved 93 to 94 to 95 by a
crosswalk re-mint and, for AIA, a REGISTRATION -- so I grade limb 2 **NOT EXERCISED** and name the
discriminator rather than claim it. **Grading it MET on an empty population would have retired the
induction mechanism as proven by its own absence.**

---

## 6. THE REMAINING SIX, IN ONE LINE EACH

| id | grade | one line |
|---|---|---|
| FWD-12 | NOT REALIZED | limb 3 alone (the team's cases). Limb 2 is MET per A1 -- 0 'not authorized' reasons across 9,183 rows in 91 dossiers. Blocked on the Upside/Downside method, RESERVED at Andrew |
| FWD-14 | NOT REALIZED | the sum holds (four names -> 94 = folders) but **none of the four literally reads the fence's `resolved / ambiguous / empty-or-workbook-only`**. Same class as round 4's R-2 on a DIFFERENT triple, which g-3's line does not cover |
| FWD-17 | NOT REALIZED | not "unmeasurable". Half (a) needs a write; half (b) carries a **candidate violation** -- 3 same-day `IMB_LN_Equity` objects, same first extract input key+sha, **different `content_sha256`**. Routed to round 6 with its discriminator |
| FWD-18 | NOT REALIZED | grade right, grounding wrong. `dossier.py` does not own `thesis_pillars`; `continuation.py` produces it. Re-measured there with controls passing: `terms` x5, none a pillar field; `keyword`/`keywords`/`feed_filter`/`filter` zero |
| FWD-2 | REALIZED | with a disclosed residual the fence's own clause does not cover: **354 bronze objects produce 353 silver rows** and the 1 bronze-without-silver is unexplained. A surprise row, not a grade change |
| FWD-4 | REALIZED | exercised on the SERVED proof rather than re-run -- refusing transport, positive-controlled poison, `vendor_calls 0`, S3 writes 0, WILL-ADD printed before anything added |

---

## 7. WHAT THIS PASS OWES FORWARD

1. **The CORPUS/RESAPP seam (section 3) is an endpoint question, not a cell.** Three outcomes cannot be
   closed by the project that holds them. Either the render clauses move to RESAPP's endpoint, or CORPUS's
   three fences are rewritten to the data plane they can actually reach. **That is an L2/L4 act at this
   seat and it is the pass's largest output.**
2. **FWD-19 limb 2's discriminator** -- did the 60 reach 0 by induction, or by re-mint? One read of the
   induction run's own history against the coverage document answers it.
3. **FWD-9's census needs a third state.** UNRESOLVED is not REACHES.
4. **FWD-2's 1 bronze-without-silver row** -- a surprise row, owner the issuer.
5. **The L10 analysis still waits on a slug.** This pass is the coverage read, not the round's grade.

## Compiler Tools

`python -c` over the evidence JSON to classify all 19 rows by what their instrument touched, with the
matched substring PRINTED per row -- which is what showed 2 of my 5 disclosure hits were matcher artifacts
-- `comp-read --enumerate 'DELIVERABLES_DIR'` for a banded count with a denominator before reading the
definition at `:117` -- `git diff --shortstat` before asserting an amendment replaced anything, the read
that killed a confident wrong finding -- `git log --since` on the PRD to bound the fence-vintage hole to
one commit, then `grep -oE 'FWD-[0-9]+'` on the diff plus a CONTROL counting changed lines WITHOUT the id
-- `git merge-base --is-ancestor` to place the evidence pin before the addendum.
