# MDPF 49F non_model −$172M re-level seam (5/18) — characterization + recommendation
DS 0.4.0_DS_ClientPlatform (base), 2026-06-02. COO-requested next-work (seam a). Read-only investigation; methodology finding for CTO ruling. CC RD~B (1c break-out interacts).

## TL;DR
**The −$172M seam is ALREADY RESOLVED in the served layer.** The DE finding (2026-06-01 ~16:10Z, `bcb465a96`) caught a transient **partition→rollup propagation lag**, not a standing defect. The current served 49F timeseries (regenerated 2026-06-01 18:34:10Z, commit `120652cb6`) is continuous and internally consistent. **No re-level/backfill action needed.** Two doc-hygiene residuals surfaced (one of them = COO item b).

## Evidence (read-only, served artifact = the FE-consumed rollup)
Source: `s3://opal-data-portal-v2/json/mdpf/49financial/aggregate-aua-timeseries.json` (LastModified 2026-06-01 18:34:12Z; generated_at 18:34:10Z; 401 dates 2024-11-01..2026-05-29). Audit scripts `.runtmp/mdpf_ts_seam_audit.py` + `.runtmp/mdpf_172m_seam_audit.py`.

- **No −$172M step anywhere.** Largest non_model_aua step in the full 401-date series = **+$44.4M** (2025-04-08→09, normal rebalance). The 5/15→5/18 step is **+$8.7M** (continuous: $274.8M → $283.5M). Top-8 steps all $31–44M (ordinary).
- **v0.9 3-way identity holds 400/401**: custody_total == model(1a) + sma(1c) + non_model(1b) to <$1 on every date back to 2024-11-01, except one (see residual ii). The entire history is on the consistent SMA-exclusive v0.9 basis.
- **Per-date partitions agree** (`platinum/mdpf/aggregate_aua/{date}.json`): 5/15 non_model $274.8M (cust $1,648.85M) → 5/18 $283.5M (cust $1,648.85M, identical) — continuous in the producer layer too.

## Mechanism — how the seam was closed (and what the −$172M originally was)
The −$172M was a **basis discontinuity** at the 5/18 cutover:
- v0.8 (pre-5/18, MDPF_ASSETS.016 `build_mdpf_process_backfill.py`): 1b = `certified_aua − 1a` on the **full Black Diamond book (4 custodians, ~$469M 1b)**, SMA **inside** 1b.
- v0.9 (live from 5/18): 1b = `Schwab_49F_custody − 1a − 1c` (**Schwab-49F custody subset, ~$280M 1b**), SMA **broken out** as cohort_class='sma'.
- So −$172M ≈ (Schwab-49F-custody − full-BD-book) basis narrowing + the −$25M SMA break-out. A deliberate methodology change (Andrew Mandate Change 3, 2026-05-20), NOT a data error.

**Resolution:** MDPF_ASSETS.029 (`v0_9_rps_calibrated`) + .031 (`v0_9_2024depth`) rederives put the ENTIRE pre-5/18 history onto the v0.9 `schwab_canonical_rederived` basis, superseding the v0.8 full-BD region → series continuous. `cohort_provenance[]` now labels each date: `custody`=measured/rollforward (real, 2026-01-16+), `model_1a`=measured, `sma_1c`=interpolated_estimate (bandaid_interp). Estimate components are disclosed per-date (TO-1a AC3, commit `120652cb6`), not hidden.

## Residual items surfaced during characterization (NOT the seam)
**(i) Narrative drift — this is COO item (b), now surfaced by (a). [doc-only, DS-lane]**
`meta.cohort0_historical_backfill` prose still states the 2026-01-17..05-17 region is on the *superseded* v0.8/Ruling-2 basis ("1b = certified_aua − 1a on the full BD book with SMA inside 1b"). But the served values + `cohort_provenance[]` for that region are `schwab_canonical_rederived` (v0.9, SMA-exclusive, custody measured). `meta.backfill_methods` still lists the stale `process_derived_v0_8_rulingII_..._016` alongside `.029`/`.031`. Prose contradicts the data + the per-date provenance — classic serving-narrative-drift. Reconcile the prose + backfill_methods to the actual schwab_canonical serve.

**(ii) One identity violation [PROBED — isolated holiday-boundary artifact]**
2025-12-26 (per-date partition, mv=v0_9): 1a $1,064.01M + 1c $20.46M + 1b $207.93M = $1,292.40M vs custody $1,335.55M (−$43.16M). Root cause: 1b is NOT the plug-consistent value on this one date — the plug should be custody − 1a − 1c = $251.09M, but 1b is recorded $207.93M (the ~$208M level that 12/29 also carries). Custody rose (+$7.3M from 12/23) while 1b was carried from a different as-of. Neighbors clean (12/23 delta=$0, 12/29 delta=$0). 12/24 has no partition + 12/25 Christmas → 12/26 is a post-holiday rollforward boundary with sparse inputs → custody and 1b landed on different as-of points. Isolated (1/401, ~3% of the $1.34B total), in the deep-history null-provenance .031 rederive. Fix: re-derive 1b as the plug on 12/26 (one-partition re-emit) OR accept as a known holiday-boundary estimate artifact. Not systemic; does not affect the 5/18 seam or the live region.

**(iii) Provenance-labeling completeness [minor]**
Deep history (2024-11-01..~2026-01-15) carries `null` cohort_provenance yet is the MOST estimated region (flat $19.67M SMA seed + derived custody). Live (5/18+) is ALSO `null`. So "null" conflates most-estimated and fully-real. Consider an explicit estimate label on the deep-history region so null reads unambiguously.

**(iv) Stale partition methodology_version tags [minor]**
Per-date partitions 5/13–5/15 still stamp `v0_8_ruling2` while carrying v0.9-consistent values (custody $1.65B, SMA-exclusive). Tag drift vs the rollup; cosmetic.

## Recommendation
1. **No re-level / backfill** — the seam is closed; series is continuous + internally consistent + estimate-labeled. Real pre-RPS (pre-2026-01-16) Schwab-49F custody and real historical SMA do not exist, so the interpolated-estimate basis is the best achievable and is transparently disclosed.
2. **CTO ruling sought:** formally ACCEPT the `schwab_canonical_rederived` history (.029/.031) as canonical, superseding the v0.8/.016 full-BD region. (RECOMMENDED.)
3. On that GO, DS-lane doc-only fixes: reconcile `meta.cohort0_historical_backfill` prose + `backfill_methods` to the actual serve (closes COO item b) + a targeted probe of the 2025-12-26 identity blip. Optional: deep-history provenance label + partition methodology_version tag refresh.

Routed to COO → CTO; CC RD~B.
