# Never-widen half, MDPF_SECCLASS BD per-ticker first act -- 16 seed rows by peer (CTO rulings batches 139, 145)

**Author:** `2.0.0_SA_COO~M`, 2026-10-02 10:5xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO`, second half.
**Status: COO half SIGNED; CTO half asked; NOT RUN.** Code on side branch `coo-m-bd-seed-first-act` @23c8e4c798 (seed source blob
`1c3dbf1082`), NOT on CLOUD. Proposal and ruling: `R8_BD_PER_TICKER_FIRST_ACT_PROPOSAL_20261002.md` @06a4b47988, batch 145.

## The act (as the 19 and the 3 seed rows)

1. Merge `coo-m-bd-seed-first-act` into CLOUD (`.tools/safe-merge.sh`); it adds 86 lines to
   `infra/aws/lambda/v2_portal/_shared/etf_classification.py` (none changed) and two files in this seat's folder.
2. Run `python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` (no flag) once, from CLOUD.

| group (ruling) | ticker | row | peer | Holdings tab today (classify_security, all TABLE fallback) | USD 49F lots 09-25 |
|---|---|---|---|---|---|
| A | AWSHX | equity / US Large Cap, active fund | IVV | fixed_income / Investment Grade | 557,339.13 |
| A | MSSGX | equity / US Small Cap, active fund | IJR | fixed_income / Investment Grade | 95,349.35 |
| A | DBO | commodities / Oil | USO | alternatives / Commodities | 63,123.18 |
| A | SCHH | alternatives / Real Estate | VNQ | equity / Real Estate | 82,063.21 |
| A | TRREX | alternatives / Real Estate, active fund | VNQ | equity / Real Estate | 55,406.39 |
| A | SMA | alternatives / Real Estate, single_security | VNQ's class, WMT's form | equity / Real Estate | 77,391.73 |
| A | OIH | equity / US Large Cap (sector Energy) | XLE (the table classes sector ETFs by size) | equity / Commodities | 95,065.00 (+ Cottonwood 12,107.84) |
| B | BMAR, QMAR, FMAR, JANW, DECZ, SIXO | structured / Hedge (sector Hedge) | VXX | alternatives / Structured Notes | 518,134.64 |
| B | JHQTX | structured / Hedge, active fund (sector Hedge) | VXX | alternatives / Hedge fund | 410,564.81 |
| B | QQH | equity / US Large Cap, active fund | QQQ's row (batch 145) | alternatives / Volatility | 57,235.75 |
| D | GLDM | commodities / Metals | GLD; settled by CUSIP 98149E303 (SPDR Gold MiniShares) | alternatives / Gold | 249,137.80 |

**Holdings tab: 15 class moves (2,165,745.99 USD), 1 sub class move (OIH, 107,172.84), none unchanged** -- each from a
bd-securities label to its peer's class. Not written by ruling: the 16 allocation funds (batch 145 C), XCAPX and NICHX (no
alternatives peer of their kind: the class holds only Real Estate and International Real Estate rows), IBIT (D).

**Named residue -- GLDM's mis-ticker:** Black Diamond carries TWO securities under ticker GLDM: CUSIP 98149E303 SPDR Gold MiniShares
(18 lots, 188,264.35 USD) and CUSIP 911478105 US Global Investors Gold & Precious Metals (6 lots, 60,873.45 USD, a gold-miners fund).
The row is keyed by ticker, so the 60,873.45 reads commodities / Metals too -- a Black Diamond feed defect (the ticker on those
rows is wrong), not this row's; it is listed here, not fixed.

**Choices named:** sector Hedge (not VXX's "Volatility") for the seven B rows; management style active for AWSHX, MSSGX, TRREX,
JHQTX, QQH, passive for the index and buffer ETFs, none for SMA (a single stock, as WMT); names from the issuers' fund names.

## Checks and stops

`R8_CHECKS/test_seed_bd_first_act_rows.py` with the two earlier seed tests: 46 passed. Seed `--dry-run` from the branch against the
live table (2,789 rows): 177 tickers, 161 already correct, **16 to write**, 0 CONFLICT. Stops: (a) the seed source at CLOUD after
the merge is not blob `1c3dbf1082`; (b) the pre-run dry run reads anything but "16 of 177" naming these 16, or any CONFLICT line.

## Served effect beyond the Holdings tab

Black Diamond gold: none until r3 re-lands (pre-r3 library runs; batch 144 sets the re-land bar). Cottonwood gold: OIH after its
re-point. Comparison list: 16 more named entries at every firm (SMA a single stock, as WMT).

## Rollback, acceptance, ledger

Rollback per key: a corrected seed row; a `delete-item` stays Andrew's. Acceptance: 16 read back `seed` with the rows above, a
second dry run reads 0; served -- the next Holdings publication reads the 15 class moves at 49 Financial. Ledger
`secclass-bd-first-act-seed-m-<date>`, opened before the merge; legs M, W, S.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-02 10:5xZ)

Signed on: 16 new seed rows, none touched; on the Holdings tab 15 class moves and 1 sub class move, all from bd-securities labels to
peer classes, 49 Financial; GLDM's 60,873.45 USD mis-ticker named. Read at signing: the peers' live rows, each ticker's Holdings
answer today, the 49F lots and GLDM's two CUSIPs, the branch tests, the dry run.
