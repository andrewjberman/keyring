# TO IRPT_ANLREQ.TO-AR-y-392.irpt-status-acceptance-pin-move-build-and-live-diff -- the function map's staged pin for irpt-status's acceptance.py moves from 361c44fa9d to 06557b6618 (the commit that adds get_commentary_ref), the package is built twice at that new commit, and its members are diffed one by one against the recorded live zip: exactly one mover, acceptance.py; BUILD ONLY, nothing uploaded, planned or applied

<to_id>IRPT_ANLREQ.TO-AR-y-392</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~291</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ53</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: the function map of a served Lambda and its package; the worker builds only, uploads and applies nothing)
**Decomp cell:** `AR-y-392` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the ticket's commentary PDF opens) | **depends_on:** worker 290's record (`TO-AR-y-391`, rows `W290-S1` and `W290-S2`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~291`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-291` (branch `wk-IRPT_ANLREQ-291`), provisioned by the issuer from the current branch (sparse: `.tools/`, `lib/`, `infra/`, `data/`, `docs/`, `org/standards/`, the project folder and the release-35 tool folder). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~291 <0.9.0_WK_IRPT_ANLREQ~291@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. A row id has the form `IRPT_ANLREQ-D2-W291-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `INVESTIGATION_v1.md` (0 deletions). Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (ruff clean: no single-letter names `l`, `O`, `I`). No non-ASCII in what you add.
- **BUILD ONLY.** No upload, no plan, no apply, no invoke, no AWS call of any kind, no network, no push. The ONE file you may change under `infra/` is `infra/aws/lambda/ci/function-map/irpt-status.json` (step 2, two values). The stage folder is OUTSIDE the repository. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-y-392`, inlined)

*Context. The LIVE irpt-status package (CodeSha256 `+TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A=`, 49 members) packages `acceptance.py` at the zip root WITHOUT `get_commentary_ref`, so `ops/owned_report.py` (lines 350 to 373) refuses `COMMENTARY_PDF_NOT_RETAINED` and the ticket's commentary PDF will not open. Worker 290 (`TO-AR-y-391`) built the package at HEAD and found it reproduces the live zip exactly (49 of 49 members same, the stage zip's CodeSha256 equal to the live one) because the function map stages `acceptance.py` from the older pin `361c44fa9d40992c8cacfd625cc789536f84b920` (sha256 `06425d4731b7d6e90b86b0001c2f2cb0449acb61023be54ae7018c35aa001faa`), whose blob has no `get_commentary_ref`; its tool also stopped at a baseline step (`CensusError: function 'irpt-status' is not in the source map at 927337a741`). The CTO (msg 10600) authorized the release: acceptance.py must carry `get_commentary_ref`; any other mover must be justified. The issuer's ruling for the pin: move it to `06557b6618` (IRPT_BCKEND IB-pr-478, 2026-10-12, the commit that adds `get_commentary_ref`), the smallest step that carries it; the blob at that commit is 11,034 bytes with sha256 `0c4acec625b7da70da82efccf58cc967e9e5bf53c32e955d67079b711701513d`. The module differs from the old pin only by `get_commentary_ref` and the write-side `accept(..., acting_principal_id)` change (a writer the status Lambda never calls: no production file under `ops/` or the status members calls `.accept(`; the only caller is `ops/tests/test_owned_requests.py`). Imports are unchanged.*

1. **Pin and base.** Print `git rev-parse 06557b6618` (it must equal a 40-hex; print it and use it below) and `git show 06557b6618:infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py | sha256sum` (it must read `0c4acec625b7da70da82efccf58cc967e9e5bf53c32e955d67079b711701513d`; any other value: STOP and file a row). Print `git rev-parse HEAD` (the base). Create `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50` first.
2. **The one map edit.** In `infra/aws/lambda/ci/function-map/irpt-status.json`, in the `files` entry whose `packaged_as` is `acceptance.py`, change TWO values and nothing else: `pin` to the full 40-hex of `06557b6618` and `sha256` to `0c4acec625b7da70da82efccf58cc967e9e5bf53c32e955d67079b711701513d`. Print `git grep -n "361c44fa9d40992c8cacfd625cc789536f84b920\|06425d4731b7d6e90b86b0001c2f2cb0449acb61023be54ae7018c35aa001faa" -- infra/aws/lambda/ci` before and after: the other entries that legitimately keep pin `361c44fa9d` (for example `retention.py`) stay; any OTHER place that names acceptance.py's old sha256 is reported in a row and not edited. Commit it ALONE (this commit is the PIN for the build). Print its full sha. `git diff --numstat HEAD~1 HEAD` must show exactly `2 2` on that one file.
3. **Write the build tool** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/r36s_build.py`: copy `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r35/r35l_build.py` and remove ONLY the baseline comparison (the block that sets `deployed = STATUS_BASELINE`, checks it is an ancestor, builds `base` and computes `delta`) and set the record's `delta_vs_deployed_commit` to an empty list and `deployed_commit` to `null`, and rename the printed tags `R36S-BUILD-OK` and `R36S-BUILD-BAD`. Keep everything else: two builds with a private TMPDIR, the identical-bytes refusal, the comparison with `census.build_members` at the pin. State in the file's docstring that the baseline step was removed because the census cannot read the old pin's source map and that the live comparison is `live_diff.py`'s. The tool passes `bash .tools/commit-gate.sh`.
4. **Run the build** at the step-2 commit (command `timeout` 590000 ms; the stage folder must not exist): `python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/r36s_build.py --pin <the step-2 full sha> --out C:/dev/irpt-release-r36s2 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/R36S_BUILD.json`. The last line must begin `R36S-BUILD-OK`; on `R36S-BUILD-BAD <why>` or any traceback file ONE row with it and the last 20 lines, change nothing, report: do not edit other tools or retry with other arguments.
5. **Write `r50/live_diff.py`** (stdlib only, run with `python -I`): arguments `<record> <live-members.json>` where the live file is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261017.json` (a `members` list of `{name,size,sha256}`; the record's `functions.irpt-status.member_sha256` is a name to sha256 map). It prints `BUILT sha=<code_sha256> members=<n>`, `LIVE sha=<code_sha256> members=<n>`, then ONE line per member of the union, sorted: `SAME|MOVED|ADDED|REMOVED <name> built=<sha12|-> live=<sha12|->`, then for each non-SAME name the commits that moved it since the live build pin: resolve the member's repository path from the function map at the step-2 commit (`git show <commit>:infra/aws/lambda/ci/function-map/irpt-status.json`; entries pair `repo_path` with `packaged_as`) and print `git log --oneline 90b69dcb12cdfedc786966ab33d034bf14229396..<commit> -- <repo_path>` (empty: `NO-COMMIT-SINCE-90b69dcb12`). It then opens `<stage>/irpt-status.zip` and checks that the built `acceptance.py` contains the text `def get_commentary_ref`, and that the built acceptance.py sha256 equals `0c4acec625b7da70da82efccf58cc967e9e5bf53c32e955d67079b711701513d`. Final line `LIVE-DIFF-OK moved=1 added=0 removed=0 same=48 mover=acceptance.py acceptance_has_get_commentary_ref=yes` ONLY when the non-SAME set is exactly `{acceptance.py: MOVED}` and both text checks hold; otherwise `LIVE-DIFF-BAD <why naming every other mover>`, exit 1 (an extra mover is the issuer's decision, not yours: do not suppress it). Its `--selftest` runs the same checks on a copy of the record in which a second member's hash is altered and prints `CONTROL-FIRES` only when that copy yields `LIVE-DIFF-BAD`.
6. **Run both, save, commit.** Save `live_diff.py`'s output to `r50/LIVE_DIFF.txt` and the selftest's to `r50/SELFTEST.txt`. Also save `git grep -n "\.accept(" <step-2 commit> -- infra/aws/lambda/investor-reporting/ops infra/aws/lambda/investor-reporting/reports` to `r50/ACCEPT_CALLERS.txt` (the expected callers are tests only; any non-test caller in a file that the irpt-status package contains is a FINDING: say so). Commit the record, then the tools and outputs, as separate commits (the map edit is already its own commit).
7. **Report** the step-2 commit sha, the tool's last line, the zip's sha256, CodeSha256 and size, the `LIVE-DIFF-OK` or `-BAD` line, the movers with their commit subjects, and `ACCEPT_CALLERS.txt`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR392-y-AC1" cell_refs="AR-y-392"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/live_diff.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/R36S_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261017.json</invocation><expect>LIVE-DIFF-OK moved=1 added=0 removed=0 same=48</expect></criterion>
`AR392-y-AC1`: exactly one mover, acceptance.py, carrying `get_commentary_ref`; at base (no script, no record) it FAILS.

<criterion id="AR392-y-AC2" cell_refs="AR-y-392"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/live_diff.py --selftest org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/R36S_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261017.json</invocation><expect>CONTROL-FIRES</expect></criterion>
`AR392-y-AC2`: the control: with a second member's hash altered the diff must reject.

<criterion id="AR392-y-AC3" cell_refs="AR-y-392"><invocation>git log -n 1 --format= --numstat -- infra/aws/lambda/ci/function-map/irpt-status.json</invocation><expect>^2\s2\sinfra/aws/lambda/ci/function-map/irpt-status\.json$</expect></criterion>
`AR392-y-AC3` (a third check, with a reason: the map edit must be exactly two lines): the last commit that touches the map file changed exactly 2 lines added and 2 removed. Also record in `r50/MAP_EDIT.txt` the output of `git diff --name-only <the base HEAD printed in step 1> HEAD -- infra`, which must list only that one file.

<criterion id="AR392-y-AC4J" cell_refs="AR-y-392" judgment="true"/>
`AR392-y-AC4J` (judgment, graded at L9, never by you): the map edit is exactly the pin and sha256 of acceptance.py; the build is of that commit, built twice identically; exactly acceptance.py moves and it is the blob of `06557b6618`; no production file in the package calls `accept(`; nothing was uploaded, planned, applied or pushed; and the record says plainly what it did not read.

<expected_criteria>AR392-y-AC1 AR392-y-AC2 AR392-y-AC3 AR392-y-AC4J</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, the deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/`, this order's file (status flip only), and the ONE infra file `infra/aws/lambda/ci/function-map/irpt-status.json` (two values). BUILD ONLY. The stage folder `C:/dev/irpt-release-r36s2` is outside the repository and is yours; leave `C:/dev/irpt-release-r36s` and `-r36sb` (worker 290's) untouched.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane or by a gate: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.

<paths>
infra/aws/lambda/ci/function-map/irpt-status.json
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-392</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/IRPT_ANLREQ.TO-AR-y-392.irpt-status-acceptance-pin-move-build-and-live-diff.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-392`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR392-y-AC1,AR392-y-AC2,AR392-y-AC3,AR392-y-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a two-value edit of a function map in a worktree and a package build in a throwaway worktree with a stage folder outside the repository; nothing is uploaded, planned, applied, invoked or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by worker 290's build and its two BLOCKING rows (the build reproduces the live package because the map stages acceptance.py from an older pin; the build tool stops at a baseline step the old pin cannot answer), the issuer's blob read (361c44fa9d 9,393 bytes without the function, 06557b6618 11,034 bytes with it, imports unchanged) and the grep of accept( callers against the cell; the lens: a pin moved too far (HEAD's blob carries two more commits), a second member riding the map edit, a mover with no commit behind it, a diff that compares against the build pin instead of the LIVE zip, a control that cannot fail, a writer change shipping into a reader-only Lambda. The cell requires exactly one mover, the blob hash of the named commit, the callers read, and a control that fires. NOT seen (blind): any apply, any live request; denominator: 49 live members, one build, 3 mechanical criteria.
</preflight>

---

## RECORD FACE

- Cut after worker 290 (`TO-AR-y-391`, closed as superseded by this order) found that the map's staged pin is the cause. The CTO's authorization is msg 10600; the pin choice is the issuer's ruling inside the CTO's terms ("acceptance.py must carry get_commentary_ref, and any other mover is justified"). Workstream `ZZ53` of round 43. Base: `r50/`, the stage folder and the edit commit are absent, so `AR392-y-AC1` and `AC2` FAIL as expected.
- After the worker: the issuer re-runs the checks, writes the never-widen packet (pin = the worker's edit commit, movers, blast radius, apply protocol, rollback to the prior artifact version) and sends the CTO the packet sha; the apply is `0.7.0_AE_CloudOps~IB2`'s (plan 0/1/0 on irpt-status code only, outside the weekday 11:30Z to 14:15Z band, an after-read that a commentary route answers 200 with a body for a synthetic request).
