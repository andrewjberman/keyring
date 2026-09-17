# TO LGIC_LGCTFM.TO-LT-e-1-r1 -- the walk -- the CURRENT half, every row with its instrument and blind spot

<to_id>LGIC_LGCTFM.TO-LT-e-1-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-e-1` (decomposition v1.1) | **outcome_ref:** FWD-1 | **depends_on:** LT-s-1 (same slot; the walk emits rows shaped by the schema)

---

## WORKER FACE

### THE CELL

`LT-e-1` (PRD T3, DEC-2, DEC-3, DEC-14). **You write `lib/opal_lgctfm.py` (the engine), `infra/logic/10_LEGACY_TRANSFORM.md` (the method) and `.claude/skills/lgctfm/SKILL.md` (the one invocation).**

**THE CONTRACT SHAPE THIS ROUND FIXES** (from `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` s.1-s.4; the planted example is `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/PLANTED_CONTRACT.json`): top level `schema_version`, `subject` {`kind`, `key`, `vintage` {`repo_head`, `graph_built`, `registry_hash`}}, `trigger_denominator` {`list_rules`, `list_schedules`} (each a cell), `ranking_rule` (a string), `rows[]`, `edges[]` {`from`, `to`, `type`}, `tensions[]`, `plan[]`. A CELL is `{value, status, evidence}` with `status` in MEASURED | UNMEASURED | INFERRED | NOT_MEASURABLE and `evidence` carrying at least `instrument` and `blind_spot`. A RESOURCE or PLANE row: `row_id`, `kind`, `node_type`, `subject`, `current` {`name`, `arn_or_path`, `drift_class`, `declaration`, `live`, `client_facing`, ...} and `desired` {`form`, `builder`, `verdict`, `missing_registry_row` on a RAISE}, every field a cell, plus `mark`. `desired.builder.value` is the call verbatim: `{"fn": <name|address|grade|lookup|fence_patterns|...>, "args": [...], "kwargs": {...}}`. A FORK row: `row_id`, `kind: FORK`, `subject`, `members[]` (row_ids), `one_job` and `canonical_member` (cells; the canonical member is a member row_id or `RULING-OWED`). A tension: `tension_id`, `row_id`, `axis`, `deciding_rules[]` (R-ids), `kind`, `object_count`, `factors` {`irreversible`, `client_facing`, `live`, `rules_colliding`} (cells).

**THE INTERFACE:** `python lib/opal_lgctfm.py walk --subject <registry key> --seed <bucket> [--seed <bucket> ...] --out <dir>` writes `<dir>/contract.json` (the CURRENT half; `desired` may be absent until LT-e-2). Standard library only (plus modules in `lib/`), ASCII only.

**THE WALK ORDER, fixed by DEC-3:** the ledger's plane rows for the subject (the seed, `infra/logic/06_CONFORMANCE_LEDGER.md`) -> the buckets and prefixes they name -> every trigger naming them, through `comp-trigger` (`org/modules/graph/comp_trigger.py`), BOTH `list-rules` and `list-schedules`, each denominator printed into `trigger_denominator` -> every compute the triggers fire -> the roles, policies, instance profiles and secrets they carry -> queues, topics, alarms, log groups -> the two declared planes' rows (`infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/ec2/EC2_MANIFEST.json`) -> the Terraform files declaring any of them -> the served routes reading any of them. **Each row's cells name the instrument that produced them and that instrument's blind spot (DEC-14).** `pipescript` is banned and never called. A resource no instrument can see is an UNMEASURED row, never a missing row.

**THE GRADED RUN.** Walk the first subject's hand-built control: `--subject 49financial --seed opal-data-bd --seed opal-data-inf --seed opal-data-cot --out org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/<your serial>/walk`. The control is `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/SUBJECT_CONTROL.json` -- you are graded AGAINST it and must not feed it to the engine. **Plant** one resource outside every instrument's scope, record it as `walk/PLANT.json` `{"name": ..., "why_outside_every_instrument": ...}`, and show it surfaces as a row with an UNMEASURED current cell.

**THE METHOD DOCUMENT** carries a heading for each of: walk order, fork test, twin, tension, plan, mark, coverage hole -- beside the canon, citing it. **THE SKILL** has frontmatter `name: lgctfm` and invokes `lib/opal_lgctfm.py`.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-2, DEC-3, DEC-14; `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md`; `org/modules/graph/comp_trigger.py` (its CLI); `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/SUBJECT_CONTROL.json`; `workflows/atom_decomposition/README.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E1R1-AC1" cell_refs="LT-e-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-control</invocation><expect>PASS-E1-CONTROL-MEMBERS-WALKED</expect></criterion>

<criterion id="E1R1-AC2" cell_refs="LT-e-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-triggers</invocation><expect>PASS-E1-BOTH-TRIGGER-APIS-COUNTED</expect></criterion>

<criterion id="E1R1-AC3" cell_refs="LT-e-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-cells</invocation><expect>PASS-E1-EVERY-CELL-NAMES-ITS-INSTRUMENT</expect></criterion>

<criterion id="E1R1-AC4" cell_refs="LT-e-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-plant</invocation><expect>PASS-E1-PLANT-SURFACES-UNMEASURED</expect></criterion>

<criterion id="E1R1-AC5" cell_refs="LT-e-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-method</invocation><expect>PASS-E1-METHOD-DOCUMENT-SECTIONED</expect></criterion>

<criterion id="E1R1-AC6" cell_refs="LT-e-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-skill</invocation><expect>PASS-E1-SKILL-INVOKES-ENGINE</expect></criterion>

<criterion id="E1R1-AC7" cell_refs="LT-e-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-stdlib</invocation><expect>PASS-E1-ENGINE-STDLIB-ONLY</expect></criterion>

<criterion id="E1R1-AC8" cell_refs="LT-e-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-ascii</invocation><expect>PASS-E1-ENGINE-ASCII-ONLY</expect></criterion>

<criterion id="E1R1-AC9" cell_refs="LT-e-1" judgment="true"/>

<expected_criteria>E1R1-AC1, E1R1-AC2, E1R1-AC3, E1R1-AC4, E1R1-AC5, E1R1-AC6, E1R1-AC7, E1R1-AC8, E1R1-AC9</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **E1R1-AC9, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the walk follows DEC-3's order, each row's declared blind spot is true of its instrument, and the plant is genuinely outside every instrument's scope rather than hidden from one.

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
infra/logic/10_LEGACY_TRANSFORM.md
.claude/skills/lgctfm/SKILL.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-e-1` (sections 3 and 10).
<owned_cells>LT-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `E1R1-AC1`, `E1R1-AC2`, `E1R1-AC3`, `E1R1-AC4`, `E1R1-AC5`, `E1R1-AC6`, `E1R1-AC7`, `E1R1-AC8`, `E1R1-AC9`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-1-r1.walk.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E1R1-AC1,E1R1-AC2,E1R1-AC3,E1R1-AC4,E1R1-AC5,E1R1-AC6,E1R1-AC7,E1R1-AC8,E1R1-AC9 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-e-1-r1.walk.md` BEFORE the `complete` flip.
Result file `walk.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`E1R1-AC9` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-1 cut: the walk READS both trigger APIs through comp-trigger (read-only); it creates no schedule.
comp-iam: RUN at the round-1 cut: the walk READS roles and policies through comp-iam (read-only); it grants and changes nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: lib/opal_lgctfm.py has four writers in round 1 (LT-e-1, LT-e-2, LT-e-3 on slot ~1, then LT-p-1 on slot ~2), strictly sequenced by the decomposition's edges; decomposition v1.1 s.10.
</preflight>

Seating: slot ~1, level 1. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
