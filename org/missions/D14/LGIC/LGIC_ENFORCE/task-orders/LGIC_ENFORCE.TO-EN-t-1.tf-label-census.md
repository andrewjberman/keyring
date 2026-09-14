# TO LGIC_ENFORCE.TO-EN-t-1 -- the Terraform-label census

<to_id>LGIC_ENFORCE.TO-EN-t-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.1 @78128f29ea (ADMITTED) | **Decomp cell:** `EN-t-1` | **outcome_ref:** FWD-4 | **depends_on:** -- (level 0; chain head) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`EN-t-1` -- the Terraform-label census (PRD candidate E8, its first half; *"specified only after the Terraform-label census"*).

Over every TRACKED `.tf` file under `infra/aws/terraform/`, list separately:
- every resource LABEL (`resource "<type>" "<label>"`);
- every resource-name ATTRIBUTE (`name`, `function_name`, `bucket`, `role_name`, and the like, whichever the resource type names by).

Grade each with the schema's rule. `grade()` is EN-b-1's and may not be at HEAD when you start. Apply `GRADING_RULE.md` (LGIC_NAMING, merged) by its written steps and state which you used. Labels are Terraform-internal identifiers, not AWS names: grade them by the rule anyway, and keep them apart.

**Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md`:** prose, then ONE fenced ```json block:
```
{"denominator": {"tf_files": <n>, "labels": <n>, "name_attributes": <n>},
 "labels": [{"file": "...", "line": <n>, "type": "...", "label": "...", "verdict": "...", "canonical": "..."}],
 "name_attributes": [{"file": "...", "line": <n>, "type": "...", "attribute": "...", "value": "...", "verdict": "...", "canonical": "..."}]}
```
`tf_files` is `git ls-files infra/aws/terraform` restricted to `.tf`, at your base.

**Read:** the tracked .tf files; GRADING_RULE.md; NAMING_SCHEMA.json.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="T1-AC1" cell_refs="EN-t-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py t1-apart</invocation><expect>VERDICT: PASS-REPORTED-APART</expect></criterion>
`T1-AC1` -- labels and name attributes are reported as separate lists.

<criterion id="T1-AC2" cell_refs="EN-t-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py t1-denominators</invocation><expect>VERDICT: PASS-DENOMINATORS</expect></criterion>
`T1-AC2` -- the denominators equal the list lengths and the tracked .tf count.

<criterion id="T1-AC3" cell_refs="EN-t-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py t1-graded</invocation><expect>VERDICT: PASS-GRADED</expect></criterion>
`T1-AC3` -- every row carries a verdict.

<expected_criteria>T1-AC1, T1-AC2, T1-AC3</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_en.py` (the checker every criterion calls), its fixtures under `tests/`, and `g1_preimage/`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform apply. Any live read is read-only through the `aws` shim.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v1.1 @53d221f334, cell `EN-t-1`.
<owned_cells>EN-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `T1-AC1`, `T1-AC2`, `T1-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-t-1.tf-label-census.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> T1-AC1,T1-AC2,T1-AC3` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `tf-label-census.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~3, queue position 1. Round 1 of LGIC_ENFORCE; issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974), leading the sequence on Andrew-direct ~16:3xZ (record @507864b842). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: `check_en.py` (every criterion's instrument) and its fixtures. Decomposition v1.1 @53d221f334.
