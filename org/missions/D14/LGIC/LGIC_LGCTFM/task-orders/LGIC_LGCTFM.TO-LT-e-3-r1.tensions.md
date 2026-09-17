# TO LGIC_LGCTFM.TO-LT-e-3-r1 -- the tensions -- typed on a closed set, four measured factors, the ranking rule printed

<to_id>LGIC_LGCTFM.TO-LT-e-3-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-e-3` (decomposition v1.1) | **outcome_ref:** FWD-4 | **depends_on:** LT-e-2 (same slot; a tension is a disagreement between current and desired)

---

## WORKER FACE

### THE CELL

`LT-e-3` (PRD T5, DEC-6). **You edit `lib/opal_lgctfm.py`.**

**THE CONTRACT SHAPE THIS ROUND FIXES** (from `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` s.1-s.4; the planted example is `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/PLANTED_CONTRACT.json`): top level `schema_version`, `subject` {`kind`, `key`, `vintage` {`repo_head`, `graph_built`, `registry_hash`}}, `trigger_denominator` {`list_rules`, `list_schedules`} (each a cell), `ranking_rule` (a string), `rows[]`, `edges[]` {`from`, `to`, `type`}, `tensions[]`, `plan[]`. A CELL is `{value, status, evidence}` with `status` in MEASURED | UNMEASURED | INFERRED | NOT_MEASURABLE and `evidence` carrying at least `instrument` and `blind_spot`. A RESOURCE or PLANE row: `row_id`, `kind`, `node_type`, `subject`, `current` {`name`, `arn_or_path`, `drift_class`, `declaration`, `live`, `client_facing`, ...} and `desired` {`form`, `builder`, `verdict`, `missing_registry_row` on a RAISE}, every field a cell, plus `mark`. `desired.builder.value` is the call verbatim: `{"fn": <name|address|grade|lookup|fence_patterns|...>, "args": [...], "kwargs": {...}}`. A FORK row: `row_id`, `kind: FORK`, `subject`, `members[]` (row_ids), `one_job` and `canonical_member` (cells; the canonical member is a member row_id or `RULING-OWED`). A tension: `tension_id`, `row_id`, `axis`, `deciding_rules[]` (R-ids), `kind`, `object_count`, `factors` {`irreversible`, `client_facing`, `live`, `rules_colliding`} (cells).

**A TENSION** is one row's halves disagreeing, typed on a closed set: `axis` in A1..A5 | PROCESS | IDENTITY; `deciding_rules[]` the R-ids the desired half's refusal names; `kind` in HOME | FORMAT | GRAMMAR | COMPUTE | DECLARATION | PROCESS | IDENTITY (record s.4; FORK is never a tension kind). **Four factor cells, each MEASURED with its instrument:** `live` from LastModified against `lib/trading_calendar.py`'s frontier (never a calendar day -- its instrument names `trading_calendar`); `client_facing` from `infra/logic/07_ROUTING_REDERIVATION.md` or `LEGACY_SERVED_PATHS.json` (its instrument names one of them); `rules_colliding` from the R-id count; `irreversible` from the canon's own word.

**THE RANKING RULE is printed** as the contract's `ranking_rule` string, naming in this order `irreversible`, `client_facing`, `live`, `rules_colliding` and the `object` count tiebreak (record s.4; `infra/logic/08_TENSION_MAP.md` s.0). **The tensions array is emitted in exactly that order**: sort key `(not irreversible, not client_facing, not live, -rules_colliding, -object_count)`, each boolean read as the cell's value's truthiness. No weighting.

**A resource no type fits** is returned, never silently graded: plant one, record it as `walk/PLANT_UNTYPEABLE.json` `{"name": ...}`; its row carries `desired.verdict = NOT_COVERED` and no tension names it.

**THE GRADED RUN:** re-run the walk into `deliverables/<your serial>/walk/`.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-6; `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` s.4; `infra/logic/08_TENSION_MAP.md` s.0; `lib/trading_calendar.py`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E3R1-AC1" cell_refs="LT-e-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e3-rule</invocation><expect>PASS-E3-RANKING-RULE-PRINTED</expect></criterion>

<criterion id="E3R1-AC2" cell_refs="LT-e-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e3-factors</invocation><expect>PASS-E3-FOUR-FACTORS-MEASURED</expect></criterion>

<criterion id="E3R1-AC3" cell_refs="LT-e-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e3-order</invocation><expect>PASS-E3-ORDER-REPRODUCED-FROM-CELLS</expect></criterion>

<criterion id="E3R1-AC4" cell_refs="LT-e-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e3-types</invocation><expect>PASS-E3-TENSION-TYPES-CLOSED</expect></criterion>

<criterion id="E3R1-AC5" cell_refs="LT-e-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e3-untypeable</invocation><expect>PASS-E3-UNTYPEABLE-RETURNED-NOT-GRADED</expect></criterion>

<criterion id="E3R1-AC6" cell_refs="LT-e-3" judgment="true"/>

<expected_criteria>E3R1-AC1, E3R1-AC2, E3R1-AC3, E3R1-AC4, E3R1-AC5, E3R1-AC6</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **E3R1-AC6, for `3.0.0_SA_CVO` at L9 (no verdict from you):** each factor cell's value is what its named instrument returns for that row (sampled), and `irreversible` is read from the canon's own words rather than asserted.

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
lib/opal_lgctfm.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-e-3` (sections 3 and 10).
<owned_cells>LT-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `E3R1-AC1`, `E3R1-AC2`, `E3R1-AC3`, `E3R1-AC4`, `E3R1-AC5`, `E3R1-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-3-r1.tensions.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E3R1-AC1,E3R1-AC2,E3R1-AC3,E3R1-AC4,E3R1-AC5,E3R1-AC6 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-e-3-r1.tensions.md` BEFORE the `complete` flip.
Result file `tensions.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`E3R1-AC6` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: lib/opal_lgctfm.py: four sequenced writers (decomposition v1.1 s.10).
</preflight>

Seating: slot ~1, level 3. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
