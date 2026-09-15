# TO LGIC_ENFORCE.TO-EN-d-1-r2 -- FWD-7 again: a new firm is one row, and draws no warning

<to_id>LGIC_ENFORCE.TO-EN-d-1-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~5</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-d-1` (round 2) | **outcome_ref:** FWD-7 | **depends_on:** EN-r-6 round 2 (merged) | **slot:** ~5, queue position 1

---

## WORKER FACE

### THE CELL

`EN-d-1` -- firm N+1 is one row (PRD candidate E11; DEC-9), again after RULING ONE: in round 1 the row alone regenerated every view but still drew a warning that the firm was not in the schema's second list (row W8-S2). The fictitious firm is FIXED: long form `quillwater`, short form `qwt`. It is never pushed and never `demo`.

On a practice copy (below):
1. **Compute the expected diff set FIRST,** from the generator's per-view declarations: every generated file that must change when one scope row is added. Write it to `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/expected_diff.r2.txt` and COMMIT it on the scratch branch. That commit is `expected_set`.
2. Add ONE `scopes.json` row for `quillwater`/`qwt`, run `python lib/opal_naming.py generate --out .`, and commit. That commit is `generated`. The actual diff, less the registry itself, must equal the expected set exactly. Save `python lib/opal_naming.py validate`'s output at `generated`.
3. A hand-typed ADDRESS for the firm (for example `opal-data-quillwater/silver/x`) in a new config file, run through `naming-gate.py --enforce --diff`: REFUSED. Save the output.
4. A hand-typed occurrence of the firm's NAME (`quillwater` or `qwt`) as a dict key in a new config map, run the same way: REFUSED. Save the output.

**Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD7_R2.md`:** prose, then ONE fenced ```json block
`{"scratch_branch": "...", "firm": {"long": "quillwater", "short": "qwt"}, "commits": {"expected_set": "<hash>", "generated": "<hash>"}, "expected_files": [...], "actual_files": [...], "outputs": {"hand_address_refused": "...", "hand_name_refused": "...", "validate": "..."}}`.
Round 1's `EXERCISE_FWD7.md` stays as its record.

- **Practice copy.** Create it as `git worktree add -b prac-lgic-enforce-d1-r2 <WS>/../prac-lgic-enforce-d1-r2 HEAD`, on a scratch branch that is NEVER pushed. Commit the exercise there, so its hashes are the evidence. When done, `git worktree remove` the CLEAN practice copy. Leave the scratch BRANCH in place: deleting an unmerged branch is destructive git. Your slot branch carries only your records.

**Read:** the registry; `lib/opal_naming.py` (`generate`, the per-view declarations); `.tools/naming-gate.py`; the generated views.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="D1R-AC1" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py d1r-firm</invocation><expect>VERDICT: PASS-R2-FIXED-FIRM</expect></criterion>
`D1R-AC1` -- the exercise uses the fixed fictitious firm.

<criterion id="D1R-AC2" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py d1r-order</invocation><expect>VERDICT: PASS-R2-EXPECTED-FIRST</expect></criterion>
`D1R-AC2` -- the expected-set commit precedes the generator's commit.

<criterion id="D1R-AC3" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py d1r-diff-equal</invocation><expect>VERDICT: PASS-R2-DIFF-EQUALS-EXPECTED</expect></criterion>
`D1R-AC3` -- the generator's actual diff equals the expected set.

<criterion id="D1R-AC4" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py d1r-zero-warnings</invocation><expect>VERDICT: PASS-NEW-FIRM-DRAWS-NO-WARNING</expect></criterion>
`D1R-AC4` -- the new row draws no validate warning (the checker validates the registry at both recorded commits).

<criterion id="D1R-AC5" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py d1r-address-refused</invocation><expect>VERDICT: PASS-R2-ADDRESS-REFUSED</expect></criterion>
`D1R-AC5` -- a hand-typed address for the firm is refused.

<criterion id="D1R-AC6" cell_refs="EN-d-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py d1r-name-refused</invocation><expect>VERDICT: PASS-R2-NAME-REFUSED</expect></criterion>
`D1R-AC6` -- a hand-typed occurrence of the firm's name in a config map is refused.

<expected_criteria>D1R-AC1, D1R-AC2, D1R-AC3, D1R-AC4, D1R-AC5, D1R-AC6</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform apply.
- **The wide grant is for the PRACTICE COPY ONLY.** The registry, the carriers and the module in `<paths>` are there so the scratch branch can commit the generator's output. Your slot branch commits only your records. Anything else on it is a defect the drain refuses.

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
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD7_R2.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-d-1`, round 2 (section 0b).
<owned_cells>EN-d-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `D1R-AC1`, `D1R-AC2`, `D1R-AC3`, `D1R-AC4`, `D1R-AC5`, `D1R-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~5/LGIC_ENFORCE.TO-EN-d-1-r2.fwd7-demo-firm.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> D1R-AC1,D1R-AC2,D1R-AC3,D1R-AC4,D1R-AC5,D1R-AC6` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fwd7-demo-firm.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~5, queue position 1. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
