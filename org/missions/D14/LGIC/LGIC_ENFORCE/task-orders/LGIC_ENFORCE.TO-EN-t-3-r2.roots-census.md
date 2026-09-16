# TO LGIC_ENFORCE.TO-EN-t-3-r2 -- the Terraform roots, read with the switch on

<to_id>LGIC_ENFORCE.TO-EN-t-3-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-t-3` (round 2) | **outcome_ref:** FWD-4 (G-F's prerequisite) | **depends_on:** EN-t-2 round 2 (merged) | **slot:** ~3, queue position 3

---

## WORKER FACE

### THE CELL

`EN-t-3` -- the Terraform roots, read with the switch on (`1.0.0_SA_CTO`'s round-1 analysis s.2, RULING ADD: *"G-F flips ONLY when the 78 roots read 0 refusals of existing resources with the switch on"*). Nothing is applied, and the switch is never left on: enforcement is per invocation (`--enforce`), never the enforce file. G-F's flip is not this cell's.

1. **Plan every root.** A root is a directory under `infra/aws/terraform/` whose tracked `.tf` files declare a `backend` block; the checker enumerates them from `git ls-files`, 73 at the cut. For each one:
   - `terraform init` from the plugin cache (`TF_PLUGIN_CACHE_DIR` is set on this box), then a read-only `plan -lock=false -input=false -out`, then `show -json`. Use `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe`, and export `OPAL_AGENT_SERIAL`.
   - Keep only `format_version`, `terraform_version`, and each resource change's `address`, `mode`, `type`, `name`, `change.actions`, and the own-name attribute of `change.before` and `change.after`. Write it to `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/roots/<root path with / written as __>.r2.json`.
   - ⛔ **ONE ROOT AT A TIME, AND DELETE THAT ROOT'S `.terraform` THE MOMENT ITS `show -json` IS CAPTURED.** Do not init the next root until the previous one's directory is gone. **This is not tidiness -- it is the only reason this cell can run at all**, and it is a CORRECTION to the cell made before any worker was spawned (row `LGIC_ENFORCE-S22`).
     MEASURED on the one root already initialised in the main checkout: `du -sh infra/aws/terraform/portal-auth/.terraform` reads **686M**, of which **686M** is `providers/registry.terraform.io/hashicorp/aws` and 4.0K is state. `TF_PLUGIN_CACHE_DIR` **IS** set and populated (722M) and it does **NOT** spare this -- `ls -la` of that providers directory shows an ordinary copied tree, not a link. So the cache's existence is not mitigation on this filesystem.
     **73 roots x 686 MB is about 50 GB. This box had 19 GB free when this cell was cut, with four other workers live.** Per-root cleanup caps the footprint at roughly ONE root; without it, this cell fills the volume and takes down every live worker and every other seat sharing the box -- **and you would have no way to know you were the cause.**
     If a root's `.terraform` cannot be removed (a lock, a permission), that root is recorded NOT planned with that reason and **you stop initialising further roots and file a BLOCKING row** -- never continue and hope. Re-measure free space every ten roots, not only at the start and the end, and stop on **the 10 GB line this order's BOUNDS section already sets** -- that is the single stop line for this cell and this clause does not add a second one.
     ⚠ This changes ONLY your housekeeping between roots. Every deliverable, every criterion, every `<paths>` entry and the NOT-planned rule are unchanged, and **a root you cannot plan is still recorded with its reason rather than skipped.**
   - A root that cannot init without fetching a provider from outside Opal infrastructure, or cannot plan, is recorded NOT planned with its reason. Never fetch off-box without the word.
2. **Run the limbs.** `python .tools/naming-apply-gate.py --plan-json <extract> --enforce` on each extract, and the pre-plan limb (`naming-apply-gate.py <dir> --enforce`) on all 78 Terraform directories. The other 5 (4 under `modules/`, and `shared-infra/apigateway-portal`) have no backend and cannot plan alone.
3. **Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/LIMB_ROOTS_CENSUS.md`:** prose, then ONE fenced ```json block
   `{"vintage": "<UTC of the plans>", "roots": [{"root": "infra/aws/terraform/...", "planned": true, "extract": "<path>", "plan_sha256": "<of the full show -json>", "reason": null}], "additions": [{"root": "...", "address": "...", "name": "...", "verdict": "<the limb's verdict word>"}]}`.
   A pending create in a root's plan is DISCLOSED, never applied and never hidden.

**Read:** `.tools/naming-apply-gate.py`; `.tools/safe-apply.sh` (how it plans); `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="T3R-AC1" cell_refs="EN-t-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t3r-preplan-zero</invocation><expect>VERDICT: PASS-PREPLAN-REFUSES-NONE</expect></criterion>
`T3R-AC1` -- the pre-plan limb, enforcing, refuses none of the Terraform directories.

<criterion id="T3R-AC2" cell_refs="EN-t-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t3r-every-root-planned</invocation><expect>VERDICT: PASS-EVERY-BACKEND-ROOT-PLANNED</expect></criterion>
`T3R-AC2` -- every root with a backend block is planned read-only, with its extract recorded.

<criterion id="T3R-AC3" cell_refs="EN-t-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t3r-zero-existing-refused</invocation><expect>VERDICT: PASS-ZERO-EXISTING-REFUSED</expect></criterion>
`T3R-AC3` -- the plan limb, enforcing, refuses no resource that is neither created nor renamed.

<criterion id="T3R-AC4" cell_refs="EN-t-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t3r-additions-disclosed</invocation><expect>VERDICT: PASS-ADDITIONS-DISCLOSED</expect></criterion>
`T3R-AC4` -- every create and rename in the extracts is disclosed with the limb's verdict.

<criterion id="T3R-J1" cell_refs="EN-t-3" judgment="true"/>
`T3R-J1` -- graded at L9 by 3.0.0_SA_CVO: the extracts are the roots' real plans (a spot re-plan of at least one root agrees). RECORD; NO VERDICT.

<expected_criteria>T3R-AC1, T3R-AC2, T3R-AC3, T3R-AC4, T3R-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **Live plane.** Read-only plans against the real backends, `-lock=false`. Nothing is applied, no state is written, and no ledger act is owed. Never create `org/mcp/naming-gate.enforce`.
- **Disk.** Every `init` writes a `.terraform` directory into your worktree; the 10G stop line binds. Record the free space at the start and the end.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/LIMB_ROOTS_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-t-3`, round 2 (section 0b).
<owned_cells>EN-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `T3R-AC1`, `T3R-AC2`, `T3R-AC3`, `T3R-AC4`, `T3R-J1`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-t-3-r2.roots-census.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> T3R-AC1,T3R-AC2,T3R-AC3,T3R-AC4,T3R-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `roots-census.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). This cell measures G-F's prerequisite; G-F's live flip is not this round.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added; the plans are read-only.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~3, queue position 3. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
