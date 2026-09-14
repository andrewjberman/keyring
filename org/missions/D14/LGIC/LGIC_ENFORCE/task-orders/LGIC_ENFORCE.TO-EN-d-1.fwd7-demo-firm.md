# TO LGIC_ENFORCE.TO-EN-d-1 -- FWD-7 and FWD-1 on a practice copy

<to_id>LGIC_ENFORCE.TO-EN-d-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~8</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.1 @78128f29ea (ADMITTED) | **Decomp cell:** `EN-d-1` | **outcome_ref:** FWD-7, FWD-1 | **depends_on:** EN-r-1, EN-b-1, EN-g-1 and EN-v-1..6 (merged) | **slot:** ~8, queue position 1

---

## WORKER FACE

### THE CELL

`EN-d-1` -- firm N+1 is one row (PRD candidate E11, its first half; DEC-9). The fictitious firm is FIXED: long form `quillwater`, short form `qwt`. L6 measured 0 hits for either as a whole segment in the live plane (2,531 nodes, vintage 2026-09-14 12:13:53 UTC), and only the decomposition names them in the repo. It is never pushed and never `demo`.

On a practice copy (below):
1. **Compute the expected diff set FIRST**, from the registry's consumer list: every file the generator writes that must change when one scope row is added. Write it to `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/expected_diff.txt` and COMMIT it on the scratch branch. That commit is `expected_set`.
2. Add ONE `scopes.json` row for `quillwater`/`qwt`, run `python lib/opal_naming.py generate --out .` and commit. That commit is `generated`. The actual diff, less the registry itself, must equal the expected set exactly.
3. A hand-typed ADDRESS for the firm (for example `opal-data-quillwater/silver/x`) in a new config file, run through `naming-gate.py --enforce --diff`: REFUSED. Save the output.
4. A hand-typed occurrence of the firm's NAME (`quillwater` or `qwt`) as a dict key in a new config map, run the same way: REFUSED. Save the output.
5. Write a NEW pipeline for the firm (a small Python script that builds its storage locations only through `key()` and `address()`) and commit it on the scratch branch. Its path is `pipeline_path`. EN-d-2, a different worker, searches it.

- **Practice copy.** Create it as `git worktree add -b prac-lgic-enforce-d1 <WS>/../prac-lgic-enforce-d1 HEAD`, on a scratch branch that is NEVER pushed. Commit the exercise there, so its hashes are the evidence. When done, `git worktree remove` the CLEAN practice copy. Leave the scratch BRANCH in place: deleting an unmerged branch is destructive git. Your slot branch carries only your records.

**Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD7.md`:** prose, then ONE fenced ```json block:
`{"scratch_branch": "...", "firm": {"long": "quillwater", "short": "qwt"}, "commits": {"expected_set": "<hash>", "generated": "<hash>"}, "expected_files": [...], "actual_files": [...], "outputs": {"hand_address_refused": "...", "hand_name_refused": "..."}, "pipeline_path": "..."}`

**Read:** the registry; lib/opal_naming.py; .tools/naming-gate.py; the generated views.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="D1-AC1" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py d1-firm</invocation><expect>VERDICT: PASS-FIXED-FIRM</expect></criterion>
`D1-AC1` -- the exercise uses the fixed fictitious firm.

<criterion id="D1-AC2" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py d1-order</invocation><expect>VERDICT: PASS-EXPECTED-FIRST</expect></criterion>
`D1-AC2` -- the expected-set commit precedes the generator's commit.

<criterion id="D1-AC3" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py d1-diff-equal</invocation><expect>VERDICT: PASS-DIFF-EQUALS-EXPECTED</expect></criterion>
`D1-AC3` -- the generator's actual diff equals the expected set.

<criterion id="D1-AC4" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py d1-address-refused</invocation><expect>VERDICT: PASS-ADDRESS-REFUSED</expect></criterion>
`D1-AC4` -- a hand-typed address for the firm is refused.

<criterion id="D1-AC5" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py d1-name-refused</invocation><expect>VERDICT: PASS-NAME-REFUSED</expect></criterion>
`D1-AC5` -- a hand-typed occurrence of the firm's name in a config map is refused.

<criterion id="D1-AC6" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py d1-pipeline</invocation><expect>VERDICT: PASS-PIPELINE-WRITTEN</expect></criterion>
`D1-AC6` -- the new pipeline is committed on the scratch branch.

<expected_criteria>D1-AC1, D1-AC2, D1-AC3, D1-AC4, D1-AC5, D1-AC6</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_en.py` (the checker every criterion calls), its fixtures under `tests/`, and `g1_preimage/`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform apply. Any live read is read-only through the `aws` shim.
- **Practice copy.** Create it as `git worktree add -b prac-lgic-enforce-d1 <WS>/../prac-lgic-enforce-d1 HEAD`, on a scratch branch that is NEVER pushed. Commit the exercise there, so its hashes are the evidence. When done, `git worktree remove` the CLEAN practice copy. Leave the scratch BRANCH in place: deleting an unmerged branch is destructive git. Your slot branch carries only your records.
- **The wide grant is for the PRACTICE COPY ONLY.** The generated carriers and the module in `<paths>` are there so the scratch branch can commit the generator's output. Your slot branch commits only your records. Anything else on it is a defect the drain refuses.

<paths>
infra/logic/registry/scopes.json
data/firm_registry.json
infra/aws/lambda-edge/_shared/firm-config.mjs
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
infra/aws/lambda/investor-reporting/_authz/loaders.py
data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py
.tools/ds-precommit-check.py
infra/aws/terraform/modules/opal_name/
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD7.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v1.1 @53d221f334, cell `EN-d-1`.
<owned_cells>EN-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `D1-AC1`, `D1-AC2`, `D1-AC3`, `D1-AC4`, `D1-AC5`, `D1-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~8/LGIC_ENFORCE.TO-EN-d-1.fwd7-demo-firm.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> D1-AC1,D1-AC2,D1-AC3,D1-AC4,D1-AC5,D1-AC6` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fwd7-demo-firm.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~8, queue position 1. Round 1 of LGIC_ENFORCE; issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974), leading the sequence on Andrew-direct ~16:3xZ (record @507864b842). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: `check_en.py` (every criterion's instrument) and its fixtures. Decomposition v1.1 @53d221f334.
