# NFRA_MCPINDEX task order -- `MX-c-6` -- the ONE catalog holds every need in Alyssa's two briefs: 29 entries, served or not, each with its owner, its class and the browser workflow it retires

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~29</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- catalog content and its emitter only; no role, policy or grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-c-2/MX-d-6 catalog-entry pattern; the battery dry-run is the control (c6.AC1 reads 0 of 29 at base).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-6` (round 8; PRD v0.7 @b06af7c0d2 FWD-12, FWD-15, FWD-17, FWD-18, contracts 1, 5, 6; decomposition section ROUND 8)

**What the catalog lacks, measured at the base.** `opal_discover` answers "not catalogued" for cost basis, a YCharts
stress test, a statement PDF and an attachment download. No catalog row names a YCharts tool. The catalog holds
data ROWS but no NEEDS, so a need with no tool cannot be said at all. PRD v0.7 contract 1: "A need with no tool is
catalogued as a GAP entry: its owner, or `unowned`, and no tool."

**The 29 needs (brief `docs/briefs/mcpindex-alyssa-workflows-midstream-brief-20261009.md` @3455b1783a Part IV.A,
measured 2026-10-09 by `4.0.0_SA_CRO~Z`; your input).** Contract 5: you may split an entry finer, but never drop one
without a GAP row.

| id | need | status | tool | owner | retires |
|---|---|---|---|---|---|
| E-1 | account number and title lookup, crosswalk from `account_ref` | GAP | `schwab_query` (dim_account, NFRA_OPLGTW v2.0) | NFRA_OPLGTW | W1, W2, W4 |
| E-2 | balances on any past date, 13 months or more | PARTIAL (30 days) | `schwab_query` | NFRA_OPLGTW | W1, W5 |
| E-3 | positions on any past date | PARTIAL (30 days) | `schwab_query` | NFRA_OPLGTW | W1, W2 |
| E-4 | lot-level unrealized cost basis as of a date | GAP | none yet | NFRA_OPLGTW | W1, W2, W4 |
| E-5 | realized gain/loss by date range, ST/LT | GAP | none yet | NFRA_OPLGTW | W1, W4 |
| E-6 | transactions with a flow tag (deposit, withdrawal, journal, transfer, fee) | PARTIAL (no tag) | `schwab_query` | NFRA_OPLGTW | W1, W4 |
| E-7 | Tax SMA master 0840-3355 | GAP | none yet | NFRA_OPLGTW | W1 |
| E-8 | Black Diamond account data | GAP (fees only today) | `blackdiamond_list_fees` | NFRA_OPLGTW | W1 |
| E-9 | statement PDFs by account and period | GAP | none | unowned | W1 |
| E-10 | corporate actions | GAP | none | unowned | W1, W4 |
| E-11 | sector per security | GAP | none | unowned | W1 |
| E-12 | account performance / TWR | GAP | none | unowned (outside Andrew's "the right information") | W1 |
| E-13 | model performance by period vs benchmark | SERVED | `mdpf_get_model_benchmarks` | -- | W6, C2 |
| E-14 | model daily return series | SERVED | `gateway_query_catalog` | -- | C2 |
| E-15 | AUA by partner and basis, with history | SERVED | `mdpf_get_aggregate_aua` | -- | W5, C2 |
| E-16 | account counts with month-end history | SERVED | `mdpf_get_aggregate_aua` | -- | W5, C2 |
| E-17 | AUM by model | SERVED | `mdpf_get_aum_metrics` | -- | W5 |
| E-18 | market overview and attribution pages | PARTIAL | none as an MCP tool (`tools/portal_lookup.py` is a repo tool) | NFRA_MCPINDEX | C2 |
| E-19 | index or security returns and prices | PARTIAL | `ycharts_snapshot_metrics`, `ycharts_time_series` | YCharts integration owner | C1, W3 |
| E-20 | YCharts Overview / Comparison / Multi-Comp report for client holdings | GAP | none | unowned | C1 |
| E-21 | save a mail attachment to a folder | DENIED (write class) | `save_email_attachment_to_site` | write-class grant | C6, W3 |
| E-22 | download a SharePoint file that does not sync | PARTIAL (read in-channel only) | `read_site_file` | NFRA_MCPINDEX | C6 |
| E-23 | move or delete mail, create a folder | GAP (write) | none | write tools (deferred) | C4 |
| E-24 | send a Teams message as herself | UNMEASURED (her grant not read) | `send_chat_message` | write-class grant | C5 |
| E-25 | Bloomberg prices and reference data | SERVED through its own queue | none as an MCP tool (the `bloomberg_standing_read` channel) | -- | C1 |
| E-26 | Microsoft Forms responses (YCharts request form) | GAP | none | unowned | none: no browser workflow (her brief section 6) |
| E-27 | Orion compliance submissions | GAP | none | unowned | none: not browser-driven (her brief, "Not browser-driven") |
| E-28 | month-end AUM and account counts by master (custodian side) | GAP | none | unowned | W5 |
| E-29 | advisor account review from an emailed SAC link | GAP until E-1 lands | `schwab_query` | NFRA_OPLGTW | W2 |

**The live errors for E-19 (row NFRA_MCPINDEX-Z-S85, measured 2026-10-09 ~03:4xZ, the session live with
`ycharts_freshness` ok HTTP 200):** `ycharts_time_series` returns HTTP 403 with 0 points, and
`ycharts_snapshot_metrics` returns HTTP 200 with its value keyed to symbol `"None"`. FWD-15's ACCEPT: "a vendor tool
that fails live reads PARTIAL with its error, never SERVED".

**The act:**
1. **A `needs:` section in the ONE catalog**, emitted by the ONE writer (C1). Author one source file per need as
   `workflows/atom_decomposition/catalog_entries/need_<id>.yaml` (for example `need_E-13.yaml`). Extend
   `workflows/atom_decomposition/emit_catalog_v02.py` to:
   - validate need files against a typed schema;
   - write a top-level `needs:` list into `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`;
   - REFUSE an invalid file, the way it refuses an invalid silver entry (`EMIT REFUSED`).
   NEVER hand-edit `DATA_CATALOG.yaml`.
2. **Each emitted entry carries:**
   - `id`, `need`, `source` (the dataset or system), `status` (SERVED | PARTIAL | GAP | DENIED | UNMEASURED);
   - `tool`: the one MCP tool that answers it, or null. Where the table names two tools, pick the primary and list
     the rest in `also_tools`. A repo tool or channel is NOT an MCP tool: tool null, said in `note`;
   - `owner`: a project code, `unowned`, or null when SERVED;
   - `retires`: a list of C1-C8 / W1-W6. When empty, add `retires_none` with the reason;
   - `op_class` (read | write);
   - `live_error` for a PARTIAL vendor entry (E-19);
   - `example_questions` in her own vocabulary, so discover can reach the entry by its own text. MX-d-8 makes
     discover read this section; you give it the words.
3. **Schema tests** in `workflows/atom_decomposition/tests/test_catalog_need_entries.py`, the three named in c6.AC2.
   The emitter's existing tests still pass.
4. **The 8 unowned gaps** (E-9, E-10, E-11, E-12, E-20, E-26, E-27, E-28) are catalogued and never built (contract 6).

**Emitter cautions (rows Z-W21-S7, Z-S57; MX-d-6 found these):**
- The emitter reads `CENSUS_DIR` and `PORTAL_API` (fixed defaults; `--census-dir` and `--portal-api` override them).
  With the census absent it SILENTLY writes `"NONE -- uncensused (L-14)"` over existing rows.
- A linked worktree has no portal submodule and may lack the census. Pass both flags, pointing READ-ONLY into the main
  tree: `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/org/tier0_utility/0.0.3_BG_BBGTerminal/refs/census` and
  `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/src/api`.
- After you emit, `git diff` the catalog. Every row outside `needs:` must be unchanged. A row that changed without cause
  is a BLOCKING row; do not commit it.

## 2. BOUNDS

1. You write the catalog sources, the emitter and the regenerated catalog only. You write NOTHING under
   `app/integrations/opal_discover/`; MX-d-7 owns that, running in parallel.
2. No tool's behaviour, role, grant or route changes. No new tool name: every `tool` you name is already registered
   (c6.AC3).
3. Nothing under `data/cot/`. No push. No deploy (MX-r-9 releases this). REFUSE a criterion you cannot meet as written,
   and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/catalog_entries/
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/tests/test_catalog_need_entries.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~29/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W29-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%Y-%m-%dT%H:%MZ`), never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/c6.AC1.sh; echo "exit=$?"</invocation><expect>needs entries 29 of 29 (ids exact=True, duplicates=0); violations 0; unowned 8 of 8 (exact=True) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/c6.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round8/checks/c6.AC3.sh; echo "exit=$?"</invocation><expect>classified tool sets read 4 of 4; needs naming a tool N >= 1; unknown 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~29/NFRA_MCPINDEX.TO-MX-c-6.catalog-needs-entries.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message, naming:
- the catalog diff summary: the `needs:` section added, and any other row that changed, with why;
- the emitter inputs you provisioned;
- every entry you split or re-statused against the table above, and why.
Do not edit this task order beyond your status flip.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-8 chain head of [MX-c-6 -> MX-d-8], worker ~29, in parallel with MX-d-7 (a
disjoint write set: decomposition A2 @7a37c5b906). Battery dry-run at base ac135370d2 (`round8/checks/`):
- c6.AC1 FAIL as expected: 0 of 29.
- c6.AC2 FAIL as expected: test file absent.
- c6.AC3 FAIL as expected: 0 needs name a tool.

Instrument controls:
- c6_tools.py first read the wrong source. Its AST over `integration.py` saw 7 tools and missed
  `mdpf_get_model_benchmarks` and `send_chat_message`. Fixed to read the gateway's own `TOOL_CLASSES` sets: 70 tools.
- On a planted fixture of 3 real tool names and 1 fake, it reports unknown 1, naming the fake.

<status>complete</status>
<round>8</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
