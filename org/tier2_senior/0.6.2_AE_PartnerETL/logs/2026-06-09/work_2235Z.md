# 0.6.2_AE_PartnerETL — work log 2026-06-09 ~2235Z

## Session: ADVI_COTETL — BACKFILL-001 resolution + COT gold re-architecture (AUA from daily Holdings snapshot)

Andrew-direct, real-time all session. Marathon. Summary of outcomes:

### 1. BACKFILL-001 — RESOLVED (moot)
COT's Black Diamond transaction history starts **2026-04-22** (recent onboarding). Wide `dateRangeType=Custom` (2010→today) == Last6Months == Last12Months == 19,188 rows. No deep history to backfill. The old `cot_backfill_date_probe.py` 400/500s were a broken probe (guessed `DateRangeType="DateRange"`, no `asOfDate`, ISO dates), not an API limit. Valid enum + Custom mechanics banked in memory. COO-accepted, closed.

### 2. Persisted-template reuse refactor (commit 808d35b47)
Stopped creating a throwaway template per call. 4 canonical persisted templates tapped by id: transactions 226274 (Custom 14d), allocations 226334 (CurrentDay, +Account Type/Registration), realized 226275, unrealized 226276. Fixed `load_template` ID-discard bug + DS's `sharingStatus:"Private"` create-400 on realized/unrealized. Cleaned orphans. **BD session real TTL ~30-60min (cf_bm + idsrv), not the 20h stated — never replay the cookie off the cot-exporter EC2.**

### 3. THE re-architecture: COT AUA from daily Holdings snapshot (Andrew direct)
Root finding (proven): the 49F positions-FIFO valuation model **structurally undercounts** a recent BD onboard — canonical holdings from positions_cube = **$43.9M / 24 accts** vs the allocations certified AUA **$372.9M / 642**. FIFO needs in-window opening txns; COT's holdings transferred in pre-04/22.
Fix (Andrew's call): track AUA from the **daily Holdings/Snapshot** (qt1, template 226355 'Assets_Dim', CurrentDay). Built end-to-end:
- **bronze**: new `holdings` table (qt1 226355) → `forwardfill_v2/holdings/` daily.
- **silver**: `holdings` config → `silver/holdings` + `cot_holdings.parquet`. Channel-validated **$373.2M / 680 accts / 10,183 holdings**, reconciles to allocations (0.1%).
- **gold**: B_00 single-custodian branch builds canonical holdings from the snapshot (`source=bd_snapshot`) → **$373.2M** (was $44M).
- Chain runs **A_00→D_04 exit 0**; D_02/D_03 correctly WARN-skip (COT has no tax-lots / advisor tiers — Andrew confirmed). D_04 platinum publisher complete (firm dashboard, 38 client timeseries, summaries).

### 4. ~20 fixes shaken out (all on the COT gold mirror opal-data-cot/code/gold/ + scripts)
pandas 3.0→**2.2.3 pin** (49F gold breaks on pandas-3); gold code + prices **mirrored to opal-data-cot** (bucket isolation, no opal-data-bd access); `run_query` re-stamps dates **only for Custom** (CurrentDay stamping nulled qt1 measures + zeroed allocations); silver reads via **openpyxl data_only** (pd.read_excel under 2.2.x nulled qt1 formula measure-cells); A_04 modal_by_group reset_index + named-index; B_00 Schwab-disconnect graceful (mapping/closures); `gold_utils._load_parquet` tolerant (missing columns→null, NoSuchKey→empty); D_00 tax-section empty-guard; A_00 snapshot account-universe union.

### CURRENT STATE
- Daily snapshot pipeline LIVE (bronze→silver), AUA reconciling $373.2M.
- Gold chain green A_00→D_04. **Portal headline AUA = $362.6M / 623 accts** (97% of $373.2M).
- **Remaining gap to full $373.2M/680**: (a) A_00 takes incremental path (existing 623 dimension) — snapshot-union only fires on full rebuild; force full-rebuild OR clear dimension. (b) B_03 account_gains (now $373.2M/680 on snapshot canonical) is NOT in the COT chain (lots-script, skipped) — must be added after B_00 so account_gains/performance rebuild nightly (else goes stale). Both → 680/$373.2M throughout.

### CTO RULING (89e1e4573) — mirror-patch durability
COT patches must live in git in the SHARED bd gold scripts as `FIRM_CAPABILITIES` config (FIRM_ID-gated, NO-OP for 49F/INF), NOT mirror-only. Rule 13: **AE hands patches → DS folds in → opal-data-bd/code/gold → re-mirror to COT**. Handoff to DS this session (below). Then update ssm.tf:194-199 mirror comment ("mirror holds no COT-specific patches; all config-gated; re-mirror always safe").

### OPEN / NEXT
- DS handoff (FIRM_CAPABILITIES fold-in of all mirror patches + the A_00-full-rebuild + B_03-in-chain refinement). Alerted DS this session.
- AC7 `platinum/cottonwood/ownership_map.json` (post-gold, ADVI_PRTORG close-gate).
- seeking-alpha i-06376c11d8b3c3443 4-point-verify-and-terminate (COO GO'd; queued behind COT, STOPPED instance no urgency).
- ssm.tf mirror comment update (AE-lane).

Commits: 808d35b47, a5150c82f, 2e7745939, 401e06062, 1d547fe7c (+tag cot-pipeline-v0.3.7), 35f8c0aa9, 6e75df585, bbd50b358, aa5aa2684, 58b27ad43. Gold mirror patches (opal-data-cot/code/gold/) are TEMPORARY pending DS fold-in.
