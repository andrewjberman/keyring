# ADVI_BDPRCE task order -- `BP-b-2` -- R1 REPLAYED OVER THE SERVED PRICES INTO THE NAMED BEFORE/AFTER LIST (STAGED, READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R2.md</decomp_doc>
<owned_cells>BP-b-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~6</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only replay; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a class partition whose sum differs from `served_rows`, `served_write` true, a non-deterministic replay, a missing variant and a write verb in `calls` (33-arm self-test OK). Blindness: the grader proves arithmetic and shape, not that a changed price is right; the issuer re-computes a sample of changed rows with the module.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-b-2` (round 2; read-only; this cell produces the list Andrew reviews, it moves nothing)

The CTO ruled the one price rule R1 and the module is built (`BP-b-1`, merged into your worktree at `data/black_diamond/scripts/silver/bd_price_rule.py`, with `tests/test_bd_price_rule.py` and the probe
`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.md`; read all three first). R1: median of DISTINCT trades (each `transaction_id` once), trades only at the executed `price`,
every non-trade row excluded, ties by `SOURCE_RANK` then a stable sort, no trade on the date -> carry-forward WITH its observation date, interpolation banned, rows keyed on `trade_date`.
Before any served price may move, Andrew sees a named before/after list. You produce its price half: what each served price would become under R1, and why. You change nothing.

### 1a. What to read and compute

1. **The served set.** The window and denominator are those of round 1's gap record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~3/GAP_ROWS.csv` (1,657 served
   `transaction_observed` rows over 2026-09-16..2026-10-13: date, asset_name, served_price, recomputed_price, class). Re-read `canonical_prices.parquet` (`opal-data-bd`, `silver/prices/`) for the same window and
   print the denominator again; if it differs from 1,657, say so and use the re-read count.
2. **Replay.** For each served row, compute R1 with variant A from the day's trades (`silver/transactions/<date>.parquet`; keyed on `trade_date`, so read the partition of that date AND the next partition
   when a row of the target `trade_date` sits there: state how many rows differ between file-day and trade-date keying) and classify the row, in this order:
   `UNCHANGED` (R1's price equals the served price within `1e-6 * max(1, |served|)`), `CHANGED` (R1 prices it differently), `NOW_CARRY_FORWARD` (R1 has no trade on that date: shows the last observed R1 price
   with its observation date), `NOT_RECOMPUTABLE` (no partition or no valid row). Run variant B (adds Dividend Reinvestment) over the same rows and record its price beside variant A: it is a sensitivity, not the result.
3. **The estimated rows.** Also list every (date, asset) in the window whose canonical source is `linear_interpolation` or `carry_forward` and whose asset has at least one `transaction_observed` row in the
   window: what R1 would show (a trade price, or "last traded <date>" with that date). These are the estimated prices the CTO banned; mark each `estimated_row`.
4. **The named reasons.** Per changed row: old price and old source, new price (variants A and B), the distinct trade count behind it, counts of excluded rows by type, and flags `dividend_dominated` (old
   median was 1.0 from cash rows), `repeat_weighted` (old median differs from the distinct median) and `estimated_row`. The 64 rows round 1 left UNEXPLAINED and the 19 recomputing to 1.0 must each appear
   with their R1 price.
   Round 2's rule probe (`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~5/RULE_PROBE.md`) found that some served prices come from NON-TRADE rows: the round-1 thread asset's
   served 168.94 on 2026-10-09 is the price of four `Transfer In` rows (no Buy or Sale that day), and `BLACKROCK INC COM` on 2026-09-22 has only `Dividend` and `Dividend Reinvestment` rows.
   So for each changed row also record `old_price_types`: the `transaction_type` values of the rows that reproduce the old served price (recompute the old median per row type group; `none` when no
   group reproduces it) and count the changed rows by that field. Under variant A such assets are `NOW_CARRY_FORWARD`; say how many, and how many variant B prices instead.
5. **Determinism and the past-date arm.** Run the whole replay twice and show equal md5; and for 20 changed rows show that the result for a past date reads that date's trades only.

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/REPLAY.json`, plus `BEFORE_AFTER.csv`

```json
{"order": "BP-b-2", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api get-object ...", "..."],
 "window": "YYYY-MM-DD..YYYY-MM-DD (n weekday dates)", "served_rows": 0,
 "classes": {"UNCHANGED": 0, "CHANGED": 0, "NOW_CARRY_FORWARD": 0, "NOT_RECOMPUTABLE": 0},
 "variants": {"A_trades_only": {"changed": 0}, "B_plus_reinvestment": {"changed": 0}},
 "no_trade_policy": "carry the last observed R1 price with its observation date; interpolation banned",
 "estimated_rows_listed": 0, "dividend_dominated": 0, "repeat_weighted": 0, "file_day_vs_trade_date_differs": 0,
 "deterministic": true, "served_write": false, "list_file": "BEFORE_AFTER.csv"}
```
`BEFORE_AFTER.csv`: one line per row of the list (date, asset_name, old_price, old_source, new_price_A, new_price_B, class, distinct_trades, excluded_by_type, flags, observation_date). The class keys are exactly
those four; their sum MUST equal `served_rows`. Also write `REPLAY.md` (one page in plain words for a reader who has not seen the code: what R1 is, how many prices move and by how much, the three largest movers, what
the estimated rows would show, what stays unknown).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited (the module is read, not changed). Downloaded files go to `C:/dev/wk-bdprce-r2-6-data/` (outside the checkout).
2. No client name, account number or advisor name is printed. An asset's name is not one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-b-2 replay needs the key listing`. `BEFORE_AFTER.csv` is committed only if under 5 MB; otherwise its path and sha256 are named in `REPLAY.md`.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/ADVI_BDPRCE.TO-BP-b-2.replay-before-after.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-b-2"><invocation>cd /c/dev/wk-bdprce-r2-6 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round2/checks/r2_checks.py replay --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/REPLAY.json</invocation><expect>^REPLAY record ok served=[0-9]+ changed=[0-9]+ unchanged=[0-9]+ deterministic=true$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-b-2"><invocation>cd /c/dev/wk-bdprce-r2-6 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r2-6 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, arithmetic, determinism and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The issuer re-computes sample rows with the module.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit your scripts, `REPLAY.json`, `REPLAY.md` and `BEFORE_AFTER.csv` FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W6-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the window, the denominator, the four class counts for variant A and the changed count for variant B,
the three largest movers (asset name, old, new), the estimated-rows count, determinism, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-1 analysis item 1 (second half); FWD-7 DEC-7 (the named list). STAGED at the cut: un-parks when `BP-b-1` is merged and PASS at the merged HEAD; its worktree is cut from that HEAD so the module is in it.
The dollar effect on the latest snapshot and the downstream readers are `BP-b-7`'s (the join), which consumes this list and the census extract.

<status>pending</status>
<round>2</round>
<workstream>REPLAY</workstream>
<to_id>ADVI_BDPRCE.TO-BP-b-2</to_id>
<slot>~6</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
