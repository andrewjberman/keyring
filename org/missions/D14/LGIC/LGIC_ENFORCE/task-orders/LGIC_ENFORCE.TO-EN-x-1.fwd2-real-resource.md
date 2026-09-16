# TO LGIC_ENFORCE.TO-EN-x-1 -- FWD-2 on a real resource

<to_id>LGIC_ENFORCE.TO-EN-x-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete -- proof-of-spec VALID (rc=0) against org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-x-1.fwd2-real-resource.proof_of_spec.json, gate run 2026-09-16 by the issuer with --governing-order bound; the work drained in its round and only the status WORD was never flipped, leaving a live ADHC_OWNPTH.005 worker grant at HEAD (0.0.0_AB_MSTR 97450)</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.1 @78128f29ea (ADMITTED) | **Decomp cell:** `EN-x-1` | **outcome_ref:** FWD-2 | **depends_on:** EN-m-1 and EN-f-2 (merged) | **slot:** ~1, queue position 7

---

## WORKER FACE

### THE CELL

`EN-x-1` -- FWD-2 on a real resource (PRD candidate E12; DEC-10). ADVI_FIRMBKTS's new buckets, DEC-10's first candidates, are NOT used: that project is held behind this one's fence.

On a practice copy (below):
1. Add `infra/aws/terraform/shared-infra/lgic-enforce-fwd2-resource.tf`, declaring ONE resource whose name comes from the `opal_name` module for `49financial` (an SQS queue suits: no data, no cost until it is created, and it is never created here). Export `SAFE_APPLY_TERRAFORM=C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe`. Plan the REAL tree read-only (`plan -lock=false -out`, then `show -json`, against the real backend), and save the JSON as `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/fwd2_plan.json`. Commit the `.tf` on the scratch branch. That commit is `before`. **Never apply.** The file never reaches your slot branch.
2. In the same practice copy, change `49financial`'s SHORT form in `scopes.json` (for example `49f` to `f49`) and regenerate. Commit it; that commit is `after`. The resource's name AND the fence's pattern for the firm must both move on that one change.

- **Practice copy.** Create it as `git worktree add -b prac-lgic-enforce-x1 <WS>/../prac-lgic-enforce-x1 HEAD`, on a scratch branch that is NEVER pushed. Commit the exercise there, so its hashes are the evidence. When done, `git worktree remove` the CLEAN practice copy. Leave the scratch BRANCH in place: deleting an unmerged branch is destructive git. Your slot branch carries only your records.

**Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD2.md`:** prose, then ONE fenced ```json block:
`{"resource": {"address": "...", "name": "..."}, "plan_json": "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/fwd2_plan.json", "registry_row": "49financial", "scratch_branch": "...", "commits": {"before": "<hash>", "after": "<hash>"}, "new_short": "<the changed short form>"}`

**Read:** the module; the registry; s3-49financial.tf (the fence, as EN-f-2 left it).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="X1-AC1" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py x1-plan</invocation><expect>VERDICT: PASS-RESOURCE-IN-PLAN</expect></criterion>
`X1-AC1` -- a resource named by the module for 49financial lands in a plan on the real tree.

<criterion id="X1-AC2" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py x1-same-row</invocation><expect>VERDICT: PASS-SAME-ROW</expect></criterion>
`X1-AC2` -- its name and the firm's fence pattern come from the same registry row.

<criterion id="X1-AC3" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py x1-moves-both</invocation><expect>VERDICT: PASS-BOTH-MOVE</expect></criterion>
`X1-AC3` -- one change to the short form moves the resource's name and the fence pattern together.

<expected_criteria>X1-AC1, X1-AC2, X1-AC3</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_en.py` (the checker every criterion calls), its fixtures under `tests/`, and `g1_preimage/`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Live plane.** A read-only `plan -lock=false` of the real tree, from the practice copy. Nothing is applied.
- **Practice copy.** Create it as `git worktree add -b prac-lgic-enforce-x1 <WS>/../prac-lgic-enforce-x1 HEAD`, on a scratch branch that is NEVER pushed. Commit the exercise there, so its hashes are the evidence. When done, `git worktree remove` the CLEAN practice copy. Leave the scratch BRANCH in place: deleting an unmerged branch is destructive git. Your slot branch carries only your records.

<paths>
infra/aws/terraform/shared-infra/lgic-enforce-fwd2-resource.tf
infra/logic/registry/scopes.json
infra/aws/terraform/modules/opal_name/
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD2.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v1.1 @53d221f334, cell `EN-x-1`.
<owned_cells>EN-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `X1-AC1`, `X1-AC2`, `X1-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-x-1.fwd2-real-resource.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> X1-AC1,X1-AC2,X1-AC3` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fwd2-real-resource.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This project registered G-B (first half DISCHARGED @ce7349b7cc; EN-s-2 waits on the second), G-C (worker admission, checked after this issuance), G-E (the never-widen sign-off before EN-f-2), G-F (the live REFUSE flip, outside this round), G-S (the ADVI_FIRMBKTS manual gate) and G-W (write logging; EN-c-2 takes writers from grants). None is owed by this cell.
comp-iam: RUN at L5 -- stats 209 roles, 189 services, 1,091 operations, 310 gaps; APPLICABLE (EN-f-2 applies a bucket policy and three roles; EN-c-2 is a grant census); blind to bucket policies, so the fence is proved by real probes (DEC-4). This cell adds no operation, policy, principal or resource.
comp-adversary: RUN at L5 on the PRD at v1.1 -- 15 of 15 cited commits verified; 19 cited paths, 12 stable, 3 MOVED (s3-49financial.tf, SEQUENCE.yaml, NAMING_SCHEMA.json now v1.4), 4 GONE (this project mints them). Blindness stated: T11, its complement is filesystem adjacency.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 7. Round 1 of LGIC_ENFORCE; issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974), leading the sequence on Andrew-direct ~16:3xZ (record @507864b842). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: `check_en.py` (every criterion's instrument) and its fixtures. Decomposition v1.1 @53d221f334.
