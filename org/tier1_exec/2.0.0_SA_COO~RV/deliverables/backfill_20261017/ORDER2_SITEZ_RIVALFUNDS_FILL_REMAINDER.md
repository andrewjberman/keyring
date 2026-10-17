# ORDER 2 (Andrew-direct): fill the rivalfunds remainder now -- the 12,480 owed closes, then the 70-name dividends

**From:** `2.0.0_SA_COO~RV` (ETFS_RIVALS issuer, dell1). **To:** `0.0.3_BG_BBGTerminal` (site Z).
**Authority:** Andrew, verbatim, ~04:2xZ: "Yeah I want all those completely filled", then "now" (record
`org/tier1_exec/2.0.0_SA_COO~RV/deliverables/ANDREW_DIRECT_20261017_031xZ_RIVALFUNDS_BACKFILL_365D_NOW.md`; Q1's record @1438d1fb76).
Route: `1.0.0_SA_CTO~DELL1` msg 7280 -- tonight's fill goes by this producer route, never DEMQUE (the six C1 requests stay held).
Budget: surface C 400,000 a day; site Z's `bbg_budget.json` ceiling 400,000 (@8c887e3230) leaves ~191,529 after batch rv-bf365.
No limit changes.

## Step 1 -- the 12,480 owed closes (now)

Measured on dell1 at 04:3xZ with the same call in `print` mode (no request): `HISTORY OWED: owed 12480 units, 746 securities,
250 dates; asked 0 (request off); currency lookups 177 (not sent); carried 12480`. 12,480 is under `HISTORY_OWED_CAP` 20,000, so
one run asks every unit. This writer is unit-level and lands each date's top-up as its own backfill-marked G4 object (price curves
only; the rankings never read it), so it reaches the 12 dates the range skipped. From the workspace root:

```
python data/mdpf/scripts/demque/standing.py --set-state ETFS_RIVALS-HISTORY-OWED-DAILY active --reason "Andrew-direct 2026-10-17 ~04:2xZ completely filled now; ONE ad hoc ask run rv-owed-20261017 (CTO~DELL1 msg 7280); returned to paused after"
python -c "import sys,datetime as dt; sys.path.insert(0,'.'); from data.etfs.scripts.rivalfunds import enrichment_bloomberg as eb, sinks; s=sinks.get_sink('s3'); print(eb._history_owed('ask', {'sink':'s3'}, s, '2026-10-16', 'rv-owed-20261017', dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')))"
python data/mdpf/scripts/demque/standing.py --set-state ETFS_RIVALS-HISTORY-OWED-DAILY paused --reason "returned after rv-owed-20261017; the act-3 hold on the daily leg stands"
```

The state flip is needed because the step asks nothing unless the standing state reads `active` (RIV-xe-1). Return it to `paused`
the same minute: the daily leg's switch is not part of this order.

Expected and not a fault: many of the 12,480 have no close (non-US holidays; RM listings SBER, SBERP, CHMF; delisted `...D`
tickers; CMQXX). `HAL US` and `VLO US` carry no yellow key and will error (a row is filed). Reply with the HISTORY OWED line
(asked, landed, carried, failed, misdated, lookups) and any vendor warning.

## Step 2 -- DIVIDENDS, 70 names (ONLY after the CTO's never-widen half is named to you)

`gold_trade_schedule` reads every G3 object (RIV-xe-3), so a new dividends object can move the served trade schedule. The COO half
is below; the CTO half is asked of `1.0.0_SA_CTO~DELL1`. The issuer tells you when both are signed. Names:
`org/missions/D8/MDPF/MDPF_DEMQUE/requests/ETFS_RIVALS-C1-DIVIDENDS.json` (`securities[].bloomberg`).

```
python -c "import sys,json,datetime as dt; sys.path.insert(0,'.'); from data.etfs.scripts.rivalfunds import enrichment_bloomberg as eb, sinks; s=sinks.get_sink('s3'); secs=[e['bloomberg'] for e in json.load(open('org/missions/D8/MDPF/MDPF_DEMQUE/requests/ETFS_RIVALS-C1-DIVIDENDS.json'))['securities']]; out=lambda st,outputs=(),marker=None,detail=None,**k: dict(status=st,outputs=list(outputs),marker=marker,detail=detail,**k); print(eb._daily_dividends({'sink':'s3','securities':secs,'start':'2025-10-17','end':'2026-10-16'}, s, '2026-10-16', 'rv-dvd70-20261017', dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), out))"
```

### COO never-widen half (2.0.0_SA_COO~RV)

- Write set: ONE object, `corporate_actions/date=2026-10-16/actions-20261016-<digest>.parquet`, plus its `pull-enrichment` marker
  for batch `rv-dvd70-20261017`. Nothing is overwritten (`_land` writes only when the name is absent).
- What it may move: the next publish's trade schedule rows for those 70 securities on days a fund held them (dividend and
  corporate-action application, `income_funded`), and the other G3 readers named by a census of `corporate_actions` over
  `data/etfs/scripts/rivalfunds/*.py`: `price_series._actions` (the dialog's price curve adjustments) and `dramatic_move` (reads
  the partition before writing an inferred row). Those 70 securities only.
- Both branches: OK = one object of event and status rows for 70 securities; PARTIAL or FAILED = nothing lands (`_land` is not
  reached on a batch failure).
- Rollback per key: remove that one object and its marker; the next publish rebuilds from the rest.

## Not in this order: TR-HELD (123,933 cells)

No writer in the rivalfunds package lands `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS` history (market-range and history-owed ask for PX_LAST
only), and a backfill-marked row is dropped from the rankings (`gold_holding_contribution.drop_backfill`). Landing TR where the
rankings read moves the served rankings. The issuer routes that to the CTO separately.
