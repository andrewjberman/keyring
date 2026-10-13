# ADVI_FIRMBKTS task order -- `FB-h-7` -- THE BLACK DIAMOND PRICING FINDINGS S32 TO S34, QUANTIFIED ON SERVED VALUES (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R5.md</decomp_doc>
<owned_cells>FB-h-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~66</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only quantification; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`/`head-object`, `cloudwatch get-metric-statistics`, `logs filter-log-events`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a recommendation that disagrees with the counts (a planted NOT_MATERIAL over a non-zero count reads FAIL), a writer list that is empty, a reader list that is not the three named readers, and a write verb in `calls`. Blindness: the grader proves shape and the CTO's rule, not that the counts are right; the issuer re-reads a sample of cited objects.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-h-7` (round 5, enrichment item 5; rows `D1-S32`, `D1-S33`, `D1-S34`)

Three findings on the Black Diamond pricing path of the 49 Financial pipeline (bucket `opal-data-bd`) say a served price or
figure may be decided by a rule nobody chose. None has been QUANTIFIED. You quantify each on SERVED values, read-only: the
counts and the amounts that would change under the corrected rule, and the writer of each rule. If a count is non-zero the
CRO takes it to a brief; if zero the row closes as not material. You change nothing and you publish nothing.

### 1a. S32 -- the T-1 median is weighted by portfolio-group repeats

`data/black_diamond/scripts/gold/bd_price_update.py` takes (line 344) the median of `calc_price` per `asset_name` over
`silver/transactions/<date>.parquet` rows that repeat once per portfolio group; the per-date loader (lines 263-271) does not
de-duplicate by `transaction_id`. Read the code first. Then, for the **20 most recent trading days that have a
`silver/transactions/<date>.parquet` object** (print the dates), compute per asset the median (a) as the code does and
(b) after de-duplicating rows by `transaction_id` (first occurrence), and report: `asset_days_considered`,
`asset_days_median_changes` (days where (a) differs from (b) by more than 0.000001), `assets_affected` (distinct assets),
`max_abs_price_delta`, and, where the served holdings quantity is readable
(`gold/holdings_lots` or the file `B_01.holdings_lots.py` writes), `sum_abs_price_delta_x_qty` for the latest day (else `null`).
`writers`: the script(s) that WRITE the served price (name file and line).

### 1b. S33 -- an unstable sort decides the same-date price tie

`data/black_diamond/scripts/gold/B_01.holdings_lots.py` lines 331-361 concatenates `silver/prices/<date>.parquet` files then
`canonical_prices.parquet`, `sort_values('date')` with the default (unstable) kind and `drop_duplicates('asset_name', keep='first')`.
For the date **2026-10-09**: replicate the price load read-only, find the assets with a same-date tie (a price row in the
daily file and one in `canonical_prices.parquet` for that date), and report `tied_assets`, `winner_in_daily_file` and
`winner_in_canonical_prices` (which object the code's order selects, with the same pandas version the code runs; say the
version), `alternative_differs` (assets whose OTHER candidate price differs from the winner), `max_abs_price_delta`.
`canonical_prices_writers`: the writer(s) of `canonical_prices.parquet` (it is rewritten four times a day), named by file
and line, or the string `unidentified` with the method you used (grep of the repository; CloudTrail data events are not
available; S3 `LastModified` times of the object's versions).

### 1c. S34 -- three served readers key on the file day, not `trade_date`

Readers: `B_03.account_gains.py` (line 327), `bd_price_update.py` (line 265) and its Lambda twin (line 143 of the file
that implements the Lambda; find it). The late-August rewrites moved 5,580 transaction ids one file each toward their trade
date. Report: for each reader, whether it RAN since 2026-09-02 (`reran_since_20260902`: true, false or null with the evidence:
S3 `LastModified` of the object it writes, a CloudWatch Lambda `Invocations` count, the chain's run log, whichever you can read);
and for the served objects that cover the trade dates 2026-08-20 to 2026-08-23 (list them by key prefix; `objects_compared`),
how many have a version written after 2026-09-02 whose content differs from the first version written after 2026-08-23
(`changed`) -- `list-object-versions` then `get-object --version-id`, compare content hashes. If a bucket has no versioning,
say so (`claim: absent`) and report what the object timestamps allow.

### 1d. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.json`

Every value carries its claim (`measured`, `inferred`, `held`, `absent`; a claim of `absent` states why). Keys exactly:

```json
{"order": "FB-h-7", "read_at": "<ISO UTC>", "calls": ["aws s3api list-objects-v2 ...", "..."],
 "s32": {"window": {"from": "YYYY-MM-DD", "to": "YYYY-MM-DD", "days": 20}, "asset_days_considered": 0,
         "asset_days_median_changes": 0, "assets_affected": 0, "max_abs_price_delta": 0.0,
         "sum_abs_price_delta_x_qty": null, "writers": ["<file>:<line>"], "claim": "measured"},
 "s33": {"date": "2026-10-09", "tied_assets": 0, "winner_in_daily_file": 0, "winner_in_canonical_prices": 0,
         "alternative_differs": 0, "max_abs_price_delta": 0.0, "canonical_prices_writers": ["<file>:<line>"], "claim": "measured"},
 "s34": {"readers": [{"reader": "B_03.account_gains.py", "reran_since_20260902": null, "evidence": "...", "claim": "absent"},
                     {"reader": "bd_price_update.py", "reran_since_20260902": null, "evidence": "...", "claim": "absent"},
                     {"reader": "<the Lambda twin's file>", "reran_since_20260902": null, "evidence": "...", "claim": "absent"}],
         "served_0820_0823": {"objects_compared": 0, "changed": 0, "claim": "measured"}},
 "recommendation": "BRIEF_TO_CRO | NOT_MATERIAL",
 "recommendation_reason": "<two sentences>"}
```

The recommendation is `BRIEF_TO_CRO` if `asset_days_median_changes`, `alternative_differs` or `served_0820_0823.changed` is
greater than zero, `NOT_MATERIAL` if all three are zero; the grader enforces it. `calls` lists every AWS call you made,
one string each, beginning `aws <service> <read-verb>`. Also write `PRICING_QUANT.md` (one page, prose) in the same folder.

## 2. BOUNDS

1. READ verbs only on AWS (get, list, head, describe, filter, lookup). No put, no delete, no copy, no invoke. No product
   file is edited; no run of a producer script (you replicate its READ logic in your own script under your deliverables folder).
2. Keep your scripts in `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/` (they are the evidence). Downloaded parquet files go to `C:/dev/wk-firmbkts-66-data/`
   (outside the checkout), never into the tree.
3. A step that cannot finish in time is reported with the partial counts and `claim: absent` for what was not read; do not
   estimate a count from a sample without saying so (`claim: inferred`, the sample size stated).
4. Dollar and price figures are reported as numbers in the record; no client name, account number or advisor id is printed.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/ADVI_FIRMBKTS.TO-FB-h-7.bd-pricing-quantification.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-h-7"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_checks.py quant --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.json</invocation><expect>^QUANT keys ok calls=[0-9]+ recommendation=(BRIEF_TO_CRO|NOT_MATERIAL)$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-h-7"><invocation>cd /c/dev/wk-firmbkts-66 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-66 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, its denominators and the recommendation rule; AC2 is the write-surface bound. The counts' truth is read by the issuer from the worker's scripts and cited objects.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/ADVI_FIRMBKTS.TO-FB-h-7.bd-pricing-quantification.proof_of_spec.json`. Commit the scripts and the two record files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W66-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the three headline counts with their denominators, the writers named, the recommendation, AC1 and AC2 outputs and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-4 analysis section 2 (D1-S32, S33, S34): real correctness findings on a pipeline FIRMBKTS moved, not defined; no active project owns its pricing rules. ONE read-only cell quantifies each on served values; non-zero goes to the CRO for a brief under its own project, zero closes the rows as not material. Class LOCAL (reads). The heaviest cell of the round: a partial result with `absent` claims is acceptable and is reported as such; the issuer does not recut a read that the data does not support.

<status>pending</status>
<round>5</round>
<workstream>BDPRICE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-h-7</to_id>
<slot>~66</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
