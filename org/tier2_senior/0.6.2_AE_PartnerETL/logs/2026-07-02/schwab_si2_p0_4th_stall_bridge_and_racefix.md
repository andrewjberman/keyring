# 0.6.2_AE_PartnerETL - Schwab SI2 P0 (4th stall): grounded fork -> 07-01 bridge -> sync-race root-fix

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, COORDINATE
**Date:** 2026-07-02 | **Window:** ~14:40Z -> 15:24Z | **Serial:** 0.6.2_AE_PartnerETL (SI2 download owner)

## Summary
Andrew-direct P0 (4th ETL stall): "Schwab raw download STUCK @06-30; box i-0f3d57a97f14727af STOPPED." GROUNDED the fork against live state and FALSIFIED the premise (Rule 22): box is HEALTHY, schedule is FIRING, and Schwab HAS POSTED 07-01. The prod-@06-30 was STRUCTURAL (box runs-to-validation-prefix + held repoint + unfed OneDrive), not a failure. Executed the Andrew-GO'd one-off 07-01 silver bridge (6 tables, CVO-verified) and deployed the DURABLE root-fix for the underlying sync-race that caused the stall. 4th stall RESOLVED.

## Work done (chronological)
1. **Grounded the fork (DIAGNOSE, live-state):**
   - Box i-0f3d57a97f14727af = **running** since 2026-06-29T15:41:15Z (LaunchTime UNCHANGED -> never stopped; CVO "box stopped" falsified; CVO later confirmed they'd described the wrong instance, the BUILD box i-0ed92ce2e72f505dc).
   - EB rule `canonical-schwab-si2-download-schedule` ENABLED, cron(35 8,20). CloudWatch AWS/Events: 4 clean Invocations (06-30 20:35Z / 07-01 08:35Z / 07-01 20:35Z / 07-02 08:35Z), 0 FailedInvocations. Box `eventbridge-cycle.log`: every cycle download+sync lastResult=0x0.
   - **Vendor POSTED 07-01:** full CRS20260701.* (11 files incl RLD) on the box local delivery folder, written 07-02 08:37:33Z by the 08:35 EB cycle's SI2 "Download all new files".
2. **Found the REAL bug (the sync race):** click-download.ps1 exits 08:35:57Z (popups quiesce) ~1.5min BEFORE the SI2 GUI finishes async writes (08:37:33Z); the same-cycle sync ran 08:36:30Z and raced PAST CRS20260701. Immediate fix: re-fired SchwabS3Sync -> CRS20260701 (11 files) into `01_raw_quartz_validation/`, S3-verified 14:51Z.
3. **Parity gate (CVO gate-1):** proved box-path == OneDrive-path -- CRS20260629 full-set (all 11 ext) BYTE-IDENTICAL across prod `01_raw/` (OneDrive-sourced) vs validation prefix (box-sourced); 06-30 ACC+TRN identical. Scope = 08242234-only. No prod divergence.
4. **Executed the 07-01 bridge (DEPLOY, Andrew-GO Option A via COO+CVO):** promoted 11 CRS20260701.* validation->prod `01_raw/` (server-side, SSE AES256) + RPS->`bronze/rps/`; ran the 6 converters. TRN Layer-A reads LOCAL OneDrive (floored 06-30) so it no-op'd -> staged the parity-verified 07-01 TRN + used `--src-dir` override (NO OneDrive write); then TRN-NNA. All 6 silver tables date=20260701 S3-verified non-zero. CVO independently verified: custody $1,604,173,986.44 (DoD -0.24%, sane).
5. **Deployed the durable sync-race root-fix (DEPLOY):** schedule.tf EB-cycle now waits for delivery-folder QUIESCENCE (90s write-stable after new data; 8min no-data early-out; 20min cap) between download-exit and sync kick. commit 61b8722e0 -> safe-apply (HALTGT ok, 0-diff) -> tag canonical-schwab-si2-schedule-v1.1.0 -> pushed.
6. Ledger indexed via deploy_ledger.py (3 legs proven, CLOSED). Skill Last-known-state -> 20260701 + banked the TRN-A-local-disk gotcha (commit c6c7f4050).

## Deployment Sequence + Verification (AE)
| Step | Action | Verification (actual) |
|---|---|---|
| Bridge L1 | promote 11 CRS20260701.* -> prod 01_raw/ + RPS -> bronze/rps/ (SSE AES256) | `aws s3 ls 01_raw/ \| grep CRS20260701` = 11 files; bronze/rps/CRS20260701.RPS=79365491B |
| Bridge L2 | 6 silver converters (acc/rps/trn/trn_nna/uln/rld) | all rc=0 ERR=0; rps 91,387 pos / uln 263,192 lots / etc. |
| Bridge L3 | S3-verify silver date=20260701 | acc 429002 / rps 1514336 / trn 439789 / trn_nna 12273 / uln 13598934 / rld 912513 B (all non-zero) |
| TF fix | schedule.tf quiesce-wait | safe-apply "Apply complete! 0 added, 1 changed"; re-plan "No changes"; tag v1.1.0 pushed |

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| (none of comp-freshness/comp-pipescript/comp-iam) | n/a | see note |

**Why minimal:** this was a LIVE-STATE grounding + raw/silver data bridge + EB-infra deploy -- the correct grounding surface is live AWS/S3/SSM/box-filesystem (F5: verify against served/live, not graph). The comp freshness/pipescript/iam tools are gold/platinum/code/IAM-scoped; my layers were raw-ingest, silver, and an EB target Input (no IAM change). Repo inspection used native Grep/Read. The cross-prefix raw byte-parity checks (no comp-tool fits) carried inline `# rail-checked:` markers (logged). **Gap:** no comp-tool verifies (a) a SILVER date= partition non-zero, or (b) cross-prefix raw-file byte/ETag parity -- both are recurring AE needs; candidate comp-tool coverage.

## Blockers
None. The one genuine gate (Option A brushing Andrew's Caution-B N=5 repoint hold) was correctly ESCALATED not self-authorized -> Andrew GO'd via CVO; released by COO+CVO. Not an assumption-block.

## Current State (handoff)
- **prod `s3://opal-data-schwab/01_raw/`** now has CRS20260701.* (11 ext, bridged one-off); `bronze/rps/CRS20260701.RPS` present. Validation prefix `01_raw_quartz_validation/` current thru 07-01.
- **`s3://opal-data-bd/schwab/silver/{acc,rps,trn,trn_nna,uln,rld}/date=20260701/`** all non-zero (CVO-verified). rps custody $1,604,173,986.44.
- **schedule.tf** (infra/aws/terraform/canonical-schwab-si2-schedule/) deployed w/ quiesce-wait; tag canonical-schwab-si2-schedule-v1.1.0; next EB cycle 20:35Z uses it. Box i-0f3d57a97f14727af running; EB rule ENABLED.
- **HOLD INTACT:** Andrew's N=5 standing-repoint hold + OneDrive going-forward prod path UNCHANGED. The bridge was a dated catch-up only.
- **Ledger:** org/critical_paths/change_management/20260702T1515Z_mdpf-schwab-silver-rollforward-0701-bridge_deploy_completion.md (CLOSED).
- **GOTCHA banked:** convert_schwab_trn_to_parquet.py reads LOCAL OneDrive (DEFAULT_SRC_DIR) -> a bridge advancing only S3 no-ops TRN-A; use `--src-dir`.

## Next Steps
- **[0.6.1_AE_*/3.0.0_SA_CVO]** ONLY open fabric item: inf-sentinel (~16:00Z) -> mdpf auto-fires -> WS-E reads schwab/silver/rps/date=20260701 -> served 49F custody=07-01 -> CVO per-field parity. NOT my leg.
- **[0.4.0_DS_ClientPlatform~A]** TRN-A -> S3 01_raw/ durable re-point (C3, CTO-approved, WS-2 Phase-1). I support, not double-drive.
- **[0.6.2 self]** P1-DURABLE: fold 0.7.0's bd_49f_auto_login Kimi-health-guard + DOM-fallback rec (non-urgent, self-healing). Optionally run Step-7.5 canonical build for 07-01 if canonical store must match silver (flagged, not P0).

## MCP traffic
~18 messages. Significant: MSTR-DIRECT P0 dispatch (in) + MSTR RAVC-VALIDATE (in, accepted); RAVC determination -> CVO+COO+MSTR (out); Andrew GO Option A via CVO+COO (in); CVO independent bridge verify PASS (in); COO ledger-index DRIVE + ACK (in/out); CTO arch-gate RAVC (out). DS~A two-path map corroboration + D-C TRN-set confirm (both directions).
