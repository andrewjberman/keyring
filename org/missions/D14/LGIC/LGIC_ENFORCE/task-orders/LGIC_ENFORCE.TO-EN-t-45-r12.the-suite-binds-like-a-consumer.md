# TO LGIC_ENFORCE.TO-EN-t-45-r12 -- THE SUITE BINDS LIKE A CONSUMER: 33 of 38 tests hold a copy no substitution can reach

<to_id>LGIC_ENFORCE.TO-EN-t-45-r12</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-t-45` (decomposition v3.11 s.0l) | **outcome_ref:** FWD-3 | **depends_on:** none -- the only cell this round

---

## WORKER FACE

### THE CELL

`EN-t-45`. Round 11 proved its two new probes catch the cheapest wrong fix by **mutating the real suite**.
`1.0.0_SA_CTO`'s round-11 analysis (@`84b02d1573`) then named what that exposed, and it is sharper than the
thing it was checking:

> *"THAT IS BLINDNESS, NOT TOLERANCE -- unmutatable by construction. A test no substitution can reach cannot
> be graded by mutation AT ALL. Its green is not weak evidence about the predicate; it is NO evidence."*

**Measured by the issuer at the cut (`eda1e967d0`), re-measure it yourself:** `lib/tests/test_opal_naming.py`
has **38** test functions. **33** call `on.<attr>()` -- the module the file loads BY PATH at `:21-23` under
the private name `opal_naming_lib`. **2** resolve the shipped module at call time (`_shipped_grade()`, `:176`,
round 11's probes). The remaining 3 touch neither.

**Why that is a defect and not a style:** a substitution of the module the estate actually imports --
`sys.modules["opal_naming"]`, which is how round 11's worker installed its mutants as plugins before
collection -- **never reaches a test holding a private by-path copy.** Those 33 greens are not weak evidence
about `grade()`. They are no evidence, and nothing in the file says so.

### WHAT YOU BUILD

1. **Make the suite bind the way a CONSUMER binds.** Every test that exercises the library resolves it at
   CALL time through the shipped module, the way `_shipped_grade()` already does. The by-path loader may stay
   as the FALLBACK it already is in that helper -- what must go is a test reaching the private copy directly
   when a consumer would not.
2. **RESIDUALS ARE ALLOWED AND MUST BE NAMED.** If a test must keep the by-path copy -- one that tests the
   loader itself, say -- your record names it and says WHY, in `binding.residuals[].why_it_must_keep_the_by_path_copy`.
   An empty reason is refused. An unnamed residual is refused. **Do not convert a real exception into a
   silent one, and do not delete a test to make a count come out.**
3. **Prove it by mutation, with the mutant installed the way the ESTATE would see one** -- a plugin loading
   before collection that puts a mutated module into `sys.modules["opal_naming"]`, never an attribute patch
   on the by-path object (that mechanism would hide the very defect this cell fixes). The mutant is BLUNT by
   design: spell `blackdiamond` back to `bd` everywhere. **It must kill a named, counted set of the repaired
   tests, and that set MUST include `test_r3_bd_left_in_the_function_is_spelled_blackdiamond`** -- the
   round-10 test, which survives every substitution today.
4. **The suite's failing set must be IDENTICAL afterwards:** `2 failed, 91 passed`, the two hand-stale worked
   cases (`inf-silver-chain|LAMBDA`, `Inflection-SilverChain-DimConversionFailure|CW_ALARM`). They are out of
   scope since round 10. ⛔ **A baseline failure that DISAPPEARS fails the arm too** -- this cell changes how
   tests BIND, never what they assert.
5. **Write the note AT THE SITE**, in `lib/tests/test_opal_naming.py`: what the by-path load does, why a
   consumer-side substitution is the one that matters, and `S90` as the record. `S87`'s comment is the model
   -- the CTO ruled that comment better than his own framing because it is read by whoever opens the file.

**RECORD SHAPE (the one carrier is `deliverables/2.0.0_SA_COO~G/fixed_inputs/r12/R12_BASE.json`; this is a quotation of it)**

```json
{
  "binding": {"tests_total": 0, "reached_the_by_path_copy_before": 0, "reached_the_by_path_copy_after": 0, "residuals": [{"test": "<name>", "why_it_must_keep_the_by_path_copy": "<...>"}]},
  "mutation": {"as_shipped_pass": 0, "killed_by_the_keyed_mutant": ["<test name>"], "round10_test_killed": false},
  "suite": {"before": "<n failed, m passed>", "after": "<n failed, m passed>", "failing_ids_identical": true},
  "note": {"path": "lib/tests/test_opal_naming.py", "states_the_construction_hazard": true},
  "stale_proofs": {"fixed_input_commits_since_cut": 0, "proofs_re_run": []}
}
```

Write it to `<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/CONSUMER_BINDING_R12.json`.
⛔ **`killed_by_the_keyed_mutant` is the MEASURED set and the arm compares it to its own run** -- a name you
did not see die fails the arm, and so does a death you did not list.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="T45R12-AC1" cell_refs="EN-t-45"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r12/check_en_r12.py t45-binding</invocation><expect>PASS-T45-BINDING</expect></criterion>

<criterion id="T45R12-AC2" cell_refs="EN-t-45"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r12/check_en_r12.py t45-mutant</invocation><expect>PASS-T45-MUTANT</expect></criterion>

<criterion id="T45R12-AC3" cell_refs="EN-t-45"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r12/check_en_r12.py t45-suite</invocation><expect>PASS-T45-SUITE</expect></criterion>

<criterion id="T45R12-AC4" cell_refs="EN-t-45"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r12/check_en_r12.py t45-note</invocation><expect>PASS-T45-NOTE</expect></criterion>

<criterion id="T45R12-AC5" cell_refs="EN-t-45"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r12/check_en_r12.py t45-stale-proofs</invocation><expect>PASS-T45-STALE-PROOFS</expect></criterion>

<criterion id="T45R12-AC6" cell_refs="EN-t-45" judgment="true"/>

<expected_criteria>T45R12-AC1, T45R12-AC2, T45R12-AC3, T45R12-AC4, T45R12-AC5, T45R12-AC6</expected_criteria>

**WIRING AT THE CUT, measured by the issuer and disclosed rather than discovered by you:**
`AC1` **FAIL** (33 of 38 by-path). `AC2` **FAIL**, and read its output -- the mutant already kills **2**
tests (round 11's probes), which proves the MECHANISM reaches a consumer-bound test, while the round-10 test
SURVIVES. That contrast is the round in one line. `AC4` **FAIL** (tokens `by-path` and `S90` absent).
⚠ `AC3` and `AC5` are **GUARD-SHAPED and read PASS at the cut**: `AC3` guards against a change you should not
make, and `AC5`'s window is empty until a fixed input moves.

**`T45R12-AC6`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether the repaired binding is what a
CONSUMER actually does, or a second private path wearing a consumer's name -- and whether any residual you
named is a real exception rather than a test that was inconvenient to convert.

**THE CHECKER'S CONTROLS:** run `... check_en_r12.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`
(the run PRINTS its own arm total and its positive-satisfiability count -- do not trust a number quoted in
an order, including this one). An arm a CORRECT record cannot satisfy is a BLOCKING surprise row: **three of
those were found and repaired in the sibling project this same night, all by the worker being graded.**

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/` and this order's own file. Nothing else.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **`lib/opal_naming.py` IS NOT IN YOUR GRANT.** This cell changes how the TESTS reach the library and
  changes nothing about what it does. A test that fails because you changed the library is out of scope.
- ⛔ **DO NOT TOUCH `deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/`.** Round 11 is CLOSED, its
  `check_en_r11.py:172` still carries the `len(listed) > 0` bar S90 falsified, and the CTO's instruction is
  explicit: a census before the next cut, **never an edit to a closed round's fixed input.**
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; assert the
  non-ASCII CHARACTER count and backslash-u count unchanged. Copy an existing row's field set exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel,
  re-measured at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
lib/tests/test_opal_naming.py
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.11, round-12 cell `EN-t-45` (section 0l).
<owned_cells>EN-t-45</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `T45R12-AC1` through `T45R12-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-t-45-r12.the-suite-binds-like-a-consumer.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> T45R12-AC1,T45R12-AC2,T45R12-AC3,T45R12-AC4,T45R12-AC5,T45R12-AC6 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-t-45-r12.the-suite-binds-like-a-consumer.md` BEFORE the `complete` flip.
Result file `the-suite-binds-like-a-consumer.r12.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`T45R12-AC6` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the before/after binding counts
with their denominator, the exact set the mutant killed, the suite's failing ids before and after, and every
residual you named with its reason.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-12 cut: no schedule is created or read.
comp-iam: RUN at the round-12 cut: no grant moves; the cell reads no IAM surface.
comp-adversary: RUN at the round-12 cut: the adversarial control is the pair AC2 + AC3. The cheapest satisfying move for AC2 is to make the mutant reach the tests by weakening what they ASSERT (or by deleting the two baseline failures); AC3 refuses any change to the failing set in EITHER direction, and AC1's record/measurement comparison refuses a residual count that disagrees with the file. The blunt mutant is deliberate: a subtle one would confound reachability with round 11's question.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_ENFORCE~1/ by the tree convention. lib/opal_naming.py has NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies, the slot does not isolate there.
</preflight>

Seating: slot `~1`, level 0, the only order this round. Round 12 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G`
on decomposition v3.11 s.0l, from `1.0.0_SA_CTO`'s round-11 analysis @`84b02d1573`. Fixed inputs:
`deliverables/2.0.0_SA_COO~G/fixed_inputs/r12/` (`check_en_r12.py`, `R12_BASE.json` pinning `eda1e967d0`).
Rulings carried: S86 (closed by mutation), S87 (answered at its site), S90 and ADDENDUM 4, R-43.
