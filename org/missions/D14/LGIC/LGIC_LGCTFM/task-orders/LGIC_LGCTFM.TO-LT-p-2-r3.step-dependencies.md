# TO LGIC_LGCTFM.TO-LT-p-2-r3 -- `dependencies` -> `step_dependencies`: a field named for a relation the plan does not carry

<to_id>LGIC_LGCTFM.TO-LT-p-2-r3</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-p-2` (decomposition v1.4 s.13) | **outcome_ref:** FWD-6 | **depends_on:** LGIC_LGCTFM.TO-LT-e-5-r3 -- same slot `~1`, same file (`lib/opal_lgctfm.py`, CONSTRAINT 1)

---

## WORKER FACE

### THE CELL

`LT-p-2`. Every plan package carries a field named `dependencies`. Measured at the cut on the graded 49F run:
**1074 packages, 895 populated, and every populated value is `<same row>-<previous R19 step>`** -- 895
same-row, 0 cross-row. The engine builds it that way by construction (`lib/opal_lgctfm.py`
`_build_one_package`: `"dependencies": [row_id-prior_step] if prior_step else []`).

**So the plan has a field named `dependencies`, 895 of them populated, and none of them is a dependency
between two resources.** A reader who searches a run for the word finds coverage that does not exist.
4.0.0_SA_CRO's RCN-0009 P4 proposed the rename and ruling R-79 (@`0e9027c6dc`) adopted it as OWED:
*"plan.json's `dependencies` is a READING HAZARD to fix rather than inherit"*.

### WHAT YOU BUILD

1. Rename the package field to **`step_dependencies`** everywhere the engine writes it (the field list, the
   package builder, `plan.md`'s rendering), and in `infra/logic/10_LEGACY_TRANSFORM.md` where the method note
   names it. No package carries `dependencies` after the change.
2. **The VALUES do not move.** On the same contract, every package's `step_dependencies` equals what its
   `dependencies` was, value for value.
3. **Frozen runs are not rewritten (R-43).** `p2-old-untouched` re-hashes the graded run's manifest files with
   `git hash-object`, the instrument its own `HASHES.json` names; every file must still match.
4. `resource_dependencies` (a real cross-row relation) is **NOT** this cell's -- that is FWD-6's, after FWD-1
   (R-79). Do not add an empty one: an empty field named for a relation is the same hazard in a new spelling.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="P2R3-AC1" cell_refs="LT-p-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py p2-renamed</invocation><expect>PASS-P2-RENAMED</expect></criterion>

<criterion id="P2R3-AC2" cell_refs="LT-p-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py p2-values-preserved</invocation><expect>PASS-P2-VALUES-PRESERVED</expect></criterion>

<criterion id="P2R3-AC3" cell_refs="LT-p-2"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_lt_r3.py p2-old-untouched</invocation><expect>PASS-P2-OLD-UNTOUCHED</expect></criterion>

<criterion id="P2R3-AC4" cell_refs="LT-p-2" judgment="true"/>

<expected_criteria>P2R3-AC1, P2R3-AC2, P2R3-AC3, P2R3-AC4</expected_criteria>

**AC1 and AC2 READ FAIL AT THE CUT** (1074 packages carry `dependencies`; 895 values differ because the new
field is absent). ⚠ **AC3 IS GUARD-SHAPED AND READS PASS AT THE CUT** -- it protects the frozen run and must
still read PASS after your change. Both AC1 and AC2 run the engine's `plan` verb on a SCRATCH COPY of the
graded run, never in place.

**`P2R3-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether any remaining reader of the old name
(a doc, a skill, a checker) was left pointing at a field that no longer exists.

**THE CHECKER'S CONTROLS:** run `... check_lt_r3.py selftest-arms` FIRST; expect `PASS-ARMS-DISCRIMINATE`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/` and this order's own file. Nothing else.
- **Branch.** Your worktree is created from HEAD AFTER `LT-e-5` has drained; build on its engine, never beside it. Never push, merge, rebase, `checkout --` or `clean`.
- ⛔ **NOTHING UNDER `workflows/legacy_transform/` IS WRITTEN.** The arms copy the graded run to scratch.
- ⛔ **YOU DO NOT CHANGE THE DISCOVERY, THE COVERAGE BLOCK OR THE SCHEMA** -- `LT-e-5`'s, drained before you start.
- **Surprises** by **TEXTUAL SPLICE**; never re-dump; assert the non-ASCII CHARACTER count and backslash-u count unchanged.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, re-measured at your own write time.
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<paths>
lib/opal_lgctfm.py
infra/logic/10_LEGACY_TRANSFORM.md
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.4, round-3 cell `LT-p-2` (section 13).
<owned_cells>LT-p-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `P2R3-AC1` through `P2R3-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-p-2-r3.step-dependencies.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> P2R3-AC1,P2R3-AC2,P2R3-AC3,P2R3-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-p-2-r3.step-dependencies.md` BEFORE the `complete` flip.
Result file `step-dependencies.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent.
`P2R3-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. PRINT the package count, the populated count, the values-differ count (must be 0), and every place the old name still appears in the repo with the reason it stays.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut: no schedule is created or read.
comp-iam: RUN at the round-3 cut: no grant moves; the cell reads no AWS surface.
comp-adversary: RUN at the round-3 cut: the adversarial control is p2-values-preserved. The cheapest satisfying move for p2-renamed is to emit an empty step_dependencies everywhere; the values arm compares package by package against the old field on the same contract and refuses any difference. p2-old-untouched is guard-shaped and disclosed.
lane: <paths> is the grant; deliverables/0.9.0_WK_LGIC_LGCTFM~1/ is granted by the tree convention. lib/opal_lgctfm.py has one writer at a time: this cell starts only after LT-e-5 drains.
contention: the channel is shared with slot ~2 -- append-only, 14b's inversion applies.
</preflight>

Seating: slot `~1`, level 1, second of three on the slot (after `LT-e-5`, before `LT-x-4`). Round 3 of LGIC_LGCTFM, issued by `2.0.0_SA_COO~G` on decomposition v1.4 s.13, from R-79 (d). Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/`. Rulings carried: R-79, R-43.
