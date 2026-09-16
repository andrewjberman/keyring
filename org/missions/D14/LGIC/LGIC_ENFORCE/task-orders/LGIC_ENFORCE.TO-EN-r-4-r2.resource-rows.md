# TO LGIC_ENFORCE.TO-EN-r-4-r2 -- the resource-to-system rows

<to_id>LGIC_ENFORCE.TO-EN-r-4-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-r-4` (round 2) | **outcome_ref:** FWD-5 (and LGIC_NAMING FWD-5, through its cell f-1) | **depends_on:** EN-r-2 round 2 (merged) | **slot:** ~1, queue position 3

---

## WORKER FACE

### THE CELL

`EN-r-4` -- the resource-to-system rows (PRD v1.2 DEC-1, candidate E13; `1.0.0_SA_CTO`'s ruling 97177). In 48 of LGIC_NAMING round 2's forms, the token after the scope is a FUNCTION word (gold, api, exporter ...), never a system, so no `systems.json` row fills `{system}`. The schema already names where the slot comes from: `org/standards/NAMING_SCHEMA.json` `grade.placeholder`, *"{system} from the identity registry's resource-to-system rows (LGIC_ENFORCE)"*. No file holds those rows yet.

**The population is fixed:** `C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/RESOURCE_GAPS.json`. It holds the 48 names (IAM roles: 49financial 14, inflection 27, cottonwood 6, demo 1) whose canonical form carries `{system}` at the cut. Fill these first. Then add rows for MDPF, ADVI and IRPT resources (96910), wherever evidence names the owner.

1. **Create `infra/logic/registry/resources.json`**, shaped `{"_about": "...", "resources": [ {"name": ..., "type": ..., "system": ..., "evidence": ...} ]}`. Each row has exactly these four fields:
   - `name`: the resource's name exactly as its plane carries it;
   - `type`: its node type, one the grade takes (`NAMING_SCHEMA.json` `kind.by_type` or `types_not_graded_by_kind`);
   - `system`: a `systems.json` key;
   - `evidence`: the `path@commit` and the line or row that attributes the resource to that system (the Terraform module that declares it, its owning project in `org/missions/DIRECTIVES.yaml`, or the census report's attribution).

   A row fills one `{system}` gap and nothing else, so it carries no scope: the name's own tokens give its scope.
2. **Add `resources.json` to the registry `lib/opal_naming.py` loads, and read it in the grade.** `grade(name, type)` reads a row ONLY where the name's own tokens resolve no system: rules R1.d and R1.e, `_slots` `:916-926` at CLOUD @7b5331c8c0 (re-read it at your base). With a row, `{system}` is the row's system and the name is graded as usual. Without one, the placeholder stays. The signature and the three verdicts are unchanged.
3. **`validate` refuses** each of the following, one line per refusal, shaped like the other files' lines: `REFUSED resources.json[<index>].<field>: <reason naming the value>`.
   - a row with a field missing or empty;
   - a repeated (`name`, `type`);
   - a `system` that is not a `systems.json` key, or is `opal`;
   - a `type` the grade does not take;
   - a row for a name whose own tokens already resolve a system (that row would be a second carrier of what the name says).
4. **A resource no owner can be named for gets NO row.** It keeps its placeholder and is counted, never guessed. If its owner is a system with no `systems.json` row, file a surprise row and count it: `systems.json` is `EN-r-2`'s, not this grant's.
5. **Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/RESOURCE_ROWS.md`:** prose, then ONE fenced ```json block
   `{"population": "<the fixed input's path>", "rows": <n>, "placeholders": [{"name": "...", "type": "...", "why": "<why no owner can be named>"}]}`.
   The rows themselves are `resources.json`'s. A placeholder is listed here and never there.

The registry's hash moves with this cell, so the generated views' headers go stale until `EN-r-6` regenerates them; that is expected, and regeneration is not this cell's. Tests of the five refusals in `lib/tests/test_opal_naming.py` are welcome.

**Read:** the fixed input; `lib/opal_naming.py` (`_slots`, `grade`, `validate`, `load_registry`, `REGISTRY_FILES`); `org/standards/NAMING_SCHEMA.json` (`grade.placeholder`, `kind.by_type`); `infra/logic/registry/systems.json`; `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md`; `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md`; `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R4-AC1" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-row-shape</invocation><expect>VERDICT: PASS-RESOURCE-ROW-SHAPE</expect></criterion>
`R4-AC1` -- every row carries exactly `name`, `type`, `system` and `evidence`, none empty.

<criterion id="R4-AC2" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-registry-valid</invocation><expect>VERDICT: PASS-R4-REGISTRY-VALID</expect></criterion>
`R4-AC2` -- the registry, `resources.json` included, validates with 0 refusals.

<criterion id="R4-AC3" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-refuses-empty</invocation><expect>VERDICT: PASS-REFUSES-EMPTY-FIELD</expect></criterion>
`R4-AC3` -- validate refuses a planted row whose `evidence` is empty.

<criterion id="R4-AC4" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-refuses-duplicate</invocation><expect>VERDICT: PASS-REFUSES-REPEATED-ROW</expect></criterion>
`R4-AC4` -- validate refuses a planted copy of an existing row.

<criterion id="R4-AC5" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-refuses-unregistered</invocation><expect>VERDICT: PASS-REFUSES-UNREGISTERED-SYSTEM</expect></criterion>
`R4-AC5` -- validate refuses a planted row whose `system` is no `systems.json` key.

<criterion id="R4-AC6" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-refuses-opal</invocation><expect>VERDICT: PASS-REFUSES-OPAL-SYSTEM</expect></criterion>
`R4-AC6` -- validate refuses a planted row whose `system` is `opal`.

<criterion id="R4-AC7" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-refuses-type</invocation><expect>VERDICT: PASS-REFUSES-UNGRADED-TYPE</expect></criterion>
`R4-AC7` -- validate refuses a planted row whose `type` the grade does not take.

<criterion id="R4-AC8" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-refuses-self-resolving</invocation><expect>VERDICT: PASS-REFUSES-SELF-RESOLVING-ROW</expect></criterion>
`R4-AC8` -- validate refuses a planted row for a name whose own tokens resolve a system.

<criterion id="R4-AC9" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-grade-fills</invocation><expect>VERDICT: PASS-GRADE-FILLS-FROM-ROW</expect></criterion>
`R4-AC9` -- `grade()` over every rowed gap puts the row's system in its canonical form, and with `resources.json` emptied in a scratch copy the same name keeps `{system}`.

<criterion id="R4-AC10" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-gaps-covered</invocation><expect>VERDICT: PASS-EVERY-GAP-ROWED-OR-COUNTED</expect></criterion>
`R4-AC10` -- each of the 48 gaps is a `resources.json` row or a counted placeholder with its reason, never both.

<criterion id="R4-AC11" cell_refs="EN-r-4"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r4-tests</invocation><expect>VERDICT: PASS-R4-NO-NEW-LIB-TEST-FAILURE</expect></criterion>
`R4-AC11` -- `lib/tests/test_opal_naming.py` has no new failure against the base's failing set (RULING RED).

<criterion id="R4-J1" cell_refs="EN-r-4" judgment="true"/>
`R4-J1` -- graded at L9 by 3.0.0_SA_CVO: every row's evidence attributes the resource to that system, and every placeholder's reason holds. RECORD; NO VERDICT.

<expected_criteria>R4-AC1, R4-AC2, R4-AC3, R4-AC4, R4-AC5, R4-AC6, R4-AC7, R4-AC8, R4-AC9, R4-AC10, R4-AC11, R4-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn (after `EN-r-2` drains, which is after gate G-V19b). Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **One writer of `lib/opal_naming.py` at a time.** `EN-r-5` and the V19 group have landed before you spawn, and `EN-r-6` spawns only after you drain. Nothing else in this round writes the file while you do.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **The checker plants rows in a scratch copy**, never in your tree; R4-AC3 to R4-AC8 each require the committed registry to validate clean first.
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform. A row is a verdict source, never a rename.

<paths>
infra/logic/registry/resources.json
lib/opal_naming.py
lib/tests/test_opal_naming.py
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/RESOURCE_ROWS.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-r-4`, round 2 (section 0b).
<owned_cells>EN-r-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `R4-AC1`, `R4-AC2`, `R4-AC3`, `R4-AC4`, `R4-AC5`, `R4-AC6`, `R4-AC7`, `R4-AC8`, `R4-AC9`, `R4-AC10`, `R4-AC11`, `R4-J1`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-r-4-r2.resource-rows.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R4-AC1,R4-AC2,R4-AC3,R4-AC4,R4-AC5,R4-AC6,R4-AC7,R4-AC8,R4-AC9,R4-AC10,R4-AC11,R4-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `resource-rows.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2.1 s.0b) and G-C (worker admission, after this issuance). None is owed by this cell; it spawns after G-V19b through EN-r-2.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, resources.json among them, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood. For this cell's source, PRD v1.2 was read as its diff from v1.1 @78128f29ea, not by its own summary.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/ or lib/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 3. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145), with this cell added by `1.0.0_SA_CTO`'s ruling 97177 on PRD v1.2 @09bde3126c. Issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). LGIC_NAMING's cell f-1 re-grade waits on this cell (97177). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
