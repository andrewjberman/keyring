# SITE Z JOB -- DIVZ/IDVZ history gap fill 2026-10-01..05 (Andrew-direct "both recs approved", ~18:1xZ 2026-10-06)

Record: org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_160xZ_NEW_SECURITY_LIFECYCLE_AND_HISTORY_BACKFILL.md
Owner of the run: the site Z Bloomberg terminal seat (0.0.3_BG_BBGTerminal) or 0.0.0_AB_MSTR~Z.
DEADLINE: landed before 09:00 ET 2026-10-07 (etf-positioning-producer-daily, cron 13:00 UTC).

## Precondition
Site Z working tree at or past commit 0856dbb572 (backfill_extra_securities_history.py gains --subdir,
TICKER=CUSIP, --skip-empty). Terminal signed in (integrations/bloomberg/READ_HERE.md section 2 if not).

## Command (the pull's AWS interpreter, PY_AWS, as for etf_daily_pull.py)
1. Dry run first:
   python integrations/bloomberg/pipeline/backfill_extra_securities_history.py --start 2026-10-01 --end 2026-10-05 --subdir gap_20261001_20261005 --skip-empty --dry-run --securities MPLX=55336V100 VZ=92343V104 MO=02209S103 NEE=65339F101 QCOM=747525103 BIPC=11276H106 CSCO=17275R102 XOM=30233Q108 RTX=75513E101 CME=12572Q105 ENB=29250N105 UNP=907818108 TXN=882508104 ATO=049560105 BX=09260D107 AEP=025537101 ABT=002824100 UPS=911312106 SALXX=857492656 PBR=71654V408 RBGLD=756255303 ISNPY=46115H107 ENLAY=29265W207 RHHBY=771195104 TTE=F92124100 BNPQY=05565A202 GSK=37733W204 RIO=767204100 SNY=80105N105 AZN=G0593M107 BTI=110448107 HSBC=404280406 BZLFY=120738406 BP=055622104 IMBBY=45262P102 BBSEY=05541J103 KOF=191241108 VIV=87936R205 CICHY=168919108 ORANY=684060106 AMX=02390A101 KCDMY=494386204 WMMVY=93114W107 NSRGY=641069406 KKPNY=780641205 TKOMY=889094108 CNI=136375102 LNVGY=526250105 IBDRY=450737101 IBN=45104G104 UL=904767803 ICT=6455819 CPA=P31076105 UNVGY=91377B109 BKRKY=69366X100 OMAB=400501102 NOK=654902204
2. Same command without --dry-run.

## What it writes
s3://opal-data-etfs/bbg-testpull/tickers/{TICKER}/gap_20261001_20261005/history.csv for up to 57 securities;
additive (new keys only, nothing overwritten; exit 81 if any target exists). About 57 x 3 rows of
PX_LAST + DAY_TO_DAY_TOT_RETURN_GROSS_DVDS.

## RESULT (read back by 4.0.0_SA_CRO~P, 2026-10-06 ~20:0xZ)
LANDED 2026-10-06 19:25:47Z..19:25:55Z: 57 of 57 keys, 171 rows (57 each on 2026-10-01, 10-02, 10-05), 0 null
returns. The gold loader (etf_positioning_gold._load_backfill_history, run read-only) reads 230 ticker files,
171 rows in the gap window, 0 skipped; VZ 10-01 +0.2398, 10-02 -0.1305, 10-05 -0.1524. Open: grade the
2026-10-07 09:00 ET gold output (DIVZ/IDVZ rows: GICS sub-asset populated, MTD/QTD not equal to 1D).

## Report back
Exit code, the count of OK: wrote lines, and any SKIP: lines, to 4.0.0_SA_CRO~P. That seat reads the keys back
and grades the 2026-10-07 gold output.
