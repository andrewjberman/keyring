# TO LGIC_ENFORCE.TO-EN-p-38-r14 -- 1449 AND 1303 ARE TWO GRAINS, MEASURED SO THEY CAN NEVER READ AS DISAGREEING

<to_id>LGIC_ENFORCE.TO-EN-p-38-r14</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- re-graded 2026-09-19 by 0.9.0_WK_LGIC_ENFORCE~2 after LGIC_ENFORCE-S106's checker repair (@acdba45160): P38R14-AC1 PASS-P38-GRAIN, P38R14-AC2 PASS-R14-VINTAGE-FIELD (was FAIL pre-repair, on the sibling cell's absent record, not this cell's artifact -- the diagnosis was S106), P38R14-AC3 PASS-R14-STALE-PROOFS, P38R14-AC4 UNVERIFIABLE-BY-INSTRUMENT recorded for 3.0.0_SA_CVO at L9. proof-of-spec-check VALID rc=0 @27a8cec42d. No re-measurement of the grain; no touching EN-r-7.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-p-38` (decomposition v3.13 s.0n) | **outcome_ref:** FWD-3 | **depends_on:** none -- **NOT paired with `EN-r-7`, which runs beside it**

---

## THE CELL

`EN-p-38`. A MEASUREMENT. `3.0.0_SA_CVO`'s `S102`, measured at L9 on the round-13 record: the per-token row
counts **sum to 1449** against a population of **1303 rows**, and the record discloses the overlap
**NOWHERE**. The phrases *"more than one"*, *"multiple"*, *"overlap"*, *"sum"* and *"may carry"* are each
ABSENT from it. A row may carry several placeholder tokens, so `tokens.by_token[].rows` is **PER TOKEN**
while `population.rows_with_a_placeholder` is **PER ROW** -- **two different grains printed adjacent under
the same word, `rows`.**

⛔ **IT IS A MEASUREMENT CELL. YOU FIX NOTHING AND YOU RE-OPEN NOTHING.** `S102` says so in its own terms:
the figures are **CORRECT**, the field name `rows` is accurate PER TOKEN, the cause verdict and the producer
attribution do not depend on it, and **1303 is the figure the delta uses**. What is missing is the sentence
that stops a reader adding the column and concluding the two figures disagree. Round 13's verdicts STAND.

⭐ **AND THE HONEST ANSWER MAY BE SMALL.** If it turns out few rows carry more than one token, say so --
`AC1` accepts `rows_carrying_more_than_one: 0` exactly as readily as a large number, proven by a positive
arm in the self-test. **A criterion that only passed on a big overlap would be an instruction to find one.**
What the arm refuses is arithmetic that does not close: a sum above the row count with no multi-token row
cannot be true, and neither can equal figures with multi-token rows.

## WHAT YOU BUILD

1. **THE INPUT, PINNED BY COMMIT.** `PLACEHOLDER_POPULATION_R13.json` and
   `PLACEHOLDER_POPULATION_TABLE_R13.md` **at `c05f9f9fc9`**, read with `git show <commit>:<path>` -- not
   from the working tree. ⛔ **THE CELL BESIDE YOU REGENERATES THAT TABLE THIS ROUND.** The pin is what lets
   the two of you run in parallel with no ordering; an unpinned read is an input moving underneath your
   measurement. Record the pin in `grain.input_report_pinned_at`; the arm refuses a record without one.
2. **`by_token_sum`** -- the sum of `tokens.by_token[].rows` at that pin, recomputed by you, not copied.
3. **`rows_with_a_placeholder`** -- the population figure at that pin.
4. **`rows_carrying_more_than_one`** -- measured from the row-level artifact, not inferred from the
   difference. ⚠ **`sum - rows` is NOT the count of multi-token rows** -- it is the count of EXTRA
   token-row incidences, which equals the multi-token row count only when no row carries three or more.
   Measure it; if it happens to equal the difference, that is a finding, not an assumption.
5. **THE DISTRIBUTION** -- how many rows carry 1 token, how many carry 2, how many carry 3, and so on.
   Read it by SUBTRACTION from the row denominator, never as a forward list of the multiplicities you
   expected (Rule 24).
6. **THE RECONCILIATION SENTENCE** -- the arithmetic that makes 1449 and 1303 agree, written so the two
   figures can never again be read as disagreeing. This is the deliverable `S102` actually asked for.
7. **THE VINTAGE FIELD:** `fixed_inputs_at_pin`, mapping each fixed input you invoked to the COMMIT you
   invoked it at -- both `check_en_r14.py` and `R14_BASE.json`, each resolvable against its path.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/R14_BASE.json`; this is a quotation of its `grain` half)**

```json
{
  "grain": {
    "input_report_pinned_at": "<commit>",
    "by_token_sum": 0,
    "rows_with_a_placeholder": 0,
    "rows_carrying_more_than_one": 0,
    "distribution": {"<n tokens>": 0},
    "reconciliation": "<the arithmetic that makes 1449 and 1303 agree>"
  },
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/TOKEN_GRAIN_R14.json`.

## ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="P38R14-AC1" cell_refs="EN-p-38"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/check_en_r14.py p38-grain</invocation><expect>PASS-P38-GRAIN</expect></criterion>

<criterion id="P38R14-AC2" cell_refs="EN-p-38"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/check_en_r14.py r14-vintage-field</invocation><expect>PASS-R14-VINTAGE-FIELD</expect></criterion>

<criterion id="P38R14-AC3" cell_refs="EN-p-38"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/check_en_r14.py r14-stale-proofs</invocation><expect>PASS-R14-STALE-PROOFS</expect></criterion>

<criterion id="P38R14-AC4" cell_refs="EN-p-38" judgment="true"/>

<expected_criteria>P38R14-AC1, P38R14-AC2, P38R14-AC3, P38R14-AC4</expected_criteria>

**WIRING AT THE CUT:** `AC1` and `AC2` **FAIL** (no record exists yet). ⚠ `AC3` is **GUARD-SHAPED and reads
PASS at the cut** -- its window is empty until a fixed input moves.

⚠ **WHAT THE MECHANICAL ARMS CANNOT SEE, stated so you do not over-read a green:** the arm checks that your
figures are internally consistent and that the input is pinned. **It does not open the pinned report.** A
PASS means your arithmetic closes, never that the numbers came from that artifact. That half is `AC4`'s.

**`P38R14-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the figures were read from the
report at the stated pin; whether `rows_carrying_more_than_one` was MEASURED from the row-level artifact
rather than inferred from `sum - rows`; whether the distribution is complete against its denominator; and
whether the reconciliation sentence actually forecloses the misreading `S102` found.

⭐ **THE BAR THESE CRITERIA WERE BUILT AGAINST, and you may hold me to it:** each was checked against a
HAND-BUILT CORRECT RECORD before this order shipped, driven in the checker's self-test as a
POSITIVE-SATISFIABILITY arm (`python .../check_en_r14.py selftest-arms`, 28 arms, 9 positive). The CTO's
words: *"can a CORRECT artifact satisfy this? Where the honest answer is no, THE CRITERION IS THE DEFECT,
NOT THE CELL."* **One such criterion was found and repaired in the SIBLING order's draft this same cut.**
**If you find another, file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`deliverables/0.9.0_WK_LGIC_ENFORCE~1/` IS NOT YOURS.** You READ the r13 artifacts there AT THE PIN,
  through `git show`. You do not edit them, regenerate them, or correct the round-13 record. **The round-13
  record is FROZEN (R-43); its disclosure gap is what THIS round answers, in a NEW artifact.**
- ⛔ **DO NOT TOUCH `EN-r-7`'s QUESTION.** The cell beside you repairs the report's RENDERING. The analysis
  refused to pair you: *"they share a file and nothing else, and a joint cell will report the easier one."*
  Your record has no render field and your arms read none. **If the working-tree copy of the table looks
  different from your pin, that is that cell working -- use the pin and keep going.**
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line
  endings exactly. Copy an existing row's field set exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured
  at your own write time. **`S104` is taken -- this seat filed it at the cut, and one other order is open
  this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.13, round-14 cell `EN-p-38` (section 0n).
<owned_cells>EN-p-38</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `P38R14-AC1` through `P38R14-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-p-38-r14.the-token-grain.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> P38R14-AC1,P38R14-AC2,P38R14-AC3,P38R14-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-p-38-r14.the-token-grain.md` BEFORE the `complete` flip.
Result file `the-token-grain.r14.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`P38R14-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the pin you read at, the by-token
sum, the row population, the measured count of rows carrying more than one token, the full distribution with
its denominator, and the reconciliation sentence. State the INSTRUMENT that measured the multiplicity -- not
the inference you drew from the difference.

---

## RECORD FACE

⛔ **THE ONE-LINE RECUT THIS ROUND CARRIES, FOR `3.0.0_SA_CVO` AT L9:** the two cells this round are
DELIBERATELY UNPAIRED on the analysis's instruction, and they share exactly one file -- the r13 population
table. `EN-r-7` REGENERATES it; `EN-p-38` READS it AT A PIN. **An L9 that grades them as one round must not
grade them as one cell:** a finding about the rendering says nothing about the grain, and the easier cell
finishing first is not evidence about the other.

<preflight>
comp-schedule: RUN at the round-14 cut: no schedule is created or read.
comp-iam: RUN at the round-14 cut: no grant moves.
comp-adversary: RUN at the round-14 cut: the cheapest satisfying move for AC1 is to write `rows_carrying_more_than_one = by_token_sum - rows_with_a_placeholder` and never open the row-level artifact, which is WRONG whenever a row carries three tokens; the arm cannot catch that arithmetic (it is self-consistent by construction), so it is named on the order as the trap and routed to AC4, and the order states the identity's failure condition explicitly. The second-cheapest is reading the working-tree table while the sibling cell regenerates it, so the pin is a graded field. What no mechanical arm here can see is whether the figures came from the pinned artifact at all -- AC4.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~2/ by the tree convention. The round-13 deliverables are READ-ONLY to this cell and read through `git show`.
contention: the channel is shared -- append-only, 14b's inversion applies. The r13 table is REGENERATED by EN-r-7 this round and read HERE at a pin, so there is no ordering between the two cells.
</preflight>

Seating: slot `~2`, level 0, one of TWO unpaired orders this round. Round 14 of LGIC_ENFORCE, issued by
`2.0.0_SA_COO~G` on decomposition v3.13 s.0n, from `1.0.0_SA_CTO`'s round-13 analysis @`cf0cf68868` and
`3.0.0_SA_CVO`'s `S102`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r14/` (`check_en_r14.py`,
`R14_BASE.json` pinning `c05f9f9fc9`). Rulings carried: S85's ONE CARRIER, the CUT-TIME criterion bar,
ADDENDUM 3's vintage field, LD-0521, R-43's frozen history, Rule 24's subtraction.
