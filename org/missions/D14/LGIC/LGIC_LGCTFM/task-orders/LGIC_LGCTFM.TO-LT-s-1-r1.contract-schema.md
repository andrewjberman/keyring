# TO LGIC_LGCTFM.TO-LT-s-1-r1 -- the contract JSON schema, authored from the Rule 24 record

<to_id>LGIC_LGCTFM.TO-LT-s-1-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-s-1` (decomposition v1.1) | **outcome_ref:** FWD-1, FWD-3 | **depends_on:** none -- level 0; LT-e-1 continues on this slot

---

## WORKER FACE

### THE CELL

`LT-s-1` (PRD T1, DEC-1). **You write `org/standards/LGCTFM_CONTRACT.schema.json`** and your Rule 24 note `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/<your serial>/CONTRACT_SCHEMA_RULE24.md`.

**WHAT.** One JSON Schema (draft 2020-12) for a run's contract, authored FROM `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` -- the four-postulate record and token census are ALREADY LANDED there; the schema cites it and names no enum value the record does not name (a new one is a Rule 24 act, never a liberty of this cell).

**THE CONTRACT SHAPE THIS ROUND FIXES** (from `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` s.1-s.4; the planted example is `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/PLANTED_CONTRACT.json`): top level `schema_version`, `subject` {`kind`, `key`, `vintage` {`repo_head`, `graph_built`, `registry_hash`}}, `trigger_denominator` {`list_rules`, `list_schedules`} (each a cell), `ranking_rule` (a string), `rows[]`, `edges[]` {`from`, `to`, `type`}, `tensions[]`, `plan[]`. A CELL is `{value, status, evidence}` with `status` in MEASURED | UNMEASURED | INFERRED | NOT_MEASURABLE and `evidence` carrying at least `instrument` and `blind_spot`. A RESOURCE or PLANE row: `row_id`, `kind`, `node_type`, `subject`, `current` {`name`, `arn_or_path`, `drift_class`, `declaration`, `live`, `client_facing`, ...} and `desired` {`form`, `builder`, `verdict`, `missing_registry_row` on a RAISE}, every field a cell, plus `mark`. `desired.builder.value` is the call verbatim: `{"fn": <name|address|grade|lookup|fence_patterns|...>, "args": [...], "kwargs": {...}}`. A FORK row: `row_id`, `kind: FORK`, `subject`, `members[]` (row_ids), `one_job` and `canonical_member` (cells; the canonical member is a member row_id or `RULING-OWED`). A tension: `tension_id`, `row_id`, `axis`, `deciding_rules[]` (R-ids), `kind`, `object_count`, `factors` {`irreversible`, `client_facing`, `live`, `rules_colliding`} (cells).

What the schema must do, each measured below:
1. **Accept the planted contract** `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/PLANTED_CONTRACT.json` exactly as committed.
2. **Refuse** the same contract with (a) a bare value where a cell belongs, (b) a trigger denominator naming only one API, (c) a cell whose `evidence` has no `instrument`. The checker derives each from the planted file in memory.
3. **`$defs.node_type.enum` is the 33 node types BY SUBTRACTION** from `org/standards/NAMING_SCHEMA.json` (`kind.by_type` keys plus `types_not_graded_by_kind` keys), not a forward list.
4. **`$defs.row_kind`, `$defs.cell_status`, `$defs.axis`, `$defs.tension_kind`** each carry an `enum` equal to the record's (s.1.2, s.3, s.4). `FORK` is a row kind and never a tension kind.

**The Rule 24 note** names the uncovered member you hunted for and the cells a rename does NOT move (record s.5), citing the record rather than restating it.

**Read:** `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` (whole); `org/standards/NAMING_SCHEMA.json` (`kind.by_type`, `types_not_graded_by_kind`, `grade`); `projects/ATOM_DECOMP/skill/atomic-decomposition/references/ssot_establishment.schema.json` (`$defs.cell`); `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-1.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="S1R1-AC1" cell_refs="LT-s-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s1-valid</invocation><expect>PASS-S1-PLANTED-VALID-ACCEPTED</expect></criterion>

<criterion id="S1R1-AC2" cell_refs="LT-s-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s1-bare-value</invocation><expect>PASS-S1-BARE-VALUE-REFUSED</expect></criterion>

<criterion id="S1R1-AC3" cell_refs="LT-s-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s1-one-api</invocation><expect>PASS-S1-ONE-API-REFUSED</expect></criterion>

<criterion id="S1R1-AC4" cell_refs="LT-s-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s1-no-instrument</invocation><expect>PASS-S1-NO-INSTRUMENT-REFUSED</expect></criterion>

<criterion id="S1R1-AC5" cell_refs="LT-s-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s1-node-types</invocation><expect>PASS-S1-NODE-TYPES-BY-SUBTRACTION</expect></criterion>

<criterion id="S1R1-AC6" cell_refs="LT-s-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py s1-enums</invocation><expect>PASS-S1-ENUMS-FROM-RECORD</expect></criterion>

<criterion id="S1R1-AC7" cell_refs="LT-s-1" judgment="true"/>

<expected_criteria>S1R1-AC1, S1R1-AC2, S1R1-AC3, S1R1-AC4, S1R1-AC5, S1R1-AC6, S1R1-AC7</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **S1R1-AC7, for `3.0.0_SA_CVO` at L9 (no verdict from you):** `CONTRACT_SCHEMA_RULE24.md` names the uncovered member hunted for and the cells a rename does not move, and every schema enum value traces to a carrier the record names.

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
org/standards/LGCTFM_CONTRACT.schema.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-s-1` (sections 3 and 10).
<owned_cells>LT-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `S1R1-AC1`, `S1R1-AC2`, `S1R1-AC3`, `S1R1-AC4`, `S1R1-AC5`, `S1R1-AC6`, `S1R1-AC7`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-s-1-r1.contract-schema.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> S1R1-AC1,S1R1-AC2,S1R1-AC3,S1R1-AC4,S1R1-AC5,S1R1-AC6,S1R1-AC7 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-s-1-r1.contract-schema.md` BEFORE the `complete` flip.
Result file `contract-schema.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`S1R1-AC7` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
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

Seating: slot ~1, level 0. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
