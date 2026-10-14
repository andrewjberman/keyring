# ADVI_FIRMBKTS task order -- `FB-l-2` -- FWD-9(a): THE MOVE PLAN FOR COTTONWOOD (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R8.md</decomp_doc>
<owned_cells>FB-l-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~82</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only plan; nothing is scheduled or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`list`, `describe`, `get`, `head`). No grant, no put. A denied read is a `not_read` entry.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL, "cannot read"); the grader rejects a write verb in `calls`, a claim outside the four, a move with no rollback, proof or evidence, a dependency on an unknown move, an id-shaped token, a decommission without the 45-day window, and a record naming none of the required functions. Blindness: the grader proves shape and read-only discipline, not that the plan is right or complete; the CTO reads the plan and the issuer re-reads a sample of rows against the live plane.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-l-2` (round 8, FWD-9(a): the move plan, Cottonwood; read-only)

Advisor Intelligence (the portal's advisor analytics) is moving from three legacy buckets to one spelled-out bucket per firm. The legacy buckets are `opal-data-bd` (the shared Black Diamond data lake), `opal-data-inf` (Inflection) and `opal-data-cot` (Cottonwood). A firm's destination is `opal-data-<firm>` in its long form; 49 Financial is DONE and is the model (`opal-data-49financial`, keys `advi/49financial/{gold|platinum|state}/...`). Inflection and Cottonwood are next. The read-only inventories of everything that runs against the old homes already exist (round 7, workstream PLANINV). Your job is a written PLAN built from them and from LIVE reads. Writing a plan starts no move: you change nothing in AWS and nothing in the repository outside your own deliverables folder.

### 1a. Your slice

Write the move plan for COTTONWOOD. The plan holds one `moves` row for every Cottonwood operating function that touches a legacy home in the two inventories (`covers` names the
inventory row ids; an inventory row you decide needs no move is listed in `retire` or `open_questions` with the reason, never silently dropped). It MUST carry, each read LIVE and never assumed:
1. The two live homes of Cottonwood holdings: the edge router resolves `cottonwood` to `opal-data-cot`, while the IRPT holdings reader reads `opal-data-cottonwood` (that bucket exists).
   The plan names which is canonical, with the evidence (the router's firm map, the IRPT reader's configuration, the bucket's contents by listing counts only), and moves the other. If the
   evidence does not decide it, it goes to `open_questions` with the read that would.
2. The Cottonwood crosswalk input: it lives OUTSIDE every legacy home, at `opal-data-assets` prefix `commonwealth/cottonwood/silver/crosswalk/`, with its builder, 7 consumers and 11 module
   importers (inventory `PLANINV_COTTONWOOD_SERVING_CROSSWALK.json`). For each consumer, a move row or an explicit "unaffected, because" with the live read that shows it.
3. `cot-etf-ownership-daily`: its `SRC_BUCKET` environment value names `opal-data-cot` but its code does not read it. A move row that repoints or removes the value, with its rollback.
4. `router_iam.tf` lines 26-29: a guard comment cites the rule `mdpf-daily-refresh-trigger`, which was destroyed on 2026-08-18. Read the file at those lines and the live rule list; the plan
   names the correction (a comment-only change is still a move row with a rollback).
5. The Black Diamond Cottonwood scope lives in `opal-data-assets/blackdiamond/cottonwood/`, NOT in `opal-data-bd`; `bd-cot-freshness-probe` exists in the repository and reads `opal-data-cot`
   but no live function has that name; the graph Lambda `cot-satellites-registry-producer-daily` is absent live; `characteristics.json` has a writer although its header says zero. Give each a
   `moves`, `retire` or `open_questions` row.
6. The Cottonwood IAM-grant and Lambda-environment column, read LIVE for every Cottonwood function in the inventories.
7. The decommission of `opal-data-cot` (and of the second home if it is not canonical): its 45-day no-write window (FWD-6) and who reads it.
Order the moves so nothing is switched off without a recorded reason, and the first move is one that can be exercised on its own.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/PLAN_COTTONWOOD.json`

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

`order` is `FB-l-2`, `firm` is `cottonwood`. `moves` are ordered: `order` is the sequence in which the moves run, `depends_on` names the moves that must have landed first. EVERY move carries a
rollback (the exact step that restores it) and a proof (the read that shows it landed). Also write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/PLAN_COTTONWOOD.md` (the plan in prose, one page per section: the ordered move table, the
decommission of the legacy bucket and its 45-day window, the legacy operations to retire, the open questions, the `not_read` list). Inputs you build from (read them first):
- `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~78/PLANINV_COTTONWOOD_PIPELINE.json` (what runs, 42 rows)
- `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~79/PLANINV_COTTONWOOD_SERVING_CROSSWALK.json` (what serves, 56 rows, the crosswalk consumers)
- `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND8_PLAN_INPUTS_20261013.md` (the rulings and findings so far)
- `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md` (CONTRACTS and FWD-5, FWD-6, FWD-9)



## 2. BOUNDS

1. READ verbs only, on AWS and on the repository. No write, no producer run, no deploy, no product file edited, no `terraform` command. AWS from bash is `.tools/aws`.
   Downloaded files go to `C:/dev/wk-firmbkts-82-data/` (outside the checkout).
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
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/ADVI_FIRMBKTS.TO-FB-l-2.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-l-2"><invocation>cd C:/dev/wk-firmbkts-82 &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py plan --file C:/dev/wk-firmbkts-82/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/PLAN_COTTONWOOD.json --firm cottonwood --min 6 --require-text opal-data-cottonwood crosswalk cot-etf-ownership-daily</invocation><expect>^PLAN: OK firm=cottonwood moves=[0-9]+ retire=[0-9]+$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-l-2"><invocation>cd C:/dev/wk-firmbkts-82 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root C:/dev/wk-firmbkts-82 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and read-only discipline; AC2 is the write-surface bound. The plan's correctness and completeness are read by the CTO and the issuer.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/ADVI_FIRMBKTS.TO-FB-l-2.proof_of_spec.json`. Commit the two plan files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W82-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`.
Report once: the move count, the retire count, the denominators, what you could not read, AC1 and AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 8, cell 1 or 2 of 3 read-only cells (CTO round-7 analysis, msg 5482, `ledger/ROUND_ANALYSIS.round7.md` section 3 item 1). The plan is READ-ONLY; no Inflection or Cottonwood move starts. Slot ~82. Class LOCAL.

**CLOSE (2.0.0_SA_COO~B1, 2026-10-14 ~13:2xZ):** worker ~82 merged at f90ecab714 (branch tip 515e60fe4c); the issuer re-ran AC1 (`PLAN: OK firm=cottonwood moves=30 retire=6`) and AC2 (`ROUND 4 SCOPE: OK 5 changed, 0 outside, 0 required missing`) in the worker's tree. The plan recommends `opal-data-cottonwood` as the canonical home (the registry grades `opal-data-cot` its alias; the CTO's ratification is open question Q1), orders the repairs M1 to M5 before any copy, and puts the cutover at M13. Rows D1-W82-S1..S6 are OBSERVATION and INERT. The record carries extra keys beyond the template (unaffected, iam_env_column, canonical_decision, surprise_rows); the grader ignores them. The ONE plan document is `ledger/FWD9_MOVE_PLAN.md`. Gate limb: none graded (no criterion changed).

<status>complete</status>
<round>8</round>
<workstream>MOVEPLAN</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-l-2</to_id>
<slot>~82</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
