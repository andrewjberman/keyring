# TO IRPT_BCKEND.TO-IB-pr-528 -- COUNT the IR holdings class rule's movers split by layer, run the FDRXX-on-Inflection check, and write the never-widen packet for the rule's later release, READ ONLY (CTO round-189 analysis item 2 @318056547a; count IB-pr-526 upper bounds 32, 253, 841; row D2-S156)

<to_id>IRPT_BCKEND.TO-IB-pr-528</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~375</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>189</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-189 analysis (item 2: "First check: FDRXX on Inflection resolves on the canonical branch. The packet counts what moves per firm against IB-pr-526's upper bounds, split by layer, as a never-widen packet. The apply waits for the pair.") | **Decomp cell:** `IB-pr-528` (decomposition section 181) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-375` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~375 <0.9.0_WK_IRPT_BCKEND~375@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read; print what a search covered before you read a zero as an absence). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-528` (inlined).** The IR cash rule (build order IB-pr-527) makes a canonical `etf-classifications` row whose `sub_asset_class` is `Cash` serve the `cash` class. IB-pr-526 counted, per firm, the served holdings that carry a cash sub-class but another class, as an UPPER BOUND because the served basis `TABLE` is also written by the bd-securities fallback: 32 (49financial, newest served 2026-10-12), 253 (cottonwood, newest served 2026-10-08) and 841 (inflection, 2026-10-12). Its record is `deliverables/0.9.0_WK_IRPT_BCKEND~373/IB188-2_holdings_class_count.json` and summary `HOLDINGS_CLASS_COUNT_SUMMARY.md`; read both first. **This order splits those movers by layer, runs the first check the CTO named, and packages the numbers as a never-widen packet. It writes and invokes nothing.**

**Client data rule:** counts, dates and PUBLIC security symbols only in any tracked file (FDRXX is a public symbol); **no account id, client id, position value, quantity or holding name**; snapshots are read into memory or into scratch OUTSIDE the worktree (`C:/dev/_scratch375/`) and the scratch is deleted at the end with a short bounded script.

**Do, in this order (every number is a MEASUREMENT with its source named in `notes`):**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit` (state it).
2. **The canonical table.** Scan the `etf-classifications` DynamoDB table (name in `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`; page to the end, count the pages; a READ). Record `canonical_table` = `{"rows": n, "cash_subclass_rows": n}` where a cash-subclass row is one whose `sub_asset_class`, trimmed and lower-cased, equals `cash`. A scan that cannot finish is a STOP with a row, not a partial count.
3. **The FDRXX check.** Read the table's row for `FDRXX` and record `fdrxx_inflection` = `{"ticker":"FDRXX","canonical_row_found":bool,"canonical_asset_class":"..","canonical_sub_asset_class":"..","inflection_nodes_with_ticker":n,"resolves_on_canonical_branch":bool,"reading":"one sentence"}` where `inflection_nodes_with_ticker` is the count of SECURITY nodes in Inflection's newest served holdings snapshot whose display symbol is FDRXX, and `resolves_on_canonical_branch` is true exactly when the row is found, its sub is cash and that count is above 0. Record top-level `rule_scope` = `"canonical_only"` when it resolves, else `"canonical_and_fallback"`.
4. **The split, per firm** (`49financial`, `cottonwood`, `inflection`): read each firm's newest ACCEPTED served snapshot as IB-pr-526's record and summary describe (its method is the starting point; take its object keys from there), in memory. A would-move node is one with a cash-type sub-class and a served class other than `cash` (IB-pr-526's definition). It is on the **canonical branch** when its display symbol is a key of the canonical table scanned in step 2, else on the **fallback branch**. Record per firm: `snapshot_read` (`{"found":bool,"business_date":"YYYY-MM-DD","nodes":n}`, or `reason` when not found), `would_move_total`, `canonical_branch`, `fallback_branch` (the two sum to the total), `canonical_tickers` and `fallback_tickers` (DISTINCT public symbols that are ticker-shaped, `A-Z`, digits, dot, dash, up to 12 characters; a non-ticker-shaped identifier is counted, never listed), `vs_ib526` = `{"upper_bound": 32|253|841, "delta": would_move_total - upper_bound}` and a `note` (which snapshot date, what the split rests on, what was not read). If a snapshot is not found: the three counts `null`, tickers `[]`, `delta` `null`.
5. **The packet** `deliverables/0.9.0_WK_IRPT_BCKEND~375/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-528.md` (3,000 characters or more), for the RULE'S LATER RELEASE, the shape of `deliverables/0.9.0_WK_IRPT_BCKEND~372/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-525.md` (read it as the model). It states: **Branch A** (the act: the holdings producer carrying `apply_cash_rule` is released, then each firm's next scheduled fire re-publishes its holdings; read from the code and `infra/` how the producer is deployed and named bundles, and say what you READ and what you did NOT census live); **Branch B** (rollback: for each firm, name the object version of `current/manifest.json` served NOW by a `list-object-versions` READ of that one named key, and say that restoring the prior manifest version returns the prior publication; state what cannot be undone); the **blast radius** per firm (the counts of step 4: nodes whose served class changes from fixed_income or another class to cash; nothing else changes: not the sub-class, the basis, the weights or the totals) and the **layer fact** (the fallback branch's cash-subclass holdings stay as served: say how many per firm); the **publish gate** (a rule-bearing candidate still meets the gate's six conditions; Cottonwood's candidates have been refused since 2026-10-13T14:17Z on one lost account, so the rule reaches Cottonwood's page only after that is resolved); the **COO half and the CTO half, both UNSIGNED**, with the packet's own sha256 left for the signers; the cash definition used (sub-class `Cash` only; `Money Market` and `T-Bill` sub-classes are NOT moved, and say how many canonical rows carry them).
6. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~375/IB189-2_cash_rule_by_layer.json`: `{"base_commit":"<40hex>","fdrxx_inflection":{...},"rule_scope":"..","canonical_table":{...},"firms":{...},"notes":["..."],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.
7. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB189-2_criteria_output.txt`, write the proof instance named under `<proof_of_spec>` and validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the deliverables FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record or packet (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB189-2-AC1" cell_refs="IB-pr-528"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r189/p189_cells.py" . IB189-2-AC1</invocation><expect>IB189-2-AC1 PASS</expect></criterion>
<criterion id="IB189-2-AC2" cell_refs="IB-pr-528"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r189/p189_cells.py" . IB189-2-AC2</invocation><expect>IB189-2-AC2 PASS</expect></criterion>
<criterion id="IB189-2-AC3" cell_refs="IB-pr-528"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r189/p189_cells.py" . IB189-2-AC3</invocation><expect>IB189-2-AC3 PASS</expect></criterion>

<expected_criteria>IB189-2-AC1, IB189-2-AC2, IB189-2-AC3</expected_criteria>

What the checks grade: AC1 the canonical table scanned (rows and cash-subclass rows above 0), the FDRXX row read, Inflection's FDRXX nodes counted, `resolves_on_canonical_branch` and `rule_scope` consistent with them; AC2 per firm the snapshot read (found with date and node count, or its stated reason), `canonical_branch + fallback_branch = would_move_total` not above the node count, tickers distinct public symbols, no more tickers than nodes, `vs_ib526` stating the right upper bound and delta, nulls for a firm not found; AC3 the packet (3,000 characters or more, naming Branch A, Branch B, blast radius, rollback, version, COO half, CTO half, unsigned, fallback, cash, publish gate), no long digit run in the packet or record, the six bound counters 0, a note per firm. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. READ ONLY. **Nothing is invoked, written, uploaded, applied or deployed:** no Lambda invoke, no S3 write, no terraform, no sign-in, no vendor call. Allowed AWS calls (READ): `s3api list-objects-v2`, `list-object-versions` and `head-object` on the served holdings prefixes and each firm's one named `current/manifest.json` key, `s3api get-object` of each firm's NEWEST snapshot into scratch (counts only come out), `dynamodb scan` of the canonical table, `sts get-caller-identity`. A denial is recorded as a statement, never worked around or widened.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes or invokes; a value, name or identifier of a client or account in a tracked file; a figure you cannot source (say so; do not estimate). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W375-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~375/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 181 (round 189, workstream ~P), cell `IB-pr-528`.
<owned_cells>IB-pr-528</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB189-2-AC1, IB189-2-AC2, IB189-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~375/IRPT_BCKEND.TO-IB-pr-528.ir-holdings-class-rule-count-by-layer-and-packet.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads each firm's newest served holdings snapshot into memory (client data, counts only out), the canonical table (a full scan, counts only out) and S3 listings of keys and versions; it writes nothing and invokes nothing; the release of the rule, its pair and its apply (which would change what a client-facing Holdings page serves) are later cells with their own blast radius.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity, which scanned the canonical table in IB-pr-526 (row D2-W373-S2).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p189_cells.py IB189-2 dry-run at base on dell2 2026-10-14 ~03:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp root the run created itself (a synthetic record and packet; removed): all three PASS; negatives, each failing its own arm: a resolves flag contradicting the row, a scope contradicting the flag, a table not scanned, a split not summing, a non-symbol ticker, a wrong delta, counts given for a firm not found, a write counter above 0, a long digit run, a missing note, a packet without Branch B, a packet too short.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~375` (worktree `C:/dev/wk-IRPT_BCKEND-375`). Class SERVED (reads served holdings snapshots, the live canonical table and S3 listings; writes only the worker's records). My own read at ~02:5xZ: the canonical row for FDRXX reads asset_class fixed_income, sub_asset_class Cash (11,361 rows scanned, 365 with sub Cash), so the expected scope is canonical_only; the worker measures it, Inflection's FDRXX node count included.
</preflight>
