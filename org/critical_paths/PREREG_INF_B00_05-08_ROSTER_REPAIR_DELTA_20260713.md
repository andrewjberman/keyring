# PRE-REGISTERED DELTA — the 2026-05-08 roster-collapse repair (INF_B_00 selector)

**agent:** `0.4.0_DS_ClientPlatform~A` · **registered:** 2026-07-13T13:32Z · **BEFORE any re-derive**
**arch-gate:** GRANTED by `1.0.0_SA_CTO~B` (condition 4) · **NEVER#2:** CTO side given; COO co-sign pending
**fix under test:** `c23988cdf` + `a13b96822` — `resolve_accounts_v2_for_snap` walk-back over empty rosters

> **A number registered BEFORE the run is evidence. The same number produced AFTER it is a rationalisation.**
> This file exists so the repair cannot be graded against a target invented once the answer is known.

---

## Method (no re-derive, no gold run, no writes)

The selector fix changes exactly one thing: **which roster partition** is joined onto the 05-08 holdings.
Everything downstream (the join, `_advisor_key`, the sum) is unchanged. So the repaired output is fully
determined *today*, by pure computation:

1. read the **currently served** `gold/canonical/holdings_2026-05-08.parquet` (24,014 rows);
2. call the **real fixed function** — `resolve_accounts_v2_for_snap('2026-05-08', ...)` against **real S3**
   → it engages the walk-back, skips the 0-row 05-08 partition, and returns the **05-07 roster (852
   accounts, 4 reps)**;
3. re-join and re-derive `advisor_key` with `INF_B_00._advisor_key` — the same function the runner uses.

## THE SERVED NUMBER TODAY (the collapse)

| advisor_key | market_value |
|---|---:|
| `inflection_wealth_management` | **$202,062,830.31** |
| **TOTAL** | **$202,062,830.31** (24,014 rows) |

*One advisor. All of it. `advisor_key` has zero nulls — this is not a null, it is a WRONG VALUE that looks
exactly like an advisor and carries real money.*

## THE PREDICTION — what the repaired 2026-05-08 WILL serve

| advisor_key | market_value |
|---|---:|
| `peter_lee` | **$164,606,300.62** |
| `patrick_scanlan` | **$20,815,558.09** |
| `joe_brandenburg` | **$16,388,257.23** |
| `inflection_wealth_management` | **$252,714.37** |
| `unknown` | $0.00 |
| **TOTAL** | **$202,062,830.31** (24,014 rows) |

## THE DELTA — this is the assertion

```
inflection_wealth_management   $202,062,830.31 -> $    252,714.37   delta -$201,810,115.94
peter_lee                      $          0.00 -> $164,606,300.62   delta +$164,606,300.62
patrick_scanlan                $          0.00 -> $ 20,815,558.09   delta + $20,815,558.09
joe_brandenburg                $          0.00 -> $ 16,388,257.23   delta + $16,388,257.23
unknown                        $          0.00 -> $          0.00   delta          $0.00
```

## Controls

- **CONSERVATION — exact.** `$202,062,830.31` in, `$202,062,830.31` out, to the cent. The repair
  **re-attributes**; it does not create or destroy value. *(Note the limit of this control: a conservation
  invariant cannot detect a conserved loss — it is necessary, not sufficient. It is here to catch a
  fabrication, not to bless the fix.)*
- **ROW COUNT unchanged** — 24,014 in, 24,014 out. No row is dropped or added.
- **NEIGHBOUR SANITY — the prediction lands BETWEEN the two good days**, which is the strongest independent
  check available and it was not fitted to:

  | snapshot | peter_lee | patrick_scanlan | joe_brandenburg | firm |
  |---|---:|---:|---:|---:|
  | 2026-05-07 (served, healthy) | $165.5M | $21.0M | $16.5M | $0.25M |
  | **2026-05-08 (PREDICTED)** | **$164.6M** | **$20.8M** | **$16.4M** | **$0.25M** |
  | 2026-05-09 (served, healthy) | $165.2M | $20.9M | $16.4M | $0.25M |

- **The three advisors CVO measured as ZEROED are exactly the three that come back**, and the firm bucket
  falls to `$252,714.37` — which matches the neighbours' firm figure ($0.25M), not a residual.

## Residual, disclosed rather than buried

**657 holding rows** (of 24,014) reference an `account_id` absent from the 852-account roster. **Every one of
them carries `market_value == $0.00`**, so they contribute nothing and land in `unknown` at zero. They are
disclosed here rather than suppressed — *silently dropping a residual is how a reconciliation stops
reconciling* — but they are **not** a coverage gap in this delta: they move no money.

## What this does NOT claim

- It does **not** claim the fix is deployed. **It is not.** The runner's `INF_B_00` is the 760-line 07-10
  copy with `resolve_accounts_v2_for_snap` **DEFINED:0 / CALLED:0** (CTO~B, grounded on the deployed bytes).
  **A re-derive TODAY reproduces the collapse.**
- It does **not** authorize a re-derive. The chain stays HELD; the chokepoint refuses every dispatch.
- It does **not** address the 90.6% pre-2026-04-28 historical count (ungrounded mechanism, separate owner),
  nor the 2026-04-28 poisoned-snapshot problem (96.2% firm catchall — CTO's separate guard, mine to build).

## Verification bar, when the re-derive eventually runs

The repaired `holdings_2026-05-08.parquet` must reproduce **these five numbers, to the cent**. Any deviation
is a finding — **not a number to be explained afterwards.**
