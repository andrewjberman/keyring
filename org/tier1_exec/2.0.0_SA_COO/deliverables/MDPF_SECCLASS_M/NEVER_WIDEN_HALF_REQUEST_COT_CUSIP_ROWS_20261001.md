# Never-widen half, MDPF_SECCLASS -- the Cottonwood CUSIP rows (CTO rulings batch 93 item 2): 29 bank CDs as `CUSIP:` rows

**Author:** `2.0.0_SA_COO~M`, 2026-10-01 18:4xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO`, second half.
**Status (2026-10-02 03:4xZ): BOTH HALVES SIGNED (CTO `CTO_HALF_SECCLASS_COT_CUSIP_ROWS_20261002.md`, batch 108, on blob
`56a1db3d3e`); WRITTEN 03:40:18Z, 29 of 29 read back, table 2,719; ledger `secclass-cot-cusip-rows-m-20261002` leg W closed, leg R
held on the re-point's served leg.** (Body below is the signed text.) A precondition of the Cottonwood re-point (`NEVER_WIDEN_HALF_REQUEST_COT_REPOINT_20261001.md`
@1ffbf6a639). The other precondition, the 19 seed rows, is WRITTEN (2026-10-02 02:12Z, ledger `secclass-cot-seed-rows-m-20261001`).

## What item 2 covers, measured (2026-09-30, read-only; script scratch `cot_cusip_gap.py`)

Cottonwood gold positions with a value, no ticker, not flagged cash, and a CUSIP from the silver row (row-for-row aligned):
338 rows, 30,283,675.30 USD. A `CUSIP:` row already exists for 258 rows (22,792,036.13 USD). **Lacking: 80 rows, 7,491,639.17 USD,
74 identifiers** -- and they are two different things:

- **43 identifiers, 48 rows, 4,470,036.55 USD are NOT CUSIPs.** 42 of the 43 are 8-character Black Diamond identifiers (`BD4HOKI9`,
  `BDGG24WF`, ...) carried in the `cusip` column, on fund units and retirement-plan funds ("Voya Index Solution 2050", "EXTENDED
  MARKET UNITS"). Writing them as `CUSIP:` rows would put a vendor identifier in the CUSIP namespace. Batch 93 item 3: a
  vendor-identifier namespace arrives as a proposal with the four-postulate record, or not at all. **Not in this act; they stay
  unclassified** (part of the re-point's named residue).
- **31 identifiers with a CUSIP's shape (9 characters, check digit position numeric), 32 rows, 3,021,602.66 USD:** 29
  brokered bank certificates of deposit and 2 old mortgage-backed bonds.

## The act: 29 new items in `etf-classifications`, each `ticker: CUSIP:<cusip>`, `asset_class: fixed_income`, no sub class

The ground of each row: Cottonwood's custody name, which states an issuing bank, a coupon and a maturity year; and the table's
own rows of the same kind -- **8 bank-CD `CUSIP:` rows already read fixed_income with no sub class** (e.g. `CUSIP:66476QFV5`
"NORTHERN BANK & 3.95%26", `classified_by: scheduled`). These follow them exactly. INFERRED from the name; no vendor called.

| CUSIP | ground: Cottonwood's custody name | USD on Cottonwood gold | row |
|---|---|---|---|
| 98970LTE3 | ZIONS BANCORPORATION NATL ASSN 3.95% 2026 | 253,141.58 | fixed_income / (none) |
| 90983WCD1 | UNITED CMNTY BK CHATHAM ILL 4% 2027 | 250,701.92 | fixed_income / (none) |
| 31986HAK1 | FIRST COMM BK LEWISBURG TENN 3.65% 2027 | 248,652.50 | fixed_income / (none) |
| 5380366P4 | LIVE OAK BKG CO NC 3.75% 2027 | 200,334.44 | fixed_income / (none) |
| 38150V5M7 | GOLDMAN SACHS BK USA 3.8% 2027 | 199,413.84 | fixed_income / (none) |
| 88269ACU0 | TEXAS SEC BK DALLAS TEX 4.3% 2028 | 148,737.84 | fixed_income / (none) |
| 726547CS9 | PLAINS ST BK TEX 3.9% 2027 | 125,086.13 | fixed_income / (none) |
| 139805CS2 | CAPITAL BK N A ROCKVILLE MD 3.9% 2027 | 124,711.78 | fixed_income / (none) |
| 31749TDB0 | FINANCIAL FED BK MEMPHIS TENN 4.15% 2028 | 123,971.01 | fixed_income / (none) |
| 06051YBM1 | BANK OF AMERICA NA 4.1% 2027 | 100,732.08 | fixed_income / (none) |
| 32110YH99 | FIRST NATL BK AMER EAST LANS 4.9% 2026 | 100,246.82 | fixed_income / (none) |
| 05612LHS4 | BMW BK NORTH AMER SALT LAKE CI 3.7% 2028 | 99,859.47 | fixed_income / (none) |
| 38151PFA4 | GOLDMAN SACHS BK USA 3.7% 2028 | 99,769.92 | fixed_income / (none) |
| 949764XN9 | WELLS FARGO BANK NATL ASSN 4.15% 2028 | 99,260.03 | fixed_income / (none) |
| 31985HDE3 | FIRST COMMERCE BANCORP INC 3.65% 2028 | 98,784.00 | fixed_income / (none) |
| 38151PET4 | GOLDMAN SACHS BK USA 3.6% 2027 | 75,221.45 | fixed_income / (none) |
| 220802AV4 | CORTRUST BK MITCHELL N A SOUTH 3.7% 2028 | 74,243.60 | fixed_income / (none) |
| 61768E3Z4 | MORGAN STANLEY PRIVATE BK NATL 4.9% 2027 | 71,459.54 | fixed_income / (none) |
| 06051X3R1 | BANK OF AMERICA NA 3.75% 2027 | 61,211.24 | fixed_income / (none) |
| 38151PCW9 | GOLDMAN SACHS BK USA 3.7% 2027 | 50,187.84 | fixed_income / (none) |
| 05612LBD3 | BMW BK NORTH AMER SALT LAKE CI 3.9% 2027 | 50,125.36 | fixed_income / (none) |
| 31925YDG4 | FIRST BANK OF THE LAKE 3.95% 2027 | 50,058.90 | fixed_income / (none) |
| 434207AA4 | HODGE BK & TR CO LA 3.5% 2027 | 49,531.29 | fixed_income / (none) |
| 554479FC4 | MACHIAS SVGS BK ME 4.2% 2028 | 49,515.85 | fixed_income / (none) |
| 05612LHJ4 | BMW BK NORTH AMER SALT LAKE CI 3.75% 2029 | 48,958.72 | fixed_income / (none) |
| 335857EJ3 | FIRST OKLA BK JENKS OKLA 3.95% 2029 | 48,495.93 | fixed_income / (none) |
| 46659CHT0 | JPMORGAN CHASE BK N A 4% 2030 | 47,909.98 | fixed_income / (none) |
| 5380366N9 | LIVE OAK BKG CO NC 3.75% 2027 | 35,023.88 | fixed_income / (none) |
| 38151PLX7 | GOLDMAN SACHS BK USA 3.95% 2028 | 20,152.35 | fixed_income / (none) |

Not written (no peer row of its kind; the table holds 0 mortgage-backed `CUSIP:` rows):

| CUSIP | name | USD | |
|---|---|---|---|
| 76114BAG3 | RESIDENTIAL ASSET 2006-A14CB 20361225 6.00000 | 11,002.22 | NOT WRITTEN: no peer row of its kind |
| 02147XAJ6 | CWALT INC 2006-32CB 20361125 6.00000 | 5,101.15 | NOT WRITTEN: no peer row of its kind |

## The writer -- BUILT

Neither existing path writes these: the seed script skips `CUSIP:` rows, and Cottonwood's `E_18` plans real tickers only.

- **Script:** `MDPF_SECCLASS_M/R7_CHECKS/write_cusip_rows.py` (blob `6dfcd7fc75`), on the `write-model-rows.py` pattern, kept
  in this seat's own folder as the 2026-09-30 CUSIP act's script was (`R5_CHECKS/r5_cusip_rows_act.py`); `yang_pipeline/` is not
  this lane's to commit. It reads an
  operator-named set file and never derives a plan; DRY RUN by default; `--write` lands the plan through
  `etf_classification_scheduled.write()`, the conditional put Black Diamond's `E_18` uses for its own `CUSIP:` rows
  (`attribute_not_exists(ticker)`); it issues no PutItem of its own and has no overwrite and no delete path. Each row:
  `ticker: CUSIP:<cusip>`, `identifier_namespace: CUSIP`, the line's class (no empty sub class written), the custody name,
  `classified_by: scheduled` (as the 8 peers carry), `updated_by: mdpf-secclass-cusip-rows` (the peers carry
  `mdpf-secclass-scheduled`; the distinct value names this writer path). Any refused line stops `--write` before the first put.
- **Test:** `MDPF_SECCLASS_M/R7_CHECKS/test_write_cusip_rows.py` (blob `e3bccd5c47`), 10 passed: an 8-character Black Diamond
  identifier, a masked CUSIP, a lower-case and an 8-character value are each refused; class and sub class outside the
  vocabulary, a duplicate, no name and a malformed line are refused; a present key is left alone; one refusal writes nothing;
  the put carries `attribute_not_exists(ticker)` and no `sub_asset_class` when the line has none.
- **Set file:** `MDPF_SECCLASS_M/COT_CUSIP_ROWS_WRITE_SET_20261002.txt`, generated from this file's table (no CUSIP typed by
  hand): 29 rows, 29 distinct, 3,005,499.29 USD.
- **Dry run against the live table, 2026-10-02 03:09Z and again 03:20Z from the script's final place:** `CUSIP-ROWS named=29 plan=29 already_present=0 refused=0 (table
  rows=2690)`, the 29 keys of the table above, each `fixed_income`, no sub class. **Stops before the write:** the pre-run dry run
  reads anything other than `named=29 plan=29 already_present=0 refused=0`, or at CLOUD the writer is not blob `6dfcd7fc75`,
  the set file not blob `85f1bff9a4`, or the shared put `etf_classification_scheduled.py` not blob `3e6e081e3b`.

## Served effect -- measured 2026-10-02 03:1xZ

- **Cottonwood gold:** none until the re-point ships (its host reads no table today). After it: 3,005,499.29 USD of bank CDs read
  fixed_income instead of unclassified.
- **Readers that build a `CUSIP:` key at CLOUD HEAD:** none. Repo census of the `CUSIP:` prefix over `*.py, *.ts, *.tsx, *.sh`
  (7 files): the two seed scripts and `seed_bd_securities.py` skip or guard such keys; `etf_classification_scheduled.py` and this
  writer write them; two scratch checks. `holdings_snapshot.classify_security` looks up by ticker only, and a CD has none, so the
  **Holdings tab** does not move. **Black Diamond gold** builds no `CUSIP:` key either; it holds one of the 29 (06051X3R1, one
  closed lot, 0.00 USD, `gold/holdings_lots/2026-09-25.parquet`; control: 112 of the 348 existing `CUSIP:` keys are in those lots).
- **The comparison list** (`comparison_catalogue.py:94`) drops every row whose `identifier_namespace` is `CUSIP`: it gains nothing.
- **Every other reader:** the table already holds 348 `CUSIP:` rows of this shape (written 2026-09-30), so 29 more meet no new
  shape.
- **Writers of these 29 keys:** this writer, and Black Diamond's `E_18` only if Black Diamond held one with no row (both the same
  conditional put; the first to land wins and the other is refused). The seed script skips `CUSIP:` keys.

## Rollback

A corrected row by the same writer path; removing a row is a delete-item, which needs Andrew's word.

## Acceptance

1. Right after the run: `get-item` returns each of the 29 keys with `classified_by: scheduled`, `identifier_namespace: CUSIP`,
   `fixed_income`, no sub class; the table counts 2,719 (2,690 + 29); a second dry run reads `plan=0 already_present=29`.
2. Served: the Cottonwood re-point's own acceptance (its page walk), since no reader keys these rows before it ships.

**Ledger:** one new entry, `secclass-cot-cusip-rows-m-20261002`, opened before the write; legs W (the write and its readback)
and R (read with the re-point's served leg).

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-02 03:1xZ)

Signed on the blast radius above: 29 new `CUSIP:` items, no existing row touched; no served move today (no reader keys these
rows; the comparison list drops them); after the re-point, 3,005,499.29 USD of Cottonwood bank CDs read fixed_income. Read at
signing: the writer and its 10 tests, the generated set (29 rows, 3,005,499.29 USD), the 03:09Z dry run (29 planned, 0 present,
0 refused), the `CUSIP:` reader census, the comparison list's drop rule, Black Diamond's holding of the 29. The two
mortgage-backed bonds and the 43 vendor identifiers are not written. I run only after the second signature, and stop on any
deviation this file does not name.

## CTO half -- NOT SIGNED
