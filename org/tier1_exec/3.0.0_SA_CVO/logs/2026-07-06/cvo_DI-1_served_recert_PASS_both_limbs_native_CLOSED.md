# CVO served re-cert: DI-1 (INF client-tax) -- PASS, both limbs Orion-native, DI-1 C-stage CLOSED

**archetype:** VALIDATE
**serial:** 3.0.0_SA_CVO | **date:** 2026-07-06 ~2340Z | **trigger:** Andrew-direct this-session drive (fix + CVO-verify the INF client-tax 13.6x re-point) | **owner-impl:** DS~B (re-point), 0.6.1 (chain-run)
**method:** exercise-on-SERVED artifact (independent diff vs a source-computed baseline), NOT self-report. Reserved word "re-certified" earned on the corrected served numbers.

## VERDICT: PASS -- DI-1 client-facing tax RE-CERTIFIED. Both C-stage limbs Orion-native. DI-1 C-stage CLOSED.

The fix: retire the derived INF_B_03 unrealized_gain (positions_cube-vs-canonical unit-mismatch + fillna(0) phantom, served ~$180.5M = 13.6x overstated) -> source INF_C_05 + INF_C_03 from Orion-native tax_unrealized (Andrew's raws-over-derived steer). Served this session (gold-c chain-run 23:26Z), NOT a plan.

### Independent served-cert (vs my locked baseline from silver tax_unrealized 07-06)
LIMB 1 -- C_05 client_tax_liability.json (gen 23:26:00.940Z, source=orion_tax_unrealized):
- firm_summary.total_unrealized_gain = $13,285,579 == baseline EXACT (was $180,511,835 -> 13.6x phantom GONE; $180.5M signature ABSENT).
- SUM(by_household) total/ST/LT = $13,285,579 / $460,465 / $12,825,108 == baseline EXACT (firm ST/LT lives per-household; aggregated to verify. ST+LT=$13,285,573, $6 amortization/rounding, immaterial).
- top-5 households ALL EXACT: 463=$3,133,581 / 449=$1,270,268 / 338=$982,963 / 407=$662,116 / 201=$485,873.
- 890 accts / 290 canonical hh; unmapped 53/$0 surfaced explicitly (honest-missing).
LIMB 2 -- C_03 account_performance.parquet (LastModified 23:25:59Z UTC, CONTENT check):
- latest-date 07-06, 790 accts, SUM unrealized_gain = $13,285,579 = NATIVE, EXACT (not the derived phantom).

Both limbs source=orion_tax_unrealized, derivation retired, phantom gone. 4-way cross-verified (DS~B + COO + CVO x2 independent reads).

### Two first-pass false-alarms I self-caught (grounding-before-verdict working; hygiene noted)
1. Fragile field-extraction: a recursive [0] grabbed household[0]'s ST/LT and I momentarily read it as a firm-ST/LT mismatch. firm_summary carries NO ST/LT (it's per-household). Re-grounded -> clean aggregate PASS. FIX: exact field-paths, not recursive-[0].
2. TIMEZONE misread: read `aws s3 ls` LOCAL (EDT) time (19:25) on account_performance as stale-vs-UTC-23:26 and wrongly flagged C_03 as pending. head-object UTC = 23:25:59Z = this run. RETRACTED. (Same mtime-timezone class I caught CTO on with the tax-pull -- easy to hit; banked.) FIX: head-object-UTC, not s3-ls-local.
Both caught + corrected BEFORE any verdict issued -> the discipline is what kept the verdict right.

### Belts (non-blocking, noted-not-gating; on my queue)
1. D-stage platinum/book D_02.capital_gains_ttm consumes C_03 but did NOT re-run in the C-only dispatch -> self-heals next FULL nightly (expected propagation, NOT regression). Verify old-derived->corrected delta on the nightly.
2. Redundant 23:38Z gold-c write (AE-owned, deterministic-identical) -> re-confirm value holds post-settle (verify, not trust).
3. DI-7 (tax bucket 100%-taxable, SEPARATE bug) -- STILL 100/0/0 this run; DS~B a1 fix GO'd; verify on its re-run.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| aws s3/s3api + pandas | served client_tax + account_performance content diff vs baseline | PASS | both limbs native $13,285,579 exact; head-object-UTC resolves the s3-ls-EDT trap |
| (pre-stage) tax_unrealized rollup | firm + canonical-hh baseline ($13.285M, top-5) | PASS | source-computed independent baseline; canonical-key + 53-unmapped($0) grain resolved pre-deploy |

## Disposition
DI-1 C-stage CLOSED (both limbs Orion-native, certified). Andrew-direct this-session met. D-stage book + redundant-write + DI-7 = belts. RAVC closed with COO. Systemic silent-default-class (DI-1/2/4/7) routed to CTO for an "honest-missing never silent-default" invariant.

-- 3.0.0_SA_CVO
