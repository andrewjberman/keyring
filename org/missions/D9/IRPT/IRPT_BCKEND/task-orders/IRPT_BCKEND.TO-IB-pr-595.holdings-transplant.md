# TO IRPT_BCKEND.TO-IB-pr-595 -- READ the TRANSPLANT release candidates of the three per-firm holdings bundles: each firm's minting-pin file with ONLY the exemption commits applied (no one-date bypass, the CUSIP port as the pin has it), BUILD ONLY, tested offline, compared with the live bundles; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-595</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~434</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~PJ</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the finding that IB-pr-590's overlay candidate also ships the unreleased one-date bypass (IB-pr-536) and reverses 49 Financial's CUSIP port, on the CTO's round analysis @57266eeb77 (the exemption pair moves the exemption alone) | **Decomp cell:** `IB-pr-595` (decomposition section 222) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-434`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~434 <0.9.0_WK_IRPT_BCKEND~434@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`). Use `python -I` only for files you do not trust; your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array (the union merge of the drain then duplicates the rows it did not touch).

**Cell `IB-pr-595` (inlined).** IB-pr-590 (record `deliverables/0.9.0_WK_IRPT_BCKEND~431/IB224-1_holdings_overlay_candidate.json`, merged) overlaid HEAD's whole `holdings_snapshot.py` and `publication.py` on each firm's MINTING pin and proved the exemption tests pass. But HEAD's `holdings_snapshot.py` is not the minting pin's file plus the exemption: it also carries (a) the unreleased ONE-DATE BYPASS of IB-pr-536 (`allow_older_date`, the `ONE-DATE-ASSERT` block, the `--allow-older-date` argument: a manual-path flag whose sign-off is NOT part of the exemption pair) for all three firms, and (b) for 49 Financial, the REVERSAL of the CUSIP port (`cusip_key` and `classify_security(..., security_id=...)`: commits `5fad7eaaa8` and `de08782c38` undid it for pin 2; pin 1, the 49 Financial pin, keeps it LIVE on purpose) and a `multi_asset` list change. The never-widen pair must move the exemption ALONE. This cell builds the TRANSPLANT candidate: each firm's minting-pin file with ONLY the exemption changes applied. Nothing is minted, uploaded, deployed or invoked.

**READ FIRST (named files only):** the IB-pr-590 record and harness (`deliverables/0.9.0_WK_IRPT_BCKEND~431/IB224-1_holdings_overlay_candidate.json` and `ib224_1_overlay_candidate.py`: reuse its pin-worktree set-up, the BUILD ONLY builder call and the live comparison, in a copy in YOUR deliverables folder), `.tools/safe_deploy_core.py`, and the git history of the two files between the pins and the overlay pin: `git log --format='%h %an %s' <minting pin>..fa2502c5b116dba01a3f7b2522f5f0e6b107b821 -- data/assets/scripts/gold/investor_reporting/holdings_snapshot.py infra/aws/lambda/investor-reporting/holdings/publication.py`. The EXEMPTION commits are the ones authored by `0.9.0_WK_IRPT_BCKEND~419`, `~420` and `~424` (IB-pr-576, 577 and 582; at least `b1f767053e`, `1b184295b6`, `738bf3d07f`, `1ad921000c`, `381be2ca6c`); the NON-exemption commits (for example `15e0361375` IB-pr-536, `de08782c38`, `5fad7eaaa8`) must NOT be applied.

**Do, per firm (three firms):**
1. A full detached worktree of the firm's MINTING pin OUTSIDE the repository (`b1d354cfc9341168a3b4c316a344876ce0049b97` for 49financial; `5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f` for Cottonwood and Inflection), sparse checkout disabled in that worktree alone (as IB-pr-589 and 590 did).
2. **Transplant:** apply to that worktree's `holdings_snapshot.py` and `publication.py` ONLY the changes of the exemption commits, in order (for example `git diff <commit>^ <commit> -- <the two paths> | git apply --3way` in the pin worktree, or an equivalent you can describe). A conflict is resolved by keeping the minting pin's text outside the exemption blocks and keeping the exemption's blocks and plumbing lines in; every conflict is counted and described in the notes. Do NOT take any hunk of a non-exemption commit.
3. **Verify the transplant:** (a) strip every `ABSENT-AT-SOURCE-A`, `-B` and `-C` block (BEGIN to END lines) from the transplanted `holdings_snapshot.py` and diff it against the minting pin's file: the remaining differing lines are the exemption's PLUMBING (the gate's new argument, the `COT_SILVER_ROOT` constant and its use, the fingerprint helper, the call-site line breaks); count them as `foreign_diff_lines` and describe them in `foreign_diff_reading` (60+ characters: name each group of lines); it must be 40 or fewer and contain no hunk of the bypass or the CUSIP port; (b) `allow_older_date` and `ONE-DATE-ASSERT` are ABSENT from the transplanted file (`one_date_bypass_absent` true); (c) `cusip_key` is present for 49financial and absent for Cottonwood and Inflection (`cusip_port_present`).
4. **Commit the two transplanted files per firm** under YOUR deliverables folder as `transplant/<firm>/holdings_snapshot.py` and `transplant/<firm>/publication.py` (the check recomputes their sha256 from those committed files).
5. Build each firm's bundle BUILD ONLY from the pin worktree with the two transplanted files in place (twice, identical members), download the LIVE bundle read-only and compare member by member: the changed members must be EXACTLY the two files; `members_equal_to_live` is `members_total` minus 2.
6. **Run the offline tests on each transplant tree.** Copy into the tree (tests are not bundle members) from the overlay pin: `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py`, `test_absent_at_source_exemption.py`, `test_absent_at_source_receipts.py`, `test_holdings_publish_gate.py` and `infra/aws/lambda/investor-reporting/holdings/tests/test_publication.py`; do NOT run `test_holdings_bypass_one_date.py` (it tests the bypass that is not shipped). Run with `python -m pytest -q -p no:cacheprovider` from the tree root. Record `overlay_tests` = `{"passed":n,"failed":0}`. A failing test is the finding: name it in a row and in the record's notes, with whether it tests a feature the pin lacks (then say which test you excluded and why, in the notes) or the exemption itself (then STOP on that firm).

**Record shape** (`IB228-1_holdings_transplant_candidate.json`): `"overlay_pin":"fa2502c5b116dba01a3f7b2522f5f0e6b107b821"`, `"firms"` for `49financial`, `cottonwood`, `inflection` with, per firm: `minting_pin`, `live_bundle_sha256`, `candidate_bundle_sha256`, `members_total`, `members_equal_to_live`, `changed_members` = two entries `{"repo_path":"<the repository path>","artifact":"org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~434/transplant/<firm>/<file name>","sha256_transplanted":"<sha256 of that committed file>"}`, `transplant` = `{"one_date_bypass_absent":true,"cusip_port_present":<bool>,"foreign_diff_lines":n,"foreign_diff_reading":"..."}`, `overlay_tests`.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~434/IB228-1_holdings_transplant_candidate.json`: the JSON object described above, plus `"base_commit":"<40hex: git rev-parse HEAD at your first act>"`, `"read_date":"<today ISO>"`, `"method":"<120+ characters: exactly what you ran, in what order, and the two arms>"`, `"claim":"measured"`, `"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added]` and the six counters, all 0: `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB228-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB228-1-AC1" cell_refs="IB-pr-595"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r228/p228_cells.py" . IB228-1-AC1</invocation><expect>IB228-1-AC1 PASS</expect></criterion>
<criterion id="IB228-1-AC2" cell_refs="IB-pr-595"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r228/p228_cells.py" . IB228-1-AC2</invocation><expect>IB228-1-AC2 PASS</expect></criterion>
<criterion id="IB228-1-AC3" cell_refs="IB-pr-595"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r228/p228_cells.py" . IB228-1-AC3</invocation><expect>IB228-1-AC3 PASS</expect></criterion>

<expected_criteria>IB228-1-AC1, IB228-1-AC2, IB228-1-AC3</expected_criteria>

What the checks grade: AC1 the identity and the pins; AC2 per firm (a different candidate hash, the changed members EXACTLY holdings_snapshot.py and publication.py, each transplanted file committed and its sha256 recomputed, the one-date bypass absent, the CUSIP port present for 49 Financial and absent for the others, 40 or fewer changed lines outside the exemption blocks with a reading of 60+ characters, every other member equal to the live bundle's); AC3 per firm the offline tests on the transplant tree (passed at least 1, failed 0), notes of 30+ characters, the six counters 0, no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W434-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~434/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 222 (round 4, workstream ~PJ), cell `IB-pr-595`.
<owned_cells>IB-pr-595</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB228-1-AC1, IB228-1-AC2, IB228-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~434/IRPT_BCKEND.TO-IB-pr-595.holdings-transplant.proof_of_spec.json`.
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
comp-adversary: RUN -- the check IB228-1 dry-run at base on dell2 2026-10-15 ~16:1xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (a git root holding the members at a commit, a synthetic record; removed): all three PASS; sixteen negatives each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~434` (worktree `C:/dev/wk-IRPT_BCKEND-434`). Class SERVED (a read of served artifacts and a build).
</preflight>
