# NNAVAR Cap Tuning EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 18:39
**End Time:** 18:59

---

## Objective

Execute all 3 suites of `diag_nnavar_cap_tuning.py` (Phase 2) on EC2
`i-01003b035d2988dfb` per `docs/briefs/devops-brief-nnavar-cap-tuning-ec2-run.md`.
Isolate AUA and velocity cap thresholds independently, then run a cross-product combo
grid to find the best combined configuration.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | git pull CLOUD | Already up-to-date at `e6e6cdd1` |
| 2 | Upload script to S3 | `s3://opal-data-bd/scripts/diagnostics/diag_nnavar_cap_tuning.py` (26.5 KB) |
| 3 | Suite: aua | CMD `9f5b6e30` — SUCCESS, 10s |
| 4 | DS/COO review aua + vel summaries | Presented — go-ahead received |
| 5 | Suite: vel | CMD `0f33e903` — SUCCESS, 40s |
| 6 | Suite: combo | CMD `0632041f` — SUCCESS, 58s |

All runtimes far faster than estimated (shared spine built once, amortized across variants).

---

## Suite Results (run_date: 20260306)

### Suite: aua (velocity OFF)

| Variant | aua_thresh | pearson_r | sign_agr | total_gap | MAE |
|---------|-----------|-----------|----------|-----------|-----|
| `aua_t1p50` | 1.5x | 0.263 | 9/13 | -$184.1M | $23.0M |
| `aua_t2p00` | 2.0x | 0.261 | 9/13 | -$189.2M | $23.2M |
| `aua_t3p00` | 3.0x | 0.261 | 9/13 | -$196.2M | $23.6M |
| `aua_t1p00` *(prod)* | 1.0x | 0.253 | 10/13 | -$168.6M | $22.3M |
| `aua_none` | off | 0.134 | 9/13 | -$540.4M | $49.9M |
| `aua_t0p50` | 0.5x | 0.109 | 13/13 | -$82.3M | $18.3M |

S3: `s3://opal-data-bd/diagnostics/nnavar_captune/20260306/aua/`

### Suite: vel (AUA fixed at 1.0x)

| Variant | vel_window | vel_thresh | pearson_r | sign_agr | total_gap | MAE |
|---------|-----------|-----------|-----------|----------|-----------|-----|
| `vel_w120_t2p00` | 120d | 2.0x | 0.260 | 10/13 | -$163.0M | $21.9M |
| `vel_w60_t1p50` | 60d | 1.5x | 0.254 | 10/13 | -$163.0M | $21.9M |
| `vel_w90_t2p00` | 90d | 2.0x | 0.254 | 10/13 | -$164.7M | $22.1M |
| `vel_w60_t2p00` | 60d | 2.0x | 0.254 | 10/13 | -$165.2M | $22.1M |
| `vel_none` | off | — | 0.253 | 10/13 | -$168.6M | $22.3M |
| `vel_w90_t1p50` | 90d | 1.5x | 0.251 | 10/13 | -$160.6M | $21.8M |
| `vel_w60_t1p00` | 60d | 1.0x | 0.162 | 10/13 | -$126.6M | $19.8M |
| `vel_w90_t1p00` | 90d | 1.0x | 0.157 | 11/13 | -$124.7M | $19.6M |
| `vel_w120_t1p50` | 120d | 1.5x | 0.239 | 10/13 | -$148.9M | $20.9M |
| `vel_w120_t1p00` | 120d | 1.0x | 0.111 | 13/13 | -$107.1M | $18.4M |

S3: `s3://opal-data-bd/diagnostics/nnavar_captune/20260306/vel/`

### Suite: combo (3 AUA x 5 velocity = 15 variants)

| Variant | AUA | Vel window | Vel thresh | pearson_r | sign_agr | total_gap | MAE |
|---------|-----|-----------|-----------|-----------|----------|-----------|-----|
| `comb_aua1p5_w120t2p00` | 1.5x | 120d | 2.0x | **0.271** | 10/13 | -$174.9M | $22.3M |
| `comb_aua2p0_w120t2p00` | 2.0x | 120d | 2.0x | 0.269 | 9/13 | -$177.4M | $22.4M |
| `comb_aua1p5_w90t2p00` | 1.5x | 90d | 2.0x | 0.264 | 10/13 | -$176.8M | $22.5M |
| `comb_aua1p5_velnone` | 1.5x | off | — | 0.263 | 9/13 | -$184.1M | $23.0M |
| `comb_aua2p0_w90t2p00` | 2.0x | 90d | 2.0x | 0.263 | 9/13 | -$179.2M | $22.6M |
| `comb_aua2p0_velnone` | 2.0x | off | — | 0.261 | 9/13 | -$189.2M | $23.2M |
| `comb_aua1p0_w120t2p00` | 1.0x | 120d | 2.0x | 0.260 | 10/13 | -$163.0M | $21.9M |
| `comb_aua1p5_w90t1p50` | 1.5x | 90d | 1.5x | 0.255 | 10/13 | -$167.8M | $21.8M |
| ... | | | | | | | |

S3: `s3://opal-data-bd/diagnostics/nnavar_captune/20260306/combo/`

---

## Key Findings (DT observations)

1. **Best overall: `comb_aua1p5_w120t2p00`** — pearson=0.271, sign_agr=10/13, gap=-$174.9M.
   AUA 1.5x + velocity 120d/2.0x is the highest-pearson config across all 31 variants tested.

2. **Velocity cap at loose threshold (1.5x-2.0x) adds ~0.008-0.018 pearson over AUA-only.**
   The velocity cap at these settings is modestly beneficial but not transformative.

3. **Tight velocity cap (1.0x) trades pearson for gap closure and sign agreement.**
   `vel_w120_t1p00` achieves 13/13 sign agreement and -$107M gap but pearson drops to 0.111.

4. **PRD target (pearson >= 0.50) is not reachable by cap tuning alone.**
   Ceiling across all 31 variants: pearson=0.271. The structural gap (-$107M to -$196M
   across all configurations) and correlation ceiling indicate the gap is not a cap
   threshold problem. Likely requires architectural investigation (relationship mapping,
   transaction classification, or Schwab comparison methodology).

5. **AUA 1.0x (production) is already near-optimal for pearson/sign balance.**
   `comb_aua1p0_*` variants cluster at pearson ~0.239-0.260, sign 10/13.
   AUA 1.5x gives +0.01-0.02 pearson but drops sign agreement to 9/13 in most configs.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Proceed to combo without MSYS_NO_PATHCONV | Same working pattern confirmed in Phase 1 |
| Report all 3 summaries together | aua+vel completed fast enough to present together before combo |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| None — script already committed by DS | Upload to S3 only | N/A |

---

## Verification

All 31 variant S3 artifacts confirmed written:
- `summary.csv` per suite (sorted by pearson_r desc)
- `stdout.txt` per suite
- `run_manifest.json` per suite
- Per-variant `monthly_nna.csv` + `metrics.json`

No `gold/` or `silver/` paths written. Safety assertions passed on every run.

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

All 3 cap tuning suites complete. 31 total variants evaluated across aua isolation,
velocity isolation, and combo grid. Best config: `comb_aua1p5_w120t2p00` at
pearson=0.271. PRD target (0.50) not reachable by threshold tuning. DS needs to
determine Phase 3 scope.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Analyze combo results + determine Phase 3 scope** —
   Key question: is pearson ~0.27 the ceiling for transaction-based NNA, or is
   there a structural fix (relationship mapping, transaction classification) that
   could push toward 0.50?

2. **[COO] Go/no-go on production parameter change** — If AUA 1.5x + vel 120d/2.0x
   is selected, DT needs a task order for the production Lambda deploy.

**Do NOT:**
- Deploy any parameter changes to production without explicit DS/COO task order
- Re-run any suite without DS instruction
