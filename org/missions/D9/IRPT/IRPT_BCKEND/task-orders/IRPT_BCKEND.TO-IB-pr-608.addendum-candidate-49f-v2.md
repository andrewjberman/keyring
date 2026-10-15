# TO IRPT_BCKEND.TO-IB-pr-608 -- READ the 49 Financial ADDENDUM 1 release candidate: the signed transplant files of IB-pr-595 plus ONLY the ABSENT-AT-SOURCE-D spans of IB-pr-604 and IB-pr-607, built from the minting pin, BUILD ONLY, tested offline, compared with the live bundle; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-608</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~444</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~PL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ADDENDUM 1 and ADDENDUM 2 to the round analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_LANES_PJ4_PJ5_PM1_PN2_PN3_PO8_20261015.md` (@9fef489152, @594e598878; msgs 8644 and 8664: the evidence-key addendum ships after the signed exemption pair, under its own candidate digest and pair) | **Decomp cell:** `IB-pr-608` (decomposition section 234) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-444`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~444 <0.9.0_WK_IRPT_BCKEND~444@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`, `infra/logic/registry`, `org/standards`). Your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence. NEVER add a row object inside an existing block's JSON array.

**Cell `IB-pr-608` (inlined).** IB-pr-595 (record `deliverables/0.9.0_WK_IRPT_BCKEND~434/IB228-1_holdings_transplant_candidate.json`, signed pair candidate digest `d2eaf305...` for 49financial) built 49 Financial's TRANSPLANT candidate: the minting pin `b1d354cfc9341168a3b4c316a344876ce0049b97` with the exemption commits applied to `holdings_snapshot.py` and `publication.py`, committed under `deliverables/0.9.0_WK_IRPT_BCKEND~434/transplant/49financial/`. IB-pr-604 (merged @f888350689) and IB-pr-607 (merged @53c238604b) added and amended three `ABSENT-AT-SOURCE-D` spans in HEAD's `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`: the SmartX evidence read (a helper pair and a reason-category exception), the provider hook, and the listing hook that writes `"evidence": "smartx_map_present"` into an exempted account's manifest entry, or `"evidence": "unread"` with `"evidence_reason"` (a category) when the map was not obtained, as the CTO half of the addendum requires (msg 8719 condition 2). The first candidate of this addendum (IB-pr-606, digest `32d6dfcb`) predates IB-pr-607 and is VOID for any apply. This cell builds the ADDENDUM candidate again: the signed transplant file plus ONLY the current spans, so the addendum pair moves the evidence key alone. Nothing is minted, uploaded, deployed or invoked.

**READ FIRST (named files only):** the IB-pr-595 record and harness (`deliverables/0.9.0_WK_IRPT_BCKEND~434/IB228-1_holdings_transplant_candidate.json` and `ib228_1_transplant_candidate.py`: reuse its pin-worktree set-up, its BUILD ONLY builder call, the twice-identical build and the live comparison, in a COPY in YOUR deliverables folder, for the 49financial firm ONLY), the transplanted files `deliverables/0.9.0_WK_IRPT_BCKEND~434/transplant/49financial/holdings_snapshot.py` and `publication.py`, HEAD's `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (the three `ABSENT-AT-SOURCE-D` spans), and `git diff e2700915d2 53c238604b -- data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (the whole change, which is the D spans and nothing else: HEAD's file with every D span stripped equals the file at `e2700915d2`).

**Do (49financial only):**
1. A full detached worktree of the minting pin `b1d354cfc9341168a3b4c316a344876ce0049b97` OUTSIDE the repository, sparse checkout disabled in that worktree alone (as IB-pr-595 did).
2. **Build the candidate file:** copy IB-pr-595's committed transplanted `holdings_snapshot.py` and `publication.py` into that worktree; apply the diff `git diff e2700915d2 53c238604b -- data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` onto the transplanted file (for example `git diff e2700915d2 53c238604b -- <path> | git apply --3way`, or an equivalent you can describe). The three spans anchor on lines that exist in the transplanted file (the helper pair before `def _absent_provider`; the hook after the `source_evidence_for(...)` call in `provide()`; the hook after the `dates[account_id].update(...)` line in `_absent_scope_listing`). A conflict is resolved by keeping the transplanted text outside the D spans and the spans exactly as HEAD has them; every conflict is counted and described in the notes. `publication.py` stays the transplanted file UNCHANGED.
3. **Verify the candidate file:** (a) strip every `ABSENT-AT-SOURCE-D` span (BEGIN line to END line, both included) from the candidate `holdings_snapshot.py`: the result equals IB-pr-595's transplanted file BYTE FOR BYTE; (b) the spans of the candidate equal HEAD's spans exactly (same count, same text); (c) `allow_older_date` and `ONE-DATE-ASSERT` are absent; `cusip_key` is present. Record `d_spans` = `{"count":<n>,"equal_to_head":true,"diff_lines_outside_spans":0}` and `cusip_port_present` true.
4. **Commit the two candidate files** under YOUR deliverables folder as `addendum/49financial/holdings_snapshot.py` and `addendum/49financial/publication.py` (the check recomputes their sha256 from those committed files).
5. Build the bundle BUILD ONLY from the pin worktree with the two candidate files in place (twice, identical members), download the LIVE bundle read-only and compare member by member: the changed members must be EXACTLY the two files; `members_equal_to_live` is `members_total` minus 2. The candidate bundle sha256 must differ from the live bundle's AND from IB-pr-595's `d2eaf305...` (a new digest).
6. **Run the offline tests on the candidate tree.** Copy into the tree (tests are not bundle members) from HEAD: `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py`, `test_absent_at_source_exemption.py`, `test_absent_at_source_receipts.py`, `test_absent_at_source_smartx_evidence.py`, `test_holdings_publish_gate.py` and `infra/aws/lambda/investor-reporting/holdings/tests/test_publication.py`; do NOT run `test_holdings_bypass_one_date.py`. Run with `python -m pytest -q -p no:cacheprovider` from the tree root. Record `tests` = `{"passed":n,"failed":0}`. A failing test is the finding: name it in a row and in the notes, with whether it tests a feature the pin lacks (then say which test you excluded and why) or the exemption or the evidence itself (then STOP).

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~444/IB239-1_addendum_candidate.json`: `{"base_commit":"<40hex: git rev-parse HEAD at your first act>","read_date":"<today ISO>","claim":"measured","method":"<120+ characters: exactly what you ran, in what order>","firm":"49financial","minting_pin":"b1d354cfc9341168a3b4c316a344876ce0049b97","transplant_ref":{"candidate_bundle_sha256":"<IB-pr-595's 49financial candidate_bundle_sha256, copied from its record>"},"live_bundle_sha256":"<64 hex>","candidate_bundle_sha256":"<64 hex>","members_total":<n>,"members_equal_to_live":<n minus 2>,"cusip_port_present":true,"changed_members":[{"repo_path":"data/assets/scripts/gold/investor_reporting/holdings_snapshot.py","artifact":"org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~444/addendum/49financial/holdings_snapshot.py","sha256_candidate":"<sha256 of that committed file>"},{"repo_path":"infra/aws/lambda/investor-reporting/holdings/publication.py","artifact":"org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~444/addendum/49financial/publication.py","sha256_candidate":"<sha256 of that committed file>"}],"d_spans":{"count":<n>,"equal_to_head":true,"diff_lines_outside_spans":0},"tests":{"passed":<n>,"failed":0},"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB239-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (candidate files, record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB239-1-AC1" cell_refs="IB-pr-608"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r239/p239_cells.py" . IB239-1-AC1</invocation><expect>IB239-1-AC1 PASS</expect></criterion>
<criterion id="IB239-1-AC2" cell_refs="IB-pr-608"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r239/p239_cells.py" . IB239-1-AC2</invocation><expect>IB239-1-AC2 PASS</expect></criterion>
<criterion id="IB239-1-AC3" cell_refs="IB-pr-608"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r239/p239_cells.py" . IB239-1-AC3</invocation><expect>IB239-1-AC3 PASS</expect></criterion>

<expected_criteria>IB239-1-AC1, IB239-1-AC2, IB239-1-AC3</expected_criteria>

What the checks grade: AC1 the identity, the transplant reference and the live bundle equal to IB-pr-595's record, the minting pin; AC2 a new candidate digest, the changed members EXACTLY holdings_snapshot.py and publication.py, each committed file's sha256 recomputed, publication.py equal to the signed transplant's, the candidate file with every D span stripped equal to the signed transplant's file byte for byte, its D spans equal to HEAD's, the one-date bypass absent; AC3 the offline tests (passed at least 1, failed 0), notes of 30+ characters, the six counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file; a hunk of the candidate file outside a D span that differs from the signed transplant. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W444-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~444/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 234 (round 4, workstream ~PL), cell `IB-pr-608`.
<owned_cells>IB-pr-608</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB239-1-AC1, IB239-1-AC2, IB239-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~444/IRPT_BCKEND.TO-IB-pr-608.addendum-candidate-49f.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a BUILD-ONLY candidate and read-only downloads of the live artifact; nothing is uploaded, minted, deployed, invoked or written to AWS; the record carries hashes, counts and member names only. The addendum pair that uses it, and its apply, are later acts.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use this box's existing credentials.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p239_cells.py IB239-1 dry-run at base on dell2 2026-10-15 ~22:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control (control237.py) in temp git roots the run created itself (a committed signed record and transplanted files, a HEAD file with D spans, a candidate, a synthetic record; removed): all three PASS; sixteen negatives each fail their own arm; 0 unexpected.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~444` (worktree `C:/dev/wk-IRPT_BCKEND-444`). Class SERVED (a read of served artifacts and a build).
</preflight>
