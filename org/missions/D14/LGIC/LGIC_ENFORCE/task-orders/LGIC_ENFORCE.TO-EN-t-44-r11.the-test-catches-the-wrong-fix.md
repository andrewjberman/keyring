# TO LGIC_ENFORCE.TO-EN-t-44-r11 -- THE TEST CATCHES THE WRONG FIX, and the branch that can never be observed says so at its own site

<to_id>LGIC_ENFORCE.TO-EN-t-44-r11</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-t-44` (decomposition v3.10 s.0k) | **outcome_ref:** FWD-5 | **depends_on:** none -- the only order this round

---

## WORKER FACE

### THE CELL

`EN-t-44`. Round 10 fixed `grade()` and added one test. Row `LGIC_ENFORCE-S86` found that **the test asserts
only the census instance's own shape -- the vendor branch, firm token BEFORE the `bd`, `cot` on both sides --
so IT WOULD PASS THE VERY SUBSTITUTION `G43R10-AC5` EXISTED TO RULE OUT.** The fix generalises; the test does
not; **and the test is what outlives the round.**

`3.0.0_SA_CVO` already ran the arms that close it at L9. This is NOT new test design, and the L10 analysis
says so in terms: *"the inputs exist, the expectation is measured, the run has happened."*

**MEASURED BY THE ISSUER AT THE CUT (`ba1dcf65e9`), so nothing here is a fishing expedition:**

```
  opal-cot-session-bd-cot-fetch   SSM_DOCUMENT -> opal-cot-session-blackdiamond-fetch-document
  opal-cot-session-cot-bd-fetch   SSM_DOCUMENT -> opal-cot-session-blackdiamond-fetch-document
  (contrast, the census instance) opal-cot-bd-session-fetch -> opal-cot-blackdiamond-session-fetch-document
  tests asserting either probe today: NONE
```

Each probe differs from the census instance on the axis round 10's test cannot see: the firm token sits
AFTER the `bd` as well as before, and the `bd` sits at a token index the census instance never occupies.

### WHAT YOU BUILD

1. **PROMOTE THE PROBE.** Add the two names to `lib/tests/test_opal_naming.py` as real assertions on
   `grade()`'s canonical form.
2. **PROVE THE PROMOTION WITH THE MUTANT, which is the round.** `t44-mutant` swaps `grade()` for a KEYED
   SUBSTITUTION -- the cheapest wrong fix, which rewrites the census instance and leaves every other name's
   `bd` raw -- and calls each test that asserts a probe. **EVERY ONE OF THEM MUST FAIL against it.** A test
   that cannot fail on the defect its round was cut to fix is a green carrying no information. Write the
   assertions so that a keyed substitution breaks them; do not assert anything that is true of both.
3. **CARRY `S87` AT THE SITE.** `_r3_spell`'s FIRM branch (`v.short[v.bd_firm]`) is implemented and can never
   be observed: every path that reaches it produces a token FN1b then subtracts as a duplicate of the scope
   slot R4 filled with the same reading. ⛔ **THE BRANCH STAYS** -- removing it needs a proof the composition
   can never change, and nobody has one. Add a comment at `_r3_spell` naming (a) that the branch has no
   observable output today, (b) the R3 + FN1b composition that makes it so, and (c) `S87` as the record.
   The arm checks for `S87`, `FN1b` and `observ` in that function's own source.
4. **MOVE NOTHING ELSE.** Re-grading the round-8 census must yield the same 2 rows round 10 named, and no
   others. You are writing a test and a comment.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/R11_BASE.json`; this is a quotation of it)**

```json
{
  "probes": [{"name": "<the probe name>", "test_id": "<the test function that asserts it>", "renders": "<what grade() returned>"}],
  "mutant": {"what": "<the keyed substitution the mutant applies>", "probe_tests_that_failed": ["<test function>"]},
  "comment_site": {"function": "_r3_spell", "file": "lib/opal_naming.py", "names_S87": true},
  "census_recheck": {"rows": 0, "moved": 0},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Written to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/TEST_PROMOTION_R11.json`.

### THE SUITE'S FAILING SET IS UNCHANGED

`lib/tests/test_opal_naming.py` reads **2 failed, 89 passed** at the cut, and both failures are the
HAND-SIDE STALE worked cases the round-9 analysis refuses to count as agreement. **They must still fail: no
new failure, and neither silenced.**

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="T44R11-AC1" cell_refs="EN-t-44"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/check_en_r11.py t44-probes</invocation><expect>PASS-T44-PROBES</expect></criterion>

<criterion id="T44R11-AC2" cell_refs="EN-t-44"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/check_en_r11.py t44-mutant</invocation><expect>PASS-T44-MUTANT</expect></criterion>

<criterion id="T44R11-AC3" cell_refs="EN-t-44"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/check_en_r11.py t44-comment</invocation><expect>PASS-T44-COMMENT</expect></criterion>

<criterion id="T44R11-AC4" cell_refs="EN-t-44"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/check_en_r11.py t44-tests</invocation><expect>PASS-T44-TESTS</expect></criterion>

<criterion id="T44R11-AC5" cell_refs="EN-t-44"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/check_en_r11.py t44-stale-proofs</invocation><expect>PASS-T44-STALE-PROOFS</expect></criterion>

<criterion id="T44R11-AC6" cell_refs="EN-t-44" judgment="true"/>

<expected_criteria>T44R11-AC1, T44R11-AC2, T44R11-AC3, T44R11-AC4, T44R11-AC5, T44R11-AC6</expected_criteria>

**AC1-AC3 READ FAIL AT THE CUT** (no test asserts either probe; the comment carries 0 of 3 references).
⚠ **AC4 AND AC5 ARE GUARD-SHAPED AND READ PASS AT THE CUT** -- AC4 protects the suite's existing failing set,
AC5 is the stale-proof bar whose `git log` returns zero until a fixed input moves. Neither measures your work.

**`T44R11-AC6`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the promoted assertions would
survive a DIFFERENT wrong fix than the one the mutant applies -- the mutant is one wrong fix, not the class --
and whether the comment tells the next seat enough to stop it re-deriving S87.

**THE CHECKER'S CONTROLS:** run `... check_en_r11.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`
(15 arms, 6 positive-satisfiability). An arm a CORRECT change cannot satisfy is a BLOCKING surprise row
quoting the arm and its output -- never a workaround, never an edit to a fixed input.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **YOU DO NOT CHANGE `grade()`'s BEHAVIOUR.** Round 10's fix is graded and PASS. If a probe does not render as measured above, that is a surprise ROW, not a licence to edit the builder.
- ⛔ **YOU DO NOT REMOVE THE UNOBSERVABLE BRANCH** and you do not edit the two hand-stale tests or GRADING_RULE.md.
- ⛔ **NOTHING LIVE MOVES.** No AWS call is needed.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; assert the non-ASCII CHARACTER count and backslash-u count unchanged.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time.
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
lib/tests/test_opal_naming.py
lib/opal_naming.py
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.10, round-11 cell `EN-t-44` (section 0k).
<owned_cells>EN-t-44</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `T44R11-AC1` through `T44R11-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-t-44-r11.the-test-catches-the-wrong-fix.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> T44R11-AC1,T44R11-AC2,T44R11-AC3,T44R11-AC4,T44R11-AC5,T44R11-AC6 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-t-44-r11.the-test-catches-the-wrong-fix.md` BEFORE the `complete` flip.
Result file `the-test-catches-the-wrong-fix.r11.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`T44R11-AC6` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the two probe assertions as written, which test each lives in, the mutant's effect per probe test (must be FAIL), the comment you added, the suite's failing set before and after, and the census re-check.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-11 cut: no schedule is created or read.
comp-iam: RUN at the round-11 cut: no grant moves; the cell reads no AWS surface.
comp-adversary: RUN at the round-11 cut: the adversarial control IS t44-mutant, and it is the round. The cheapest satisfying move for t44-probes alone is two assertions that any implementation of the right shape passes; the mutant arm calls those same tests under a keyed substitution and refuses any that survive. t44-tests and t44-stale-proofs are guard-shaped and disclosed on the worker face.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ by the tree convention. lib/opal_naming.py is granted for a COMMENT at _r3_spell only -- the behaviour is graded and frozen, and t44-tests plus the census re-check would show any change.
contention: the channel is the only shared file; one order this round.
</preflight>

Seating: slot `~1`, level 0, the only order this round. Round 11 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.10 s.0k, from the L10 round analysis @`ba1dcf65e9` (S86, S87) and its stale-proof bar (S32). Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/` (`check_en_r11.py`, `R11_BASE.json` pinning `ba1dcf65e9`). Rulings carried: R-47, S85, S79, S32.
