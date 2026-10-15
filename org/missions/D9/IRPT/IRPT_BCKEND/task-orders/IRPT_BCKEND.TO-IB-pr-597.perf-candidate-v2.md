# TO IRPT_BCKEND.TO-IB-pr-597 -- READ the REBUILT release candidate of the 49 Financial performance function at the current HEAD (with the named ratio-absent manifest list of IB-pr-592): BUILD ONLY with a candidate source map, compared with the live package member by member; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-597</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~435</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~PJ</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO half of the 49 Financial split pair (condition 3, the manifest names the ratio-absent days) on the merged builds IB-pr-578, 583 and 592 | **Decomp cell:** `IB-pr-597` (decomposition section 224) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-435`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~435 <0.9.0_WK_IRPT_BCKEND~435@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/irpt_holdings_performance/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`). Use `python -I` only for files you do not trust; your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array (the union merge of the drain then duplicates the rows it did not touch).

**Cell `IB-pr-597` (inlined).** IB-pr-585 (record `deliverables/0.9.0_WK_IRPT_BCKEND~427/IB221-1_perf_candidate.json`, merged @5bdf4f810a) built the release candidate of `irpt-holdings-performance-lambda` carrying the 49 Financial split adjustment: digest `fvmE5j1hkNA16csMEtB3/WydmovkAucF/AmBxLCIqEg=`, 2 of 14 members moved. The CTO signed the split pair on the condition (its item 3) that the served manifest NAMES the ratio-absent security-days by security and day; IB-pr-592 (merged @f005060a06) builds that (`SPLIT-ADJUST-C` blocks in `holdings_performance.py`), so the candidate must be REBUILT at the current HEAD and the pair re-issued on its new digest. This cell rebuilds it, BUILD ONLY, and compares it with the live package and with the first candidate. It uploads, deploys and invokes nothing. The method, the bounds and the record are IB-pr-585's, restated below (the worker's own earlier harness and candidate-map writer sit in `deliverables/0.9.0_WK_IRPT_BCKEND~427/`: read and reuse them in a copy in YOUR deliverables folder).

**READ FIRST (named files only):** `deliverables/0.9.0_WK_IRPT_BCKEND~312/make_candidate_map.py` (the method: a writer of a candidate source map that re-pins chosen `staged_from` rows to a commit with the sha256 recomputed from `git show`; READ it, do not edit it; write your own `make_candidate_map_perf.py` in YOUR deliverables folder from it, re-pinning ONLY the rows of function `irpt-holdings-performance-lambda` whose `repo_path` is one of the two members), `deliverables/0.9.0_WK_IRPT_BCKEND~408/IB205-1_ycharts_generate_rebuild_v2.json` (its `notes` give the build line: `BUILD_ONLY=1 BAU_SOURCE_MAP_OVERRIDE=<map> TMPDIR=<scratch> bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-holdings-performance-lambda`, from the worktree at the base, scratch OUTSIDE the repository), `infra/aws/lambda/ci/build-and-upload.sh` and the source map entry of the function.

**Do:**
1. `git rev-parse HEAD` is your base and your pin (it carries both merges). `aws lambda get-function-configuration` for `irpt-holdings-performance-lambda`: CodeSha256 must equal `o9UugRAVhYmF3Q2ULtU6eaaNiLFRAFWW4tjjQPyj2Ok=`; any other value (another release landed first): STOP and file a row. Download the live zip with `get-function` (read-only) into scratch and check its sha256 equals that CodeSha256.
2. Write the candidate map and build twice (BUILD ONLY; the two zips must be byte-identical; the real source map file is NOT edited). The candidate's CodeSha256 must differ from the live one.
3. Compare the candidate zip's members with the live zip's, member by member (name, sha256). `moved_members` = the names that differ or are added or removed. The two members must be among them. Any OTHER moved member is named with a reason of 30+ characters in `extra_moved_reasons` (for example "a member the live package carries at an older pin than the trunk map" with its name): this is the silent-revert and drift guard, and an unexplained extra is a STOP.
4. For each of the two members record `repo_path`, `pin`, `sha256_now` (the sha256 of the file at the pin by `git show`), and for the producer `split_blocks_a` and `split_blocks_b` (the counts of `BEGIN SPLIT-ADJUST-A` and `BEGIN SPLIT-ADJUST-B` lines at the pin) and for `sources.json` `split_adjust_declared` true.

**Record shape** (`IB230-1_perf_candidate.json`): `"function":"irpt-holdings-performance-lambda"`, `"live_codesha256"`, `"override_map_used":true`, `"candidate":{"codesha256":"<base64>","moved_count":n,"total_members":n,"moved_members":[names]}`, `"members":{"holdings_performance.py":{"repo_path","pin","sha256_now","split_blocks_a","split_blocks_b"},"sources.json":{"repo_path","pin","sha256_now","split_adjust_declared":true}}`, `"siblings_unmoved":["irpt-inf-holdings-performance-lambda","irpt-cot-holdings-performance-lambda"]`, `"extra_moved_reasons":{}`.


**Also record** `"previous_candidate_codesha256":"fvmE5j1hkNA16csMEtB3/WydmovkAucF/AmBxLCIqEg="` and, in the notes, that the new candidate differs from it and why (the `SPLIT-ADJUST-C` blocks of IB-pr-592: `holdings_performance.py` carries them, counted in a `split_blocks_c` field of its member entry).

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~435/IB230-1_perf_candidate.json`: the JSON object described above, plus `"base_commit":"<40hex: git rev-parse HEAD at your first act>"`, `"read_date":"<today ISO>"`, `"method":"<120+ characters: exactly what you ran, in what order, and the two arms>"`, `"claim":"measured"`, `"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added]` and the six counters, all 0: `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB230-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB230-1-AC1" cell_refs="IB-pr-597"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r230/p230_cells.py" . IB230-1-AC1</invocation><expect>IB230-1-AC1 PASS</expect></criterion>
<criterion id="IB230-1-AC2" cell_refs="IB-pr-597"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r230/p230_cells.py" . IB230-1-AC2</invocation><expect>IB230-1-AC2 PASS</expect></criterion>
<criterion id="IB230-1-AC3" cell_refs="IB-pr-597"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r230/p230_cells.py" . IB230-1-AC3</invocation><expect>IB230-1-AC3 PASS</expect></criterion>

<expected_criteria>IB230-1-AC1, IB230-1-AC2, IB230-1-AC3</expected_criteria>

What the checks grade: AC1 the identity (base commit, read date, the live CodeSha256 the issuer read, a NEW candidate digest built with the override map, the two members among the moved ones); AC2 the members at their pins (sha256 recomputed from git, the split blocks present, the declaration present, the pin an ancestor of HEAD, siblings left unmoved, any extra moved member named with a reason); AC3 notes of 30+ characters, the six counters 0, no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W435-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~435/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 224 (round 5, workstream ~PJ), cell `IB-pr-597`.
<owned_cells>IB-pr-597</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB230-1-AC1, IB230-1-AC2, IB230-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~435/IRPT_BCKEND.TO-IB-pr-597.perf-candidate-v2.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a BUILD-ONLY candidate and read-only downloads of the live artifact; nothing is uploaded, minted, deployed, invoked or written to AWS; the record carries hashes, counts and member names only. The never-widen pair that uses it, and its apply, are later acts.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use this box's existing credentials.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- the check IB230-1 dry-run at base on dell2 2026-10-15 ~16:1xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (a git root holding the members at a commit, a synthetic record; removed): all three PASS; nine negatives each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~435` (worktree `C:/dev/wk-IRPT_BCKEND-435`). Class SERVED (a read of served artifacts and a build).
</preflight>
