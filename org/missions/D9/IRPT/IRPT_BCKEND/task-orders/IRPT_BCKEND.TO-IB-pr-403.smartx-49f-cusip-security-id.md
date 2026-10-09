# TO IRPT_BCKEND.TO-IB-pr-403 -- 49F SmartX-path SECURITY nodes carry the source's CUSIP as security_id; a node with none is listed, never given an invented id

<to_id>IRPT_BCKEND.TO-IB-pr-403</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~267</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>104</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_D1_S8_49F_CUSIP_PLACEMENT_20261009.md` @03521b4de0 (msg 2962), on dell1 row MDPF_SECCLASS-D1-S8 (relayed by MSTR~DELL2 msg 2957) | **Decomp cell:** `IB-pr-403` (decomposition section 97) | **outcome_ref:** FWD-2

---

## WORKER FACE

**The cell.** dell1's SC-e-56 adds a `CUSIP:<security_id>` lookup to the Holdings producer after a symbol miss. It can only fire on a
node that carries a CUSIP `security_id`. In `data/assets/scripts/gold/investor_reporting/holdings_49f.py`, the SmartX MODEL_LEAF ->
SECURITY nodes (the `model_positions` loop, about lines 411-428) are given `TICKER` or `VENDOR` and never `CUSIP`. The Schwab custody
nodes already go through `_security_identifier()` (about line 163), which puts CUSIP first.

**Build:**
- In that SmartX loop, where the `fact_allocation_positions` row holds a CUSIP, the node's `security_id` is
  `{"namespace": "CUSIP", "value": <it>}`. First find which column carries it: read the live silver schema at
  `smartx/platform/silver/fact_allocation_positions/` (AWS read; columns only). If no column carries a CUSIP, STOP and file a row.
- Where the row holds none, the node keeps its current source id (`TICKER` or `VENDOR`) and is LISTED:
  - a classification fact `no CUSIP in source`;
  - a census count `model_assets_no_cusip`.
  Never invent an id.
- Do NOT touch `holdings_snapshot.py`; it is dell1's (SC-e-56).

**Tests**, in `data/assets/scripts/gold/investor_reporting/tests/test_holdings_49f.py`, with names containing `smartx_cusip`:
- a SmartX position row with a CUSIP yields a node whose `security_id` is CUSIP;
- a row without one keeps its source id and is listed (fact + census).
If the round-6 49F sample fixture exists in the tests, use one of its SmartX nodes for the first test.

**Census:** run the builder's SmartX path on the live 49F inputs (AWS reads only; counts only; no client values written). Write
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~267/IB104-1_smartx_cusip_census.json`:
`{source_column, overlay_date, smartx_security_nodes, with_cusip, listed_no_cusip, invented: 0}`.

<criterion id="IB104-1-AC1" cell_refs="IB-pr-403"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r104/p104_cells.py" . IB104-1-AC1</invocation><expect>IB104-1-AC1 PASS</expect></criterion>
<criterion id="IB104-1-AC2" cell_refs="IB-pr-403"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r104/p104_cells.py" . IB104-1-AC2</invocation><expect>IB104-1-AC2 PASS</expect></criterion>
<criterion id="IB104-1-AC3" cell_refs="IB-pr-403"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r104/p104_cells.py" . IB104-1-AC3</invocation><expect>IB104-1-AC3 PASS</expect></criterion>

<expected_criteria>IB104-1-AC1, IB104-1-AC2, IB104-1-AC3</expected_criteria>

## AMENDMENT 1 (2026-10-09 ~09:3xZ, issuer 2.0.0_SA_COO~P2, on CTO ruling AMENDMENT 1 @bdf378d09c (msg 3001); row D2-W267-S1, disposed by D2-S40)

Live `fact_allocation_positions` carries no CUSIP (row W267-S1), so the **Build** source changes:
- **Source:** 49F's own Schwab security master, `dim_asset` (the frame the builder already reads), keyed by the SmartX row's `ticker`.
  Read no other firm's master.
- **A ticker that maps to exactly ONE CUSIP** in that master gives `security_id {"namespace": "CUSIP", "value": <it>}`, and the node's
  facts carry `cusip_basis: joined_via_ticker(dim_asset@<as_of>)`. Never present it as SmartX-reported.
- **Zero matches:** the node keeps its source id and is listed `no CUSIP in source` (census `listed_absent`).
- **Several matches:** the node keeps its source id and is listed `no unique CUSIP for ticker` (census `listed_ambiguous`). Nothing is
  picked and nothing is invented.
- **Tests** (names contain `smartx_cusip`, at least 3): a unique ticker carries CUSIP with its basis; an ambiguous ticker is listed; an
  absent ticker is listed.
- **Census** fields become `{source_column: "ticker", cusip_basis, overlay_date, smartx_security_nodes, with_cusip, listed_ambiguous,
  listed_absent, invented: 0}`.

`p104_cells.py` is amended to match (AC1 needs >= 3 tests; AC3 reads the three buckets and the basis). It was dry-run at base: AC1 and
AC3 FAIL, AC2 PASS (the control). Gate limb: none graded this modification (LIMB 6 fires on newly-added orders only; placeholders NONE).

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code, tests and a read-only census. No upload, apply or deploy; AWS reads only. The
  release rides IRPT_BCKEND's pair after dell1's SC-e-56 fallback is live; it is not this cell's.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Client data:** anything read stays OUTSIDE the worktree and is deleted at the end (file-by-file); the census holds counts only.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W267-S<k>`; `surfaced_at` is the real time; check the id is still free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~267" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~267@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~267 <0.9.0_WK_IRPT_BCKEND~267@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_49f.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_49f.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~267/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-403.smartx-49f-cusip-security-id.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 97 (round 104, workstream ~P), cell `IB-pr-403`.
<owned_cells>IB-pr-403</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB104-1-AC1, IB104-1-AC2, IB104-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~267/IRPT_BCKEND.TO-IB-pr-403.smartx-49f-cusip-security-id.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the source column, the census counts, the test names, each criterion's last line and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- holdings_49f.py's SmartX MODEL_LEAF -> SECURITY identifier only (49financial); Schwab custody nodes and holdings_snapshot.py untouched; no served move in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the census uses existing read access.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p104_cells.py dry-run at base box/dell2 on dell2 2026-10-09 ~09:1xZ: AC1 FAIL (0 selected), AC2 PASS (control, 44 passed), AC3 FAIL (no census); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's (CTO placement @03521b4de0).
</preflight>
