# MDPF WS-A page-wire note (MDPF_ASSETS.016 / .024 / .025 sidecar)

**Author:** 0.4.0_DS_ClientPlatform~B | **Date:** 2026-05-20
**Sidecar to:** `docs/architecture/MDPF_ASSETS_WSA_CONTRACT.md`
(informational; the canonical contract is amended by CTO ratify only)

Updated 2026-05-20 for the PRD v0.8 taxonomy correction + Andrew Ruling 2
(supersedes the earlier 1a+1b+1c+2a / Schwab-basis framing of this note).

## What the Model Portfolios page must consume

The Model Portfolios global AUA headline is **`aggregate.opal_aggregate_aua`**
in the platinum partitions (`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json`)
and the `aggregate.opal_aggregate_aua` array in the rollup
`platinum/mdpf/aggregate_aua_timeseries.json`.

`opal_aggregate_aua = Cohort 1a + 1b + 2a` — every partner's model AUA, plus
49 Financial's non-model (1b). **Cohort 1c (SMA) is a NON-ADDITIVE sub-slice
of 1b** — already inside the non-model figure, never a separate addend
(Andrew 2026-05-20: "1c is a subdivision of 1b, so cant double count that").
PRD `docs/architecture/MDPF_ASSETS.md` v0.8 §3.0.1 / §3.4. Shipped to the live
aggregator by **MDPF_ASSETS.024** (`mdpf_aggregate_aua.py`) and to the
historical series by **MDPF_ASSETS.016** (`build_mdpf_process_backfill.py`).

The page must NOT consume, as the headline:
- `partner_aua_subtotal` — the all-partner 2-term sum (includes Cohort 2b).
- `cohort_2b_audit` — Inflection non-model (2b). Audit field; tracked, not in
  the headline.
- `etf_public_residual_total` — Cohort 0, ETF public residual. Audit field;
  tracked daily, NOT emitted to the portal-facing slice.

`headline_formula` on the aggregate block states this in-artifact.

## 49 Financial basis (Andrew Ruling 2)

`non_model_aua(49F)` = `certified_aua - model_aua(1a)` — the FULL Black Diamond
book (`certified_aua`, all four custodians), SMA-inclusive. NOT the
Schwab-custodied subset. WS-E (`build_mdpf_wse_49f_non_model_aua.py`,
MDPF_ASSETS.025). 49F total (1a+1b) reconstructs `certified_aua` to the cent.

## methodology_version — basis discontinuity at 2026-03-11

Every .016 platinum partition carries a machine-readable `methodology_version`
field (top-level). A downstream consumer reads it to detect the 1b basis
discontinuity:
- `v0_8_ruling2` — 2026-03-11 → 2026-05-15 (46 dates): 1b on the full-book
  certified_aua basis (PRD v0.8 / Ruling 2).
- `pre_ruling2` — 2026-01-19 → 2026-03-10 (35 dates): pre-Ruling-2; 30 carry
  the pre-existing Schwab-basis 1b (`certified_aua` history starts 2026-03-11
  so the early window could not be re-run on the full-book basis — AC8
  preserved these), 5 are market-holiday null-1b dates.
- absent (null) — partitions outside the .016 scope (pre-2026-01-19;
  daily-forward 2026-05-18+).

The `aggregate_aua_timeseries.json` rollup carries a parallel
`methodology_version` array, one entry per date.

## Historical coverage (MDPF_ASSETS.016)

- 2026-03-11 → 2026-05-15: full v0.8/Ruling-2 re-run; `non_model_aua` on the
  certified_aua basis; `etf_decomposition` populated where WS-D feeders exist
  (DIVZ/IDVZ real Cohort 0; PFDE/PFOE honest-null pre-2026-05-18 — no
  Filepoint NAV history).
- 2026-01-19 → 2026-03-10: pre-existing partitions preserved (AC8 empty-
  overwrite guard); pre-Ruling-2 Schwab-basis 1b. Tagged `pre_ruling2`.
- `opal_aggregate_aua` on the historical 49F-only series == the 49F partner
  total = 1a+1b (2a=0, no Inflection partner historically), which is the
  1a+1b+2a headline for those dates.

## Known tail gap (for COO -- tracked follow-up)

The 2026-05-18 / 05-19 daily-forward partitions still carry the pre-.024
headline (`partner_total`, includes 2b). MDPF_ASSETS.016 scopes the backfill
to <= 2026-05-17; MDPF_ASSETS.024/.025 are forward-only. 2026-05-20 was
re-materialized on the v0.8 headline by the .024/.025 end-to-end verification
run. 05-18 / 05-19 converge to the 1a+1b+2a headline on the next daily-chain
re-materialization. Tracked by COO~B as a data-quality follow-up.

## Optional future follow-on (CTO~B -> Andrew)

A uniform pre-2026-03-11 series on the full-book basis would require the BD
pipeline to backfill `gold/aua_certification/` for 2026-01-17 → 2026-03-10.
Out of MDPF_ASSETS.016 scope; routed to Andrew as an optional follow-on.
