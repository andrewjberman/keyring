# ADVI_FIRMBKTS task order -- `FB-l-1` -- FWD-9(a): THE MOVE PLAN FOR INFLECTION (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R8.md</decomp_doc>
<owned_cells>FB-l-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~81</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only plan; nothing is scheduled or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`list`, `describe`, `get`, `head`). No grant, no put. A denied read is a `not_read` entry.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL, "cannot read"); the grader rejects a write verb in `calls`, a claim outside the four, a move with no rollback, proof or evidence, a dependency on an unknown move, an id-shaped token, a decommission without the 45-day window, and a record naming none of the required functions. Blindness: the grader proves shape and read-only discipline, not that the plan is right or complete; the CTO reads the plan and the issuer re-reads a sample of rows against the live plane.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-l-1` (round 8, FWD-9(a): the move plan, Inflection; read-only)

Advisor Intelligence (the portal's advisor analytics) is moving from three legacy buckets to one spelled-out bucket per firm. The legacy buckets are `opal-data-bd` (the shared Black Diamond data lake), `opal-data-inf` (Inflection) and `opal-data-cot` (Cottonwood). A firm's destination is `opal-data-<firm>` in its long form; 49 Financial is DONE and is the model (`opal-data-49financial`, keys `advi/49financial/{gold|platinum|state}/...`). Inflection and Cottonwood are next. The read-only inventories of everything that runs against the old homes already exist (round 7, workstream PLANINV). Your job is a written PLAN built from them and from LIVE reads. Writing a plan starts no move: you change nothing in AWS and nothing in the repository outside your own deliverables folder.

### 1a. Your slice

Write the move plan for INFLECTION. The plan holds one `moves` row for every Inflection operating function that touches the legacy home (`opal-data-inf`) in the two
inventories (`covers` names the inventory row ids; an inventory row you decide needs no move is listed in `retire` or `open_questions` with the reason, never silently dropped). It
MUST carry, each read LIVE and never assumed:
1. `inf-portal-publisher` and `inf-silver-aggregator`: `opal-data-inf` carries two S3 notifications, `gold/meta/` + `pipeline-complete.json` -> `inf-portal-publisher` and
   `silver/_silver_complete/` + `.json` -> `inf-silver-aggregator`. For the publisher, FIRST read how the comparable 49 Financial portal publish is triggered today (the live
   EventBridge rule, Scheduler schedule or S3 notification on `opal-data-49financial` and its target; read it, do not infer it), then give the publisher that same shape in Inflection's
   own new bucket, with its rollback and its proof; or, if 49 Financial's shape cannot be mirrored, an `open_questions` entry saying why. Give the silver aggregator its own move.
2. The Door 6 marker `opal-data-inf/gold/meta/pipeline-complete.json`, its S3 notification, the rule `mdpf-feeder-accelerator` and the `router_iam` Door 6 deny: Andrew ruled they RETIRE, but
   NOT before `inf-portal-publisher` has a new trigger (the marker IS the publisher's trigger today). Put their retirement in ONE move ordered AFTER the publisher's move
   (`depends_on` it), with a rollback.
3. `exec-summary-trigger`: ENABLED live (event pattern `chain-complete` from `bd-pipeline.gold-chain`, sole target `exec-summary-generator`), but Terraform declares only a DISABLED
   placeholder and nothing declares the live rule. Read the live rule and the Terraform placeholder (`infra/aws/terraform/exec-summary/main.tf`) and give a move that brings the live rule
   under Terraform (import, or replace the placeholder), or record why not.
4. The Inflection IAM-grant and Lambda-environment column, read LIVE (the served graph cannot answer it): for every Inflection function in the inventories, the roles with an Allow on
   `opal-data-inf` and the environment variables that name a bucket. A move row that changes a function's bucket names the grant it needs on the new bucket.
5. `inf-canonical-prices-daily` (disabled and held) and `FIRMSEP-s3-direct-access-bypass`: a `retire` entry each, with the plan's recommendation and who decides.
6. The decommission of `opal-data-inf`: B2 (`opal-data-inf/orion/jwt/current.json`) STAYS by Andrew's word, so the bucket stays open for that one credential alone; the decommission names it as
   out of the 45-day set.
Order the moves so nothing is switched off without a recorded reason, and the first move is one that can be exercised on its own.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json`

```json
{"order": "<cell id>", "read_at": "<ISO UTC>", "firm": "<inflection|cottonwood>",
 "calls": ["aws events list-rules ...", "comp-find --corpus aws ...", "..."],
 "denominators": {"<what was scanned>": 0},
 "moves": [
  {"id": "M1", "function": "<resource name or file path>", "kind": "rule|schedule|lambda|edge|notification|script|role|reader|other",
   "from": "<its legacy home or trigger, as read live>", "to": "<its new home or trigger>", "order": 1, "depends_on": [],
   "rollback": "<the exact step that puts it back>", "proof": "<the read that shows the move landed>",
   "covers": ["<inventory row ids this move covers>"], "evidence": "<the call or file:line>", "claim": "measured|inferred|held|absent"}],
 "decommission": {"legacy_bucket": "<opal-data-...>", "window_days": 45, "basis": "<what starts the 45-day no-write window and who reads it>", "claim": "measured|inferred|held|absent"},
 "retire": [{"id": "R1", "operation": "<legacy operation the move makes unnecessary>", "consumers": 0, "decision": "<what the plan recommends and who decides>"}],
 "open_questions": ["<each fork the plan cannot close, with what would close it>"],
 "not_read": ["<each thing you could not read, and why>"], "claim": "measured"}
```

`order` is `FB-l-1`, `firm` is `inflection`. `moves` are ordered: `order` is the sequence in which the moves run, `depends_on` names the moves that must have landed first. EVERY move carries a
rollback (the exact step that restores it) and a proof (the read that shows it landed). Also write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.md` (the plan in prose, one page per section: the ordered move table, the
decommission of the legacy bucket and its 45-day window, the legacy operations to retire, the open questions, the `not_read` list). Inputs you build from (read them first):
- `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~76/PLANINV_INFLECTION_PIPELINE.json` (what runs, 54 functions)
- `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~77/PLANINV_INFLECTION_SERVING.json` (what serves and notifies, 97 rows)
- `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND8_PLAN_INPUTS_20261013.md` (the rulings and findings so far)
- `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md` (CONTRACTS and FWD-5, FWD-6, FWD-9)



## 2. BOUNDS

1. READ verbs only, on AWS and on the repository. No write, no producer run, no deploy, no product file edited, no `terraform` command. AWS from bash is `.tools/aws`.
   Downloaded files go to `C:/dev/wk-firmbkts-81-data/` (outside the checkout).
2. Read AWS through the served graph first: `comp-find --corpus aws '<regex>'` lists CloudNodes with a printed denominator; then ONE live `describe`/`get`/`list` of one resource
   per call. The repository is searched with the Grep and Glob tools or `comp-find` (a recursive shell grep is denied by the rail; the denial prints the command to run next).
3. Print NO secret and no credential. For a Lambda environment record the variable NAMES, and a value only when it is a bucket, region, table or queue name. Print no client name, no
   account number and no relationship id: where a key or text holds one, write `<id>` in its place (the grader rejects any token of nine or more digits except the AWS account number 313476888478).
   `opal-data-inf/orion/jwt/current.json` is a live credential object that stays where it is: never read or print its contents.
4. Every row carries its claim in a field a consumer can reject on: `measured` (you read it live or in the file at a stated line), `inferred`, `held`, `absent`. A thing you could not read is
   a `not_read` entry, never a guess and never a silent omission. Print the DENOMINATOR of every sweep in `denominators`.
5. Each AWS call is bounded (`timeout 100`); a sweep too large to finish is reported as partial counts, not left running.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/ADVI_FIRMBKTS.TO-FB-l-1.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-l-1"><invocation>cd C:/dev/wk-firmbkts-81 &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py plan --file C:/dev/wk-firmbkts-81/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json --firm inflection --min 10 --require-text inf-portal-publisher inf-silver-aggregator exec-summary-trigger mdpf-feeder-accelerator</invocation><expect>^PLAN: OK firm=inflection moves=[0-9]+ retire=[0-9]+$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-l-1"><invocation>cd C:/dev/wk-firmbkts-81 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root C:/dev/wk-firmbkts-81 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and read-only discipline; AC2 is the write-surface bound. The plan's correctness and completeness are read by the CTO and the issuer.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/ADVI_FIRMBKTS.TO-FB-l-1.proof_of_spec.json`. Commit the two plan files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W81-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`.
Report once: the move count, the retire count, the denominators, what you could not read, AC1 and AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 8, cell 1 or 2 of 3 read-only cells (CTO round-7 analysis, msg 5482, `ledger/ROUND_ANALYSIS.round7.md` section 3 item 1). The plan is READ-ONLY; no Inflection or Cottonwood move starts. Slot ~81. Class LOCAL.

<status>pending</status>
<round>8</round>
<workstream>MOVEPLAN</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-l-1</to_id>
<slot>~81</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
