# TO LGIC_LGCTFM.TO-LT-m-2-r5 -- WHICH PRODUCER WRITES AN S3Key WITH NO BUCKET, AND HOW MANY PRODUCERS ARE THERE

<to_id>LGIC_LGCTFM.TO-LT-m-2-r5</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-m-2` (decomposition v1.6 s.16) | **outcome_ref:** FWD-1 | **depends_on:** none -- the only cell this round

---

## WORKER FACE

### THE CELL

`LT-m-2`, and **it is a MEASUREMENT cell, not a repair cell.** `1.0.0_SA_CTO`'s round-4 analysis
(@`abea09f936`) cut it that way for a stated reason:

> *"The malformed and the tier-prefixed rows are plausibly TWO causes, and a cell that assumes one remedy
> will make the numbers agree rather than the data. The first question is WHICH PRODUCER writes an S3Key
> with no bucket, and HOW MANY producers there are."*

⛔ **YOU DO NOT FIX ANYTHING THIS ROUND.** A remedy is the next round's question, and proposing one here is
the assumption the analysis refuses.

**Measured by the issuer at the cut (`a25a11ab75`) from the round-4 run's own contract -- RE-MEASURE IT
YOURSELF, do not carry these numbers:** 404 contract rows, **154 S3Key**, all with a string path. Leading
segment after `s3:` -- `opal-data-bd` 130, `platinum` 12, `gold` 10, `silver` 1, `blackdiamond` 1. So **24
of 154 resolve to no bucket**: 23 tier-prefixed and 1 firm-prefixed.

⚠ **WHERE THE ISSUER'S MEASUREMENT DISAGREES WITH THE ANALYSIS, AND IT MATTERS TO YOUR HUNT.** The analysis
describes the 24th row as a **malformed single-colon `s3:`**. In the run this seat read there is **no bare
`s3:` row at all** -- the 24th is `s3:blackdiamond/49f/_ops/pull_state.json`, FIRM-prefixed, a different
shape with a plausibly different producer. The total (24 of 154) and the tier split (12/10/1) agree
exactly; only that one row's characterisation differs. **Hunt, do not confirm:** if a bare `s3:` row exists
in a run this seat did not read, find it and say so.

### WHAT YOU BUILD

1. **The POPULATION, re-measured at your own write time** -- every S3Key row whose bucket resolves to
   nothing, by `row_id`, with the denominator (S3Key rows, and contract rows) printed. The arm compares
   your list to its own measurement and refuses BOTH an under-enumeration and an invented row.
2. **THE PRODUCER OF EACH ROW, NAMED AT A CODE SITE** -- `file:line` or the leg's name in
   `lib/opal_lgctfm.py`, plus **HOW you attributed it**: the instrument you ran, not the inference you
   drew. ⛔ **A GUESS FROM THE PATH'S SHAPE IS NOT AN ATTRIBUTION** -- the whole reason this is a
   measurement cell is that the shapes are what mislead.
3. **THE PRODUCER COUNT**, stated, and it must equal the length of your `by_producer` list.
4. ⭐ **AN UNATTRIBUTED ROW IS ALLOWED AND MUST BE NAMED WITH ITS REASON.** If an instrument genuinely
   cannot reach a row's producer, list it in `unattributed` with `why`. **What the arm refuses is SILENCE
   -- a row in neither list.** You are not required to invent a producer to make a count come out, and if
   you feel pressure to, that pressure is the defect and it is a BLOCKING row.
5. **THE VINTAGE FIELD, NEW THIS ROUND** (`1.0.0_SA_CTO` ADDENDUM 3 @`b1693a5b79`, ruled into round 5's
   carrier): your record carries `fixed_inputs_at_pin`, mapping each fixed input you actually invoked to
   the COMMIT you invoked it at. Both `check_lt_r5.py` and `R5_BASE.json` must appear, and each commit must
   resolve against that path. **This is what retires the sweep: a proof that carries the commit of the
   input it invoked cannot be aimed at the wrong window, because the value and its claim travel together.**

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/R5_BASE.json`; this is a quotation of it)**

```json
{
  "population": {"s3key_rows": 0, "without_a_resolvable_bucket": 0, "by_shape": {"<shape>": 0}, "row_ids": ["<row_id>"]},
  "producers": {"count": 0, "by_producer": [{"producer": "<file:line or leg name>", "rows": ["<row_id>"], "how_it_was_attributed": "<the instrument, not the inference>"}]},
  "unattributed": {"rows": ["<row_id>"], "why": "<what the instrument could not answer>"},
  "no_repair": {"engine_or_registry_commits_by_this_cell": 0},
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/BUCKETLESS_S3KEY_R5.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="M2R5-AC1" cell_refs="LT-m-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_lt_r5.py s41-population</invocation><expect>PASS-S41-POPULATION</expect></criterion>

<criterion id="M2R5-AC2" cell_refs="LT-m-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_lt_r5.py s41-producers</invocation><expect>PASS-S41-PRODUCERS</expect></criterion>

<criterion id="M2R5-AC3" cell_refs="LT-m-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_lt_r5.py s41-no-repair</invocation><expect>PASS-S41-NO-REPAIR</expect></criterion>

<criterion id="M2R5-AC4" cell_refs="LT-m-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_lt_r5.py r5-vintage-field</invocation><expect>PASS-R5-VINTAGE-FIELD</expect></criterion>

<criterion id="M2R5-AC5" cell_refs="LT-m-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_lt_r5.py r5-stale-proofs</invocation><expect>PASS-R5-STALE-PROOFS</expect></criterion>

<criterion id="M2R5-AC6" cell_refs="LT-m-2" judgment="true"/>

<expected_criteria>M2R5-AC1, M2R5-AC2, M2R5-AC3, M2R5-AC4, M2R5-AC5, M2R5-AC6</expected_criteria>

**WIRING AT THE CUT, measured by the issuer and disclosed rather than discovered by you:** `AC1`, `AC2` and
`AC4` **FAIL** (no record exists yet). ⚠ `AC3` and `AC5` are **GUARD-SHAPED and read PASS at the cut** --
`AC3` guards against a repair you must not make, and `AC5`'s window is empty until a fixed input moves.

**`M2R5-AC6`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the causes are genuinely
DISTINGUISHED or merely made to agree -- and whether each `how_it_was_attributed` describes an instrument
that was RUN, rather than a reading of the path that was already on the page.

⭐ **THE BAR THIS ROUND'S CRITERIA WERE BUILT AGAINST, and you may hold me to it:** every criterion above
was checked against a HAND-BUILT CORRECT RECORD before this order shipped, and that record is driven in the
checker's own self-test as a POSITIVE-SATISFIABILITY arm. The CTO's words, from round 4's analysis: *"can a
CORRECT artifact satisfy this? Where the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."*
**Round 4 produced FOUR criteria that no correct record could satisfy, and all four were found by the
worker being graded.** If you find a fifth, file it as BLOCKING and keep working -- that is the expected
behaviour here, not an escalation.

**THE CHECKER'S CONTROLS:** run `... check_lt_r5.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`.
The run PRINTS its own arm total and positive count -- do not trust a number quoted in an order, including
this one.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`lib/opal_lgctfm.py`, `infra/logic/registry/` AND `LEGACY_SERVED_PATHS.json` ARE NOT YOURS THIS ROUND.**
  `s41-no-repair` grades the commits **YOU** authored against those paths -- another seat's commit there is
  excused and printed, never charged to you. You may READ the engine freely; instrumenting it to attribute
  a producer is done in a scratch copy outside the repo, never by editing it.
- ⛔ **NO NEW RUN IS REQUIRED and none is forbidden.** If you run the engine to attribute a producer, the run
  lands in the run home as usual and your record names the run you measured.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve the file's
  line endings exactly. Copy an existing row's field set exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured
  at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.6, round-5 cell `LT-m-2` (section 16).
<owned_cells>LT-m-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `M2R5-AC1` through `M2R5-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-m-2-r5.which-producer-writes-a-bucketless-key.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> M2R5-AC1,M2R5-AC2,M2R5-AC3,M2R5-AC4,M2R5-AC5,M2R5-AC6 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-m-2-r5.which-producer-writes-a-bucketless-key.md` BEFORE the `complete` flip.
Result file `which-producer-writes-a-bucketless-key.r5.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`M2R5-AC6` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the population with its
denominator, every producer with the instrument that attributed it, the producer COUNT, every unattributed
row with its reason, and -- in one sentence each -- whether the tier-prefixed and firm-prefixed shapes have
the SAME producer or different ones, and whether a bare `s3:` row exists anywhere you looked.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-5 cut: no schedule is created or read.
comp-iam: RUN at the round-5 cut: no grant moves; the cell reads no IAM surface.
comp-adversary: RUN at the round-5 cut: the adversarial control is AC2's pairing of attribution with instrument. The cheapest satisfying move is to attribute every row to one producer read off the path's shape -- exactly the "make the numbers agree rather than the data" failure the analysis refuses -- so `how_it_was_attributed` is required per entry and an EMPTY reason fails, while an honestly unattributed row PASSES when named with its why. AC3 grades the cell's own commits by author (W1-S39's repair) so no foreign commit can make it unsatisfiable.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ by the tree convention. The engine and registries have NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies, the slot does not isolate there.
</preflight>

Seating: slot `~1`, level 0, the only order this round. Round 5 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G`
on decomposition v1.6 s.16, from `1.0.0_SA_CTO`'s round-4 analysis @`abea09f936`. Fixed inputs:
`deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/` (`check_lt_r5.py`, `R5_BASE.json` pinning `a25a11ab75`).
Rulings carried: the CUT-TIME criterion bar (round-4 analysis), ADDENDUM 3's vintage field, R-43, W1-S39's
author-scoped no-repair shape.
