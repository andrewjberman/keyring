# TO LGIC_ENFORCE.TO-EN-g-30-r5 -- S62's remedy: a right total beside a wrong split

<to_id>LGIC_ENFORCE.TO-EN-g-30-r5</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-g-30` (decomposition v3.4 s.0e) | **outcome_ref:** FWD-3 | **depends_on:** none -- this cell's write surface is disjoint from every other round-5 cell's

---

## WORKER FACE

### THE CELL

`EN-g-30`. **You re-count one split FROM the table it describes, and you correct one stale word.** The document is
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/NAMING_CENSUS_COMPARISON.r4.md` -- your own
slot's deliverable, which is why this cell is yours.

**THE DEFECT, measured at the cut.** The document's machine-readable fence carries:

```
  "uncompared_reasons": {"NOT-GRADED-TYPE": 23, "AWS_FIXED-EXCLUDED": 2,
                         "CARDED": 11, "HAND-SPECIMEN-ABSENT": 11, "total": 42}
```

`23 + 2 + 11 + 11 = 47`, over a population the document's own Section 3 table and its own `total` field both put at
**42**. **A right TOTAL beside a wrong SPLIT is what lets the error survive every reader**, because a reader who
checks anything checks the total, and the total is correct.

**WHAT YOU DO.**

1. **Re-count each reason FROM the Section 3 table**, which is the population the split describes -- not from the
   fence, not from recall, and not from this order. The parts must sum to the total AND each part must equal what the
   table actually holds.
2. **PRINT THE SPLIT BESIDE THE TOTAL** in the document's prose, so the next reader can check the PARTS rather than
   the sum. That is the remedy's real content: the sum was always checkable and was always right.
3. **Correct Section 3's stale count word.** It says *"THREE distinct, individually-verified reasons"* above a list of
   FOUR, while Section 4 says four. `THREE` occurs exactly **once** in the document at the cut, and the arm requires
   zero -- write the number that matches the list.

**NOTHING IN THE COMPARISON'S SUBSTANCE MOVES.** No row's individually stated reason is wrong; all 42 carry one. You
are repairing a summary, not a finding. Do not re-open a disagreement, do not re-run a census, and do not change any
row's reason.

**Read:** the comparison document whole; row `LGIC_ENFORCE-S62` on
`org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` and its remediation row in
`.../remediations/REMEDIATION_v2.md`; decomposition v3.4 s.0e.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G30R5-AC1" cell_refs="EN-g-30"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py g30-split</invocation><expect>PASS-G30-REASON-SPLIT-RECONCILES-TO-ITS-OWN-TABLE</expect></criterion>

<criterion id="G30R5-AC2" cell_refs="EN-g-30"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py g30-prose</invocation><expect>PASS-G30-STALE-COUNT-WORD-REMOVED</expect></criterion>

<criterion id="G30R5-AC3" cell_refs="EN-g-30" judgment="true"/>

<expected_criteria>G30R5-AC1, G30R5-AC2, G30R5-AC3</expected_criteria>

**AT THE CUT both mechanical criteria read FAIL** and each names its live defect: `g30-split` prints
`SUM MISMATCH: 47 != 42`, and `g30-prose` counts the one surviving `THREE`.

**HOW `g30-split` GRADES, stated because you should not have to guess and because the arm was repaired before you saw
it:** it takes the reason keys YOUR FENCE declares, counts exactly those in the document's table rows, and requires
(i) the parts to sum to the declared total AND (ii) every part to equal the table's count. Either test alone passes
the defect: a self-consistent split that disagrees with the table still fails, and so does a split that matches the
table but not its own total. **The arm's table-counting helper first counted every uppercase token in every table
cell and returned 36 keys summing to 149 -- resource types, verdicts, even two CloudFront distribution ids -- which
would have made a CORRECT fix fail.** That was found by running the real reader against this real document, not by
its self-test, and repaired before this order was cut.

**`G30R5-AC3`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the corrected document now lets a reader
check the parts without re-deriving them -- the remedy is legibility, and an arm can only measure arithmetic.

`<WS>` is your worktree's absolute path.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. **`NAMING_CENSUS_COMPARISON.r4.md` is inside YOUR OWN serial's folder, which is why this cell is yours** -- `.tools/owned-paths-validate.py` clause 4 permits exactly the serial named by the `deliverables/<SERIAL>/` sub-folder and refuses every other, measured the same night on a sibling project.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only.** A wrong arm is a BLOCKING row, never an edit.
- **Surprises** go to the project's `INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array, id `LGIC_ENFORCE-W<n>-S<k>` with `<k>` one above the highest already present in ANY document under that channel. Keep working after filing.
- **Judge from the files this order names and cite them** (`path:line @commit`).
- **Numbers in this order are CONTEXT, never acceptance values** -- the 20/2/10/10 the remediation row proposes is ANOTHER SEAT'S PARSE, not your measurement. Count the table yourself; if you get something else, that is a finding and a row, not a discrepancy to reconcile silently.
- **Commit before you grade.**
- **Nothing live moves.** This cell edits one markdown document.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.4, round-5 cell `EN-g-30` (section 0e).
<owned_cells>EN-g-30</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G30R5-AC1`, `G30R5-AC2`, `G30R5-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-g-30-r5.reason-split.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G30R5-AC1,G30R5-AC2,G30R5-AC3 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-g-30-r5.reason-split.md` BEFORE the `complete` flip.
Result file `reason-split.r5.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`G30R5-AC3` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and print your own table counts in it.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-5 cut: no schedule is created or read.
comp-iam: RUN at the round-5 cut: no grant moves; the cell edits one markdown document.
comp-adversary: RUN at the round-5 cut: the arm was exercised against the REAL document on three branches before this order was cut -- the live defective fence (FAIL, naming S62's shape), a simulated correct fence (PASS), and a self-consistent fence disagreeing with the table (FAIL) -- because an arm that only ever sees its own fixture cannot be known to be satisfiable by a correct fix.
lane: the <paths> block is the grant (RULING 1 shape c); NAMING_CENSUS_COMPARISON.r4.md sits under deliverables/0.9.0_WK_LGIC_ENFORCE~2/, which the tree convention grants to THIS serial and no other -- the seating follows the folder.
contention: this document is written by no other open order in either LGIC project at the cut, and no other round-5 cell writes inside deliverables/0.9.0_WK_LGIC_ENFORCE~2/.
</preflight>

Seating: slot ~2, level 0, the only cell on its slot and the only round-5 component that can run beside the queue. Round 5 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.4 s.0e. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/`. Rulings carried: S62's remediation row, R-40.
