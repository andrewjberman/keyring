# TO LGIC_LGCTFM.TO-LT-v-1-r1 -- the reviewer's reproduction of the desired strings and the tension order, and the card that puts one subject's list in front of Andrew

<to_id>LGIC_LGCTFM.TO-LT-v-1-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-v-1` (decomposition v1.1) | **outcome_ref:** FWD-3, FWD-4 | **depends_on:** LT-e-3 and LT-x-1 (drained; the reviewer reproduces from a real run's rows) and LT-x-2 (same slot)

---

## WORKER FACE

### THE CELL

`LT-v-1` (PRD T13). **You write only records in your deliverables folder.** You are NOT the engine's author (slot ~1 and ~2 wrote it; you are slot ~3) -- a reproduction by the author is repetition, not corroboration.

1. **Reproduce.** From the first real run's contract (`workflows/legacy_transform/blackdiamond-49financial/<first run-id>/contract.json`), sample at least 20 rows whose `desired.builder` names `name`, `address`, `grade`, `lookup` or `fence_patterns` (all of them if fewer than 20). For each, call `lib/opal_naming.py` yourself with the row's own arguments and compare to `desired.form` (a RAISE must raise and the row must be a RAISE row). Re-derive the tension order from the four factor cells by the printed rule, independently of the engine.
2. **Record** `deliverables/<your serial>/REPRODUCTION.json`: `{"contract": <repo-relative path of that contract.json>, "results": [{"row_id", "fn", "args", "kwargs", "got", "expected", "equal"}], "order": [<tension_ids in the order you derived>]}`.
3. **The card for Andrew (FWD-4, NAMED-PERSON)** `deliverables/<your serial>/ANDREW_CARD.md`: the subject, the contract's `ranking_rule` VERBATIM, and the top ten tensions by `tension_id` with their four factor values, so he can ask "why is this above that" and be answered from the row. You cannot deliver it; the issuer carries it. Andrew's read stays APPLIED with the named actor until he has read it -- never a report standing in.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` T13 and FWD-3, FWD-4; `lib/opal_naming.py`; the first run's `contract.json`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="V1R1-AC1" cell_refs="LT-v-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py v1-reproduced</invocation><expect>PASS-V1-SAMPLE-REPRODUCED-BY-CALL</expect></criterion>

<criterion id="V1R1-AC2" cell_refs="LT-v-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py v1-order</invocation><expect>PASS-V1-REVIEWER-ORDER-EQUALS-RULE</expect></criterion>

<criterion id="V1R1-AC3" cell_refs="LT-v-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py v1-not-author</invocation><expect>PASS-V1-REVIEWER-IS-NOT-ENGINE-AUTHOR</expect></criterion>

<criterion id="V1R1-AC4" cell_refs="LT-v-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py v1-card</invocation><expect>PASS-V1-ANDREW-CARD-CARRIES-RULE</expect></criterion>

<criterion id="V1R1-AC5" cell_refs="LT-v-1" judgment="true"/>

<expected_criteria>V1R1-AC1, V1R1-AC2, V1R1-AC3, V1R1-AC4, V1R1-AC5</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **V1R1-AC5, for `3.0.0_SA_CVO` at L9 (no verdict from you):** FWD-3: the sample spans the builder kinds present rather than the easiest rows; FWD-4 (NAMED-PERSON): Andrew's read of the card is recorded with his question and the factors that answered it -- APPLIED with the named actor until then.

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
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-v-1` (sections 3 and 10).
<owned_cells>LT-v-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `V1R1-AC1`, `V1R1-AC2`, `V1R1-AC3`, `V1R1-AC4`, `V1R1-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-v-1-r1.reviewer-reproduction.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> V1R1-AC1,V1R1-AC2,V1R1-AC3,V1R1-AC4,V1R1-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-v-1-r1.reviewer-reproduction.md` BEFORE the `complete` flip.
Result file `reviewer-reproduction.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`V1R1-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: writes only this slot's deliverables folder.
</preflight>

Seating: slot ~3, level 6. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
