# Never-widen half request, MDPF_SECCLASS -- BD's three served classify sites reach the ticker-no-row NAME:: fallback (FWD-1, cell SC-e-87, row MDPF_SECCLASS-D1-S26)

**Author:** `0.9.0_WK_MDPF_SECCLASS~77` for `2.0.0_SA_COO~M1`, 2026-10-11 (~03:3xZ). **For:** `2.0.0_SA_COO~M1` (COO half) and `1.0.0_SA_CTO` (CTO half).
**Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been deployed or written to any bucket or table. Order `MDPF_SECCLASS.TO-SC-e87` (worktree branch `wk-MDPF_SECCLASS-77`, commit pending the COO's sign-off on the cell).

## What is wrong

The SC-e-79 lib (`lib/etf_classifier.py`, served now) places a NON-BLANK ticker with no `etf-classifications` row by its `NAME::` row (identity hop `ticker-no-row-name-key`), but only when the caller reaches `classify_with_identity`. Measured at the base, the three served sites called it ONLY for a BLANK ticker, so a ticker-no-row position never reached the branch and the 23 securities of the D1-W66-S3 list still served `unclassified`. Base dry run (2026-10-11): `SERVED-REACH site=D_04|C_06|D_03 ok=False target=('unclassified', '', '', 'unclassified') controls=3/3`.

## The fix (staged in the worktree, LOCAL, not deployed)

One change per site, nothing else. Where `classify()` returns no class and the ticker is non-blank, the site calls `classify_with_identity(ticker, name[, cusip])` and serves the returned class with class_source `etf-classifications` exactly as the blank-ticker branch does:

| site | file:line (new branch) | call |
|---|---|---|
| D_04 | `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` :170-176 (`else:` of the `if not t.strip():` block) | `classify_with_identity(t, n, c)`, `c` = the cusip the site holds |
| C_06 | `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` :235-238 (`elif not canonical_class:`) | `classify_with_identity(ticker, name)`, no cusip (as the blank call) |
| D_03 | `data/black_diamond/scripts/gold/D_03.composition_artifacts.py` :141-144 (`elif not canonical_class:` in `_classify`) | `classify_with_identity(ticker, asset_name, cusip)` |

Kept unchanged at every site: a ticker that has a row (`classify()` returns it first, never overridden); a blank ticker (its own branch, unchanged); a position with no ticker row and no `NAME::` row stays `unclassified` (the cash-keyword rule still decides `cash`).

Served bytes check (read-only, 2026-10-11): the three served code objects have the same MD5 as the base HEAD bytes of the same files (ETags below), so the deploy delta is exactly this change.

## The act (by the issuer, after both halves sign)

1. Deploy ONLY these three files to `s3://opal-data-bd/code/gold/` with `bash .tools/safe-deploy.sh data/black_diamond/scripts/gold/D_04.client_portal_summary.py data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py data/black_diamond/scripts/gold/D_03.composition_artifacts.py` (the deploy core ships only named files), under a change-management ledger opened at start and closed at completion, before the next BD gold fire.
2. Precondition, measured: the SC-e-79 lib is the served `code/gold/lib/etf_classifier.py` (VersionId `hnOzzH4QClDqa_qbd6Y5tqKu3Kag4vtM`, ETag `eb9bb85208c96fa15ede01cf3618782d`, LastModified 2026-10-09T09:54:21Z), whose MD5 equals the HEAD lib. The new site branches therefore reach the NAME:: row on the next fire. No lib file rides this deploy.
3. Read back (leg G): `platinum/firm/mix_summary.json` unclassified share, beside the candidate diff below.

## Blast radius

**Objects the act writes:** the three code objects above. No table, no data key. **Objects the next fire writes:** the set the nightly fire already writes (`gold/views/mix_daily_summary.json` from C_06, the D_03 composition artifacts, D_04's `platinum/firm/mix_summary.json` and `platinum/clients/{rid}/...`); the change is CONTENT only. **Not touched:** `etf-classifications` (read-only), the lib, any ticker that has a row, any chain-placed blank-ticker position, any ticker-no-row position without a `NAME::` row.

**Writers of the served `platinum/firm/mix_summary.json`: N = 1**, grep over `data/black_diamond/scripts/` (Grep tool, worktree path):
- `data/black_diamond/scripts/gold/D_04.client_portal_summary.py:554` -- `_write_batch([(summary, 'platinum/firm/mix_summary.json')], ...)` (the only writer; :11, :450 and :458 are docstring or listing lines).
- Not writers of this key: C_06 writes `MIX_DAILY_SUMMARY` (:411-417), D_03 writes the composition keys, and `E_25` and `test_d04_unclassified_line.py` only read or assert it.

The classify-site count for the lib is unchanged: N = 3 (C_06, D_03, D_04), each calls `classify_with_identity`.

**Local candidate diff** (this worker ran the NEW D_04 `_classify_with_canonical` against the LIVE `etf-classifications` table, read-only: `get_item` only, through the shared client's `get_classification`; no write, no query, no scan). Security-level fields only; the list is `D1W66S3_TICKER_NO_ROW_LIST_20261009.json` `entries`, dollars are its 2026-10-06 partition.

| ticker | security name | dollars | NAME:: row class (live) | class the new code returns | moved? |
|---|---|---:|---|---|---|
| LBSAX | COLUMBIA DIVIDEND INCOME A | 365,335.72 | equity | equity | yes |
| SCGE1 | LARGE CAP EQUITY MANAGED POOL | 151,435.14 | equity | equity | yes |
| SCGN1 | INTERNATIONAL EQUITY INDEX POOL | 149,833.97 | equity | equity | yes |
| TWCUX | AMERICAN CENTURY ULTRA INV | 88,936.60 | equity | equity | yes |
| SCSI1 | SHORT TERM INCOME POOL | 59,242.28 | fixed_income | fixed_income | yes |
| ASMIY | ASM INTL NV NY REGISTER SH | 27,730.24 | equity | equity | yes |
| BALCX | AMERICAN FUNDS AMERICAN BALANCED C | 23,420.00 | equity | equity | yes |
| SCGS1 | SMALL CAP EQUITY POOL | 22,958.00 | equity | equity | yes |
| SCGG1 | GROWTH POOL | 22,773.13 | equity | equity | yes |
| SCGT1 | TREASURY INFLATION PROTECTED SECS | 15,574.65 | fixed_income | fixed_income | yes |
| PFF | ISHARES PREFERRED & INCOME SECURITIES ETF | 11,808.00 | fixed_income | fixed_income | yes |
| SCGL1 | INTL EQUITY MANAGED POOL | 5,585.81 | equity | equity | yes |
| FBCVX | FIDELITY BLUE CHIP VALUE | 4,812.51 | equity | equity | yes |
| CEMVX | CAUSEWAY EMERGING MARKETS INVESTOR | 4,109.08 | equity | equity | yes |
| AEMGX | ACADIAN EMERGING MARKETS INVESTOR | 3,973.06 | equity | equity | yes |
| VWIGX | VANGUARD INTERNATIONAL GROWTH INV | 3,832.43 | equity | equity | yes |
| FIADX | FIDELITY ADVISOR INTERNATIONAL DISCV I | 2,882.52 | equity | equity | yes |
| FG | F&G ANNUITIES & LIFE INC COMMON STOCK | 1,533.60 | equity | equity | yes |
| DJT | TRUMP MEDIA & TECHNOLOGY GROUP COM | 390.26 | equity | equity | yes |
| GLPI | GAMING & LEISURE P COM | 67.24 | equity | equity | yes |
| SKYQ | SKY QUARRY INC COM NEW | 33.00 | equity | equity | yes |
| TDSC | ETC CABANA TARGET DRAWDOWN 10 ETF | 17.18 | equity | equity | yes |
| BLIAQ | BB LIQUIDATING INC CL A | 1.04 | equity | equity | yes |

Totals (printed by `.scratch/r20_e87_live_reach.py`, denominator 23): **MOVED 23 securities, $966,285.46** (equity 20 at about $879,661; fixed_income 3 at about $86,625, SCSI1, SCGT1, PFF). **STAYING 0 securities, $0.00.** Every moved row's new class equals its NAME:: row's class (mismatch count 0). The live NAME:: row for TWCUX's name reads equity, so the 10-09 candidate's fixed_income for TWCUX no longer applies; the cause (the SC-e-83 row write the 10-09 COO half asked for first) was not traced in this read.

**Both branches of the expected outcome, read from the code written:**
- A ticker-no-row security WITH a `NAME::` row: D_04 :175-176 and the C_06 / D_03 `classify_with_identity` returns (class, sub, `etf-classifications`, `ticker-no-row-name-key`), so the site serves that row's class. Measured above for all 23 (the moved branch).
- A ticker-no-row security WITHOUT a `NAME::` row: `classify_with_identity` returns `('', '', 'unclassified', 'ticker-no-row')`, the site's cash-keyword rule decides `cash` or `unclassified`, and the class is listed by name here. NONE of the 23 is in this branch today (0 staying); the branch is exercised by the test file (`tests/test_served_path_reach_r20.py`, arm "no name row stays unclassified" and "cash keyword still decides cash") and by the sites' own check (`sc_r20_served_reach.py` CONTROL2).

**Tests:** `data/black_diamond/scripts/gold/tests/test_served_path_reach_r20.py` (new): 21 pass, driving each site's own function with a stubbed table client, no AWS call. The full BD gold suite (`data/black_diamond/scripts/gold/tests`) passes, 120 of 120. Sites' own checks: `sc_r20_served_reach.py D_04|C_06|D_03` each `ok=True controls=3/3`.

**Known edge (surfaced, not changed):** a ticker literal `NAN` or `NONE` normalizes to no ticker in the lib, so it takes the blank-ticker identity chain (hop `name-key`) rather than `ticker-no-row`; recorded as a surprise row, not in this act's scope.

## Rollback per key

Read-only `bash .tools/aws s3api head-object --bucket opal-data-bd --key code/gold/<file>`, 2026-10-11:

| key | VersionId | ETag | LastModified | size | role |
|---|---|---|---|---|---|
| `code/gold/D_04.client_portal_summary.py` | `In6p3j24Ok0Vyi3LRitAAfGi0yNgcGWq` | `23d2f2ae5797834638bbda5b9e5eb584` | 2026-10-09T07:07:36Z | 164019 | CURRENT served = base HEAD bytes; **the rollback target** |
| `code/gold/C_06.client_mix_timeseries.py` | `y1QO4QB9EeDDn4jVUL6k25ZGuhqifMdm` | `d7eb83b655b63143c24552bdfff197ad` | 2026-10-08T19:20:53Z | 45269 | CURRENT served = base HEAD bytes; **the rollback target** |
| `code/gold/D_03.composition_artifacts.py` | `kAktHpSbSrN0xq0CqbIJS3eqL8F2jt6e` | `84f9bf8e9ececc0712b0a6e3f67694f4` | 2026-10-07T04:16:24Z | 41785 | CURRENT served = base HEAD bytes; **the rollback target** |

(ETags are the MD5 of the served bytes; `head-object` reads quote them.) Code rollback: `s3api get-object --version-id <VersionId>` for each key, then `safe-deploy.sh` of that file; this restores today's behaviour (ticker-no-row stays `unclassified` at the three sites). It does not restore mix content a fire already rewrote. Data rollback per key: the issuer records, before the first fire on the new code, the VersionIds of `gold/views/mix_daily_summary.json`, `platinum/firm/mix_summary.json` and each `gold/entities/clients/{rid}.json` the fire rewrites; any of them is restored to its pre-fire version. This worker did not enumerate the data VersionIds.

## COO half -- UNSIGNED

Left for `2.0.0_SA_COO~M1`. Read: the writers count above (N = 1 for `mix_summary.json`, N = 3 for the lib's classify sites), the candidate table, both branches, the precondition (served lib = HEAD lib).

## CTO half -- UNSIGNED

Left for `1.0.0_SA_CTO`. Read: the named three files only, the blast radius of 23 securities and $966,285.46 moved, the rollback per key above.
