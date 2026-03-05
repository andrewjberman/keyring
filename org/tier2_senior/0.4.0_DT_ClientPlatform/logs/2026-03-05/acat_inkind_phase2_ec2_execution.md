# ACAT In-Kind Diagnostic Phase 2: EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-05
**Execution Time:** ~10 minutes (including EC2 start, SSM command, monitoring)
**Status:** ✅ COMPLETE — Diagnostic output successfully captured to S3

---

## Objective

Execute the ACAT in-kind diagnostic v3 script on BD gold-layer-runner EC2 instance via S3 artifact model per `docs/briefs/devops-brief-acat-inkind-diagnostic-v3.md`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Push CLOUD to remote | ✅ `c1c50e3a` pushed (18 commits including Phase 1) |
| 2 | Upload v3 script to S3 | ✅ `s3://opal-data-bd/diagnostics/diag_acat_inkind_scan_v3.py` (17.2 KB) |
| 3 | Start EC2 instance | ✅ `i-01003b035d2988dfb` transitioned from stopped to running |
| 4 | Run diagnostic via SSM | ✅ Command ID: `2333de55-5439-4bf9-a866-9a05679a4fb1` (Success) |
| 5 | Capture output to S3 | ✅ `s3://opal-data-bd/diagnostics/acat_scan_v3_output.txt` (12.9 KB) |

---

## Verification

**S3 Artifact Status:**
```
s3://opal-data-bd/diagnostics/diag_acat_inkind_scan_v3.py        17,189 bytes
s3://opal-data-bd/diagnostics/acat_scan_v3_output.txt            13,235 bytes
```

**EC2 Execution Summary:**
- Instance: `i-01003b035d2988dfb` (bd-gold-layer-runner)
- Transaction partitions loaded: 1,742 partitions
- Total transaction rows processed: 3,419,039
- Load time: 39.4 seconds
- Memory usage: Well within instance capacity

**Diagnostic Results Captured:**

- **Total accounts flagged:** 867 (with ≥3 buys in 30-day window, positive ACAT estimate)
- **Total ACAT estimate:** $97,961,152
- **Monthly breakdown:** 60+ months (Jul 2020 – Mar 2026)
- **Schwab gap closure:** Original gap -$32.7M → Adjusted gap +$13.2M (sign flip)
- **Top 25 accounts audit:** Included with account IDs, first dates, transaction details
- **Relationship rollup:** Top 15 households and 10 architects by ACAT volume

---

## Current State

**Status:** COMPLETE

**Active Branch:** CLOUD

**What's done:**
- Phase 1: DS committed diagnostic scripts and DT brief (commits 90424dba, d3c28755)
- Phase 1: DT pushed CLOUD to remote
- Phase 2: DT uploaded script, ran on EC2, captured output

**What's ready for Phase 3:**
- S3 output available at `s3://opal-data-bd/diagnostics/acat_scan_v3_output.txt`
- DS ready to read and analyze: gap closure %, volume sanity checks, top-25 audit, sensitivity tests (threshold + window)

---

## Next Steps

> **Immediate handoff to 0.4.0_DS_ClientPlatform for Phase 3**

1. **[Data Scientist] Read S3 output** — `s3://opal-data-bd/diagnostics/acat_scan_v3_output.txt`
2. **[Data Scientist] Perform gap closure analysis** — month-by-month improvement, sign flips, overshoot risk
3. **[Data Scientist] Volume sanity checks** — account distribution, ACAT estimate outliers, cross-check vs known zero-inflow relationships
4. **[Data Scientist] Top-25 account edge case audit** — verify genuine ACAT transfers vs false positives
5. **[Data Scientist] Sensitivity testing** — BURST_THRESHOLD (2/3/5) and onboarding window (14/30/45 days)
6. **[Data Scientist] Production design brief** — recommended approach, parameters, false positive assessment, rebuild sequence
7. **[COO/CEO review]** — review design brief before Phase 4 implementation task order issued

**Do NOT:**
- Modify or re-run the diagnostic script locally
- Make any changes to production gold layer scripts (05, 09, 10)
- Deploy anything to production before design brief review

---

## No Issues

- EC2 instance transitioned smoothly (was in stopped state, started without error)
- SSM command executed successfully on first attempt
- Output captured with complete formatting (60+ months, top-25 accounts, rollups)
- No memory errors, Python warnings only (pandas FutureWarning, expected)

---

## Session Log Reference

- DS Phase 1 log: `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-03-05/acat_inkind_phase1_diagnostics_committed.md`
- Task order: `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/acat-inkind-nna-testing.md`
- DT brief: `docs/briefs/devops-brief-acat-inkind-diagnostic-v3.md`
