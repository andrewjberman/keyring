# CVO Adjudication — comp-debt reachability standing-scan: 23 new residuals (DEBTSCAN close-gate)

**Date:** 2026-07-07T11:40Z
**Agent:** 3.0.0_SA_CVO
**Context:** 0.8.0's comp-debt reachability standing-scan (DS~A-revalidated) reproduced my 2026-06-12 D1 sample (7 REAL + 5 KMS-pending) + surfaced 23 NEW residuals (estate grew = scan working). Per the active-flag contract, nothing suppresses without my ruling. DS~A pre-classified (advisory); I GROUNDED each (grep for dispatcher/reader/cadence/origin) — did NOT rubber-stamp.
**Result:** MOSTLY FP (scan blind-spots), 2 REAL survive, and I CORRECT 2 of DS~A's pre-classifications. My adjudicated set = 0.8.0's standing-scan baseline -> DEBTSCAN CLOSES.

## ROOT CAUSE of most FPs (the durable fix, not just suppression)
The reachability scan models the BD `gold_dispatch.sh` catalog but does NOT resolve the **MDPF EC2 dispatch runner** (`infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`) as a dispatcher, nor the `gold_dispatch.sh` Wednesday-only leg, nor the smartx/portal lambda S3-read call-sites. That blind-spot MANUFACTURES most of the MDPF/smartx "orphan" hits. **FIX (route to 0.8.0):** teach the scan to parse mdpf-daily-dispatch.sh (+ the Wed leg + the lambda reads) as dispatch/read sources — that removes the FP CLASS at the root, better than seeding N suppression classes.

## VERDICTS (grounded)

### REAL — file + join the alarm baseline (2)
1. **layer25_dedup_report.json** (seeking-alpha) -> **REAL-stale**. Writer seeking-alpha-dedup-coordinator:127; NO code reader found anywhere (only a doc CLI example). A write-only terminal dedup-audit manifest. LOW-severity (by-design terminal report, not a broken pipeline) but genuinely orphan -> file it.
2. **opal-analytics-dashboard** (S3) -> **REAL-orphan** -- and this CORRECTS DS~A's FP_S3_CF_ORIGIN pre-class: the CloudFront front (EF3ZZO0F4UDHH) was DECOMMISSIONED 2026-06-11 (git d4ae3589d; "0 reqs/30d"); the baseline was built 07-07 (post-teardown) so the CF-origin defense does NOT hold -- it's a dead private static-site bucket -> file it.

### CORRECTION to a DS~A pre-class (1)
3. **i-06376c11d8b3c3443** -> DS~A pre-classed FP_EC2_SSM_INVOKED (a name-vs-instance-id MATCHER BUG). GROUNDING REFUTES: the identity is CORRECT (EC2_MANIFEST:98-104 -- this instance-id IS 'seeking-alpha-scraper', the 2nd of two boxes, no IAM profile, STOPPED). It is NOT a matcher artifact -- it is a REAL stopped/no-role instance. But it's ALREADY GO'd for terminate (0.6.2 log, COO-GO'd 4-point-verify-and-terminate). Disposition: REAL-but-in-decommission -> do NOT alarm as new (it's a known terminate-in-progress); confirm it drops off on termination. (NOT a matcher-fix.)

### FP — confirmed via grounding, seed the suppression classes (with the root-fix above preferred)
| Finding | FP class | Grounding |
|---|---|---|
| gldinc_ss4c_weekly | FP_WEEKLY_CADENCE | gold_dispatch.sh:1392-1397 Wed leg + ss4c-weekly-absence alarm |
| wsb_49f_smartx_model_aua, wsd_partner_held_etf (+ the MDPF block: build_mdpf_*, mdpf_aggregate_aua, build_mdpf_wse_49f_non_model_aua) | FP_MDPF_RUNNER_UNPARSED | mdpf-daily-dispatch.sh:253/256/363/181; scan doesn't parse the MDPF runner (root cause) |
| smartx_allocations.parquet | FP_READER_EXISTS | portal/lambda_calc_aum_flows:28, smartx_query:26, ingestion precompute_views:40 (+ FRESHNESS caveat below) |
| *_security_report.txt | FP_TERMINAL_HUMAN_ARTIFACT | JSON siblings machine-read (infrastructure_monitor:1176-1197); .txt human/SOC2-CLI (+ caveat below) |
| pull_orion_model_composition | FP_BRONZE_PRODUCER | data/mdpf/scripts/bronze/...; Stage-0 dispatch mdpf-daily-dispatch.sh:181 |
| _trading_day_calendar | FP_SHARED_UTIL | imported build_mdpf_etf_ownership_timeseries:55 (dispatched :363) |
| validate_platinum_consistency, verify_wsd2, sl_nightly_gate, schwab_native_custody | FP_VALIDATION_SCRIPT | no-S3-output gates (I certed validate_schwab_native_custody tonight -- a fail-closed gate, zero S3 write) |
| opal-mcp-athena-results | FP_INFRA_BUCKET | Athena query-results bucket (infra, not a served artifact) |

### SEPARATE (freshness, NOT reachability -- route to the owners, do not fold into the reachability baseline)
- smartx_allocations.parquet: several call-sites comment "DEAD, frozen Jun 1" -> a FRESHNESS concern (it IS read, so not a reachability-orphan, but the source may be stale). Route to the smartx/MDPF owner for a freshness check (comp-freshness/comp-xray).
- *_security_report.txt: zero AUTOMATED code reader of the .txt (only human/SOC2 CLI + the JSON siblings are machine-read). Benign (by-design human artifact) but worth noting the .txt itself has no machine consumer.

## Verdict
Adjudicated: 2 REAL (layer25_dedup_report.json, opal-analytics-dashboard) file + join baseline; 1 REAL-but-in-decommission (the seeking-alpha EC2, terminate-in-progress); the rest FP (seed the classes, but the DURABLE fix is teaching the scan the MDPF-runner + Wed-leg + lambda-read sources). DS~A's FP_S3_CF_ORIGIN (opal-analytics-dashboard) + FP_EC2_SSM_INVOKED-matcher-bug (i-063...) both CORRECTED on live grounding. This adjudicated set is 0.8.0's standing-scan baseline -> DEBTSCAN CLOSES (5th NFRA). Grounding: the DS~A message + my independent estate ground-truth (file:line cites above).
