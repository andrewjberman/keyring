# ADVI_BDPRCE task order -- `BP-b-8` -- FWD-1'S THREAD ON A TRULY UNLISTED HOLDING, TRACED TO R1 AND ITS DISTINCT TRADES (JOIN, STAGED, READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R2.md</decomp_doc>
<owned_cells>BP-b-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~12</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only trace; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`head-object`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a raw account id or a name, a served ticker, a rule id other than R1, distinct trade ids that disagree with the list, fewer than three ticker sources checked, a catch-all client entity and a record that does not claim one served price (33-arm self-test OK). Blindness: the grader proves shape and PII discipline, not that the holding is truly unlisted; the issuer re-opens the object and re-checks the sources.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-b-8` (round 2; the join; read-only)

The project's first outcome, again: on the served T-1 object, someone opens ONE 49 Financial client account holding ONE security that has no public ticker, reads its served price, and from the record alone names
the rule that produced it and the trades (by trade id) behind it, and the price recomputed from those trades equals the served price. Round 1's exemplar was rejected as not truly unlisted (a listed common stock with a
null served ticker: row `W4-S9`) and its tie unruled (`W4-S5`). You re-draw it on a holding that has no ticker in ANY source, and trace it to the ruled rule R1.

R1 (CTO ruling, `org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md`): median of DISTINCT trades (each `transaction_id` once), trades only at the executed `price` column, every non-trade row
excluded, ties by `SOURCE_RANK` then a stable sort, no trade on the date -> the last observed price carried WITH its observation date; interpolation banned.

Three earlier cells are merged into your worktree (read them first):
- `data/black_diamond/scripts/silver/bd_price_rule.py` with `tests/test_bd_price_rule.py` and `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.md`: R1 as a module. Import it; do not reimplement it.
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~7/CENSUS.json`, `CENSUS.md` and the extract `C:/dev/wk-bdprce-r2-7-data/lot_extract.csv` (check its sha256 against `extract_sha256`; a mismatch is a BLOCKING row and you stop):
  every lot of every client object, with its price class and the list of listed-but-untickered assets.
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~8/trace_price_v2.py` (with `TRACE2_README.md`): the trace that follows the served row. Run it; do not rewrite it.

### 1a. What to do

1. **Candidates.** From the extract: untickered lots (served `ticker` null, empty or `UNKNOWN`) in a client object whose entity class is NOT the catch-all `0`, whose asset is NOT in the census's `listed_untickered` list,
   whose class is `PRICED_FROM_CANONICAL`, and whose asset carries ONE `current_price` across all its lots in that object. State how many candidates fall away at each condition.
2. **Truly unlisted.** For each finalist, check at least THREE sources for a ticker and record each by name and result: the served ticker; `config/ticker_lookup.json` (`opal-data-bd`); the `ticker` column of
   `canonical_prices.parquet` for the asset across all dates; `silver/historical_prices.parquet` (ticker set); the constant tables `YF_OVERRIDES`, `OPAL_ETF_OVERRIDES`, `TICKER_CORRECTIONS` in
   `data/black_diamond/scripts/silver/bd_price_update.py`; and the assets dimension (find it from `build_bd_assets_dim.py`). The asset is truly unlisted only if NONE of them gives a ticker. A security that is a private
   fund, a structured note, a model sleeve or a similar instrument is the natural exemplar; say which kind it is, from the asset's name and the dimension, without guessing.
3. **Trace to R1.** For the chosen (asset, date = the object's `data_as_of`): run the module `price_for_date` (variant A) over the day's trades (`silver/transactions/<date>.parquet` rows with that `trade_date`, which
   may sit in the next day's partition: read both) and take `recomputed_price` and the DISTINCT `transaction_id`s. Run `trace_price_v2.py` with the lot's `current_price` as the served price; record what it
   followed (canonical or daily), and where a same-date tie exists, state how R1's tie order (`SOURCE_RANK`, then a stable sort) decides it and whether that agrees with the row the lot read.
   If the day has no trade for the asset, take the carry-forward shape: the recompute is the last observed R1 price on `observation_date`, and `recompute_equals_served` compares that price with the served one.
4. **One price.** Show that every lot of the asset in that object carries the same `current_price`.
5. **Do not choose dishonestly.** If no candidate passes, report the counts at each condition and file a BLOCKING row; never relax a condition. If the module is absent from your tree, stop and file a BLOCKING row.

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/THREAD2.json`

```json
{"order": "BP-b-8", "read_at": "<ISO UTC>", "claim": "measured",
 "served_object_key": "<bucket>/<key>@<VersionId>", "as_of_date": "YYYY-MM-DD",
 "account_ref": "<first 12 hex of sha256(str(account_id))>", "asset_name": "<name>", "ticker": null,
 "kind": "<private fund | structured note | model sleeve | other, with the evidence>",
 "served_price": 0.0, "rule_id": "R1", "trade_ids": ["<transaction_id>", "..."], "distinct_trade_ids": 0,
 "recomputed_price": 0.0, "recompute_equals_served": true, "carry_observation_date": null,
 "tie_order_applied": "<what R1's order decided, or none needed>",
 "unlisted_sources_checked": [{"source": "<name>", "result": "<no ticker | n/a>"}],
 "client_entity_class": "normal", "one_served_price": true,
 "candidates_considered": {"start": 0, "after_entity": 0, "after_listed": 0, "after_class": 0, "after_one_price": 0},
 "writer": "<writer id from WRITERS.json, or unidentified>",
 "instrument": "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~8/trace_price_v2.py"}
```
`unlisted_sources_checked` is a list (the grader needs at least three entries). `distinct_trade_ids` is the count of distinct ids in `trade_ids`. Never write the raw `account_id`, a client name or an advisor name anywhere.
Also write `THREAD2.md` (one page an analyst can read: the served price, R1 in plain words, the trades, the recompute, why the holding is unlisted, the tie, and the three commands that reproduce it).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited (the module is imported, not changed). Downloaded files go to `C:/dev/wk-bdprce-r2-12-data/` (outside the checkout).
2. No client name, account number or advisor name is printed anywhere; do not print raw lists of client or account keys; count them.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-b-8 thread needs the listing`. A step that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/ADVI_BDPRCE.TO-BP-b-8.thread-unlisted.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-b-8"><invocation>cd /c/dev/wk-bdprce-r2-12 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py thread2 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/THREAD2.json</invocation><expect>^THREAD2 record ok rule=R1 distinct_trades=[1-9][0-9]* sources_checked=[0-9]+ equal=true$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-b-8"><invocation>cd /c/dev/wk-bdprce-r2-12 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r2-12 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~12/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, PII discipline, the sources checked and that the recompute equals the served price; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). That the row is real and unlisted is read by the issuer from the cited object and sources.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit `THREAD2.json`, `THREAD2.md` and your trace outputs FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W12-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the served object key, date, asset (name) and kind, served price, rule, distinct trade count, recompute and equality,
the sources checked, the tie, candidate counts at each condition, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 analysis item 3; closes `W4-S9` and the tie of `W4-S5` for the exemplar; FWD-1's grade is the CTO's on the issuer's re-open. STAGED at the cut: un-parks when `BP-b-1`, `BP-b-3` and `BP-b-4` are merged and PASS; its worktree is cut from that HEAD.
The module is imported by a read-only order: nothing is deployed and no writer imports it.

<status>staged</status>
<round>2</round>
<workstream>THREAD2</workstream>
<to_id>ADVI_BDPRCE.TO-BP-b-8</to_id>
<slot>~12</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
