# ETFS_RIVALS task order -- `RIV-ps-1` -- ROUND 15 (ENRICHMENT): ONE PRICE SERIES PER SECURITY: MARKET CLOSE, THEN HOLDING-IMPLIED, THEN A GAP WITH ITS REASON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-ps-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the backfill is ad hoc by Andrew's word and is run by the issuer, never scheduled)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the chart objects sit under the page prefix the publisher already writes and the gateway already reads)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. **Round 15** (PRD v0.18 FWD-22, FWD-23): every period becomes 30 / 90 / 365 calendar days; the security dialog gains a price curve with the fund's buys and sells marked on it, fed by a per-fund chart object behind one gateway route and drawn by the page's one script; a Bloomberg close-price backfill is built (never run by a worker). Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

Shared vocabulary (binding on every cell):
- **Periods:** `R30`, `R90`, `R365` -- calendar days. `asof = prev_trading_day(page_day)` (the existing CALL 3 rule); a window's
  first day is `asof - N calendar days`, its last day `asof`. `MTD`, `QTD`, `YTD` keep computing and are never displayed.
- **Chart object:** one JSON per fund per page day at `homes.page(<day>, "charts/<FUND>.json")` (opal_naming output), shape
  `{"fund", "asof", "generated_at", "ranges": {"R30": <first day>, "R90": ..., "R365": ...}, "securities": {<security_key>:
  {"name", "source_words", "points": [[<YYYY-MM-DD>, <price>|null, <source code>], ...], "gaps": [{"start", "end", "reason"}],
  "markers": [{"side": "buy"|"sell", "start", "end", "span": bool, "usd", "bps", "r", "n_trades"}]}}}`. Source codes:
  `m` market close, `i` holding-implied. `points` ascend by date and cover `asof - 365d .. asof`.
- **Route:** `GET /rivalfunds/<YYYY-MM-DD>/chart/<FUND>` on the gateway, JSON, behind the same identity wall.

### `RIV-ps-1` -- one price series per security: market close first, holding-implied second, a gap with its reason third (FWD-22; C-MODAL-PRICE-SOURCE)
- Measured: `gold/security_market` holds 4 day partitions; `trade_schedule` 504. No module assembles a per-security daily series.
- Interface: new `rivalfunds/price_series.py`. `series(g4: DataFrame, g1: DataFrame, keys, start: date, end: date) -> {key:
  {"points": [(date, price|None, "m"|"i"|None)], "gaps": [{"start","end","reason"}], "source_words": str}}`. For each NYSE
  trading day in `[start, end]`: the G4 `px_close` of that date when present and positive (`m`); else the price implied by any
  universe fund's G1 report of that date, `market_value / quantity` with quantity > 0 (`i`; when several funds report, the
  median); else `None`. Consecutive `None` days form one gap with reason `"no market close on file and no fund reported the
  holding"`. `source_words` names in plain words which sources the series uses. No vendor call, no S3 call: pure over frames.
  `load(s, keys, start, end)` reads the two tables through the sink for the publisher.
- Rulings at the cut (issuer): a G1 row maps to a key through `gold_holding_contribution.row_keys` (the page's own key rule,
  raw-identifier alias included), never `security_id` alone. Several lots of one security in one fund's report are summed
  (market value and quantity) before the ratio. A key in neither frame returns all-None points and one gap over the range.
  Point dates are ISO strings. `load(s, keys, start, end)` returns the same dict `series` returns.
- **Organic trigger:** the publisher's chart object (RIV-co-1).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD f14a8198f7)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ps-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- Read how `gold_holding_contribution.py` reads G4 (`_prices`) and G1 and maps a row to a key (`row_keys`); reuse, do not re-derive.
- You run ps-1 FIRST; RIV-tm-1 and RIV-co-1 follow on the same branch.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r15ps1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/price_series.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- market close first, holding-implied second (median of several funds), None with one gap per run of missing days, trading days only; control: the fixture frames hold the planted values (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ps-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-ps-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/ps-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-ps-1.one-price-series-per-security-market-then-implied-then-gap.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-ps-1.one-price-series-per-security-market-then-implied-then-gap`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.5 (round 15 appended). Chain `~2`, slot `~2`, position 1 of 3. Checks dry-run at base by the issuer: ps-1.AC1 FAIL as expected (control PASS). Check files drafted by read-only helpers under the issuer's brief and re-run by the issuer.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~2</slot>
<fabric>site-z</fabric>
