# TO LGIC_ENFORCE.TO-EN-d-2 -- the second worker's search

<to_id>LGIC_ENFORCE.TO-EN-d-2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~8</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.1 @78128f29ea (ADMITTED) | **Decomp cell:** `EN-d-2` | **outcome_ref:** FWD-1 | **depends_on:** EN-d-1 (merged); a NEW spawn, never EN-d-1's worker | **slot:** ~8, queue position 2

---

## WORKER FACE

### THE CELL

`EN-d-2` -- the second worker's search (PRD candidate E11, its second half; FWD-1: *"by a second worker's search"*). You are NOT the worker that wrote the pipeline.

Read `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD7.md` for `scratch_branch`, the `generated` commit and `pipeline_path`. Search that file at that commit (`git show <commit>:<path>`) for every storage-location literal: a bucket name (`opal-data-...`), `s3://`, or a tier or key prefix (`bronze/`, `silver/`, `gold/`, `platinum/`). Print the denominator (files and lines searched). **Positive control:** plant one literal in a scratch copy of the file (never committed) and show that your search finds exactly one.

**Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD1_SEARCH.md`:** prose, then ONE fenced ```json block:
`{"pipeline": {"branch": "...", "commit": "...", "path": "..."}, "patterns": [...], "denominator": {"files": <n>, "lines": <n>}, "hits": [], "control": {"planted": "<the literal>", "hits": 1}}`

**Read:** EXERCISE_FWD7.md; the pipeline file at its commit.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="D2-AC1" cell_refs="EN-d-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py d2-zero</invocation><expect>VERDICT: PASS-ZERO-LITERALS</expect></criterion>
`D2-AC1` -- the pipeline holds no storage-location literal, by your search and by the checker's re-search.

<criterion id="D2-AC2" cell_refs="EN-d-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py d2-control</invocation><expect>VERDICT: PASS-CONTROL-FIRES</expect></criterion>
`D2-AC2` -- the search's positive control finds exactly one planted literal.

<expected_criteria>D2-AC1, D2-AC2</expected_criteria>

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
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/EXERCISE_FWD1_SEARCH.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v1.1 @53d221f334, cell `EN-d-2`.
<owned_cells>EN-d-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `D2-AC1`, `D2-AC2`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~8/LGIC_ENFORCE.TO-EN-d-2.fwd1-second-search.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> D2-AC1,D2-AC2` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `fwd1-second-search.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~8, queue position 2. Round 1 of LGIC_ENFORCE; issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974), leading the sequence on Andrew-direct ~16:3xZ (record @507864b842). Fixed inputs committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`: `check_en.py` (every criterion's instrument) and its fixtures. Decomposition v1.1 @53d221f334.
