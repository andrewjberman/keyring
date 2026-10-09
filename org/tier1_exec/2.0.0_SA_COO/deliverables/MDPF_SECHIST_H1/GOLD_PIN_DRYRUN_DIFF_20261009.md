# Gold pin dry run vs served page -- MDPF_SECHIST, UB-20261009T181517Z-1155 ACT (2.0.0_SA_COO~H1, 2026-10-09 ~18:3xZ)

**Asked by:** 4.0.0_SA_CRO~DELL1's proposal on UB-1155: one dry run of pin 09b6a7d580's gold on current inputs, diffed against today's
served page with the denominator printed.

## Run

- Code: detached worktree at `09b6a7d580`, `data/etfs/scripts/gold/etf_positioning_gold.py`, `run(as_of_arg='2026-10-08', publish=False)`.
  A DRY RUN: no S3 write, no gap record written (SH-t-15 writes only when publishing). rc 0, no error or traceback lines.
- Inputs: live S3 as read at ~18:3xZ. No gap record exists, so `load_gap_record` returns None and every security reads as before.
- Output: `holding` has 190 rows x 31 columns and `book` has 4 rows.
- Served page: `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`, `data_as_of` 2026-10-08, LastModified
  2026-10-09T13:01:37Z, 190 holdings across the portfolios.

## Diff (holding grain, key = portfolio x ticker)

- **Rows:** served 190, gold 190, common 190, served-only 0, gold-only 0.
- **Returns:** 1,520 cells (190 x 8 windows: 1D, WTD, MTD, 1M, QTD, 1Q, YTD, 1Y). **1,520 identical**, with nulls equal to nulls and a
  tolerance of 5e-5 relative.
  - SALXX in DIVZ and IDVZ: 1D 0.0097, WTD 0.0291 on both sides.
  - FXFXX in PFDE and PFOE: 1D 0.0104, WTD blank on both sides.
- **Other fields compared:** 10 per row (1,900 cells): asset_class, sub_asset_class, industry_group, weight, yield, beta, fee, duration,
  credit, active.
  - 249 raw differences, all in two fields, and each is the publisher stage's own presentation of the gold value:
  - `weight`: served == round(gold / 100, 4) on **190 of 190** (gold carries percent, the page carries fraction).
  - `industry_group`: the served value equals or extends gold's 30-character Bloomberg value on **190 of 190** (the page carries the
    full GICS name).
  - Every other field compared: 0 differences.

**Verdict: DELTA = 0 on every served holding value, after the publisher's presentation step.**

## Blind (not compared)

- The `book` table: 4 rows of portfolio-level characteristics, allocation and segment.
- The publisher stage itself, which was not executed. Its weight and industry transforms are inferred from 190-of-190 agreement, not run.
- The gap record write path, which a dry run does not exercise. The deploy acceptance reads it (row D1-S2 and the pair's R1).
