# Session Log — 0.4.0_DS_ClientPlatform~B

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, DEPLOY, VALIDATE
**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-29
**Session span:** ~18:19Z (MSTR spawn) → ~21:15Z
**Projects:** MDPF_SCOPED (primary), ADVI_INFMVP (secondary), ADVI bell-curve (Andrew-direct)

---

## Session purpose

MSTR-provisioned per Andrew sovereign 3-project directive. Mandate: MDPF_SCOPED maturation — close the three open CVO findings (F1/F4/F5). Session evolved to include ADVI_INFMVP F4b (cohort-dim) and an Andrew-direct per-firm account-distribution bell-curve build.

---

## Deliverables — completed this session

### MDPF_SCOPED maturation — ALL 5 FINDINGS CLOSED

#### F4 — 49F 12/26 LTC period-end-roll tagging bug (CLOSED)

**Diagnosis (CONCLUSIVE):** The 49F 12/26/2025 "$42M model/non-model reclass" was a period-end-roll snapshot-selection artifact, not a real reclass. `load_1a_daily` kept newest-LastModified CSV per (date, asset-class) ignoring PeriodEnd. On 12/26 the LTC December period-end re-export (uploaded 12/29) won, putting LTC alone on a Dec roster (2368 allocs, $508.27M) while the other 4 models stayed on November (2242 allocs, $464.94M). Non-model is a residual → drops in lockstep. Net custody smooth. Proved with raw SmartX export CSV open-allocation sums.

**Systemic:** 52 single-model >4% month-boundary jumps across the series + a 12/27 partial-coverage day (1 of 5 CSVs published entire $1.107B book into Ultra-Short-Term).

**Fixes landed:**
- `a27c02971` — `load_1a_daily` period-end-coherent selection (modal PeriodEnd suffix across 5 ACs per date); partial-coverage SUPPRESS (<5 of 5 models → 1a null, not carried); F4 regression sentinel (ERROR-class: >6% DoD single-model + equal-opposite non_model residual + <3 correlated models = period-end-roll class blocked at re-emit)
- `f44ab785d` — targeted patch script: `patch_mdpf_per_date_partitions.py` (COO+CTO authorized); PATCH-1 corrected 12/26 LTC from $512.4M → $469.3M (12/23 stored value, calibration-space consistent per COO precision gate); PATCH-2 added Inflection partner blocks to 391 pre-5/18 per-date partitions

**Verification:** 12/23↔12/26 LTC delta = $0.00 (exact match). F4 regression sentinel fired correctly on the empirical test date; refined to 6%+isolation threshold after a real-market-move false-positive (04/07 UST −4.8%, all 5 models on 202604 = correlated, not period-end-roll).

#### F1 — Inflection AUA spine-reuse (CLOSED)

**CHANGE-1 (ACCEPTED `30c19b26c`):** Repointed `build_mdpf_wsc_inflection_feeder.py` `partner_custody_total` to `client_performance.parquet` (opal-data-inf `gold/timeseries/`, the INF_D_00b / Assets Overview lineage) instead of Eclipse `portfolios_full.total_value`. Latest spine value @ 2026-05-28 = **$205,530,479.45** — ties to canonical $205.53M to the dollar (was $203.98M, ~$1.5M gap resolved). Eclipse-book sum retained as diagnostic-only (`eclipse_vs_spine_gap` field).

**CHANGE-2 (`a1a344e6d`):** New `build_mdpf_inflection_history_from_spine.py` — reads `client_performance` per-date total_aua → emits `non_model_aua/inflection/{date}.parquet` feeders. Replaces the retired S2 Orion assets_v2 per-household API backfill (COO+CTO concurred; client_performance spans 2020-05-26→2026-05-29, 2195 dates, no gaps — fully covers the trend window).

**Pre-5/18 history (PATCH-2):** 391 per-date platinum JSONs got Inflection partner block added (model=0/sma=0/non_model=custody=spine_total for pre-funding dates). Result: 393 non-null Inflection custody dates in the final consolidated artifact (was 9 of 401).

#### F5 — S4 canonical model display names (CLOSED, `e88c54e23`)

Registry v4 renamed the 5 core models to S4 canonical: Ultra-Short Term / Short Term / Intermediate Term / Long Term / Ultra-Long Term. Consolidation script re-resolves `by_model.display_name` from the registry by model_key at consolidation time — overrides stale baked names in historical partitions without re-emitting every JSON. Drops portal dependence on the `modelPortfolioColors.ts` legacy alias map.

#### F3 (S2) — Retired

S2 Orion assets_v2 API backfill retired; client_performance spine supersedes.

#### F2 — Already closed (`aa8c9de4`) prior session.

### 4-gate final verification (all PASS)

| Gate | Result |
|------|--------|
| G1: 12/26 LTC step gone + 12/26==12/23 | PASS (delta $0.00) |
| G2: Inflection 393/402 non-null + model-split at 5/18 | PASS |
| G3: S4 canonical display names | PASS |
| G4: sentinel 0 fires on re-emit-eligible dates | PASS |

Per-firm Non-Model band confirmed subsumed by F1 (COO+CTO accepted). MDPF_SCOPED fully closed.

---

### ADVI_INFMVP F4b — nmnc/nmec cohort-dim (CLOSED, `f5ac50af1`)

Added `nmnc` and `nmec` window-NNA sub-buckets to `advisor_nna_canonical.json` via `INF_D_00f`, mirroring the existing `fee_paying`/`no_fee` pattern. Source: `gold/dimensions/accounts_dimension_latest.parquet` `first_trade_date` per household. NMNC = household inception within window, not pre-existing at data_start. NMEC = all others.

AC-F4b.1 PASS: nmnc+nmec == window total to the cent for all 4 advisors × QTD/YTD/MAX. AC-F4b.3 PASS: all existing fields byte-identical. AC-F4b.2 finding: `nmec_nmnc_nna.json` cross-tie is apples-to-oranges (single-day snapshot vs full-history window-sum); CTO PRD scribe dropped that AC. Accepted on AC1+AC3.

Interpretation: QTD/YTD nmnc>0/nmec<0 = new clients net inflow, existing clients net outflow. MAX nmnc ($134.3M) >> nmec ($1.5M) = firm grew primarily via new-client acquisition since inception.

---

### Per-firm account-distribution bell-curves (Andrew-direct, DE VERIFIED PASS)

Built `data/smartx/scripts/compute_per_firm_account_distribution.py` — emits:
- `json/mdpf/49financial/account-distribution.json` (49F: 6,838 accounts, $1.38B, 5 models, S4 canonical names)
- `json/mdpf/inflection/account-distribution.json` (Inflection: 400 accounts, $96.6M, 7 models incl. 50/50 blends)

Shape mirrors global `json/portfolios/account-distribution.json` exactly including histogram. Self-checks PASS (sum(by_model)==total both firms). DE shape/key verified (EXISTS/FRESH/SCALED + field-match; zero rework). Query wired in portal/DEV `5e88321d`, RD~B handed.

**Owned-paths gap:** `data/smartx/**` is AE lane — script staged but not committed. Routed to COO for AE commit.

---

## Commits this session (chronological)

| Commit | Description |
|--------|-------------|
| `30c19b26c` | F1 CHANGE-1: Inflection custody → client_performance spine (ACCEPTED) |
| `e88c54e23` | F5: registry v4 S4 canonical names + consolidation re-resolve |
| `a27c02971` | F4: load_1a_daily period-end-coherent selection + partial-suppress + sentinel |
| `a1a344e6d` | F1 CHANGE-2: Inflection history backfill script (S2 retired) |
| `f44fc3079` | Fix: restore certified_aua load (wse.load_certified_aua → inline fn) |
| `23b0cf755` | Sentinel refinement: 4%→6% threshold + isolation check |
| `f44ab785d` | Patch script: F4 12/26 LTC correction + F1 pre-5/18 Inflection blocks (COO+CTO authorized) |
| `f5ac50af1` | F4b: nmnc/nmec cohort-dim in advisor_nna_canonical.json |
| staged only | `data/smartx/scripts/compute_per_firm_account_distribution.py` (AE owned-paths gate) |

All pushed to CLOUD.

---

## Compiler Tools

| Situation | Tool run | Result |
|-----------|----------|--------|
| Before editing F1 feeder | `comp-pipescript io build_mdpf_wsc_inflection_feeder.py` | MDPF scripts not in comp-graph (BD-gold only); no COLUMN GAPS available. Attempted per Rule 14; fallback to direct reads. Gap flagged twice; COO logged as low-pri follow-on. |
| Before editing F4 backfill | `comp-pipescript io build_mdpf_process_backfill.py` | Same — MDPF not in comp-graph |
| Before editing F4b (INF_D_00f) | `comp-pipescript io INF_D_00f.advisor_nna_canonical.py` | No S3 path constants detected (dynamic key construction); manual review substituted |
| Pre-commit gates | `ds-commit-gate.sh` on all .py edits | All PASS (py_compile + AST + ruff) |
| S3 deploy verification | `comp-pipescript deployed` | MDPF/Inflection scripts not covered by BD-gold deploy checker |

---

## Current State

- MDPF_SCOPED: ALL 5 FINDINGS CLOSED. Project closure with CTO in progress (S1 Phase-2b whole-page scope question assessed by COO+CTO).
- ADVI_INFMVP F4b: CLOSED.
- Per-firm bell-curve: DELIVERED + DE VERIFIED. Commit pending AE path-class resolution.
- F1 daily feeder S3 deploy pending (Rule 13 cycle: aws s3 cp data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py → opal-data-mdpf/code/gold/).

## Next Steps

- [AE] Commit `data/smartx/scripts/compute_per_firm_account_distribution.py` (owned-paths gap resolution)
- [DS~B on next dispatch] F1 daily feeder S3 deploy after COO nod for coherent deploy
- [COO/CTO] MDPF_SCOPED project closure (S1 Phase-2b scope decision)
- [RD~B] Per-firm bell-curve render (DE handed off already)
