# TO LGIC_ENFORCE.TO-EN-f-2 -- the fence, applied and proved

<to_id>LGIC_ENFORCE.TO-EN-f-2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.1 @78128f29ea (ADMITTED) | **Decomp cell:** `EN-f-2` | **outcome_ref:** FWD-2; the sequence gate on ADVI_FIRMBKTS | **depends_on:** EN-f-1 (merged) AND gate G-E (both SIGNOFF lines on the ledger entry) | **slot:** ~1, queue position 6

---

## WORKER FACE

### THE CELL

`EN-f-2` -- the fence, applied and proved (PRD candidate E5, its second half). **This is the round's one APPLIED act.** You are spawned only after both never-widen sign-off halves are on the ledger entry (`SIGNOFF 1.0.0_SA_CTO ...` and `SIGNOFF 2.0.0_SA_COO~G ...`). If either is missing when you start, stop: that is a BLOCKING row.

1. Export `SAFE_APPLY_TERRAFORM=C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe` and `OPAL_AGENT_SERIAL`. Re-plan `infra/aws/terraform/shared-infra/` and confirm it equals EN-f-1's plan (only the policy and the three probe roles). Then apply through `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/shared-infra apply <that plan>`. Close ledger leg L2 with the apply output and the changed-resource list.
2. **The probes, real ones.** Never `simulate-principal-policy`, which does not evaluate a resource policy. As each probe role (`aws sts assume-role`), read one object of `opal-data-49financial`, and as one principal `exemptions.json` names, do the same. Record every probe in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PROBES.md`, ONE fenced ```json block:
   `{"probes": [{"role": "<name>", "kind": "<probe|exempt>", "action": "s3:GetObject", "object": "<key>", "result": "<ALLOWED|DENIED>", "evidence": "<request id + the exact error or ETag>"}]}`
   The expected arms: `mdpf-49f-fenceprobe-role` ALLOWED; `mdpf-cot-fenceprobe-role` DENIED; `mdpf-fenceprobe-role` DENIED; the exempt principal ALLOWED. Close leg L3.
3. **Remove the probe roles.** Delete `infra/aws/terraform/shared-infra/lgic-enforce-fence-probes.tf` and apply the removal. `aws iam get-role` must return NoSuchEntity for all three. Re-plan: 0 diff. Close leg L4, then `python .tools/deploy_ledger.py close --slug lgic-enforce-fence-49financial`, and append a `CLOSED <YYYYMMDDTHHMMSSZ>` line to the entry. Commit the entry and the sentinel.
4. **If a probe arm fails:** roll back to `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PRIOR_POLICY.json` in the same session (NEVER-2: a confirmed deploy is never left half-landed). Record it, and file a BLOCKING row.

**Read:** the ledger entry and sentinel; FENCE_PLAN.md; fence_plan.json; exemptions.json.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="F2-AC1" cell_refs="EN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f2-signoff</invocation><expect>VERDICT: PASS-SIGNED-BEFORE-APPLY</expect></criterion>
`F2-AC1` -- both SIGNOFF lines precede the apply leg's close time.

<criterion id="F2-AC2" cell_refs="EN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f2-policy-live</invocation><expect>VERDICT: PASS-POLICY-LIVE</expect></criterion>
`F2-AC2` -- the live bucket policy carries the derived Deny and none of the four enumerated patterns.

<criterion id="F2-AC3" cell_refs="EN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f2-probe-49f</invocation><expect>VERDICT: PASS-49F-READS</expect></criterion>
`F2-AC3` -- `mdpf-49f-fenceprobe-role` reads opal-data-49financial.

<criterion id="F2-AC4" cell_refs="EN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f2-probe-cot</invocation><expect>VERDICT: PASS-COT-DENIED</expect></criterion>
`F2-AC4` -- `mdpf-cot-fenceprobe-role` is denied.

<criterion id="F2-AC5" cell_refs="EN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f2-probe-unscoped</invocation><expect>VERDICT: PASS-UNSCOPED-DENIED</expect></criterion>
`F2-AC5` -- the unscoped, non-exempt `mdpf-fenceprobe-role` is denied.

<criterion id="F2-AC6" cell_refs="EN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f2-probe-exempt</invocation><expect>VERDICT: PASS-EXEMPT-ALLOWED</expect></criterion>
`F2-AC6` -- a principal exemptions.json names is allowed.

<criterion id="F2-AC7" cell_refs="EN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f2-removed</invocation><expect>VERDICT: PASS-PROBES-REMOVED</expect></criterion>
`F2-AC7` -- all three probe roles are gone from the account.

<criterion id="F2-AC8" cell_refs="EN-f-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f2-closed</invocation><expect>VERDICT: PASS-LEDGER-CLOSED</expect></criterion>
`F2-AC8` -- the ledger entry is closed.

<expected_criteria>F2-AC1, F2-AC2, F2-AC3, F2-AC4, F2-AC5, F2-AC6, F2-AC7, F2-AC8</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_en.py` (the checker every criterion calls), its fixtures under `tests/`, and `g1_preimage/`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Live plane. THIS CELL APPLIES:** the opal-data-49financial policy and three transient probe roles, through `.tools/safe-apply.sh`, under the never-widen sign-off (G-E) and the ledger entry, with the rollback in hand. Nothing else moves.

<paths>
infra/aws/terraform/shared-infra/lgic-enforce-fence-probes.tf
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PROBES.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/lgic-enforce-fence-49financial.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v1.1 @53d221f334, cell `EN-f-2`.
<owned_cells>EN-f-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F2-AC1`, `F2-AC2`, `F2-AC3`, `F2-AC4`, `F2-AC5`, `F2-AC6`, `F2-AC7`, `F2-AC8`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-f-2.fence-applied.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F2-AC1,F2-AC2,F2-AC3,F2-AC4,F2-AC5,F2-AC6,F2-AC7,F2-AC8` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fence-applied.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This project registered G-B (first half DISCHARGED @ce7349b7cc; EN-s-2 waits on the second), G-C (worker admission, checked after this issuance), G-E (the never-widen sign-off before EN-f-2), G-F (the live REFUSE flip, outside this round), G-S (the ADVI_FIRMBKTS manual gate) and G-W (write logging; EN-c-2 takes writers from grants). G-E is owed BEFORE this cell spawns.
comp-iam: RUN at L5 -- stats 209 roles, 189 services, 1,091 operations, 310 gaps; APPLICABLE (EN-f-2 applies a bucket policy and three roles; EN-c-2 is a grant census); blind to bucket policies, so the fence is proved by real probes (DEC-4). This cell's own IAM surface: the policy change and the three probe roles.
comp-adversary: RUN at L5 on the PRD at v1.1 -- 15 of 15 cited commits verified; 19 cited paths, 12 stable, 3 MOVED (s3-49financial.tf, SEQUENCE.yaml, NAMING_SCHEMA.json now v1.4), 4 GONE (this project mints them). Blindness stated: T11, its complement is filesystem adjacency.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 6. Round 1 of LGIC_ENFORCE; issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974), leading the sequence on Andrew-direct ~16:3xZ (record @507864b842). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: `check_en.py` (every criterion's instrument) and its fixtures. Decomposition v1.1 @53d221f334.
