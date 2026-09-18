# TO LGIC_LGCTFM.TO-LT-a-2-r2 -- THE RE-DERIVATION RECORD: which of round 1's fourteen claims a LATER seat can actually check

<to_id>LGIC_LGCTFM.TO-LT-a-2-r2</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `LT-a-2` (decomposition v1.3 s.12) | **outcome_ref:** FWD-3, FWD-9 | **depends_on:** none -- FIRST cell of slot ~1's queue

---

## WORKER FACE

### THE CELL

`LT-a-2`. **Round 1 graded fourteen judgment claims. Your job is to say which of them a LATER SEAT CAN
RE-DERIVE, and for each one that cannot, WHY.** You repair nothing and you re-grade nothing.

⛔ **THIS IS A RECORD, NOT A REPAIR, AND THE OBVIOUS READING OF THE TASK IS THE WRONG ONE.** The tempting
act is to fix round 1's checker. That is REFUSED: `check_lt_r1.py` is a FIXED INPUT of a CLOSED, GRADED
round, its arms' windows were NON-EMPTY on their own branches so the grades they fed are SOUND, and an
edit now moves no grade. **R-43 scopes a frozen-history defect's remedy to ONE LIVE-DIRECTION document,
never a sweep over rounds already closed.** If you edit that file this cell has failed regardless of its
arms.

### WHAT IS ACTUALLY MISSING

A claim that can only be verified in the place that makes verification REPETITION is not a claim an R19
migration can rely on. Nobody has ever written down which of round 1's claims survive that test. You write
it.

**THE DENOMINATOR IS THE ORDERS, NOT A LIST ANYONE REMEMBERS.** Fourteen round-1 task orders each carry
exactly one criterion with `judgment="true"`. `R2_BASE.json` pins the enumeration and its instrument, and
the arm partitions against it. Read them from the orders yourself as a control.

### WHAT YOU DO

1. **Pick a THIRD POSITION and declare it.** Not the branch that produced a claim, and not the checkout
   that graded it. A fresh detached checkout at a drained tip is the shape. Record it as `ran_from`.
2. **For each of the fourteen, try to re-derive the claim from that position** by running the invocation
   its own evidence names. Classify into `re_derived` (with `how`) or `not_re_derivable`.
3. **Every `not_re_derivable` entry carries `mechanism` AND `verdict_observed`** -- what is structurally
   wrong, and what the run actually PRINTED. A class with no mechanism is an opinion; the observed verdict
   is what makes it a measurement.
4. **Write `unscoped_read`**: how you SEARCHED the population, not what you found.

### FOUR IS A FLOOR AND NOT AN ANSWER, AND THIS IS THE CRITERION MOST LIKELY TO BE FAILED HONESTLY

`R2_BASE.json` names four arms already known checkout-dependent -- `x1-r16`, `x1-footprint`, `x2-flag`,
`x3-filed` -- and their polarities differ in a way that matters:

```
  x1-r16, x1-footprint   FALSE FAIL off-branch   loud; REPAIRED at 39e6977e95; they now pass in the shared tree
  x2-flag, x3-filed      VACUOUS PASS off-branch silent; NOT repaired; x2-flag would pass identically had
                                                 its cell touched the very file it exists to watch
```

⛔ **A FALSE FAIL ANNOUNCES ITSELF. A VACUOUS PASS DOES NOT** (`R-47`). The silent pair was found ONLY by
an unscoped read of the shared mechanism both arms call (`base_ref()`), never from the list of observed
failures -- because a vacuous pass produces no observation to start from. **So do what found them: census
the MECHANISM, not the sightings.** `grep` the round-1 checker for every caller of anything
checkout-relative or position-relative, then inspect each caller. A fifth shape is already named and NOT
counted in the four: `_last_two()` resolves a cell's subject BY POSITION in a directory five runs now
share.

**Your arm requires AT LEAST four, not exactly four**, and it requires the `unscoped_read` note. Landing
on exactly the handed list is admissible and will pass -- but say in the note how you searched, because a
count that equals the floor is the shape of a record that worked from the list.

**Read:** rows `LGIC_LGCTFM-S10` and `S18` whole; `R2_BASE.json`; the fourteen round-1 orders' judgment
criteria and the evidence each one's proof instance records.

### WHERE YOUR RECORD GOES

`<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/RE_DERIVATION_R2.json`

**AND ITS `instrument_path` MUST BE A TRACKED FILE.** Put any script you cite inside your own deliverables
folder and COMMIT it. Row `LGIC_ENFORCE-S69`: a sibling project's record cited `.scratch/measure_armed.py`
as the second reader whose agreement WAS its corroboration claim, and that file was untracked and one
`git worktree remove` from gone. Nothing in the estate grades an `instrument` string, so this cell's arm
does.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="A2R2-AC1" cell_refs="LT-a-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py a2-partition</invocation><expect>PASS-A2-PARTITION-COVERS-ROUND-1</expect></criterion>

<criterion id="A2R2-AC2" cell_refs="LT-a-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py a2-mechanism</invocation><expect>PASS-A2-EVERY-CLASS-NAMES-ITS-MECHANISM</expect></criterion>

<criterion id="A2R2-AC3" cell_refs="LT-a-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py a2-floor</invocation><expect>PASS-A2-KNOWN-FOUR-ARE-A-FLOOR</expect></criterion>

<criterion id="A2R2-AC4" cell_refs="LT-a-2"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_lt_r2.py a2-instrument</invocation><expect>PASS-A2-INSTRUMENT-IS-TRACKED</expect></criterion>

<criterion id="A2R2-AC5" cell_refs="LT-a-2" judgment="true"/>

<expected_criteria>A2R2-AC1, A2R2-AC2, A2R2-AC3, A2R2-AC4, A2R2-AC5</expected_criteria>

**ALL FOUR MECHANICAL CRITERIA READ FAIL AT THE CUT**, each because your record does not exist yet --
MEASURED by the issuer at the cut, not assumed. There is no guard-shaped criterion in this cell.

**`A2R2-AC5`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether each `re_derived` entry was
GENUINELY re-run from the declared third position rather than restated from the instance, and whether the
`not_re_derivable` population is the result of a mechanism census rather than the handed list of four. The
arms can only count and check fields.

**THE CHECKER'S OWN CONTROLS, so you know what it will and will not catch:** `selftest-arms` drives 28
arms, **10 of them POSITIVE-SATISFIABILITY against simulated correct records**. Run it first. A mutant test
proves an arm CAN fail; only the positive arm proves it can pass for the right reason. If an arm cannot be
satisfied by work you believe is right, that is a BLOCKING surprise row quoting the arm and its output --
never a workaround, and never an edit to a fixed input.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row, never an override.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`fixed_inputs/r1/check_lt_r1.py` IS READ-ONLY AND SO IS EVERY OTHER ROUND-1 FIXED INPUT.** Editing one fails this cell.
- ⛔ **YOU RE-GRADE NOTHING.** No round-1 criterion's verdict moves. You record re-derivability, which is a different property from correctness, and a claim can be SOUND AT ITS VINTAGE and NOT RE-DERIVABLE today. Say so where that is what you find.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md`, appended by **TEXTUAL SPLICE** to the fence that PARSES AS A LIST. ⛔ **NEVER RE-DUMP THE ARRAY** -- see the contention note in the RECORD FACE; this round is a stated test of that method. Id `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time.
- **Numbers in this order are CONTEXT, never acceptance values.**
- **Commit before you grade.**
- **Nothing live moves.** No apply, no AWS write, no deploy. This cell reads records and writes one.

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.3, round-2 cell `LT-a-2` (section 12).
<owned_cells>LT-a-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `A2R2-AC1` through `A2R2-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-a-2-r2.re-derivation-record.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> A2R2-AC1,A2R2-AC2,A2R2-AC3,A2R2-AC4,A2R2-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-a-2-r2.re-derivation-record.md` BEFORE the `complete` flip.
Result file `re-derivation-record.r2.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`A2R2-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and PRINT the partition with its denominator, the `not_re_derivable` count against the floor of four, and how you searched the mechanism.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-2 cut: no schedule is created or read by this cell.
comp-iam: RUN at the round-2 cut: no grant moves; the cell reads round-1 records and writes one of its own.
comp-adversary: RUN at the round-2 cut: the adversarial control is built into the arm rather than added beside it -- a2-floor requires the count to EXCEED OR EQUAL the handed list AND requires a note on how the population was searched, because the defect this cell exists to record was found by a mechanism census and would be missed by any cell working from the list of four.
lane: the <paths> block is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ is granted by the tree convention. Round-1 fixed inputs are READ-ONLY by a BOUND rather than by the absence of a grant, because the grant cannot express read-only and the order states it.
contention: the channel is written by LT-c-2 later in THIS SAME QUEUE and by LT-n-2 on slot ~2 CONCURRENTLY. That is DELIBERATE and it is this round's stated experiment. Round 6 of LGIC_ENFORCE put both cells on one queue on the rule that two worker branches appending to one channel is a guaranteed conflict, measured 3 of 3 on a sibling project's round-4 drains. But at round 6's own second drain a genuine concurrent append -- 1.0.0_SA_CTO's LGIC_ENFORCE-S70 in the shared tree against the worker's W1-S70 on its branch -- merged with NO conflict, union verified at 190 ids expected and 190 merged. HYPOTHESIS: a TEXTUAL SPLICE merges where a WHOLE-ARRAY RE-DUMP conflicts, because a splice touches only the bytes between the last row and the closing bracket. Both orders therefore MANDATE a splice and FORBID a re-dump. If the second drain conflicts anyway the hypothesis is refuted and recorded as such; n=1 is a reason to run the test with the cost bounded to one union merge, not a result.
</preflight>

Seating: slot `~1`, level 0, FIRST of a two-order queue (`LT-a-2-r2` -> `LT-c-2-r2`). Round 2 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.3 s.12, from `1.0.0_SA_CTO`'s round-1 analysis item 1 AS CORRECTED BY THE REGISTER at `last_updated 2026-09-18T06:55:00Z` -- the analysis says TWO arms, the register says FOUR citing row `S18` and `3.0.0_SA_CVO`'s confirmation @`98f7074714`, and the fresher carrier governs. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` (`check_lt_r2.py`, 11 subcommands and a 28-arm self-test with 10 positive-satisfiability arms; `R2_BASE.json` pinning `d0d4c6065f`). Rulings carried: R-43, R-47, R-40.
