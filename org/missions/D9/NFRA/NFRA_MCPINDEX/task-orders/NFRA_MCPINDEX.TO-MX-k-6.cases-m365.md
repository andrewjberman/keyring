# NFRA_MCPINDEX task order -- `MX-k-6` -- write the FWD-24 battery cases for m365 (43 tools): real arguments, plain-English questions, readers expect an answer, senders preview only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-k-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-k-6.cases-m365</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~67</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-k-6` (round 23, workstream GATEWAY; PRD v0.18 FWD-24; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). Round 22 built the battery (`tool_battery.py plan|grade|plant`) and ran it on harvest. This cell supplies the cases for the other channels; a signed-in session runs them.

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~67/cases_m365.json`, a CASES file (`gateway_battery_cases/1`) with at least one case for each of the 43 tools below (channels: m365), case ids `K6-01`, `K6-02`, ... in file order. 8 of these tools are senders.

The m365 tools read the SIGNED-IN caller's OWN mailbox, files, calendar and Teams. The cases only name the tool and its arguments; the issuer runs them as the owner and records COUNTS, never message or file text. Prefer list and search reads with a small `top` or `limit` (3 or fewer).

| tool | channel | access | write_class | catalog rows linked |
|---|---|---|---|---|
| `copy_site_file_to_s3` | m365 | write | write_files | 0 |
| `create_draft` | m365 | write | write_comms | 0 |
| `find_online_meeting` | m365 | read | none | 0 |
| `find_sharepoint_site` | m365 | read | none | 0 |
| `get_item` | m365 | read | none | 0 |
| `get_site_item` | m365 | read | none | 0 |
| `inspect_email_attachment` | m365 | read | none | 0 |
| `list_calendar` | m365 | read | none | 0 |
| `list_channels` | m365 | read | none | 0 |
| `list_chats` | m365 | read | none | 0 |
| `list_email_attachments` | m365 | read | none | 0 |
| `list_email_filtered` | m365 | read | none | 0 |
| `list_meeting_transcripts` | m365 | read | none | 0 |
| `list_onedrive` | m365 | read | none | 0 |
| `list_recent_email` | m365 | read | none | 0 |
| `list_shared_folder` | m365 | read | none | 0 |
| `list_site_drives` | m365 | read | none | 0 |
| `list_site_files` | m365 | read | none | 0 |
| `list_teams` | m365 | read | none | 0 |
| `poll_addressed_teams_messages` | m365 | read | none | 0 |
| `profile_site_file` | m365 | read | none | 0 |
| `read_channel_messages` | m365 | read | none | 0 |
| `read_chat_message_images` | m365 | read | none | 0 |
| `read_chat_messages` | m365 | read | none | 0 |
| `read_document` | m365 | read | none | 0 |
| `read_email` | m365 | read | none | 0 |
| `read_file` | m365 | read | none | 0 |
| `read_meeting_transcript` | m365 | read | none | 0 |
| `read_site_file` | m365 | read | none | 0 |
| `read_site_workbook` | m365 | read | none | 0 |
| `read_teams_attachment` | m365 | read | none | 0 |
| `read_workbook` | m365 | read | none | 0 |
| `reply_email` | m365 | write | write_comms | 0 |
| `save_email_attachment_to_site` | m365 | write | write_files | 0 |
| `search_email` | m365 | read | none | 0 |
| `search_files` | m365 | read | none | 0 |
| `search_site_files` | m365 | read | none | 0 |
| `send_channel_message` | m365 | write | write_comms | 0 |
| `send_chat_message` | m365 | write | write_comms | 0 |
| `send_email` | m365 | write | write_comms | 0 |
| `upload_text_to_site` | m365 | write | write_files | 0 |
| `validate_ssavail_attachment` | m365 | read | none | 0 |
| `whoami` | m365 | read | none | 0 |

### The contract (verbatim from the decomposition; it is the whole specification)

**CASES** `gateway_battery_cases/1`: `{"schema":...,"cases":[{"case_id","tool","question","args":{},"expect":"nonempty|empty|refused|preview","source_hint"}]}`. `question` is the plain-English example a sheet may show.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json`: the census (read-only); each tool's `access`, `write_class` and linked-row count are in the table above.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/cases/harvest.json`: the 16 cases written for harvest in round 22, as a model of the shape and the style of the questions.
- The gateway source under `infra/aws/ec2/opal-gateway/app/` and the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (read-only).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; `git sparse-checkout add <folder>` is the only sparse change you may make.
1. Read the definition of each tool in the gateway source (`infra/aws/ec2/opal-gateway/app/`: search with the Grep tool for `def <tool>` and the tool name in quotes; integration tools sit under `app/integrations/<name>/integration.py`) so its `args` are the real parameters with real, valid example values. Write 1 to 3 cases per tool. A READER tool (census `write_class` none and access read) gets at least one case that expects an answer (`nonempty` when the example surely returns rows, `empty` when it surely returns none, with the reason in `source_hint`) and may also get a `refused` case for a request the tool should refuse. A SENDER (a tool whose census `write_class` is a real class, `write_comms` or `write_files`, or the tool `opal_data_refresh_upload`) gets only `preview` cases: its non-sending path (a `confirm=false` preview or a dry-run flag, read in the definition); NEVER a case that sends or writes. A tool whose `write_class` is `UNCLASSIFIED` is NOT thereby a sender: it only means the gateway has no `destructive_ops` entry for it (the census then shows `access: write`). Read its definition: if it only reads, treat it as a reader and END every one of its cases' `source_hint` with `[app/<file>.py:<line>]`, the line of the definition that shows it only reads; if it can write or send, treat it as a sender. `question` is a plain-English sentence a staff member would type (at least four words, ASCII, unique); it appears on a cheat sheet, so write it for the person. `source_hint` says how a second instrument would check the answer (a second read of the same source; a count; a date), in one phrase. Never put an email address, credential or account number in `args`; use public examples (a ticker such as AAPL, a fund ticker, a date) and read the catalog's own `example_questions` for the dataset a tool reads where one exists (`infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`). A case that needs an id returned by an earlier case lists that case in `depends_on` and puts a placeholder string like `<id from K6-03>` in `args`.
2. Write the file named in section 4's invocation, then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py` for exactly what each arm grades.
3. Then spot-check yourself: open five of your entries at random and re-read their source line; if one is wrong, fix it. The issuer reads a sample at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/k6.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py`). Read `h_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~67/cases_m365.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~67/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-k-6.cases-m365.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W67-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-k-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/k6.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~67/cases_m365.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (43 tools in scope); the schema; case ids unique and starting K6-; every tool in scope has a case and no case names another tool; every case carries case_id, tool, question, args as an object, expect and source_hint -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-k-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/k6.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~67/cases_m365.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every case of a sender is preview and each sender has one; every reader has a case expecting an answer; questions are ASCII, at least four words and unique; no argument holds an email address or a credential; depends_on names an existing case -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~67/NFRA_MCPINDEX.TO-MX-k-6.cases-m365.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~67. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). Generated reference files pass `k6.AC1` and `k6.AC2`; the checks prove coverage and safety, not that an argument is valid, which the live run finds. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
