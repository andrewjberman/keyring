# TO IRPT_BCKEND.TO-IB-pr-405 -- the owned analysis read returns the persist inputs (artifact_id, composition_sha256, retention policy, persisted report index); svc-custody-statement reads it for cottonwood only

<to_id>IRPT_BCKEND.TO-IB-pr-405</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~268</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>106</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 3088, IRPT_DASHBD ADDENDUM 9.2 (2) (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUNDS_30_31_20261009.md`), on ~D2 msg 3084 / row W61-S2 | **Decomp cell:** `IB-pr-405` (decomposition section 99) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The cell.** IRPT_DASHBD's custody-statement runner (DB-b-85) reads the `irpt-requests` DynamoDB table directly to get a request's
`artifact_id` and composition hash. The CTO ruled that it gets no table grant. Instead, IRPT's owned served read returns those values.
Root: `C:/dev/wk-irpt-bckend-268/infra/aws/lambda/investor-reporting/`.

**Build:**
- **Where:** extend ONE existing owned read in `ops/owned_report.py` (`OwnedAnalysisReader`) or the owned request read in
  `ops/owned_requests.py`, and its route in `ops/entry.py`. Pick the one whose record already holds these values. Add NO new route.
- **What:** its response gains one object, `persist_inputs`, with exactly four members:
  - `artifact_id` (`ART-<64 hex>`, the retained request the persist step takes; see `export/custody_persist.py` `_request`);
  - `composition_sha256` (the record's `composition_ref.sha256`);
  - `retention_policy` (the policy id the record is retained under, e.g. `irpt-custody-x10-v1`; read it, never type it);
  - `report_index` (the persisted report's index entry: `report_id`, `revision`, `retention_ref`), or `null` when nothing is persisted.
- **Authorization:** re-authorized per request through the read's existing path (owner binding, firm binding, retention `require_live`).
  Another firm is REFUSED, and a non-owner is REFUSED.
- **svc-custody-statement** (`_authz/served.py`, `SVC_CUSTODY_STATEMENT_OPERATIONS`): it may read this ONE operation, bound to cottonwood.
  - If the operation is not already in its set, add only that one operation. The CTO authorized exactly this (msg 3088).
  - Never give it any-firm or ALL reach; its firm stays the registry's cottonwood.

**Tests** (names contain `persist_inputs`, at least 5), in `ops/tests/` and `_authz/tests/test_svc_custody_statement.py`:
1. the owner reads all four members;
2. another firm is refused;
3. a non-owner in the same firm is refused;
4. svc-custody-statement reads cottonwood;
5. svc-custody-statement with any other firm claim is refused.

**Release packet** (no upload) in your deliverables folder:
- `IB106-1_release_census.json`: `{pin, build_only:{rc,tree_clean}, artifacts:[{function, built_sha256, live_before, changed_members}]}`.
  List every function that packages a changed member, from `infra/aws/lambda/ci/lambda-source-map.json`. BUILD_ONLY twice,
  byte-identical, from a clean tree.
- `IB106-1_release_replay.json` `{arms:[{name, verdict, negative_control}]}`, live zip vs built zip, at least:
  - existing callers of the extended read: `identical` apart from the new member;
  - another firm: refused on both sides;
  - svc-custody-statement for cottonwood: `expected-diff` (refused live, admitted built);
  - one negative control.
- `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-405.md`: blast radius, Branch A, Branch B (rollback version per function), the pin and every built
  sha256.

Criteria (run each from the worktree root C:/dev/wk-irpt-bckend-268):

<criterion id="IB106-1-AC1" cell_refs="IB-pr-405"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r106/p106_cells.py" . IB106-1-AC1</invocation><expect>IB106-1-AC1 PASS</expect></criterion>
<criterion id="IB106-1-AC2" cell_refs="IB-pr-405"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r106/p106_cells.py" . IB106-1-AC2</invocation><expect>IB106-1-AC2 PASS</expect></criterion>
<criterion id="IB106-1-AC3" cell_refs="IB-pr-405"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r106/p106_cells.py" . IB106-1-AC3</invocation><expect>IB106-1-AC3 PASS</expect></criterion>

<expected_criteria>IB106-1-AC1, IB106-1-AC2, IB106-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code, tests, BUILD_ONLY, offline replays; no upload, apply or deploy. AWS reads only.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test. If the four
  values cannot be read from the record the read already loads, that is a row, not a table grant.
- **Row ids** are `IRPT_BCKEND-D2-W268-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~268" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~268@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~268 <0.9.0_WK_IRPT_BCKEND~268@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/ops/owned_report.py
infra/aws/lambda/investor-reporting/ops/owned_requests.py
infra/aws/lambda/investor-reporting/ops/entry.py
infra/aws/lambda/investor-reporting/ops/tests/
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_svc_custody_statement.py
infra/aws/lambda/investor-reporting/_contracts/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~268/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-405.persist-inputs-owned-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 99 (round 106, workstream ~P), cell `IB-pr-405`.
<owned_cells>IB-pr-405</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB106-1-AC1, IB106-1-AC2, IB106-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~268/IRPT_BCKEND.TO-IB-pr-405.persist-inputs-owned-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the route and operation extended, the four values' sources, the test names, the census (functions
+ built sha256), the replay verdicts, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one owned read's response gains persist_inputs; svc-custody-statement gains at most that one operation, cottonwood-bound (CTO msg 3088); every function packaging a changed member is censused in the packet; no upload in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the CTO refused a table grant (ADDENDUM 9.2 (2)); the read uses its existing grants.
comp-routes: DECLARED-NOT-APPLICABLE -- no new route; an existing owned route's response gains one member.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p106_cells.py dry-run at base (clean worktree at box/dell2 HEAD) on dell2 2026-10-09 ~10:2xZ: AC1 FAIL (0 selected), AC2 PASS (control: ops 277, _authz 303 with test_every_entry_carries_the_published_route_table_it_serves excused by name, D2-S43), AC3 FAIL (no census); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO msg 3088).
</preflight>
