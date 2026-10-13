# ADVI_FIRMBKTS task order -- `FB-k-5` -- PLAN INVENTORY (READ-ONLY): THE LEGACY OPERATIONS THE MOVE WOULD MAKE UNNECESSARY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_PLANINV.md</decomp_doc>
<owned_cells>FB-k-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~80</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only inventory; nothing is scheduled or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only. A denied read is a `not_read` entry.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a write verb in `calls`, a claim or decision owner outside the closed sets, a row with no evidence, fewer than four candidates, an id-shaped token, and a record that omits any of the four named operations. Blindness: shape and discipline only; the issuer judges whether each candidate is real from the evidence it cites.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-k-5` (workstream PLANINV; read-only)

When Advisor Intelligence has moved to its spelled-out firm buckets, some operations that exist only to serve the old homes become unnecessary: a rule, a schedule, a Lambda, a grant, a script.
The PRD's FWD-9 asks that each is retired by a RECORDED decision naming what replaced it, or that nothing did. You list the CANDIDATES with their evidence. You decide nothing and change nothing.

Facts: legacy buckets `opal-data-bd`, `opal-data-inf`, `opal-data-cot`. `opal-data-inf/gold/meta/pipeline-complete.json` is a prohibited key ("Door 6"), watched by the `mdpf-feeder-accelerator` rule;
Andrew has ruled it RETIRE with no successor marker, inside the Inflection move after a no-other-consumer read. `opal-data-inf/orion/jwt/current.json` (B2) is a live credential that STAYS (never read its contents).
`inf-canonical-prices-daily` is disabled and held. `FIRMSEP-s3-direct-access-bypass` is a named exposure whose fate the PRD does not rule. `opal-cot-value-parity` is a Cottonwood reader of a legacy bucket.
Another worker inventories what runs against each firm's home; you list only what the move would make unnecessary.

### 1a. What to do

1. For EACH of the four named operations (`FIRMSEP-s3-direct-access-bypass`, `inf-canonical-prices-daily`, `mdpf-feeder-accelerator`, `opal-cot-value-parity`): find it (live graph and repository), read its definition, state what it exists for, what it reads or
   writes in a legacy home, who else consumes its output or the key it watches (a no-other-consumer read: name the search you ran and its denominator), what would replace it after the move (`replaced_by`: a named
   thing, or the word `nothing`) with a claim, and who must decide (`decision_owner`: `Andrew`, `CTO`, `COO` or `none`).
2. Then search for ANY further candidate: a rule, schedule, Lambda, IAM grant or script whose only inputs or targets are a legacy home and that has no use once the firm buckets serve (for example a legacy-prefix
   publisher, a `state/` or `code/` sync to a legacy home, a legacy alarm that only watches a legacy home). Add each with its evidence. A candidate you suspect but cannot show is `claim: inferred` or `held`.
3. Record at least four candidates (the four above are the floor).

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/PLANINV_LEGACY_OPERATIONS.json`

```json
{"order": "FB-k-5", "read_at": "<ISO UTC>", "calls": ["..."], "denominators": {"<what was scanned>": 0},
 "candidates": [
  {"id": "<short stable id>", "kind": "rule|schedule|task|service|lambda|edge|topic|email|script|role|reader|other", "name": "<exact resource name or file path>",
   "legacy_reason": "<why the move makes it unnecessary, one sentence>", "replaced_by": "<named replacement, or nothing>", "replaced_by_claim": "measured|inferred|held|absent",
   "decision_owner": "Andrew|CTO|COO|none", "other_consumers": "<names found by the no-other-consumer read, or none found with the search named>",
   "evidence": "<the call or file:line>", "claim": "measured|inferred|held|absent"}],
 "not_read": ["<each thing you could not read, and why>"], "claim": "measured"}
```
Also write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/PLANINV_LEGACY_OPERATIONS.md` (one page: a table of the candidates with owner and replacement).

## 2. BOUNDS

1. READ verbs only, on AWS and on the repository. No write, no producer run, no deploy, no product file edited, no `terraform` command. AWS from bash is `.tools/aws`.
   Downloaded files go to `C:/dev/wk-firmbkts-80-data/` (outside the checkout).
2. Read AWS through the served graph first: `comp-find --corpus aws '<regex>'` lists CloudNodes with a printed denominator; then ONE live `describe`/`get`/`list` of one
   resource per call. The repository is searched with the Grep and Glob tools or `comp-find` (a recursive shell grep is denied by the rail; the denial prints the command to run next).
3. Print NO secret and no credential. For a Lambda environment record the variable NAMES, and a value only when it is a bucket, region, table or queue name. Print no client name, no account
   number and no relationship id: where a key or text holds one, write `<id>` in its place (the grader rejects any token of nine or more digits except the AWS account number 313476888478).
4. Every row carries its claim in a field a consumer can reject on: `measured` (you read it live or in the file at a stated line), `inferred`, `held`, `absent`. A thing you could not read is a
   `not_read` entry and `claim: absent`, never a guess and never a silent omission. Print the DENOMINATOR of every sweep (rules, schedules, functions, files scanned) in `denominators`.
5. Each AWS call is bounded (`timeout 100`); a sweep too large to finish is reported as partial counts, not left running.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/ADVI_FIRMBKTS.TO-FB-k-5.legacy-operations-retire.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-k-5"><invocation>cd C:/dev/wk-firmbkts-80 &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py planinv --shape retire --min 4 --file C:/dev/wk-firmbkts-80/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/PLANINV_LEGACY_OPERATIONS.json --require-text FIRMSEP-s3-direct-access-bypass inf-canonical-prices-daily mdpf-feeder-accelerator opal-cot-value-parity</invocation><expect>^PLANINV: OK shape=retire rows=[0-9]+$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-k-5"><invocation>cd C:/dev/wk-firmbkts-80 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root C:/dev/wk-firmbkts-80 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline and that the four named operations appear; AC2 is the write-surface bound. Whether each candidate is real is read by the issuer from its evidence.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/ADVI_FIRMBKTS.TO-FB-k-5.legacy-operations-retire.proof_of_spec.json`. Commit the scripts and the two record files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W80-S<k>`, `k` from 1,
`surfaced_at` from `date -u +%FT%TZ`. Report once: the candidate count, which are Andrew's to decide, the denominators, what you could not read, AC1 and AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's word (msg 5215) and Andrew's DEC-12/13/14 answers (msg 5128): Door 6 RETIRE with its rule after a no-other-consumer read; DEC-14 `mockadv` is a census, not this cell's. Class LOCAL.

<status>pending</status>
<round>7</round>
<workstream>PLANINV</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-k-5</to_id>
<slot>~80</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
