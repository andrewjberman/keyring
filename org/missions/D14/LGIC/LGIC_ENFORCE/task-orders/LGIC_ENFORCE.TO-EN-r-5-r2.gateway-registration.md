# TO LGIC_ENFORCE.TO-EN-r-5-r2 -- the gateway registration, whole

<to_id>LGIC_ENFORCE.TO-EN-r-5-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~6</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-r-5` (round 2) | **outcome_ref:** FWD-5, FWD-7 | **depends_on:** -- (level 0; spawned at issuance) | **slot:** ~6, queue position 1

---

## WORKER FACE

### THE CELL

`EN-r-5` -- the gateway registration, whole (CLAUDE.md Rule 30; `1.0.0_SA_CTO` msgs 97130 and 97167). `gateway` is a PLATFORM_SUBSYSTEM owned by D9 (`infra/logic/02_DOCTRINE.md` s.1 names it a platform subsystem; NFRA_OPLGTW, "Opal Gateway", is a D9 member), and it is the `{source}` of the Tax workbook bronze.

The change is prepared and verified by the issuer: `C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/gateway_whole.patch` (12 paths). In your worktree, run `git apply <that path>`. If it no longer applies, re-make its four parts by hand from the patch's own text, and never widen it:

1. `infra/logic/registry/systems.json`: the `gateway` row (class `PLATFORM_SUBSYSTEM`, owner `D9`, with the basis the patch states) and the `_about` `platform_subsystems` line.
2. `lib/opal_naming.py`: the vector shape `("opal", "gateway", None, "lb")` becomes `("opal", "ingress", None, "lb")`. With gateway a system, R2 refuses the old shape's `name()`.
3. `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md`: the `opal-gateway` LOAD_BALANCER worked case reads canonical `gateway-lb`, with the why the patch states. No other worked case moves.
4. The 9 generated views, regenerated with `python lib/opal_naming.py generate --out .`: the 7 DEC-5 carriers, `infra/aws/terraform/modules/opal_name/generated_locals.tf` and `infra/aws/terraform/modules/opal_name/tests/vectors.json`.

Registering gateway re-grades 14 live `opal-gateway-*` names to `gateway-*` canonical forms. That is a verdict, not a rename (`1.0.0_SA_CTO` 97167). Nothing live moves. This cell lands on CLOUD before any cell of gate G-V19 spawns: it writes `lib/opal_naming.py` and `GRADING_RULE.md`, as those cells do.

**Read:** the patch; `infra/logic/registry/systems.json`; `lib/opal_naming.py`; `GRADING_RULE.md` section 9.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R5-AC1" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r5-validate</invocation><expect>VERDICT: PASS-R5-SEVENTEEN-SYSTEMS</expect></criterion>
`R5-AC1` -- the registry validates with 0 refusals and 17 system rows.

<criterion id="R5-AC2" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r5-generate</invocation><expect>VERDICT: PASS-R5-VIEWS-MATCH</expect></criterion>
`R5-AC2` -- `generate` reproduces the 9 committed views byte for byte.

<criterion id="R5-AC3" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r5-tests</invocation><expect>VERDICT: PASS-R5-NO-NEW-SUITE-FAILURE</expect></criterion>
`R5-AC3` -- `lib/tests/test_opal_naming.py` has no new failure against the base's failing set (RULING RED).

<criterion id="R5-AC4" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r5-address</invocation><expect>VERDICT: PASS-R5-ADDRESS-IN-ASSETS</expect></criterion>
`R5-AC4` -- `address("gateway","49financial","bronze","taxsma_workbook","date=2026-09-15","snap-0001.json")` returns the `opal-data-assets` address.

<criterion id="R5-AC5" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r5-name</invocation><expect>VERDICT: PASS-R5-NAME-BUILT</expect></criterion>
`R5-AC5` -- `name("gateway","49financial","taxsma","role")` returns `gateway-49f-taxsma-role`.

<criterion id="R5-AC6" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r5-sharepoint</invocation><expect>VERDICT: PASS-R5-SHAREPOINT-STILL-REFUSED</expect></criterion>
`R5-AC6` -- a `sharepoint` source is still refused.

<criterion id="R5-AC7" cell_refs="EN-r-5"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r5-worked-case</invocation><expect>VERDICT: PASS-R5-ONE-WORKED-CASE-MOVED</expect></criterion>
`R5-AC7` -- only the `opal-gateway` worked case of `GRADING_RULE.md` moves, and it reads canonical `gateway-lb`.

<expected_criteria>R5-AC1, R5-AC2, R5-AC3, R5-AC4, R5-AC5, R5-AC6, R5-AC7</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18; the one-shot sentinel went stale on round 1's EN-x-1).
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform. Nothing deploys: the regenerated views are byte-equivalent in what they export, and a deploy rides each owner's path (Rule 13).

<paths>
infra/logic/registry/systems.json
lib/opal_naming.py
org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md
data/firm_registry.json
infra/aws/lambda-edge/_shared/firm-config.mjs
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
infra/aws/lambda/investor-reporting/_authz/loaders.py
data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py
.tools/ds-precommit-check.py
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/tests/vectors.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-r-5`, round 2 (section 0b).
<owned_cells>EN-r-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `R5-AC1`, `R5-AC2`, `R5-AC3`, `R5-AC4`, `R5-AC5`, `R5-AC6`, `R5-AC7`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~6/LGIC_ENFORCE.TO-EN-r-5-r2.gateway-registration.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R5-AC1,R5-AC2,R5-AC3,R5-AC4,R5-AC5,R5-AC6,R5-AC7` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `gateway-registration.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). This cell owes none of them; G-V19's cells wait on it.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). This cell exists because six of these paths' lanes refused the issuer (CLOUD_OPS_OR_ETL, PLATFORM_LOGIC_DOCS, TREE_DELIVERABLES); a worker grant is the canonical route.
</preflight>

Seating: slot ~6, queue position 1. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
