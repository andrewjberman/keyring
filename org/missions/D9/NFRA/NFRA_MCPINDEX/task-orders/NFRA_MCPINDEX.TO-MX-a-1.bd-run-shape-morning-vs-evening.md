# NFRA_MCPINDEX task order -- `MX-a-1` -- confirm the shape of the BD morning run against the evening run before the evening writer is decommissioned (Andrew-direct)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-a-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-a-1</to_id>
<issued_to>0.7.0_AE_CloudOps~MI</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE for PHASE A -- read-only; nothing is published, applied or invoked.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change in PHASE A.
comp-adversary: DECLARED-NOT-APPLICABLE -- an investigation record; its answers are graded at L9 (AC2).
EGRESS CLASS, declared: NONE beyond Opal's own AWS. NO call to Black Diamond (its REST API or portal) -- read what the runs already landed.
</preflight>

## 1. THE CELL -- `MX-a-1` (Andrew-direct 2026-10-06 ~19:4xZ)

**Andrew's word, verbatim** (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261006_194xZ_BD_CONSOLIDATE_WRITERS_INVESTIGATE_SHAPE_FIRST_SEAT_AE_MI.md`):
"Yes we can consolidate writers. I need you to investigate first. I need you to check what the shape of the morning
run is (is it rest api? what fields/data come back? does it have as of provenance in any metadata BD-side?). Then i
need you to compare that to the evening run, which im guessing is a manual ec2 browser crawl thing. If the morning one
is in better condition, more rich data, id rather get rid of the night one. But we need to confirm the shape first
before making that move. ... If it turns out that the evening one is extraneous, then the agent can decommission that
run, and you proceed with your work on the MCPINDEX side"

**The two runs, as the issuer read them at 2026-10-06T19:4xZ.** Confirm or correct every line below with your own
read.
- **MORNING:**
  - `bd-49f-runner` (Lambda `infra/aws/lambda/bd-pipeline/bd-49f-runner/`, rule `bd-49f-session-daily`
    `cron(0 0 * * ? *)`) pulls from Black Diamond and lands bronze at
    `s3://opal-data-bd/forwardfill_v2/<table>/...xlsx`. For transactions it also writes a sidecar,
    `forwardfill_v2/transactions/_complete/<date>.json` (`has_data_rows`, `basis`).
  - On a complete day it writes `bronze/<date>/_BRONZE_COMPLETE.json`. The S3 notification
    `BronzeCompleteSilverMerge` then fires `bd-silver-merge` (`infra/aws/lambda/bd-pipeline/bd-silver-merge/`), which
    runs `s3://opal-data-bd/code/silver/merge-daily-incremental.py` and writes `silver/{transactions,realized,
    unrealized,allocations}/`.
  - Session plumbing: `bd-49f-session-trigger`, `bd-49f-keepalive`.
  - Terraform: `infra/aws/terraform/bd-pipeline/bd-49f-interim.tf`.
- **EVENING:**
  - SSM documents `opal-bd-transaction-download` and `opal-bd-realized-download` (repo JSON under `infra/aws/ssm/`),
    dispatched by rules `bd-transaction-pipeline-trigger` `cron(53 21 ? * MON-FRI *)` and
    `bd-realized-pipeline-trigger` `cron(45 21 ? * MON-FRI *)` onto an EC2 instance (`/opt/bd-exporter`, t3.medium,
    shuts itself down).
  - The repo JSON says the Playwright portal download was REMOVED after BD added MFA (~2026-06-23; order MX-s-14).
    The document now runs only `scripts/merge-daily-incremental.py` over the morning run's bronze.
  - **If the SERVED Default version agrees, the evening run fetches nothing from BD. It is a second merger of the
    same bronze, not a second source.**
- **Why the evening run still matters today:** on Mondays and Tuesdays BD posts transactions late. The morning puller
  withholds the complete marker (9 of 9 Mon/Tue dates since 09-03, plus 10-05 and 10-06, measured ABSENT at 18:29Z),
  so `bd-silver-merge` does not fire, and the evening document is the only same-day merger on those days.
- **Prepared work you inherit:** `NFRA_MCPINDEX.TO-MX-s-18` (the runner's own completeness check, built and tested on
  branch `wk-nfra_mcpindex-r7-24` @3709ae40d6) and `NFRA_MCPINDEX.TO-MX-s-19` (retire the documents' merge step).
  Read both ANNOUNCEs:
  - `git show 3709ae40d6:org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/ANNOUNCE_MX-s-18.md`
  - `git show 3709ae40d6:org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/ANNOUNCE_MX-s-17.md`

### PHASE A -- read-only (this order's whole scope)

1. **MORNING SHAPE.** From the runner's code and what it landed, never by calling BD:
   - Transport: REST or browser; the base URL and endpoint paths as named in code; auth and session.
   - Per table (transactions, realized, unrealized, allocations): the request the runner makes; the landed object's
     key pattern; its columns (read 1 recent bronze xlsx per table: header row, column count, row count);
     date-window semantics.
   - **BD-side as-of provenance:** does any BD response field, header or landed column carry an as-of, posting or
     run date that BD itself stamps (as opposed to our own `as_of`/sidecar)? Name the field and the file it was read
     from, or state ABSENT with the files read as the denominator.
2. **EVENING SHAPE.**
   - `aws ssm describe-document` + `get-document --document-version <Default>` for both documents: quote the served
     Default content's fetch lines. Does any step call BD, the portal or Playwright?
   - Read the latest 3 evening logs at `s3://opal-data-bd/logs/{transaction,realized}-download-<date>.log`: what
     they did, rows written, rc.
   - Read the instance's identity: instance id, state, and what else that instance runs (the other `opal-bd-*`
     documents and their rules). Decommissioning these two must not strand another job.
3. **COMPARE + VERDICT.**
   - Same source or different?
   - Is any field present in the evening's output and absent from the morning's? Compare silver columns from one
     morning-written and one evening-written partition of the same table.
   - `evening_extraneous` true/false.
   - If true, `preconditions_to_decommission`. At minimum: the Mon/Tue gap must be closed first (MX-s-18 live),
     otherwise Mon/Tue silver lands about 2 days late.
4. **WRITE** `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/BD_RUN_SHAPE_COMPARISON.json` in
   the keys AC1 reads, plus a one-page `BD_RUN_SHAPE_COMPARISON.md` in plain words for Andrew. Report once and STOP.
   The decommission is PHASE B of a later order, issued on the issuer's read of your verdict, under never-widen
   halves (CTO + COO).

## 2. BOUNDS

1. Read-only: no publish, apply, invoke, rule change, instance start or stop, or SSM send-command.
2. No call to Black Diamond by any route (vendor egress needs Andrew's per-use word). Nothing under `data/cot/`.
3. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/tier2_senior/0.7.0_AE_CloudOps~MI/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-AEMI-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

Commit with `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~MI <0.7.0_AE_CloudOps~MI@opal.agent>" -F <msgfile> -- <paths>`.

## 4. PROOF OF SPEC (literal; run from the workspace root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-a-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/a1.AC1.sh; echo "exit=$?"</invocation><expect>morning tables: 4; every required key present with evidence; evening fetches_from_bd and verdict evening_extraneous are booleans -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-a-1" judgment="true"><invocation>JUDGMENT at L9: read BD_RUN_SHAPE_COMPARISON.md against its cited files</invocation><expect>each of Andrew's three questions (transport, fields returned, BD-side as-of provenance) and the evening comparison is answered from a cited file or log, not inferred</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-a-1.bd-run-shape-morning-vs-evening.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`, flip `<status>` to `complete`, and report once to
`2.0.0_SA_COO~MI`: the verdict in one line, plus the record's path.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).**
- Andrew-direct cell, cut mid-round 7 on his word, as workstream BDOPS: its boundary is the BD run-shape record and
  its write surface is the AE seat's deliverables, disjoint from the first issuance.
- `<risk>SERVED</risk>`: it reads live AWS state and changes none.
- Battery dry-run at base: a1.AC1 FAIL as expected (record absent).
- **ISSUER CORRECTIONS (2026-10-06 ~21:2xZ, on the seat's rows Z-S81 and msg 30308):** the id `MX-a-1` was already a
  decomposition cell (the portal property row, decomp line 377); this order is the Andrew-direct BD run-shape cell of
  workstream BDOPS and serves no decomposition row. The gate's "1 owned cell resolves" matched that other cell. The id
  is kept because the order is terminal and cited. The prescribed row-id form `Z-AEMI-S<k>` was wrong; the seat minted
  Z-S77..Z-S81.
- **ISSUER GRADE:** a1.AC1 re-run on CLOUD @b4e1284fad: 4 tables, fetches_from_bd=False, evening_extraneous=True,
  RESULT: PASS. AC2 is the CVO's at L9.
- MX-s-17 (repoint the evening documents) is likely superseded if the verdict reads `evening_extraneous: true`. The
  issuer rules that on the verdict, not before.

<status>complete</status>
<round>7</round>
<workstream>BDOPS</workstream>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
