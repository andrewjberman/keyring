# NFRA_MCPINDEX task order -- `MX-z-2` -- name the copier of the catalogued Eclipse tables (the job that fills `opal-data-assets/eclipse/inflection/silver/` from the producer's `opal-data-inf/silver/eclipse/`), its schedule, its owner and why the copy is one trading day behind

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md</decomp_doc>
<owned_cells>MX-z-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-z-2.eclipse-copier</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~91</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is created; one JSON data file that NAMES an existing schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (both criteria FAIL at the base) and the planted negatives inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-z-2` (round 26, workstream GATEWAY; PRD v0.19 FWD-23; CTO ruling `CTO_RULING_ADVISOR_TABLES_PER_VENDOR_ROUTING_20261020_Z.md`, item 8: "The Eclipse catalogued copy is 1 trading day behind. Name its copier and schedule")

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The CRO's brief (`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md`, section 4.2) measured that the producer's own output `opal-data-inf/silver/eclipse/` holds the partition 2026-10-20 while the catalogued copy `opal-data-assets/eclipse/inflection/silver/` (four tables: `fact_models`, `fact_model_composition`, `fact_portfolios_simple`, `fact_portfolios_full`) stops at 2026-10-17 and misses 2026-10-19: one trading day behind. Nobody has named the job that fills the copy. You name it, its schedule and its owner, from the repository, and say why it runs a day behind.

**What was seen (the issuer's leads; verify them, do not trust them).** The census entries for the two prefixes are in `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/census.json` (the `live-extra` entry `opal-data-inf` `silver/eclipse/`, newest partition 2026-10-20; the four `catalog` entries `opal-data-assets` `eclipse/inflection/silver/<table>/`, newest 2026-10-17). A first search points at the `opal-assets` pipeline rather than a plain copy of the producer's silver: the Lambda `opal-assets-ingest-mirror` (`infra/aws/lambda/opal-assets/opal-assets-ingest-mirror/lambda_function.py`, its `eclipse/inflection` row) mirrors the producer's BRONZE (`opal-data-inf` `bronze/eclipse/`) into `opal-data-assets` `eclipse/inflection/bronze/`, and the Lambda `opal-assets-silver-eclipse` (`infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/`) converts that bronze into the silver copy; the schedules sit in `infra/aws/terraform/opal-assets/mirror.tf` and `silver.tf`. Decide for yourself whether that chain is "the copier", read each schedule, and follow the lag to its cause (the mirror slots against the producer's landing time, the silver sweep slot, the bronze event rule).

**What to build.** `deliverables/0.9.0_WK_NFRA_MCPINDEX~91/eclipse_copier.json`, one object, and no other deliverable.

### The contract (verbatim from the decomposition; it is the whole specification)

**Z2 ECLIPSE COPIER** `eclipse_copier.json`, schema `gateway_eclipse_copier/1`: `{"schema","producer":{"bucket","prefix","owner_project"},"copy":{"bucket","prefix"},"copier":{"kind":"lambda"|"script"|"glue"|"ecs-task"|"terraform-only"|"other","name":str,"cite":"<path>:<line>"},"schedule":{"expression":str,"cite":"<path>:<line>"},"lag":{"trading_days":int,"cause":str},"owner":str,"evidence":[str,...]}`. `producer` is `opal-data-inf` `silver/eclipse/`; `copy` is the catalogued copy named by the catalog (the Eclipse silver prefix under `opal-data-assets`, read from the catalog rows of the Eclipse entities and the CRO brief section 4.2). Find, in the repository, the code or infrastructure that copies producer output into the copy (a Lambda, script, Glue job or scheduled task) and its schedule. `copier.cite`, `schedule.cite` and every `evidence` entry must resolve (the file and line exist); at least two evidence entries; `lag.trading_days` is 1 (the brief); `lag.cause` is at least eight ASCII words explaining the lag from the schedule against the producer's cadence; `owner` is the project code that owns the copier (a code that exists in `org/projects/`). When no copier is found in the repository, `copier.kind` is `terraform-only` or `other` with `name` `none-found`, `cite` the path of the closest candidate searched, and `evidence` at least three entries naming what was searched.

How the checks read it, so you write it to pass:
- `producer` is exactly `{"bucket": "opal-data-inf", "prefix": "silver/eclipse/", "owner_project": <a project code>}`; `copy` is exactly `{"bucket": "opal-data-assets", "prefix": "eclipse/inflection/silver/"}` (the common prefix of the four catalogued Eclipse tables in the census). `owner_project` and `owner` are project codes that have a file `org/projects/<CODE>.json` (for example `OPAL_ASSETS`); `owner_project` is the project that owns the PRODUCER's output, `owner` the project that owns the COPIER.
- `copier.kind` is one of `lambda`, `script`, `glue`, `ecs-task`, `terraform-only`, `other`; `copier.name` is a nonempty ASCII string (it may name the chain: two Lambdas); `schedule.expression` is a nonempty ASCII string (the cron or rate expression(s) as written in the source, in your own words if there are several).
- `copier.cite` and `schedule.cite` are `<repo-relative path>:<line number>` where the file exists in your worktree and the line is inside it; every `evidence` entry is the same form; the entries are DIFFERENT strings; at least two (three when `copier.name` is `none-found`, with `copier.kind` `terraform-only` or `other`).
- `lag.trading_days` is the integer `1`; `lag.cause` is one plain ASCII sentence of at least eight words.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/4.0.0_SA_CRO~Y/ADVISOR_TABLES_PER_VENDOR_BRIEF_20261020.md` (section 4.2) and `census.json` (the five entries named above).
- The infrastructure and ETL sources, READ-ONLY: `infra/aws/lambda/` (notably `opal-assets/`), `infra/aws/terraform/` (notably `opal-assets/` and `inf-pipeline/`), `infra/aws/lambda/ci/function-map/`, `data/` (notably `data/inf/scripts/` and `data/assets/scripts/`), `workflows/`, `lib/`, and any ETL scheduler you find. The catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` holds the rows of the four Eclipse tables.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. THE SPARSE CONE MAY LACK THE FOLDERS YOU MUST READ. Your first step is `git sparse-checkout add` of whichever of `infra`, `data`, `lib`, `workflows` you need (the issuer pre-adds `infra/aws`, `workflows`, `lib` and `data`; verify with `ls`); adding sparse folders is the ONLY sparse change you may make, and you MUST add what you need BEFORE you conclude that no copier exists (an absent folder is not an absent copier). A cited file must exist in YOUR worktree for the checks to resolve it, so add the folder of every file you cite.
1. Search with the Grep tool (a `path` and a `glob`) and the Glob tool, or `comp-find`; the repository-wide recursive-search rail denies a blind recursive grep run through Bash (CLAUDE.md rule 21), so do not shell out to `grep -r` or `find` over the repository. Start with the strings `eclipse/inflection/silver`, `eclipse/inflection/bronze` and `silver/eclipse`, and with file names containing `eclipse` (Glob `**/*eclipse*` under `infra` and `data`). Read the Lambda that writes the copy's prefix, then the rule or schedule that invokes it, and the code that fills its INPUT. Note the producer's landing time (the comments in `mirror.tf` and `channel_sources.py` state it).
2. Choose `copier.kind`, `copier.name`, the schedule, the owner (the project named by the tags or headers of the infrastructure file, which must be a code in `org/projects/`) and the producer's owner project, and write the lag cause by setting the schedule slots against the producer's cadence. Keep every claim to what a cited line shows.
3. Write the file named above with the Write tool, ASCII, `indent=1`. Run both criteria of section 4 until each prints `RESULT: PASS`. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z2_check.py` for exactly what each arm grades.
4. Then spot-check yourself: re-read each cited line; if it does not show what your sentence says, fix the entry. The issuer reads it at the drain.

## 2. BOUNDS

1. You change only the files in `<paths>`. You READ the infrastructure, data, workflow and library sources named above and edit none of them. Do NOT edit the issuer's checks or decomposition, `members.yaml`, the catalog or its row files, the emitter, the PRD, or any other file. No AWS call, no network call, no grant, no deploy, no push.
2. ASCII only in the data file. You write one data file and no code.
3. The data file is JSON written with the Write tool, `indent=1`, ASCII.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z2.AC1.sh` and `.AC2.sh` (they run `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z2_check.py`). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~91/eclipse_copier.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~91/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-z-2.eclipse-copier.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W91-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-z-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z2.AC1.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~91/eclipse_copier.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line (the census producer opal-data-inf/silver/eclipse/ and the catalogued copy opal-data-assets/eclipse/inflection/silver/); the clean control and the six planted negatives behave; the schema; the producer and copy equal the census values; copier kind from the enum; owners are projects of org/projects/; lag of one trading day -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-z-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round26/checks/z2.AC2.sh org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~91/eclipse_copier.json; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the clean control and the seven planted negatives behave; the copier and schedule cites and at least two different evidence entries each name an existing repository file with the line inside it (three in the none-found form); the lag cause is ASCII and at least eight words -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~91/NFRA_MCPINDEX.TO-MX-z-2.eclipse-copier.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the copier, its schedule and the owner in one line with the one-sentence lag cause; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 26, workstream GATEWAY, worker ~91. Source: the CTO's round-25 analysis `ledger/ROUND_ANALYSIS.round25.md` (`1.0.0_SA_CTO~Z`, round-26 list item 2) and the CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_ADVISOR_TABLES_PER_VENDOR_ROUTING_20261020_Z.md` item 8 (CRO~Y brief @1ce8848c4b; Andrew-direct @790786dcfc). Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round26-GATEWAY.md` (the contract R26.3 Z2 is frozen at the cut). Base dry-runs 2026-10-20: `z2.AC1 base: FAIL as expected` and `z2.AC2 base: FAIL as expected` (the deliverable is absent; the census, clean-control and planted-negative arms pass, the final arm FAILs; ARMS 8 ok 1 failed for each). A scratch reference file (outside the repository) written from the issuer's own search passes both criteria (AC1 9 of 9 arms, AC2 9 of 9). The issuer's reading, for the worker to verify: the catalogued copy is built in two hops, not copied from the producer's silver. (1) `opal-assets-ingest-mirror` (`lambda_function.py:121`, the `eclipse/inflection` row: source `opal-data-inf` `bronze/eclipse/`, destination `eclipse/inflection/bronze/`) runs on `mirror.tf:106` `cron(5 13 * * ? *)` and the late poll `mirror.tf:230` `cron(5 17 * * ? *)`, both with `{"firm":"inf"}`. (2) `opal-assets-silver-eclipse` converts the bronze `.json` keys into `eclipse/inflection/silver/` on the bronze event rule `silver.tf:246` and on the sweep `silver.tf:292` `cron(0 16 * * ? *)`. The producer's eclipse landing is stated as about 14:48Z at `mirror.tf:98`, and the comment at `mirror.tf:99-105` says the first mirror slot "MUST postdate eclipse's landing" while the expression reads 13:05Z: that mismatch is the leading lag cause, so a same-day partition waits for the 17:05Z poll and the event convert. Owner of the copier: `OPAL_ASSETS` (tags at `mirror.tf:107`); the producer's bronze puller sits in the inf-pipeline Terraform (`br1-eclipse-rehome.tf`, plan under project `OPAL_VENDORPROVENANCE`); the worker decides the producer's owner project from the headers it reads. The checks prove shape and grounding (the real census prefixes, enums, project codes, cites that resolve), not that the chosen cause is the right one; the issuer samples the cited lines at the drain and relays the owner and schedule MSTR to MSTR (decomposition R26.4 step 2).

<status>issued</status>
<round>26</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
