# MDPF WS-A page-wire note (MDPF_ASSETS.016 / .024 sidecar)

**Author:** 0.4.0_DS_ClientPlatform (DS Base) | **Date:** 2026-05-20
**Sidecar to:** `docs/architecture/MDPF_ASSETS_WSA_CONTRACT.md`
(informational; the canonical contract is amended by CTO ratify only)

## What the Model Portfolios page must consume

The Model Portfolios global AUA headline is **`aggregate.opal_aggregate_aua`**
in the platinum partitions (`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json`)
and the rollup `aggregate.opal_aggregate_aua` array in
`platinum/mdpf/aggregate_aua_timeseries.json`.

`opal_aggregate_aua = Cohort 1a + 1b + 1c + 2a` — every partner's model + SMA,
plus 49 Financial's non-model (1b). This is the Andrew 2026-05-20 ruling
(PRD `docs/architecture/MDPF_ASSETS.md` §3.0.1), shipped to the live aggregator
by **MDPF_ASSETS.024** and to the historical series by **MDPF_ASSETS.016**.

The page must NOT consume, as the headline:
- `partner_aua_subtotal` — the all-cohort partner sum (includes Cohort 2b).
- `cohort_2b_audit` — Inflection non-model (2b). Audit field; tracked, not in
  the headline.
- `etf_public_residual_total` — Cohort 0, ETF public residual. Audit field;
  tracked daily, NOT emitted to the portal-facing slice.

`headline_formula` on the aggregate block states this in-artifact.

## Historical coverage (MDPF_ASSETS.016)

- 2026-01-19 → 2026-05-15: `etf_decomposition` populated; Cohort 0 =
  DIVZ + IDVZ public residual. PFDE/PFOE are honest-null historically
  (no Filepoint NAV history before 2026-05-18) — ~5.4% of Cohort 0.
- Pre-2026-01-19: partner-only, no etf_decomposition (out of backfill scope).
- `opal_aggregate_aua` on the historical 49F-only series == the 49F partner
  total (1a+1b+1c; 2a=0 — no Inflection partner historically), which is the
  1a+1b+1c+2a headline for those dates. The .016 backfill ADDED the Cohort 0
  audit data; it did not move `opal_aggregate_aua`.

## Known tail gap (for COO)

The 2026-05-18 / 05-19 / 05-20 daily-forward partitions still carry the
pre-.024 headline (partner_total, includes 2b). MDPF_ASSETS.016 scopes the
backfill to ≤ 2026-05-17; MDPF_ASSETS.024 is forward-only. Those 3 dates are
covered by neither — they converge to the 1a+1b+1c+2a headline only on a
re-materialization or as the daily chain rolls forward. Surfaced to COO.
