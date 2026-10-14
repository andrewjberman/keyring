# TO IRPT_BCKEND.TO-IB-pr-544 -- VERIFY release pin 2 (the closure-fix pin plus the reverse of the CUSIP port): the bundle imports clean, the closure equals the trace, and the bundle differs from the closure-fix pin's by exactly holdings_snapshot.py (CTO round-197 ruling 2)

<to_id>IRPT_BCKEND.TO-IB-pr-544</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~389</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>197</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-197 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_ROUND_197_20261014.md` | **Decomp cell:** `IB-pr-544` (decomposition section 189) | **outcome_ref:** FWD-3 | **Depends on:** none (pin 2 is committed by the issuer)

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-389`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~389 <0.9.0_WK_IRPT_BCKEND~389@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, object names, field names, classification labels and public security symbols only in any tracked file; no account id, client id, node id, quantity or holding name; the largest delta is a NUMBER with its field name and no id. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch389/`); a recursive delete the harness refuses is left and named in your report.

**Cell `IB-pr-544` (inlined).** The CTO's round-197 ruling: the release ships the cash rule WITHOUT the CUSIP port (`01e843ce2e`), which becomes its own release. **Pin 2 already exists** (the issuer committed it, because a worker cannot commit on a tree that lacks its order): `new_pin` = `5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f` on branch `pin2-ib-pr-544`, a single commit on `b1d354cfc9341168a3b4c316a344876ce0049b97` (the closure-fix pin) that applies the round-196 hand-resolved CUSIP toggle to `holdings_snapshot.py` (the file's blob goes 3a19dcf591 to ed3cf609a7; 3 lines added, 20 removed). **This order verifies pin 2 mechanically and packages the proof; it mints, uploads, applies and signs NOTHING.**

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`. `git diff --numstat b1d354cfc9341168a3b4c316a344876ce0049b97 5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f` must read exactly one file, `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, and `.tools/safe_deploy_core.py` must be byte-equal at the two pins.
2. **Build the bundles at both pins, no upload.** `git worktree add --detach C:/dev/wk-ib544-pin 5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f` and `git worktree add --detach C:/dev/wk-ib544-base b1d354cfc9341168a3b4c316a344876ce0049b97`. From each tree (its own `.tools` first on `sys.path`, `import safe_deploy_core as core`): for `irpt_holdings_49f`, `irpt_holdings_cot`, `irpt_holdings_inf` call `core.find_bundle(name)` then `core.build_bundle_payload(b)` and untar into `C:/dev/_scratch389/pin2/<firm>/` and `C:/dev/_scratch389/base/<firm>/`. `bundle_delta` = the member comparison by sha256 of each member's bytes (the generated `SHA256SUMS` index excluded and named in `notes`): `members_changed` must be exactly `["data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"]`, `members_added` and `members_removed` both `[]`.
3. **The import proof (under `python -I`, per firm).** For EVERY `.py` member of the closure (the closure is the same at both pins), in a clean interpreter `python -I -c "<code>"` where the code inserts into `sys.path` the pin-2 extracted tree's member directories and `<tree>/lib` and then does `import <module stem>`. Record per firm `{"python_flags":"-I","members_imported":[every .py closure member path],"import_errors":[..],"bundle_tree_members":<files in the tree, the closure plus SHA256SUMS>}`. An ImportError is a FAIL: record it and report.
4. **The closure equals the traced import set, both ways.** As in IB-pr-540 (`deliverables/0.9.0_WK_IRPT_BCKEND~385/`, READ its record and scripts for the method): a clean `python -I` process on the extracted PIN-2 tree per firm with `sys.addaudithook` recording every file opened under the tree and a real read-only build `holdings_snapshot.build_snapshot(firm, VersionedInputs(boto3 s3 client), as_of)` (custody pins: 49financial 2026-10-12, cottonwood 2026-10-12, inflection 2026-10-13; get/list calls only), collecting files under the tree that appear in `sys.modules` or in the open events. `closure_vs_trace` = `{"traced_files":[..],"missing":[],"extra":[{"path","import_site":"<closure member>:<line>"}]}`; `missing` must be empty; each `extra` carries an import site the check reads at pin 2.
5. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~389/IB197-1_pin2_record.json`: `{"base_commit":"<40hex>","base_pin":"b1d354cfc9341168a3b4c316a344876ce0049b97","new_pin":"5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f","import_proof":{..},"closure_vs_trace":{..},"bundle_delta":{..},"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB197-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove the worktrees and scratch you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB197-1-AC1" cell_refs="IB-pr-544"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-1-AC1</invocation><expect>IB197-1-AC1 PASS</expect></criterion>
<criterion id="IB197-1-AC2" cell_refs="IB-pr-544"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-1-AC2</invocation><expect>IB197-1-AC2 PASS</expect></criterion>
<criterion id="IB197-1-AC3" cell_refs="IB-pr-544"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py" . IB197-1-AC3</invocation><expect>IB197-1-AC3 PASS</expect></criterion>

<expected_criteria>IB197-1-AC1, IB197-1-AC2, IB197-1-AC3</expected_criteria>

What the checks grade: AC1 pin 2 is the recorded hash, descends from b1d354cfc9, changes only `holdings_snapshot.py`, leaves the closure file byte-equal, its subject names the reverted port, and its added and removed lines EQUAL the round-196 cusip toggle diff (`deliverables/0.9.0_WK_IRPT_BCKEND~387/toggle_cusip_fallback.diff`); AC2 for each firm `python -I`, every `.py` closure member listed as imported, no import error; AC3 the traced files in the closure (missing none), each extra with a verifiable import site, a bundle delta of exactly `holdings_snapshot.py` changed, the six bound counters 0 and no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktrees and the scratch directory outside the repository. READ ONLY. **Nothing is minted, invoked, written to AWS, uploaded, applied, deployed, signed or sent:** the only AWS calls are `s3api get-object` on live bundle keys by version id and the harness's get/list reads with your identity. A denial is recorded, never worked around or widened. (AWS CLI goes through the `.tools/aws` shim.)
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a bundle delta other than `holdings_snapshot.py` changed; an ImportError at pin 2; a traced file outside the closure that you cannot explain; a client identifier or node id in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W389-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~389/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 189 (round 197, workstream ~P), cell `IB-pr-544`.
<owned_cells>IB-pr-544</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB197-1-AC1, IB197-1-AC2, IB197-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~389/IRPT_BCKEND.TO-IB-pr-544.verify-release-pin-2-without-the-cusip-port.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order builds the three bundle payloads in memory at pin 2 and at the closure-fix pin, extracts them to scratch and runs real read-only builds from the extracted pin-2 trees; no bundle is minted, so no served byte moves
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p197_cells.py IB197-1 dry-run at base on dell2 2026-10-14 ~22:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a throwaway git repo the run created itself (a base pin, a pin 2 whose diff is saved as the toggle diff; synthetic records; removed): all three PASS; seven negatives across IB197-1, each failing its own arm: a member left unimported, an ImportError recorded, a traced file outside the closure, a bundle delta of two changed members, a bundle delta that adds a member, a stray file in pin 2, a closure change in pin 2.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~389` (worktree `C:/dev/wk-IRPT_BCKEND-389`). Class LOCAL (builds in scratch and reads a served source read-only; no served byte, no infra path).
</preflight>
