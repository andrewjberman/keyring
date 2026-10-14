# TO IRPT_ANLREQ.TO-AR-y-336.resident-r31-commentary-queue-and-packager-bindings -- the resident bindings gain the commentary_ready queue and the packager block together (neither ships alone) and the one test that pinned their absence is re-pinned; source and tests only, nothing deployed

<to_id>IRPT_ANLREQ.TO-AR-y-336</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~143</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZV</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; source and tests only, the worker deploys NOTHING)
**Decomp cell:** `AR-y-336` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-333` (merged `6ad1e0d97a`), `AR-y-335` (merged `282fcafc77`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~143`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-143` (branch `wk-IRPT_ANLREQ-143`), provisioned by the issuer. Commit WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~143 <0.9.0_WK_IRPT_ANLREQ~143@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W143-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH, no deploy, no upload, no apply, no invoke, no AWS call. Scratch outside the product tree.

### THE CELL (`AR-y-336`, inlined)

*The CTO ruled (msg 7777) that this project builds the packager principal; the bindings read (`AR-y-328`), the packager door read (`AR-y-335`, merged `282fcafc77`; record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~142/r41/PACKAGER_DOOR_READ.json`, read it first: `q1`, `q4` and `resident_path_note`) and the first source cell (`AR-y-333`, merged `6ad1e0d97a`) left two keys out of the resident's bindings that must ship TOGETHER: `reports/resident_installed.py` (about lines 98-106) refuses a document that carries `commentary_ready_queue_url` without a `packager` block (`RESIDENT_PACKAGER_REQUIRED`). This cell adds both, and re-pins the one test that pinned their absence.*

1. **Read first** (under `C:/dev/wk-irpt-anlreq-143/infra/aws/lambda/investor-reporting/`): the two records above; `reports/build_resident_package.py` as `AR-y-333` left it (the `bindings` dict, how it takes the `analysis_ready_queue_url` from the queue NAMES source at its pin, the member list); `reports/resident_installed.py` (about lines 60-110: `PACKAGER_KEYS`, the `packager` block check, `RESIDENT_PACKAGER_REQUIRED`); `reports/tests/test_resident_package_imports.py` (the case `test_branch_a_without_commentary_ready_queue_url_resolves_every_import`, its `_bind` helper about line 102, and the branch-B case that passes) and `reports/tests/test_resident_packager_binding.py` (about lines 78-80, the refusal pin); `ycharts/research/opal_packager.py` (`live_ticket_ports`, about lines 259-345: the config keys `api_base`, `secret_name`, how `api_base` is used and the secret value shape `{"token": ...}`); `infra/aws/terraform/investor-reporting/ycharts/resident.tf` (about lines 160-175: the IAM statement whose ARN pattern the secret NAME must match); and the precedent of the shared API origin in `integrations/ticketing/intake/runner_config.json` (about line 6).
2. **The change (`reports/build_resident_package.py` and tests only):** (a) the `bindings` dict gains `commentary_ready_queue_url`, in the same URL form and from the same queue NAMES source as `analysis_ready_queue_url`; (b) the `bindings` dict gains the `packager` block with EXACTLY the keys `api_base` and `secret_name`: `secret_name` is `opal/ticketing/svc-irpt-packager` (a secret NAME, never a value or an ARN; it must match the IAM ARN prefix `opal/ticketing/svc-irpt-packager-??????` that `resident.tf` grants), and `api_base` is the https origin of the shared ticketing API that carries the package route, taken from the precedent value in `integrations/ticketing/intake/runner_config.json` as a NAMED constant with a comment citing that file and line and saying 'confirmed against the live API by TO-READ-R32 before the release is built'; (c) the document the builder writes loads through the INSTALLED factory's `load_bindings` (the packager shape check and the commentary-requires-packager rule both pass); (d) the branch-A case: keep branch A reachable if the builder already has a way to build the branch-A document (read how the branch-B case selects its document); if it has none, re-pin the one case honestly (the document now carries both keys, and an explicit control builds a document WITHOUT them and shows the factory refuses `RESIDENT_PACKAGER_REQUIRED` for a commentary key alone), and record case by case what it pinned before and now. No other existing test changes.
3. **The tests** (NEW file `reports/tests/test_resident_r31_packager_bindings.py`; copy the style of the neighbouring builder tests; run as the neighbours do, with MSYS_NO_PATHCONV=1 in any subprocess that builds, as the record of `AR-y-333` advises): (a) the built bindings carry `commentary_ready_queue_url` and the `packager` block with exactly `api_base` and `secret_name`; (b) the document passes `load_bindings`; (c) removing the `packager` block from that document makes `load_bindings` raise `RESIDENT_PACKAGER_REQUIRED`; (d) `secret_name` matches the resident.tf ARN prefix pattern (read the pattern from the Terraform text in the test, so a rename on either side fails) and `api_base` starts with `https://` and has no path; (e) the unit text the builder or installer writes still contains no `IRPT_ANALYSIS_READY_QUEUE_URL` and no token; (f) a test whose NAME states the scope: `the resident bindings carry the commentary queue and the packager block together; neither ships alone`. `before_arm`: run the new tests on the base so (a), (b), (d), (f) FAIL.
4. **Commit** the source and tests; record the full sha and `git diff --stat <base> <commit>`.
5. **Write `r41/RESIDENT_R31_PACKAGER_BINDINGS_RECORD.json`**: `base`, `commit`, `files_changed`, `bindings_added` (keys and the SOURCES of their values with file:line, never a secret value), `branch_a` (what you did and why), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `claim`, `build_note` (the MSYS note), `not_read` (the live API origin, the live secret, the deployed tarball).
6. **Write the three checker scripts** named in ACCEPTANCE. In your report: the commit, the counts, the before-arm failures, the branch-A decision.


### ACCEPTANCE

<criterion id="AR336-y-AC1" cell_refs="AR-y-336"><invocation>python C:/dev/wk-irpt-anlreq-143/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~143/tests_check.py</invocation><expect>^TESTS-OK </expect></criterion>
`AR336-y-AC1`: you write `tests_check.py`: it runs the new test file AND every test file in `reports/tests/` and `ycharts/generate/tests/` whose name contains `resident`, `packager`, `bindings`, `installed` or `build` (print the file list; one process per file, as the neighbours need), parses the counts, and prints `TESTS-OK <new passed> new, <others passed> others, 0 failed` only when the new file has every case passing and the others have 0 failed; otherwise `TESTS-BAD <why>` and exit 1.

<criterion id="AR336-y-AC2" cell_refs="AR-y-336"><invocation>python C:/dev/wk-irpt-anlreq-143/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~143/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR336-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `reports/build_resident_package.py` to a scratch folder OUTSIDE the product tree with the `packager` block removed (the commentary key kept), runs the new test file against the copy (copy first on the import path, with the siblings it needs), and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR336-y-AC3" cell_refs="AR-y-336"><invocation>python C:/dev/wk-irpt-anlreq-143/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~143/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR336-y-AC3` (a third check, with a reason: the cell edits the resident's bindings, which a signed release carries): you write `scope_check.py`: it prints `SCOPE-OK` only when `git diff --name-only <base> HEAD` (`<base>` = the `base` field of your record JSON, printed) lists only `reports/build_resident_package.py`, `reports/tests/test_resident_package_imports.py` (only if re-pinned), the new test file and paths under `org/missions/D9/IRPT/IRPT_ANLREQ/` (source paths under `infra/aws/lambda/investor-reporting/`), AND the diff of `build_resident_package.py` adds only the two binding keys, their named constants and comments; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR336-y-AC4J" cell_refs="AR-y-336" judgment="true"/>
`AR336-y-AC4J` (judgment, graded at L9, never by you): the resident's bindings carry the commentary queue and the packager block together, naming a secret (never a value) that matches the granted ARN pattern and a plain https origin, and no token or credential appears in any file.

<expected_criteria>AR336-y-AC1 AR336-y-AC2 AR336-y-AC3 AR336-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~143/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/reports/build_resident_package.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_package_imports.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_r31_packager_bindings.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-336</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~143/IRPT_ANLREQ.TO-AR-y-336.resident-r31-commentary-queue-and-packager-bindings.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-336`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR336-y-AC1,AR336-y-AC2,AR336-y-AC3,AR336-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and tests in a worktree; nothing is landed, pushed, deployed or called. The packager principal's grant is POST /tickets/{id}/package only; the resident release that carries these bindings is under a signed never-widen pair.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; any route this cell adds is source only and is served only after a later signed release. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO ruling (msg 7777) and the door read against the cell; the lens: a secret value or token anywhere in the source or tests, an ARN instead of a name, an api_base with a path, a commentary key shipped without the packager block, an existing test weakened rather than re-pinned. The cell requires a name matching the granted pattern, an https origin, both keys together, the factory's own loader accepting the document, and a before-arm that fails. NOT seen (blind): the live system and the deployed bytes; denominator: 6 test cases (a) to (f), 2 binding keys, 1 re-pinned case at most.
</preflight>


---

## RECORD FACE

- Cut on the CTO's ruling msg 7777, the door read (`AR-y-335`, merged `282fcafc77`) and the narrowing of `AR-y-333` (rows D2-W141-S1, S2). Workstream `ZV` of round 40. Base: `AR336-y-AC1`, `AC2`, `AC3` FAIL as expected (no checker files).
- The `api_base` constant is a precedent value confirmed live by `TO-READ-R32` before the release build. The secret's value is never read or written by this cell.
