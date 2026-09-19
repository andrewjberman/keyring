# TO LGIC_LGCTFM.TO-LT-e-7-r6 -- DOES ONE REPAIR RESOLVE BOTH SITES? MEASURE IT; DO NOT CONFIRM IT

<to_id>LGIC_LGCTFM.TO-LT-e-7-r6</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-e-7` (decomposition v1.7 s.17) | **outcome_ref:** FWD-1 | **depends_on:** none -- the only cell this round

---

## WORKER FACE

### THE CELL

`LT-e-7`. Round 5 measured 24 bucketless S3Key rows, attributed them to TWO code sites, and reported that
both **plausibly** trace to one upstream root -- portal-stitch leaving `arn` empty when it cannot resolve a
single firm-writer bucket. `1.0.0_SA_CTO`'s round-5 analysis (@`cf0cf68868`) cut this round to ESTABLISH
that, and named the trap in the same sentence:

> *"The record says 'plausibly', which is a hypothesis the round EARNED, not a finding; **a cell that assumes
> it will report agreement rather than measure it.**"*

⛔ **YOU ARE NOT HERE TO CONFIRM THE SHARED ROOT. You are here to find out.**

**THE HYPOTHESIS UNDER TEST, stated so you can falsify it:** *a single repair at the portal-stitch S3Key
ingestion -- making it resolve or record a firm-writer bucket rather than leaving `arn` empty -- removes BOTH
the 23 tier-prefixed and the 1 firm-prefixed bucketless rows.*

**WHAT WOULD FALSIFY IT:** any outcome where the single change resolves one class and leaves the other,
resolves neither, or resolves both only with a second change at the other site.

⭐ **WHY THE ANSWER MATTERS OPERATIONALLY, and it is the reason this round exists:** if the hypothesis is
TRUE the remedy is one change at one site. **If it is FALSE, a single-change remedy would ship a fix that
LOOKS COMPLETE AND LEAVES A CLASS BEHIND -- and the leftover class is the one nobody re-measures, because the
count moved.**

### WHAT YOU BUILD

1. **State the hypothesis and its FALSIFIER in your record, in your own words, BEFORE the experiment.** The
   arm refuses a record with no falsifier: a hypothesis with none is a conclusion waiting for evidence.
2. **Run ONE discriminating experiment.** Apply the single candidate repair **in a scratch copy outside the
   repo**, re-run the walk, and count BOTH classes before and after over the same denominator. Name the
   instrument you ran.
3. **Report the verdict: `ONE_REPAIR`, `TWO_REPAIRS` or `UNDETERMINED`, with evidence that speaks to BOTH
   classes.** ⭐ **ALL THREE PASS THE ARM.** The checker's self-test drives one positive arm per verdict, so
   you can see for yourself that the grading does not reward agreement -- and `ONE_REPAIR` is REFUSED on the
   counts if a class still carries rows after the change.
4. ⛔ **DO NOT LAND THE REPAIR.** This round establishes WHICH remedy is needed; landing it is the next
   round's cut once the shape is known. `lib/opal_lgctfm.py` has NO writer this round, and `e7-no-landed-repair`
   grades **the commits YOU authored** against it -- another seat's commit there is excused and printed.
5. **The vintage field:** `fixed_inputs_at_pin` naming `check_lt_r6.py` and `R6_BASE.json` with the commits
   you invoked them at, each resolvable against its path.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/R6_BASE.json`; this is a quotation of it)**

```json
{
  "hypothesis": {"stated": "<H, in the cell's own words>", "falsifier": "<what result would mean TWO repairs>"},
  "experiment": {"what_was_changed": "<the single candidate repair, and WHERE>", "where_it_ran": "<scratch copy outside the repo>", "instrument": "<the command run>", "before": {"tier_prefixed": 0, "firm_prefixed": 0, "denominator_s3key": 0}, "after": {"tier_prefixed": 0, "firm_prefixed": 0, "denominator_s3key": 0}},
  "verdict": {"value": "<ONE_REPAIR|TWO_REPAIRS|UNDETERMINED>", "evidence": "<what the two classes did, separately>"},
  "no_landed_repair": {"engine_commits_by_this_cell": 0},
  "fixed_inputs_at_pin": {"<path>": "<commit>"},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/ONE_REPAIR_OR_TWO_R6.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E7R6-AC1" cell_refs="LT-e-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_lt_r6.py e7-hypothesis</invocation><expect>PASS-E7-HYPOTHESIS</expect></criterion>

<criterion id="E7R6-AC2" cell_refs="LT-e-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_lt_r6.py e7-experiment</invocation><expect>PASS-E7-EXPERIMENT</expect></criterion>

<criterion id="E7R6-AC3" cell_refs="LT-e-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_lt_r6.py e7-verdict</invocation><expect>PASS-E7-VERDICT</expect></criterion>

<criterion id="E7R6-AC4" cell_refs="LT-e-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_lt_r6.py e7-no-landed-repair</invocation><expect>PASS-E7-NO-LANDED-REPAIR</expect></criterion>

<criterion id="E7R6-AC5" cell_refs="LT-e-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_lt_r6.py r6-vintage-field</invocation><expect>PASS-R6-VINTAGE-FIELD</expect></criterion>

<criterion id="E7R6-AC6" cell_refs="LT-e-7"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_lt_r6.py r6-stale-proofs</invocation><expect>PASS-R6-STALE-PROOFS</expect></criterion>

<criterion id="E7R6-AC7" cell_refs="LT-e-7" judgment="true"/>

<expected_criteria>E7R6-AC1, E7R6-AC2, E7R6-AC3, E7R6-AC4, E7R6-AC5, E7R6-AC6, E7R6-AC7</expected_criteria>

**WIRING AT THE CUT, measured by the issuer:** `AC1`, `AC2`, `AC3` and `AC5` **FAIL** (no record yet).
⚠ `AC4` and `AC6` are **GUARD-SHAPED and read PASS at the cut** -- `AC4` guards against a repair you must not
land, `AC6`'s window is empty until a fixed input moves.

**`E7R6-AC7`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the experiment actually
DISCRIMINATES -- whether the single change was applied where the hypothesis says the root is, and whether the
evidence would have looked different had the answer been the other one.

⭐ **THE BAR THESE CRITERIA WERE BUILT AGAINST:** *"can a CORRECT artifact satisfy this? Where the honest
answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* Here that bar has a specific shape worth naming:
**every verdict value is reachable**, and the self-test proves it with one positive arm each for
`ONE_REPAIR`, `TWO_REPAIRS` and `UNDETERMINED`. **A criterion that only passed on `ONE_REPAIR` would be an
instruction to confirm the hypothesis** -- exactly what the analysis forbids, and the cheapest way for this
round to produce a comfortable answer instead of a true one.

**THE CHECKER'S CONTROLS:** run `... check_lt_r6.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`.
The run PRINTS its own arm total and positive count -- do not trust a number quoted in an order, this one
included.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`lib/opal_lgctfm.py` IS NOT YOURS THIS ROUND.** Read it freely; apply the candidate repair ONLY in a
  scratch copy outside the repo, and say in the record where that was.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line
  endings exactly. Copy an existing row's field set exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured
  at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.7, round-6 cell `LT-e-7` (section 17).
<owned_cells>LT-e-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `E7R6-AC1` through `E7R6-AC7`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-7-r6.one-repair-or-two.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E7R6-AC1,E7R6-AC2,E7R6-AC3,E7R6-AC4,E7R6-AC5,E7R6-AC6,E7R6-AC7 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-e-7-r6.one-repair-or-two.md` BEFORE the `complete` flip.
Result file `one-repair-or-two.r6.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`E7R6-AC7` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the hypothesis and its falsifier as
you stated them, the single change you applied and where, the instrument you ran, both classes' counts before
and after over the same denominator, and the verdict with the evidence that decided it -- **including, in one
sentence, what you would have concluded had the other class moved instead.**

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-6 cut: no schedule is created or read.
comp-iam: RUN at the round-6 cut: no grant moves.
comp-adversary: RUN at the round-6 cut. The cheapest satisfying move here is to apply a change and report ONE_REPAIR because the headline count fell -- so the verdict arm refuses ONE_REPAIR while EITHER class still carries rows, requires the evidence to name BOTH classes, and makes TWO_REPAIRS and UNDETERMINED pass on their own evidence. The second cheapest is to skip the experiment and reason from the round-5 story, which AC2 refuses by requiring before/after counts and a named instrument.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ by the tree convention. The engine has NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies.
</preflight>

Seating: slot `~1`, level 0, the only order this round. Round 6 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on
decomposition v1.7 s.17, from `1.0.0_SA_CTO`'s round-5 analysis @`cf0cf68868`. Fixed inputs:
`deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/` (`check_lt_r6.py`, `R6_BASE.json` pinning `a9e5185bc3`).
Rulings carried: the CUT-TIME criterion bar, Rule 24's inherited-universal clause @`cf0cf68868`, ADDENDUM 3's
vintage field, W1-S39's author-scoped no-repair shape.
