# TO IRPT_ANLREQ.TO-AR-y-333.resident-r31-source-bindings-and-producer-list -- the resident release's SOURCE: the two queue bindings, the opal_map member and the one synthetic producer-list address (CTO msg 7767) with their tests; source and tests only, nothing deployed

<to_id>IRPT_ANLREQ.TO-AR-y-333</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~141</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; source and tests only, the worker deploys NOTHING)
**Decomp cell:** `AR-y-333` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-328` (merged `6cea17c760`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~141`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-141` (branch `wk-IRPT_ANLREQ-141`), provisioned by the issuer. Commit WORKSPACE files with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~141 <0.9.0_WK_IRPT_ANLREQ~141@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W141-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE repository. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH, no deploy, no upload, no apply, no invoke, no AWS call. Scratch outside the product tree.

### THE CELL (`AR-y-333`, inlined)

*The CTO ruled (msg 7767, C-SWITCH A') that ONE address is added to `OPAL_PRODUCER_PRINCIPALS` inside the single resident release that binds the three queues and the packager. The bindings read (`AR-y-328`, merged `6cea17c760`; record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~136/r41/RESIDENT_BINDINGS_READ.json`, read it first, especially `q1`, `q2`, `q4` and `recommendation`) lists what the release's SOURCE must change. This cell is that source change and its tests. The release BUILD (tarball, host scripts) is a later cell.*

1. **Read first** (under `C:/dev/wk-irpt-anlreq-141/infra/aws/lambda/investor-reporting/`): the record above; `reports/build_resident_package.py` (the `bindings` dict, about lines 81-98, the member list about line 100, and how it writes `reports/resident_bindings.json`); `reports/resident_installed.py` (the bindings factory: `analysis_ready_queue_url` about line 411, `commentary_ready_queue_url`/`package_queue_url` about line 424, the `packager` block about line 101, `opal_map` about lines 64 and 291-293, and the installer's second check about line 274); `ycharts/generate/resident_worker.py` (the producer list and its comment, about lines 159-177; the producer choice about line 748); `ycharts/generate/tests/test_resident_worker.py` (about line 770, the test that pins the one-entry tuple); the r19 recipe the row `IRPT_ANLREQ-D2-W136-S2` names (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/recipe_evidence/bin/write_record.py` line about 143 and `RESIDENT_RECIPE_AND_DELTA.json` line about 79: how the `opal_map` source and its sha256 were bound); and `infra/aws/terraform/transcripts/commentary.tf` plus the queue NAMES file the builder already reads (line about 84 of the builder: the URL form it uses), to take the queue NAMES.
2. **The change.**
   - (a) **Queue bindings.** `build_resident_package.py`'s `bindings` dict gains `analysis_ready_queue_url` and `commentary_ready_queue_url`, in the URL form the builder already uses for its other queue, with the queue NAMES from the same names source (never typed a second way). Read how `resident_installed.py` consumes each key and keep the key names it expects. `IRPT_ANALYSIS_READY_QUEUE_URL` is NOT added to the unit or any env: the factory sets it in-process.
   - (b) **The packager block is NOT in this cell.** The packager's `api_base` and `secret_name` have no declared source yet (the issuer asks the CTO); leave the `packager` binding exactly as it is and say so in the record.
   - (c) **The `opal_map` member.** The builder gains the `opal_map` binding (path and sha256) the way the r19 recipe bound it, so a listed principal's job is not refused `OPAL_MAP_BINDING_REQUIRED`: find the map file the r19 recipe names in tracked source; if it is not in the tracked tree, STOP on this limb with a BLOCKING row naming the file and what is missing, and finish (a) and (d).
   - (d) **The producer list.** `OPAL_PRODUCER_PRINCIPALS` becomes EXACTLY `("andrew@opalinvest.com", "fwd1-staff-r41a@opal.invalid")`. Its comment (about lines 159-164) is rewritten to state: the list holds Andrew's sign-in principal and ONE synthetic test principal for the FWD-1 run, a non-routable `@opal.invalid` name unique to that run and never reused; the second entry is a WIDENING ruled by the CTO (msg 7767, C-SWITCH A', 2026-10-14) and is removed in the next resident release after the FWD-1 run; a real staff filer still takes the YCharts path. Update the one test that pins the tuple (`test_resident_worker.py` about line 770) to the two-entry tuple, and add a test that `producer_for` returns "OPAL" for a record whose `owner.principal_id` is the new address and "YCHARTS" for `someone@opalinvest.com`.
3. **The tests** (NEW file `reports/tests/test_resident_r31_source.py`, or the folder the neighbouring builder tests live in; copy their style): (a) the bindings the builder writes carry `analysis_ready_queue_url` and `commentary_ready_queue_url` with the names from the names source, and the unit text the builder or installer writes does not contain `IRPT_ANALYSIS_READY_QUEUE_URL`; (b) the bindings carry the `opal_map` member (path and sha256 of the tracked map) or, if (c) was blocked, a test is NOT written for it; (c) `producer_for` for the new address is "OPAL" and for any other `@opal.invalid` or `@opalinvest.com` address is "YCHARTS"; (d) the list is exactly the two entries (the re-pinned assertion); (e) the installer's second check (`resident_installed.py` about line 274) accepts a record for the new address; (f) a test whose NAME states the scope: `the producer list holds Andrew and one synthetic test principal; a real staff filer takes the YCharts path`. `before_arm`: run the new tests on the base so (a), (c), (d), (f) FAIL.
4. **Commit** the source and tests; record the full sha and `git diff --stat <base> <commit>`.
5. **Write `r41/RESIDENT_R31_SOURCE_RECORD.json`**: `base`, `commit`, `files_changed`, `bindings_added` (the keys and where their values come from, with file:line), `opal_map` (what you bound and from where, or BLOCKED and why), `producer_list` (old, new), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `claim`, `not_read` (the live queues, the deployed tarball).
6. **Write the three checker scripts** named in ACCEPTANCE. In your report: the commit, the counts, the before-arm failures, the opal_map outcome.


### ACCEPTANCE

<criterion id="AR333-y-AC1" cell_refs="AR-y-333"><invocation>python C:/dev/wk-irpt-anlreq-141/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~141/tests_check.py</invocation><expect>^TESTS-OK </expect></criterion>
`AR333-y-AC1`: you write `tests_check.py`: it runs the new test file AND every test file in `ycharts/generate/tests/` and `reports/tests/` whose name contains `resident`, `producer`, `bindings`, `installed` or `build` (print the file list), parses the counts, and prints `TESTS-OK <new passed> new, <others passed> others, 0 failed` only when the new file has every case it has passing and the others have 0 failed; otherwise `TESTS-BAD <why>` and exit 1.

<criterion id="AR333-y-AC2" cell_refs="AR-y-333"><invocation>python C:/dev/wk-irpt-anlreq-141/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~141/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`AR333-y-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `ycharts/generate/resident_worker.py` to a scratch folder OUTSIDE the product tree with the list made one-entry again (the base shape), runs the new test file against the copy (copy first on the import path), and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="AR333-y-AC3" cell_refs="AR-y-333"><invocation>python C:/dev/wk-irpt-anlreq-141/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~141/scope_check.py</invocation><expect>SCOPE-OK</expect></criterion>
`AR333-y-AC3` (a third check, with a reason: the cell edits the resident's producer list, a widening ruled for ONE address): you write `scope_check.py`: it prints `SCOPE-OK` only when `git diff --name-only <base> HEAD` (`<base>` = the `base` field of your record JSON, printed) lists only `reports/build_resident_package.py`, `ycharts/generate/resident_worker.py`, `ycharts/generate/tests/test_resident_worker.py`, new test files under `reports/tests/` or `ycharts/generate/tests/`, a tracked `opal_map` file only if (c) required one, and paths under `org/missions/D9/IRPT/IRPT_ANLREQ/` (all under `infra/aws/lambda/investor-reporting/` for the source), AND `git diff <base> HEAD -- infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py` adds exactly one entry to the list and the comment lines (no other hunk); otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="AR333-y-AC4J" cell_refs="AR-y-333" judgment="true"/>
`AR333-y-AC4J` (judgment, graded at L9, never by you): the producer list gains exactly one non-routable synthetic address and its comment says so; the bindings carry the two queue URLs from the names source and the opal_map member or a named blocker; no real person's address was added; the packager binding is untouched.

<expected_criteria>AR333-y-AC1 AR333-y-AC2 AR333-y-AC3 AR333-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~141/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/reports/build_resident_package.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_r31_source.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_r31_source.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-333</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~141/IRPT_ANLREQ.TO-AR-y-333.resident-r31-source-bindings-and-producer-list.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-333`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR333-y-AC1,AR333-y-AC2,AR333-y-AC3,AR333-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and tests in a worktree; nothing is landed, pushed, deployed or called. The widening (one address on the producer list) is ruled by the CTO (msg 7767) and lands only in the resident release under a signed never-widen pair.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed by the worker; any route this cell adds is source only and is served only after a later signed release. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO ruling (msg 7767) and the bindings read against the cell; the lens: a second address, a routable address, a real person's address, an env variable the pre-read refuses, a queue name typed a second way, an opal_map assumed present. The cell requires exactly one `@opal.invalid` address, names from the names source, the in-process URL left out of the unit, an opal_map bound or blocked by name, and a before-arm that fails. NOT seen (blind): the live system and the deployed bytes; denominator: 6 test cases (a) to (f), 2 queue keys, 1 list entry.
</preflight>


---

## RECORD FACE

- Cut on the CTO's ruling msg 7767 (C-SWITCH A') and the bindings read (`AR-y-328`, merged `6cea17c760`). Workstream `ZS` of round 40. Base: `AR333-y-AC1`, `AC2`, `AC3` FAIL as expected (no checker files).
- The synthetic address `fwd1-staff-r41a@opal.invalid` is the issuer's choice under the CTO's conditions (non-routable, unique to this run, never reused); the FWD-1 run order mints that user. The packager binding (secret and principal row) waits on the CTO's answer to the issuer's question and is a later cell; the release BUILD is a later cell that consumes this cell and `AR-y-331`.
