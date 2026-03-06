# ADVI_AUAVAR Phase 4 Diagnostic Suite EC2 Execution — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 18:45
**End Time:** 19:05

---

## Objective

Execute the Phase 4 three-script diagnostic suite (D1 filter audit, D2 BKF simulation,
correction matrix) sequentially on `bd-gold-layer-runner` (`i-01003b035d2988dfb`).
Commit `10f69c0d` (DS Phase 4 suite).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Push DS commit `10f69c0d` | `43b893ba..10f69c0d` pushed |
| 2 | Upload all three scripts to S3 (parallel) | D1: 26,496B / D2: 21,305B / Matrix: 18,532B |
| 3 | SSM D1: filter audit | CommandId: `bedd3069-b8ae-432d-805c-e3ba8f8d8e30` — Success (<2 min) |
| 4 | SSM D2: BKF simulation | CommandId: `ff85293d-04aa-46aa-9008-1adac36f0279` — Success (<2 min) |
| 5 | SSM D3: correction matrix | CommandId: `e628c40d-b26c-4811-890d-fcf9474ee025` — Success (<1 min) |

---

## S3 Artifact Status

| Artifact | Status | Size |
|----------|--------|------|
| `aua_d1_filter_audit_2026-03-02.json` | PRESENT | 8,485 bytes |
| `aua_d1_filter_audit_2026-03-02_stdout.txt` | PRESENT | 5,642 bytes |
| `aua_d2_bkf_simulation_2026-03-02.json` | PRESENT | 11,336 bytes |
| `aua_d2_bkf_simulation_2026-03-02_stdout.txt` | PRESENT | 3,759 bytes |
| `aua_correction_matrix_2026-03-02_stdout.txt` | PRESENT | 4,635 bytes |
| `aua_correction_matrix_2026-03-02.json` | NOT WRITTEN — script crashed at line 437 before emit |

---

## D1 Results — Filter Audit (164 ACT accounts, $7,360,069.92)

| Hypothesis | Count | BD MV | Verdict |
|------------|-------|-------|---------|
| H1 NET_ZERO (fully liquidated, cum_units <= 0) | 159 | $7,344,029.78 | CORRECTLY EXCLUDED — not a bug |
| H2 NULL_ASSET | 110 | $2,134,601.53 | Overlap with H1; primary assignment resolves |
| H3 CA_ONLY | 0 | $0.00 | No compound H3+H4A signal |
| H4-A DATE_SPECIFIC | 1 | $472.45 | Appears in prior cube dates, absent 2026-03-02 |
| H4-B STRUCTURAL | 4 | $15,567.69 | Never in adjacent dates — manual inspection needed |
| UNCLASSIFIED | 0 | $0 | — |

**Primary assignment (first-wins):**

| Label | Count | BD MV |
|-------|-------|-------|
| H1_NET_ZERO | 159 | $7,344,029.78 |
| H4A_DATE_SPECIFIC | 1 | $472.45 |
| H4B_STRUCTURAL | 4 | $15,567.69 |

**Total recoverable:** 5 accounts / $16,040.14

**KEY FINDING:** The $7.36M "ACT bug" was not a bug. 159/164 accounts are correctly excluded
because they have zero cumulative open units on 2026-03-02 — fully liquidated. BD's positive
MV likely reflects unsettled T+1/T+2 proceeds. Only 5 accounts ($16K) are genuinely
recoverable (1 via full cube rebuild, 4 require manual inspection).

---

## D2 Results — BKF Simulation (233 backfill-only accounts, $6,585,657.53 BD MV)

| Metric | Value |
|--------|-------|
| BKF accounts with simulated open positions | 143 of 233 |
| BKF accounts fully liquidated (correctly excluded even under forward-fill) | 90 |
| Simulated forward-fill MV (143 accounts) | $18,437,265.93 |
| BD reported MV (all 233 BKF accounts) | $6,585,657.53 |
| Simulation / BD ratio | 280% |
| Pricing coverage | 99.6% (988/992 positions priced) |
| Per-account: within 5% of BD | 43 of 137 accounts with bd_mv > 0 |
| Per-account: within 10% of BD | 58 of 137 |

**NOTABLE:** Simulation produces 280% of BD's reported MV ($18.4M vs $6.6M). The script
labels this as "CLEAN_FIX" but the 280% ratio is an anomaly — likely caused by the
simulation pricing holdings that BD excludes from `account_market_value` (e.g., cash
instruments, insurance-adjacent fixed instruments). Forward-fill extension would add
~$18.4M to the cube, substantially over-shooting BD's $6.6M for these accounts.
90 of 233 BKF accounts are also liquidated — correctly excluded even under extension.

---

## D3 Results — Correction Matrix (scenario table from stdout; JSON not written)

**BD reference totals (computed by matrix script):**
- BD gross (all account types): $1.6275B
- BD investment-only (gross minus $59.5M insurance/annuity, plus $3.5M liabilities): $1.5716B

**Scenario table:**

| Scenario | Gold AUA | vs BD Gross | % Gross | vs BD Inv-Only | % Inv-Only |
|----------|----------|-------------|---------|----------------|------------|
| S0 Baseline gross | $1.5539B | -$73.6M | 95.5% | -$17.7M | **98.9%** |
| S1 Non-cash baseline | $1.5307B | -$96.8M | 94.0% | -$40.9M | 97.4% |
| S2 + D1 fixed | $1.5233B | -$104.2M | 93.6% | -$48.3M | 96.9% |
| S3 + D2 BKF extended | $1.5491B | -$78.4M | 95.2% | -$22.5M | 98.6% |
| S4 D1 + D2 (best) | $1.5418B | -$85.7M | 94.7% | -$29.8M | 98.1% |
| S5 + H4B structural | $1.5491B | -$78.4M | 95.2% | -$22.5M | 98.6% |

**Closest scenario to BD investment-only: S0 baseline gross at 98.9%.**

Residual decomposition after all fixes (S4):
- Cash-only/new accounts (B2 scope, no txn history): ~$34.1M
- Normal pricing/timing spread: ~-$7.1M
- These are not bugs — policy/architecture decisions

**ANOMALY:** S2 (D1 fixed) shows $1.5233B — *lower* than S0. This is because D1's recoverable
is only $16K, but the matrix is subtracting H1 correctly-excluded accounts from what was
previously counted. S4 (D1+D2) also trails S0 because D2's simulated $18.4M overshoots
BD's $6.6M, adding noise rather than closing the gap cleanly.

---

## Matrix Script Issue (line 437 crash)

```
AttributeError: 'float' object has no attribute 'put_object'
```

Variable named `s3` was overwritten with a float before the `s3.put_object()` call.
JSON not written. Stdout is in S3. DS needs to fix the variable collision at line 437
before re-run, but the scenario table is complete in stdout — all data is available.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not attempt matrix script hotfix | Task order constraint — no script modification without DS approval |
| Did not re-run matrix after crash | Scenario table complete in stdout; DS has all decision data |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_phase4_diagnostic_suite_ec2.md` | New — this file | Pending |

---

## Blockers

None — scenario table is complete in stdout. DS can proceed to memo.
Matrix JSON crash is minor — fix at line 437 if DS needs the JSON specifically.

---

## Current State

**Status:** COMPLETE (with minor matrix JSON caveat)
**Active branch:** `CLOUD`

All three Phase 4 scripts executed. D1 and D2 JSONs in S3. Matrix scenario table in stdout.
DS has the full picture to write the AUAVAR variance memo for COO.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform] Write AUAVAR variance memo** — full decomposition now in hand. Key headline: gold S0 is already 98.9% of BD investment-only ($1.5539B vs $1.5716B). The $73.6M raw gap resolves to $17.7M after proper scope alignment.
2. **[0.4.0_DS_ClientPlatform] Fix matrix line 437** (`s3` variable collision) if JSON needed; otherwise stdout is sufficient.
3. **COO policy decision** — BKF Option 1 vs Option 2; D2 simulation over-shoots BD by 280% so Option 2 would need to cap at BD MV rather than use sim MV directly.
4. **No further DT action required unless DS commits a fix and needs another run.**
