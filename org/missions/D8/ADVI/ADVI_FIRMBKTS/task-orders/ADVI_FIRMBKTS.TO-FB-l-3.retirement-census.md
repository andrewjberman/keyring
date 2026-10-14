# ADVI_FIRMBKTS task order -- `FB-l-3` -- FWD-9(b): THE CONSUMER CENSUS OF EVERY RETIREMENT CANDIDATE, AND THE FIRST ONE WITH NO LIVE CONSUMER (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R8.md</decomp_doc>
<owned_cells>FB-l-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~83</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census; nothing is scheduled or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`list`, `describe`, `get`, `head`). No grant, no put. A denied read is a `not_read` entry.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL, "cannot read"); the grader rejects a write verb in `calls`, a claim outside the four, a candidate whose census scanned nothing (a zero with no denominator), a `first_zero_consumer` that is not a candidate with consumers 0 and scanned above 0, and an id-shaped token. Blindness: the grader proves shape and the zero-needs-a-denominator discipline, not that every consumer was found; the issuer re-reads the chosen candidate's census against the live plane before any retirement is ordered.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-l-3` (round 8, FWD-9(b): the retirement census; read-only)

Advisor Intelligence (the portal's advisor analytics) is moving from three legacy buckets to one spelled-out bucket per firm. The legacy buckets are `opal-data-bd` (the shared Black Diamond data lake), `opal-data-inf` (Inflection) and `opal-data-cot` (Cottonwood). A firm's destination is `opal-data-<firm>` in its long form; 49 Financial is DONE and is the model (`opal-data-49financial`, keys `advi/49financial/{gold|platinum|state}/...`). Inflection and Cottonwood are next. The read-only inventories of everything that runs against the old homes already exist (round 7, workstream PLANINV). Your job is a written PLAN built from them and from LIVE reads. Writing a plan starts no move: you change nothing in AWS and nothing in the repository outside your own deliverables folder.

### 1a. Your slice

Run the CONSUMER CENSUS of the legacy operations the move would make unnecessary, to find the first one with NO live consumer. The candidates are the rows of
`PLANINV_LEGACY_OPERATIONS.json` (16 candidates, round 7) plus three named here: the `mockadv` alias (Andrew's recommendation is RETIRE it once a census reads zero live use; a census
found 255 repository files carrying the token, most under `org/`, live use unread), `inf-canonical-prices-daily` (disabled and held), and `FIRMSEP-s3-direct-access-bypass`. For EACH candidate,
read LIVE and print the denominator beside the count:
1. Consumers in AWS: Lambda environment variables and event-source mappings, EventBridge rule targets and Scheduler targets, S3 bucket notifications, API Gateway and CloudFront
   origins and behaviours, IAM policies naming it, SNS subscriptions. Use `comp-find --corpus aws` first, then live reads of the resources it names.
2. Consumers in the repository: files that import, call or name it, grouped as production code, tests, docs/records. Production code means a path a deployed artifact is built from.
3. For `mockadv`: also the portal's user rows, the dropdown entry, the two router map entries and the registry rows (read the files; do not read any user's data).
A candidate has `consumers` = the count of LIVE consumers (a test fixture or a record that merely mentions it is not a consumer; list those separately in its `consumer_census.notes`).
`first_zero_consumer` is the id of the first candidate (in the file's order) whose `consumers` is 0 with `scanned` above 0; null with a `none_reason` if there is none. A zero
with no denominator is not a zero: the grader rejects it.

Inputs (read first): `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/PLANINV_LEGACY_OPERATIONS.json` (the 16 candidates, with their evidence and decision owners) and its `.md`.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~83/RETIRE_CENSUS.json`

```json
{"order": "FB-l-3", "read_at": "<ISO UTC>", "calls": ["aws lambda list-functions ...", "..."],
 "denominators": {"<what was scanned>": 0},
 "candidates": [
  {"id": "C1", "operation": "<name>", "source": "<FB-k-5 row id or 'named in this order'>",
   "consumer_census": {"scanned": 0, "consumers": 0, "claim": "measured|inferred|held|absent", "notes": "<non-consumer mentions listed here>"},
   "replaced_by": "<what replaces it, or 'nothing'>", "decision_owner": "Andrew|CTO|COO|none", "rollback_if_retired": "<the exact step that restores it>",
   "evidence": "<the calls or files>", "claim": "measured|inferred|held|absent"}],
 "first_zero_consumer": "<candidate id or null>", "none_reason": "<only when null>",
 "not_read": ["<each thing you could not read, and why>"], "claim": "measured"}
```

Also write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~83/RETIRE_CENSUS.md` (one page: the table of candidates with consumers and denominators, the first zero-consumer case and why it is first, the `not_read` list).

## 2. BOUNDS

1. READ verbs only, on AWS and on the repository. No write, no producer run, no deploy, no product file edited, no `terraform` command. AWS from bash is `.tools/aws`.
   Downloaded files go to `C:/dev/wk-firmbkts-83-data/` (outside the checkout).
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
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~83/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~83/ADVI_FIRMBKTS.TO-FB-l-3.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-l-3"><invocation>cd C:/dev/wk-firmbkts-83 &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py census --file C:/dev/wk-firmbkts-83/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~83/RETIRE_CENSUS.json --min 10</invocation><expect>^CENSUS: OK candidates=[0-9]+ zero=[0-9]+ first=.+$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-l-3"><invocation>cd C:/dev/wk-firmbkts-83 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root C:/dev/wk-firmbkts-83 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~83/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and the zero-needs-a-denominator discipline; AC2 is the write-surface bound. Completeness is read by the issuer from the denominators and a sample re-read.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~83/ADVI_FIRMBKTS.TO-FB-l-3.proof_of_spec.json`. Commit the two record files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W83-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`.
Report once: the candidate count, how many have zero consumers, the first zero-consumer case, the denominators, what you could not read, AC1 and AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 8, cell 3 of 3 read-only cells (CTO round-7 analysis, msg 5482, section 3 item 2: "the first legacy operation the plan finds with NO live consumer (read live, with the consumer census printed)"; never the Door 6 marker before the publisher moves). This census feeds `FB-l-4`, the retirement act, which waits on it, the CTO's naming of the case, and a signed pair. Class LOCAL.

<status>pending</status>
<round>8</round>
<workstream>RETIREMENT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-l-3</to_id>
<slot>~83</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
