# Session Log -- 0.4.0_DS_ClientPlatform -- served-$0 P0 hardening + cot-ADVI go-live reconcile + ETFS_SETUP W1 producer + WORK-A defect

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, VALIDATE, COORDINATE

## Summary

Window since the 06-22 cotetl-cleanup log. Drove the overnight served-firm-AUA=$0 P0 from
diagnosis to a structurally-hardened never-$0 with proven defense-in-depth; reconciled the
cot-ADVI go-live to full 5-surface page-consistency @06-22; reconciled my ADVI_COTETL TO
queue (closed-6/kept-2); drove the ETFS_SETUP W1 Inflection producer from un-paced-to-HOT to
LIVE the same day (contract locked, compute owner-reviewed/refined/committed, config locked);
and source-confirmed a CVO-caught WORK-A assets_dim defect (fix pending Andrew-go). **Zero
false-fixes across the window. Served firm-AUA live + correct + page-consistent at
$397,979,116.54 @06-22.**

## Threads (chronological)

1. **Overnight P0 -- served firm-AUA=$0 (e171ca3e1).** Root cause source-confirmed: the BD
   same-day pull returned FULL position rows with UNPOPULATED prices (06-23: 10,735 rows, $0
   MV, 0% non-zero); C_03 summed it -> served $0. FIX: completeness guard (non-zero-MV-account
   fraction >= 0.5, CTO signal-strengthening) caps C_03 (account_performance, the served-AUA
   keyer) + C_01 (nna date-axis) at the last-COMPLETE snapshot. D_00/D_01/D_04/C_01b inherit
   via account_performance.max. CTO-authorized launch-critical; dry-run-verified; restored
   then advanced to 06-22 currency.
2. **C_01b account_team fallback (3397fd95e).** Mirror-D_01 derive from accounts_dimension so
   role_aua stops erroring on missing gold/views/account_team.parquet (NoSuchKey). role_aua
   EMPTY for cot (architect null) = DEFERRED-by-data-absence. CTO-approved gate-note bypass
   (pre-existing bd-fork ruff debt; my change clean).
3. **Durable (b) fix -- cot_bronze_ingest source-completeness guard (fdd5f28d4).** Reject an
   UNVALUED holdings snapshot AT-PULL/PRE-MANIFEST (non-zero-MV-fraction<0.5, before
   land_to_s3) -> the $0-day never lands in bronze -> never enters the silver-merge manifest ->
   a later valued re-pull is the first entry (no dedup-collision, the class that blocked the
   06-22 advance). Sentinel verifies LANDED tables only. Same 0.5 signal as C_03/C_01
   (defense-in-depth); exercised live today (06-23 $0 excluded).
4. **Leg-3 C_03 cross-val retire (ec5831836).** Retired the C_03 cross-val-vs-client_performance
   (+ unused import): client_performance is the dead/frozen-06-09 C_02 path -> the cross-val
   could only DIVERGE (false-WARN growing daily, 6.65% @06-22 -> alarm-masking). WARN-removal
   only; dry-run total_aua @06-22 = $397,979,117 UNCHANGED. C_01 NNA cross-val (woven) deferred.
5. **Go-live page-consistency reconcile.** CVO render-walk PASS caught a within-page skew: my
   (c) surgical currency-subset (B_00->C_03->C_01->D_00->D_01->D_04) advanced the served-AUA
   surfaces but skipped the timeseries/mix producers (C_04/C_05/C_06/D_00b/D_02/D_03). AE ran a
   full gold-run (a15b7fca, idempotent off the 06-22 silver; my guards capped at 06-22) -> all
   5 surfaces @06-22. I reconciled vs source: timeseries_overview AUA @06-22 = $397,979,116.54
   = account_performance EXACT (the "06-23" I first saw was generated_at run-time metadata,
   grounded not assumed); mix_summary @06-22. Go-live cert CLOSED.
6. **TO-hygiene (18b4fe543, COO /drive).** Reconciled my 8 ADVI_COTETL TOs: closed-6
   verifiably-DONE (AUAFIX-L2/L3/L6/DATEMODE-A = $24M cert; CHAINFIX; ASSETSDIM-BACKFILL),
   kept-2 genuinely-open (the bd-fork ruff-sweep; the C_02-rewire residual legs). Verify-each,
   no blanket-close. COO-accepted.
7. **ETFS_SETUP W1 Inflection producer (14309912f + config).** New P1 wave (COO/CTO/Andrew),
   un-paced to HOT mid-window. Locked the daily-slice schema (CTO-signed Sec-8:
   partner/date/etf_ticker/ownership_value=USD-sum(MV)/account_count/source_artifact/
   source_as_of=TRUE-vintage -- the COTETL vintage lesson in the contract). Chose path (b)
   rate-limit-aware: AE authored the first-cut compute, I OWNER-REVIEWED + committed-through.
   Verified source_as_of=inf-holdings-date-col=data-vintage (06-22 partition==internal date);
   compute ties ($82.14M/476 accts). Folded CTO's 2 refinements + my etf_ticker fix: the
   ZERO-vs-MISSING completeness guard (no-valued-source day writes NO slice, vs a held-zero 0
   row -- value-axis of the vintage lesson) + schema_version=1.0. AE deployed LIVE
   (inf-pipeline-v1.7.74). Locked etf_universe.json at s3://opal-data-etfs/config/ (repo-source
   AE-committed in his infra lane after the owned-paths hook correctly bounced my infra/aws
   commit).
8. **WORK-A assets_dim defect (CVO-caught, fix PENDING).** CVO proactive ground-check: A_05
   nightly-chain over-advanced assets_dim to the unvalued 06-23 ($0) + skipped the valued
   06-22. Mechanism source-confirmed: A_05 `_find_latest_canonical_date()` returns max(dates)
   = 06-23; its reconcile guard passes $0==$0 (checks build-breakage, not completeness). Same
   over-advance class as the served-$0 P0; A_05 never got the completeness-guard. Validated the
   threshold (06-22=86.4% valued, 06-23=0.0% unvalued). NON-URGENT (gold/dimensions, zero
   served/portal impact). Fix designed (last-valued-date targeting + completeness-guard +
   backfill 06-22), held for Andrew-go.

## Compiler Tools

Window was dominated by SERVED-artifact verification (boto3 S3 reads of served/canonical/dim
partitions -- data-access, off-rail per the Rule-21 governing principle: comp-tools mandatory
IFF an associated graph backs the target; served-data reads don't) + SOURCE-mechanism reads
(native Read on A_05/C_03/C_01/the ETFS producer -- free) + the cross-firm-isolated ETFS
producer owner-review. The pending WORK-A fix will run comp-pipescript io (A_05 column
gaps/consumers) + comp-blast pre-edit per Rule 20. No estate/graph traversal this window that a
raw search would have under-served.

| Tool | Run | Result | Note |
|---|---|---|---|
| (boto3 served/source verify) | served-AUA, 5-surface reconcile, canonical/dim partitions | PASS | data-access grounding, off-rail |
| (native Read) | A_05, C_03, ETFS lambda | n/a | source-mechanism grounding (Rule 22) |

**What worked:** ground-the-mechanism-by-reading-content (caught the unpopulated-prices root
cause, not file-size; caught the generated_at metadata vs a real 06-23 skew; confirmed the
A_05 max-date targeting). **What failed:** none (zero false-fixes). **Gap:** none new.

## Files Modified (see commit messages for per-file detail)

- `data/cot/scripts/gold/C_03.account_performance.py`, `C_01.canonical_nna.py` -- e171ca3e1
  (completeness guard), ec5831836 (C_03 cross-val retire)
- `data/cot/scripts/gold/C_01b.role_aua_backfill.py` -- 3397fd95e (account_team fallback)
- `data/cot/scripts/bronze/cot_bronze_ingest.py` -- fdd5f28d4 (source-completeness guard)
- `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py` -- 14309912f
  (ETFS W1 producer, owner-reviewed/refined commit-through)
- `infra/aws/etfs/config/etf_universe.json` -- AE-committed in his lane (my authored content)
- 8 ADVI_COTETL TO files -- 18b4fe543 (reconcile-close notes)
- silver/cot_incremental_manifest_holdings.json (S3, boto3) -- cleared the 06-22 dedup entry
- s3://opal-data-etfs/config/etf_universe.json (boto3 put) -- config lock

## MCP Traffic

~25 broker messages handled (COO/CTO/CVO/AE). Significant: CTO P0 launch-critical authorization;
COO go-live cert close + TO-hygiene /drive + ETFS_AVGCAP.W1 charter; CTO ETFS schema Sec-8
SIGN-OFF + 2 refinements; AE go-live full-gold-run coordination + ETFS producer first-cut ->
my owner-review/commit-through; CVO WORK-A defect flag (RAVC pending at fix). RAVCs opened/closed:
P0 (closed), go-live reconcile (closed), ETFS producer (closed to AE+COO), WORK-A (OPEN -> CVO).

## Current State

- **Served firm-AUA: $397,979,116.54 @ data_as_of=2026-06-22**, live + correct + page-consistent
  across all 5 cot ADVI surfaces (header_metrics, clients_tab, partner_analytics,
  timeseries_overview, mix_summary). Go-live cert CLOSED.
- **All P0/currency-hardening deployed:** C_03/C_01 completeness guards + cot_bronze_ingest (b)
  source-guard live; defense-in-depth proven (06-23 $0 excluded at source + downstream).
- **ETFS_SETUP W1: producer LIVE** (inf-etf-ownership-daily, inf-pipeline-v1.7.74), triggered
  on inf-gold pipeline-complete. Config locked (s3://opal-data-etfs/config/etf_universe.json,
  tickers=[DIVZ,IDVZ,PFDE,PFOE], schema_version 1.0). First slice fires on tonight's inf-gold
  nightly -> writes daily/inflection/{date}.json (expect ~$82.14M/476 accts).
- **WORK-A assets_dim defect: OPEN, fix designed not started.** assets_dim has degenerate
  06-23 ($0) + missing valued 06-22; A_05 needs last-valued-date targeting + completeness-guard.
  HELD for Andrew-go (non-urgent, zero served impact).
- **Kept-open (non-urgent):** C_01 NNA woven cross-val removal; bd-fork ruff-sweep
  (C_01/C_03/C_01b); C_02 client_performance dead-lots-FIFO retire (maxdate 06-09).

## Next Steps

- **[0.4.0_DS_ClientPlatform]** WORK-A assets_dim fix on Andrew-go: A_05 last-valued targeting +
  completeness-guard + backfill 06-22 + RAVC [3.0.0_SA_CVO].
- **[0.7.0_AE_CloudOps]** morning-refresh EventBridge (auto-currency = full hardening complete)
  -> I RAVC [1.0.0_SA_CTO] at land. First ETFS slice reconcile when tonight's nightly fires.
- **[0.4.0_DS_ClientPlatform]** ETFS_AVGCAP.W1 (the averaging metric) -- gated on the ETFS slice
  going live.

## Blockers

None. WORK-A fix is HELD-for-Andrew-go (a choice, not a blocker); all other threads landed or
are event-gated on others' lanes.
