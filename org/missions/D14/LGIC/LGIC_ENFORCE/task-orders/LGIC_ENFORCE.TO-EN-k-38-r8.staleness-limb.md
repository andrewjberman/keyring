# TO LGIC_ENFORCE.TO-EN-k-38-r8 -- THE STALENESS LIMB: a row that EXISTS, is OPEN, is OWNED, and has not moved is invisible to every mechanism ruled to date

<to_id>LGIC_ENFORCE.TO-EN-k-38-r8</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-k-38` (decomposition v3.7 s.0h) | **outcome_ref:** FWD-2 | **depends_on:** `EN-g-37-r8` -- SECOND of slot `~2`'s queue

---

## WORKER FACE

### THE CELL

`EN-k-38`. Add a SECOND limb to `.tools/surprise-row-gate.py`: **grade an OPEN remediation row that has
a named owner and has not moved across N rounds.**

`LGIC_ENFORCE-W7-S1` is the instance that named the class. It is class BLOCKING, `remediation.state`
OPEN, `remediation.owner` `1.0.0_SA_CTO`, and its clock opened `2026-09-15T15:33Z`. **It sat OPEN and
OWNED for 67 hours, through every census report that re-measured its own token, and nothing in the
estate could see it.**

### WHY THIS IS NOT `EN-g-37` AGAIN, AND IT IS THE WHOLE POINT OF THE CELL

```
  MISSING     (S74)   GRADUATED, no remediation row   -> EN-g-37's rowlessness limb catches it
  UNSERVED    (S75)   the row EXISTS, OPEN, owned     -> NO ROWLESSNESS LIMB WILL EVER SEE IT
```

⛔ **A CHECK SCOPED TO ROWLESSNESS CANNOT SEE A DEFECT IN A ROW THAT IS PRESENT.** That is Rule 22's
shared-blindness clause, and it is exactly why `W7-S1` survived eight rounds: every instrument that
looked asked *"does a row exist?"* and the answer was always yes.

**`k38-distinct` IS THE ARM THAT PROVES THE ROUND BOUGHT TWO THINGS.** Your mutant must be a row that
`EN-g-37`'s limb **PASSES** -- a real, present, OPEN remediation row -- and that YOUR limb REFUSES.
Record all three facts:

```
  {"distinct_from_rowlessness": {"mutant_row_exists": true,
                                 "rowlessness_limb_verdict": "PASS",
                                 "staleness_limb_verdict": "REFUSED"}}
```

⛔ **IF `EN-g-37`'s LIMB ALSO REFUSES YOUR MUTANT, THE ROUND BUILT ONE LIMB TWICE AND BOUGHT NOTHING.**
That is a BLOCKING surprise row, not something to work around by reshaping the mutant.

### THE SAME TWO CONTROLS, GRADED AS PEERS

- **MUTANT** -- a planted stale OPEN row is REFUSED.
- **POSITIVE CONTROL** -- a FRESH open row, legitimately in flight, still PASSES.

⛔ **A STALENESS LIMB WITH NO POSITIVE CONTROL REFUSES EVERY ROUND THAT HAS ANY OPEN WORK**, which is
every round. The positive control is the half that makes "stale" mean something other than "open".

**DEFINING N IS YOURS AND IT IS A JUDGMENT THE ARMS DO NOT MAKE.** State the threshold you chose, in
ROUNDS or in TIME, and say what you measured it against. The CVO grades the choice; the arms only check
that a fresh row passes and a stale one does not.

**Read:** `R8_BASE.json`'s `clock_failure_classes_that_must_not_share_a_remedy`; rows
`LGIC_ENFORCE-S75`, `S76` and `W7-S1`; `EN-g-37-r8`'s record, which will be at HEAD on your branch
before you start.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/STALENESS_LIMB_R8.json`

```
  {"limb": {"positive_control": {"what": "...", "outcome": "PASS"},
            "mutant":           {"what": "...", "outcome": "REFUSED"}},
   "distinct_from_rowlessness": {"mutant_row_exists": true,
                                 "rowlessness_limb_verdict": "PASS",
                                 "staleness_limb_verdict": "REFUSED"}}
```

The limb's function must be named `_stale_open_row` -- the arm reads that token in the gate source, and
R8_BASE pins its absence at the cut.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="K38R8-AC1" cell_refs="EN-k-38"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py k38-limb-present</invocation><expect>PASS-K38-LIMB-PRESENT</expect></criterion>

<criterion id="K38R8-AC2" cell_refs="EN-k-38"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py k38-controls</invocation><expect>PASS-K38-CONTROLS</expect></criterion>

<criterion id="K38R8-AC3" cell_refs="EN-k-38"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py k38-distinct</invocation><expect>PASS-K38-DISTINCT</expect></criterion>

<criterion id="K38R8-AC4" cell_refs="EN-k-38" judgment="true"/>

<expected_criteria>K38R8-AC1, K38R8-AC2, K38R8-AC3, K38R8-AC4</expected_criteria>

**ALL THREE MECHANICAL CRITERIA READ FAIL AT THE CUT**, MEASURED: the `_stale_open_row` token has 0
occurrences in the gate across 2437 lines, and your record does not exist.

**`K38R8-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the chosen N is defensible
against the estate's real round cadence rather than picked to make `W7-S1` fire, and whether the
positive control is a genuinely fresh row. The arms can only check that the three verdicts differ in
the required directions.

**THE CHECKER'S CONTROLS:** `selftest-arms` drives **31 arms, 13 POSITIVE-SATISFIABILITY**. Run it
first. An arm a correct record cannot satisfy is a BLOCKING surprise row quoting the arm and its
output.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/` and this order's own file. Nothing else.
- **Branch.** The SAME worktree as `EN-g-37-r8`, continued. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU DO NOT EDIT `EN-g-37`'s LIMB.** If you believe it is wrong, that is a surprise ROW with its measurement, not an edit. Its criteria are already graded.
- ⛔ **NOTHING LIVE MOVES.**
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump the array; assert the non-ASCII CHARACTER count and the backslash-u count unchanged.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, re-measured at your own write time.
- **Commit before you grade.**

<paths>
.tools/surprise-row-gate.py
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.7, round-8 cell `EN-k-38` (section 0h).
<owned_cells>EN-k-38</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `K38R8-AC1` through `K38R8-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-k-38-r8.staleness-limb.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> K38R8-AC1,K38R8-AC2,K38R8-AC3,K38R8-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-k-38-r8.staleness-limb.md` BEFORE the `complete` flip.
Result file `staleness-limb.r8.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`K38R8-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the N you chose and what you measured it against, and the THREE verdicts of `k38-distinct` -- because those three are what say the round bought two limbs rather than one twice.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-8 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-8 cut: no grant moves and no IAM surface is touched.
comp-adversary: RUN at the round-8 cut: the adversarial control is k38-distinct, and it is adversarial against THIS ROUND'S OWN DESIGN rather than against the cell. If the two limbs turn out to answer one question, the arm fails and the round's central choice -- two cells, not one -- is falsified in public. It is the only arm in round 8 that can refuse the DECOMPOSITION rather than the work.
lane: the <paths> block is the grant; .tools/ is lane ANY.
contention: .tools/surprise-row-gate.py is written by EN-g-37-r8 FIRST on this SAME SLOT and then by this cell. Sequenced, never concurrent -- that serialisation is why round 8 is three slots over four cells.
</preflight>

Seating: slot `~2`, level 1, SECOND of a two-order queue (`EN-g-37-r8` -> `EN-k-38-r8`). Round 8 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.7 s.0h, from the REGISTER's ROUND 8 MATERIAL block `(d)` second half. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/`. Rulings carried: R-66 addendum, R-70.
