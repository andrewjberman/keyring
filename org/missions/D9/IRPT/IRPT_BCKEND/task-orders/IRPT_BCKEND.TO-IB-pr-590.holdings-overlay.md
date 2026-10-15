# TO IRPT_BCKEND.TO-IB-pr-590 -- READ the OVERLAY release candidates of the three per-firm holdings bundles: each firm's minting pin with only holdings_snapshot.py and publication.py overlaid, BUILD ONLY, proven offline, compared with the live bundles; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-590</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~431</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~PJ</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round analysis @57266eeb77 (msg 8435: the exemption and the receipts ship under a never-widen pair) and the finding of IB-pr-589 (six unrelated closure members drifted since the minting pins) | **Decomp cell:** `IB-pr-590` (decomposition section 219) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-431`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~431 <0.9.0_WK_IRPT_BCKEND~431@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`). Use `python -I` only for files you do not trust; your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array (the union merge of the drain then duplicates the rows it did not touch).

**Cell `IB-pr-590` (inlined).** IB-pr-589 (record `deliverables/0.9.0_WK_IRPT_BCKEND~428/IB222-1_holdings_bundles_candidate.json`, merged) built the three per-firm holdings bundles from the current HEAD and compared them with the live bundles IB-pr-549 minted: besides `holdings_snapshot.py` and `publication.py` (the two files IB-pr-576, 577 and 582 changed), SIX unrelated closure members differ, because other projects' commits landed since the minting pins (`dim_mdpf_aggregate_aua_timeseries.py`, `dim_mdpf_aum_metrics.py`, `mdpf_category_registry.py` from MDPF_CANON; `infra/logic/registry/exemptions.json` and `lib/opal_naming.py` from the registry owner; `infra/logic/registry/reporting_policies.json` from IB-pr-553). Shipping them would widen the never-widen pair beyond the exemption. This cell builds the MINIMAL candidate: each firm's bundle from its MINTING pin with ONLY `holdings_snapshot.py` and `publication.py` overlaid from the current HEAD, BUILD ONLY, and PROVES offline that the two overlaid files run on the minting-pin versions of everything else. Nothing is minted, uploaded, deployed or invoked.

**READ FIRST (named files only):** the record and harness of IB-pr-589 (`deliverables/0.9.0_WK_IRPT_BCKEND~428/IB222-1_holdings_bundles_candidate.json` and `ib222_1_holdings_candidate.py`: read the harness and REUSE its builder call, in a copy in YOUR deliverables folder), `.tools/safe_deploy_core.py` (the bundle builder and the declarations of the three bundles), and the IB-pr-549 order's minting pins (49financial `b1d354cfc9341168a3b4c316a344876ce0049b97`; Cottonwood and Inflection `5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f`).

**Do, per firm (three firms):**
1. `git rev-parse HEAD` is your base and the OVERLAY PIN (it carries the merges: `holdings_snapshot.py` there holds the `ABSENT-AT-SOURCE-A`, `-B` and `-C` blocks).
2. Make a full detached worktree of the firm's MINTING pin OUTSIDE the repository (`git worktree add --detach <scratch>/<firm> <minting pin>`). **Disable sparse checkout in THAT worktree alone** (the shared repository config sets `core.sparseCheckout`; the pin worktree then lacks its closure: use `git -C <wt> config --worktree core.sparseCheckout false` after enabling worktree config, as IB-pr-589's row W428-S1 did). Overlay exactly two files into it from the overlay pin by `git show <overlay pin>:<path> > <wt>/<path>`: `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` and `infra/aws/lambda/investor-reporting/holdings/publication.py`. Nothing else is copied.
3. Build the firm's bundle from that overlay tree BUILD ONLY (the harness's builder call; NEVER an upload). Build twice: identical member names and sha256 (the tarball bytes may differ by timestamp: say so).
4. Download the firm's LIVE bundle read-only; compare member by member with the candidate. **The changed members must be EXACTLY the two overlaid files; every other member must equal the live bundle's.** `members_total` is the closure count and `members_equal_to_live` is `members_total` minus 2. Any other difference is a STOP and a row (it means the live bundle is not the minting pin's content; IB-pr-589 measured 138 of 138 equal).
5. **Run the offline tests on the overlay tree.** Copy into the overlay tree (tests are not bundle members) from the overlay pin: `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py`, `test_absent_at_source_exemption.py`, `test_absent_at_source_receipts.py`, `test_holdings_publish_gate.py`, `test_holdings_bypass_one_date.py` and `infra/aws/lambda/investor-reporting/holdings/tests/test_publication.py`, then run them with `python -m pytest -q -p no:cacheprovider` from the overlay tree root (with its own directories on the path as the repository's tests expect). Record `overlay_tests` = `{"passed":n,"failed":0}`. A failure is the finding: it means the new code needs a drifted member; do NOT patch, STOP on that firm, file a row naming the failing test and the import or call, and write the record with the failure.

**Record shape** (`IB224-1_holdings_overlay_candidate.json`): `"overlay_pin":"<40 hex>"`, `"firms":{"49financial":{...},"cottonwood":{...},"inflection":{...}}` with, per firm: `minting_pin` (the pin stated above for that firm), `live_bundle_sha256`, `candidate_bundle_sha256`, `members_total`, `members_equal_to_live`, `changed_members` = `[{"repo_path":"data/assets/scripts/gold/investor_reporting/holdings_snapshot.py","sha256_at_pin":"<sha256 of that file at the overlay pin>"},{"repo_path":"infra/aws/lambda/investor-reporting/holdings/publication.py","sha256_at_pin":"..."}]`, `overlay_tests`. Use the three firm keys exactly as written.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~431/IB224-1_holdings_overlay_candidate.json`: the JSON object described above, plus `"base_commit":"<40hex: git rev-parse HEAD at your first act>"`, `"read_date":"<today ISO>"`, `"method":"<120+ characters: exactly what you ran, in what order, and the two arms>"`, `"claim":"measured"`, `"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added]` and the six counters, all 0: `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB224-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB224-1-AC1" cell_refs="IB-pr-590"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r224/p224_cells.py" . IB224-1-AC1</invocation><expect>IB224-1-AC1 PASS</expect></criterion>
<criterion id="IB224-1-AC2" cell_refs="IB-pr-590"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r224/p224_cells.py" . IB224-1-AC2</invocation><expect>IB224-1-AC2 PASS</expect></criterion>
<criterion id="IB224-1-AC3" cell_refs="IB-pr-590"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r224/p224_cells.py" . IB224-1-AC3</invocation><expect>IB224-1-AC3 PASS</expect></criterion>

<expected_criteria>IB224-1-AC1, IB224-1-AC2, IB224-1-AC3</expected_criteria>

What the checks grade: AC1 the identity and the pins (base commit, read date, the overlay pin an ancestor of HEAD that carries the ABSENT-AT-SOURCE A, B and C blocks, each firm's minting pin one of the two IB-pr-549 pins); AC2 per firm (a different candidate hash, the changed members EXACTLY holdings_snapshot.py and publication.py recomputed from git at the overlay pin, every other member equal to the live bundle's); AC3 per firm the offline tests on the overlay tree (passed at least 1, failed 0), notes of 30+ characters, the six counters 0, no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W431-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~431/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 219 (round 3, workstream ~PJ), cell `IB-pr-590`.
<owned_cells>IB-pr-590</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB224-1-AC1, IB224-1-AC2, IB224-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~431/IRPT_BCKEND.TO-IB-pr-590.holdings-overlay.proof_of_spec.json`.
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
comp-adversary: RUN -- the check IB224-1 dry-run at base on dell2 2026-10-15 ~16:1xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (a git root holding the members at a commit, a synthetic record; removed): all three PASS; nine negatives each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~431` (worktree `C:/dev/wk-IRPT_BCKEND-431`). Class SERVED (a read of served artifacts and a build).
</preflight>
