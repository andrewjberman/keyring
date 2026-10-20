# NFRA_MCPINDEX task order -- `MX-w-4` -- attribute the 7 remaining battery FAILs (tool_error 3, source_disagrees 2, unexpected_empty 1, route_unproven 1): code, catalog, battery or data, with the evidence and the owner

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md</decomp_doc>
<owned_cells>MX-w-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-w-4.fail-attribution</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~80</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (both criteria FAIL at the base) and the planted negatives inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-w-4` (round 24, workstream GATEWAY; PRD v0.19 FWD-24; CTO round-23 analysis `ledger/ROUND_ANALYSIS.round23.md`, item 4)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 graded the FWD-24 battery over all 127 gateway tools: PASS 38, EMPTY-CORRECT 4, FAIL 85. Of the 85, 67 are the battery's own coverage and 18 are tool or route defects; 7 of those 18 need a name and an owner and are your cell. For each of the 7 tools you decide WHERE the fault lives -- the gateway code, the catalog, the battery case itself, or the data -- prove it from the code and the evidence, and name who fixes it.

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~80/fail_attribution.json` (schema `gateway_fail_attribution/1`), one item for each of these 7 tools and no other:

| tool | graded class | graded case(s) | what the round-23 run saw (the issuer's notes; verify them, do not trust them) |
|---|---|---|---|
| `portal_get_security_scan` | `tool_error` | `K2-31` | an absent-universe case expected an empty answer with an absent_reason; it returned a raw AWS `AccessDenied` for `s3:ListBucket` on `opal-data-portal-v2` for the role `gateway-global-internal-reader-role` |
| `ycharts_time_series` | `tool_error` | `K5-04` | the tool call returned normally with `http_status` 403, points 0, series empty (an upstream YCharts refusal) |
| `ycharts_risk_return_scatter` | `tool_error` | `K5-06` | the same: `http_status` 403, series empty |
| `etfs_who_holds` | `unexpected_empty` | `K1-29` | 0 holders where a nonempty answer was expected; the response cited gold `security_universe` and `canonical_shape` objects of `date=2026-10-16`; the tool reads only the newest date |
| `opal_describe` | `source_disagrees` | `K4-11`, `K4-12` | DynamoDB `opal-news-articles` ItemCount 386383 against the catalog contract size.objects 381261 (+1.3%) |
| `inspect_email_attachment` | `source_disagrees` | `K6-09` | the listed attachment size 15441 against the inspected byte count 15199 |
| `harvest_resolve_security` | `route_unproven` | `H3` | the response is correct (the crosswalk key counted 3 lines naming the test security) but the routing table could not prove the route |

### The contract (verbatim from the decomposition; it is the whole specification)

**W4 FAIL ATTRIBUTION** `fail_attribution.json`, schema `gateway_fail_attribution/1`: `{"schema","items":[{"tool","fail_class","cause":"code"|"catalog"|"battery"|"data","owner":str,"evidence":str,"fix":str}]}`. One item for each of the 7 tools graded `tool_error` (3), `source_disagrees` (2), `unexpected_empty` (1) or `route_unproven` (1) in `BATTERY_GRADED_20261019.json`, exactly those; `fail_class` equals the graded class. `evidence` is `<path>:<line>` of a file in the repository or `<results file>#<case_id>`, and must resolve (the file exists, the line exists, or the case id is in the file). A `code` cause names `2.0.0_SA_COO~O` as owner; a `catalog` cause names `2.0.0_SA_COO~MI`; a `battery` or `data` cause names the producing project code. `fix` is at least eight ASCII words.

How the checks read it, so you write it to pass:
- `cause` is one of `code`, `catalog`, `battery`, `data` -- `code` when the gateway code or its IAM grant is wrong, `catalog` when a catalog row, link or contract count is wrong, `battery` when the case or its comparison is wrong, `data` when the producing data or the upstream vendor is the cause.
- `owner` for `battery` or `data` is a project code in capitals with an underscore (for example `NFRA_MCPINDEX`, `NFRA_OPLGTW`, `ETFS_INGEST`); name the project that produces the data or owns the case.
- `evidence` is ONE string. Either `<repo-relative path>:<line number>` (for example `infra/aws/ec2/opal-gateway/app/tools.py:1577`; the file must exist and the line must be inside it), or `<repo-relative results path>#<case id>` (for example `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/results_all_20261019.json#K1-29`; the case id must be one of the tool's graded cases listed in the table above). No absolute paths, no `..`.
- `fix` is one plain ASCII sentence of at least eight words that says what changes and where.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/BATTERY_GRADED_20261019.json`: the graded battery (`tools[]` with `tool`, `verdict`, `fail_class`, `cases`).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/results_all_20261019.json` and `cases_all_20261019.json`: every result and every case of the run (`error_text`, `source_check`, `answer_source`).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/ROUTING_TABLE_20261019.json`: the routing table (for `harvest_resolve_security`, its entry and pairs).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~74/source_sets_harvest.json`, `~72/source_sets_etfs.json`, `~73/source_sets_portal.json`, `~75/source_sets_integrations.json`, `~76/source_sets_m365.json`: the traced source sets.
- The gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only): the tool definitions are `portal_macro.py:367` (`portal_get_security_scan`), `tools.py:1577` and `etfs_rivals.py:496` (`etfs_who_holds`), `integrations/opal_discover/integration.py:962` (`opal_describe`), `tools.py:438` (`inspect_email_attachment`), `harvest_identity.py:374` and `tools.py:1377` (`harvest_resolve_security`), `integrations/ycharts/integration.py:196` and `:220` (the two YCharts tools). Search with the Grep tool; the catalog is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; `git sparse-checkout add <folder>` is the only sparse change you may make.
1. For each of the 7 tools, read the graded case and its result in `results_all_20261019.json` and `cases_all_20261019.json`, then read the tool's code at the lines above and follow the failing call to the line that fails or the line that makes the comparison. Decide the cause by what the evidence shows, never by the tool's name:
   - `portal_get_security_scan`: find which S3 call the tool makes for the universe (the serving helper it calls) and whether the reader role the error names could ever be granted that call by the code's own design; a missing grant is a `code` cause (the IAM grant is applied through Terraform by `2.0.0_SA_COO~O`'s lane); a case that asks for a universe the tool is meant to answer as absent is a `battery` cause.
   - the two YCharts tools: the call returned normally with the vendor's status; decide whether the integration code mishandles a refusal (`code`), the vendor entitlement or credential is missing (`data`, owner the project that owns the integration), or the case asked for something the entitlement never covered (`battery`).
   - `etfs_who_holds`: decide whether the tool should have found a holder on the date it reads (`code`), the case named a security the date does not hold (`battery`), or the source object lacks the row (`data`).
   - `opal_describe`: the catalog states an object count and the live table states another; decide whether the catalog count is stale (`catalog`) or the live source changed in a way the contract should not have pinned (`data`).
   - `inspect_email_attachment`: decide whether the listed size and the inspected bytes measure the same thing (`battery` if the comparison is unfair, `code` if the tool mis-reads).
   - `harvest_resolve_security`: find why the routing table could not prove the route (read its entry in the routing table, its source set and the response's cited key); a missing or too-coarse source set or link is a `catalog` cause.
2. Write the file named above with the Write tool, ASCII, `indent=1`, items sorted by `tool`. Then run both criteria of section 4 until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w4_check.py` for exactly what each arm grades.
3. Then spot-check yourself: open three of your entries at random and re-read the evidence line you cited; if it does not show what your `cause` says, fix the entry. The issuer reads a sample at the drain. An honest `data` or `battery` cause beats a convenient `code` one.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter, any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w4.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w4_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~80/fail_attribution.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~80/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-w-4.fail-attribution.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W80-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-w-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w4.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~80/fail_attribution.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (7 graded FAIL tools of four classes); the clean control and the three planted negatives behave; the schema; exactly the 7 tools, each once; fail_class equals the graded class; cause is code, catalog, battery or data; the owner follows the cause -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-w-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w4.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~80/fail_attribution.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the clean control and the four planted negatives behave; every evidence is an existing repository file with the line inside it, or a graded case id of that tool inside its results file; every fix is ASCII and at least eight words -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~80/NFRA_MCPINDEX.TO-MX-w-4.fail-attribution.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; for each of the 7 tools its `cause` and `owner` in one line; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 24, workstream GATEWAY, worker ~80. Source: the CTO's round-23 analysis `ledger/ROUND_ANALYSIS.round23.md` (`1.0.0_SA_CTO~Z`, item 4: "name each one by tool; a code fault goes to `2.0.0_SA_COO~O` as a defect row; a catalog fault is fixed here") and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md` (the contract R24.3 W4 is frozen at the cut). Base dry-runs 2026-10-20: `w4.AC1 base: FAIL as expected` and `w4.AC2 base: FAIL as expected` (the deliverable is absent; the control and planted-negative arms pass, the final arm FAILs). A scratch reference file (outside the repository) passes both criteria, and three planted mutants of it (a wrong class, an evidence line past the end of its file, a case id of another tool) each FAIL the matching criterion. The checks prove shape, ownership rules and that every evidence resolves; whether each cause is RIGHT is judgment the checks cannot make, and the issuer reads every item at the drain before any defect row goes to `2.0.0_SA_COO~O`. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>24</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
