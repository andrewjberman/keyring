# TO IRPT_BCKEND.TO-IB-pr-526 -- COUNT the holdings the IR cash rule would move, per firm, READ ONLY: served holdings that carry a cash-type `sub_asset_class` but a class other than cash (CTO round-188 analysis @f82cf22b5c, item 2 first half; row D2-S156; D2's read IR_HOLDINGS_CLASS_SOURCE.json)

<to_id>IRPT_BCKEND.TO-IB-pr-526</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~373</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>188</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-188 analysis (item 2: "the count of holdings that move per firm, then the build from ONE shared definition, then its pair") | **Decomp cell:** `IB-pr-526` (decomposition section 180) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-373` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~373 <0.9.0_WK_IRPT_BCKEND~373@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read; print what a search covered before you read a zero as an absence). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-526` (inlined).** Andrew's point: the Investor Reporting Holdings page shows FDRXX (a money-market fund) as Fixed Income; it should be Cash. D2's read (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~149/IR_HOLDINGS_CLASS_SOURCE.json`; read it first) found: the page takes its class from `classify_security` at `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` lines 977-984, which serves a canonical `etf-classifications` row's `asset_class` exactly as stored and carries its `sub_asset_class` beside it, but never reads `sub_asset_class`; the Black Diamond gold classifier (`data/black_diamond/scripts/gold/lib/etf_classifier.py`, `_row_class`, lines 104-116) already serves cash when a row's `sub_asset_class` (trimmed, lower-cased) is `cash`. The proposed rule: on the canonical-row branch, when `sub_asset_class` is cash, serve `cash` whatever `asset_class` the row stores. **This order only COUNTS what that rule would move: in each firm's served holdings, how many nodes carry a cash-type `sub_asset_class` but a served class other than cash.** It writes and invokes nothing.

**Client data rule:** counts, dates and PUBLIC security symbols only in any tracked file (a ticker such as FDRXX is a public symbol and may be listed); **no account id, client id, position value, quantity or holding name**; the snapshot is read into memory or into scratch OUTSIDE the worktree (`C:/dev/_scratch373/`) and the scratch is deleted at the end with a short bounded script.

**Read first:** D2's file above; `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (the node fields, `classify_security`, where the snapshot is written and its object key shape); `lib/opal_naming.py` and `infra/logic/registry/` (the firm's gold bucket and prefix come from `address()` output, rule 30; never type a bucket); `infra/aws/lambda/investor-reporting/holdings/` (what the `irpt-holdings` Lambda reads and serves).

**Do, in this order (every number is a MEASUREMENT with its source named in `notes`):**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit` (state it).
2. **The served snapshot, per firm** (`49financial`, `cottonwood`, `inflection`): find from the builder and the registry where each firm's LATEST served holdings snapshot lives and its key shape; with `s3api list-objects-v2` (READ, keys and sizes only) find the newest snapshot object per firm. GET each newest snapshot object into scratch OUTSIDE the repository (the order grants this read: counts only come out; the firm's own holdings are client data and never appear in a tracked file). If your identity cannot read a firm's snapshot, record `found` false with the reason and say so in `notes`; do not widen. Record `firms.<firm>.snapshot_read` as `{"found": true|false, "business_date": "YYYY-MM-DD", "nodes": n}` (`reason` when not found): `nodes` is the count of SECURITY (position-level) nodes the page lists, defined in `notes` the way the builder does.
3. **The counts, per firm, computed in memory from the snapshot** (never written): `cash_subclass_nodes` = nodes whose `sub_asset_class`, trimmed and lower-cased, equals `cash`; `already_cash` = of those, nodes whose served `asset_class` is already cash (the builder's own cash value: read it from the code, for example `cash`); `would_move` = `cash_subclass_nodes` minus `already_cash` (the nodes whose served class the rule would change); `moving_tickers` = the DISTINCT public symbols of the would-move nodes (empty when `would_move` is 0; symbols only). If a firm's served nodes do not carry `sub_asset_class` at all, record `cash_subclass_nodes`, `would_move` and `already_cash` as 0 and state in that firm's `note` that the field is absent from the served nodes, so the rule cannot act on that firm's snapshot as served. For a firm with no snapshot found, record the three counts as `null` and `moving_tickers` `[]`.
4. **What the code serves for a money-market ticker with NO canonical row** (read the code, do not run it): the bd-securities fallback answer (`data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py` lines 54-55 and 152-153, via `holdings_snapshot.py` 985-993) is fixed_income for money-market names, UNCHANGED by the proposed rule; say so in `notes` and name how many of the would-move tickers (if any) come from the canonical branch versus the fallback branch if the snapshot lets you tell, else say it does not.
5. **The canonical table (optional read).** If your identity may `dynamodb:Scan` or `dynamodb:Query` the canonical `etf-classifications` table (read the table name from `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`), record `canonical_table` as `{"rows": n, "cash_subclass_rows": n}` (counts only). If you cannot (a denial is the likely answer: D2's grant excluded it), record `"canonical_table": null` and `"canonical_table_absence": "<one line: the denial or the choice not to scan>"`. Do not widen an identity; do not guess.
6. **Per firm `note`:** what the counts rest on (which snapshot object date), and what was NOT read (the canonical table if not scanned, the node field definitions you did not verify, any snapshot you could not read).
7. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~373/IB188-2_holdings_class_count.json`: `{"base_commit":"<40hex>","firms":{"49financial":{"snapshot_read":{...},"cash_subclass_nodes":n|null,"would_move":n|null,"already_cash":n|null,"moving_tickers":[...],"note":"..."},"cottonwood":{...},"inflection":{...}},"canonical_table":{...}|null,"canonical_table_absence":"..."|omitted,"notes":["..."],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}` and a short readable `deliverables/0.9.0_WK_IRPT_BCKEND~373/HOLDINGS_CLASS_COUNT_SUMMARY.md` (what moves per firm, the tickers, and what the build cell needs to know: no more than 50 lines).
8. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB188-2_criteria_output.txt`, write the proof instance named under `<proof_of_spec>` and validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the deliverables FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB188-2-AC1" cell_refs="IB-pr-526"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r188/p188_cells.py" . IB188-2-AC1</invocation><expect>IB188-2-AC1 PASS</expect></criterion>
<criterion id="IB188-2-AC2" cell_refs="IB-pr-526"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r188/p188_cells.py" . IB188-2-AC2</invocation><expect>IB188-2-AC2 PASS</expect></criterion>
<criterion id="IB188-2-AC3" cell_refs="IB-pr-526"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r188/p188_cells.py" . IB188-2-AC3</invocation><expect>IB188-2-AC3 PASS</expect></criterion>

<expected_criteria>IB188-2-AC1, IB188-2-AC2, IB188-2-AC3</expected_criteria>

What the checks grade: AC1 per firm the served snapshot read (found or not, with its business date and node count, or its stated reason); AC2 per firm the counts consistent (`cash_subclass_nodes` = `would_move` + `already_cash`, not above the node count; `moving_tickers` distinct public symbols, empty exactly when nothing moves, no more tickers than movers; counts null when no snapshot was found) and the canonical table counted or its absence stated; AC3 a note per firm, no long digit run, the six bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. READ ONLY. **Nothing is invoked, written, uploaded, applied or deployed:** no Lambda invoke, no S3 write, no terraform, no sign-in, no vendor call. Allowed AWS calls (READ): `s3api list-objects-v2` and `head-object` on the served holdings snapshot prefixes, `s3api get-object` of each firm's NEWEST snapshot into scratch (counts only come out), `dynamodb scan`/`query` on the canonical table ONLY if your identity already may (a denial is recorded, not worked around), `sts get-caller-identity`.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes or invokes; a value, name or identifier of a client or account in a tracked file; a figure you cannot source (say so; do not estimate). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W373-S<k>` (start at 1); file a row for anything odd and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~373/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 180 (round 188, workstream ~P), cell `IB-pr-526`.
<owned_cells>IB-pr-526</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB188-2-AC1, IB188-2-AC2, IB188-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~373/IRPT_BCKEND.TO-IB-pr-526.ir-holdings-class-count.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the count reads each firm's newest served holdings snapshot into memory (client data, counts only out), lists its prefix, and reads code; it writes nothing and invokes nothing; the build of the shared rule, its pair and its apply (which would change what a client-facing Holdings page serves) are later cells with their own blast radius.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the read uses the worker's own identity and records a denial as a statement, never widened.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p188_cells.py IB188-2 dry-run at base on dell2 2026-10-14 ~02:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp root the run created itself (a synthetic record; removed): all three PASS; negatives, each failing its own arm: a found snapshot without a date, a snapshot not found without a reason, cash-subclass not equal to move plus already-cash, a non-symbol ticker, tickers present with no mover, counts given for a firm with no snapshot, a write counter above 0, a missing note.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~373` (worktree `C:/dev/wk-IRPT_BCKEND-373`). Class SERVED (reads served holdings snapshots and code; writes only the worker's records). The premises (the code path, the rule) are D2's read, which I read; the served counts are what this order measures.
</preflight>
