# NFRA_MCPINDEX task order -- `MX-h-4` -- classify the 13 unindexed member-b tools outside Microsoft 365: each is c with a reason or b with an owner and a reason, grounded in the gateway source

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-h-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-h-4.dispositions-outside-m365</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~65</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-h-4` (round 23, workstream GATEWAY; PRD v0.18 FWD-23; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). Fifty-six member-b tools already have a catalog index and the applier will make them `a`. These 13 have none, so a person must say what each is.

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~65/disposition_non_m365.json`, a DISPOSITION file whose `tools` list holds exactly the 13 tools in the table below, once each, `scope` set to `outside m365`. `member` is `b` or `c` (none of them has an index, so none can be `a`).

| tool | channel | access | write_class | catalog rows linked |
|---|---|---|---|---|
| `graph_cypher` | globgrph | write | UNCLASSIFIED | 0 |
| `harvest_get_article` | opal-data-harvest | read | none | 0 |
| `harvest_get_published_analysis` | opal-data-harvest | read | none | 0 |
| `harvest_list` | opal-data-harvest | read | none | 0 |
| `mdpf_get_security_classification` | dynamodb | read | none | 0 |
| `news_for_security` | opal-data-harvest | read | none | 0 |
| `opal_data_refresh_status` | opal_portal | write | UNCLASSIFIED | 0 |
| `schwab_get_access` | schwab | write | UNCLASSIFIED | 0 |
| `ycharts_fund_series` | ycharts | write | UNCLASSIFIED | 0 |
| `ycharts_risk_return_scatter` | ycharts | write | UNCLASSIFIED | 0 |
| `ycharts_search` | ycharts | write | UNCLASSIFIED | 0 |
| `ycharts_snapshot_metrics` | ycharts | write | UNCLASSIFIED | 0 |
| `ycharts_time_series` | ycharts | write | UNCLASSIFIED | 0 |

### The contract (verbatim from the decomposition; it is the whole specification)

**DISPOSITION** `gateway_disposition/1`: `{"schema":"gateway_disposition/1","scope":<free text>,"tools":[{"tool","member":"b"|"c","owner"?,"reason"}]}`. It covers ONLY tools with no catalog index (an indexed tool is made `a` by the applier without a disposition). `c`: `reason` non-empty, no `owner`. `b`: `owner` (a project code or `unowned`) and `reason` (why no row exists and what would create one), both non-empty. A `reason` is ASCII, at least 40 characters, and ENDS with a source reference `[app/<file>.py:<line>]` naming a real line of the gateway source (`infra/aws/ec2/opal-gateway/app/`) where the tool's definition or the code it reaches sits.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json`: the census (read-only).
- `workflows/atom_decomposition/tool_index/members.yaml` and `workflows/atom_decomposition/tool_index/pending_members.yaml`: the current tool-index entries (read-only): each of the 13 is `member: b` today.
- The gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; `git sparse-checkout add <folder>` is the only sparse change you may make.
1. For each of the 13 tools below, open its definition in the gateway source (`infra/aws/ec2/opal-gateway/app/`: search with the Grep tool for `def <tool>` and for the tool name in quotes; integration tools sit under `app/integrations/<name>/integration.py`, harvest tools under `app/harvest_*.py`) and decide: `c` when the tool reads no dataset a catalog row could describe (it lists names, probes a status, passes a vendor call through, or reads only the caller's own data), `b` when it reads a dataset that SHOULD have a catalog row and has none (name the owning project, or `unowned`, and say what row is missing). Starting points, to be verified in the code and not copied: `harvest_list` lists object names and sizes of the served prefixes; `harvest_get_article`, `harvest_get_published_analysis` and `news_for_security` read harvest tables; `mdpf_get_security_classification` reads a DynamoDB table; `graph_cypher` runs a read query on a graph store; `opal_data_refresh_status` reads a refresh status; `schwab_get_access` reports a grant; the five `ycharts_*` tools call the YCharts API. Write each reason as one sentence about THIS tool, ending with `[app/<file>.py:<line>]`.
2. Write the file named in section 4's invocation, then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py` for exactly what each arm grades.
3. Then spot-check yourself: open five of your entries at random and re-read their source line; if one is wrong, fix it. The issuer reads a sample at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h4.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py`). Read `h_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~65/disposition_non_m365.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~65/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-h-4.dispositions-outside-m365.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W65-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-h-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h4.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~65/disposition_non_m365.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (13 tools in scope); the schema; every tool in scope exactly once; every member b or c; a c with a reason and no owner, a b with an owner and a reason -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-h-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h4.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~65/disposition_non_m365.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every reason ASCII and at least 40 characters; every reason ends with a [app/<file>.py:<line>] reference to a real line; no reason text pasted on more than 60 percent of the tools -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~65/NFRA_MCPINDEX.TO-MX-h-4.dispositions-outside-m365.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.
5. When you finish, the issuer may continue you with a second order (`MX-k-4`) on the same worktree; its face arrives as your next message.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~65. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). Generated reference files pass `h4.AC1` and `h4.AC2`; the checks prove form and grounding, not truth, so the issuer reads a sample. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
