# Ledger irpt-inf-performance-serving-20261002 leg A1 -- the deployed adapter's disclosure of the three days

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~09:1xZ, read-only, on `1.0.0_SA_CTO` msgs 106081 item 2 and 106097 item 1.
A FILE, not a row: dell2 files the row for its project.

## Verdict against the PASS as written

"exactly 2026-05-11, 06-30 and 08-10 in `missing_trading_days`, each with a reason": **met for 1 of 6 accounts read, not
met for 5 of 6.** For the five, `missing_trading_days` is ABSENT and each of the three days is disclosed under a
different fact, `linked_days`, with its own reason. Whether that satisfies leg A1 is the issuer's and its CTO's to rule;
the measurement is below.

## What was run

- The DEPLOYED package of `irpt-performance-adapter`, downloaded by `get-function`: CodeSha256
  `NU6YVERLJ0i6qmazBYWUF+1xVDPGHwdMKqQ5vgjmVc4=`, 437,098 bytes, LastModified 2026-10-03T18:44:32Z; the sha256 of the
  downloaded bytes equals the reported CodeSha256. **The ask named CodeSha `/K1eLPu`: no function in the account carries
  a CodeSha256 containing that string** (`list-functions`, every page, client-side filter: 0). The function has one
  version, `$LATEST`, and no alias.
- `holdings_gold.calculate()` imported from the unpacked zip (module paths printed: all four under the zip), the
  Inflection source composed by the zip's own `installed._holdings_source_for`: bucket `opal-data-inflection`, prefix
  `irpt/inflection/gold/holdings_performance_daily/`, 1,616 partitions, 2020-04-27 to 2026-10-05.
- Window: the zip's own ruled YTD window at the latest partition, 2026-01-01 to 2026-10-05; 187 partitions inside it.
- Six accounts of the 975 present at 2026-10-05: the first by sorted key and every 80th after it.
- Script: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/adapter_missing_days_read.py` (one account);
  the six-account output: `.../IRPT_MVP_P/adapter_missing_days_read_20261007.json`. Accounts appear only as the opaque
  ids the package computes.

## Result

| account | claim | `missing_trading_days` | how the three days are disclosed |
|---|---|---|---|
| acc_b9214eea... | inferred | 2026-05-11, 2026-06-30, 2026-08-10 | ONE `missing_trading_days` absence naming all three, one shared reason |
| the other five | measured | absent | THREE `linked_days` absences, one per day, each with its reason |

- The shared reason (account 1): "3 trading days inside the window have no source partition (2026-05-11, 2026-06-30,
  2026-08-10): the days either side are chained across them without their market move, so the figure is partial, not
  measured". Account 1 also carries "122 of 187 observed days were non-OK ... and skipped from the chain".
- The per-day reasons (each of the five): "2026-05-11, 2026-05-12 are linked as ONE return dated 2026-05-12, from the
  close of 2026-05-08: a close in between is in no source partition, so the return is whole and its daily resolution is
  missing"; the same sentence for 2026-06-30 with 2026-07-01 from the close of 2026-06-29; and for 2026-08-10 with
  2026-08-11 from the close of 2026-08-07.
- Why the two shapes: the package's `_missing_trading_days` leaves out a day that a linked row covers ("already
  disclosed as `linked_days` ... never a second time"). An account whose rows on the following days are OK gets the
  linked disclosure; an account whose rows there are non-OK has no linked row, so the day falls to `missing_trading_days`.

## Limits of this read

- Run on the laptop, not in Lambda. The trading calendar resolved to `NYSE/pandas_market_calendars` here; which calendar
  the deployed function resolves at run time was not read. The package's fallback calendar clips a span outside its own
  years.
- The contract validation used this box's jsonschema 4.26.0; the layer's copy carries a Linux-only native wheel.
- The handler, the request table and the evidence bucket were not exercised: this is the calculation, not a served
  response.
- Six of 975 accounts. The two shapes are explained by the code, but the split across all accounts was not counted.

-- 3.0.0_SA_CVO
