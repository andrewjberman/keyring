# TO LGIC_LGCTFM.TO-LT-e-4-r1 -- the untypeable plant becomes OPT-IN, and an ungraded node is CARRIED and COUNTED

<to_id>LGIC_LGCTFM.TO-LT-e-4-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-e-4` (decomposition v1.2, section 11) | **outcome_ref:** FWD-1, FWD-4 | **depends_on:** LT-p-1 (the `run` verb, drained on this slot) and LT-e-3 (the plant this cell makes opt-in, drained on slot ~1)

---

## WORKER FACE

### THE CELL

`LT-e-4`, round 1's AMENDMENT, on `1.0.0_SA_CTO`'s RULING **R-36** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md`). **You edit `lib/opal_lgctfm.py` and you produce TWO REAL RUNS.**

**WHY, measured -- and neither drained cell was wrong.** `org/standards/LGCTFM_CONTRACT.schema.json`'s `$defs.node_type.enum` holds 33 values and they are EXACTLY `org/standards/NAMING_SCHEMA.json`'s `kind.by_type` plus `types_not_graded_by_kind`, which `LT-s-1`'s order required BY SUBTRACTION. `LT-e-3`'s untypeable plant emits a row whose `node_type` is `COGNITO_USER_POOL`, in neither list, and the plant is UNCONDITIONAL in `cmd_walk()` -- so every contract this engine writes, for any subject, fails schema validation on that one row. That single row is all of `LT-x-1`'s `X1R1-AC1` FAIL. Row `LGIC_LGCTFM-W2-S2`. R-36 keeps the enum equality (it is what lets the contract say a type is ungraded at all) and moves the plant behind a flag.

**FOUR THINGS, and R-36's words govern where this face and the ruling differ:**

1. **`--plant-untypeable`, OFF by default.** `cmd_walk()` plants the untypeable resource only when the flag is passed. With the flag absent, a real run's `contract.json` validates. The `run` verb passes the flag through, so a run can be assembled either way.
2. **LT-e-3's path stays exercised DELIBERATELY.** The untypeable path is not deleted and not left to chance: your flag-on run is what exercises it, and criterion `E4R1-AC5` grades `LT-e-3`'s own check against that run. `LT-e-3` is DRAINED and is NOT reopened -- this cell owns the invocation change, and you do not edit that order.
3. **CARRY AND COUNT.** A node whose type `NAMING_SCHEMA.json` does not grade is **NOT written into `contract.json`'s `rows`** and is **NOT discarded**: it is carried in the run's own `PLANT_UNTYPEABLE.json` with verdict `NOT_COVERED`, and its **COUNT is printed in the contract**. The carrier's shape is `{"untypeable": [{"name", "node_type", "verdict": "NOT_COVERED", ...}], "count": <int>}`; the contract's `untypeable` property is a `$defs/cell` -- `{"value": <int>, "status": ..., "evidence": {"instrument", "blind_spot"}}` -- and **the count prints even at ZERO**. A printed zero is a measurement; an absent one is silence.
4. **RE-RUN `LT-x-1`'s `X1R1-AC1`** on a real run. `LT-x-1`'s order is `pending` at HEAD; **you do not touch it.** You re-run `x1-run-dir` as criterion `E4R1-AC6`; the ISSUER re-opens and flips `LT-x-1` at this cell's drain.

**ALREADY LANDED BY THE ISSUER at your base, so every criterion below is satisfiable inside your `<paths>`:** the schema carries `untypeable` as a REQUIRED cell property (`$defs.node_type` untouched); `PLANTED_CONTRACT.json` carries that cell at `value: 0`; and `check_lt_r1.py` carries the five `a4-*` arms plus a `core_untypeable` that grades either carrier shape. **You do not edit the schema, the planted contract or the checker** -- all three are fixed inputs.

**YOUR TWO RUNS, and the record that names them.** Produce a DEFAULT-OFF run and a FLAG-ON run with the `run` verb, then write `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/AMENDMENT_RUNS.json`:
```
{"default_off": "<repo-relative run directory>", "flag_on": "<repo-relative run directory>"}
```
Both directories are real run directories under `workflows/legacy_transform/<subject>/<UTC stamp>-<short head>/`. **R-35 landed this session** (`.tools/naming-gate.py` @5fd4251792): a measured run artifact inside a run directory is a RECORD and the naming gate no longer refuses it, so **a committed run is possible now and was not before** -- that is what row `LGIC_LGCTFM-W2-S1` blocked. The exemption is the run DIRECTORY only: engine code and anything one level up is still graded, so never put a hand-authored file in there to dodge the gate.

**Read:** `lib/opal_lgctfm.py` (`cmd_walk`, `desired_cells`, `_type_uncovered`, `cmd_run`); R-36 in the rulings file; `org/standards/LGCTFM_CONTRACT.schema.json` (`$defs.cell`, the `untypeable` property); the two rows `LGIC_LGCTFM-W2-S1` and `LGIC_LGCTFM-W2-S2` in this project's `surprise-channel/investigations/INVESTIGATION_v1.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E4R1-AC1" cell_refs="LT-e-4"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py a4-plant-off</invocation><expect>PASS-A4-PLANT-OFF-BY-DEFAULT</expect></criterion>

<criterion id="E4R1-AC2" cell_refs="LT-e-4"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py a4-flag-on</invocation><expect>PASS-A4-FLAG-ON-CARRIES-AND-COUNTS</expect></criterion>

<criterion id="E4R1-AC3" cell_refs="LT-e-4"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py a4-count-typed</invocation><expect>PASS-A4-COUNT-IS-A-TYPED-CELL</expect></criterion>

<criterion id="E4R1-AC4" cell_refs="LT-e-4"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py a4-schema-valid</invocation><expect>PASS-A4-BOTH-RUNS-SCHEMA-VALID</expect></criterion>

<criterion id="E4R1-AC5" cell_refs="LT-e-4"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py a4-e3-exercised</invocation><expect>PASS-A4-E3-PATH-STILL-EXERCISED</expect></criterion>

<criterion id="E4R1-AC6" cell_refs="LT-e-4"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x1-run-dir</invocation><expect>PASS-X1-RUN-DIRECTORY-COMPLETE</expect></criterion>

<criterion id="E4R1-AC7" cell_refs="LT-e-4"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py e1-stdlib</invocation><expect>PASS-E1-ENGINE-STDLIB-ONLY</expect></criterion>

<criterion id="E4R1-AC8" cell_refs="LT-e-4"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py d1-pytest</invocation><expect>PASS-D1-DETERMINISM-SUITE-PASSES</expect></criterion>

<criterion id="E4R1-AC9" cell_refs="LT-e-4" judgment="true"/>

<expected_criteria>E4R1-AC1, E4R1-AC2, E4R1-AC3, E4R1-AC4, E4R1-AC5, E4R1-AC6, E4R1-AC7, E4R1-AC8, E4R1-AC9</expected_criteria>

**AC1-AC6 read RED at the cut**, measured by the issuer: AC1-AC5 because `AMENDMENT_RUNS.json` does not exist yet, AC6 because `x1-run-dir` still reads `FAIL-X1-RUN-DIRECTORY-COMPLETE` on the schema error this cell removes. **AC7 and AC8 read PASS at the cut and must STILL pass** -- they are the regression arms on an engine edit: the engine stays standard-library-only, and the determinism suite (whose negative arm fires FIRST on a de-sorted copy) still passes under two hash seeds. **E4R1-AC9, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the flag's default is genuinely OFF rather than defaulted-on-with-a-name, the carried entry's evidence names a real instrument and a true blind spot, and the count in the contract equals what the carrier holds for a reason a reader can check.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/`, AND `org/standards/LGCTFM_CONTRACT.schema.json` (`LT-s-1`'s drained deliverable, already carrying the field you populate). If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Do not reopen or edit another cell's order**, in particular `LGIC_LGCTFM.TO-LT-x-1-r1` and `LGIC_LGCTFM.TO-LT-e-3-r1`. The issuer re-opens and flips `LT-x-1` at this cell's drain.
- **Do not edit rows `LGIC_LGCTFM-W2-S1` or `LGIC_LGCTFM-W2-S2`** -- both are the issuer's to disarm. You may cite them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array in the file with every existing row's indentation kept byte-for-byte, id `LGIC_LGCTFM-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest such id in ANY document under that channel). Never re-serialize the whole array. Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifacts, then run every criterion, then write the proof instance.
- **Nothing live moves (DEC-13).** Every instrument is read-only against AWS (the `.tools/aws` shim, `comp-trigger`); never `pipescript`. No Terraform apply, no AWS write, no deploy, no rename of a live resource.
- **The naming gate ENFORCES.** Never hand-type a firm token where a registry value or the run's own `--subject` key can be read; an `LT-e-3` commit was refused this session for exactly that.

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
lib/opal_lgctfm.py
workflows/legacy_transform/blackdiamond-49financial/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.2, round-1 amendment cell `LT-e-4` (section 11).
<owned_cells>LT-e-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `E4R1-AC1`, `E4R1-AC2`, `E4R1-AC3`, `E4R1-AC4`, `E4R1-AC5`, `E4R1-AC6`, `E4R1-AC7`, `E4R1-AC8`, `E4R1-AC9`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-e-4-r1.untypeable-opt-in.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E4R1-AC1,E4R1-AC2,E4R1-AC3,E4R1-AC4,E4R1-AC5,E4R1-AC6,E4R1-AC7,E4R1-AC8,E4R1-AC9 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-e-4-r1.untypeable-opt-in.md` BEFORE the `complete` flip.
Result file `untypeable-opt-in.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`E4R1-AC9` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and run records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed; every AWS read is read-only.
comp-adversary: RUN -- denominator 2 carriers of the contradiction this cell closes (org/standards/LGCTFM_CONTRACT.schema.json $defs.node_type.enum, 33 values; lib/opal_lgctfm.py cmd_walk's unconditional plant), both read at the cut by the issuer; blind spot: the enum equality was re-measured against NAMING_SCHEMA.json at this vintage only, so a later schema bump moves it without moving this cell's text.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: lib/opal_lgctfm.py: FIVE sequenced writers across round 1 (decomposition v1.2 s.11); this cell is the last and starts only after LT-p-1 has drained on this same slot. workflows/legacy_transform/blackdiamond-49financial/: the run home for this subject, narrowed to the subject directory rather than the whole tree. It overlaps LT-x-1 (pending, its worker has reported and no worker is live on it; the issuer flips it at this drain) and LT-x-3 (UNSPAWNED and dependent on LT-x-1), so the three are sequenced and never concurrent. The surprise channel is named by every order of this project and is append-only by convention, which is not a contention.
</preflight>

Seating: slot ~2, level 5. Round 1 of LGIC_LGCTFM, the AMENDMENT issuance on decomposition v1.2 (v1 @686d196fa1, s.10 at the L6 cut, s.11 here), issued by `2.0.0_SA_COO~G` on RULING R-36. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py with the five a4-* arms, PLANTED_CONTRACT.json carrying the untypeable cell at 0, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json) and `org/standards/LGCTFM_CONTRACT.schema.json`. Rulings carried: R-35 (the run home is a record tree for the naming gate), R-36 (this cell), R-16, R-24.
