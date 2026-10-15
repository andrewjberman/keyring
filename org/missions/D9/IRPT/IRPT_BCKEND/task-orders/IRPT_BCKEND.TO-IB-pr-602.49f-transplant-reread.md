# TO IRPT_BCKEND.TO-IB-pr-602 -- READ 49 Financial's refusal anatomy AND the exemption-alone DELTA again, on IB-pr-595's transplant tree (pin 1 plus the exemption); READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-602</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~437</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~PL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling ADDENDUM 1 @334382c7f4 (msg 8538: re-run the anatomy and the exemption-alone DELTA on IB-pr-595's tree; cut the join, classification and dry-run cells only for what still trips) | **Decomp cell:** `IB-pr-602` (decomposition section 227) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-437`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~437 <0.9.0_WK_IRPT_BCKEND~437@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`). Use `python -I` only for files you do not trust; your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array (the union merge of the drain then duplicates the rows it did not touch).

**Cell `IB-pr-602` (inlined).** The CTO's ruling (ADDENDUM 1 @334382c7f4, msg 8538) orders a re-measure: IB-pr-584 read 49 Financial's refusal (1 of 7,640 served accounts lost, 4 of 1,839 served placed securities unclassified) and IB-pr-580 read the exemption's DELTA, both on HEAD's `holdings_snapshot.py`, which REVERSES the CUSIP port that 49 Financial's live bundle keeps (pin 1, `b1d354cfc9`). IB-pr-595 (merged @5bf120faa2) built the TRANSPLANT tree for 49 Financial: pin 1 plus the exemption alone, 12 CUSIP lines present, the one-date bypass absent. **This cell repeats BOTH measurements on that tree.** Counts only, READ-ONLY, in process; nothing is written, landed or published.

**READ FIRST (named files only):** the two harnesses (reuse their set-up lines, do not edit them): `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~422/ib218_1_exemption_delta.py` and the anatomy harness of IB-pr-584, `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~426/IB220-1_49f_refusal_anatomy_harness.py`, and their records `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~422/IB218-1_exemption_delta.json` and `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~426/IB220-1_49f_refusal_anatomy.json` for the numbers you compare with. The tree: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~434/transplant/49financial/holdings_snapshot.py` and `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~434/transplant/49financial/publication.py` (these two files REPLACE `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` and `infra/aws/lambda/investor-reporting/holdings/publication.py` for this run) and `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~434/IB228-1_holdings_transplant_candidate.json` (the 49financial entry: their sha256, `cusip_port_present`, `one_date_bypass_absent`).

**Do:**
1. **Pin the tree.** Compute the sha256 of the two transplant files and compare with the `sha256_transplanted` values in IB-pr-595's record for `49financial`; a difference is a STOP. Run the harnesses' code with those two files in place of the repository's: build a scratch copy OUTSIDE the repository (for example `%TEMP%`) of what the harnesses import, drop the two files into it, and put it first on `sys.path`; do NOT edit any tracked file. Check by reading the loaded module's file path that the transplant files are the ones imported, and record `tree.cusip_port_present` (the 49 Financial CUSIP port is present in the loaded module) and `tree.one_date_bypass_absent` (the loaded module has no `allow_older_date`).
2. **The anatomy (IB-pr-584's method, unchanged), 49 Financial only:** build the candidate once, read the served publication, compute `lost = served account ids - (candidate scope account ids | candidate account node ids)` as the gate does; classify EVERY lost account into exactly one class, first match in this order: `exempted_absent_at_source`, `closed_by_directory`, `in_source_with_positions`, `evidence_incomplete`, `other`; compute `classified_security_lost` as the gate does; list the conditions the gate still names with the exemption applied, each with `tripped`, `denominator`, `threshold`, `value` and a `cause_split` (`source`, `join`, `undetermined`, summing to `tripped`). Record NO identifier.
3. **The DELTA (IB-pr-580's method, unchanged), 49 Financial only:** the same candidate gated WITHOUT and WITH the evidence provider: for each side the `outcome` (`REFUSED` or `PUBLISHED`), the `conditions`, `node_count`, `account_count`; `with` also `exempted_accounts`, `first_absent_day`, `since_bound_reached`, `listing_applied`; `exemption_alone` the `nodes_added`, `accounts_added`, `amount_added_usd` (0) and `other_nodes_changed` (0); `second_fire` the same candidate gated again with the served set plus the listed ids: `exempt_again` and `outcome_account_lost`.
4. **Compare, in the notes,** the HEAD-code numbers of IB-pr-584 with these: which conditions no longer trip, and by how many. If a count cannot be measured, STOP on that part, file a row, and write what you have with the field absent; never estimate.

**Record shape** (`IB233-1_49f_transplant_reread.json`): `"firm_scope":"49financial"`, `"candidate_day"`, `"served_day"`, `"builder"`, `"tree":{"holdings_snapshot_sha256","publication_sha256","cusip_port_present","one_date_bypass_absent"}`, `"anatomy":{"lost_accounts":{"total","exempted","remaining","classes":{"exempted_absent_at_source","closed_by_directory","in_source_with_positions","evidence_incomplete","other"}},"classified_security_lost":{"total","served_placed_total","candidate_unclassified_total","reading"},"conditions_remaining":[...],"conditions_detail":[{"condition","tripped","denominator","threshold","value","cause_split":{"source","join","undetermined"}}, ...]}`, `"delta":{"without":{...},"with":{...},"exemption_alone":{...},"second_fire":{...}}` as above, plus the common keys of the record shape below. `conditions_detail` holds exactly one entry for `account_lost` and one for `classified_security_lost` (a `tripped` of 0 where it no longer trips).

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~437/IB233-1_49f_transplant_reread.json`: the JSON object described above, plus `"base_commit":"<40hex: git rev-parse HEAD at your first act>"`, `"read_date":"<today ISO>"`, `"method":"<120+ characters: exactly what you ran, in what order, and the two arms>"`, `"claim":"measured"`, `"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added]` and the six counters, all 0: `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB233-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB218-1-AC1" cell_refs="IB-pr-602"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r233/p233_cells.py" . IB218-1-AC1</invocation><expect>IB218-1-AC1 PASS</expect></criterion>
<criterion id="IB218-1-AC2" cell_refs="IB-pr-602"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r233/p233_cells.py" . IB218-1-AC2</invocation><expect>IB218-1-AC2 PASS</expect></criterion>
<criterion id="IB218-1-AC3" cell_refs="IB-pr-602"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r233/p233_cells.py" . IB218-1-AC3</invocation><expect>IB218-1-AC3 PASS</expect></criterion>

<expected_criteria>IB233-1-AC1, IB233-1-AC2, IB233-1-AC3</expected_criteria>

What the checks grade: AC1 the identity and method (base commit, read date, days, the tree named by the sha256 of its two transplanted files and equal to IB-pr-595 record, the CUSIP port present, the one-date bypass absent); AC2 the arithmetic (the anatomy: lost = exempted + remaining, the classes sum, the classified_security_lost counts, the remaining conditions; the DELTA: with = without + the exemption alone, no other node, no amount, the outcomes and the second fire); AC3 notes of 30+ characters, the six counters 0, no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W437-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~437/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 227 (round 2, workstream ~PL), cell `IB-pr-602`.
<owned_cells>IB-pr-602</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB233-1-AC1, IB233-1-AC2, IB233-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~437/IRPT_BCKEND.TO-IB-pr-602.49f-transplant-reread.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a READ-ONLY in-process run over the live pinned inputs and the served publication through the repository's own readers and the two transplant files; nothing is written to AWS or to any served prefix; the record carries counts only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use this box's existing credentials.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p233_cells.py IB233-1 dry-run at base on dell2 2026-10-15 ~19:1xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (the real calendar and IB-pr-595's record, a synthetic record; removed): all three PASS; fifteen negatives and the no-record case each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~437` (worktree `C:/dev/wk-IRPT_BCKEND-437`). Class SERVED (a read of served data and the live pinned inputs).
</preflight>
