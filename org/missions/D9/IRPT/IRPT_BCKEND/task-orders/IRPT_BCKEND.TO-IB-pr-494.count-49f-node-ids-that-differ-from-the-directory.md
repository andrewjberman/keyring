# TO IRPT_BCKEND.TO-IB-pr-494 -- the read-only COUNT of 49 Financial accounts whose node id differs from the directory's account id (row DSGN_IRPTV1-D2-W72-S2)

<to_id>IRPT_BCKEND.TO-IB-pr-494</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~345</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>170</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's DSGN_IRPTV1 ROUND-33 ANALYSIS section 1 ("the pair's packet carries the count the row says is unmeasured") and the CTO ROUND-170 ANALYSIS section 4 (msg 6739) | **Decomp cell:** `IB-pr-494` (decomposition section 162) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-494` (inlined):** the live 49 Financial holdings builder mints each ACCOUNT node's id from the Schwab custody key (`data/assets/scripts/gold/investor_reporting/holdings_49f.py` :331-339: `hs.opaque_id("account", firm_id, raw_account)` over `dim_balance.account_id`), while the directory's account ids come from `dim_account` (`directory_runner.py`). Nobody has COUNTED how many accounts differ. Produce the count, READ-ONLY, **counts only, no account id, no name, no example in any file, message or log line you keep**.

**What to count (the denominator is every account in the live builder's custody `dim_balance` at its latest custody date):**
- For each account: its NODE id is `hs.opaque_id("account", firm_id, raw_account)`; the DIRECTORY's ids are the set `hs._directory_account_ids(s3, bucket, firm_id)` returns (the landed directory, `holdings_snapshot.py:1290`). Classify each account as `equal` (the node id IS in the directory's set), `differs_resolvable` (the node id is not in the set but `hs.opaque_id("account", firm_id, hs._pad10(raw_account))` is) or `differs_unresolvable` (neither is).
- Split by STATE as the builder itself decides it: `served` (the account's ACCOUNT node is built and not refused), `refused` (in the builder's `refused` list: a row for a node refused), `withheld` (the account's drill is withheld: the builder's `withheld` list / `drill_withheld`). Read `build_49f_actual` (`holdings_49f.py:286`) to see where each list is filled. If the three states do not partition the accounts as the builder fills them, say so in `not_established` and state how you partitioned.
- If no directory has landed (`_directory_account_ids` returns None), record `directory_present` false and classify nothing as `equal`: put every account in `differs_unresolvable` and say so in `not_established`.

**How:** write ONE script `mismatch_count.py` in your deliverables folder that imports the builder module read-only (`sys.path` to `data/assets/scripts/gold/investor_reporting`), reads S3 with the default credentials through `boto3` GET/HEAD/LIST calls ONLY (the builder's own source reads; no PutObject, no write verb anywhere in the file), and prints and writes ONLY the counts. Prefer calling `build_49f_actual` itself (it reads S3 and returns nodes, census, refused and withheld in memory; check that it makes no S3 write before running it; if it writes or you cannot run it read-only, STOP and file a row). Keep every account id in memory only; delete any scratch you create.

**Write** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~345/IB170-3_node_id_mismatch_count.json`: `{as_of: "YYYY-MM-DD" (the builder's custody date), directory_present: true|false, denominator: <int accounts>, states: {served: {n, equal, differs_resolvable, differs_unresolvable}, refused: {...}, withheld: {...}}, not_established: ["..."]}`. Counts and words only: no id, no number longer than 8 digits, no client name, no key named account, ids, nodes or examples.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB170-3-AC1" cell_refs="IB-pr-494"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-3-AC1</invocation><expect>IB170-3-AC1 PASS</expect></criterion>
<criterion id="IB170-3-AC2" cell_refs="IB-pr-494"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-3-AC2</invocation><expect>IB170-3-AC2 PASS</expect></criterion>
<criterion id="IB170-3-AC3" cell_refs="IB-pr-494"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-3-AC3</invocation><expect>IB170-3-AC3 PASS</expect></criterion>

<expected_criteria>IB170-3-AC1, IB170-3-AC2, IB170-3-AC3</expected_criteria>

What the checks grade: AC1 the record's arithmetic closes (each state's `n` equals its three parts; the three states sum to `denominator`; `as_of` and `directory_present` present); AC2 the record carries no id, no long digit run and no identifying key; AC3 your script file holds no write verb. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and nothing else. READ-ONLY: S3 GET/HEAD/LIST only; no write of any kind to AWS; no vendor call; no edit of any product file.
- **Refusal clause:** STOP, file a row, write no record, on any of: an AWS read refused (say which bucket class and the error code, never a key), a builder function that writes, a denominator of 0, or any need to print an account id to proceed.
- **Row ids** are `IRPT_BCKEND-D2-W345-S<k>` (the next free `k`).
- **Commit** on your worktree branch per your definition (the script, the record, the proof, the rows); ASCII only. Report once, under 150 words, with the counts only.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~345/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-494.count-49f-node-ids-that-differ-from-the-directory.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 162 (round 170, workstream ~P), cell `IB-pr-494`.
<owned_cells>IB-pr-494</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB170-3-AC1, IB170-3-AC2, IB170-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~345/IRPT_BCKEND.TO-IB-pr-494.count-49f-node-ids-that-differ-from-the-directory.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- read-only: S3 GET/HEAD/LIST of the builder's own custody sources and the landed directory object of one firm bucket, by the builder's code path in memory; no write, no deploy, no new resource. Class SERVED because it reads served client data (account keys stay in memory; only counts are kept).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the reads use the default credentials the worker's shell carries (the same path IB-pr-482's worker used for the served gold). An AccessDenied is a STOP, not a request for a grant.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p170_cells.py dry-run at base on dell2 2026-10-13 ~02:2xZ: IB170-3 AC1, AC2 and AC3 FAIL (no record, no script). The cut has no positive control for the arithmetic beyond the shape rules; AC3 is a text scan of the script.
lane: the paths block IS the grant; worker slot ~345 of IRPT_BCKEND. Class SERVED.
</preflight>
