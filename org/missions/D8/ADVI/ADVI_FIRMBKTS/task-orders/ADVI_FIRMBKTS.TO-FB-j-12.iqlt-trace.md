# ADVI_FIRMBKTS task order -- `FB-j-12` -- TRACE IQLT'S -69.2 PERCENT (A COST-BASIS OR PRICE DEFECT, OR A REAL LOSS?) BEFORE ANY SERVE (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~75</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only trace; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`/`head-object`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a write verb in `calls`, fewer than two price sources, a classification outside the closed set and a claim outside the four. Blindness: the grader proves shape and read-only discipline, not that the trace is right; the issuer re-reads the cited lots.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-j-12` (round 7; the CTO's reading of the sample, ruling (c); read-only)

In the ten-advisor dry run, advisor `garrett_newberry`'s `tax_loss_candidate` and `top_loser` bullets read IQLT as "down $302,321 (-69.2%)".
A 69 percent unrealized loss on a broad international equity ETF is implausible; the CTO suspects a cost-basis or price defect of the kind
the Black Diamond pricing findings (S32-S34) describe. Before any serve, you TRACE the number and classify it. You change nothing.

### 1a. What to read (every AWS call a READ verb; `.tools/aws` from bash; the worker's own scripts under your deliverables folder)

1. The bullet's figures: `DRYRUN10_FIGURES.json` in `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/`: the rows for `garrett_newberry` and ticker `IQLT`
   (market value, cost basis or unrealized loss, account count, percentage), and the objects its `evidence_keys` name
   (`platinum/advisors/garrett_newberry/positions.json` in the canonical home `opal-data-49financial`, key prefix
   `advi/49financial/`).
2. The lots behind it: the holdings-lots object the positions are built from (`gold/holdings_lots/...` in `opal-data-bd`, or the file
   `B_01.holdings_lots.py` writes: find it from the producer script), filtered to IQLT for that advisor's accounts: count of lots, total
   quantity, total cost basis, total market value, and the per-share cost and per-share price implied (cost basis over quantity; market
   value over quantity).
3. The price: the price the position was valued at (the `silver/prices/<date>.parquet` and `canonical_prices.parquet` rows for IQLT on the
   served date, as `B_01.holdings_lots.py` reads them) and AT LEAST ONE independent price for the same date: another price table of the
   estate (for example the per-date transactions' `calc_price` median for IQLT, or the custodian pricing in the silver tables), each with
   its source and as-of date.
4. The cost: for each lot, its acquisition date and per-share cost, against the security's own price history in the estate's price tables
   within five days of that date; flag lots whose per-share cost is more than 20 percent away from every price seen near the date.
5. Classify: `DATA_DEFECT` (the price used or the cost basis is inconsistent with the estate's other sources, naming which), `REAL_LOSS`
   (price and cost are consistent with other sources and the loss is real), or `NOT_DETERMINED` (say what could not be read).

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.json`

```json
{"order": "FB-j-12", "read_at": "<ISO UTC>", "calls": ["aws s3api get-object ...", "..."],
 "ticker": "IQLT", "advisor_id": "garrett_newberry", "accounts": 0, "lots": 0,
 "quantity": 0.0, "market_value": 0.0, "cost_basis": 0.0, "unrealized_loss": 0.0, "loss_pct": 0.0,
 "price_used": 0.0, "price_sources": [{"source": "<table or file>", "as_of": "YYYY-MM-DD", "price": 0.0}, {"source": "...", "as_of": "...", "price": 0.0}],
 "lots_cost_flagged": 0,
 "classification": "DATA_DEFECT | REAL_LOSS | NOT_DETERMINED", "reason": "<three sentences naming the source of the discrepancy, or why the loss is real>",
 "affected_scope": "<how many advisors' bullets rest on the same price or cost-basis input, if it is a defect>",
 "claim": "measured"}
```

Also write `IQLT_TRACE.md` (one page). `price_sources` names at least TWO sources (or one source and a statement of which could not be read).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited. Downloaded files go to `C:/dev/wk-firmbkts-75-data/` (outside the
   checkout). No client name, account number or advisor name beyond the advisor id the sample already names is printed.
2. A step that cannot finish reports partial counts and `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/ADVI_FIRMBKTS.TO-FB-j-12.iqlt-trace.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-12"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py iqlt --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.json</invocation><expect>^IQLT record ok classification=(DATA_DEFECT|REAL_LOSS|NOT_DETERMINED) loss_pct=-?[0-9.]+$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-j-12"><invocation>cd /c/dev/wk-firmbkts-75 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-75 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline; AC2 is the write-surface bound. The trace's truth is read by the issuer from the cited objects.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/ADVI_FIRMBKTS.TO-FB-j-12.iqlt-trace.proof_of_spec.json`. Commit the scripts and the two record files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W75-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the classification, the loss percentage, the two or more prices with their sources, the affected scope, AC1 and AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's ruling (c): "garrett_newberry's IQLT -69.2 pct is traced to its cost basis and price before serve; if it is a data defect, the affected bullets are held." If it is a defect in the pricing path, it joins the CRO's pricing brief (`FB-h-7`: S32-S34). Read-only; class LOCAL.

<status>pending</status>
<round>7</round>
<workstream>IQLTTRACE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-12</to_id>
<slot>~75</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
