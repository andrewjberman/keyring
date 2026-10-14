# ADVI_BDPRCE task order -- `BP-c-2` -- THE REPLAY RE-RUN ON THE AMENDED RULE (R1.3), WITH THE FATE OF EVERY INTERPOLATED ROW (READ-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BDPRCE/decompositions/ADVI_BDPRCE_DECOMP_R3.md</decomp_doc>
<owned_cells>BP-c-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_BDPRCE~21</issued_to>
<issued_by>2.0.0_SA_COO~K1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only replay; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`s3api get-object`/`list-objects-v2`/`list-object-versions`). No grant, no put. A denied read is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a class partition whose sum differs from `served_rows`, `served_write` true, a non-deterministic replay, a par-quoted row not UNCHANGED, a carry-forward without an observation date, interpolated fates that do not sum and a write verb in `calls` (35-arm self-test OK). Blindness: the grader proves arithmetic and shape, not that a price is right; the issuer recomputes sample rows with the module.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `BP-c-2` (round 3; read-only; it produces the list Andrew reviews, it moves nothing)

Round 2 replayed R1 over the 1,657 served `transaction_observed` rows (`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~6/`: `replay_r1.py`, `lookback_scan.py`, `REPLAY.md`, `REPLAY.json`, `BEFORE_AFTER.csv`, `ESTIMATED_ROWS.csv`; read `REPLAY.md` first). The CTO then ruled AMENDMENT 1 of R1
(`org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md`), and `BP-c-1` put it into the module (merged into your worktree: `data/black_diamond/scripts/silver/bd_price_rule.py`, its test and `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.md`; read all three).
You re-run the replay on the AMENDED module so the list Andrew sees carries it. You change nothing served.

### 1.00 AMENDMENT 3 -- THIS ORDER IS REOPENED A SECOND TIME (issuer, 2026-10-14 ~04:0xZ); it REPLACES sections 1b, 4 and the paths where they differ

You are the THIRD seat of this slot. The first two seats' work is merged in your tree (`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~14/`: `replay_r1_r3.py`, `verify_partitions.py`, `REPLAY2.*`, `BEFORE_AFTER2.csv`, `ESTIMATED_ROWS2.csv`, `PARTITIONS2.csv`; read `REPLAY2.md` first). The CTO ruled AMENDMENT 3 (call 19b2; `org/missions/D8/ADVI/ADVI_BDPRCE/ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md`, section AMENDMENT 3): **R1 changes a price's value, never an asset's unit; each asset is served in the unit of its own served series.** `BP-c-1`'s third seat built it into the module (merged into your tree: `data/black_diamond/scripts/silver/bd_price_rule.py` at `AMENDMENT = "R1.3"`, with `served_unit_map(lots)` and the REQUIRED keyword `served_units` on `price_for_date`; read the module and `RULE_PROBE3.md` under `deliverables/0.9.0_WK_ADVI_BDPRCE~20/` first). Round 3's second seat found row `W14-S5`: MORGAN STANLEY FIN LLC 0% 05/03/2029 would have moved 115.995 to 1.0 (a 100x unit change) and 214 interpolated carries shared it. You re-run the replay so none does. You change nothing served.
Do exactly the section 1a work again (copy `replay_r1_r3.py` and `verify_partitions.py` into your folder and adapt; same served set, same four classes, same tolerance, same keying across all partitions, same fates for interpolated rows, same determinism arm) with these differences:
1. **The unit map.** Build `served_units` with the module's `served_unit_map(pairs)` exactly as `BP-c-1`'s third seat did (merged into your tree: read the module, `rule_probe3.py` and `RULE_PROBE3.md` under `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~20/`; copy its pair builder, do not rewrite it). A pair is `asset_name`, `served_price`, `per_unit_value`; the bands are coarse ([50, 200] -> `per100`, [0.5, 2] -> `per_unit`, else `unreadable`). Pair sources, in PRIORITY order, one source per asset: (1) the served canonical row (source `transaction_observed`, window 2026-09-16..2026-10-13) against the Buy / Sale / reinvestment trade rows of that asset on the same trade_date; (2) for an asset with no such pair, the served row against the asset's most recent EARLIER trade row with a computable |market_value| / |units| in any partition; (3) ONLY for an asset with no pair from (1) or (2), the lot pairs (`current_price`, |market_value| / |quantity|) of the extract `C:/dev/wk-bdprce-r2-7-data/lot_extract.csv` (its sha256 must read `e7e618d76516c8b7977179aefb3f77ce4fc13c17fbcf1dbeb92001a6e0a2b50b`, else a BLOCKING row and you stop). Trade pairs outrank lot pairs because the lot market values are cap-scaled on some lots (the third seat measured ISHARES CORE U.S. AGGREGATE BOND ETF at 3.5498 from lots against 1.0 from its own trades; row W20-S13). Expected, not forced: 888 served assets, about 1 `per100` (MORGAN STANLEY FIN LLC 0% 05/03/2029), about 59 with no pair at all. Write `UNIT_MAP.csv` (asset_name, unit, median_ratio, pairs, source) and carry the counts in the record: `served_units` = `{"assets": n, "per100": n, "per_unit": n, "unreadable": n}`. Every module call passes the map.
2. **An unreadable unit withholds.** A served row of a Fixed Income asset whose unit is `unreadable` (or absent from the map) is `NOT_RECOMPUTABLE` with the reason `unit_unreadable`; count them in `unit_withheld_rows`, and list the assets in `REPLAY3.md`. Never guess a unit.
3. **No row changes unit.** `unit_changed_rows` = the number of served rows (CHANGED or NOW_CARRY_FORWARD) whose `new_price / old_price` is within 1 percent of 100 or of 0.01. It must be 0; a row that is not 0 is a BLOCKING row naming it, not a number you adjust. State in `REPLAY3.md` what MORGAN STANLEY FIN LLC 0% 05/03/2029 on 2026-10-05 reads now (expected: from the 2025-05-28 par Buy, 100.0 against the old 115.995, with its observation date) and how the 214 interpolated rows that shared the case read now.
4. **Compare with round 3's second seat.** `REPLAY3.md` has a short table: each class count under `REPLAY2` and under `REPLAY3`, the number of withheld Fixed Income trade rows and assets (442 rows on 25 assets, 14 served, before), and the interpolated fates (29 / 15,997 / 2,394 before).
Outputs, in `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~21/`: `REPLAY3.json`, `REPLAY3.md`, `BEFORE_AFTER3.csv`, `ESTIMATED_ROWS3.csv`, `UNIT_MAP.csv`, `PARTITIONS3.csv` if you re-verify partitions (the verified cache of the second seat is read; refetch any partition whose S3 ETag or length differs; state the count). Record: the section 1b record with `"amendment": "R1.3"`, `"list_file": "BEFORE_AFTER3.csv"`, plus `"served_units"`, `"unit_map_file": "UNIT_MAP.csv"`, `"unit_changed_rows": 0`, `"unit_withheld_rows": n`. Downloads go to `C:/dev/wk-bdprce-r3-21-data/`. Row ids `ADVI_BDPRCE-D1-W21-S<k>`.
Proof (replaces section 4): AC1 runs `r3_checks.py replay3 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~21/REPLAY3.json` and expects the line `REPLAY3 record ok served=N moved=N unchanged=N unit_changed=0 unit_withheld=N deterministic=true`; AC2 is the write-surface bound (`--root /c/dev/wk-bdprce-r3-21`, allowing `~21/`, the investigation file and this order file). Where the text below names `~14`, `REPLAY2`, `R1.2` or `r3-14`, THIS section wins.

### 1a. What to do (the first seat's text; section 1.00 above wins where it differs)

0. **AMENDMENT 2 binds (CTO call d799, `ledger/CTO_RULING_R1_THE_PRICE_RULE_20261013.md` AMENDMENT 2):** par-quoted is decided PER ROW by the module: Fixed Income class AND price over (market value / units) within 1 percent of 100 -> scaled; within 1 percent of 1 -> per unit, left alone; any other ratio -> withheld with its printed ratio. The caller passes the set of Fixed Income asset names (`asset_super_class_bd == 'Fixed Income'` from `silver/bd_assets_dim.parquet`), not a coupon-based set. All EIGHT round-2 `scale_100x` rows must read UNCHANGED and no Fixed Income fund may scale; a withheld row prints its ratio in the flags. `BP-c-1` is reopened and its second seat's merge is what you receive.
0b. **What the merged second seat found (read `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~13/RULE_PROBE2.md`):** on the four probe dates all eight `scale_100x` rows read UNCHANGED, 24 Fixed Income rows scaled (none a fund), and 9 rows of two Fixed Income FUNDS were WITHHELD because their ratio sits outside both 1 percent bands (VANGUARD SHORT-TERM INVESTMENT-GRADE INV 1.0844; POLEN OPPORTUNISTIC HIGH YIELD INS 1.0433).
   Over the whole window, QUANTIFY it: put into `REPLAY2.json` the field `withheld_rows` (a count), and in `REPLAY2.md` the list of withheld assets with their printed ratios and how many served prices each touches, so the CTO can see what the 1 percent band costs before any widening is asked. Withheld rows count as `NOT_RECOMPUTABLE` with the reason `ratio_unrecognised` in the flags; never guess a price for them.
1. **Copy, do not edit, round 2's scripts** into your folder and adapt them to import the amended module and call it with the par-quoted candidate set (build it from `silver/bd_assets_dim.parquet` exactly as `BP-c-1`'s probe did; read its `RULE_PROBE2.md`).
   Same served set (the 1,657 rows; re-read `canonical_prices.parquet` for the window 2026-09-16..2026-10-13 and print the denominator; if it differs, say so), same four classes: `UNCHANGED`, `CHANGED`, `NOW_CARRY_FORWARD`, `NOT_RECOMPUTABLE`, same tolerance `1e-6 * max(1, |served|)`.
2. **Expected movements from the amendment** (check each and report the measured counts, do not force them): the reinvestment-sourced carry-forwards of round 2 (77) price from the reinvestment buys; the Transfer-In-sourced carry-forwards (153) stay carry-forwards, EACH with its last observation date; the eight `scale_100x` rows
   read `UNCHANGED`. Withheld par rows (ratio disagreement) are reported separately and count as `NOT_RECOMPUTABLE` with the reason in the flags.
3. **The late-landed trades (round-2 row `W6-S3`).** Round 2's lookback read trade dates t and t+1 only, while 61,583 trade rows land more than a day after their trade date. Key the replay on `trade_date` ACROSS ALL PARTITIONS you hold or fetch: round 2's scratch cache `C:/dev/wk-bdprce-r2-6-data/tx_back/` (about 1,300 partitions, 2020-03 to 2026-10) is on this disk;
   use it, verify each partition against S3 `head-object` ContentLength and ETag before relying on it (a mismatch is refetched), and fetch what is missing. If a date range cannot be keyed completely (the `silver/transactions` gaps of row `W6-S5`: 50 dates in 2026, 436 in 2020-2025),
   state the limit on the list. `lookback_keying.mode` is `trade_date_all_partitions` when every window date is keyed across all partitions and the gaps are named, else `limited` with the statement.
4. **The fate of every interpolated row (round-2 row `W12-S1`).** Every (date, asset) in the window whose canonical source is `linear_interpolation` (18,566 rows over 886 assets in round 2, re-count) gets its fate under the amended R1: `trade_price` (a trade that day), `last_traded_date` (a carry-forward WITH its observation date), or `unresolved` (no R1 trade back to the floor).
   Write them to `ESTIMATED_ROWS2.csv`. `interpolated.rows` = their count; the three fates sum to it.
5. **Determinism and the past-date arm.** Run the whole replay in two separate processes: equal md5 of `BEFORE_AFTER2.csv`. And for 20 CHANGED rows show the result for a past date reads that date's trades only.
6. **Named reasons** per changed row, as in round 2 (old price and source, new price, distinct trades, excluded counts by type, flags `dividend_dominated`, `repeat_weighted`, `estimated_row`, `scale_100x`, `withheld`), and `old_price_types`.
7. **Round-1 rows:** the 64 UNEXPLAINED and the 19 recomputing to 1.0 from round 1, each with its amended price (round 2 had them as 27 carry-forward, 20 changed, 16 not recomputable, 1 unchanged).

### 1b. The record: `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~14/REPLAY2.json`, plus `BEFORE_AFTER2.csv`, `ESTIMATED_ROWS2.csv`

```json
{"order": "BP-c-2", "read_at": "<ISO UTC>", "claim": "measured", "calls": ["aws s3api get-object ...", "..."], "amendment": "R1.2",
 "window": "YYYY-MM-DD..YYYY-MM-DD (n weekday dates)", "served_rows": 0,
 "classes": {"UNCHANGED": 0, "CHANGED": 0, "NOW_CARRY_FORWARD": 0, "NOT_RECOMPUTABLE": 0},
 "par_quoted_rows": 0, "par_rows_unchanged": 0, "par_withheld": 0,
 "transfer_in_carry_forwards": 0, "carry_forwards_with_date": 0,
 "interpolated": {"rows": 0, "with_trade_price": 0, "with_last_traded_date": 0, "unresolved": 0},
 "lookback_keying": {"mode": "trade_date_all_partitions | limited", "statement": "<what is keyed, the gaps, the late-landed count>"},
 "deterministic": true, "served_write": false, "list_file": "BEFORE_AFTER2.csv", "list_sha256": "<64 hex>"}
```
`par_quoted_rows` is the count of round-2 `scale_100x` rows (eight) and `par_rows_unchanged` how many of them now read UNCHANGED: the grader requires all of them. `carry_forwards_with_date` must equal `NOW_CARRY_FORWARD`. The four class keys are exactly those; their sum MUST equal `served_rows`.
`BEFORE_AFTER2.csv`: one line per served row (date, asset_name, old_price, old_source, new_price, class, distinct_trades, excluded_by_type, flags, observation_date, old_price_types, round2_class, round2_new_price). Commit it if under 5 MB; otherwise name its path and sha256 in `REPLAY2.md`.
Also write `REPLAY2.md` (one page in plain words for a reader who has not seen the code: what changed from round 2 and why, how many prices move and by how much, the three largest movers, the interpolated rows' fates, the limits of the lookback, what stays unknown).

## 2. BOUNDS

1. READ verbs only on AWS. No write, no producer run, no product file edited (the module is imported, not changed). Downloaded files go to `C:/dev/wk-bdprce-r3-14-data/` (outside the checkout); round 2's cache is READ, never modified.
2. No client name, account number or advisor name is printed. An asset's name is not one.
3. A raw S3 listing the rail denies is re-run with a trailing `# rail-checked: BP-c-2 replay needs the key listing`.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~21/
org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~21/ADVI_BDPRCE.TO-BP-c-2.replay-rerun.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="BP-c-2"><invocation>cd /c/dev/wk-bdprce-r3-21 &amp;&amp; timeout 120 python org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round3/checks/r3_checks.py replay3 --file org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~21/REPLAY3.json</invocation><expect>^REPLAY3 record ok served=[0-9]+ moved=[0-9]+ unchanged=[0-9]+ unit_changed=0 unit_withheld=[0-9]+ deterministic=true$</expect></criterion>
  <criterion id="AC2" cell_refs="BP-c-2"><invocation>cd /c/dev/wk-bdprce-r3-21 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-bdprce-r3-21 --allow org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/0.9.0_WK_ADVI_BDPRCE~21/ --allow org/missions/D8/ADVI/ADVI_BDPRCE/surprise-channel/investigations/INVESTIGATION_v1.md --allow org/missions/D8/ADVI/ADVI_BDPRCE/task-orders/ADVI_BDPRCE.TO-BP-c-2.replay-rerun.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape, arithmetic, determinism, the par-quoted rows and read-only discipline; AC2 is the write-surface bound (its printed label says ROUND 4 because the checker is reused unchanged). The issuer re-computes sample rows with the module.

## 5. WHEN YOU ARE DONE

Instance at the path above. Commit your scripts, `REPLAY2.json`, `REPLAY2.md`, `BEFORE_AFTER2.csv` (if under the bound) and `ESTIMATED_ROWS2.csv` (if under the bound) FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_BDPRCE-D1-W21-S<k>` (D1 coordinate required), `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the window, the denominator, the four class counts, the changed-and-carry count, the par rows (of eight, how many UNCHANGED, how many withheld), the Transfer-In carry-forwards with dates,
the interpolated fates, the keying mode and its limits, the three largest movers, determinism, AC1, AC2 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 analysis item 1 (second half); FWD-7 DEC-7. STAGED at the cut: un-parks when `BP-c-1` is merged and PASS at the merged HEAD; its worktree is cut from that HEAD so the amended module is in it. The packet (dollar effect, readers) is `BP-c-3`'s, which consumes this list.
Round 2's replay took about four hours, mostly the lookback download; this order reuses that cache, so it should take far less. Class LOCAL.

<status>pending</status>
<round>3</round>
<workstream>REPLAY2</workstream>
<to_id>ADVI_BDPRCE.TO-BP-c-2</to_id>
<slot>~21</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
