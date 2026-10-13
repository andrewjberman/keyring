# ADVI_BDPRCE task order -- `BP-a-3` -- THE 603-OF-1,610 GAP: EXPLAINED OR BOUNDED, WITH ITS DENOMINATOR (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP.md</decomp_doc>
<owned_cells>BP-a-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~3</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; a read-only measurement adds and changes no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`/`head-object`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a write verb in `calls`, a class partition whose sum differs from the denominator, an open class set, an empty bound statement and a claim outside the closed set (14-arm self-test OK). Blindness: the grader proves arithmetic and shape, not that a row sits in the right class; the issuer re-reads a sample of rows of each explained class.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-a-3` (round 1; read-only)

Black Diamond's price for an asset with no public ticker is the MEDIAN of that day's trades (`source == transaction_observed`). A measurement on 2026-10-13 found that of 1,610 such served rows over 20
weekday partitions (2026-09-16 to 2026-10-13), 1,007 equal what today's file recomputes and 603 do not. The cause is not isolated. Candidate causes the measurer named: a multi-day backfill, or the
file's state at the time the price was written. A price trace that cannot reproduce what was served cannot answer "where did this price come from?", so you classify EVERY such row and bound what stays unexplained.
You change nothing.

### 1a. The rule and the objects (read these lines)

- `data/black_diamond/scripts/silver/bd_price_update.py`: `load_transactions_for_date` :263-271 (reads `silver/transactions/<YYYY-MM-DD>.parquet`; no de-duplication); `extract_t1_prices` :327-344
  (valid rows: `asset_name` not null, `units` not null and abs > 1e-8, `market_value` not null and != 0; `calc_price = |market_value|/|units|`; keep 0 < calc_price < 100000; median per `asset_name` over ALL rows).
- Bucket `opal-data-bd`. Served prices: `silver/prices/canonical_prices.parquet` (date, asset_name, ticker, price, source) and the daily `silver/prices/<date>.parquet`. Both are VERSIONED, and so is
  `silver/transactions/<date>.parquet`.
- The earlier measurement's replica scripts (read them, copy what you need into your folder, never edit them):
  `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/pricing_quant_s32_s33.py`, `.../pricing_quant_s34.py`, `.../PRICING_QUANT.md`.

### 1b. The measurement

1. **Window and denominator.** The window is the 20 weekday dates ending at the newest `silver/prices/<date>.parquet`. Read the served `transaction_observed` rows of those dates from
   `canonical_prices.parquet`. Print `served_rows` (the denominator). If it is not 1,610, say what changed (a window shift is expected); do not force it.
2. **Recompute.** For each (date, asset_name), apply the rule to the CURRENT version of that day's transactions partition. Equal within `1e-6 * max(1, |served|)` -> `EQUAL`.
3. **Explain each difference, in this order; the first that reproduces the served price within the same tolerance takes the row:**
   a. `EXPLAINED_BY_VERSION_AT_WRITE` -- the version of that day's partition that was current when the price was written reproduces the served price. The write time of the served row is the
      LastModified of the first version of `silver/prices/<date>.parquet` (or of the canonical object version that first carries the row) at or after which the row is present; state which you used.
   b. `EXPLAINED_BY_MULTIDAY_WINDOW` -- the rule applied to the concatenated partitions of a window of several days (a backfill window) reproduces it. State the window.
   c. `EXPLAINED_OTHER` -- any other cause you can show reproduces the served price. Name it in `other_causes` (a list of `{cause, rows, evidence}`).
   d. `UNEXPLAINED` -- none reproduces it. `NOT_RECOMPUTABLE` -- the day's partition is absent or holds no valid row for the asset.
4. **Bound.** `bound_statement` is one or two sentences stating how many rows stay UNEXPLAINED and what the largest absolute and relative differences among them are. If none stays unexplained, say so.

### 1c. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/GAP.json`

```json
{"order": "BP-a-3", "read_at": "<ISO UTC>", "claim": "measured",
 "calls": ["aws s3api list-object-versions ...", "..."],
 "window": "YYYY-MM-DD..YYYY-MM-DD (n weekday dates)",
 "served_rows": 0,
 "classes": {"EQUAL": 0, "EXPLAINED_BY_VERSION_AT_WRITE": 0, "EXPLAINED_BY_MULTIDAY_WINDOW": 0,
             "EXPLAINED_OTHER": 0, "UNEXPLAINED": 0, "NOT_RECOMPUTABLE": 0},
 "other_causes": [], "bound_statement": "<...>",
 "largest_unexplained": [{"date": "YYYY-MM-DD", "asset_name": "<name>", "served": 0.0, "recomputed": 0.0}],
 "rows_file": "GAP_ROWS.csv"}
```

The six class keys are exactly those (a closed set); their sum MUST equal `served_rows`. `GAP_ROWS.csv` holds one line per served row: date, asset_name, served_price, recomputed_price, class, evidence_ref.
Also write `GAP.md` (one page: the table, the cause or causes, the bound, what read would close the residue).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited. Downloaded files go to `C:/dev/wk-bdprce-r1-3-data/` (outside the checkout); `GAP_ROWS.csv` is committed only if under 5 MB, otherwise its path and sha256 are named in `GAP.md`.
2. No client name, account number or advisor name is printed. An asset's name is not one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-a-3 measurement needs the version listing`. A step that cannot finish reports partial counts and `claim: absent`
   for what was not read; never a class assigned by guess.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/ADVI_BDPRCE.TO-BP-a-3.gap-603-of-1610.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-a-3"><invocation>cd /c/dev/wk-bdprce-r1-3 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round1/checks/r1_checks.py gap --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/GAP.json</invocation><expect>^GAP record ok served=[0-9]+ equal=[0-9]+ explained=[0-9]+ unexplained=[0-9]+$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-a-3"><invocation>cd /c/dev/wk-bdprce-r1-3 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r1-3 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, arithmetic and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The classification's truth is read by the issuer from sampled rows.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit your scripts, `GAP.json`, `GAP.md` and `GAP_ROWS.csv` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-W3-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the window, the denominator, the six class counts, the cause or causes with one example row each, the bound statement, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PRD cell C9 (gap half), DEC-8 third bullet (the gap is explained or bounded before FWD-1 and FWD-3), brief V.7. Read-only; class LOCAL. A residue that stays UNEXPLAINED is bounded and named at the drain; it does not block the thread's own row.

<status>pending</status>
<round>1</round>
<workstream>GAP</workstream>
<to_id>ADVI_BDPRCE.TO-BP-a-3</to_id>
<slot>~3</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
