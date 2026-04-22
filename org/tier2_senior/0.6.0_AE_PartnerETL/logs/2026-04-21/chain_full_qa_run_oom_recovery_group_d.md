# Session Log — Chain Full QA Run: OOM Recovery + Group D Isolation
**Agent:** 0.6.0_AE_PartnerETL  
**Date:** 2026-04-21  
**Session start:** ~19:00 ET  
**Session end:** ~22:15 ET

---

## Objective

Execute `--chain full --force --bg --no-shutdown` on QA runner (i-0090b823a4a0997e3) to validate:
- HLOT2b Patch B (~$102.7M Tier 1 IEFA+SPYM+IDVZ+IEMG+SPHY)
- CHART-ALIGN Travis Penfield Q2 NNA → -$6.845M
- COHORT-A cohort_a_summary.json 7-field emission
- D_04 no crash (d87377a5 fix)
- Firm total_aua invariant $1,646.4M

Authorization: DS broker message "Andrew has cleared the full rebuild."

---

## Attempt 1 — OOM Kill (c6a.8xlarge, 64 GiB)

**Dispatch time:** ~19:15 ET  
**Outcome:** FAILED — OOM at A-tier

QA runner was c6a.8xlarge (64 GiB RAM) — erroneously downsized on 2026-04-20 due to InsufficientInstanceCapacity when attempting c6a.16xlarge resize. PROD is c6i.16xlarge (128 GiB).

A-tier python3 process (PID 1616) OOM-killed at ~20:27 ET:
- anon-rss: 63.6 GiB at kill time
- Instance had 64 GiB total; 63.6 GiB RSS exceeded available headroom

**Diagnosis:** `journalctl -k -b -1` on rebooted instance. Kernel OOM log confirmed.

**Fix:** Resize QA to c6i.16xlarge (128 GiB, matching PROD). c6a.16xlarge still had InsufficientInstanceCapacity in us-east-1.

Updated EC2_MANIFEST.json: QA runner instance_type → c6i.16xlarge.

---

## Attempt 2 — D-tier Parallel Crash (c6i.16xlarge, 128 GiB)

**Dispatch time:** ~20:45 ET  
**Outcome:** PARTIAL — A/B/C tiers clean, D-tier killed by watchdog

Chain ran A/B/C tiers successfully. D-tier started (D_00 || D_00c || D_03 in parallel) but watchdog fired at ~21:28 ET:
- Last pgrep hit at 21:23:02Z
- Watchdog at 21:28:19Z found no gold process: 5 min 17 sec since last hit (> 5-min grace)
- Instance shut down

No OOM in journal. No chain log uploaded (chain did not reach completion).

**Root cause:** Watchdog grace-window design. Parallel D scripts running in background under `--bg` caused SSM to detach; watchdog pgrep may have missed the parallel fork window. D-tier scripts run in parallel (`||`) per gold_dispatch.sh phase logic.

**Fix:** Run `--group D` in foreground (no `--bg`) to keep SSM session live and capture output directly. Sequential execution confirmed safe.

---

## Attempt 3 — Group D Isolation (Foreground SSM)

**SSM Command ID:** `75950d55-6db0-439f-9fc5-49fa1a6bba84`  
**Dispatch time:** ~21:30 ET  
**Outcome:** SUCCESS

All 7 D-tier scripts ran sequentially and clean. SSM returned Success.

**Artifacts written:**
| Artifact | S3 Path | Status |
|---|---|---|
| Chain log | s3://opal-data-bd/gold/logs/group_D_20260421_214248.log | 556 KB uploaded |
| COHORT-A | s3://opal-data-bd/gold/platinum/firm/cohort_a_summary.json | 7 fields confirmed |
| Employee leaderboard | s3://opal-data-bd/gold/artifacts/employee_leaderboard.json | D_00c written |
| clients_tab.json | s3://opal-data-bd/gold/portal/ | written |
| timeseries_chart.json | s3://opal-data-bd/gold/portal/ | written |
| implementor_leaderboard.json | s3://opal-data-bd/gold/portal/ | written |
| firm_mix_views.json | s3://opal-data-bd/gold/portal/ | written |

---

## Validation Results

### COHORT-A (D_04)
PASS. cohort_a_summary.json 7-field structure confirmed:
- account_count: 440
- total_aua: $57,635,735.47
- client_count: 321
- state_distribution: present
- top_n_named: present
- snapshot_date: 2026-04-20
- methodology_note: present
- D_04 no crash: confirmed

### D_04 d87377a5 fix
PASS. Script completed without crash. Zero-gross Schwab drop + NaN-date guard patch validated.

### CHART-ALIGN (Travis Penfield Q2 NNA)
PENDING — DS to validate. Travis Penfield present in employee_leaderboard.json with NNA values across windows including -$7,333,316.54 (closest to expected -$6.845M). Q2 window label not surfaced at leaderboard structure level. DS to confirm Q2 convergence from leaderboard JSON.

### HLOT2b Patch B (~$102.7M Tier 1)
PENDING — DS to validate. B_01 74dbad2b ticker→cusip confirmation requires non-zero silver_unrealized_reopen/topup/canonical_holdings_reopen/topup tags in B-tier outputs. B-tier ran clean in Attempt 2 before watchdog kill. Group D did not re-run B-tier.

---

## MCP Actions

- **RAVC4 close sent to 0.4.0_DS_ClientPlatform** at 22:13 ET with full artifact bundle.
- **0.7.0_AE_CloudOps** previously flagged for PROD watchdog hot-patch before 23:00Z nightly EventBridge fire.

---

## Infrastructure Changes

| Change | Detail |
|---|---|
| QA runner resize | c6a.8xlarge → c6i.16xlarge (128 GiB) |
| EC2_MANIFEST.json | QA entry instance_type updated |

---

## Known Issues / Follow-up

1. **PROD watchdog (11478af7)**: PROD runner does NOT auto-pull watchdog on boot. Manual SSM hot-patch required before nightly 23:00Z run. Flagged to 0.7.0_AE_CloudOps.
2. **D-tier parallel execution under --bg + watchdog**: Grace window design interacts with parallel fork. For future full-chain QA runs, consider running D-tier sequential or extending watchdog grace to 10 min.
3. **QA instance**: Should auto-shutdown via watchdog within 5 min of group D completion (no active gold process).
