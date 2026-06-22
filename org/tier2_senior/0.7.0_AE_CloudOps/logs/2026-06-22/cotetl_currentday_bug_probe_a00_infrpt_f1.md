# COTETL CurrentDay-bug decisive probe + A_00 determination + NFRA_INFRPT verify + F-1 egress

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

Window: session start (Mon 2026-06-22 ~12:51Z) -> ~13:55Z. Serial: 0.7.0_AE_CloudOps.
Startup: /watcher (re-registered, Monitor task boy0gzsy4 armed) + /cloud-ops loaded. No code/infra COMMITS this window -- all diagnosis/verification/RAVC. cot-exporter EC2 i-0643a5bee8a8feabf STARTED (session refresh, see Ops).

## Current State

Four work-streams, all delivered to record (RAVC'd); no code committed (diagnosis/verify session).

**1. A_00 (bd accounts_dimension) -- CVO #9 gate. CLOSED + CVO-VALIDATED.**
CVO asked: is A_00 INPUT-GATED or UNCONDITIONAL (2 bd-gold FAILs frozen 06-19 ~62h). Answer: INPUT-GATED. gold_dispatch.sh CATALOG L79 hardcodes `A_00 --upload --incremental`; chain mode BLOCKS --full (L899-919, INCREMENTAL_CAPABLE="A_00 A_02 C_06"); `_run_incremental` L629-631 early-returns "dimension is current" with NO write when no silver/transactions key > watermark. Ground truth: served dimension frozen 06-19 22:07; latest silver/transactions = 2026-06-18.parquet; no 06-19/20/21/22 (Juneteenth+weekend). Freeze BENIGN, not an incident. CVO #9 NNA-by-advisor CLEARED (advisor fields are txn-derived; no new txns => roster unchanged). Forward tripwire: A_00 must rewrite after 06-23 nightly lands a new txn file. CVO RAVC-closed 133057Z.

**2. COTETL.AUAFIX-L1 -- DECISIVE: INTERNAL CurrentDay bug (was thought BD-vendor gap). CTO L2 PENDING.**
Served cot firm-AUA data_as_of frozen 06-09 (content, not just timestamp: platinum/firm/header_metrics.json generated_at 06-22T02:03 but data_as_of 2026-06-09). Traced: D_00 data_as_of = perf['date'].max(); gold reads DAILY partitions (Prefix='silver/transactions/' fresh thru trade_date 06-18) NOT the frozen consolidated cot_transactions.parquet (write-only, 0 readers -- vestigial). Binding basis = holdings/alloc/unrealized snapshots. ALL 3 BD exports (forwardfill_v2/{holdings,alloc,unrealized}) pull fresh daily but stamp early-June asOfDate (Timestamps EndDate holdings=6/8, unrealized=6/9, alloc=6/5) under dateRangeType=CurrentDay (cot_bronze_ingest.py TABLE_DATE_MODE L87-93). My initial read = "BD-source gap." DS diverged (content mutates 10183->10736 under frozen 6/8 = live pull, mis-stamped). **Decisive Custom probe (COO+CTO ask, read-only) FALSIFIED my read:** Custom-mode holdings (reuse persisted templateId + dRT=Custom + MM/DD/YYYY + asOfDate) returns date-DISTINCT data -- 06/18=10736rows/$397.65M, 06/15=$390.45M, 06/08=$373.58M (MV totals all DIFFER => BD HAS per-date snapshots through 06/18, not a relabel). VERDICT: INTERNAL CurrentDay-resolution bug, fabric-fixable, NOT vendor. Magnitude: served ~$373.6M (06/08) vs actual ~$397.7M (06/18) = ~$24M / ~6.5% AUA understatement. Sentinel-required-set determination delivered + CTO-RULED: transactions correctly REQUIRED, keep set; fix-target = serve-time vintage assertion (AUAFIX L4). CTO ACCEPTED L1; L2 ruling on the CurrentDay->Custom fix PENDING.

**3. NFRA_INFRPT source-map verify (COO /drive flag) -- CLOSED, MATCH.**
opal-infrastructure-monitor LIVE CodeSha256 == source-map artifact_sha256 == S3 artifact content-sha256 = GpTiwjFJZMkGAVZzNRAWSmIM+BRZULlztWb4oAvwUy8= (all 3 identical). Artifact uploaded 06-17T23:09:19 -> TF deployed 06-17T23:09:32. Deployed-fine; AE0.6's source-map commit recorded reality (was lagging at old udV+ sha). NOT an undeployed-tail. RAVC'd 133837Z.

**4. F-1 SNS-egress delivery-verify -- split verdict.**
find-insure-budget-alerts: email sub CONFIRMED + NumberOfNotificationsDelivered=1 -> DELIVERS (Delivered>0). opal-critical-surface-alerts (SEV1 D8 alerter): 06-17 pending email sub never confirmed -> AWS auto-deleted after 72h -> only sandboxed SMS sub remains -> STILL NON-DELIVERING (Delivered=0 since ~06-16). TF declares the email sub (globgrph/item2c_surface_alarm.tf:30) = live-drift. Remediation Andrew-gated (re-confirm email OR lift SMS sandbox). Ties to AUAFIX-L4 (CTO ruled L4 needs working SES egress -- route to find-insure-budget, not critical-surface). RAVC'd 134926Z.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-pipescript io | A_00.accounts_dimension.py | PASS | confirmed reads/writes + 17 downstream consumers; grounded the input-gated answer |
| comp-which | "verify SNS topic delivers..." | GAP | returned irrelevant grep hits -> no comp tool for SNS-delivery; raw cloudwatch is correct (rail honored) |
| comp-freshness | `comp-freshness cot` | FAIL/GAP | invalid arg 'cot' (takes chain/script/artifact/ddb/all) -- not cot-aware; used raw head-object + content reads |
| comp-pipescript deployed | `comp-pipescript deployed cot` | GAP | 0 matched (bd-tree-oriented; "No scripts matched filter cot") -- banked [[reference_comp_pipescript_io_postdeps_bd_only_silent_unknown]] |

**What worked:** the decisive Custom BD-DataMining probe (date-distinct MV totals) conclusively settled BD-gap-vs-internal-bug and FALSIFIED my own earlier read -- the molecule-grade ground truth (S3 head-object + parquet/xlsx Timestamps + 3-way MV compare) that no comp tool covers. NFRA_INFRPT triangle (live CodeSha256 == S3 content-sha == source-map). F-1 verified to the DELIVERY metric, not publish-accepted. **What failed:** my L1 inference "BD has no newer data" (config-read right, inference wrong) -- corrected loudly via the probe. **Gap:** comp-freshness + comp-pipescript are bd-oriented, NOT cot-aware -> cot ground-truth needs raw aws (banked); no comp tool for SNS delivery or BD-source asOfDate.

## Blockers

None blocking me. COTETL fix is GATED (not blocked) on CTO L2 ruling (CurrentDay->Custom approach + lane split: cot_bronze_ingest.py is DS commit-lane Rule 13, BD template re-provision is my lane). F-1 critical-surface remediation Andrew-gated.

## Next Steps

- **[1.0.0_SA_CTO]** L2 ruling on the COTETL CurrentDay->Custom fix (approach + lane split) -> I execute the BD template re-provision; DS lane for TABLE_DATE_MODE edit.
- **[0.7.0_AE_CloudOps]** On CTO GO: re-provision holdings/alloc/unrealized BD templates to Custom mode (--provision path -> new templateIds into code/bronze/templates/{table}.json) + probe-validate; build AUAFIX-L4 serve-time vintage alert (route egress to find-insure-budget). Then DEBTSCAN TO-D3 (canon-motif scorer, queued) + TSGRAPH.P2-2.
- **[2.0.0_SA_COO]** HOLD the legit-latest-vs-stuck Andrew escalation (it's our bug, not vendor). Decide cot-exporter EC2 stop (or leave for nightly).
- **[Andrew]** F-1 critical-surface: re-confirm the SNS email sub OR lift SMS sandbox (standing).

## Ops note

cot-exporter EC2 i-0643a5bee8a8feabf STARTED via cot-bd-session-trigger (session-refresh, async) to refresh the idle-dead BD session (was session_live=false, captured 02:00Z) for the read-only probe. New session captured 13:48:48Z. EC2 left RUNNING (stop needs confirmation; will be used by the nightly). No writes to the cot data plane (probe did not land_to_s3).
