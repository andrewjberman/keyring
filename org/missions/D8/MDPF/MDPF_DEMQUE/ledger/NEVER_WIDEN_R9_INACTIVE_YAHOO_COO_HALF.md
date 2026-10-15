# NEVER-WIDEN co-sign, ROUND 9 -- the COO half: active names Bloomberg only, every other name may take Yahoo (gate swap, `use_class` column, backfill placement)

**Signer:** `2.0.0_SA_COO~Q1` | **Date:** 2026-10-15 ~18:3xZ | **Acts covered:** (1) the MERGE of `DQ-t-66` (the Yahoo gate and tier rule) and `DQ-t-68` (the `use_class` index column), both built and held unmerged; (2) the PLACEMENT of the `YAHOO-INACTIVE-BACKFILL-NN.json` files built by `DQ-t-67` into the daily draw's queue folder; (3) the nightly runs that follow, until the backfill is drawn |
**Read against:** `priority_gate.py`, `daily_draw.py`, `extend_frontier.py`, `price_store.py`, `hold_lock_records.py` at HEAD `b3b9b93e2b`; the census of `DQ-t-64/65` (4,634 CUSIPs held, 2,929 in V2, 1,705 outside it, 1,071 of those with a symbol, 10 stored; 477 stored names are V2-held) |
**The other half:** `1.0.0_SA_CTO~DELL1`, `ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_CTO_HALF.md`. Source: Andrew-direct 2026-10-15, CTO msgs 6105 and 6114, ruling `org/missions/D8/ADVI/ADVI_COTBKF/ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` items 2 to 4 and amendment 1.

**Verdict:** SIGNED for the blast radius below, and ONLY it, once the CTO half is signed. Until then neither cell is merged and no request file is placed.

## What changes in the world

Today the Yahoo leg (the standing extension and the daily draw) leaves out the P2 and P3 names (DQ-t-52) and extends every landed name that is not in the IRPT rolling request. After the act: (a) a name in V2 is never drawn or extended on Yahoo; (b) every other name, P1, P2 or P3, may be; (c) a landed name enrolled in no tier joins the ROLLING cohort instead of the daily tier (without this the day's request passes 380 once ~1,000 names land, and the nightly extension, which fails the whole run loudly, would stop it); (d) the index gains `use_class`; (e) up to 1,071 new names are drawn over several nights.

## The `use_class` column, with its TAXONOMY LAW record

Values: `NOT_FOR_ACTIVE` (the row's CUSIP is in V2) | `INACTIVE_USE` (it is not). A separate column, not a value of `porting_verdict` (parity) or `claim` (measured/inferred/held/absent).
- (i) MECE over a DECLARED domain: the domain is the index rows; the partition is V2 membership; no row falls outside (AC2 of `DQ-t-68` counts both sides independently and they sum to `rows`). Token census: `use_class`, `NOT_FOR_ACTIVE` and `INACTIVE_USE` returned 0 hits in `*.py *.ts *.tsx *.js *.json *.yaml *.tf *.sh` over the repo before the cell (13 hits, all in the cell's own check file).
- (ii) SAME GRAIN: one value per CUSIP row. (iii) INTENT COHERENCE: one axis, who may use a price. (iv) STATE COHERENCE: a `PASS` porting verdict does not move a V2-held name out of `NOT_FOR_ACTIVE`; the porting test calibrates the INACTIVE prices only (ruling item 5); the remedy for a `NOT_FOR_ACTIVE` row is Bloomberg replacing it, not a verdict.
- **Fail closed:** an unreadable V2 set writes `NOT_FOR_ACTIVE` for every row.

## What the act MAY touch (the whole permitted set)

| keys | what moves | bound | rollback |
|---|---|---|---|
| `s3://opal-data-assets/yahoo/global/silver/price_history/index/index.parquet` and `.../index.csv` | one new column and new rows (one per newly landed name); every existing column and row unchanged | 2 keys; rows 538 today, at most 538 + 1,071 | the newest S3 version older than the run start (versioning **Enabled**, read today with `get-bucket-versioning`) |
| `.../cusip=<C>/prices.parquet`, `splits.parquet`, `dividends.parquet`, `lock.json` for a NEW name | created only when the name's identity lock reads LOCKED (`lock.check`); a REJECTED or UNRESOLVED name writes nothing to the store | at most 1,071 names x 4 keys; the draw's own list of keys written is the receipt | each key is NEW, so rollback is deleting the version the run created: an S3 delete, which waits on a human confirmation per CLAUDE.md |
| the existing `cusip=<C>/` keys of the 10 stored inactive names | extended as today | as today | newest version older than the run start |

**No `cusip=<C>/` key of a V2-held name moves**: the 477 stored V2-held names are left out of every tier, so their series stop at their present `valid_to` and stay stored (ruling item 4). The queue folder on the box (`~/.opal/demque/queue`) gains the placed request files; it is local state, not the store.

## Writers of the named property, counted

The property is "the keys under `yahoo/global/silver/price_history/`". **N = 4 writer functions in 2 files**: `price_store.write` (`.put` at `price_store.py:169-170`), `price_store.write_incremental` (`:212-222`), `price_store.write_index` (`:295-296`), `hold_lock_records.py:71` (`lock.json` only). The first three are reached from `daily_draw.py` (`on_result`, `on_incremental`, the closing `write_index`); `hold_lock_records` is a separate CLI this act does not call. The WRITE RULE of each: a price key lands only after `lock.check` returns LOCKED and only up to that lock's `valid_to`; `write_index` rewrites the two index keys from the store's `lock.json` files. **The Yahoo TARGET SET has two writers of the queue**: `extend_frontier.apply` (the one standing request, rebuilt each trading day from the tiers this act changes) and `redraw_stale.enqueue` (one tier-2 reset request, unchanged); the placed backfill files are a third input, the issuer's one act.

## Both branches named

- **V2 readable (today):** the gate is the V2 set; the day's standing request omits V2 names; the backfill files draw in rank order, tier 2, behind the tier-1 standing request, at the pacer's 380 a day (the `DQ-t-64` census prices one pass at 1,071 requests, three nights when nothing else draws, more with the standing request ahead of it).
- **V2 unreadable or its sha256 differing:** `yahoo_excluded_for` raises `GateUnreadable`; the daily draw refuses before any pull and the extension plan refuses; the run exits non-zero and NO store key moves. The index writer, reached only from a completed draw, writes `NOT_FOR_ACTIVE` for every row if it is ever reached with the set unreadable.
- **A name's identity lock rejects:** it is not written, it enters the unresolved list as today, and it is not retried within the night.
- **The pacer cap ends a night mid-backfill:** the draw stops at the cap, records the request PARTIAL (as it did for the IRPT P1 request on 2026-10-13: 29,124 of 81,270 cells) and resumes it the next night; a name not drawn writes nothing.
- **A P2 holder later matches into V2:** its names are then in V2, leave the Yahoo tiers at the next plan, and join ADVI_COTBKF's Bloomberg need (CTO amendment 1); the stored Yahoo price stays and reads `NOT_FOR_ACTIVE`.

## The consumers, and what the act changes in each

| consumer | what it reads | change |
|---|---|---|
| `data/assets/scripts/silver/commonwealth_price_need.py` (ADVI_COTBKF; reads `index.parquet`, already carries `demque_claim` and `porting_verdict`) | the index by column name | an extra column is ignored today; it does not yet carry `use_class` downstream: a **named gap**, a cell of ADVI_COTBKF, not closed here. Until it lands, its output does not say a Yahoo price is `NOT_FOR_ACTIVE`; the ruling's guard that a Yahoo price never feeds an ACTIVE account's return rests on that project reading the column. |
| `extend_frontier.py`, `daily_draw.py`, `p1_coverage.py`, `porting_test.py`, `lag_report`, `redraw_stale.py`, `incremental_*`, `batch_*` (inside the DEMQUE folder) | the index and per-CUSIP files | each reads by column name; the 9 test files that mention the gate are updated only where they pin the old P2/P3 rule; the whole folder (228 passed on the merged tree) must pass before the merge, and the pair is not honoured if it does not. |
| `commonwealth_daily_valuation.py` (reads `splits.parquet` version-aware) | per-CUSIP `splits.parquet` at an `as_of` | **nothing for a V2-held name** (no key of one moves); new names are not held by any V2 account. |
| the portal, any TypeScript or Terraform reader | 0 files match the store prefix (counted before this act) | nothing |

**Limit:** the repo is the population measured, not the AWS account; a notebook or a reader outside the repo would not appear.

## What the act may NOT touch

Any Bloomberg draw, request or quota; the V2 file; the P2/P3 gate on the Bloomberg side; `claim`'s value set; `porting_verdict`'s; any `cusip=<C>/` key of a V2-held name; the identity-lock rule (no looser rule, CTO msg 5411 stands); a daytime run (the nightly run is the only Yahoo draw; the pacer's cap is unchanged at 400, 380 for the standing request).

## Order of the act, and its stop

1. CTO half signed. 2. `DQ-t-66` and `DQ-t-68` merged (the issuer, through `safe-merge.sh`), the folder green. 3. A ledger entry opened in `org/critical_paths/change_management/` for the run window. 4. The backfill files placed in the queue after a `--plan` read shows the gate and the cap. 5. The first run's receipt read against the store's version list (as the 2026-10-14 run was). **Stop:** a run that exits non-zero or writes a key not in the table above is the stop; the queue files are removed and the entry closed with the finding.

-- `2.0.0_SA_COO~Q1`
