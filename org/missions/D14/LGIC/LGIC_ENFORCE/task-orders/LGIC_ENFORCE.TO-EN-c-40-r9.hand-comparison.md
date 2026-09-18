# TO LGIC_ENFORCE.TO-EN-c-40-r9 -- THE COMPARISON THE CENSUS DECLINES: FWD-5's only remaining structural clause, never attempted in eight rounds

<to_id>LGIC_ENFORCE.TO-EN-c-40-r9</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-c-40` (decomposition v3.8 s.0i) | **outcome_ref:** FWD-5 | **depends_on:** none -- the only order on slot `~1`

---

## WORKER FACE

### THE CELL

`EN-c-40`. **The round-8 census report names its own gap, one occurrence, verbatim:**

> *"The comparison against LGIC_NAMING's hand gradings is EN-s-2's and is not made here."*

**THAT SENTENCE IS `W7-S4`, and it is `FWD-5`'s clause 3 -- "totals agree with the hand ranking".
IT HAS NEVER BEEN ATTEMPTED IN EIGHT ROUNDS.** Your job is to make the comparison.

⛔ **AND IT HAS BEEN POSSIBLE SINCE ROUND 4, NOT ROUND 8.** The census first ran to completion at
round 4 (`.r4.md`, judged_live 1690 / judged_repo 1547, stopped null). Round 7's analysis asserted
*"judged_live is 3 of 1829"* while that report had been in the tree for 13 hours. The item sat four
rounds under three analyses because a stale figure made its precondition look unmet. `1.0.0_SA_CTO`
recorded that against itself. Do not let a stale figure do it again -- **re-measure every number you
use.**

### THE THREE SURFACES, AND YOU COMPARE ALL THREE

```
  GRADING_RULE.md section 9   worked cases    org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md
  n6-grader-a.tsv             grader rows     .../deliverables/exercises/n6-grader-a.tsv
  TENSION_RANKING.md          ranked surfaces .../deliverables/TENSION_RANKING.md
```

Their shapes were verified by the issuer at the cut: 510 / 89 / 149 lines, all three MATCHING their
cited counts. `n6-grader-a.tsv` is 89 LINES == 1 `# base` header + **88 DATA ROWS** -- both figures
circulate and both are right.

⛔ **THE ONE FIGURE THAT DOES NOT MATCH, AND IT IS AN ARM.** The register and the round-8 analysis
both say section 9 carries **43** worked cases. The issuer parsed the fence and got **45**
(CONFORMANT 18, OUT-OF-PATTERN 20, ALIAS 3, RAISE 2, NOT-GRADED 2, across 26 types).
`c40-recount` requires you to **RE-COUNT AT YOUR OWN WRITE TIME, PRINT THE DENOMINATOR, AND NAME WHICH
CARRIER IS STALE.** Whichever number you get, say which document is wrong. An arm that accepted 43
unexamined would have compared 43 cases against a population of 45.

### WHAT A COMPARISON HAS TO BE

For each of the three surfaces: take each hand grading, take `grade()`'s verdict for the same name at
the completed census's vintage, and record **AGREE or DISAGREE**. Then per surface:

```
  agree + disagree == compared,  with `compared` re-measured at YOUR write time
  every DISAGREEMENT named, with its `name` and a `why`
```

⛔ **A COUNT OF DISAGREEMENTS WITH NO IDS IS A NUMBER NOBODY CAN ACT ON.** Clause 3's whole point is
that the totals be RECONCILABLE, so `disagreements` must list exactly as many entries as `disagree`.

⛔ **DISAGREEMENT IS NOT FAILURE.** A hand grading and the builder differing is a real finding about
one of them, and it is worth more than a comparison engineered to agree. Record what you find.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/HAND_COMPARISON_R9.json`

```
  {"worked_cases": {"counted": <int>, "which_carrier_is_stale": "...",
                    "denominator_measured_at_write_time": {"instrument": "...", "value": <int>}},
   "surfaces": {"grading_rule_worked_cases": {"compared": <int>, "agree": <int>, "disagree": <int>,
                                              "disagreements": [{"name": "...", "why": "..."}],
                                              "denominator_measured_at_write_time": {...}},
                "n6_grader_rows":            { ... the same ... },
                "tension_ranking_surfaces":  { ... the same ... }}}
```

Any instrument you cite goes in that same folder and is **COMMITTED** (row `LGIC_ENFORCE-S69`).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="C40R9-AC1" cell_refs="EN-c-40"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py c40-recount</invocation><expect>PASS-C40-RECOUNT</expect></criterion>

<criterion id="C40R9-AC2" cell_refs="EN-c-40"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py c40-population</invocation><expect>PASS-C40-POPULATION</expect></criterion>

<criterion id="C40R9-AC3" cell_refs="EN-c-40"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py c40-agreement</invocation><expect>PASS-C40-AGREEMENT</expect></criterion>

<criterion id="C40R9-AC4" cell_refs="EN-c-40"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py c40-disagreements</invocation><expect>PASS-C40-DISAGREEMENTS</expect></criterion>

<criterion id="C40R9-AC5" cell_refs="EN-c-40" judgment="true"/>

<expected_criteria>C40R9-AC1, C40R9-AC2, C40R9-AC3, C40R9-AC4, C40R9-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, MEASURED by the issuer. No guard-shaped
criterion in this cell.

**`C40R9-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each AGREE is a genuine
match rather than a comparison loosened until it agreed, and whether each DISAGREE's `why` identifies
which side is wrong. The arms can only check that the arithmetic closes and every disagreement is
named.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **27 arms, 13 POSITIVE-SATISFIABILITY**. Run it
first. An arm a CORRECT record cannot satisfy is a BLOCKING surprise row quoting the arm and its
output -- never a workaround, never an edit to a fixed input.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **THE THREE LGIC_NAMING INSTRUMENTS ARE READ-ONLY.** They are another project's deliverables and you CITE them; you never edit them. If one is wrong, that is a surprise ROW with its measurement.
- ⛔ **YOU DO NOT EDIT `org/standards/NAMING_SCHEMA.json`** -- that is `EN-s-41`'s this round.
- ⛔ **NO GRADE MOVES.** You are comparing existing verdicts, not re-deciding them.
- ⛔ **NOTHING LIVE MOVES.** Every AWS read is read-only through the `.tools/aws` shim.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump the array; assert the non-ASCII CHARACTER count and the backslash-u count unchanged. `len(b)-len(b.decode())` is a BYTE DELTA, not a character count; for a count use `sum(1 for ch in text if ord(ch) > 127)`.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **Two other orders are open this round.**
- **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.8, round-9 cell `EN-c-40` (section 0i).
<owned_cells>EN-c-40</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `C40R9-AC1` through `C40R9-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-c-40-r9.hand-comparison.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> C40R9-AC1,C40R9-AC2,C40R9-AC3,C40R9-AC4,C40R9-AC5 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-c-40-r9.hand-comparison.md` BEFORE the `complete` flip.
Result file `hand-comparison.r9.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** The instance's `controls` block admits only `mutant`/`determinism`; fold positive-control evidence into `mutant`. `introduces` entries must be LITERAL tokens present at the pin and absent at its parent, not prose.
`C40R9-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the worked-case count you measured and WHICH CARRIER IS STALE, then per surface `agree + disagree == compared` with its own denominator, and name every disagreement.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-9 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-9 cut: no grant moves. The cell READS another project's deliverables and writes NONE of them -- a read-only widening of what it consults, stated here because the <paths> block cannot express "may read, must not write".
comp-adversary: RUN at the round-9 cut: the adversarial control is c40-recount. The cheapest way to satisfy every other arm is to take the register's 43 and compare 43 cases; the arm forces a re-count and a named stale carrier, so the cell cannot inherit the very figure that hid this item for four rounds. It is the arm that makes the cell about the POPULATION rather than about the comparison.
lane: the <paths> block is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ is granted by the tree convention. LGIC_NAMING's deliverables are read-only by a BOUND rather than by a path.
contention: the channel is written by two other open orders this round. THREE SLOTS and the channel is the ONLY shared file -- 14b's append-only inversion applies and no slot isolates there. No other round-9 cell reads or writes LGIC_NAMING.
</preflight>

Seating: slot `~1`, level 0, the only order on its slot. Round 9 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.8 s.0i, from the REGISTER's WHAT ROUND 9 OWES `(a)`, read at HEAD. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/` (`check_en_r9.py`, 12 real arms and a 27-arm self-test with 13 positive-satisfiability arms; `R9_BASE.json` pinning `d9cdb39063`). Rulings carried: R-66, S81, R-38.
