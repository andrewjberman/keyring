# TO LGIC_ENFORCE.TO-EN-p-1 -- FWD-6 on a practice copy

<to_id>LGIC_ENFORCE.TO-EN-p-1</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.1 @78128f29ea (ADMITTED) | **Decomp cell:** `EN-p-1` | **outcome_ref:** FWD-6 | **depends_on:** EN-g-1 and EN-r-1 (merged) | **slot:** ~2, queue position 3

---

## WORKER FACE

### THE CELL

`EN-p-1` -- a clean-up cannot quietly stall (PRD candidate E10; DEC-8: *"A remediation is data"*).

**The planted surface, by rule, because this issuance precedes EN-c-1's run:** take `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/CARRIER_CENSUS.md`'s carriers sorted by (path, line). The first whose `token` `grade(token, "S3Key")` marks OUT-OF-PATTERN is the SURFACE. State the rule's result.

On a practice copy (below):
1. Plant ONE `remediations.json` row: a fictitious remediation project owning that surface. Commit it on the scratch branch. That commit is `plant`.
2. Edit the surface so that it TOUCHES the old-style string without removing it. Run `python .tools/naming-gate.py --enforce --diff <that git diff>` and save its output: it must REFUSE, naming the surface. Discard the edit.
3. Edit the surface so that it REMOVES the string. Run the gate the same way and save its output: it must PASS.

The two edits are graded as diffs and never committed, because the surface's lane would refuse a commit before the naming stage could speak.

- **Practice copy.** Create it as `git worktree add -b prac-lgic-enforce-p1 <WS>/../prac-lgic-enforce-p1 HEAD`, on a scratch branch that is NEVER pushed. Commit the exercise there, so its hashes are the evidence. When done, `git worktree remove` the CLEAN practice copy. Leave the scratch BRANCH in place: deleting an unmerged branch is destructive git. Your slot branch carries only your records.

**Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD6.md`:** prose, then ONE fenced ```json block:
`{"scratch_branch": "...", "surface": "<path>", "planted_row": {...}, "commits": {"plant": "<hash>"}, "outputs": {"refused": "<the gate's output, verbatim>", "passed": "<the gate's output, verbatim>"}}`

**Read:** CARRIER_CENSUS.md; lib/opal_naming.py; .tools/naming-gate.py; the registry.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="P1-AC1" cell_refs="EN-p-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py p1-surface</invocation><expect>VERDICT: PASS-SURFACE-BY-RULE</expect></criterion>
`P1-AC1` -- the surface is the one the rule selects.

<criterion id="P1-AC2" cell_refs="EN-p-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py p1-refused</invocation><expect>VERDICT: PASS-REFUSED</expect></criterion>
`P1-AC2` -- the touching diff is refused, naming the surface.

<criterion id="P1-AC3" cell_refs="EN-p-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py p1-passed</invocation><expect>VERDICT: PASS-REMOVAL-PASSES</expect></criterion>
`P1-AC3` -- the removing diff passes.

<criterion id="P1-AC4" cell_refs="EN-p-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py p1-branch</invocation><expect>VERDICT: PASS-EVIDENCE-ON-BRANCH</expect></criterion>
`P1-AC4` -- the planted-row commit is on the scratch branch.

<expected_criteria>P1-AC1, P1-AC2, P1-AC3, P1-AC4</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds the issuer's files: `check_en.py` (the checker every criterion calls), its fixtures under `tests/`, and `g1_preimage/`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform apply. Any live read is read-only through the `aws` shim.
- **Practice copy.** Create it as `git worktree add -b prac-lgic-enforce-p1 <WS>/../prac-lgic-enforce-p1 HEAD`, on a scratch branch that is NEVER pushed. Commit the exercise there, so its hashes are the evidence. When done, `git worktree remove` the CLEAN practice copy. Leave the scratch BRANCH in place: deleting an unmerged branch is destructive git. Your slot branch carries only your records.

<paths>
infra/logic/registry/remediations.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD6.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v1.1 @53d221f334, cell `EN-p-1`.
<owned_cells>EN-p-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `P1-AC1`, `P1-AC2`, `P1-AC3`, `P1-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-p-1.fwd6-practice.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> P1-AC1,P1-AC2,P1-AC3,P1-AC4` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fwd6-practice.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~2, queue position 3. Round 1 of LGIC_ENFORCE; issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974), leading the sequence on Andrew-direct ~16:3xZ (record @507864b842). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: `check_en.py` (every criterion's instrument) and its fixtures. Decomposition v1.1 @53d221f334.
