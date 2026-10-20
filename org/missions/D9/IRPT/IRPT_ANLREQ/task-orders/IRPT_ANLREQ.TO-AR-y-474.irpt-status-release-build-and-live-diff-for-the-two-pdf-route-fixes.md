# TO IRPT_ANLREQ.TO-AR-y-474.irpt-status-release-build-and-live-diff-for-the-two-pdf-route-fixes -- BUILD ONLY: build the irpt-status package twice at the trunk commit that carries the commentary-PDF route fix (AR-y-470) and the Overview-PDF route fix (AR-y-472), and diff its members one by one against the issuer's record of the LIVE zip: exactly one mover, `owned_report.py`; nothing is uploaded, planned or applied

<to_id>IRPT_ANLREQ.TO-AR-y-474.irpt-status-release-build-and-live-diff-for-the-two-pdf-route-fixes</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~348</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ133</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (a served Lambda's package; the worker builds only) | **Decomp cell:** `AR-y-474` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 and FWD-9 (both reports open from the ticket) | **depends_on:** AR-y-470 (trunk d8497f8adc5), AR-y-472 (trunk 06cb0e999d7), the build and diff tools of worker 291 (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~348`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-348` (branch `wk-IRPT_ANLREQ-348`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~348 <0.9.0_WK_IRPT_ANLREQ~348@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W348-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **BUILD ONLY.** No upload, no plan, no apply, no invoke, no AWS call of any kind, no network, no push. NO file under `infra/` is changed by this order. The stage folder is OUTSIDE the repository and is yours (`C:/dev/irpt-release-r37`); it must not exist when you start; never `rm -rf` a folder you did not create. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (the live_diff `--selftest`) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR474-y-AC1,AR474-y-AC2,AR474-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-474`, inlined)

*Context.* The LIVE irpt-status package (CodeSha256 `274dl2bCd2VC3OcX4Uqc4AMbWep65B97F1+CVNoKfMc=`, 49 members, handler `status_installed.lambda_handler`, LastModified 2026-10-17T16:41:08Z, zip 368788 bytes) was read by the issuer on 2026-10-20 and each member hashed: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261020.json` (a `members` list of `{name,size,sha256}`, 49 entries). Its `owned_report.py` is the pre-fix route code. Trunk now carries two changes to that member: AR-y-470 (`commentary_pdf` binds by logical id and signs the PDF's own sha, drained d8497f8adc5) and AR-y-472 (`pdf` resolves the retained Opal Overview PDF through the artifact binding when `release.protected_pdf_ref` is absent, drained 06cb0e999d7). `owned_report.py` is packaged straight from the source dir `infra/aws/lambda/investor-reporting/ops` (function map `infra/aws/lambda/ci/function-map/irpt-status.json`, `source_dir` and `files`), so NO map edit is needed. Worker 291's tools (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/r36s_build.py` and `live_diff.py`, record `R36S_BUILD.json`, outputs `LIVE_DIFF.txt`) did the same job for release r36s: copy their shape.

1. **Pin and base.** Print `git rev-parse HEAD` (the base) and confirm `git merge-base --is-ancestor 06cb0e999d7707a5d918e724305b74c0dbcecd2d HEAD` exits 0. Print `git show 06cb0e999d7707a5d918e724305b74c0dbcecd2d:infra/aws/lambda/investor-reporting/ops/owned_report.py | sha256sum` (call it OR_SHA; the built `owned_report.py` must equal it). Print `git diff --name-only 06cb0e999d7707a5d918e724305b74c0dbcecd2d HEAD -- infra/aws/lambda/investor-reporting/ops infra/aws/lambda/ci` (it must print NOTHING: the build tree at HEAD must carry the same package inputs as 06cb0e999d7; if it prints a path, STOP with a BLOCKING row naming it). Create `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51` first.
2. **Build tool.** Copy `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/r36s_build.py` to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/r37_build.py`, rename the printed tags to `R37-BUILD-OK` and `R37-BUILD-BAD`, and change nothing else except what the new pin needs (its docstring states the lineage). Passes `bash .tools/commit-gate.sh`.
3. **Run the build** at HEAD (command `timeout` 590000 ms; the stage folder must not exist): `python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/r37_build.py --pin <the full HEAD sha printed in step 1> --out C:/dev/irpt-release-r37 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/R37_BUILD.json`. The last line must begin `R37-BUILD-OK`; on `R37-BUILD-BAD <why>` or any traceback file ONE row with it and the last 20 lines, change nothing, report: do not edit other tools or retry with other arguments.
4. **Live diff.** Copy `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~291/r50/live_diff.py` to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/live_diff.py` and adapt it (stdlib only, run with `python -I`): arguments `<record> <live-members.json>`; it prints `BUILT sha=<code_sha256> members=<n>`, `LIVE sha=<code_sha256> members=<n>`, then ONE line per member of the union, sorted: `SAME|MOVED|ADDED|REMOVED <name> built=<sha12|-> live=<sha12|->`; for each non-SAME name it prints `git log --oneline 90b69dcb12cdfedc786966ab33d034bf14229396..HEAD -- <repo_path>` using the function map entry (as the tool already does). It opens `<stage>/irpt-status.zip` and checks (a) the built `owned_report.py` sha256 equals OR_SHA of step 1, (b) its text contains the AR-y-472 marker `-overview-` in the `pdf` method and the AR-y-470 form (`retained_sha` used as the argument of `signer.sign` in `commentary_pdf`), and (c) its text no longer contains the old comparison `retained.get("sha256") != sha`. Final line `LIVE-DIFF-OK moved=1 added=0 removed=0 same=48 mover=owned_report.py has_commentary_fix=yes has_overview_fallback=yes` ONLY when the non-SAME set is exactly `{owned_report.py: MOVED}` and (a), (b), (c) hold; otherwise `LIVE-DIFF-BAD <why naming every other mover>`, exit 1 (an extra mover is the issuer's decision, not yours: do not suppress it). Its `--selftest` runs the same checks on a copy of the record in which a second member's hash is altered and prints `CONTROL-FIRES` only when that copy yields `LIVE-DIFF-BAD`.
5. **Run both, save, commit.** Save `live_diff.py`'s output to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/LIVE_DIFF.txt` and the selftest's to `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/SELFTEST.txt`. Commit the record, then the tools and outputs, as separate commits.
6. **Report** the base sha, the tool's last line, the zip's sha256, CodeSha256 and size, the `LIVE-DIFF-OK` or `-BAD` line, and any mover other than `owned_report.py` with its commit subjects.

---

## ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR474-y-AC1" cell_refs="AR-y-474"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/live_diff.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/R37_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261020.json</invocation><expect>LIVE-DIFF-OK moved=1 added=0 removed=0 same=48 mover=owned_report.py has_commentary_fix=yes has_overview_fallback=yes</expect></criterion>
<criterion id="AR474-y-AC2" cell_refs="AR-y-474"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/live_diff.py --selftest org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/r51/R37_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261020.json</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR474-y-AC3" cell_refs="AR-y-474"><invocation>git diff --name-only 06cb0e999d7707a5d918e724305b74c0dbcecd2d HEAD -- infra | wc -l</invocation><expect>^0$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/IRPT_ANLREQ.TO-AR-y-474.irpt-status-release-build-and-live-diff-for-the-two-pdf-route-fixes.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-474.irpt-status-release-build-and-live-diff-for-the-two-pdf-route-fixes`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR474-y-AC1,AR474-y-AC2,AR474-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-474</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write; nothing under `infra/`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~348/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-474.irpt-status-release-build-and-live-diff-for-the-two-pdf-route-fixes.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a package build in a throwaway stage folder outside the repository and tools and records in the worker deliverables; nothing is uploaded, planned, applied, invoked or pushed; no infra file changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the issuer's live read (49 members, zip sha256 dbbe1d97...), the map's source_dir and files list, and the two drained route commits against this cell; the lens: a second member riding the build (the diff must name it, not hide it), a built owned_report.py that is not the blob of the pinned commit, a diff against the build pin instead of the LIVE record, a build tree at HEAD that differs from the pinned commit in a package input, a control that cannot fail, an upload or apply by the worker. NOT seen (blind): any apply, any live request; denominator: 49 live members, one build, 3 mechanical criteria.
</preflight>
