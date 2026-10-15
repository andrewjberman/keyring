# TO IRPT_BCKEND.TO-IB-pr-584 -- READ why 49 Financial still refuses after the exemption: the lost accounts by class (counts only), what classified_security_lost names, the conditions that remain; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-584</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~426</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the READ IB-pr-580's finding (the exemption alone does not unblock 49 Financial) and the CTO's msg 8359 | **Decomp cell:** `IB-pr-584` (decomposition section 216) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-426`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~426 <0.9.0_WK_IRPT_BCKEND~426@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`). Use `python -I` only for files you do not trust; your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array (the union merge of the drain then duplicates the rows it did not touch).

**Cell `IB-pr-584` (inlined).** IB-pr-580 (record `deliverables/0.9.0_WK_IRPT_BCKEND~422/IB218-1_exemption_delta.json`, merged @d1ba413cec) found that the `absent_at_source` exemption does NOT unblock 49 Financial: candidate 2026-10-14 against served 2026-10-12 is REFUSED with and without it, on `account_lost` and `classified_security_lost`; the exemption exempts ONE lost account and the gate still refuses on the others. This cell READS why: it classifies every lost account by evidence, counts what `classified_security_lost` names, and states the conditions that remain. Counts only, READ-ONLY, in process; nothing is written, landed or published.

**READ FIRST (named files only):** the harness `deliverables/0.9.0_WK_IRPT_BCKEND~422/ib218_1_exemption_delta.py` (it builds the candidate once, reads the served publication and gates twice: reuse its set-up lines, do not edit it), `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (`evaluate_publish_gate` near line 3076 to 3200: the `account_lost` and `classified_security_lost` branches, `_gate_served_keys`, `_gate_account_ids`; the `ABSENT-AT-SOURCE-B` block: `source_evidence_for`, `_absent_evidence`, `_absent_spec_49f`, `absent_at_source_exempt`; `closed_account_ids`, `directory_marks_no_closures`), and `deliverables/0.9.0_WK_IRPT_BCKEND~422/IB218-1_exemption_delta.json` for the numbers you must reproduce.

**Do:**
1. Mirror the harness up to the gate for the 49 Financial firm only, WITHOUT writing: build the candidate once (`build_snapshot` over `VersionedInputs`), read `served_publication`, compute `lost = served["account_ids"] - (candidate scope account ids | candidate account node ids)` exactly as the gate does. `lost_accounts.total` is `len(lost)`; it must reproduce the harness record's refusal (more than the one exempted).
2. Classify EVERY lost account into exactly one class, first match in this order: `exempted_absent_at_source` (the exemption exempts it: call `absent_at_source_exempt` with the evidence the provider returns); `closed_by_directory` (in `closed_account_ids(...)` the gate calls); `in_source_with_positions` (the evidence shows positions above zero for it in ANY of the four partitions: candidate or prior day, positions or balance table: this is an account the source still reports but the candidate lacks, so the build dropped it); `evidence_incomplete` (the evidence is None or fails completeness, so no account could be exempted: classify the REST this way); `other`. Record `lost_accounts` = `{"total":n,"exempted":n,"remaining":n,"classes":{"exempted_absent_at_source":n,"closed_by_directory":n,"in_source_with_positions":n,"evidence_incomplete":n,"other":n}}` (classes sum to total; `remaining` = total - exempted).
3. `classified_security_lost`: compute it as the gate does (`now_unclassified & (placed - unplaced)`); record `{"total":n,"served_placed_total":n,"candidate_unclassified_total":n,"reading":"<60+ characters: what the securities have in common that you can state without naming one: for example the asset-class values the served snapshot placed them in, whether the candidate's unclassified count moved against the previous candidate, and which input the build classifies from, read from the code>"}`. Record NO security identifier.
4. `conditions_remaining` = the gate's refusing condition names with every exemption applied (from the gate result), and it must agree with steps 2 and 3.
5. If a count cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**AMENDMENT 1 (CTO round analysis @57266eeb77, msg 8435; this ADDS to the record, nothing above is removed).** For EACH of the two conditions record one entry of `conditions_detail` = a list of two objects `{"condition":"account_lost"|"classified_security_lost","tripped":n,"denominator":m,"threshold":"<what the gate's rule says trips it, in words, read from the code, 30+ characters>","value":"<the value measured against it, in words, 20+ characters>","cause_split":{"source":n,"join":n,"undetermined":n}}`. `tripped` is the accounts (or securities) that trip it (for `account_lost` the remaining lost accounts after the exemption; for `classified_security_lost` its total); `denominator` the served accounts (or served placed securities); `cause_split` sums to `tripped`: **source** = the custodian stopped reporting it (an account the source shows with no positions or absent on the candidate day; a security the day's positions no longer carry), **join** = we dropped it (an account the source still reports with positions but the candidate lacks; a security the positions still carry with an identifier but the candidate leaves unclassified because a classification or account key was not matched), **undetermined** = neither can be shown from the reads. For `account_lost` the classes you already record map as: `in_source_with_positions` is join; `closed_by_directory`, `exempted_absent_at_source` and `evidence_incomplete` are source or undetermined as the evidence shows; say in the notes how you mapped them. No identifier in any field.

**Record shape** (`IB220-1_49f_refusal_anatomy.json`): `"firm_scope":"49financial"`, `"candidate_day"`, `"served_day"`, `"lost_accounts"`, `"classified_security_lost"`, `"conditions_remaining"` as above.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~426/IB220-1_49f_refusal_anatomy.json`: the JSON object described above, plus `"base_commit":"<40hex: git rev-parse HEAD at your first act>"`, `"read_date":"<today ISO>"`, `"method":"<120+ characters: exactly what you ran, in what order, and the two arms>"`, `"claim":"measured"`, `"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added]` and the six counters, all 0: `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB220-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB220-1-AC1" cell_refs="IB-pr-584"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r220/p220_cells.py" . IB220-1-AC1</invocation><expect>IB220-1-AC1 PASS</expect></criterion>
<criterion id="IB220-1-AC2" cell_refs="IB-pr-584"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r220/p220_cells.py" . IB220-1-AC2</invocation><expect>IB220-1-AC2 PASS</expect></criterion>
<criterion id="IB220-1-AC3" cell_refs="IB-pr-584"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r220/p220_cells.py" . IB220-1-AC3</invocation><expect>IB220-1-AC3 PASS</expect></criterion>

<expected_criteria>IB220-1-AC1, IB220-1-AC2, IB220-1-AC3</expected_criteria>

What the checks grade: AC1 the identity and method (base commit, read date, candidate and served days, firm scope 49financial, the claim measured, both gates named); AC2 the arithmetic (lost = exempted + remaining; the five classes sum to the lost accounts; exempted equals its class; the classified_security_lost counts do not exceed the served placed or candidate unclassified securities; a reading of 60+ characters; the remaining conditions agree with the counts); AC3 notes of 30+ characters, the six counters 0, no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W426-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~426/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 216 (round 1, workstream ~PL), cell `IB-pr-584`.
<owned_cells>IB-pr-584</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB220-1-AC1, IB220-1-AC2, IB220-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~426/IRPT_BCKEND.TO-IB-pr-584.49f-refusal-anatomy.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a READ-ONLY in-process run over the live pinned inputs and the served publication through the repository's own readers; nothing is written to AWS or to any served prefix; the record carries counts only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use this box's existing credentials.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p220_cells.py IB220-1 dry-run at base on dell2 2026-10-15 ~15:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (the real calendar, a synthetic record; removed): all three PASS; nine negatives and the no-record case each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~426` (worktree `C:/dev/wk-IRPT_BCKEND-426`). Class SERVED (a read of served data and the live pinned inputs).
</preflight>
