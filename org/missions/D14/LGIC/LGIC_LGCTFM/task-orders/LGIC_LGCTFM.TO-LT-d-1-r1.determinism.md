# TO LGIC_LGCTFM.TO-LT-d-1-r1 -- determinism -- the negative arm fired first, then the positive

<to_id>LGIC_LGCTFM.TO-LT-d-1-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-d-1` (decomposition v1.1) | **outcome_ref:** FWD-9 | **depends_on:** LT-e-2 (drained on slot ~1; determinism is measured on an engine that produces something) and LT-r-1 (same slot)

---

## WORKER FACE

### THE CELL

`LT-d-1` (PRD T9, DEC-10). **You write `lib/tests/test_opal_lgctfm.py`**, and records in your deliverables folder.

1. **Negative arm FIRST.** Make a deliberately DE-SORTED copy of the engine -- remove the sort at one set's build site -- and commit it as `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/<your serial>/desorted/opal_lgctfm_desorted.py` (never in `lib/`, never replacing the engine). Show that two of its runs on one pinned input produce DIFFERENT files. If one de-sort does not change the output, the sort you removed was not load-bearing -- remove another and say which in the result file.
2. **Positive arm, recorded AFTER the negative.** Two runs of the real engine on the same pinned input produce byte-identical files.
3. **Record** `deliverables/<your serial>/DETERMINISM.json`: `{"negative_arm": {"copy_path": <the committed copy's repo-relative path>, "outputs_differ": true, "recorded_utc": <ISO>}, "positive_arm": {"identical": true, "recorded_utc": <ISO, later than the negative's>}}`.
4. **The suite** `lib/tests/test_opal_lgctfm.py` runs both arms on a small pinned offline input you build under the test (no AWS call inside the suite), and passes. A determinism test whose negative arm cannot fail is a constant.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-10; `lib/opal_lgctfm.py`; `lib/tests/test_opal_naming.py` (the house test style).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="D1R1-AC1" cell_refs="LT-d-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py d1-pytest</invocation><expect>PASS-D1-DETERMINISM-SUITE-PASSES</expect></criterion>

<criterion id="D1R1-AC2" cell_refs="LT-d-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py d1-negative-first</invocation><expect>PASS-D1-NEGATIVE-ARM-FIRED-FIRST</expect></criterion>

<criterion id="D1R1-AC3" cell_refs="LT-d-1" judgment="true"/>

<expected_criteria>D1R1-AC1, D1R1-AC2, D1R1-AC3</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **D1R1-AC3, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the removed sort is at a real build site whose order reaches the output, and the pinned input is one the engine genuinely walks rather than a stub that bypasses the walk.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array in the file, id `LGIC_LGCTFM-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest `LGIC_LGCTFM-W<n>-S` id already present in ANY document under `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/`). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves (DEC-13).** Every instrument you call is read-only against AWS; the portal is read, never written. No Terraform apply, no AWS write, no deploy, no rename of a live resource.
- **Disk on this box is tight.** Keep scratch small; delete any temporary worktree you create before you report.

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
lib/tests/test_opal_lgctfm.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-d-1` (sections 3 and 10).
<owned_cells>LT-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `D1R1-AC1`, `D1R1-AC2`, `D1R1-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-d-1-r1.determinism.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> D1R1-AC1,D1R1-AC2,D1R1-AC3 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-d-1-r1.determinism.md` BEFORE the `complete` flip.
Result file `determinism.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`D1R1-AC3` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: lib/tests/test_opal_lgctfm.py is written by this cell alone; lib/opal_lgctfm.py is READ here while slot ~1's LT-e-3 may still be editing it -- run the arms against the engine at your own branch tip and cite that commit.
</preflight>

Seating: slot ~3, level 3. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
