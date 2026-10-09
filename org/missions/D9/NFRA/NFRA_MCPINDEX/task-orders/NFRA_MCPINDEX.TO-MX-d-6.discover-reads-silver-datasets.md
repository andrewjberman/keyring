# NFRA_MCPINDEX task order -- `MX-d-6` -- opal_discover reads `silver_datasets`, Schwab gets catalog rows, and every catalog row is graded by REACHABILITY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-d-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-d-6</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~22</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy changes; discover's reads are unchanged in kind (catalog file + S3 HEAD).
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-d-3/d-4/d-5 discover pattern; the battery dry-run is the control.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (discover's existing S3 HEAD on served objects).
</preflight>

## 1. THE CELL -- `MX-d-6` (round 6; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round5.md` @1edec80f63, section 5 item 1; rows Z-W21-S22, Z-W15-S3)

**The defect, measured.** Live on the gateway, `opal_discover("what fees did Black Diamond charge")` returns
`catalogued: false`, 0 matches. Neither the tool nor the catalog row is missing: `blackdiamond_list_fees` is served, and
its row `blackdiamond_fees` sits at `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml:1363` with
`read_tool: blackdiamond_list_fees`. The row is unreachable because of where it sits:
- `discover()` (`app/integrations/opal_discover/integration.py:307`) iterates only `cat.get("channels")` artifacts
  (:316-317).
- `_purpose_built_tool()` (:181-188) reads `portal_datasets` only to map an accessor to its `read_tool`.
- `silver_datasets` (header `DATA_CATALOG.yaml:1359`) is read by nothing (0 hits in the file).
- Schwab has NO catalog row at all. Its 4 served datasets are `dim_position`, `dim_balance`, `dim_asset` and
  `dim_transaction` (`app/integrations/schwab/datasets.json:5-169`). Its 5 tools are `TOOL_NAMES` at
  `schwab/integration.py:70-71`: `schwab_get_access`, `schwab_list_files`, `schwab_describe_dataset`, `schwab_query` and
  `schwab_prepare_download`.

**The CTO's ruling (section 3, Z-W21-S22): FIX THE READER, NOT THE ROW.** Do not move the BD row into another section.

**The act:**
1. **`opal_discover` reads `silver_datasets` beside the sections it reads today.** A `silver_datasets` row matches on its
   own `entity`, `business_meaning` and `example_questions`. Its `next_tool` is its `read_tool` (`kind: mcp_tool`).
   - The row carries no S3 key, so `served_written_at` is honestly absent for it, never invented.
   - Its caveats and `firm_scope_rule` travel with the match, as for every other row.
   - Firm scope: a `firm-scoped` silver row is servable to the principal kinds the existing gate admits for that rule.
     Reuse the gate; do not write a second one.
2. **Schwab catalog rows**, one per served dataset (4), each with `read_tool` a real `TOOL_NAMES` member. Use
   `schwab_query` for a data question, unless the dataset's own surface says otherwise.
   - Author them as `workflows/atom_decomposition/catalog_entries/schwab_<dataset>.yaml`, on the
     `catalog_entries/blackdiamond_fees.yaml` pattern.
   - Regenerate `DATA_CATALOG.yaml` with `workflows/atom_decomposition/emit_catalog_v02.py`. NEVER hand-edit the
     catalog.
   - Schwab is FIRM-SCOPED: per-master data under per-principal grants. `never_sum_rules` and caveats say so.
3. **Reachability for every row** (Z-W15-S3, folded in). At the base, `mdpf_get_model_benchmarks`'
   `portal_mdpf_model_benchmarks` row is ALSO unreachable: discover asked each of its 2 `example_questions` names no tool.
   - Make it reachable through its catalog entry's own vocabulary or example questions, or through discover's ranking
     if that is the cause.
   - Measure first; do not guess.
4. **Retire the MX-d-5 assertion** (CTO section 3, Z-W21-S15):
   - `tests/test_opal_discover.py:390` `assert etf["catalogued"] is False` is now false by design, because MX-t-10's
     ETF row is Andrew-acknowledged (R20 X11).
   - Replace it with an assertion that the ETF ask names `etfs_get_positioning`. Keep the S&P half (:389).
   - Add tests for the silver read and for one Schwab ask.

**Emitter cautions (rows Z-W21-S7, Z-S57):**
- `emit_catalog_v02.py` reads a census directory (`CENSUS_DIR`, :386) and a portal API path (`PORTAL_API`, :429).
  These are fixed paths, not arguments. With the census absent it SILENTLY writes `"NONE -- uncensused (L-14)"` over
  existing rows (`census_ref_for`, :410-422).
- Before you emit, confirm those inputs exist in your worktree (copy them read-only from
  `C:/Users/Opal Bloomberg/Desktop/ajb_workspace` if the worktree lacks them).
- After you emit, `git diff` the catalog. Every untouched row's `census_ref` must be unchanged. A row that changed
  without cause is a BLOCKING row; do not commit it.
- MX-x-4 (another worker) is changing the emitter's CLI this round. You RUN it at your base; you never edit it.

**Naming gate:** a new literal (an S3 key or a bucket) refused by `.tools/naming-gate.py` at commit is a BLOCKING row on
that criterion, never an override. The Schwab rows should need no S3 literal (no `s3_key` field, like the BD row).

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-01 ~09:4xZ) -- rules row Z-W22-S1 (OBSERVATION, ARMED, issuer-owned): FAIL
CLOSED on cross-firm visibility.**
- A `silver_datasets` row carries no firm field. Reusing `catalog_gate.gate()` with its `firm_scope_rule` therefore
  serves a firm-scoped row to EVERY known firm principal (`KNOWN_FIRMS`, `catalog_gate.py:40`). A cottonwood principal
  would see the 49financial-only BD fees row. cot and bd are separate firms (CLAUDE.md rule 13).
- **Ruling:** until the catalog carries a firm field, discover serves a firm-scoped `silver_datasets` row ONLY to the
  `OPAL_INTERNAL` principal (`catalog_gate.py:39`). Every firm principal gets no match for it, never a match with a
  caveat.
- Add one test proving both arms:
  - `OPAL_INTERNAL` still gets `blackdiamond_list_fees` and `schwab_query`;
  - each of the 3 `KNOWN_FIRMS` gets no silver match for the same two asks.
- d6.AC1-AC3 are unchanged; they run as `OPAL_INTERNAL`.
- The firm field in the C1 schema (emitter + README) is carried to the round-7 enrichment list. It is not cut this
  round, because the emitter is in MX-x-4's write set.
- **Continuation order for the worker:**
  1. `git merge CLOUD`.
  2. Set this order's `<status>` to `in_progress` on your branch. Your earlier `complete` flip withdrew your own grant.
  3. Implement A1, re-run AC1-AC3 and the new test.
  4. Re-validate the instance, flip to `complete`, and commit.
- Graded by: no gate limb graded this modification (LIMB 6 grades only a newly-added order; GATE (viii) finds
  `<placeholders>NONE</placeholders>`).

## 2. BOUNDS

1. No change to any tool's behaviour, any role, grant or identity, `query_v0`, or the HTTP route.
2. `catalog_gate.py` changes only if discover cannot read `silver_datasets` without it. If it does change, `query_v0`'s
   catalog behaviour stays byte-equal in effect, and your report names the change.
3. Nothing under `data/cot/`. No push. No deploy (MX-r-8 releases this). REFUSE a criterion you cannot meet as written,
   and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/app/graphql_plumbing/catalog_gate.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
workflows/atom_decomposition/catalog_entries/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W22-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-d-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/d6.AC1.sh; echo "exit=$?"</invocation><expect>OK: BD fees ask ... blackdiamond_list_fees; OK: Schwab positions ask ... schwab_*; routed 2 of 2 asks -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-d-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/d6.AC2.sh; echo "exit=$?"</invocation><expect>OK: ETF positioning ask ... etfs_get_positioning; ROUTING: n of 27 with n >= 24 (floor 24) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-d-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/d6.AC3.sh; echo "exit=$?"</invocation><expect>every row OK:, none UNREACHABLE:; REACHABILITY: N of N catalog rows naming a read tool are reachable (N >= 10: 5 portal + 1 BD + 4 Schwab) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/NFRA_MCPINDEX.TO-MX-d-6.discover-reads-silver-datasets.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message, naming:
- the catalog diff summary: rows added, and rows changed with why;
- the emitter inputs you provisioned.
Do not edit this task order beyond your status flip.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-6 item 1 (thread-relevant, so first). Battery dry-run at base (CLOUD
81887e8ae8):
- d6.AC1 FAIL as expected (routed 0 of 2);
- d6.AC2 PASS as expected (control: ETF routed; ROUTING 24 of 27);
- d6.AC3 FAIL as expected (REACHABILITY 4 of 6; BD fees and model_benchmarks UNREACHABLE).
Chain head of [MX-d-6 -> MX-g-3 -> MX-r-8 -> MX-v-7], worker ~22.

<status>complete</status>
<round>6</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
