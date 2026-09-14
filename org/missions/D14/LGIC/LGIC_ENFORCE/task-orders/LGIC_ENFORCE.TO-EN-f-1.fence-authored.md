# TO LGIC_ENFORCE.TO-EN-f-1 -- the fence, authored

<to_id>LGIC_ENFORCE.TO-EN-f-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.1 @78128f29ea (ADMITTED) | **Decomp cell:** `EN-f-1` | **outcome_ref:** FWD-2; the sequence gate on ADVI_FIRMBKTS | **depends_on:** EN-c-2, EN-r-1 and EN-m-1 (merged) | **slot:** ~1, queue position 5

---

## WORKER FACE

### THE CELL

`EN-f-1` -- the fence, authored (PRD candidate E5, its first half; DEC-4, Andrew's three conditions as ACCEPTANCE). **You plan; you do not apply.**

1. **The exemptions.** For every principal in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_WRITER_CENSUS.md` under `opal-data-49financial` that `fence_patterns("49financial")` does not match, add an `exemptions.json` row under `opal-data-49financial` with its `reason` and a `signoff_ref` naming this ledger entry (DEC-4 (ii)). LGIC_NAMING's LN-f-1 measured that the derived patterns catch only 12 of 68 live firm roles, so expect most of them to need a row. `bd-gold-layer-runner` is named in the template's own comment (`:76`). Then regenerate the module locals (`generate`).
2. **The policy.** In `infra/aws/terraform/shared-infra/s3-49financial.tf`, replace `DenyForeignFirmPrincipals`' enumerated list (`:98-112` at L5; the four patterns `role/cot-*`, `role/inf-*`, `role/mdpf-*`, `role/opal-assets-mdpf-*`) with the scope-derived Deny: deny every principal EXCEPT one whose resource-name scope slot is `49f`, or one `exemptions.json` names for this bucket. Both lists come from the module's generated locals and are never typed (DEC-4 (iii)). Touch only the policy's lines: LGIC_NAMING's notice at `:16-20` and CloudOps' read-logging block stay.
3. **The three probe roles**, in `infra/aws/terraform/shared-infra/lgic-enforce-fence-probes.tf`: `mdpf-49f-fenceprobe-role`, `mdpf-cot-fenceprobe-role` and the unscoped `mdpf-fenceprobe-role`. Each is named by the module, and each has one inline policy able to read only `opal-data-49financial`.
4. **The plan.** Export `SAFE_APPLY_TERRAFORM=C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe` and `OPAL_AGENT_SERIAL` at spawn. Plan `infra/aws/terraform/shared-infra/` read-only (`plan -lock=false -out`, then `show -json`). Save the JSON as `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/fence_plan.json`. It must show ONLY the policy update and the three roles with their three inline policies.
5. **The ledger (NEVER-2).** Save the LIVE policy now as `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PRIOR_POLICY.json`, verbatim (`aws s3api get-bucket-policy`): that is the rollback. Open the entry:
   `python .tools/deploy_ledger.py open --slug lgic-enforce-fence-49financial --title "LGIC_ENFORCE fence on opal-data-49financial" --author <your serial> --leg "L1|git|the authored change committed|commit hash" --leg "L2|activation|safe-apply shared-infra: the policy + 3 probe roles -- ROLLBACK: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PRIOR_POLICY.json|apply output + changed-resource list" --leg "L3|verify|the four probe arms|FENCE_PROBES.md" --leg "L4|verify|probe roles removed + re-plan 0-diff|get-role NoSuchEntity x3 + plan"`
   Close L1 with your commit's hash. **Commit the entry file AND its sentinel** (`org/critical_paths/.open_deploys/lgic-enforce-fence-49financial.json`): only a committed sentinel survives a forced worktree removal.
6. **The sign-off packet.** Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PLAN.md`: every principal whose access changes, per key; the rollback; both branches covered. Leave two blank lines in the ledger entry for `SIGNOFF 1.0.0_SA_CTO <YYYYMMDDTHHMMSSZ> <scope>` and `SIGNOFF 2.0.0_SA_COO~G <...>`. Those are the two seats' acts, never yours (gate G-E).

**Read:** FENCE_WRITER_CENSUS.md; the registry; the module; s3-49financial.tf; the live bucket policy (read-only).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="F1-AC1" cell_refs="EN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f1-covered</invocation><expect>VERDICT: PASS-EVERY-WRITER-COVERED</expect></criterion>
`F1-AC1` -- every opal-data-49financial writer matches the derived pattern or has an exemption row with reason and sign-off reference.

<criterion id="F1-AC2" cell_refs="EN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f1-no-typed-list</invocation><expect>VERDICT: PASS-NO-TYPED-LIST</expect></criterion>
`F1-AC2` -- the Deny carries no typed role-ARN list and reads the module's generated locals.

<criterion id="F1-AC3" cell_refs="EN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f1-plan</invocation><expect>VERDICT: PASS-PLAN-SCOPED</expect></criterion>
`F1-AC3` -- the plan shows only the policy update and the three probe roles with their inline policies.

<criterion id="F1-AC4" cell_refs="EN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f1-prior</invocation><expect>VERDICT: PASS-PRIOR-VERBATIM</expect></criterion>
`F1-AC4` -- FENCE_PRIOR_POLICY.json equals the live policy read now.

<criterion id="F1-AC5" cell_refs="EN-f-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f1-ledger-open</invocation><expect>VERDICT: PASS-LEDGER-OPEN</expect></criterion>
`F1-AC5` -- the ledger sentinel is OPEN with legs L1..L4, and L1's proof is a commit that exists.

<criterion id="F1-J1" cell_refs="EN-f-1" judgment="true"/>
`F1-J1` -- graded at L9 by 3.0.0_SA_CVO: FENCE_PLAN.md names every principal whose access changes and the rollback for each, covering both branches. RECORD; NO VERDICT.

<expected_criteria>F1-AC1, F1-AC2, F1-AC3, F1-AC4, F1-AC5, F1-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_en.py` (the checker every criterion calls), its fixtures under `tests/`, and `g1_preimage/`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Live plane.** Read-only: the bucket policy and a `plan -lock=false`. Nothing is applied in this cell.

<paths>
infra/aws/terraform/shared-infra/s3-49financial.tf
infra/aws/terraform/shared-infra/lgic-enforce-fence-probes.tf
infra/logic/registry/exemptions.json
infra/aws/terraform/modules/opal_name/
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PRIOR_POLICY.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FENCE_PLAN.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/lgic-enforce-fence-49financial.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v1.1 @53d221f334, cell `EN-f-1`.
<owned_cells>EN-f-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F1-AC1`, `F1-AC2`, `F1-AC3`, `F1-AC4`, `F1-AC5`, `F1-J1`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-f-1.fence-authored.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F1-AC1,F1-AC2,F1-AC3,F1-AC4,F1-AC5,F1-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fence-authored.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This project registered G-B (first half DISCHARGED @ce7349b7cc; EN-s-2 waits on the second), G-C (worker admission, checked after this issuance), G-E (the never-widen sign-off before EN-f-2), G-F (the live REFUSE flip, outside this round), G-S (the ADVI_FIRMBKTS manual gate) and G-W (write logging; EN-c-2 takes writers from grants). None is owed by this cell.
comp-iam: RUN at L5 -- stats 209 roles, 189 services, 1,091 operations, 310 gaps; APPLICABLE (EN-f-2 applies a bucket policy and three roles; EN-c-2 is a grant census); blind to bucket policies, so the fence is proved by real probes (DEC-4). This cell's own IAM surface: the policy change and the three probe roles.
comp-adversary: RUN at L5 on the PRD at v1.1 -- 15 of 15 cited commits verified; 19 cited paths, 12 stable, 3 MOVED (s3-49financial.tf, SEQUENCE.yaml, NAMING_SCHEMA.json now v1.4), 4 GONE (this project mints them). Blindness stated: T11, its complement is filesystem adjacency.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 5. Round 1 of LGIC_ENFORCE; issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974), leading the sequence on Andrew-direct ~16:3xZ (record @507864b842). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: `check_en.py` (every criterion's instrument) and its fixtures. Decomposition v1.1 @53d221f334.
