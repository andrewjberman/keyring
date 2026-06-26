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
- [ ] STEP-4 silver holdings merge 06-23/24/25 (0.6.0 chain) -> silver/holdings advance:
- [ ] STEP-5 0.6.0 fires cot gold/forwardfill/served chain -> served data_as_of advances:
- [ ] STEP-6 VERIFY served firm-AUA data_as_of = 06-25 BY CONTENT; bd-cot-served-aua-stale + bd-cot-silver-stale-holdings self-clear:
- [ ] STEP-7 close ledger.

## Coordination
- 0.6.0_AE_PartnerETL owns the box SSM sequencing + the chain-fire. Backfill runs on the current stable session (reseeded 13:07Z) BEFORE 0.6.0's item-2 e2e session-rewrite.
- Forward-fix (valued-re-pull retry net) = SEPARATE follow-on, CTO-gated draft + DS co-author (NOT in this ledger).

## Status: OPEN
