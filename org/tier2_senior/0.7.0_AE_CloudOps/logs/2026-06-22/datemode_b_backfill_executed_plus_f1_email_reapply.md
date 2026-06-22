# DATEMODE-B fix executed to bronze-backfill gate + F-1 email re-apply

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

Window: ~13:55Z (prior log) -> ~14:33Z. Serial: 0.7.0_AE_CloudOps. TO: ADVI_COTETL.AUAFIX-DATEMODE-B (LEAD).
Continues the morning's COTETL CurrentDay-bug diagnosis (prior log) into the FIX execution.

## Current State

**ADVI_COTETL.AUAFIX-DATEMODE-B (LEAD) -- bronze backfill DONE + verified; silver handed to DS; nightly = binding verify.**

The fix (CTO L2-ruled): cot holdings/alloc/unrealized BD templates were CurrentDay -> mis-stamped live data early-June -> ~$24M/6.5% served-AUA understatement. Fix = CurrentDay->Custom + backfill. Lane split: AE template re-provision + backfill; DS TABLE_DATE_MODE code (Rule 13).

Executed this window:
1. VERIFIED all 3 tables return correct per-date via Custom probe (alloc 06/18 $776.4M, unrealized 06/18 $385.4M, holdings done prior).
2. RECONCILED 2 stale TO assumptions to CTO+COO (both ACCEPTED): (a) in-place dateRangeType flip (keep templateId) supersedes "update templateId" -- the fresh-create 500'd, CTO 140041Z; (b) DS's repo-drift catch -> templates fold into DS's ATOMIC bronze push (supersedes "AE-first" gate; both half-states broken so atomic required).
3. HANDED DS the final inputs: tuple ("Custom",14) all three (DS's holiday-gap argument: 3d misses 06-18 over Juneteenth; 14 = gap floor, not restatement lookback); exact diff = dateRangeType "CurrentDay"->"Custom" in templates/{holdings,allocations,unrealized}.json, templateIds 226355/226334/False preserved.
4. DS deployed atomic code+templates MATCH (commit a7a4d974c).
5. VALIDATION run (deployed Custom code, named SSM doc opal-cot-bronze-run RunDate=2026-06-18 Table=holdings): landed HOLDINGS_DAILY_2026-06-18.xlsx stamped EndDate=6/18 Custom (was 6/8). Deployed path confirmed.
6. FULL BACKFILL (SSM RunShellScript loop 9ffbd47e over the DEPLOYED script, sequential, 21 runs = 7 biz days 06-10..06-18 x holdings/alloc/unrealized): rc=0, 21/21 OK. Spot-check holdings: 06-10 EndDate 6/10 $373.2M / 06-15 6/15 $390.5M / 06-18 6/18 $397.7M -- distinct dates, advancing MV = correct per-date snapshots.
7. FLAGGED DS 2 silver-merge gotchas that would silently no-op: (a) incremental merge dedups by FILENAME; backfill overwrote files already in manifests (alloc 5: 06-12/15/16/17/18; unrealized 4: 06-15/16/17/18 from old CurrentDay pulls) -> force-reprocess needed; (b) holdings excluded from _SILVER_STAGE_TABLES -> needs a separate holdings silver merge. Without these, the freeze persists despite corrected bronze.

**F-1 SNS-egress path (a):** safe-applied globgrph/item2c_surface_alarm.tf critical_surface_alerts_email re-create (1 added/0 destroyed, targeted, complete in-session). Verified live: opal-critical-surface-alerts email sub back as PendingConfirmation (+ SMS retained). Andrew-gated (click confirm -> verify Delivered>0).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | (Rule 21 reflex, SNS-delivery) | GAP | no comp tool for SNS delivery -> raw cloudwatch (rail honored) |
| safe-apply.sh | globgrph -target=critical_surface_alerts_email apply | PASS | HALT-gate clean; 1 added/0 destroyed |
| (BD probe / SSM) | Custom holdings/alloc/unrealized probes + opal-cot-bronze-run + RunShellScript backfill | PASS | operational aws (free per Rule 21); the decisive empirical + the deployed-path backfill |

**What worked:** verify-before-bulk (single validation run before the 21-run backfill caught nothing wrong but de-risked); catching the FILENAME-dedup silver no-op before handoff (would've silently failed the whole fix); reconciling the 2 stale TO premises rather than executing them blind (the fresh-create 500 / repo-drift). **What failed:** nothing this window. **Gap:** comp-freshness/comp-pipescript still cot-blind (raw aws for cot ground-truth); no comp tool for SNS delivery or BD-source asOfDate.

## Blockers

None blocking me. DATEMODE-B binding verify is GATED (not blocked) on: DS silver force-reprocess -> then tonight's scheduled nightly gold -> served AUA past 06-09 + ~$397.7M (review tomorrow-AM, no overnight watcher). F-1 Andrew-gated (email click).

## Next Steps

- **[0.4.0_DS_ClientPlatform]** silver leg: force-reprocess the 9 already-listed backfilled files (alloc 5 + unrealized 4) + separate holdings silver merge -> silver gains 06-10..06-18 partitions. (Flagged precisely.)
- **[0.7.0_AE_CloudOps]** TOMORROW-AM: verify served cot AUA data_as_of past 06-09 + total_aua ~$397.7M on the nightly's served artifacts (binding verify); fold in the A_00 forward-tripwire (must rewrite after 06-23 lands a new txn file). RAVC COO.
- **[Andrew]** F-1: click the critical-surface email confirm link (re-sent). Then I verify Delivered>0 + ping AE0.6 to re-verify the 4 SS4c alarms deliver.
- **[0.6.0_AE_PartnerETL]** drafting the watch-the-watcher critical-surfaces.yaml limb (deliverable-asserting) for my review+commit.

## Ops note

cot-exporter EC2 i-0643a5bee8a8feabf left RUNNING (CTO+COO confirmed -- nightly + the backfill used it; BD session refreshed 13:48Z stayed live through the 21-run loop). No writes to the cot data plane beyond the sanctioned forwardfill_v2 bronze backfill (deployed ingest, not ad-hoc inline).
