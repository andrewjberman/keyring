# TO LGIC_LGCTFM.TO-LT-s-2-r1 -- the receiving checker's lgctfm-contract artifact type

<to_id>LGIC_LGCTFM.TO-LT-s-2-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-s-2` (decomposition v1.1) | **outcome_ref:** FWD-1, FWD-6 | **depends_on:** LT-s-1 (drained on slot ~1; the checker validates against the schema)

---

## WORKER FACE

### THE CELL

`LT-s-2` (PRD T2, DEC-11). **You edit `.tools/receiving-check.py` and write its owning tool `.tools/lgctfm-contract-check.py`.**

`receiving-check.py` is a DISPATCHER that re-implements nothing: every artifact type routes to an OWNING tool run as a subprocess (its `ROUTES` table). So:
1. **The owning tool** `python .tools/lgctfm-contract-check.py <contract.json>` exits 0 when the contract is valid and non-zero otherwise, printing one line per defect that NAMES it with one of these tokens: `bare-value` (a field where a cell belongs), `trigger-denominator` (either API missing from `trigger_denominator`), `evidence-instrument` (a cell with no `evidence.instrument`), `vintage` (a `subject.vintage` value missing), plus schema errors against `org/standards/LGCTFM_CONTRACT.schema.json`.
2. **The route**: a `ROUTES` row labelled exactly `lgctfm-contract` matching a run's `workflows/legacy_transform/<subject>/<run-id>/contract.json` AND any file ending `.lgctfm-contract.json`, handoff `L5 input (a COO lane decomposes from a run's contract)`, tool `lgctfm-contract-check.py`. Put it BEFORE any broader route that would also match. Add self-test cases for it; `--self-test` must stay green.
3. **UNCHECKED is never ACCEPT**: an artifact matching no route still reads UNCHECKED.

The checker exercises it with the planted contract `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/PLANTED_CONTRACT.json` (ACCEPT) and four doctored copies (HAND BACK, each naming its token).

**Read:** `.tools/receiving-check.py` (the docstring's design rules, `ROUTES`, `run_one`, `self_test`); `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-11 and the RECEIVING CHECKER contract row.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="S2R1-AC1" cell_refs="LT-s-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s2-accept-valid</invocation><expect>PASS-S2-VALID-ACCEPTED</expect></criterion>

<criterion id="S2R1-AC2" cell_refs="LT-s-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s2-refuse-bare</invocation><expect>PASS-S2-BARE-VALUE-HANDED-BACK</expect></criterion>

<criterion id="S2R1-AC3" cell_refs="LT-s-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s2-refuse-one-api</invocation><expect>PASS-S2-ONE-API-HANDED-BACK</expect></criterion>

<criterion id="S2R1-AC4" cell_refs="LT-s-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s2-refuse-no-instrument</invocation><expect>PASS-S2-NO-INSTRUMENT-HANDED-BACK</expect></criterion>

<criterion id="S2R1-AC5" cell_refs="LT-s-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s2-refuse-no-vintage</invocation><expect>PASS-S2-NO-VINTAGE-HANDED-BACK</expect></criterion>

<criterion id="S2R1-AC6" cell_refs="LT-s-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s2-unchecked</invocation><expect>PASS-S2-UNKNOWN-TYPE-STAYS-UNCHECKED</expect></criterion>

<criterion id="S2R1-AC7" cell_refs="LT-s-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s2-selftest</invocation><expect>PASS-S2-RECEIVING-SELFTEST-GREEN</expect></criterion>

<criterion id="S2R1-AC8" cell_refs="LT-s-2" judgment="true"/>

<expected_criteria>S2R1-AC1, S2R1-AC2, S2R1-AC3, S2R1-AC4, S2R1-AC5, S2R1-AC6, S2R1-AC7, S2R1-AC8</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **S2R1-AC8, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the owning tool re-implements no rule the schema already carries beyond the four named checks, and the new route cannot capture an artifact type another route owns.

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
.tools/receiving-check.py
.tools/lgctfm-contract-check.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-s-2` (sections 3 and 10).
<owned_cells>LT-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `S2R1-AC1`, `S2R1-AC2`, `S2R1-AC3`, `S2R1-AC4`, `S2R1-AC5`, `S2R1-AC6`, `S2R1-AC7`, `S2R1-AC8`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-s-2-r1.receiving-check.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> S2R1-AC1,S2R1-AC2,S2R1-AC3,S2R1-AC4,S2R1-AC5,S2R1-AC6,S2R1-AC7,S2R1-AC8 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-s-2-r1.receiving-check.md` BEFORE the `complete` flip.
Result file `receiving-check.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`S2R1-AC8` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: written by this cell alone in round 1.
</preflight>

Seating: slot ~3, level 1. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
