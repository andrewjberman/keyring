# NEVER-WIDEN co-sign, ROUND 9 -- the COO half, pair B: label Yahoo-sourced client prices UNVERIFIED until the porting test passes

**Signer:** `2.0.0_SA_COO~Q1` | **Date:** 2026-10-13 ~22:1xZ | **Act covered:** a not-yet-cut order (`DQ-t-59`) that adds ONE column, `porting_verdict`, to the store's index |
**Read against:** `price_store.py` (`INDEX_COLS`, `index`, `write_index`) at HEAD `38d4309537`, and the consumer lines named below |
**The other half:** `1.0.0_SA_CTO~DELL1`, `ledger/NEVER_WIDEN_R9_YAHOO_B_CTO_HALF.md`. Source: Andrew-direct 2026-10-13, CTO msg 5245 (print the consumer list first).

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## The shape, and why it is not the `claim` field

Andrew's rule: a Yahoo client price reads UNVERIFIED until it passes the porting test. The index already has a `claim` column. **The label does NOT go there:** `claim` carries the measured / inferred / held / absent family (CLAUDE.md, a value must carry its claim), and a new value in an existing enum is a
value-enum proposal that needs its four-postulate record and a word-boundary census (TAXONOMY LAW). A separate column avoids that. The act adds **`porting_verdict`** to `INDEX_COLS` with values `UNVERIFIED` (default) | `PASS` | `FAIL` | `UNTESTABLE`, filled at `write_index` time from
a verdicts file that the porting-test comparator (`porting_test.compare`) writes after the Bloomberg draw. No verdicts file means every row reads `UNVERIFIED`, which is the true state today: the porting-test request (326 CUSIPs, 3,195 cells) is filed and not yet drawn.

## What the act MAY touch (the whole permitted set)

| key | what moves | measured after | rollback |
|---|---|---|---|
| `s3://opal-data-assets/yahoo/global/silver/price_history/index/index.parquet` | one new column; every existing column and row unchanged | column list = old list + `porting_verdict`; row count 326 | newest S3 version older than the run start (versioning **Enabled**, read today) |
| `.../index/index.csv` | the same column | same | same |

**2 keys.** No `cusip=<C>/` key moves: `prices.parquet`, `splits.parquet`, `dividends.parquet` and `lock.json` are not touched by this pair. The verdicts file is written by the porting-test cell to a repo path, not to the store.

## Writers of the named property, counted

The property is "the index's columns". **N = 1 writer**: `price_store.write_index` (`.put(` for `index/index.parquet` and `index/index.csv`, `price_store.py:181-182`), called by `daily_draw.py:137` and by `price_store.main`. No new writer is added; `write_index` reads one more input.

## The consumers of the index and the stored files, and what the label changes in each

Counted by native Grep for `import price_store`, `INDEX_COLS`, `index\.parquet`, `index\.csv` and the literal `yahoo, global, silver, price_history`, over every `*.py`, `*.ts`, `*.tsx`, `*.js`, `*.tf`, `*.yaml`, `*.sh`, `*.cmd` in the repo (the non-Python extensions returned 0 files).

| consumer | what it reads | what an added `porting_verdict` column changes |
|---|---|---|
| `data/assets/scripts/silver/commonwealth_price_need.py:68,158-160` (ADVI_COTBKF's price need) | `index/index.parquet`; reads `cusip`, `valid_from`, `valid_to`, `claim` by name | **nothing now** (extra column ignored). It carries `demque_claim` to its output; it does not yet carry the verdict. Carrying it is a later cell of that project, named here, not done. |
| `data/assets/scripts/silver/commonwealth_daily_valuation.py:469-535` | `cusip=<C>/splits.parquet` only, version-aware at a named `as_of` | **nothing** (no key it reads moves). |
| `data/mdpf/scripts/demque/land_cot.py:150,279` (the lander to `opal-data-cot`) | `as_traded_close` from a directory of `<SYMBOL>.parquet` the caller passes with `--prices`; not the store's index | **nothing** (no price key moves, and it does not read the index). It does not read a verdict, so landed prices are NOT labelled downstream; that is a named gap, not closed by this pair. Whether the `--prices` directory is a copy of the store is the caller's act, not measured here. |
| `porting_test.py:273`, `priority_gate.py`, `p1_coverage.py`, `secclass_sync.py:210`, `extend_frontier.py` (3 reads of `ps.index`), `lock_cause.py`, `redraw_stale.py`, `incremental_plan.py`, `incremental_equal.py`, `batch_*.py` | the index and per-CUSIP files, inside the DEMQUE folder | **nothing if each reads by column name**; `test_demque_store.py:64` pins the column list and is updated by the order. The order runs the whole folder's tests (198 today) and the pair is not signed if any importer breaks. |
| `index/index.csv` | read by `price_store` and its test only (0 other files) | the extra column in the csv. |
| the portal / any TypeScript or Terraform reader | 0 files match the store prefix | nothing. |

**Limit:** a reader that builds the S3 address through `lib.opal_naming.address()` with a table name typed in a non-listed extension, or a notebook outside the repo, would not appear; the repo is the population measured, not the account.

## Both branches named

- **Verdicts file absent (today):** every row reads `UNVERIFIED`. Signed: that is the true state and changes no number a consumer reads.
- **Verdicts file present, a name `PASS`:** its row reads `PASS`; `FAIL` or `UNTESTABLE` read as such. Signed: the column changes, no price does. A name with no verdict row reads `UNVERIFIED`.
- **Verdicts file unreadable or malformed:** `write_index` writes `UNVERIFIED` for every name and says why in its output; it never writes `PASS` on a read it could not complete (fail closed).

## What the act may NOT touch

Any `cusip=<C>/` key; `claim`'s value set; any consumer's code; the porting-test request or the Bloomberg draw; the verdicts file's content (written only by the comparator). The label is not "the price is wrong": it says the price has not been checked against Bloomberg.

-- `2.0.0_SA_COO~Q1`
