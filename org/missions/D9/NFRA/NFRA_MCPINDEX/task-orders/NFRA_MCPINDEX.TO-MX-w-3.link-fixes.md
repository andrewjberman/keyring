# NFRA_MCPINDEX task order -- `MX-w-3` -- write the link fixes for the 10 tools the routing table grades MISROUTED class link: which linked catalog rows to remove, keep or add, each tied to a code line

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md</decomp_doc>
<owned_cells>MX-w-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-w-3.link-fixes</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~79</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-w-3` (round 24, workstream GATEWAY; PRD v0.19 FWD-23 routing arm; CTO round-23 analysis, item 3: "misrouted link (10): fix the catalog rows here, then re-run the routing script")

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 emitted a ROUTING TABLE: for each gateway tool, each (tool, linked catalog row) pair is graded against the SOURCE SET that workers traced from the tool's own code. Ten tools read `MISROUTED` with class `link`: a catalog row the tool is linked to is not read by the tool, per its traced sources. The link rule (`workflows/gateway_battery/routing_table.py`, function `s3_matches`): a pair is ROUTED when some `s3` source of the tool has the same `bucket` as the row and one of the two prefixes starts with the other; a source of kind `store` or `integration` never matches a row.

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~79/link_fixes.json`: for each of the 10 tools, which of its linked rows to remove, keep or add. The issuer applies your file to the tool index at the drain; you edit no catalog or members file.

### The contract (verbatim from the decomposition; it is the whole specification)

**W3 LINK FIXES** `link_fixes.json`, schema `gateway_link_fixes/1`: `{"schema","fixes":[{"tool","remove":[row ids],"add":[row ids],"keep":[{"row","reason"}],"basis":str,"cite":"<path>:<line>"}]}`. One entry for each tool the routing table grades `MISROUTED` with class `link` (10 tools), exactly those. Every MISROUTED pair of the tool is in `remove` or in `keep` (with a reason that names the source that justifies leaving the link); `remove` and `keep` hold only that tool's MISROUTED pairs; `add` holds only catalog rows (entities of `silver_datasets`, `portal_datasets`, `harvest_datasets`) that overlap an `s3` source of the tool's source set and that the tool does not already link. After applying the fixes to the tool's linked rows, every remaining pair is ROUTED against the tool's source set by the link rule of `routing_table.py` (same bucket; one prefix starts with the other).

### Issuer clarifications (the check implements exactly these)

- "Remaining" means the tool's linked rows, minus `remove`, minus `keep`, plus `add`: a KEPT pair is excluded from the remaining set, which is why it needs its reason. Keep a pair only when the traced source justifies the link even though the s3 link rule cannot grade it (a `store` source reading the very table the row names; a template row whose placeholder the traced per-firm sources expand). Remove a pair when the code does not read what the row names.
- `keep[].reason` is ASCII, at least eight words, and contains a `path:line` token (for example `app/news_typed.py:458`) naming the code line that justifies the link.
- `cite` is one `path:line` that resolves: the path is relative to the repository root or to `infra/aws/ec2/opal-gateway/`, the file exists and the line number is within it. It is the code line that is the main evidence for the tool's entry. `basis` is ASCII, at least eight words.
- `add` rows are catalog row ids (the `entity` of a row); the measured candidates below are the only rows that overlap a source of the tool and are not yet linked.

### Measured state (the issuer's reading of the routing table on 2026-10-19; verify it yourself from the inputs)

| tool | MISROUTED pair (row id, bucket, prefix) | traced `s3`/other sources of the tool (kind bucket prefix, cite) | candidate rows to add |
|---|---|---|---|
| `harvest_get_filing_analysis` | `harvest_issuer_site_harvest_silver_filing_source` (opal-data-harvest, `issuer-site/harvest/silver/filing_source/`) | s3 `filings/v1/` :58, `drafting/v1/` :59, `sec/harvest/silver/filing_source/` :60 (app/harvest_research.py) | none |
| `harvest_get_fundamentals` | `harvest_bloomberg_harvest_bronze_exec_officers`, `harvest_bloomberg_harvest_bronze_histdata_daily_px`, `harvest_bloomberg_harvest_bronze_price_history_tot_return` | s3 `derived/model_block/` :37, `derived/model_block_fye/` :38, `bloomberg/harvest/bronze/{bestdata,refdata,histdata,segments,price_history_px_last}/` :39-:43 (app/harvest_figures.py) | none |
| `harvest_get_research` | `harvest_amgt_harvest_silver_research_report`, `harvest_research-continuation`, `harvest_research-dossier` | s3 `amgt/harvest/gold/{research_dossier,research_continuation,ai_fill}/`, `amgt/harvest/silver/research_report/`, `management/v1/`, `bloomberg/harvest/bronze/exec_officers/` :52-:57 (app/harvest_research.py) | `harvest_bloomberg_harvest_bronze_exec_officers` |
| `harvest_resolve_security` | `harvest_identity_v1` (`identity/v1/`) | s3 `crosswalk/v1/` :40, `universe/v1/` :41, `bloomberg/harvest/bronze/identity/` :42, `amgt/harvest/gold/research_dossier/` :43 (app/harvest_identity.py) | `harvest_research_dossier` |
| `mdpf_get_model_composition` | `opal_data_mdpf_feeds_model_composition` (opal-data-mdpf, `mdpf/feeds/model_composition/<firm>/`) | s3 `mdpf/feeds/model_composition/49financial/` and `.../inflection/` :248 (app/portal_served.py) | none |
| `news_keyword_intelligence` | `dynamodb_dynamodb_opal_keyword_intelligence` (bucket `dynamodb`, prefix empty) | store (DynamoDB, vendor opal) app/news_typed.py:458 | none |
| `news_market_mood` | `opal_data_portal_v2_served_news_trending_and_sentiment` (`json/trending/latest.json; json/sentiment/`) | s3 `json/sentiment/` app/news_typed.py:497 | none that is not already linked (the row `opal_data_portal_v2_served_sentiment_singletons` is linked and ROUTED) |
| `news_search_articles` | `dynamodb_dynamodb_opal_news_articles` | store (DynamoDB, vendor other) app/news_typed.py:340 | none |
| `news_trending_topics` | `dynamodb_dynamodb_opal_news_trending_daily`, `opal_data_news_v2_gold_trending_reports` (opal-data-news-v2, `trending_reports/`) | store (DynamoDB) app/news_typed.py:394 | none |
| `schwab_describe_dataset` | `schwab_dim_asset` (opal-data-assets, empty prefix) | integration (schwab) app/integrations/schwab/integration.py:516 | none |

(The table is the issuer's reading, not an answer: the decision for each pair is yours, from the code. Where the code does not read what a row names, remove; where a traced source justifies the link, keep with the cite; add only the measured candidates.)

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/ROUTING_TABLE_20261019.json`: the routing table (`tools[]` with `tool`, `verdict`, `class`, `pairs[]` with `row`, `row_source`, `verdict`, and `source_set[]`).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json`: the census (`tools[]` with `name`, `indexes` = the linked row ids).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~71/source_sets_assets.json`, `~72/source_sets_etfs.json`, `~73/source_sets_portal.json`, `~74/source_sets_harvest.json`, `~75/source_sets_integrations.json`, `~76/source_sets_m365.json`: the traced source sets (`source_sets/1`).
- `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`: the catalog rows (`silver_datasets`, `portal_datasets`, `harvest_datasets`, and the `channels` artifacts) with `entity`, `bucket`, `prefix`.
- The gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only): the code lines your cites point at.
- `workflows/gateway_battery/routing_table.py`: the link rule.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; run `git sparse-checkout add workflows/gateway_battery` first (the checks import the link rule from it); that is the only sparse change you may make.
1. For each of the 10 tools, read the pair(s) in the routing table, the tool's source set, the catalog row(s) and the code line(s) of the sources. Decide `remove`, `keep` or `add` per section 1; write one entry per tool, in tool-name order.
2. Write the file with the Write tool: JSON, `indent=1`, ASCII, `"schema": "gateway_link_fixes/1"`. Run both criteria of section 4 until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w3_check.py` for exactly what each arm grades.
3. Spot-check yourself: open three of your cites at random and re-read the line; if one is wrong, fix it. The issuer reads a sample at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), the routing script, any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
5. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w3.AC1.sh` and `.AC2.sh` (they run `w3_check.py` beside them). Do not edit any of them.
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~79/link_fixes.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~79/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-w-3.link-fixes.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W79-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-w-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w3.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~79/link_fixes.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (10 tools in scope, the MISROUTED pairs counted); the schema gateway_link_fixes/1, exactly the 10 tools once each, remove and add as lists of row ids, keep reasons of eight ASCII words naming a path:line, basis and cite resolving; every MISROUTED pair in remove or keep and remove/keep holding only those pairs; the planted negatives all fire -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-w-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w3.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~79/link_fixes.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every add is a catalog row, not yet linked, overlapping an s3 source of the tool; after the fixes no remaining pair is MISROUTED by the link rule; the planted negatives all fire -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~79/NFRA_MCPINDEX.TO-MX-w-3.link-fixes.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 24, workstream GATEWAY, worker ~79. Source: the CTO's round-23 analysis `ledger/ROUND_ANALYSIS.round23.md` (`1.0.0_SA_CTO~Z`, item 3) and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md` (contract W3, R24.3, frozen at the cut). Base dry-runs 2026-10-20: `w3.AC1 base: FAIL as expected` and `w3.AC2 base: FAIL as expected` (the deliverable is absent). The issuer's scratch reference (outside the repo, built from the routing table and the code lines in section 1) passes `w3.AC1` (4 arms, 4 planted negatives fire) and `w3.AC2` (4 arms, 2 planted negatives fire). Ambiguity resolved at the cut: the decomposition says every remaining pair is ROUTED; three of the ten tools read a `store` source that the s3 link rule can never match, so a KEPT pair is excluded from "remaining" and needs a reason with a cite (section 1 clarifications). The check proves coverage and grounding of the fixes, not that a removal is the right call, which the issuer samples at the drain. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>24</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
