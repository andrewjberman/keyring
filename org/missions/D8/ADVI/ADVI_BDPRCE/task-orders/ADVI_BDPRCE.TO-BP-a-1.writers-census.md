# ADVI_BDPRCE task order -- `BP-a-1` -- WHO WRITES THE SERVED 49F T-1 PRICE (READ-ONLY CENSUS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP.md</decomp_doc>
<owned_cells>BP-a-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~1</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; a read-only census adds and changes no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api list-object-versions`/`list-objects-v2`/`head-object`/`get-object`; `logs`, `events` and `lambda get-*`/`list-*` reads; `cloudtrail get-event-selectors`/`lookup-events`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a write verb in `calls`, a missing denominator, a missing canonical row and a claim outside the closed set (14-arm self-test OK). Blindness: the grader proves shape and read-only discipline, not that a writer is correctly named; the issuer re-reads the cited versions.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-a-1` (round 1; read-only)

Black Diamond prices for the 49 Financial firm are written to S3 by more than one program. The project's first outcome needs the COMPLETE list of writers of the served T-1 price, and
today three are known and one is not identified: the silver script `data/black_diamond/scripts/silver/bd_price_update.py` (writes at :609 and :639), the Lambda twin
`infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py` (writes at :441), the emergency rebuild `data/black_diamond/scripts/gold/build_canonical_prices_v2.py` (writes at :660),
and a fourth writer that rewrites `canonical_prices.parquet` about four times a day and has not been identified. You name every writer, and for each the copy of the pricing rule it applies. You change nothing.

Facts already read (re-verify, do not trust): `s3://opal-data-bd/silver/prices/canonical_prices.parquet` is versioned; today (2026-10-13 UTC) it has versions at 00:15:27Z (105,292,662 bytes),
04:03:26Z (109,605,884) and 04:03:42Z (109,972,952), 09:49:32Z and 09:49:48Z, 12:47:50Z and 12:48:05Z: paired writes about 15 seconds apart. The pricing rule lives in `bd_price_update.py`:
`SOURCE_RANK` at :65-71, `extract_t1_prices` at :327-344, `upsert_canonical` at :587-602.

### 1a. What to read (every AWS call a READ verb; use the `.tools/aws` shim from bash)

1. **Versions.** `list-object-versions` for `silver/prices/canonical_prices.parquet` and for the daily objects `silver/prices/<day>.parquet` of the last 7 days, in `opal-data-bd`. Record VersionId,
   LastModified, Size and `IsLatest` for each. Print the count read: it is the denominator `object_versions_read`.
2. **Where the same keys live in the served 49F home.** The 49 Financial served home is `opal-data-49financial` (prefixes `advi/`, `gold/`, `irpt/`, `mdpf/`). Determine whether either price object
   (or a copy) is written there too, and by what. If not, say so with the listing that shows it.
3. **Candidate writers, each with evidence.** For each of the four named writers: where it runs (Lambda function name, EC2/ECS runner, schedule or event rule), its last 7 days of runs
   (`logs filter-log-events` or `describe-log-streams` on its log group; `lambda get-function`; `events list-rules`/`describe-rule`/`list-targets-by-rule`), and which price object versions fall within
   one minute of one of its runs. Then look for writers not on the list: any other rule, schedule, Lambda or runner whose run time matches a version time in step 1 (read `events list-rules`,
   `lambda list-functions` names containing `price`, `canonical`, `bd-`, and the runner's scripts under `data/black_diamond/scripts/` that name `canonical_prices.parquet` or `silver/prices/`
   with the repo-search tool or the native Grep tool).
4. **The rule copy per writer.** For each writer, name the file and line of the `SOURCE_RANK` and of the median it applies, or `unknown`. A writer that imports `bd_price_update` shares its copy;
   a writer with its own literal copy is a second copy.
5. **The pairs.** Explain the 15-second pairs (two puts of one run? two writers? a put then a rewrite?) from the evidence, or write `unexplained`.

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~1/WRITERS.json`

```json
{"order": "BP-a-1", "read_at": "<ISO UTC>", "claim": "measured",
 "calls": ["aws s3api list-object-versions ...", "..."],
 "object_versions_read": 0,
 "writers": [
  {"writer_id": "<lambda:name | script:path | runner:name | unidentified-N>", "bucket": "opal-data-bd",
   "object_key": "silver/prices/canonical_prices.parquet", "runs_last_7d": 0,
   "evidence": "<the versions and the runs that match, by id and time>",
   "rule_copy": "<file:line of SOURCE_RANK and of the median, or unknown>", "claim": "measured | inferred | held | absent"}],
 "unidentified": ["<a version time no known writer's run matches, by VersionId>"],
 "pairs_explained": "<one paragraph, or unexplained>",
 "served_home_note": "<what is in opal-data-49financial>"}
```

One `writers` row per (writer, object key). The record MUST have a row whose `object_key` contains `canonical_prices.parquet` and a row whose `object_key` contains `silver/prices/`.
`claim` per row is `measured` only when a run and a version time match by id; `inferred` when matched by time only; `absent` when nothing was read. `unidentified` is a list (empty when none).
Also write `WRITERS.md` (one page: the table, the pairs, what stays unidentified and what read would close it).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no invoke, no producer run, no product file edited. Downloaded files go to `C:/dev/wk-bdprce-r1-1-data/` (outside the checkout).
2. No client name, account number or advisor name is printed anywhere.
3. A raw S3 listing the repo's rail denies is re-run with a trailing `# rail-checked: BP-a-1 census needs the version listing`. A read that cannot finish reports partial counts and `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~1/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~1/ADVI_BDPRCE.TO-BP-a-1.writers-census.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-a-1"><invocation>cd /c/dev/wk-bdprce-r1-1 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round1/checks/r1_checks.py writers --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~1/WRITERS.json</invocation><expect>^WRITERS record ok writers=[0-9]+ unidentified=[0-9]+ versions_read=[0-9]+$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-a-1"><invocation>cd /c/dev/wk-bdprce-r1-1 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r1-1 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~1/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The census's truth is read by the issuer from the cited versions.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit `WRITERS.json` and `WRITERS.md` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_BDPRCE-W1-S<k>`, `k` from 1,
`surfaced_at` from `date -u +%FT%TZ`. Report once: the writer list (id, object, rule copy), the unidentified versions, the pair explanation, AC1 and AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PRD cell C5 (census half), DEC-8 (the fourth writer is identified before FWD-2; its identity also bears on the 603-of-1,610 gap). Read-only; class LOCAL. The build half of C5 (the one rule's home) is an enrichment item.

<status>complete</status>
<round>1</round>
<workstream>WRITERS</workstream>
<to_id>ADVI_BDPRCE.TO-BP-a-1</to_id>
<slot>~1</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
