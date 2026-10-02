# Never-widen half, MDPF_SECCLASS -- the BD re-land residual, first per-ticker act: 36 CUSIP rows by peer (CTO batch 161)

**Author:** `2.0.0_SA_COO~M`, 2026-10-02 12:3xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO`, second half.
**Status: COO half SIGNED; CTO half asked; NOT RUN.** Batch 161: "the private funds in the residual go to the next per-ticker act,
in dollar order."

## Population and dispositions

The re-land residual (`R8_CHECKS/R8_BD_RELAND_RESIDUAL_BY_NAME_20260930.csv`, 767 names, 86,480,584.86 USD) splits: no CUSIP in the
lots 13,541,021.49; several CUSIPs per name 8,998,711.41; VANGUARD MORNINGSTAR GROWTH ETF 35,784,712.98 (the guard, row S14); and
**648 names with one valid CUSIP (check digit), 28,156,138.98**. The first act takes those in dollar order to 80 percent: **68 names,
22,562,299.27 USD** (`R8_CHECKS/R8_RESIDUAL_FIRST_ACT_68_20261002.json`). Each name is read by kind from its custody name (INFERRED;
no vendor called) and given one disposition in `R8_CHECKS/build_residual_cusip_set.py` (`PLAN`, `NOT_WRITTEN`):

| disposition | rows | USD | ground |
|---|---|---|---|
| WRITE, the same security as a ticker row | 5 | in the 12.05 M | VB, VO, VOE, VVIAX, BAC: the CUSIP is that ticker's; the row copies it |
| WRITE, peer of its kind | 25 | in the 12.05 M | ETFs and mutual funds (IVV, IJH, IJR, VEA, ACWI, AGG, VCSH, BNDX, HYG, JEPI peers), 529 pools, one municipal bond (MUB), two non-traded REITs (VNQ) |
| WRITE, ruled pair structured / Hedge | 6 | in the 12.05 M | structured notes (Barclays, JPMorgan, Morgan Stanley, BBVA zero-coupon and outcome notes) -- the kind batch 145 B ruled structured / Hedge for buffer ETFs |
| **all WRITE** | **36** | **12,053,436.96** | |
| NOT, allocation | 12 CUSIPs | in the 10.51 M | batch 145 C |
| NOT, private credit / alternative with no peer of its kind | 6 | in the 10.51 M | Cliffwater Corporate Lending (2.61 M), Blue Owl Credit Income, Variant Alternative Income, ACAP Strategic, Kensington Managed Income, Blackstone Private Credit -- batch 145 C's XCAPX/NICHX rule |
| NOT, IBIT | 1 | | batch 145 D |
| NOT, single stock with no ticker row of its own | 8 | | SpaceX, Nebius, USA Compression Partners, Angel Studios, UWM, Invivyd, Honeywell Aerospace, Elixirr: the table classes single stocks two ways (legacy by sector, seed by size; row S8's split), so the sub class is not settled |
| NOT, kind not readable from the name | 2 | | Prospera Income ETF; NH Total Market Index |
| **all NOT** | | **10,508,862.31** | |

## The act

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/write_cusip_rows.py --set-file
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/RESIDUAL_CUSIP_WRITE_SET_20261002.tsv --write`, once (the CUSIP
writer signed for the 29 Cottonwood CDs, batch 108: conditional put, `classified_by: scheduled`, `updated_by: mdpf-secclass-cusip-rows`).
Dry run against the live table, 12:3xZ: `named=36 plan=36 already_present=0 refused=0 (table rows=2805)`. Stops: the dry run reads
anything else; the set file differs from the blob this file names at commit.

## Served effect

**None today:** no reader keys a Black Diamond position by CUSIP until the r3 re-land (its identity read takes a `CUSIP:` row first);
the Holdings tab looks up by ticker; the comparison list drops `CUSIP:` rows. **At the re-land:** 49 Financial's unclassified on the
09-30 positions falls from 4.63 to **3.99 pct** (12,053,436.96 USD of 1,866,381,354.90 move from `unclassified` to the rows' classes).

## Rollback, acceptance, ledger

A corrected row by the same writer; a `delete-item` stays Andrew's. Acceptance: 36 read back, table 2,841, a second dry run
`plan=0 already_present=36`; served at the re-land's leg R. Ledger `secclass-bd-residual-cusip-rows-m-<date>`; legs W, R.

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-02 12:3xZ)

Signed on: 36 new `CUSIP:` rows, none touched, no served move until the re-land; the 32 names not written are listed with their
reason. Read at signing: the residual census, each of the 68 names, the peers' live rows, the dry run.
