# TO IRPT_BCKEND.TO-IB-pr-580 -- READ the served DELTA of the absent_at_source exemption ALONE, per firm: the same candidate gated WITHOUT and WITH the evidence provider, the nodes the exemption adds, the second fire; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-580</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~422</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PJ</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8302 and CVO v118 (measure the exemption ALONE: the same candidate with and without it, per firm) on the merged build IB-pr-577 | **Decomp cell:** `IB-pr-580` (decomposition section 214) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-422`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~422 <0.9.0_WK_IRPT_BCKEND~422@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them.

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting/`, then add (locally, never committed) the further directories the import chain of the modules you call needs: import the module, and add the directory of each import error until it imports (earlier workers on these files needed `infra/aws/lambda/investor-reporting`, `data/mdpf/scripts/gold`, `data/mdpf/scripts/silver`, `data/assets/scripts/silver`, `infra/aws/lambda/v2_portal/_shared`, `docs/contracts/investor-reporting`, `lib`). Use `python -I` only for files you do not trust; your own harness runs with the repository's modules on `sys.path`.

**Client data rule:** counts, dates, hashes, commit ids and file paths only in any tracked file; no real account id, household id, client id, name, quantity or value, no real security identifier, no object key that carries an account. The harness script you commit prints and writes counts only.

**READ-ONLY on every served prefix.** You may call AWS read APIs through the repository's own readers (`get_object`, `list_objects_v2`, `head_object`) with this box's credentials, nothing else: no `put`, `delete`, copy, invoke, publish or sign-in, no upload flag, no call of `land`, `write_refusal_record`, `HoldingsPublication.publish` or any function that writes. Scratch files go in a directory OUTSIDE the repository.

**Cell `IB-pr-580` (inlined).** IB-pr-577 (merged @95ca50c91e) wired the `absent_at_source` exemption of the holdings publish gate live in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, with the visible listing: a gate-exempted account stays in the snapshot as a zero-value account node. The CTO ruled (msg 8302, CVO v118) that the never-widen pair for 49 Financial and Cottonwood measures **the exemption ALONE**: the same candidate with and without it, per firm, so the pair's served DELTA is the exemption's own and not another release's. This cell measures it by a READ-ONLY dry run of the HEAD code over the live pinned inputs. It writes no snapshot anywhere.

**READ FIRST (named files only):** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (`run_firm` near line 3188 to 3400 and the helpers it calls, `build_snapshot`, `VersionedInputs`, `select_business_date`, `served_publication`, `evaluate_publish_gate`, `closed_account_ids`, `directory_marks_no_closures`, `firm_bucket_map`, `BUILDERS`, and the block `ABSENT-AT-SOURCE-B`: `source_evidence_for`, `_absent_provider`, `_absent_scope_listing`), `infra/aws/lambda/investor-reporting/holdings/publication.py` (`HoldingsPublication.begin` is a read of the current index), and the tests `data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py` (`fire`) and `data/assets/scripts/gold/investor_reporting/tests/test_absent_at_source_wiring.py`.

**Do, per firm (the 49 Financial firm and the Cottonwood firm: take their ids from `BUILDERS` and the registry, type no firm name in a tracked file):**
1. Mirror `run_firm` up to the gate WITHOUT writing: `s3` = the box's default client; `publisher = HoldingsPublication(s3, firm_id, qa=False)`; `expected = publisher.begin()` (a read); `inputs = VersionedInputs(s3)`; `snapshot = build_snapshot(firm_id, inputs, select_business_date())`; `served = served_publication(publisher, expected)`. Print the candidate's business date and the served business date. Never call `land`, never pass `upload`.
2. **Arm WITHOUT:** `gate0 = evaluate_publish_gate(snapshot, served, <the closed_accounts and marks_no_closures lambdas run_firm passes>)` with no evidence provider. Record outcome, the condition names, `len(snapshot["nodes"])` and the account-node count.
3. **Arm WITH:** a `copy.deepcopy` of the candidate; the provider exactly as `run_firm` builds it (`_absent_provider(captured, firm_id, inputs, snapshot_copy, served)`); `gate1 = evaluate_publish_gate(snapshot_copy, served, <same lambdas>, absent_at_source_evidence=provider)`; if the gate PUBLISHED with `listed.account_lost_absent_at_source`, apply `_absent_scope_listing(snapshot_copy, gate1, captured)`. Record outcome, conditions, node and account counts, `exempted_accounts` (the number exempted), `first_absent_day` and `since_bound_reached` from the captured evidence.
4. **The exemption alone:** compare the two candidates node by node by `node_id` and amount: `nodes_added`, `accounts_added` (account nodes), `amount_added_usd` (sum of the added nodes' amounts; 0 expected), `other_nodes_changed` (a node in both whose amount or any field differs; 0 expected). If the fresh build is not byte-deterministic between the arms, say so in the notes: build ONCE and deep-copy for the second arm, never build twice.
5. **The second fire:** simulate it by serving the WITH candidate's account ids as the served set (a copy of `served` whose `account_ids` is the WITH candidate's account-id set) and gating the WITHOUT candidate (no listed node) again with the provider: record `exempt_again` (true when the account is exempted again) and `outcome_account_lost` (true when the gate still lists `account_lost` as a refusing condition).
6. If a firm has NO lost account (nothing to exempt) the arms are identical: record that honestly with `exempted_accounts` 0; do not force it.

**Record shape** (`IB218-1_exemption_delta.json`): `"firms": {"<firm key>": {"candidate_day":"YYYY-MM-DD","served_day":"YYYY-MM-DD","builder":"<builder function name>","without":{"outcome":"REFUSED|PUBLISHED","conditions":[names],"node_count":n,"account_count":n},"with":{"outcome":...,"conditions":[...],"node_count":n,"account_count":n,"exempted_accounts":n,"first_absent_day":"YYYY-MM-DD"|null,"since_bound_reached":true|false},"exemption_alone":{"nodes_added":n,"accounts_added":n,"amount_added_usd":0,"other_nodes_changed":0},"second_fire":{"exempt_again":true,"outcome_account_lost":false}}}` with the two keys exactly `49financial` and `cottonwood`. A `PUBLISHED` outcome has no condition and a `REFUSED` outcome at least one; the conditions that REMAIN after the exemption (for example a stale frontier) are the pair's other facts, list them as they are.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~422/IB218-1_exemption_delta.json`: the JSON object described above, plus `"base_commit":"<40hex: git rev-parse HEAD at your first act>"`, `"read_date":"<today ISO>"`, `"method":"<120+ characters: exactly what you ran, in what order, and the two arms>"`, `"claim":"measured"`, `"notes":[at least three lines of 30+ characters: what each fact rests on, what was not read, the sparse directories you added]` and the six counters, all 0: `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`. Commit the harness script you ran under your deliverables folder beside the record, so the issuer can re-run it. If a number cannot be measured, STOP on that part, file a row, and write what you have with the field absent: the check then fails honestly; never estimate.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB218-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record, harness, criteria output first; then the instance alone in a second commit). Do not flip the order's status: the issuer does. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB218-1-AC1" cell_refs="IB-pr-580"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r218/p218_cells.py" . IB218-1-AC1</invocation><expect>IB218-1-AC1 PASS</expect></criterion>
<criterion id="IB218-1-AC2" cell_refs="IB-pr-580"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r218/p218_cells.py" . IB218-1-AC2</invocation><expect>IB218-1-AC2 PASS</expect></criterion>
<criterion id="IB218-1-AC3" cell_refs="IB-pr-580"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r218/p218_cells.py" . IB218-1-AC3</invocation><expect>IB218-1-AC3 PASS</expect></criterion>

<expected_criteria>IB218-1-AC1, IB218-1-AC2, IB218-1-AC3</expected_criteria>

What the checks grade: AC1 the identity and method (base commit, read date, both firms, candidate and served days, builder, the claim measured, both arms named); AC2 the arithmetic per firm (counts with equal counts without plus the exemption alone, no other node changed, no amount added, outcomes and conditions consistent, the second fire exempts again); AC3 notes of 30+ characters, the six counters 0, no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS and on every served prefix, as above. **Nothing is deployed, published, minted, written to AWS, signed or sent.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes to AWS; a need to edit a file outside the paths block (the issuer amends); a step that would take longer than 25 minutes of wall clock without progress (record where it stalled); a real account id or security identifier in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W422-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~422/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 214 (round 1, workstream ~PJ), cell `IB-pr-580`.
<owned_cells>IB-pr-580</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB218-1-AC1, IB218-1-AC2, IB218-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~422/IRPT_BCKEND.TO-IB-pr-580.exemption-delta.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a READ-ONLY dry run: it reads the live pinned inputs and the served publication through the repository's own readers and writes nothing to AWS or to any served prefix; the record carries counts only. The apply of the changed code and the never-widen pair that uses this DELTA are later acts.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use this box's existing credentials.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p218_cells.py IB218-1 dry-run at base on dell2 2026-10-15 ~14:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in temp roots the run created itself (the real calendar, a synthetic record; removed): all pass; eight negatives each fail their own arm.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~422` (worktree `C:/dev/wk-IRPT_BCKEND-422`). Class SERVED (a read of served data and the live pinned inputs).
</preflight>
