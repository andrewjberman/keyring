# NEVER-WIDEN -- COO half request: MDPF_DEMQUE round 9, the standing T-1 extension of the price store (DQ-t-31; `2.0.0_SA_COO~Q1`, 2026-10-11 ~17:5xZ)

**Asked of** `1.0.0_SA_CTO~DELL1` (his CTO half, round-8 analysis section 3 item 1 and ADDENDUM 1, msg 3956). **Bytes read** (box/dell1 HEAD
`1bb7035580`): DQ-t-30+t-31 `1961d4ee7a`, DQ-t-36 `df9aaa34cc`, DQ-t-37 `8e63ec0a23`, DQ-t-38 `1bb7035580`. Every line number is at those bytes.

## 1. The act

`data/mdpf/scripts/demque/run_daily_draw.sh` (the scheduled task `Opal MDPF_DEMQUE daily draw`, 22:30 local, dell1) now runs
`extend_frontier.py --apply` (:16) before the draw (:17). The act this half covers is: (a) ONE deliberate run of that script by the issuer after
signing, then (b) the schedule continuing at 22:30 local. It writes a standing request and resets the pacer entries of the 141 symbols; the
draw then re-pulls each once and `price_store.write` rewrites a name's files only when its lock is LOCKED.

## 2. Writers and readers of the named property (counted, N printed)

- **Writers of `price_history/cusip=*/{prices,splits,dividends}.parquet`:** N = 1, `price_store.write` (:112), called from `daily_draw.py:93` only
  (a repo-wide read of non-test callers under `data/` printed that one call site; `price_store.write_index` :160 writes `index/` from
  `daily_draw.py:101`, N = 1). `lock.json`: N = 2, the same `write` (:139) and `hold_lock_records.py --apply` (applied 2026-10-11 to 14 names,
  its own CTO half = round-8 R2); the second changes `claim`/`claim_reason` only.
- **Readers found by name (a code read, not a census of the estate):** `data/assets/scripts/silver/commonwealth_daily_valuation.py:469` reads
  `cusip=<CUSIP>/splits.parquet` only (split dates, `SPLIT_STORE`); `data/assets/scripts/silver/commonwealth_price_need.py:68` reads
  `index/index.parquet`. ADVI_COTBKF's reader of `prices.parquet` (named in TO-DQ-t21) was not re-read here and no page reads the Yahoo file for the
  production chain (D1-S12 disarm evidence): both are RESIDUAL, named, not claimed clean.

## 3. Blast radius, and the rollback per key

- **May touch:** S3 `opal-data-assets/yahoo/global/silver/price_history/` only: for each of the 141 `cusip=<CUSIP>/` prefixes, the four files
  `prices.parquet`, `splits.parquet`, `dividends.parquet`, `lock.json`, and `index/index.parquet|csv`. Locally: the queue file
  `~/.opal/demque/queue/Z-STANDING-T1-EXTEND.json` and 141 pacer entries in `~/.opal/demque/pacer.json`. No other firm's bucket or prefix; no
  code, schedule, IAM or portal object.
- **Rollback per key:** the bucket has versioning `Enabled` (read 2026-10-11). BEFORE the run the issuer saves, for every object above, its
  current `VersionId` and body to `deliverables/2.0.0_SA_COO~Q1/R9_PRE_EXTENSION_SNAPSHOT/` (the receipt names the path). Restore = `PutObject` of
  the saved body (or copy-object of the saved VersionId) per key; the local files are removed (queue file) and `pacer.json` is restored from a copy
  taken first. The first restore command is printed in the receipt.

## 4. The expected outcome, from the producers' own rules (N rules read: 4)

Rules read: `lock.check` (:67-111, incl. `_proved_through` :58-65), `price_store.write` (:112-141), `daily_draw.on_result` (:74-98),
`yahoo_pull.Pacer` (:144-217). Window of the new request: `[earliest valid_from, frontier]`, frontier = `expected_last_trading_day(local date)`
(2026-10-09 if run on 2026-10-11, 2026-10-12 on the Monday).

Per name, ONE of these branches (a name is never in two):

| branch | condition (the rule) | served effect |
|---|---|---|
| A. LOCKED, claim `held` | agreement >= 90 pct and an agreeing observation in the first third of `[vf, frontier]` (:105-106), AND `valid_to` > the name's `trades_through` (:60-65) | the three files are REWRITTEN to the frontier; `lock.json` carries `trades_through` (DQ-t-38) and claim `held`; rows dated up to the prior end are written from the same Yahoo pull |
| B. LOCKED, claim `held`, no trades | no trade rows for the name (:94) | same as A; `trades_through` null |
| C. REJECTED (`LOW_TRADE_AGREEMENT` / `PRICE_MISMATCH`) | agreement < 90 (:108) or no agreeing observation in the extended first third (:110) | `write` returns `written: false` (:116): the existing files and `lock.json` are UNTOUCHED |
| D. pull not OK (`FAILED_EMPTY`, `FAILED_REFUSED`, `STOPPED_PUSHBACK`) | `write` :118 | untouched; the pacer records the outcome; a pushback stops the day (`allow` :200) and later names are not processed |

- **Why no name moves from C to A:** the client's trades end 2026-06-22 (`trades_through`, D1-S11), so no new observation enters any name's
  agreement; the 14 held names stay C and the 127 stay A/B, except a name whose first agreeing observation lies after the extended first third
  (`early_end` moves later by about a third of 76 trading days): that name goes A -> C and its file is untouched. The count is printed after the run.
- **What can differ in an A file for dates already served:** `as_traded_close` is byte-identical; `close_served`, `cash`, `total_return` and the
  `splits.parquet`/`dividends.parquet` rows change only where Yahoo reports a split or dividend inside the 76-day tail or restates one inside the
  old range. The issuer counts changed rows against the snapshot and prints per-name counts; a file with FEWER rows than before (a vendor that
  dropped history) is restored from the snapshot the same turn.
- **Pacer:** about 141 requests at 8 to 12 s (about 20 to 28 minutes), under the daily cap of 400. A pushback leaves the remaining names untouched
  (branch D), never half-written.

## 5. Overrides and manual paths (covered, or they do not land)

- `extend_frontier.py --today D`: refused when `D` is after the local date (:75-77, DQ-t-37) and when its frontier is before the store's latest
  `valid_to` (:81-83, DQ-t-36); both before anything is written. `--root`, `--state`, `--queue` redirect to other roots (tests); the issuer uses none.
- `OPAL_TX_PARTITION` (DQ-t-30) pins an older transactions partition: it can only move `trades_through` earlier, so claims go `held`, never
  `measured` (the narrowing direction). Not used.
- `price_store.write` is also reachable by `daily_draw.py --store <local root>`; that writes a local root, not this property.

## 6. Conditions

1. The pre-extension snapshot (section 3) exists, with its path in the receipt, BEFORE the run.
2. After the run, printed with denominators: files written (A+B), untouched (C+D), per-name changed-row counts against the snapshot, files with
   fewer rows than before (expected 0, each restored), `max(date)` per written file against the frontier (141 of 141 for the names written),
   the pacer outcomes by status.
3. The written `lock.json` carries `claim` `held` and `trades_through`; none reads `measured` with `valid_to` past `trades_through`.
4. The schedule is read as DESIRED (`run_daily_draw.sh`) and APPLIED (the task's last run result) after the first scheduled 22:30 run; the
   `comp-freshness` entry for the store carries `freshness_basis: trading-day-frontier`.
5. Residuals named, not accepted away: the readers of section 2; whether `silver/historical_prices.parquet` (FWD-1's last hop) will later put
   these files on a page (round 10 cell 1).

## 7. What this half does not cover

Any run with a different `--root`/`--state`/`--queue`; any run before the pre-snapshot; the 14 names' `held` records (their own half, applied);
the transactions store's freshness (cross-fabric, MSTR to MSTR, not a round-9 condition per ADDENDUM 1).
