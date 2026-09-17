# TO LGIC_LGCTFM.TO-LT-e-2-r1 -- the DESIRED half from the builders, and the fork test by the twin

<to_id>LGIC_LGCTFM.TO-LT-e-2-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-e-2` (decomposition v1.1) | **outcome_ref:** FWD-2, FWD-3 | **depends_on:** LT-e-1 (same slot; the desired half is computed FOR the current rows)

---

## WORKER FACE

### THE CELL

`LT-e-2` (PRD T4, DEC-4, DEC-5). **You edit `lib/opal_lgctfm.py`.**

**THE CONTRACT SHAPE THIS ROUND FIXES** (from `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` s.1-s.4; the planted example is `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/PLANTED_CONTRACT.json`): top level `schema_version`, `subject` {`kind`, `key`, `vintage` {`repo_head`, `graph_built`, `registry_hash`}}, `trigger_denominator` {`list_rules`, `list_schedules`} (each a cell), `ranking_rule` (a string), `rows[]`, `edges[]` {`from`, `to`, `type`}, `tensions[]`, `plan[]`. A CELL is `{value, status, evidence}` with `status` in MEASURED | UNMEASURED | INFERRED | NOT_MEASURABLE and `evidence` carrying at least `instrument` and `blind_spot`. A RESOURCE or PLANE row: `row_id`, `kind`, `node_type`, `subject`, `current` {`name`, `arn_or_path`, `drift_class`, `declaration`, `live`, `client_facing`, ...} and `desired` {`form`, `builder`, `verdict`, `missing_registry_row` on a RAISE}, every field a cell, plus `mark`. `desired.builder.value` is the call verbatim: `{"fn": <name|address|grade|lookup|fence_patterns|...>, "args": [...], "kwargs": {...}}`. A FORK row: `row_id`, `kind: FORK`, `subject`, `members[]` (row_ids), `one_job` and `canonical_member` (cells; the canonical member is a member row_id or `RULING-OWED`). A tension: `tension_id`, `row_id`, `axis`, `deciding_rules[]` (R-ids), `kind`, `object_count`, `factors` {`irreversible`, `client_facing`, `live`, `rules_colliding`} (cells).

**THE DESIRED HALF (DEC-4)** is the builders' output at the run's vintage and nothing else: `lib/opal_naming.py` `address()` for a key, `name()` for a resource name, the bucket grammar for a bucket, `grade()` for the verdict; the run stamps `registry_hash()`. Every `desired.builder` cell carries the call verbatim so anyone can re-make it. **A builder that RAISES is a RAISE row** (`desired.verdict = RAISE`, `desired.missing_registry_row` naming the row Rule 30 requires) -- never graded OUT-OF-PATTERN on a placeholder. A builder gap is a finding for LGIC_ENFORCE (a row), never patched in `lib/opal_naming.py`.

**THE FORK TEST (DEC-5):** a fork is two current rows whose DESIRED form is ONE string, found from the desired twin, never from name patterns. The FORK row names its members, the one job and the canonical member (the conformant one; else the ledger's disposition; else `RULING-OWED`).

**TWO GRADED RUNS.** (1) Re-run the walk into `deliverables/<your serial>/walk/` so its contract carries the desired half. (2) A forks run into `deliverables/<your serial>/forks/`, seeded with the buckets or prefixes that hold the members of `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/FORK_CONTROLS.json` -- record the seeds in `forks/SEEDS.json`. The seeds are storage locations, never the pairs: the engine must FIND the four positive forks and must NOT join the SmartX negative pair. Plant a name whose system has no registry row so a RAISE row exists.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-4, DEC-5; `lib/opal_naming.py` (`name`, `address`, `grade`, `registry_hash`); `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/FORK_CONTROLS.json` (read-only; it is the grader's list, not your input).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E2R1-AC1" cell_refs="LT-e-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e2-reproduce</invocation><expect>PASS-E2-DESIRED-EQUALS-BUILDER</expect></criterion>

<criterion id="E2R1-AC2" cell_refs="LT-e-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e2-forks</invocation><expect>PASS-E2-POSITIVE-FORKS-FOUND</expect></criterion>

<criterion id="E2R1-AC3" cell_refs="LT-e-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e2-negative</invocation><expect>PASS-E2-SMARTX-PAIR-NOT-A-FORK</expect></criterion>

<criterion id="E2R1-AC4" cell_refs="LT-e-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e2-raise</invocation><expect>PASS-E2-RAISE-ROW-NAMES-MISSING-ROW</expect></criterion>

<criterion id="E2R1-AC5" cell_refs="LT-e-2" judgment="true"/>

<expected_criteria>E2R1-AC1, E2R1-AC2, E2R1-AC3, E2R1-AC4, E2R1-AC5</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **E2R1-AC5, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the forks run's seeds name storage locations and not the control pairs, and each canonical member follows DEC-5's order (conformant, ledger disposition, RULING-OWED).

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
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-e-2` (sections 3 and 10).
<owned_cells>LT-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `E2R1-AC1`, `E2R1-AC2`, `E2R1-AC3`, `E2R1-AC4`, `E2R1-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-e-2-r1.desired-and-forks.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E2R1-AC1,E2R1-AC2,E2R1-AC3,E2R1-AC4,E2R1-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-e-2-r1.desired-and-forks.md` BEFORE the `complete` flip.
Result file `desired-and-forks.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`E2R1-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: lib/opal_lgctfm.py: four sequenced writers (decomposition v1.1 s.10). lib/opal_naming.py is READ here and edited by LGIC_ENFORCE round 3's EN-g-9, which drains before this cell starts.
</preflight>

Seating: slot ~1, level 2. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
