# TO IRPT_ANLREQ.TO-AR-y-441.o1-upload-door-lambda-rebuild-v2-served-py-and-ticket-confirmation -- BUILD ONLY: rebuild the upload-door Lambda irpt-ycharts-generate (r37 version 2) with TWO movers against the live package: _authz/served.py (the O1 scratch pin, unchanged) and ycharts/generate/ticket_confirmation.py (AR-y-440, so a Ticket Center filing is ticket_confirmed); nothing is uploaded, applied or run

<to_id>IRPT_ANLREQ.TO-AR-y-441.o1-upload-door-lambda-rebuild-v2-served-py-and-ticket-confirmation</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~319</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ100</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-441` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a staff filing takes the Opal producer; the owner falls back), C-SWITCH | **depends_on:** AR-y-426 (r37 version 1, merged 1f7fb64f3c2; its zip 51dc323c... is superseded and never uploaded), AR-y-440 (merged 57fbab70491, the confirm fix at commit 752e87d46b73b8d92dc638a1040a17ad359dcfd8), CTO msg 11206 item 2

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~319`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-319` (branch `wk-IRPT_ANLREQ-319`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~319 <0.9.0_WK_IRPT_ANLREQ~319@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W319-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-441`, inlined)

*Context.* The upload door is the Lambda `irpt-ycharts-generate` (handler `generate_installed.lambda_handler`, 107 members, live CodeSha256 `kxOEgpbspky10PYWQ28y0+7V2UXG28whJ2riMa4CkTE=`; the issuer's read of the live members is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/o1_release/LIVE_IRPT_YCDGEN_MEMBERS_20261020.json`). Version 1 of this release (AR-y-426, your predecessor's tools in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/`: `r37_build.py`, `check_r37.py`, the record `R37_BUILD.json`) moved ONE member, `served.py`, through the function map's `staged_from` entry (its pin is already `720e125d31469ed60b6e698812c7be731bd6d8e8` at trunk HEAD). The run-5C finding (see the order of AR-y-440) adds a SECOND mover: `ycharts/generate/ticket_confirmation.py`, which the function map also stages from a pin (`staged_from` entry with `repo_path` `infra/aws/lambda/investor-reporting/ycharts/generate/ticket_confirmation.py`, `packaged_as` `ticket_confirmation.py`, today `pin` `a0da937b3e77da89a0f8d8ad224e25585246b3a2`, `sha256` `073cc83143040487cb70af52db4dd977b7a42b5f9c196c07e0dcfa9ccc4fbabd`, which EQUALS the live member). AR-y-440 changed the file (commit `752e87d46b73b8d92dc638a1040a17ad359dcfd8`, now merged; the blob at that commit has sha256 `e76593c7951a2949a42ba78dba85aa45a8eaa4a5633fe58f0e636291b2c5dc6d`): `confirm` also returns True for an `analysis_request` ticket created through `/tickets` whose `created_by` equals the principal.

*What to do.*
1. **Pins.** Print `git rev-parse 752e87d46b73b8d92dc638a1040a17ad359dcfd8` (it must read `752e87d46b73b8d92dc638a1040a17ad359dcfd8`; else STOP and file a BLOCKING row), `git show 752e87d46b73b8d92dc638a1040a17ad359dcfd8:infra/aws/lambda/investor-reporting/ycharts/generate/ticket_confirmation.py | sha256sum` (it must read `e76593c7951a2949a42ba78dba85aa45a8eaa4a5633fe58f0e636291b2c5dc6d`) and `git rev-parse HEAD`. Create `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/` first.
2. **The one map edit.** In `infra/aws/lambda/ci/function-map/irpt-ycharts-generate.json`, in the `staged_from` entry whose `packaged_as` is `ticket_confirmation.py`, change TWO values and nothing else: `pin` to `752e87d46b73b8d92dc638a1040a17ad359dcfd8` and `sha256` to `e76593c7951a2949a42ba78dba85aa45a8eaa4a5633fe58f0e636291b2c5dc6d`. Print `git grep -n 073cc8314304 -- infra/aws/lambda/ci` before and after: any OTHER place naming the old sha256 is reported in a row and not edited. Commit it ALONE with a subject that begins `pin(IRPT_ANLREQ TO-AR-y-441,` (this commit is the PIN of the build). `git diff --numstat HEAD~1 HEAD` must show exactly `2 2` on that one file.
3. **The tools.** Copy `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/r37_build.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/r37/check_r37.py` into `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/` and change ONLY: in `r37_build.py` the printed tags to `R37V2-BUILD-OK` and `R37V2-BUILD-BAD` and the docstring's names; in `check_r37.py` the three modes' expectations and tags as below. Everything else stays (two builds with a private TMPDIR, the identical-bytes refusal, the comparison with `census.build_members` at the pin). Both pass `bash .tools/commit-gate.sh`.
4. **Run the build** at the step-2 commit (up to 590000 ms; the stage folder `C:/dev/irpt-release-r37o2` must NOT exist): `python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/r37_build.py --pin <the step-2 full sha> --out C:/dev/irpt-release-r37o2 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/R37V2_BUILD.json`. The last line must begin `R37V2-BUILD-OK`; on `R37V2-BUILD-BAD <why>` or a traceback file ONE row with it and the last 20 lines, change nothing, report.
5. **Smoke of the BUILT package** (private temp folder you create and remove; `python -I`, that folder as the only extra `sys.path` entry): print whether `import served` and `import generate_installed` both succeed (exception class and first line if not), and then BEHAVIOUR: `import ticket_confirmation`, build `make_confirm_ticket(fake, "tickets")` with an in-memory `fake.get_item` and print `confirm_created_by=<true|false>` for a ticket item `{ticket_type: analysis_request, source: portal, created_by: <principal>, requester: {email: someone else}}` confirmed for `<principal>` (it must be true) and `other=<true|false>` for a different principal (it must be false). Record the lines in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/IMPORT_SMOKE.txt`.
6. **The checker** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/check_r37.py` (stdlib only, ruff clean), three modes, each printing ONE final line:
   - `diff <record> <live-members.json>`: compares the BUILT zip's member sha256 map with the live members file and prints `R37V2-DIFF-OK moved=2 added=0 removed=0 same=105 movers=served.py,ticket_confirmation.py` ONLY when the non-SAME set is exactly those two as MOVED, the built `served.py` sha256 equals `600a934c4b34da1e14ec8b7d4de4a3f69cc55c331257dd90abb525def9929fcd` and the built `ticket_confirmation.py` sha256 equals `e76593c7951a2949a42ba78dba85aa45a8eaa4a5633fe58f0e636291b2c5dc6d`; otherwise `R37V2-DIFF-BAD <why naming every other mover>` and exit 1 (an extra mover is the issuer's decision: do not suppress it).
   - `identity <record> <smoke-file>`: prints `R37V2-IDENTITY-OK builds_identical=yes import_served=ok import_generate_installed=ok confirm_created_by=true other=false` ONLY when the record shows the two builds byte-identical and the smoke file shows exactly those results.
   - `map` (no argument): finds the step-2 commit itself with `git log --format=%H --grep='^pin(IRPT_ANLREQ TO-AR-y-441,' -1` and prints `R37V2-MAP-OK numstat=2/2 pin=752e87d46b73 sha256=e76593c79519` ONLY when `git diff --numstat <commit>~1 <commit>` is exactly one file, `infra/aws/lambda/ci/function-map/irpt-ycharts-generate.json`, with `2 2`, and the `pin` and `sha256` of the `ticket_confirmation.py` entry at the commit equal the values of step 2; otherwise `R37V2-MAP-BAD <why>` and exit 1.
   Its `--selftest` runs the `diff` mode on a copy of the record with a third member's hash altered and prints `CONTROL-FIRES` only when that copy yields `R37V2-DIFF-BAD`.
7. **Run, save, commit.** Save the outputs next to the record (`DIFF.txt`, `IDENTITY.txt`, `MAP.txt`, `SELFTEST.txt` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/`), commit the record, then the tools and outputs, as separate commits (the map edit is already its own commit). Write the proof instance (shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~314/IRPT_ANLREQ.TO-AR-y-426.o1-upload-door-lambda-build-served-py-live-plus-o1-only.proof_of_spec.json`; `controls.mutant` = the diff mode on the altered record copy must print `R37V2-DIFF-BAD`; `controls.determinism` = the two builds identical) and flip on VALID with all three PASS.
8. **Report** the step-2 commit sha, the build's last line, the zip's sha256, CodeSha256 and size, the three checker lines, the smoke lines, and any extra mover with its commit subject.

---

## ACCEPTANCE

<criterion id="AR441-y-AC1" cell_refs="AR-y-441"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/check_r37.py diff org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/R37V2_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/o1_release/LIVE_IRPT_YCDGEN_MEMBERS_20261020.json</invocation><expect>^R37V2-DIFF-OK moved=2 added=0 removed=0 same=105 movers=served.py,ticket_confirmation.py</expect></criterion>
<criterion id="AR441-y-AC2" cell_refs="AR-y-441"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/check_r37.py identity org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/R37V2_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/IMPORT_SMOKE.txt</invocation><expect>^R37V2-IDENTITY-OK builds_identical=yes import_served=ok import_generate_installed=ok confirm_created_by=true other=false$</expect></criterion>
<criterion id="AR441-y-AC3" cell_refs="AR-y-441"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/r59/check_r37.py map</invocation><expect>^R37V2-MAP-OK numstat=2/2 pin=752e87d46b73 sha256=e76593c79519$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/IRPT_ANLREQ.TO-AR-y-441.o1-upload-door-lambda-rebuild-v2-served-py-and-ticket-confirmation.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-441.o1-upload-door-lambda-rebuild-v2-served-py-and-ticket-confirmation`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR441-y-AC1,AR441-y-AC2,AR441-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-441</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/ci/function-map/irpt-ycharts-generate.json
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~319/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-441.o1-upload-door-lambda-rebuild-v2-served-py-and-ticket-confirmation.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a build in a stage folder outside the repository, one map edit commit and tool copies in the worker deliverables; nothing is uploaded, applied or run on a host.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the AR-y-426 cell and record against this cell; the lens: a second mover riding the staged pins (extra movers are reported, not suppressed), the AC3 invocation that names HEAD (row W314-S2: it now finds the commit by subject), a build that passes its delta and import gates and is wrong (the behavioural smoke of the built ticket_confirmation), the stage folder inside the repository. NOT seen (blind): the live Lambda; denominator: three criteria.
</preflight>
