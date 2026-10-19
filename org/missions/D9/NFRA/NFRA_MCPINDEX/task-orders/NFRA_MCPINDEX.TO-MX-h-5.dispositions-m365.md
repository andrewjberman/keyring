# NFRA_MCPINDEX task order -- `MX-h-5` -- classify the 35 unindexed member-b tools of Microsoft 365: each is c with a reason naming what it reads of the caller's own data, grounded in the gateway source

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md</decomp_doc>
<owned_cells>MX-h-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-h-5.dispositions-m365</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~66</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-h-5` (round 23, workstream GATEWAY; PRD v0.18 FWD-23; CTO round-22 analysis @44e6950a24)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 23 moves the whole gateway census, not one channel, toward FWD-23 (every channel indexed), FWD-24 (every tool tested) and FWD-25 (a sheet per employee). The census it counts against is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` (14 channels, 127 tools, read from the gateway host on 2026-10-19). The Microsoft 365 reads have no Opal catalog row by design; the round-23 ruling classifies them `c` with a reason that says so.

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~66/disposition_m365.json`, a DISPOSITION file whose `tools` list holds exactly the 35 tools in the table below, once each, `scope` set to `m365`.

| tool | channel | access | write_class | catalog rows linked |
|---|---|---|---|---|
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
| `search_email` | m365 | read | none | 0 |
| `search_files` | m365 | read | none | 0 |
| `search_site_files` | m365 | read | none | 0 |
| `validate_ssavail_attachment` | m365 | read | none | 0 |
| `whoami` | m365 | read | none | 0 |

### The contract (verbatim from the decomposition; it is the whole specification)

**DISPOSITION** `gateway_disposition/1`: `{"schema":"gateway_disposition/1","scope":<free text>,"tools":[{"tool","member":"b"|"c","owner"?,"reason"}]}`. It covers ONLY tools with no catalog index (an indexed tool is made `a` by the applier without a disposition). `c`: `reason` non-empty, no `owner`. `b`: `owner` (a project code or `unowned`) and `reason` (why no row exists and what would create one), both non-empty. A `reason` is ASCII, at least 40 characters, and ENDS with a source reference `[app/<file>.py:<line>]` naming a real line of the gateway source (`infra/aws/ec2/opal-gateway/app/`) where the tool's definition or the code it reaches sits.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json`: the census (read-only).
- `workflows/atom_decomposition/tool_index/members.yaml` and `workflows/atom_decomposition/tool_index/pending_members.yaml`: the current tool-index entries (read-only): each of the 35 is `member: b` today.
- The gateway source under `infra/aws/ec2/opal-gateway/app/` (read-only).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; `git sparse-checkout add <folder>` is the only sparse change you may make.
1. For each of the 35 tools below, open its definition in the gateway source (`infra/aws/ec2/opal-gateway/app/`: the Microsoft 365 tools are in `app/tools.py` and the modules it imports, e.g. `app/graph_read.py`; search with the Grep tool for `def <tool>` and the tool name in quotes). They read the signed-in caller's own mailbox, files, calendar, Teams chats, channels, meetings or SharePoint, which is data but has no Opal catalog row by design. The ruling (R23.4 ruling 3): classify each `c`, with a reason that names WHAT the tool reads and that it is the caller's own Microsoft 365 data, one sentence about THIS tool, ending with `[app/<file>.py:<line>]`. Use `b` only for a tool that turns out to read an Opal-owned dataset that deserves a row (say which in the reason and name the owner). Do not write one sentence and paste it on every tool.
2. Write the file named in section 4's invocation, then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py` for exactly what each arm grades.
3. Then spot-check yourself: open five of your entries at random and re-read their source line; if one is wrong, fix it. The issuer reads a sample at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter (`emit_catalog_v02.py`), any file under `infra/`, the PRD, or any other file under `workflows/`. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h5.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h_check.py`). Read `h_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~66/disposition_m365.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~66/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-h-5.dispositions-m365.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W66-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-h-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h5.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~66/disposition_m365.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (35 tools in scope); the schema; every tool in scope exactly once; every member b or c; a c with a reason and no owner, a b with an owner and a reason -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-h-5" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/checks/h5.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~66/disposition_m365.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; every reason ASCII and at least 40 characters; every reason ends with a [app/<file>.py:<line>] reference to a real line; no reason text pasted on more than 60 percent of the tools -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~66/NFRA_MCPINDEX.TO-MX-h-5.dispositions-m365.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count (code cells); your commit shas; every place the contract was silent and what you did.
5. When you finish, the issuer may continue you with a second order (`MX-k-5`) on the same worktree; its face arrives as your next message.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 23, workstream GATEWAY, worker ~66. Source: the CTO's round-22 analysis @44e6950a24 (msg 35997) and PRD v0.18 @4b8dcf3b86, cut on the CORRECTED census. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md` (the contracts R23.2 are frozen at the cut). Base dry-runs 2026-10-19: every criterion of this order FAILs as expected (the script, test file or deliverable is absent, or the gate lacks the explained field). Generated reference files pass `h5.AC1` and `h5.AC2`; the issuer reads a sample. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>23</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
