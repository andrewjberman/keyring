# NFRA_MCPINDEX task order -- `MX-w-2` -- plan the 32 battery tools that were NOT RUN: run them, preview them, or give them a (c) reason

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md</decomp_doc>
<owned_cells>MX-w-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-w-2.not-run-plan</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~78</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one JSON data file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-w-2` (round 24, workstream GATEWAY; PRD v0.19 FWD-24; CTO round-23 analysis, item 2)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). In round 23 the FWD-24 battery graded 127 gateway tools. 32 of them were graded `not_run`: at least one planned case of the tool has no result. This cell writes the PLAN that says, for each of the 32, what happens to it at the drain: it is run, it is previewed only, or it gets a (c) reason. You write one JSON file and no code.

**What to build.** `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~78/not_run_plan.json`.

### The contract (verbatim from the decomposition; it is the whole specification)

**W2 NOT-RUN PLAN** `not_run_plan.json`, schema `gateway_not_run_plan/1`: `{"schema","plans":[{"tool","plan":"run"|"preview-only"|"c","case_ids":[existing case ids still to run],"new_cases":[full case objects of `gateway_battery_cases/1`],"test_send":null|{"case_id","to":"tester mailbox"|"tester chat"},"reason":str,"cite":"<path>:<line>"}]}`. One entry for each tool graded `not_run` in `BATTERY_GRADED_20261019.json`, exactly those tools, once each. Rules: `run` lists every planned case of the tool (from `cases_all_20261019.json`) that has no result in `results_all_20261019.json`, plus `new_cases` for a case whose input was a placeholder, with a real input read from the catalog rows or the gateway code (no `<...>` token in any argument, no email address, no account number); a sender tool (census `write_class` a real class, or `opal_data_refresh_upload`, or `schwab_prepare_download`) is never `run`: it is `preview-only` with its preview case ids and, if the CTO's rule applies (open call c5c2: ONE real message to the tester's own mailbox or chat), a `test_send` naming the one case; a tool that cannot run without a write elsewhere is `preview-only` and says which write; `c` gives the reason the tool reads no data row, with a `cite` that exists. Every `reason` is ASCII, at least eight words.

**Issuer rulings that settle the places the contract is silent (they bind you):**

1. A case that is unrun but holds a placeholder argument (`<...>`) is handled one of three ways. (a) The placeholder names an answer of an earlier case through the case's `depends_on` field: leave the case in `case_ids`; it is run in order at the drain. (b) The input can be read from the catalog rows or the gateway code: add a `new_cases` entry with the real value and put `"supersedes": "<the old case id>"` on it; leave the old id out of `case_ids`. (c) The input is a client account identifier that only the staff member holds (the five `client_*` tools of K3): set `"input_owner": "staff"` on the plan entry, keep the case ids in `case_ids`, and say so in `reason`; no account number or last-four digits is ever written to the repository.
2. `new_cases` entries carry all of `case_id` (new ids `W2-01`, `W2-02`, ... in file order, never an existing id), `tool` (the entry's tool), `question` (plain English, four words or more), `args` (an object), `expect` (`nonempty`, `empty`, `refused` or `preview`) and `source_hint`; optionally `depends_on`, `supersedes`, `expect_source`.
3. A sender tool is `preview-only` with the ids of its `expect` = `preview` cases. `test_send` applies to a sender only: `send_email`, `reply_email`, `create_draft` may name `"to": "tester mailbox"` and `send_chat_message` may name `"to": "tester chat"`; `send_channel_message`, `upload_text_to_site`, `copy_site_file_to_s3`, `save_email_attachment_to_site`, `opal_data_refresh_upload` and `schwab_prepare_download` stay preview only with `test_send` null. `test_send.case_id` is one of the entry's `case_ids`.
4. A non-sender that the battery cannot run because a write elsewhere must happen first is `preview-only`, and its `reason` contains the word `write` and names the write. Prefer `run` whenever a real input exists.
5. `cite` is `path:line` of the tool's own definition line (or the line that shows why it is previewed or (c)), repository-relative, forward slashes; the file and the line must exist. The gateway source is `infra/aws/ec2/opal-gateway/app/` (integration tools under `app/integrations/<name>/integration.py`).

### Inputs you read (you do NOT edit them), all under `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/`

- `round23/evidence/BATTERY_GRADED_20261019.json`: `tools[]` with `tool`, `verdict`, `fail_class`, `cases`. The 32 tools of this cell are those with `fail_class` equal to `not_run`.
- `round23/evidence/cases_all_20261019.json`: `gateway_battery_cases/1`, every planned case (`case_id`, `tool`, `question`, `args`, `expect`, `source_hint`, optional `depends_on`).
- `round23/evidence/results_all_20261019.json`: `gateway_battery_results/1`, the cases that have a result (`case_id`, `status`).
- `round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json`: the census; each tool has `name`, `access`, `write_class` (`null`, `UNCLASSIFIED` or a real class such as `write_comms`, `write_files`).
- `infra/aws/ec2/opal-gateway/app/` and `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (read-only).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree carries the sparse folders `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app`; `git sparse-checkout add <folder>` is the only sparse change you may make.
1. Read the graded file and list the 32 `not_run` tools. For each, list its planned cases in `cases_all_20261019.json` and mark which have no result in `results_all_20261019.json` (those are the unrun cases).
2. Classify each tool with the census (`write_class` real, or `opal_data_refresh_upload` or `schwab_prepare_download`, is a sender) and write its entry by the rulings above. Read the tool's definition in the gateway source for the `cite` and for any real input a `new_cases` entry needs.
3. Write the file with the Write tool (JSON, `indent=1`, ASCII), then run both criteria until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w2_check.py` for exactly what each arm grades.
4. Then spot-check yourself: open five entries at random and re-read their `cite` line; if one is wrong, fix it. The issuer reads a sample at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks or decomposition, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter, any file under `infra/` or `workflows/`, the PRD, or any other file. No AWS call, no network call, no gateway call, no grant, no deploy, no push.
2. ASCII only. You write one data file and no code.
3. No email address, account number, last-four digits, credential or customer text appears in the file.
4. The contract and rulings in section 1 are the whole specification. Where they are silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w2.AC1.sh` and `.AC2.sh` (they run `w2_check.py` beside them). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~78/not_run_plan.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~78/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-w-2.not-run-plan.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W78-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-w-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w2.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~78/not_run_plan.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (32 tools graded not_run, 32 entries); the schema; one entry per not_run tool, once each, with every field and enum; the planted dropped tool and duplicate tool are caught -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-w-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w2.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~78/not_run_plan.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; senders are never run; every unrun case is listed or superseded; no placeholder, email address or account-like number as input; test_send, reasons (ASCII, eight words or more) and cites hold; the five planted defects are caught -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~78/NFRA_MCPINDEX.TO-MX-w-2.not-run-plan.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 24, workstream GATEWAY, worker ~78. Source: the CTO's round-23 analysis `ledger/ROUND_ANALYSIS.round23.md` (item 2) and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md` (the contract R24.3 W2 is frozen at the cut). Base dry-runs 2026-10-20: w2.AC1 base: FAIL as expected; w2.AC2 base: FAIL as expected (the plan file is absent). A scratch reference plan (32 entries: 10 senders preview-only with 4 test sends, 5 client tools run with input_owner staff, opal_asker_query preview-only, the rest run) passes w2.AC1 (4 of 4 arms) and w2.AC2 (7 of 7 arms) and the base fails both. The checks prove coverage, the sender rule, the input rules, test_send and the cites; they do not prove that an input is valid, which the live run finds. Contract ambiguity settled by the issuer rulings in section 1: the contract says `run` lists every unrun case AND supplies `new_cases` for placeholder cases, which cannot both hold for a case that has no real input; ruling 1 gives three ways (depends_on, supersedes, input_owner staff). Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>24</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
