# NFRA_MCPINDEX task order -- `MX-z-3` -- plan the second-client read for each of the 46 tools whose source check is still open: the route, the exact call, the fact compared, and whether it can be run at all

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md</decomp_doc>
<owned_cells>MX-z-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-z-3.probe-plan</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~92</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant. The plan NAMES reads for the issuer to make later; you make none.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (both criteria FAIL at the base) and the planted negatives inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-z-3` (round 26, workstream GATEWAY; PRD v0.19 FWD-24; CTO round-25 analysis `ledger/ROUND_ANALYSIS.round25.md`, item 3 of the round-26 list)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The list-only source compare (round 25) could check an answer against its source for 30 tools; for 46 tools it could not, because the source is not an S3 listing: 33 read Microsoft Graph, 9 read an integration, 4 read DynamoDB. The CTO's ruling: **the independent read is the SAME source reached by a DIFFERENT client, outside the gateway: the tester's own direct Graph call, the vendor's own API, or a direct DynamoDB read. The cross-check is two clients, not two sources. A tool that has no such route stays `FAIL source_unchecked` with its reason recorded; it is never upgraded to PASS.**

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~92/probe_plan.json`, one object, and no other deliverable. It is a PLAN: you make no call. The issuer runs the feasible items later at the drain and writes the probes file from them.

**The 46 tools (the denominator; recompute it, do not trust this list).** They are the entries of `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/evidence/SOURCE_COMPARE_20261020c.json` whose `agrees` is null and whose `source.kind` is `graph`, `integration` or `store`.
- graph (33): `find_online_meeting`, `find_sharepoint_site`, `get_item`, `get_site_item`, `inspect_email_attachment`, `list_calendar`, `list_channels`, `list_chats`, `list_email_attachments`, `list_email_filtered`, `list_meeting_transcripts`, `list_onedrive`, `list_recent_email`, `list_shared_folder`, `list_site_drives`, `list_site_files`, `list_teams`, `poll_addressed_teams_messages`, `profile_site_file`, `read_channel_messages`, `read_chat_message_images`, `read_chat_messages`, `read_document`, `read_email`, `read_file`, `read_meeting_transcript`, `read_site_file`, `read_workbook`, `search_email`, `search_files`, `search_site_files`, `validate_ssavail_attachment`, `whoami`.
- integration (9): `graph_cypher`, `graph_status`, `harvest_get_published_analysis`, `opal_data_refresh_status`, `schwab_describe_dataset`, `ycharts_freshness`, `ycharts_fund_series`, `ycharts_search`, `ycharts_snapshot_metrics`.
- store (4): `mdpf_get_security_classification`, `news_keyword_intelligence`, `news_search_articles`, `news_trending_topics`.

### The contract (verbatim from the decomposition; it is the whole specification)

**Z3 PROBE PLAN** `probe_plan.json`, schema `gateway_probe_plan/1`: `{"schema","items":[{"tool","class":"graph"|"integration"|"store","route":"direct-graph"|"vendor-api"|"direct-dynamodb"|"none","call":str,"fact":str,"answer_field":str,"feasible":bool,"reason":str,"cite":"<path>:<line>"}]}`. One item for each tool of `SOURCE_COMPARE_20261020c.json` whose `agrees` is null and whose source `kind` is graph, integration or store (46 tools), exactly those, sorted by tool; `class` equals the source kind. The plan states the SECOND-CLIENT read that would check the answer against its own source: `route` direct-graph (the tester's own Microsoft Graph call outside the gateway), vendor-api (the vendor's own API outside the gateway), direct-dynamodb (a direct DynamoDB read); `call` names the exact request (method and path or table and key) in at least eight ASCII words; `fact` is the one fact compared (a count, a latest date, an id) and `answer_field` is the field of the gateway answer (from `results_all_r25.json` for the tool's ok result, or the tool's definition when it has no ok result) that carries the same fact. `feasible` is true only when the route needs nothing beyond the owner's own delegated sign-in or an AWS read the repository already uses (cite the path:line of the same call in the gateway source); otherwise `feasible` is false, `route` may stay the intended route or `none`, and `reason` (at least eight ASCII words) says what is missing (a vendor key, a write, no read-only call exists). Every `cite` resolves. Tools whose answer is a write-gated or sender tool, or which have no ok result and no read-only definition, are `feasible` false with that reason.

How the checks read it, so you write it to pass:
- `items` is sorted by `tool` (plain string order) and holds each of the 46 tools exactly once; `class` is the tool's source kind from the compare file; `route` is one of the four values; `feasible` is a JSON boolean (`true` or `false`).
- `tool`, `class`, `route`, `call`, `fact`, `answer_field` and `cite` are non-empty strings; `reason` is a string (empty when `feasible` is true).
- `cite` is `<repo-relative path>:<line number>` of an existing file UNDER `infra/aws/ec2/opal-gateway/app/` with the line inside it. A `feasible` true item cites the gateway line that makes the SAME call (the Graph request, the vendor request, the DynamoDB read, or the line that names the table or its environment variable). The check looks for the request path of your `call` (for a Graph or vendor route, the part that starts with `/`, such as `/me/messages`, up to the first `{`, `(`, `?` or `$`) or, for `direct-dynamodb`, the table name after `--table-name` or an environment name ending `_TABLE`, within six lines of the cited line. A `feasible` false item cites the line of the tool's source read (its definition or the source-set cite), with no such test.
- `call` is plain ASCII in at least eight words and names the method and path (or the table and key); write a full Graph URL as the path it reads (the check ignores `https://graph.microsoft.com/v1.0`). Avoid the character `/` inside ordinary prose (write "and" or "or", not "and/or"): every `/word` in `call` counts as a request path.
- A `feasible` false item carries a `reason` of at least eight ASCII words and states what is missing. A `feasible` true item needs a `route` other than `none`.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/evidence/SOURCE_COMPARE_20261020c.json`: the compare run; the 46 tools and each one's `source` and `case_ids`.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/evidence/results_all_r25.json` and `cases_all_r25.json`: every result (status, rows, as_of, answer_source) and every planned case with its arguments; the answer body is not stored there, so read the fact's field from the tool's definition when you need its name.
- The gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only): `tools.py` (the Microsoft tools: each `graph.call(t, "GET", <path>)` is the request; helpers near `tools.py:1060` and `tools.py:1200` build the Teams paths), `mdpf_classification.py` and `news_typed.py` (the DynamoDB stores: `TABLE`, `_TABLE_ENV`), and `app/integrations/*/` (`schwab`, `ycharts`, `globgrph`, `opal_portal`) and `harvest_published.py` (the integrations).
- The source sets `deliverables/0.9.0_WK_NFRA_MCPINDEX~71/source_sets_*.json` .. `~76/`: each tool's traced sources, with the store's `table` or the integration's route where the round-25 supplement added one.
- Whether an integration can be reached by a second client is a question of what the repository shows: a vendor request that needs a credential held only inside the gateway, a store reachable only through an in-VPC proxy, or an answer that is a constant in the code has NO second-client route (`feasible` false, with that reason). Do not guess a route the code does not show.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The issuer has added the sparse folders `infra/aws/ec2/opal-gateway/app`, `workflows/atom_decomposition` and `workflows/gateway_battery` to your worktree; if any is missing, `git sparse-checkout add infra/aws/ec2/opal-gateway/app workflows/atom_decomposition workflows/gateway_battery` is the only sparse change you may make.
1. Recompute the 46 from the compare file and print the count by kind (graph 33, integration 9, store 4).
2. For each tool, read its definition in the gateway source and decide: (a) the second-client route; (b) the exact request (method and path, or table and key) that a client outside the gateway would make to read the same source; (c) the one fact the two reads must agree on and the field of the gateway answer that carries it; (d) whether the issuer can run it (`feasible` true) or what is missing (`feasible` false). Write the cite as the line of the gateway code that makes the same read.
3. Write the file named above with the Write tool, ASCII, `indent=1`, items sorted by `tool`. Then run both criteria of section 4 until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z3_check.py` for exactly what each arm grades.
4. Then spot-check yourself: open five items at random and re-read the cited lines; if one does not show the request your `call` names, fix the item. An honest `feasible` false beats a convenient `true`: the issuer will run every `true` item.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks or decomposition, `source_compare.py`, `members.yaml`, the catalog or its row files, the emitter, any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no Graph call, no grant, no deploy, no push: the plan names reads, it makes none.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z3.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z3_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~92/probe_plan.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~92/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-z-3.probe-plan.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W92-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-z-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z3.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~92/probe_plan.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (46 tools, graph 33, integration 9, store 4); the clean control and the eight planted negatives behave; the plan holds exactly the 46 tools once each, sorted, with class equal to the source kind, a route from the enum and a boolean feasible -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-z-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z3.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~92/probe_plan.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (the plan items to ground); the clean control and the six planted negatives behave; every cite resolves under the gateway source, every call and every false-feasibility reason is long enough, and every feasible item's cited lines show its call -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~92/NFRA_MCPINDEX.TO-MX-z-3.probe-plan.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the count of `feasible` true and false items by class; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 26, workstream GATEWAY, worker ~92. Source: the CTO's round-25 analysis `ledger/ROUND_ANALYSIS.round25.md` (`1.0.0_SA_CTO~Z`, ruling: the independent read is the same source through a different client, otherwise the tool stays `FAIL source_unchecked` with its reason; round-26 item 3) and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md` (the contract R26.3 Z3 is frozen at the cut). The 46 are graph 33, integration 9, store 4 (read from the compare file at the cut). Base dry-runs 2026-10-20: `z3.AC1 base: FAIL as expected` (the deliverable is absent; the clean control and the eight planted negatives pass, the final arm FAILs; ARMS 10 ok 1 failed) and `z3.AC2 base: FAIL as expected` (the control and the six planted negatives pass, the final arm FAILs; ARMS 7 ok 1 failed). A scratch reference plan (outside the repository) passes both criteria (AC1 11 of 11 arms, AC2 8 of 8) and records the issuer's own reading: the 33 Graph tools are read-only requests the owner's delegated sign-in can repeat (feasible true, route direct-graph, cite the gateway's own request line); the 4 stores are DynamoDB reads the repository already makes (feasible true, route direct-dynamodb, cite `mdpf_classification.py:34` and `news_typed.py:41`); the 9 integrations have no second-client route (the in-VPC graph proxy, the scoped-API Lambda, the portal status route and the YCharts session credential are reachable only from inside the gateway, and `schwab_describe_dataset` answers from a constant): feasible false with those reasons. Three mutants of the reference (a wrong class, a feasible item whose cited lines do not show its call, a short reason) each FAIL. The worker decides from the code and may differ from the reference on any item; the checks prove shape and grounding (the real tool set, the enum, resolving cites, lengths, the call shown at the cited lines), not that a route is the right one. The issuer samples at the drain and runs every `true` item with the owner's own sign-in or AWS read; an item that cannot be run is rewritten `false` with its reason, and the tool stays `FAIL source_unchecked`. Gate limb: none yet (an order cut at the issuance).

<status>issued</status>
<round>26</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
