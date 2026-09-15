# TO LGIC_ENFORCE.TO-EN-x-1-r2 -- FWD-2 again, on one carrier

<to_id>LGIC_ENFORCE.TO-EN-x-1-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~4</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-x-1` (round 2) | **outcome_ref:** FWD-2 | **depends_on:** gate G-V19b (the one-carrier group on CLOUD) | **slot:** ~4, queue position 1

---

## WORKER FACE

### THE CELL

`EN-x-1` -- FWD-2 again: one change moves a resource's name and its firm's fence pattern together (RULING ONE; row W1-S19 was the second carrier, and row W1-S21 the filters that were not disjoint).

On a practice copy (below):
1. Add `infra/aws/terraform/shared-infra/lgic-enforce-fwd2-resource.tf`, declaring ONE resource whose name comes from the `opal_name` module for `49financial` (round 1's SQS queue suits: no data, and no cost until it is created, which it never is here). Export `SAFE_APPLY_TERRAFORM=C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe` and `OPAL_AGENT_SERIAL`. Plan the REAL `shared-infra` tree read-only (`plan -lock=false -out`, then `show -json`, against the real backend). Save the JSON as `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/fwd2_plan_before.r2.json`. Commit the `.tf` on the scratch branch: that commit is `before`.
2. In the same practice copy, change `49financial`'s SHORT form in `infra/logic/registry/scopes.json` ONLY (`49f` to `f49`), run `python lib/opal_naming.py generate --out .`, and commit: that commit is `after`. Plan again, read-only, and save `fwd2_plan_after.r2.json` beside the first.
3. **Never apply.** The `.tf` never reaches your slot branch.

**Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD2_R2.md`:** prose, then ONE fenced ```json block
`{"resource": {"address": "...", "name": "..."}, "plans": {"before": "<path of fwd2_plan_before.r2.json>", "after": "<path of fwd2_plan_after.r2.json>"}, "registry_row": "49financial", "scratch_branch": "...", "commits": {"before": "<hash>", "after": "<hash>"}, "new_short": "f49"}`.
Round 1's `EXERCISE_FWD2.md` stays as its record.

- **Practice copy.** Create it as `git worktree add -b prac-lgic-enforce-x1-r2 <WS>/../prac-lgic-enforce-x1-r2 HEAD`, on a scratch branch that is NEVER pushed. Commit the exercise there, so its hashes are the evidence. When done, `git worktree remove` the CLEAN practice copy. Leave the scratch BRANCH in place: deleting an unmerged branch is destructive git. Your slot branch carries only your records.

**Read:** the `opal_name` module; the registry; `infra/aws/terraform/shared-infra/s3-49financial.tf` (the fence reads `module.opal_name.fence_patterns`).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="X1R-AC1" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py x1r-one-hand-edit</invocation><expect>VERDICT: PASS-ONE-HAND-EDIT</expect></criterion>
`X1R-AC1` -- between `before` and `after` exactly one file is hand-edited, `scopes.json`; every other changed file carries the GENERATED mark.

<criterion id="X1R-AC2" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py x1r-name-moved</invocation><expect>VERDICT: PASS-NAME-MOVED</expect></criterion>
`X1R-AC2` -- the resource's name in the plan moves from the old short form to the new one.

<criterion id="X1R-AC3" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py x1r-fence-moved</invocation><expect>VERDICT: PASS-FENCE-MOVED</expect></criterion>
`X1R-AC3` -- the firm's fence pattern in the generated locals moves from the old short form to the new one.

<expected_criteria>X1R-AC1, X1R-AC2, X1R-AC3</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn (after gate G-V19b). Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **Live plane.** Two read-only `plan -lock=false` runs of the real `shared-infra` tree, from the practice copy. Nothing is applied.
- **The wide grant is for the PRACTICE COPY ONLY.** The registry, the carriers and the module in `<paths>` are there so the scratch branch can commit the generator's output. Your slot branch commits only your records. Anything else on it is a defect the drain refuses.

<paths>
infra/aws/terraform/shared-infra/lgic-enforce-fwd2-resource.tf
infra/logic/registry/scopes.json
data/firm_registry.json
infra/aws/lambda-edge/_shared/firm-config.mjs
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
infra/aws/lambda/investor-reporting/_authz/loaders.py
data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py
.tools/ds-precommit-check.py
infra/aws/terraform/modules/opal_name/
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD2_R2.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-x-1`, round 2 (section 0b).
<owned_cells>EN-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `X1R-AC1`, `X1R-AC2`, `X1R-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/LGIC_ENFORCE.TO-EN-x-1-r2.fwd2-one-carrier.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> X1R-AC1,X1R-AC2,X1R-AC3` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fwd2-one-carrier.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). G-V19b is owed before this cell spawns.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added; this cell's resource is planned, never created.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~4, queue position 1. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
