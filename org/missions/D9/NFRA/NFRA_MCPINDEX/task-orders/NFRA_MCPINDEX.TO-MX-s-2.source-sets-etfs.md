# NFRA_MCPINDEX task order -- `MX-s-2` -- trace the source set of each of the 18 tools of opal-data-etfs: what the tool's code can read, one cited source per dispatch branch

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-s-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-s-2.source-sets-etfs</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~72</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-s-2` (round 23, workstream GATEWAY; PRD v0.18 FWD-23; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). The routing table can only be as good as the trace it is joined to. Round 22's links and `bucket_source` claims are what the code is SUPPOSED to read; this cell reads the code.

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~72/source_sets_etfs.json`, a SOURCE SETS file with exactly the 18 tools in the table below, once each, `scope` set to `etfs`.

| tool | channel | linked rows in the census (claim) | bucket and bucket_source in members.yaml (claim) |
|---|---|---|---|
| `etfs_compare_peers` | opal-data-etfs | opal_data_etfs_gold_buying_trend, opal_data_etfs_gold_holding_contribution | none |
| `etfs_get_coverage` | opal-data-etfs | opal_data_etfs_gold_holdings_coverage, opal_data_etfs_gold_input_census | none |
| `etfs_get_fund_bloomberg_characteristics` | opal-data-etfs | opal_data_etfs_silver_bbg_derived_geo_allocation, opal_data_etfs_silver_bbg_derived_sector_allocation, opal_data_etfs_silver_bbg_derived_summary, opal_data_etfs_silver_bbg_fund_daily | none |
| `etfs_get_fund_flows` | opal-data-etfs | opal_data_etfs_gold_flow_reconciliation | none |
| `etfs_get_fund_holdings` | opal-data-etfs | opal_data_etfs_gold_holding, opal_data_etfs_silver_holdings | none |
| `etfs_get_fund_nav_history` | opal-data-etfs | opal_data_etfs_silver_netassets_daily | none |
| `etfs_get_fund_snapshot` | opal-data-etfs | opal_data_etfs_silver_snapshots | none |
| `etfs_get_fund_trades` | opal-data-etfs | opal_data_etfs_gold_trade_schedule | none |
| `etfs_get_monthly_report` | opal-data-etfs | opal_data_etfs_platinum_monthly_ownership_report | none |
| `etfs_get_new_securities` | opal-data-etfs | opal_data_etfs_gold_mdpf_new_securities | none |
| `etfs_get_ownership_rollup` | opal-data-etfs | opal_data_etfs_platinum_etf_ownership_dashboard | none |
| `etfs_get_partner_ownership` | opal-data-etfs | opal_data_etfs_gold_daily_partner_ownership | none |
| `etfs_get_peer_group_members` | opal-data-etfs | opal_data_etfs_gold_peer_group_map | none |
| `etfs_get_research_notes` | opal-data-etfs | opal_data_etfs_gold_research_hypotheses | none |
| `etfs_get_rival_fund_holdings` | opal-data-etfs | opal_data_etfs_gold_canonical_shape | none |
| `etfs_get_rival_page_status` | opal-data-etfs | opal_data_etfs_platinum_rivalfunds_page | none |
| `etfs_get_security_reference` | opal-data-etfs | opal_data_etfs_gold_corporate_actions, opal_data_etfs_gold_security_market, opal_data_etfs_gold_security_names | none |
| `etfs_who_holds` | opal-data-etfs | opal_data_etfs_gold_security_universe | none |

### The contract (verbatim from the decomposition; it is the whole specification)

**SOURCE SETS** `gateway_source_sets/1` (the TRACE of what each tool's code can read; a data file written by a worker who read the code):
```
{"schema":"gateway_source_sets/1","scope":<free text>,"tools":[{"tool","vendors":[sorted distinct vendors of its sources],
  "sources":[{"kind":"s3"|"store"|"integration"|"graph","bucket"?,"prefix"?,"store"?,"integration"?,"graph"?,"vendor","cite":"app/<file>.py:<line>"}]}]}
```
- One entry per tool of the cell's scope, once. One source per dispatch branch the code can take (a multi-vendor `client_*` tool has one source per vendor branch).
- `s3` carries `bucket` (the bucket id, resolved from the constant or config key the code uses) and `prefix` (the key prefix that branch reads; the empty string only when it reads the whole bucket); `store` carries `store`; `integration` carries `integration`; `graph` carries `graph` (the Microsoft Graph endpoint family).
- `vendor` is the data's owner: the catalog's own vendor values (`schwab`, `blackdiamond`, `orion`, `eclipse`, `smartx`, `commonwealth`, `gateway`, `market`) or `opal` (Opal's own non-client data), `ycharts`, `microsoft`, `bloomberg`, `other`.
- `cite` is `app/<file>.py:<line>` of the line that names the source or the branch that selects it; the cited file must contain the bucket, store, integration or graph string. `bucket_source` in `members.yaml` and the tool's linked rows are index CLAIMS: the trace is checked against them and never copied from them; a disagreement is a surprise row.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json`: the census (read-only; each tool's `indexes` and its channel `segments`).
- `workflows/atom_decomposition/tool_index/members.yaml` and the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (read-only): the claims you check your trace against.
- The gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; `git sparse-checkout add <folder>` is the only sparse change you may make.
1. For each tool in the table, open its definition in the gateway source (`infra/aws/ec2/opal-gateway/app/`: search with the Grep tool for `def <tool>` and the tool name in quotes; integration tools sit under `app/integrations/<name>/integration.py`, harvest tools under `app/harvest_*.py`, client tools under `app/client_*.py`) and FOLLOW THE CODE that serves it until you reach the call that names its source: an S3 bucket and key prefix, a DynamoDB table or other store, an integration endpoint, or a Microsoft Graph endpoint. A tool with dispatch branches (one per vendor, master or firm) gets ONE source per branch. Resolve the bucket id from the constant or config key the code uses (read `app/config.py` and the module constants) and write the bucket id string; write the key prefix that branch reads (the empty string only if it reads the whole bucket). `vendor` is the owner of that data by the vocabulary in the contract. `cite` is `app/<file>.py:<line>` of the line that names the source or selects the branch. THE TRACE IS YOUR READING OF THE CODE: do NOT copy the last two columns of the table (the index claims `bucket_source` and the linked rows) as your answer; they are claims to be checked against your trace, and where your trace disagrees with them you add one OBSERVATION row to the surprise channel naming the tool, the claim and the line (this is the round's routing finding; a Black Diamond row linked on a Schwab tool is the first named case). `vendors` is the sorted distinct set of your sources' vendors.
2. Write the file named in section 4's invocation, then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py` for exactly what each arm grades.
3. Then spot-check yourself: open five of your entries at random and re-read their source line; if one is wrong, fix it. The issuer reads a sample at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/s2.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py`). Read `h_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~72/source_sets_etfs.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~72/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-s-2.source-sets-etfs.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W72-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/s2.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~72/source_sets_etfs.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (18 tools in scope); the schema; every tool in scope exactly once and no other; every tool has at least one source -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/s2.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~72/source_sets_etfs.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every source has the fields of its kind; every vendor is in the allowed vocabulary; every cite is app/<file>.py:<line> naming a real line; the cited file names the bucket, store, integration or graph string; a tool's vendors list equals the set of its sources' vendors -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~72/NFRA_MCPINDEX.TO-MX-s-2.source-sets-etfs.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~72. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). Generated reference files pass `s2.AC1` and `s2.AC2`; the checks prove form and grounding, not that the trace is right, so the issuer reads a sample and the live responses cross-check it (a response citing a source the trace lacks is FAIL misrouted). Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY-TRACE</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
