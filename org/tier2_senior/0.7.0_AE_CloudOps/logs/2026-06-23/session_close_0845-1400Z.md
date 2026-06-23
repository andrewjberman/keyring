# Session close -- 06-23 AM: cot served-$0 P0 -> restore -> 06-22 currency-advance -> go-live provisioning -> render-skew polish

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, DEPLOY, COORDINATE

Window: ~08:45Z -> ~14:00Z (06-23). Serial: 0.7.0_AE_CloudOps. The morning arc off the overnight nightly: caught a live served firm-AUA=$0, drove + verified the restore, grounded the currency root + advanced the served to the last-complete day, provisioned the go-live users, and resolved a render-skew -- every claim ground-truthed on the live served number.

## Current State (the handoff)

**Cottonwood is LIVE on ADVI, page-consistent @06-22, served firm-AUA $397,979,116.54.** The COTETL served-$0 P0 + the go-live are fully resolved/verified. Remaining = the (b) durable morning-refresh (gated on DS) + the paced queue.

### COTETL served-$0 P0 (06-23 AM) -- CLOSED
- **Caught at the AM ledger-verify:** served firm-AUA = $0.0 at data_as_of=06-23 (account_performance.total_aua=0.0, aua_change=-397.3M; NNA/counts populated = AUA-specific). HELD the 3 nightly-verify ledgers (clean deploy != valid served). CTO+COO accepted "exemplary."
- **Mechanism (DS-corrected):** 06-23 holdings = FULL 10,735 rows but 0% non-zero MV (BD same-day UNPOPULATED prices) -> C_03 sum(MV)=0. The DATEMODE freeze-fix exposed the opposite edge: OVER-advancing to today/incomplete.
- **(a) restore (DS, e171ca3e1):** C_03/C_01 completeness-guard (non-zero-MV-fraction>=0.5) caps the served at the last-COMPLETE = 06-18. I live-CF-verified ($397,313,612.21/06-18 across header/clients_tab/partner_analytics, X-Cache Miss) -> CLOSED the 3 ledgers (3f60facf9).
- **(c) currency-advance to 06-22:** test-pulled 06-22 holdings @09:41Z = 86.7% non-zero/$397.98M (proved valuation lags overnight->morning; 02:08Z nightly too early). DS manifest-cleared the dedup-by-filename block (the silver-merge skipped the re-pulled-valued 06-22 -- caught via verify-on-served, NOT assumed) -> re-merge + gold -> served advanced to 06-22/$397,979,116.54. Banked: [[reference_cot_served_overadvance_incomplete_day_zero_aua_valuation_lag]].

### Go-live provisioning + render-skew polish -- CLOSED
- **Provisioned 2 test users** in opal-users-v2 (mirrored the 17-attr cottonwood-scoped schema): jane@cottonwood.com (admin) + john@cottonwood.com (user), firmId=cottonwood, isInternal ABSENT. Uniform pw CottonwoodGoLive2026!. Login-smoke verified (POST /auth/login -> JWT firm-pinned cottonwood). CVO render-walk PASSED -> Cottonwood LIVE.
- **Render-skew polish:** my (c) surgical subset was served-AUA-path-only (B_00->C_03->C_01->D_00->D_01->D_04), so timeseries_overview + mix_summary (producers C_06/D_03 + D_04) stayed @06-18 = within-page skew. Full gold-run (mode=gold-run, a15b7fca, DS-GO, idempotent off the 06-22 silver) advanced all 18 scripts -> all 5 surfaces @06-22. Verified on the ACTUAL FE routes (timeseries_overview/mix_summary served via /platinum/firm/ NOT /artifacts/ -- found in api/endpoints/advisor-intelligence.ts:356/551 after my first probe 403'd the wrong route). CVO pixel-verified + DS reconciled (ties exact to account_performance @06-22). 403 on header_metrics_fresh = BY-DESIGN cottonwood graceful-degrade (PartnerAnalytics.tsx:244-249), not staleness-masking -> L4 follow-on.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| (SSM/aws) | session-refresh + 06-22 test-pull + (c) re-merge/gold + full gold-run + ~15 served-AUA verifies | PASS | the exporter-IP BD path; verify-on-served caught the $0, the dedup-skip non-advance, the partial-advance |
| comp-freshness | --list (L4 cadence-config) | PASS | grounded cot ABSENT (bd 32-entry only) -> L4 genuinely-open |
| comp-grep | timeseries_overview/mix_summary producers | PASS | D_04 + C_06/D_03 = the skipped producers |
| deploy_ledger.py | close-leg/close x3 (d01/cleanup/a05) | PASS | closed on the served-reconcile, not the clean-deploy |
| comp-which | L4 routing | PARTIAL | fell through to raw grep (the ~8-of-36 backstop gap, known) |

**What worked:** verify-on-served at every edge -- the $0 catch (vs the freshness-grounding that PASSED), the dedup-skip non-advance (re-run "succeeded" but served stayed 06-18), the partial-advance (3 of 5), and the wrong-route 403 (found the real FE path vs accepting S3-data as a proxy). **What failed:** nothing shipped wrong. **Gap:** comp-freshness cot-blind (L4); comp-which backstop (known).

## Blockers

None. (b) morning-refresh gated on DS's at-pull check (in flight, not blocked).

## Next Steps

- **[0.4.0_DS]** author the at-PULL/pre-manifest holdings completeness-check in cot_bronze_ingest (reject non-zero-MV<0.5 BEFORE land_to_s3 -> no manifest footprint = collision-safe). Pings AE at deployed.
- **[0.7.0_AE_CloudOps]** on DS's check: deploy the `cot-morning-refresh` EventBridge rule (DESIGNED: 2nd ~10:00Z cron -> cot-bd-session-trigger mode=session-refresh, reusing the event-driven session->bronze->silver->gold chain; the at-pull check rejects today-unvalued + lands D-1-valued -> served auto-advances). TF/safe-apply + verify collision-safety (rejected-$0-day then valued-re-pull merges clean) + verify-on-served. RAVC CTO.
- **[0.7.0_AE_CloudOps] queue (paced, post morning-refresh):** L4 (cot gold_freshness_config.yaml + comp-freshness cot-support -- ELEVATED defensive-monitor; a registered monitor would've auto-caught this AM's $0) -> DEBTSCAN-D3 scorer-build -> ETFS-W1 (REUSE existing opal-data-etfs per CTO/COO amend; delta = write-out IAM + daily/{partner}/ prefix + Inflection producer, 0-diff-on-bucket) -> COTETL TO-reconcile (DATEMODE-B/AUAFIX-L1/CHAIN-FIX/BACKFILL.ae-session = DONE; DATEMODE-C superseded-by-(b); L4 open).

## Ops note

cot-exporter i-0643a5bee8a8feabf running (warm from the AM runs; start-on-demand, idles out). Both go-live test users + the 2 smoke creds LIVE. All cot writes = sanctioned exporter SSM runs of DS-deployed code (no inline, no ad-hoc gold). 3 AM ledgers closed + committed (3f60facf9).
