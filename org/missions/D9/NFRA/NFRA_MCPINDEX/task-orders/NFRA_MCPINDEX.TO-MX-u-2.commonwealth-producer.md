# NFRA_MCPINDEX task order -- `MX-u-2` -- name the producer, schedule and owner of the Commonwealth silver feed (`opal-data-assets/commonwealth/cottonwood/silver/`), say why its newest partition is 2026-06-23 (83 trading days behind), and file one surprise row with the measured gap

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round27-GATEWAY.md</decomp_doc>
<owned_cells>MX-u-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-u-2.commonwealth-producer</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~95</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is created; one JSON data file that NAMES an existing schedule, or the absence of one.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (both criteria FAIL at the base) and the planted negatives inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-u-2` (round 27, workstream GATEWAY; PRD v0.19 FWD-23/FWD-24; the CTO's round-26 analysis item 3: "name the producer, its schedule and its owner for the Commonwealth silver feed (as was done for the Eclipse copier), and file a surprise row on the project's channel with the measured gap. No fix in this project.")

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The CRO's brief (`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md`, section 4.7, line 220 onward) and the census (`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/census.json`, the twelve `catalog` entries whose prefix starts `commonwealth/cottonwood/silver/`) measured that every Commonwealth table holds ONE partition, 2026-06-23 (one table, `price_evidence`, holds 2022-10-12). The gateway adapter states it as "ONE CLOSED DELIVERY" (`infra/aws/ec2/opal-gateway/app/client_adapter_commonwealth.py:6`). At 2026-10-21 that is 83 trading days behind the T-1 frontier (the round-26 report `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/evidence/ROUND26_REPORT.md` states "83 trading days"). Nobody has named what writes the feed, on what schedule, or who owns it. You name them from the repository, say why no later partition exists, and file one surprise row. You change nothing else.

**What was seen (the issuer's leads; verify them, do not trust them).** A first search found no Terraform, Lambda or scheduler under `infra/aws` that names a Commonwealth job: the only infrastructure files that mention Commonwealth are consumers (the gateway adapter and tools, the `investor-reporting` Lambdas `account-return-daily` and `reporting-gold-cot`, IAM and bucket policy files). The writers look like scripts under `data/assets/scripts/`: a bronze landing script `bronze/commonwealth_landing.py` (its docstring: "Land one Commonwealth delivery zip into bronze exactly as shipped"; dry run by default, `--apply` at line 149 writes to S3) and a family of silver builders `silver/commonwealth_*.py` (for example `commonwealth_transactions.py` and `commonwealth_crosswalk.py`, whose `DATA_DATE = "2026-06-23"` is at line 70) whose headers name the project `ADVI_COTBKF` ("The Cottonwood 10-year backfill from Commonwealth: the delivery kept as received", `org/projects/ADVI_COTBKF.json`). The silver `daily_returns`, `account_day_value` and `month_grades` objects were rewritten on 2026-10-16 with the partition still 2026-06-23, which fits a hand-run rebuild, not a new delivery. Decide for yourself whether the producer is "a manual landing plus hand-run silver builders" (kind `manual`) or something scheduled you can cite, read every place a schedule could live, and follow the gap to its cause.

**What to build.** Two things and no other deliverable: (1) `deliverables/0.9.0_WK_NFRA_MCPINDEX~95/commonwealth_producer.json`, one object; (2) ONE surprise row appended to the project's channel `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md` (see section 3 for its fields).

### The contract (verbatim from the decomposition; it is the whole specification)

**U2 COMMONWEALTH PRODUCER** `commonwealth_producer.json`, schema `gateway_commonwealth_producer/1`: `{"schema","feed":{"bucket","prefix"},"newest_partition":str,"trading_days_behind":int,"producer":{"kind":"lambda"|"script"|"glue"|"ecs-task"|"terraform-only"|"manual"|"other","name":str,"cite":"<path>:<line>"},"schedule":{"expression":str,"cite":"<path>:<line>"},"owner":str,"gap_cause":str,"evidence":[str,...]}`. `feed` is the Commonwealth silver feed `opal-data-assets` `commonwealth/cottonwood/silver/` (read the catalog rows and the CRO brief section 4.7 and `census.json`); `newest_partition` and `trading_days_behind` come from the CRO files and the round-26 report (2026-06-23, 83 trading days at 2026-10-21); find in the repository the job that writes that feed and its schedule (Lambda, script, Glue job, scheduled task, or a manual upload with its runbook) and the project that owns it (`owner` is a project code that exists in `org/projects/`). `gap_cause` is at least twelve ASCII words explaining, from the code and the schedule, why no partition after 2026-06-23 exists, or says what cannot be established from the repository and why. All `cite` and `evidence` entries resolve (at least two evidence entries); when no producer is found the `producer.kind` is `manual` or `other` with `name` `none-found` and at least three evidence entries naming what was searched. The cell ALSO files ONE surprise row on the project's channel (`surprise-channel/investigations/INVESTIGATION_v1.md`): class OBSERVATION, hazard INERT, `disarm_owner` `2.0.0_SA_COO~MI`, `one_line` stating the measured gap (newest partition 2026-06-23, 83 trading days behind), `grounding` GROUNDED with the cites. No fix in this project.

How the checks read it, so you write it to pass:
- `feed` is exactly `{"bucket": "opal-data-assets", "prefix": "commonwealth/cottonwood/silver/"}` (the common prefix of the twelve catalogued Commonwealth tables in the census); `newest_partition` is the string `2026-06-23` (the newest partition among those tables); `trading_days_behind` is the integer `83` (not a string, not a boolean).
- `producer.kind` is one of `lambda`, `script`, `glue`, `ecs-task`, `terraform-only`, `manual`, `other`; `producer.name` is a nonempty ASCII string (it may name the chain); `schedule.expression` is a nonempty ASCII string (the cron or rate expression as written in the source, or a plain statement that no schedule exists, in your own words); `owner` is a project code with a file `org/projects/<CODE>.json`.
- `producer.cite` and `schedule.cite` are `<repo-relative path>:<line number>` where the file exists in your worktree and the line is inside it; every `evidence` entry is the same form; the entries are DIFFERENT strings; at least two (three when `producer.name` is `none-found`, with `producer.kind` `manual` or `other`). A cited file must exist in YOUR worktree, so add the folder of every file you cite to the sparse cone.
- `gap_cause` is one plain ASCII sentence of at least twelve words.
- The surprise row: among the rows of the channel file whose `id` is `NFRA_MCPINDEX-Z-W95-S<k>` there is at least one with `class` `OBSERVATION`, `hazard_standing` `INERT`, `disarm_owner` `2.0.0_SA_COO~MI`, a `one_line` that contains both `2026-06-23` and `83`, and `grounding.status` `GROUNDED`.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md` (section 4.7) and `census.json` (the twelve Commonwealth entries); `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/evidence/ROUND26_REPORT.md`.
- The infrastructure and ETL sources, READ-ONLY: `infra/aws/lambda/`, `infra/aws/terraform/`, `infra/aws/ec2/opal-gateway/app/client_adapter_commonwealth.py`, `data/assets/scripts/bronze/` and `data/assets/scripts/silver/` (the `commonwealth_*.py` files), `data/`, `workflows/`, `lib/`, and any scheduler you find. The catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` holds the Commonwealth rows.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. THE SPARSE CONE MAY LACK THE FOLDERS YOU MUST READ. Your first step is `git sparse-checkout add` of whichever of `infra/aws`, `workflows`, `data`, `lib` you need (the issuer pre-adds them; verify with `ls`); adding sparse folders is the ONLY sparse change you may make, and you MUST add what you need BEFORE you conclude that no producer or schedule exists (an absent folder is not an absent job).
1. Search with the Grep tool (a `path` and a `glob`) and the Glob tool, or `comp-find`; the repository-wide recursive-search rail denies a blind recursive grep run through Bash (CLAUDE.md rule 21), so do not shell out to `grep -r` or `find` over the repository. Start with the strings `commonwealth/cottonwood`, `commonwealth_landing`, `commonwealth` in `*.tf` and `handler.py`/`lambda_function.py` files under `infra/aws`, and `cron(` or `schedule_expression` near them; then read the landing script and two silver builders' headers.
2. Choose `producer.kind`, `producer.name`, the schedule statement, the owner (the project named by the headers of the scripts, which must be a code in `org/projects/`) and write the gap cause from what the cited lines show. Keep every claim to what a cited line shows; where the repository cannot show why no later delivery came, say so in the `gap_cause` sentence.
3. Write the JSON file with the Write tool, ASCII, `indent=1`. Append the ONE surprise row to the channel file (fabric `site-z`; `surfaced_at` a full UTC timestamp from `date -u +%FT%TZ`; id `NFRA_MCPINDEX-Z-W95-S<k>` with `k` the next unused number of your slot). Run both criteria of section 4 until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u2_check.py` for exactly what each arm grades.
4. Then spot-check yourself: re-read each cited line; if it does not show what your sentence says, fix the entry. The issuer reads it at the drain and relays the owner and schedule MSTR to MSTR.

## 2. BOUNDS

1. You change only the files in `<paths>`. You READ the infrastructure, data, workflow and library sources named above and edit none of them. Do NOT edit the issuer's checks or decomposition, `members.yaml`, the catalog or its row files, the emitter, the PRD, or any other file. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file and the row. You write one data file, one surprise row and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output. No fix is proposed or made in this project (the gap is a data-freshness finding).
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u2.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u2_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~95/commonwealth_producer.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~95/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-u-2.commonwealth-producer.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W95-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).
The Commonwealth gap row is required by the contract (U2); any further row you file (a premise failure, a naming-gate note) is an additional row with its own number.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-u-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u2.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~95/commonwealth_producer.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (the Commonwealth feed opal-data-assets/commonwealth/cottonwood/silver/, its newest partition 2026-06-23 and 83 trading days behind); the clean control and the six planted negatives behave; the schema; the feed, newest partition and lag equal the census and report values; producer kind from the enum; the owner is a project of org/projects/ -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-u-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u2.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~95/commonwealth_producer.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the clean control and the nine planted negatives behave; the producer and schedule cites and at least two different evidence entries each name an existing repository file with the line inside it (three in the none-found form); the gap cause is ASCII and at least twelve words; the surprise row NFRA_MCPINDEX-Z-W95-S<k> stands in the channel file with the measured gap -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~95/NFRA_MCPINDEX.TO-MX-u-2.commonwealth-producer.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Commit the work first (the data file and the surprise row), then write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance).
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip. Message files are written with the Write tool, ASCII, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL.
4. Report once, with: what you built; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the producer, its schedule and the owner in one line with the one-sentence gap cause; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 27, workstream GATEWAY, worker ~95. Source: the CTO's round-26 analysis `ledger/ROUND_ANALYSIS.round26.md` (`1.0.0_SA_CTO~Z`, msg 36269, round-27 list item 3) and the CRO brief section 4.7 (@1ce8848c4b). Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round27-GATEWAY.md` (the contract R27.3 U2 is frozen at the cut). Base dry-runs 2026-10-21: `u2.AC1 base: FAIL as expected` and `u2.AC2 base: FAIL as expected` (the deliverable is absent; the census, clean-control and planted-negative arms pass, the final arm FAILs; ARMS 8 ok 1 failed for AC1, 10 ok 1 failed for AC2). A scratch reference file and channel (outside the repository, selected by the check's `U2_CHANNEL` hook) written from the issuer's own search passes both criteria (AC1 9 of 9 arms, AC2 11 of 11); the reference minus its surprise row fails AC2, and a copy with a single evidence entry and a fake owner fails both. The issuer's reading, for the worker to verify: there is no scheduled job. The bronze landing is `data/assets/scripts/bronze/commonwealth_landing.py` (`--apply` at line 149, a person's run, "Land one Commonwealth delivery zip"); the silver builders are the hand-run `data/assets/scripts/silver/commonwealth_*.py` of project `ADVI_COTBKF` (header of `commonwealth_transactions.py:1`; `DATA_DATE = "2026-06-23"` at `commonwealth_crosswalk.py:70`); `infra/aws` holds consumers only (the gateway adapter, `account-return-daily`, `reporting-gold-cot`). So the producer is `manual`, the schedule is none, the owner is `ADVI_COTBKF`, and the gap cause is that the feed is one closed vendor delivery with nothing that would fetch a later one. The count of 83 trading days was recomputed by the issuer from the calendar (24 June to 20 October 2026, weekdays less 3 July and 7 September). The checks prove shape and grounding (the real census values, enums, a project code, cites that resolve, the row), not that the chosen cause is the right one; the issuer samples the cited lines at the drain and relays the owner and schedule MSTR to MSTR (decomposition R27.4 step 3).

<status>complete</status>
<round>27</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
