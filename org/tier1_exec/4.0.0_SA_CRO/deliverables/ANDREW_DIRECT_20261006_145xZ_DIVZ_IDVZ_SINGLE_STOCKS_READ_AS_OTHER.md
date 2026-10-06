# ANDREW-DIRECT 2026-10-06 ~14:5xZ -- DIVZ / IDVZ single stocks read as non-single-stock on /positioning

Channel: Claude Code terminal, seat 4.0.0_SA_CRO~P. Screenshots 2026-10-06 10:52 and 10:52 ET.

## Verbatim

> I need you to take a look at these two images, which depict the ETFS view of DIVZ and IDVZ in the "Positioning"
> page, "Holdings Breakdown" panel: [two screenshot paths]. FOr some reason all these single stocks are being listed as
> non-single stocks. I think this may be linked to some of our work on the positioning canonical securities table. We
> need to understand why these two ETFs were adversely affected, however PFDE and PFOE were unscathed and depict all
> security rows with correct classification.

## Read (measured 2026-10-06, live S3 + CloudWatch)

The canonical securities table work is NOT the cause. The chain:

1. `etfs-netassets-daily` (code unchanged since 2026-08-29) fails the TrueShares scrape from the 2026-10-01 run on:
   `WARN: [divz] tier 1 trueshares FAILED: TrueShares page layout changed; missing ['nav', 'market_price',
   'net_assets', 'shares_outstanding']` (same for idvz; 10-01 and 10-05 runs read; 09-30 run captured 30 + 41 rows).
2. `s3://opal-data-etfs/silver/holdings/{date}.parquet` therefore carries DIVZ 30 + IDVZ 41 rows on 2026-09-30 and
   zero from 2026-10-01 (10-01 and 10-05 read: PFDE 90, PFOE 25 only).
3. The Bloomberg pull takes its security list from that day's silver file only (`run_manifest.json`
   `universe_source: silver/holdings/2026-10-05.parquet`, constituents 108; 166 on 2026-09-29, 108 from 2026-10-01).
   VZ, MO, NEE, NSRGY, WMMVY are present in bbg characteristics on 09-15..09-29 and absent on 10-01, 10-02, 10-05.
4. The gold job (`data/etfs/scripts/gold/etf_positioning_gold.py:1180`, per-fund walk-back) still serves DIVZ/IDVZ's
   2026-09-30 holdings, but looks each one up in the current characteristics (`:1210`); no row -> no GICS sector ->
   `sub_asset_class` null -> portal `getSubAssetClass` renders "Other" and the single-stock split
   (`HoldingsBreakdownTable.tsx:348`) files it as non-single-stock with blank MC / yield / beta.
5. MSFT (DIVZ) and TSM, ASML (IDVZ) still classify because PFDE/PFOE also hold them, so they are in the pull.

Side effects: DIVZ/IDVZ holdings are as of 2026-09-30 and NAV / net assets as of 2026-09-29 (carryforward, 10-05 run
logs `ERROR: tier 4 stale_carryforward`), under a panel footer reading October 5th.

## Owners (not this seat)

- TrueShares scraper fix: `infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py` `fetch_trueshares`.
- Bloomberg pull universe should include walked-back holdings so the two inputs agree.
