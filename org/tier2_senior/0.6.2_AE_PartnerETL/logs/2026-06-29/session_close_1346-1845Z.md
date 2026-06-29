# 0.6.2_AE_PartnerETL — session-close log 2026-06-29 (~13:46Z->18:45Z)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, DIAGNOSE, COORDINATE

## Session: two deliverables shipped + accepted -- 49f durable-auth port + freeze recovery, and the Schwab Quartz/SI2 EC2 de-risk spike. This is the capstone; the two work bodies have detailed logs (below).

Detailed logs (already committed):
- `bdapimig_p1_durable_49f_boxpull_unfreeze.md` -- 49f durable port LEG0->LEG2 (grounding, arch-gate, deploy, live re-mint).
- `schwab_ssot_derisk1_quartz_ec2_spike.md` -- the full Schwab Quartz/SI2-on-EC2 spike.

This capstone records the UNLOGGED middle band (the 49f silver-recovery + 1a steady-state tail) + the session arc.

### 49f silver freeze-recovery + 1a steady-state (the tail not in the LEG2 log)
- Fired the off-cycle bd-49f-runner (COO freeze-recovery GO, NEVER#4-clear): auth OK with the fresh cookie -> forwardfill_v2 4/4 fresh (CRS... 2026-06-29) S3-verified. cookie->runner->bronze proven e2e.
- bd_silver was a SEPARATE blocker (DS-owned merge). De-risked a location mismatch: the silver SSM docs fetch s3://opal-data-bd/SCRIPTS/merge-daily-incremental.py (stale Apr-17 crasher) while DS deployed the ASCII-fix to CODE/SILVER/. DIFFED them -> the only delta was DS's own 12cc7e111 fix (no deploy-only edits) -> safe to refresh; 0.7.0 synced scripts/ (md5 418d6225, I verified the served object). Grounded the silver runtime = per-table TF boxes (bd-transactions/allocations/fees/assets, stopped) started by bd-transaction-pipeline-trigger cron(53 21) = tonight 21:53Z. Both root causes (cookie + scripts) verified-fixed -> COO ruled (my rec) the 21:53Z nightly closes AC#3 NEVER#4-clean (no manufactured off-cycle silver run -- it's purely mechanical, nothing to prove).
- Delivered base the 1a ephemeral-re-auth chain contract (mint-invocation recipe from LEG2 cmd e748132b + the cot-OTP-span ~15-20min -> cron(0 0) stagger numbers). base wired it LIVE (bd-v2.39.2): bd-49f-session-daily cron(0 0) -> session-trigger -> opal-bd-49f-session-fetch -> on-success bd-49f-runner; runner-daily cron(0 2) DISABLED (collision gone). Paired the verify: step (a) mint PROVEN (captured_at 14:15:15Z -> 15:20:47Z autonomous).
- GROUNDING CORRECTION (live-falsified my own claim): device-trust does NOT skip OTP -- the 1a mint injected bd_DeviceRegistration but BD still challenged MFA -> gateway fetched the code -> shared-mailbox WAS contacted. So the STAGGER is the load-bearing firm-sep mechanism, NOT OTP-skip. Corrected the banked memory. GATE-B cross-firm lock = designed (09d0883cd) but build HELD (CTO thin-tether; stagger replaces it).
- Closed side-loops: comp-freshness firm-shorthand fix (CVO f613a470e, committed) + all 3 CVO proxy-drift residuals (re-verified map==territory).

### Schwab Quartz/SI2 spike -- see the dedicated log
SI2-on-EC2 proven (720MB June->S3), durability proven, fully-unattended UI-automation pipeline built (no CLI/scheduler-service exists), 5 PRD findings, Path-C rec. RAVC-ACCEPTED COO 183610Z; TO complete (d6f3c7d01). Box persistent (Andrew-direct).

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-iam service bd-49f-auto-login-role | LEG2 IAM pre-flight | PASS (covered in LEG2 log) |
| comp-freshness bd / chain bd | read the bd silver freeze status (post the firm-shorthand fix I committed) | PASS-as-tool / FINDING: silver transactions/realized/unrealized FAIL ~64h (frozen); used it to ground the unfreeze need |
| deploy_ledger.py | LEG2 box-pull (covered in LEG2 log) | CLOSED 4/4 |

**What worked:** `comp-freshness bd` (the shorthand I committed this session) gave the decisive silver-freeze read. Grounding served objects over self-reports throughout (the scripts/ md5, the forwardfill landing, the S3 milestone) caught the stale-prefix mismatch + made the nightly-closes-it call trustworthy. **Gap:** comp-freshness has no Schwab coverage (the Quartz spike was off-rail by design -- a net-new Windows-EC2 build no comp-tool models; noted in that log).

## Blockers
None. Two scheduled external gates remain (not blockers): 49f AC#3 silver (tonight 21:53Z nightly) + the first Schwab with-files run (tomorrow 12:00Z) -- both fire automatically; I verify the served evidence.

## Current State (handoff)
- **49f:** durable port DONE+ACCEPTED; 1a chain LIVE (cron(0 0) stagger, runner-daily disabled); cookie fresh (captured_at 15:20:47Z); forwardfill fresh; scripts/ fixed (418d6225). AC#3 silver closes on the 21:53Z per-table nightly. GATE-B lock designed (09d0883cd) build HELD. Open finding: device-trust OTP-skip not honored by BD (affects cot too) -- non-blocking follow-on.
- **Schwab:** box i-0f3d57a97f14727af (PERSISTENT, 3.89.31.201) running 3 scheduled tasks (SchwabAutoDownload daily 12/16/20Z, SchwabS3Sync 30min, SchwabKeepConsole 5min). Validation prefix opal-data-schwab/01_raw_quartz_validation/ (720MB landed). Creds schwab/sdd-credentials, acct 08242234. RDP scoped to Andrew's IP.

## Next Steps
- **[0.6.2 self]** verify Schwab with-files run tomorrow 12:00Z (served S3) + tune dismiss timing if needed -> RAVC COO.
- **[0.6.2 self]** verify 49f AC#3 silver on the 21:53Z nightly (comp-freshness bd PASS, served) -> RAVC COO; closes base's 1a-(c) + the authtoken-dead retirement.
- **[Andrew/CTO]** Schwab cutover-prefix decision (validation vs 01_raw/) + the Schwab enterprise-MSI (Path-C) ask. **[2.0.0_SA_COO]** GATE-B lock TO (held). **[0.7.0_AE]** the device-trust-OTP-skip follow-on (cross-firm).

## MCP traffic
~50+ messages this session (the heaviest coordination band of the day). Significant: COO GO + 2 RAVC-ACCEPTs (49f port, Quartz) + the silver-runner GO + nightly-close ruling; CTO arch-gate (C1/C2/Q4 + GATE A/B split) + 2 RAVC-ACCEPTs; CVO 3-loop close + the comp-freshness fix; 0.7.0 1a-chain-wire + blast/bearer gates + silver-runtime ground-truth; DS silver coordination; UA 0.0.1 x3 SI2 feasibility consults.
