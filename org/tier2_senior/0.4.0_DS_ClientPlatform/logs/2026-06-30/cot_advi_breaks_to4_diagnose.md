# ADVI_BREAKS TO-4 / TO-4b — Cottonwood (cot) served-AUA freeze: DIAGNOSE (read-only)

**archetype:** DIAGNOSE
**agent:** 0.4.0_DS_ClientPlatform (base; cot standing lane) | **date:** 2026-06-30 | **window:** session start (~12:44Z) -> ~13:47Z

## Summary

Spawned toward DATA_SSOTMG TO-1/TO-3, but an Andrew-sovereign PRIORITY-OVERRIDE landed mid-spawn: NEW #1 = fix the pipeline LOGIC for Inflection + 49F + Cottonwood, nothing else until all three confirmed. DATA_SSOTMG TO-1/TO-3 HELD. COO dispatched me the cot lane: ADVI_BREAKS (the P0 gate PRD, CTO d2cae58f9) TO-4 (Cottonwood DIAGNOSE) + TO-4b (root-ground). Entire session READ-ONLY (no cot re-run / write / fix); all fixes held for the CTO+COO+Andrew gate.

DELIVERED: full cot freeze diagnosis, grounded source + S3 forensics + AE runtime logs, with one honest mid-stream self-correction. cot resolves to TWO SEPARATED ROOTS + the Andrew-flagged cot-vs-49F divergence assessment + the e2-alarm/TO-6 reframe.

## What was found (the diagnosis)

**ROOT 1 — HOLDINGS (the AUA driver): BD-side $0-price pricing-lag, NOT a producer bug.**
- Served `platinum/firm/header_metrics.json` is MTIME-fresh (rewritten nightly 06-30T02:19Z, 728B every night) but CONTENT-stale: `data_as_of=2026-06-26`, `aua=432,464,116.36`. NOT the inf 132B stub-clobber (single writer/night, no size collapse).
- Chain: `forwardfill_v2/holdings/HOLDINGS_DAILY_{date}.xlsx` (BD DataMining qt1 snapshot) -> cot_silver_merge -> `silver/holdings/{date}.parquet` -> B_00 canonical_holdings -> C_03 account_performance (snapshot-first) -> `D_00.portal_aggregates.py:690` `data_as_of = perf['date'].max()` -> D_04 -> served. D_00 HONESTLY serves the latest COMPLETE holdings (06-26).
- Binding mechanism = the INGEST source-completeness guard `cot_bronze_ingest.py:449-455` (`_holdings_nonzero_mv_fraction < 0.5` floor): BD returns the 06-29 holdings ALL $0-priced -> guard REJECTS (no land, no bronze) -> served pins to last-priced (06-26). AE log confirmed verbatim: `REJECT: holdings @2026-06-29 non-zero-MV 0.0% < 50% floor`. Sidecars (`forwardfill_v2/holdings/_complete/`) show 06-23..06-26 priced (nzf 0.85) only on the 06-30 retry-net sweep = a multi-day BD T+N pricing lag. Login + firm-context + trigger ALL healthy (BD session secret LastChanged 06-30T02:03Z; both nights `auth OK (firm=cottonwood)`). NOT a dead session, NOT firm-scope.
- => No pipeline fix. The freeze is BD's pricing cadence (BD prices snapshots T+N; our 02:00 UTC pull catches the still-$0 newest date). Disposition: accept + retry-net self-heal (works) + LOUD alarm + (optional) shift the pull later. Residual lag tolerance = an Andrew product call (CTO asked Andrew).

**ROOT 2 — UNREALIZED (secondary, feeds B_00 CUSIP->asset_name bridge): OUR OWN regression.**
- `forwardfill_v2/unrealized/` collapsed from 10.7MB (06-21) to 3743-byte stubs every date since 06-22. Template version-diff (`code/bronze/templates/unrealized.json`, 2 versions): the ONLY 06-22 change = `dateRangeType: CurrentDay -> Custom` (facts/levels identical) = the ADVI_COTETL.AUAFIX-DATEMODE fix (CTO L2, cot_bronze_ingest.py:88-92) that un-froze the 06-09 holdings/alloc AUA freeze. It fixed holdings/alloc but REGRESSED unrealized (qt4) to empty.
- Mechanism: unrealized.json has `templateId=False` (create-per-run). Under CurrentDay create-per-run returned full data; under Custom+create-per-run it returns EMPTY. AE confirmed: the xlsx has ZERO `<row>` elements. (holdings works under Custom because it has a persisted templateId 226355.)
- => Targeted fix (CTO co-signed, gated): PROVISION a persisted templateId for unrealized (mirror holdings 226355). NOT a CurrentDay revert (would re-freeze asOfDate). Apply conditions: STEP-1 `--provision` BD-write on COO apply-GO; STEP-2 verify-before-wire (non-empty qt4 under Custom, Rule 22); STEP-3 ds-gate the templates/unrealized.json change + RAVC CTO the verify result before serving.

**cot != 49F (AE cousin test AGREE):** cot = BRONZE $0-price-lag (snapshot method), 49F = GOLD D_03 composition-empty (lots method, served frozen 06-26T05:00). Separate layer/signature/fix — do NOT cross-apply. Andrew-flagged divergence table (7 items: method, custodian firm-context, shared-C_03-different-branch, nzf guard [cot fails safe / 49F fails open], AUAFIX date-key sensitivity, B_00 CUSIP bridge, short-history) sent to CTO 133057Z. REST-fidelity verdict: cot $0-price = a FRESHNESS/pricing-lag on a populated field (template DOES request Market Value; 06-23..26 priced fine), NOT 49F's is_open PERSISTENT field-coverage gap — different classes; possible shared THEME = REST pull-timing < old scrape.

**cross-lane (~B 49F):** answered ~B's unrealized cross-check (134646Z) — cot unrealized-empty = BD DataMining template date-mode edit + templateId=False; shared CODE/silver-engine (merge-daily-incremental.py is BD_S3_BUCKET-parameterized), per-firm template. Gave ~B the disambiguator (49F empty at BRONZE xlsx = shared template fragility + same fix=provision; vs only SILVER = 49F-specific merge). COO confirmed 49F's ENTIRE freeze traces to empty unrealized via B_01 CUSIP bridge -> unrealized-empty is load-bearing, shared-fix-pattern leverage across both firms.

**TO-6 (prevention) reframe:** the e2 pricing-defect alarm is FULLY WIRED — retry-net runs nightly (ssm.tf:140), `COT_DETECTION_SNS_ARN` set (ssm.tf:137) -> topic `opal-bd-cot-cookie-alerts` with a CONFIRMED email sub to andrew@opalinvest.com. The freeze was silent NOT from missing wiring but from `CADENCE_BDAYS=2` (06-29 within honest-lag). Reframed TO-6 for 0.8.0~B = (a) tune cadence to Andrew's tolerance + (b) add a SERVED-as_of-freshness alarm on the platinum artifact (fires on the symptom Andrew watches).

## MCP traffic

~30 messages (COO/CTO/AE/~B). Significant: COO TO-4 GO + TO-4 sharpens + TO-4b GO + apply-GO HELD-pending-Andrew; CTO RAVC-accepts (TO-4, TO-4b root, cot-assess) + arch-gate + unrealized provision co-sign (verify-before-wire); AE ingest-log clincher (holdings REJECT line + unrealized 0-rows + cousin AGREE); ~B 49F<->cot unrealized cross-check answered. RAVC loops: all opened-and-closed within window except the apply-GO (held for Andrew) + the fix-applies (gated).

## Compiler Tools

| run | result | note |
|---|---|---|
| comp-freshness cot | PASS-as-tool | confirmed served header/timeseries CONTENT-STALE @06-26 vs silver fresh; date-key vs content divergence surfaced |
| pipescript --resource header_metrics.json | PASS | producer = cot-pipeline (advi-cot) + advi-bd publisher |
| comp-pipescript io D_00.portal_aggregates.py | PASS | 15 reads / 5 writes; pinned ACCOUNT_PERFORMANCE <- C_03 as the perf source |
| comp-grep (header_metrics / data_as_of / COT_DETECTION_SNS_ARN / backfill-holdings-net) | PASS | located producers, as_of resolution, e2-alarm wiring |
| comp-to ADVI_BREAKS.TO-4 | OK | race-free per-session TO_ID set |

What worked: comp-freshness's MTIME-FRESH/CONTENT-STALE flag immediately disambiguated cot from the inf clobber; comp-pipescript io pinned the perf source in one call. What failed: none. Gap found: comp-freshness reports silver by date-KEY (run-date), which diverges from the real content frontier — a raw `s3 ls` partition enumeration was needed (rail-checked) to find the true 06-26 holdings frontier; comp-freshness could expose a content-vs-date-key flag. Raw aws (s3api list-object-versions / s3 ls forwardfill_v2 / sns list-subscriptions / secretsmanager describe-secret) used read-only with inline `# rail-checked:` markers for the version/partition/subscription forensics no comp-tool covers.

## Briefs written

None — read-only DIAGNOSE; findings delivered via RAVC2 messages + this log. (cot seam-doc update HELD per COO.)

## Blockers

None hard. STEP-1 unrealized provision-run is HELD ~30min pending Andrew's fix-GO posture (COO surfacing as the forcing instance of BD-write fix-GO discipline — a sequencing hold, evidence-cited, not a defect block). All fixes gated CTO+COO+Andrew.

## Current State (handoff)

- cot TO-4/TO-4b DIAGNOSE COMPLETE + accepted by CTO + COO; runtime-confirmed by AE log.
- TWO roots: (1) HOLDINGS = BD T+N pricing-lag (no pipeline fix; gate/product decision + LOUD alarm); (2) UNREALIZED = our 06-22 AUAFIX-DATEMODE CurrentDay->Custom flip + templateId=False (targeted fix = provision persisted templateId; CTO co-signed verify-before-wire).
- Unrealized fix sequence on COO apply-GO: STEP1 `cot_bronze_ingest.py --table unrealized --provision` (BD metadata write) -> STEP2 verify non-empty qt4 under Custom -> STEP3 ds-gate templates/unrealized.json + RAVC CTO before serving.
- TO-6 (0.8.0~B): e2 alarm wired+subscribed-to-Andrew; reframe = tune CADENCE_BDAYS + add served-as_of-freshness alarm on platinum/firm/header_metrics.json.
- Files of record (read, not modified): data/cot/scripts/bronze/cot_bronze_ingest.py (ingest+guard+retry-net), cot_bd_session_fetch.py (session, healthy), data/cot/scripts/gold/{D_00:690, C_03:234-258}, code/bronze/templates/unrealized.json (Custom+templateId=False), infra/aws/terraform/cot-pipeline/ssm.tf:137/140.

## Next Steps

- **[2.0.0_SA_COO]** relay Andrew's fix-GO posture -> apply-GO STEP-1 unrealized provision. Sequence the holdings gate/product decision (BD-lag tolerance) to Andrew.
- **[0.4.0_DS_ClientPlatform]** (me, base) on COO GO: execute STEP1-3 unrealized provision-fix (verify-before-wire); RAVC CTO the verify result before serving.
- **[1.0.0_SA_CTO]** holds the holdings arch-gate (BD-pricing-cadence); surfacing the residual-lag tolerance + pull-timing to Andrew.
- **[0.8.0_AE_CloudComp~B]** TO-6: tune CADENCE_BDAYS + add served-as_of-freshness alarm (reframed scope delivered to COO 134445Z).
- **[0.4.0_DS_ClientPlatform~B]** 49F<->cot unrealized cross-check: confirm 49F bronze-xlsx empty + template Custom+templateId=False -> shared provision-templateId fix pattern.
- **[0.7.0_AE_CloudOps]** (optional) old-scrape vs REST pull-timing comparison for the holdings pull-timing lever (gated).
