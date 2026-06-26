# Deploy-Completion Ledger: cot DATEMODE-B fast-path backfill re-pull (holdings 06-23/24/25)

- **Owner:** 0.7.0_AE_CloudOps
- **Opened:** 20260626T1456Z (at re-pull START, per CTO GO 145510Z condition 4)
- **Project:** ADVI_COTETL.AUAFIX-DATEMODE-B
- **Gate:** CTO arch-GO 20260626T145510Z (fast-path backfill APPROVED, 5 conditions); COO DRIVE-NOW 145327Z; (e1) TIMING source+live-confirmed by no-land probe d92b5b21.
- **Change class:** data-recovery WRITE (cot bronze re-pull -> silver -> 0.6.0 chain -> served advance). cot-clean (NEVER#1).

## Mechanism (confirmed, not hypothesis)
Served cot firm-AUA frozen at 06-22 because the scheduled SAME-DAY (T+0) holdings pulls of 06-23/24/25 hit BD before pricing completed (nzf<0.5) -> HOLDINGS_COMPLETENESS_FLOOR correctly rejected them -> nothing re-pulled once BD priced them (cadence ~T+1). Probe d92b5b21 proved all biz days 06-22..06-25 are FULLY PRICED now (nzf~0.85); the only nzf=0 days are Sat/Sun (verified, no defect). Re-pulling now lands the legitimately-priced days via the standard floor-gated path.

## Conditions (CTO 145510Z)
1. STANDARD floor-gated path ONLY -- no override/force; land iff nzf>=0.5. [HONORED: script has no DRY_RUN/override; ingest_table floor-gates]
2. Per-day bronze --table holdings --date 2026-06-2X -> silver holdings leg -> 0.6.0 fires gold/forwardfill/served chain.
3. ACCEPTANCE = served firm-AUA data_as_of advances to 06-25, verified by CONTENT (not mtime). 06-25 = correct DONE-STATE (06-26 is T+0/expected-unpriced).
4. THIS LEDGER -- open at START, close on served-advance-verified. Finish-in-session.
5. cot infra/session/silver only.

## Steps
- [x] STEP-1 bronze re-pull holdings 06-23 -- SSM 483722f4, completeness OK 85.2% -> LANDED forwardfill_v2/holdings/HOLDINGS_DAILY_2026-06-23.xlsx (825198 B). Floor PASSED, no override.
- [x] STEP-2 bronze re-pull holdings 06-24 -- OK 85.2% -> LANDED HOLDINGS_DAILY_2026-06-24.xlsx (824665 B).
- [x] STEP-3 bronze re-pull holdings 06-25 -- OK 85.6% -> LANDED HOLDINGS_DAILY_2026-06-25.xlsx (825015 B). BACKFILL_RC=0, firm=cottonwood (clean).
- [x] STEP-4 silver holdings merge 06-23/24/25 (0.6.0, SSM 66d57a5b Success) -> silver/holdings/2026-06-{23,24,25}.parquet 11279 rows/22 cols ea (overwrote 06-23 partial). partitions 11->12.
- [x] STEP-5 0.6.0 fired cot gold chain (SSM 1855a971 = SUCCESS, exit 0) -> B_00 canonical_holdings --force-recent-days 14 (read fresh silver) -> C_01 -> C_04 validate_aua PASS=1/FAIL=0 -> C_03 --upload -> D_00/D_00b portal_timeseries --upload -> served. (Non-fatal optional-step gaps: OFC office-dim view empty / C_05 tax / D_02 advisor-detail / D_03 lots -- all pre-existing, non-gating, separate from #1.)
- [x] STEP-6 SERVED VERIFIED BY CONTENT (independent read by me AND 0.6.0): platinum/firm/timeseries_overview.json data_as_of = 2026-06-25 (was 06-22), STABLE across 2 reads, generated_at 2026-06-26T15:12:33Z, firm_id cottonwood, AUA REAL (Q2'26 NMNC $401,437,408.55 end_date 06-25, not degraded/empty). **Served firm-AUA UN-FROZE 06-22 -> 06-25 = the #1 data condition MET (CTO condition 3 / COO oracle).**
- [x] STEP-6b alarm self-clear: BOTH OK. bd-cot-served-aua-stale -> OK (Updated 1782487622), bd-cot-silver-stale-holdings -> OK (Updated 1782487647). Cleared in ~8min (seeded a fresh freshness-probe datapoint: served_aua_lag=1 / holdings_lag=1 < threshold 2 -> Max-window aged the pre-fix high-lag out fast). Content fresh, NOT silenced.
- [x] STEP-7 CLOSE: full acceptance MET -- served-advance (06-25, 4-way content-verified: me x2 + 0.6.0 + COO) AND alarm-quiet (both OK). NEVER-law honored: begun re-pull FINISHED in-session.

## Coordination
- 0.6.0_AE_PartnerETL owns the box SSM sequencing + the chain-fire. Backfill runs on the current stable session (reseeded 13:07Z) BEFORE 0.6.0's item-2 e2e session-rewrite.
- Forward-fix (valued-re-pull retry net) = SEPARATE follow-on, CTO-gated draft + DS co-author (NOT in this ledger).

## Status: CLOSED 20260626T~1527Z. #1 cot served-AUA freeze RESOLVED (06-22 -> 06-25), floor-clean, content-grounded, in-session. Forward-fix retry-net (durable close) tracked separately (CTO-gated, DS co-author).
