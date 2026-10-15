# TO IRPT_BCKEND.TO-IB-pr-589 -- READ the release CANDIDATES of the three per-firm holdings bundles carrying the exemption, its listing and the receipts: built from a pin BUILD ONLY and compared with the live bundles member by member; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-589</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~428</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PJ</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round analysis @57266eeb77 (msg 8435: the exemption and the receipts ship under a never-widen pair) on the merged builds IB-pr-576, 577 and 582 | **Decomp cell:** `IB-pr-589` (decomposition section 217) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-428`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~428 <0.9.0_WK_IRPT_BCKEND~428@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`). Use `python -I` only for files you do not trust; your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array (the union merge of the drain then duplicates the rows it did not touch).

**Cell `IB-pr-589` (inlined).** The holdings producer `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` reaches each firm only through that firm's standalone bundle `irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz` (declared in `.tools/safe_deploy_core.py` as `irpt_holdings_49f`, `irpt_holdings_cot` and `irpt_holdings_inf`), which the scheduled fire fetches; IB-pr-549 minted the three bundles from two pins on 2026-10-15 (its record is in `deliverables/0.7.0_AE_CloudOps~IB2/`, the file for criteria `IB-pr-549`/its apply: list the folder newest first). IB-pr-576, 577 and 582 (merged; the exemption, its listing and the receipts) change `holdings_snapshot.py` after those pins. The CTO ruled (round analysis @57266eeb77) that they ship under a never-widen pair per firm. The pair needs a RELEASE CANDIDATE per firm: the bundle built from a pin that carries the three merges, compared with the live bundle. This cell BUILDS the candidates, BUILD ONLY, and compares. It mints, uploads, deploys and invokes nothing.

**READ FIRST (named files only):** `.tools/safe_deploy_core.py` (the declarations of the three holdings bundles and the bundle builder they use: what goes into the tarball, which member list, the key), the IB-pr-549 order `task-orders/IRPT_BCKEND.TO-IB-pr-549.apply-holdings-producer-release-per-firm-pins.md` (its worker face shows how a bundle is minted from a pin worktree and which gates it applies; you only BUILD), and the IB2 record of IB-pr-549 (the landed bundle sha256 per firm).

**Do:**
1. `git rev-parse HEAD` is your base; the PIN is that commit (it carries the three merges). `holdings_snapshot.py` at the pin must hold the `ABSENT-AT-SOURCE-A`, `-B` and `-C` blocks.
2. Build each firm's bundle from the pin, BUILD ONLY: create a worktree OUTSIDE the repository with `git worktree add --detach <scratch>/pin <PIN>` and run the builder `.tools/safe_deploy_core.py` declares, in its build-only/dry mode if it has one, otherwise by calling its tarball-building function directly in process (read the code first); NEVER its upload. If the builder cannot build without uploading, STOP and file a row naming the line. Build each firm twice: the two tarballs must have identical member lists and member hashes (a tarball's own bytes can differ by timestamp: compare members, and say so).
3. Download each firm's LIVE bundle read-only (`get_object` on the declared key) into scratch; record the live bundle's sha256 (it must equal the sha256 IB2's record states as landed; a difference is a STOP: another change landed).
4. Compare member by member (name, sha256): `changed_members` per firm = the members that differ, as `{"repo_path": <the repository path the member comes from>, "sha256_at_pin": <sha256 of that file at the pin by git show>}`; `holdings_snapshot.py` must be among them; every OTHER changed member is named in `extra_changed_reasons` (`{repo_path: reason of 30+ characters}`): the drift guard. `members_total` is the candidate's member count.
5. The candidate bundle hash per firm is the sha256 of the tarball you built (state in the notes that it is not byte-reproducible and that the member hashes are the identity).

**Record shape** (`IB222-1_holdings_bundles_candidate.json`): `"pin":"<40 hex>"`, `"holdings_snapshot_blob":"<git blob of holdings_snapshot.py at the pin>"`, `"firms":{"49financial":{...},"cottonwood":{...},"inflection":{...}}` with, per firm, `live_bundle_sha256`, `candidate_bundle_sha256`, `members_total`, `changed_members`, `extra_changed_reasons`. Use the three keys exactly as written.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~428/IB222-1_holdings_bundles_candidate.json`: the JSON object described above, plus `"base_commit":"<40hex: git rev-parse HEAD at your first act>"`, `"read_date":"<today ISO>"`, `"method":"<120+ characters: exactly what you ran, in what order, and the two arms>"`, `"claim":"measured"`, `"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added]` and the six counters, all 0: `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB222-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB222-1-AC1" cell_refs="IB-pr-589"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r222/p222_cells.py" . IB222-1-AC1</invocation><expect>IB222-1-AC1 PASS</expect></criterion>
<criterion id="IB222-1-AC2" cell_refs="IB-pr-589"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r222/p222_cells.py" . IB222-1-AC2</invocation><expect>IB222-1-AC2 PASS</expect></criterion>
<criterion id="IB222-1-AC3" cell_refs="IB-pr-589"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r222/p222_cells.py" . IB222-1-AC3</invocation><expect>IB222-1-AC3 PASS</expect></criterion>

<expected_criteria>IB222-1-AC1, IB222-1-AC2, IB222-1-AC3</expected_criteria>

What the checks grade: AC1 the identity and the pin (base commit, read date, the pin an ancestor of HEAD that carries the ABSENT-AT-SOURCE A, B and C blocks, the blob, the three firms); AC2 per firm (the live bundle hash, a different candidate hash, the changed members recomputed from git at the pin with holdings_snapshot.py among them, any other changed member named with a reason); AC3 notes of 30+ characters, the six counters 0, no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W428-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~428/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 217 (round 2, workstream ~PJ), cell `IB-pr-589`.
<owned_cells>IB-pr-589</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB222-1-AC1, IB222-1-AC2, IB222-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~428/IRPT_BCKEND.TO-IB-pr-589.holdings-candidates.proof_of_spec.json`.
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
comp-adversary: RUN -- the check IB222-1 dry-run at base on dell2 2026-10-15 ~16:1xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (a git root holding the members at a commit, a synthetic record; removed): all three PASS; seven negatives each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~428` (worktree `C:/dev/wk-IRPT_BCKEND-428`). Class SERVED (a read of served artifacts and a build).
</preflight>
