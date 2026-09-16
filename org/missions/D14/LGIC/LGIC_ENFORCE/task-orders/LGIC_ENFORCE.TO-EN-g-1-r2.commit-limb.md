# TO LGIC_ENFORCE.TO-EN-g-1-r2 -- the commit limb refuses only additions to authored files

<to_id>LGIC_ENFORCE.TO-EN-g-1-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete -- 4/4 mechanical criteria PASS by output (G1R-AC1 re-graded PASS after the issuer's fixture fix @6f640ead30, drained @4f7f050f2c; proof-of-spec VALID rc=0); LGIC_ENFORCE-W3-S10 disposed by LGIC_ENFORCE-W3-S11 (GRADUATED)</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-g-1` (round 2) | **outcome_ref:** FWD-4 | **depends_on:** gate G-V19b (the one-carrier group, with NAMING_SCHEMA.json v1.9's map, on CLOUD) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`EN-g-1` -- the commit limb refuses only what a change ADDS to an AUTHORED file (`1.0.0_SA_CTO`'s round-1 analysis s.2, RULING ADD; rows W2-S9 and W1-S22; C-S11). Edit `.tools/naming-gate.py`:

1. **A machine-written plan file is not graded at commit.** A JSON file whose top level carries `format_version`, `terraform_version`, and `resource_changes` or `planned_values` (a `terraform show -json` artifact) is skipped, and the limb prints that it skipped it. An authored JSON file is graded exactly as today. Row W1-S22 measured the old behaviour: 115 REFUSE and 13 RAISE on one ordered plan file.
2. **The limb validates the registry BEFORE it reads it** (row W2-S9). When `lib/opal_naming.py validate` refuses the registry, the limb prints `NAMING ERROR <a reason that names the registry refusal>` and grades nothing. Enforcing, it exits 1 (fail-closed); in WARN mode it exits 0.
3. **The Terraform-type-to-node-type map is read from `org/standards/NAMING_SCHEMA.json` v1.9** (C-S11), and the limb keeps no map of its own. You may keep the name `TF_NODE`, bound to the map read from the schema, so the apply limb's import of it still resolves; no literal map remains.

Nothing else in DEC-6's matrix moves: round 1's 14 commit-limb criteria must still pass.

**Read:** `.tools/naming-gate.py`; `org/standards/NAMING_SCHEMA.json` v1.9 (the map); `lib/opal_naming.py` (`validate`); the fixtures under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/tests/g1r/`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G1R-AC1" cell_refs="EN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py g1r-plan-not-graded</invocation><expect>VERDICT: PASS-PLAN-FILE-NOT-GRADED</expect></criterion>
`G1R-AC1` -- the limb tells a machine-written plan file (not graded) from an authored file carrying the same name (refused).

<criterion id="G1R-AC2" cell_refs="EN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py g1r-registry-first</invocation><expect>VERDICT: PASS-REGISTRY-VALIDATED-FIRST</expect></criterion>
`G1R-AC2` -- the limb validates the registry first: over a refused registry it prints `NAMING ERROR` and exits 1 enforcing and 0 in WARN mode, and over the valid registry it prints none.

<criterion id="G1R-AC3" cell_refs="EN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py g1r-map-from-schema</invocation><expect>VERDICT: PASS-COMMIT-LIMB-READS-SCHEMA-MAP</expect></criterion>
`G1R-AC3` -- the limb holds no Terraform-type map of its own, and the schema carries one.

<criterion id="G1R-AC4" cell_refs="EN-g-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py g1r-regression</invocation><expect>VERDICT: PASS-G1-SUITE-HOLDS</expect></criterion>
`G1R-AC4` -- round 1's 14 commit-limb criteria still pass.

<expected_criteria>G1R-AC1, G1R-AC2, G1R-AC3, G1R-AC4</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn (after gate G-V19b). Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **The WARN window stays shut.** Never create `org/mcp/naming-gate.enforce`; enforcement is per invocation (`--enforce`). G-F's live flip is not this round.
- **The checker plants a registry row.** G1R-AC2 appends a refused FIRM row to `infra/logic/registry/scopes.json` and restores the file's bytes afterwards. Run it on a clean tree.

<paths>
.tools/naming-gate.py
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-g-1`, round 2 (section 0b).
<owned_cells>EN-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G1R-AC1`, `G1R-AC2`, `G1R-AC3`, `G1R-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-g-1-r2.commit-limb.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G1R-AC1,G1R-AC2,G1R-AC3,G1R-AC4` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `commit-limb.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). G-V19b is owed before this cell spawns; G-F (the live flip) stays outside this round.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~3, queue position 1. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
