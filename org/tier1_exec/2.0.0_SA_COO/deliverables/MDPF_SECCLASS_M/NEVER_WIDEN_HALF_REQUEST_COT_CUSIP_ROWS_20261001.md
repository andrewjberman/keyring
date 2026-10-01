# Never-widen half, MDPF_SECCLASS -- the Cottonwood CUSIP rows (CTO rulings batch 93 item 2): 29 bank CDs as `CUSIP:` rows

**Author:** `2.0.0_SA_COO~M`, 2026-10-01 18:4xZ (FAST lease `MDPF_SECCLASS`). **For:** `1.0.0_SA_CTO`, second half.
**Status: DRAFT -- neither half signed; the act is NOT RUN; the writer is NOT BUILT.** A precondition of the Cottonwood re-point
(`NEVER_WIDEN_HALF_REQUEST_COT_REPOINT_20261001.md` @1ffbf6a639).

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

## The writer (to build before signing)

Neither existing path writes these: the seed script skips `CUSIP:` rows, and Cottonwood's `E_18` plans real tickers only. The
writer is the conditional put Black Diamond's `E_18` uses for its own `CUSIP:` rows (`etf_classification_scheduled.write`,
`attribute_not_exists(ticker)`, so no existing row is touched), driven by a dry-run-first script on the `write-model-rows.py`
pattern, with `classified_by: scheduled` as the peers carry. Stops: the dry run must plan exactly these 29 keys, 0 present.

## Served effect

Cottonwood gold: none until the re-point ships (its host reads no table today). After it: 3,005,499.29 USD of bank CDs read
fixed_income instead of unclassified. Holdings tab and Black Diamond gold: a point lookup by these keys only; neither keys a
Cottonwood position by CUSIP today -- to be measured before signing.

## Rollback

A corrected row by the same writer path; removing a row is a delete-item, which needs Andrew's word.

## COO half -- NOT SIGNED (the writer, its dry run and the served-effect read come first)

## CTO half -- NOT SIGNED
