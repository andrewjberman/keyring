# Build Log — ADVI_FEREFI.W2 #6 fee-substreams (INF code done; deploy routed AE)

**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-03T1425Z
**TO:** ADVI_FEREFI.W2 (GO: Andrew "ok sick lets do it" + COO 141036Z) · **Commit:** c42c5e6ed (CLOUD)

## Trace findings (corrected the build plan)
- Advisor Lifetime-Activity `timeseries.json` (FE reads `platinum/advisors/{id}/timeseries.json`) is built by a **Lambda** for BOTH firms (`inf-`/`bd-portal-advisor-publisher`) — NOT the gold-runner cycle. INF deploy = **Terraform/Lambda apply (Rule 1, AE-owned)**.
- INF flow-split (`*_canonical_fee_paying`, "F11-B") committed **2026-05-28 by my lane** (`982394f01`) but **never deployed** → served artifact (6/2) has zero fee fields → that's WHY Inflection still shows "approx". Committed-not-deployed (banked lesson).
- `total_aua_fee_paying` (AUM-mode split the FE `pickAua` needs) was **absent on BOTH firms'** served artifacts.

## INF — code DONE (`c42c5e6ed`, pushed)
- `_build_timeseries`: added **F11-C** `total_aua_fee_paying`/`_no_fee` per-period. Back-attribution = current per-account `is_fee_earning` (fee_map, already loaded for F11-B) × AUA-timeseries periods (AUA point-in-time → per-date groupby, no cumsum). `fee_paying+no_fee==total_aua` per date by construction.
- Gates: `ds-commit-gate` PASS, `py_compile` OK. Pure-additive (new keys + a groupby); no new deps/IAM/memory.
- **Deploy ships F11-B + F11-C together** → `hasFeeSplitSeries` fires on nna/inflows/total_aua → FE synthetic approx dies for Inflection.
- **Routed to AE** (142537Z) for the Terraform apply; post-deploy I served-verify + RAVC2.

## 49F — TO bar MET; one finding routed to CTO
- TO's 49F bar ("served timeseries surfaces a fee-split so `hasFeeSplitSeries` fires"): **already met** — `nna_canonical_fee_paying` + per-role `aua_fee_paying` present. NNA-mode toggle works today; no TO-required change.
- FINDING: `total_aua_fee_paying` absent on 49F too → AUM-mode toggle falls back to unsplit `total_aua` (inert). Routed CTO: is AUM-mode split in #6 scope? If yes → 49F `D_02` deduped total_aua split (careful edit into the melt/dedup agg + its gold-cycle+publisher deploy). Did NOT unilaterally expand into 49F's working pipeline.

## Honesty flags (in INF code comment; for FE label)
1. INF pre-Q3-2025 fee-paying INFERRED (back-attributed), not measured. 2. Can't detect pre-floor fee-status changes. 3. 49F equal-split backfill pre-data.

## Open (blocking RAVC2)
- AE Terraform apply of inf-portal-advisor-publisher (+ confirm publisher re-trigger regenerates artifacts).
- CTO ruling on 49F AUM-mode scope.
- Then: served-verify (pull timeseries.json?firm=inflection, confirm fields + reconciliation) → RAVC2 COO+CTO.
