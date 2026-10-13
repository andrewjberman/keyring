# ADVI_BDPRCE task order -- `BP-a-4` -- THE THREAD: ONE 49F ACCOUNT, ONE UNTICKERED HOLDING, ITS SERVED PRICE TRACED TO ITS RULE AND TRADES (JOIN, STAGED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP.md</decomp_doc>
<owned_cells>BP-a-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~4</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; a read-only trace adds and changes no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`head-object`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a raw account id or a name in the record, a tickered holding, an empty trade list and a claim outside the closed set (14-arm self-test OK). Blindness: the grader proves shape and PII discipline, not that the chosen row is the right one; the issuer re-opens the served object at the cited key and re-reads the row.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-a-4` (round 1; the join; read-only)

The project's first outcome, in one sentence: on the served T-1 object, someone opens ONE 49 Financial client account holding ONE security that has no public ticker, reads its served price, and from the record
alone names the rule that produced it and the trades (by trade id) behind it, and the price recomputed from those trades equals the served price. You produce that record for one real holding. You change nothing.

Three earlier cells of this round are merged into your worktree (read them first, in this order):
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~1/WRITERS.json` and `WRITERS.md`: who writes the served price objects, and the rule copy each applies.
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/trace_price.py` (with `TRACE_README.md`): the instrument. Run it; do not rewrite it.
- `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/GAP.json`, `GAP_ROWS.csv`, `GAP.md`: which served transaction_observed rows reproduce from their day's trades and which do not, and why.

### 1a. What to do

1. **Find the served T-1 object.** The 49 Financial served home is `opal-data-49financial` (prefixes `advi/49financial/gold/`, `advi/49financial/platinum/`, `gold/advi/`). Find, from the producer chain
   (`data/black_diamond/scripts/gold/B_01.holdings_lots.py` writes lots to `opal-data-bd`; read what carries the holdings, with a per-holding price and a date, into the served home and which object the portal
   reads at the default T-1 date), the one served object that lists a client account's holdings with a price per holding. Record its bucket, key and VersionId.
2. **Choose the holding.** One account, one holding with NO public ticker (the served object's `ticker` is null, empty or `UNKNOWN`, or the asset has no entry in `config/ticker_lookup.json` of `opal-data-bd`).
   Its served price at the served date has one of two shapes; take the first shape for which a candidate exists, and state the counts of both:
   a. **Direct:** the served price's source is `transaction_observed` at the served date and `GAP_ROWS.csv` classes that (date, asset) `EQUAL`.
   b. **Chain:** the served price's source is `carry_forward` or `linear_interpolation` at the served date, and its anchor (the most recent earlier row of that asset in `canonical_prices.parquet`/the
      daily files whose source is `transaction_observed`) is classed `EQUAL` in `GAP_ROWS.csv`, and the served price equals the anchor's price within `1e-6 * max(1, |price|)`. (The newest two daily
      price files carry no `transaction_observed` row, measured by worker ~2 in row `ADVI_BDPRCE-D1-W2-S1`, so shape b is expected to be the normal case at the served T-1 date.)
   State how many candidates there were of each shape and why you took this one (the first in file order that fits is enough).
   Two further conditions bind BOTH shapes (amendment 2, issuer; measured by the issuer on the first candidate, which sat in `entities/clients/0/detail.json`):
   c. **A normal client entity.** Take the holding from a client object whose `client_key` is NOT `0`: the entity `0` is a catch-all (its `client_name` reads as a bucket label, it holds 210 accounts and 3,052 open lots),
      not a client an advisor opens. Use an object under `advi/49financial/platinum/entities/clients/` keyed `acct_z...` or `z0...`. Name the entity's key class in the record as `client_entity_class: "normal"`.
   d. **One served price for the asset.** In the chosen client object, every open lot of that asset carries the SAME `current_price` on that object's `data_as_of`. Count the objects you try and how many fail this
      (the asset showing two prices at once is a finding: file a row naming the asset class, the two prices and the lot counts, never an asset or account name beyond the asset's name).
   Keep the first candidate in `THREAD_TRACE.md` as a rejected candidate with the reason (catch-all entity; two served prices for the asset in its object).
3. **Trace it.** Run `trace_price.py --asset "<asset_name>" --date <the date>` with `--out <your TRACE.json>`: for shape a the served date; for shape b the SERVED date (it reports the carry-forward
   row and its rule) AND again at the anchor date (it reports the median and the trade ids). `trade_ids`, `recomputed_price` and `recompute_equals_served` carry into the record from the anchor trace
   for shape b (the recompute is the anchor's median, and `recompute_equals_served` compares it with the price SERVED at the served date). `rule` names the whole chain in one or two sentences
   (for example "carry_forward from <anchor date>; anchor is the median of that day's trades per bd_price_update.py:327-344"). Set `chain` to `true` and `anchor_date` to the anchor's date for shape b.
4. **Name the writer.** From `WRITERS.json`, name which writer wrote the price row served for that date (writer id and the rule copy it applies), or say `unidentified`. For shape b also name the writer of
   the anchor row if the versions let you (the version history is in `WRITERS_VERSIONS.tsv`), or say `unidentified`.
5. **Do not choose a favourable row dishonestly.** If no candidate fits (no untickered transaction_observed holding with `EQUAL`), say exactly how many candidates failed each condition and file a BLOCKING row; do not relax a condition.

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/THREAD_TRACE.json`

```json
{"order": "BP-a-4", "read_at": "<ISO UTC>", "claim": "measured",
 "served_object_key": "<bucket>/<key>@<VersionId>", "as_of_date": "YYYY-MM-DD",
 "account_ref": "<first 12 hex of sha256(str(account_id))>", "asset_name": "<name>", "ticker": null,
 "served_price": 0.0, "price_source": "transaction_observed | carry_forward | linear_interpolation",
 "chain": false, "anchor_date": null, "shape_counts": {"direct": 0, "chain": 0},
 "client_entity_class": "normal", "objects_tried": 0, "objects_failing_one_price": 0,
 "rule": "<one sentence, with file:line>", "trade_ids": ["<transaction_id>", "..."],
 "recomputed_price": 0.0, "recompute_equals_served": true,
 "writer": "<writer id and rule copy from WRITERS.json, or unidentified>",
 "gap_class": "EQUAL (the anchor's, for a chain)", "candidates_considered": 0,
 "instrument": "org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~2/trace_price.py"}
```

Never write the raw `account_id`, a client name or an advisor name anywhere (the grader refuses the key `account_id`). Also write `THREAD_TRACE.md` (one page an analyst can read: the served price, the rule in plain
words, the trades, the recompute, the writer, and the three commands that reproduce it).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited. Downloaded files go to `C:/dev/wk-bdprce-r1-4-data/` (outside the checkout).
2. No client name, account number or advisor name is printed anywhere.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-a-4 thread needs the served prefix listing`. A step that cannot finish reports `claim: absent` for what was not read.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/ADVI_BDPRCE.TO-BP-a-4.thread.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-a-4"><invocation>cd /c/dev/wk-bdprce-r1-4 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round1/checks/r1_checks.py thread --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/THREAD_TRACE.json</invocation><expect>^THREAD record ok rule=\S+ trades=[1-9][0-9]* equal=true$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-a-4"><invocation>cd /c/dev/wk-bdprce-r1-4 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r1-4 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~4/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, PII discipline and that the recompute equals the served price; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). That the row is real is read by the issuer from the cited object.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit `THREAD_TRACE.json`, `THREAD_TRACE.md` and your trace output FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W4-S<k>` (the dell1 gate requires the D1 coordinate; row `ADVI_BDPRCE-D1-W2-S5`), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the served object key, date, asset (name), served price, source, trade count, recompute and equality, the writer, the gap class, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PRD cell C10; FWD-1 DONE WHEN. STAGED at the cut: it un-parks when `BP-a-1`, `BP-a-2` and `BP-a-3` are merged and PASS at the merged HEAD; its worktree is cut from that HEAD, so the three deliverables are in it.
The FWD-1 grade (REALIZED) is the CTO's at the round-1 analysis, on the issuer's one real run of this record at the drain (the served object re-opened). Read-only; class LOCAL.

<status>complete</status>
<round>1</round>
<workstream>THREAD</workstream>
<to_id>ADVI_BDPRCE.TO-BP-a-4</to_id>
<slot>~4</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
