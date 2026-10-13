# ADVI_FIRMBKTS task order -- `FB-k-3` -- PLAN INVENTORY (READ-ONLY): COTTONWOOD: WHAT RUNS (EVENTBRIDGE RULES, SCHEDULES, TASKS, S3 EVENTS, PIPELINE SCRIPTS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_PLANINV.md</decomp_doc>
<owned_cells>FB-k-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~78</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only inventory; nothing is scheduled or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`list`, `describe`, `get`, `head`). No grant, no put. A denied read is a `not_read` entry.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL, "cannot read"); the grader rejects a write verb in `calls`, a claim outside the four, a row with no evidence, fewer than the minimum rows, a wrong firm, an id-shaped token, and (for the Cottonwood serving cell) a record naming no crosswalk consumer. Blindness: the grader proves shape and read-only discipline, not completeness; the issuer re-reads a sample of rows against the live plane and judges coverage from the denominators.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-k-3` (workstream PLANINV: the evidence base for the FWD-9 move plan; read-only)

Advisor Intelligence is moving from the three legacy buckets to a spelled-out bucket per firm (49 Financial is done; Inflection and Cottonwood are next, after the plan). The plan needs
a list of everything that runs against the old homes, so that nobody has to discover, at shutdown, an operation still running against one. You produce the INVENTORY for your slice. You
change nothing and you propose nothing; the plan is written later from your record.

Facts you may rely on: the legacy buckets are `opal-data-bd` (the shared Black Diamond data lake), `opal-data-inf` (Inflection) and `opal-data-cot` (Cottonwood); the destination for a firm is
`opal-data-<firm>` in its long form (`opal-data-49financial` exists and is the model: keys read `advi/49financial/{gold|platinum|state}/...`); `opal-data-inf/gold/meta/pipeline-complete.json` is a
prohibited key watched by the `mdpf-feeder-accelerator` rule; `opal-data-inf/orion/jwt/current.json` is a live credential object that stays where it is (never read or print its contents). Starting
points: `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md` (CONTRACTS), `docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md`, and the key-class tables
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json` and `census.json` (key paths there may hold ids: copy none).

### 1a. Your slice

Inventory every thing that STARTS or RUNS an Advisor Intelligence pipeline for the Cottonwood firm and touches `opal-data-cot` or the Cottonwood scope inside `opal-data-bd`:
1. EventBridge rules (list all, then describe those whose pattern, input or targets name `opal-data-cot`, the Cottonwood scope or the gold chain), with their targets.
2. EventBridge Scheduler schedules (the scheduler API).
3. ECS task definitions and services, Step Functions state machines and the gold runner that read or write those buckets; S3 bucket notification configurations on `opal-data-cot` and `opal-data-bd`.
4. The repository's pipeline scripts that name `opal-data-cot` (gold, ingest, dispatch, value-parity scripts under `data/` and `infra/`): one row per script with the keys it reads and writes.
Record at least five rows. Denominators: rules, schedules, task definitions, notification configurations and repository files scanned.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/PLANINV_COTTONWOOD_PIPELINE.json`

```json
{"order": "FB-k-3", "read_at": "<ISO UTC>", "firm": "cottonwood", "scope": "<one sentence: what this inventory covers>",
 "calls": ["aws events list-rules ...", "comp-find --corpus aws ...", "..."],
 "denominators": {"<what was scanned>": 0},
 "functions": [
  {"id": "<short stable id>", "kind": "rule|schedule|task|service|lambda|edge|topic|email|script|role|reader|other", "name": "<resource name or file path>",
   "trigger": "<what starts it: cron, event pattern, S3 event, invocation, manual>",
   "reads":  [{"bucket": "<bucket>", "prefix": "<key prefix or key class>", "claim": "measured|inferred|held|absent"}],
   "writes": [{"bucket": "<bucket>", "prefix": "<key prefix or key class>", "claim": "measured|inferred|held|absent"}],
   "legacy_touch": true, "consumer_note": "<who or what consumes its output; for the Cottonwood crosswalk name it>",
   "evidence": "<the call or file:line that shows it>", "claim": "measured|inferred|held|absent"}],
 "not_read": ["<each thing you could not read, and why>"],
 "claim": "measured"}
```
`legacy_touch` is true when the function reads or writes the firm's LEGACY home (`opal-data-cot`, or the firm's scope inside `opal-data-bd`); such a row lists the access. Also write
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/PLANINV_COTTONWOOD_PIPELINE.md` (one page: the table of rows, the totals, the `not_read` list).

## 2. BOUNDS

1. READ verbs only, on AWS and on the repository. No write, no producer run, no deploy, no product file edited, no `terraform` command. AWS from bash is `.tools/aws`.
   Downloaded files go to `C:/dev/wk-firmbkts-78-data/` (outside the checkout).
2. Read AWS through the served graph first: `comp-find --corpus aws '<regex>'` lists CloudNodes with a printed denominator; then ONE live `describe`/`get`/`list` of one
   resource per call. The repository is searched with the Grep and Glob tools or `comp-find` (a recursive shell grep is denied by the rail; the denial prints the command to run next).
3. Print NO secret and no credential. For a Lambda environment record the variable NAMES, and a value only when it is a bucket, region, table or queue name. Print no client name, no account
   number and no relationship id: where a key or text holds one, write `<id>` in its place (the grader rejects any token of nine or more digits except the AWS account number 313476888478).
4. Every row carries its claim in a field a consumer can reject on: `measured` (you read it live or in the file at a stated line), `inferred`, `held`, `absent`. A thing you could not read is a
   `not_read` entry and `claim: absent`, never a guess and never a silent omission. Print the DENOMINATOR of every sweep (rules, schedules, functions, files scanned) in `denominators`.
5. Each AWS call is bounded (`timeout 100`); a sweep too large to finish is reported as partial counts, not left running.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/ADVI_FIRMBKTS.TO-FB-k-3.cottonwood-pipeline.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-k-3"><invocation>cd C:/dev/wk-firmbkts-78 &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py planinv --file C:/dev/wk-firmbkts-78/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/PLANINV_COTTONWOOD_PIPELINE.json --firm cottonwood</invocation><expect>^PLANINV: OK firm=cottonwood rows=[0-9]+ legacy=[0-9]+$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-k-3"><invocation>cd C:/dev/wk-firmbkts-78 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root C:/dev/wk-firmbkts-78 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and read-only discipline; AC2 is the write-surface bound. The inventory's completeness is read by the issuer from the denominators and a sample re-read.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/ADVI_FIRMBKTS.TO-FB-k-3.cottonwood-pipeline.proof_of_spec.json`. Commit the scripts and the two record files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W78-S<k>`, `k` from 1,
`surfaced_at` from `date -u +%FT%TZ`. Report once: the row count, how many are `legacy_touch`, the denominators, what you could not read, AC1 and AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's word (msg 5215, Andrew-direct ~21:1xZ "don't hold back"): read-only per-firm inventories NOW as workstream PLANINV under PRD v1.5 FWD-9, a separate workstream from
round 7's frozen decomposition, disjoint write surface (this deliverables folder). The plan itself stays round 8; writing it starts no Inflection or Cottonwood move. Class LOCAL.

<status>complete</status>
<round>7</round>
<workstream>PLANINV</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-k-3</to_id>
<slot>~78</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
