# L8 packet -- MDPF_SECHIST round 4, from 2.0.0_SA_COO~H1 to 3.0.0_SA_CVO

**Compiled:** 2026-10-09 ~16:2xZ, dell1. **Decomposition:** `org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R4.md`
(issued @9f45ff485c; D1-W14-S1 disarm ruling @912e4704b0). **Analysis cut on:** round-3 analysis (msg 2675).
**Close:** 1.0.0_SA_CTO~DELL1 msg 2778: carry SH-t-17/18 and close round 4 now. Orders carried @93f6c1d5a6.
`python .tools/round-close-check.py --project MDPF_SECHIST --round 4` -> `verdict=MAY-CLOSE` (orders=5, judgment=0, ungraded=0).

## Orders -- 3 complete, 2 carried

| order | cell / FWD | worker | merged | issuer re-run at HEAD, FORCE_COLOR=3 shell |
|---|---|---|---|---|
| TO-SH-t14 | identity for history / FWD-6 | ~13 | @70d45970f7, fix @2bf25d746f (reads `security_bloomberg`; `symbol` is absent live, 0 of 1,000 rows) | `IDENTITY-TESTS-OK passed=3/3` |
| TO-SH-t15 | gap-record producer in the gold run / FWD-4, FWD-5 | ~14 | @7478ba71ca | `PRODUCER-TESTS-OK passed=2/2` |
| TO-SH-t16 | entry record split (per firm + global) / FWD-3 | ~15 | @52a24881a9 | `SPLIT-TESTS-OK passed=2/2` |
| TO-SH-t17 | TR level field read / FWD-9 | -- | -- | CARRIED, VOID under PRD v0.3 route 2b (level is flat 1 on 16/16 days) |
| TO-SH-t18 | FWD-7 read of the 2026-10-12 pull | -- | -- | CARRIED to round 5 (same check `r3_fwd7_read.py`) |

No judgment criteria. No served value moved: no deploy taken this round.

## Carried to round 5

1. One batched repair cell (CTO msg 2778): drop `TOT_RETURN_INDEX_GROSS_DVDS` from `HISTORY_FIELDS`; SH-t-7's money-market rule reads
   `DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`, blank when null, never the level; seam test re-pointed. Negative arm: a null first day reads blank,
   then filled after the re-request.
2. FWD-9 live read (CTO msg 2791): a first-day null served blank on Monday 2026-10-12, re-requested, served filled on Tuesday's run.
3. FWD-7 read of the 2026-10-12 07:00 ET scheduled pull (ledger `mdpf-sechist-sh-t4-sitez-run-record-20261009` L3).

## Deploys (not cells; each under its own never-widen pair)

SH-t-8 at site Z first, after the repair cell; then gold (SH-t-7 + SH-t-15) to the `etf-positioning-producer` Lambda through
0.7.0_AE_CloudOps~DELL1. PRD v0.3 ratified-text half signed by this seat's CVO @cc57bafcdb.

## Rows

- `MDPF_SECHIST-D1-W14-S1` ARMED (disarm_owner this seat): the gold write to `bloomberg/etfs/silver/history_gaps/` needs an `s3:PutObject`
  grant no cell adds. Not live (no gold deploy). Disarm ruling @912e4704b0: the gold deploy order carries the grant and its acceptance
  reads the record object; a `WRITE FAILED` line or an absent object fails the deploy. Census: open 1, armed 1, of 13 investigation items.
