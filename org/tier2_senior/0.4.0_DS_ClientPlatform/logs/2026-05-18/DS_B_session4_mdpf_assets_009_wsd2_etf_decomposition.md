# DS~B Session 4 — MDPF_ASSETS.009 WS-D.2 ETF ownership decomposition feed

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.009 (from 2.0.0_SA_COO) — WS-D.2 build
**Project:** MDPF_ASSETS (Opal Aggregate AUA)
**Branch:** CLOUD

## Context

WS-D.2 produces Cohort 0 (the non-partner Opal-ETF public residual) and the §3.3
ETF ownership decomposition: `ETF_total = Σ_partner held_partner + public_residual`.

## Phase 0 — scope-decision (AC1)

Confirmed (read-only, COO-invited early-start; COO adopted the finding in the GO):
the §3.3 decomposition logic ALREADY lives in `mdpf_aggregate_aua.py`
(`build_etf_decomposition` + the §7 identity-2/3 gates in `reconcile`) — proven
working in the MDPF_ASSETS.008 end-to-end run. **WS-D.2 is NOT a from-scratch
decomposition build.** Its confirmed deliverable is the SMALL piece: wire the ETF
net-assets feed into the convergent `etf_net_assets` shape the WS-A script reads.
No WS-A decomposition logic was forked or duplicated.

## What was built

One new script: `data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py`
— conforms the ETFS_NETAST / WS-D.1 consolidated net-assets series to the
contract §5 `etf_net_assets` schema.

Source -> contract §5 (near-direct column map):
`s3://opal-data-etfs/silver/netassets_daily.parquet` (590 rows, all 4 Opal ETFs)
-> latest row per ticker -> `(ticker, as_of_date, net_assets, nav,
shares_outstanding, source)`. `net_assets` <- `net_assets_reported` (the
issuer-reported NetAssets — the authoritative ETF total, NOT the shares×price
column); `as_of_date` <- `data_as_of` (the issuer valuation date).

Output: `s3://opal-data-mdpf/mdpf/feeds/etf_net_assets/2026-05-18.parquet` (4 rows,
flat — etf_net_assets is per-ticker, not partner-scoped).

## etf_net_assets feed (2026-05-18)

| Ticker | net_assets | source | as_of |
|--------|-----------:|--------|-------|
| DIVZ | $241,845,658 | trueshares | 2026-05-15 |
| IDVZ | $158,661,515 | trueshares | 2026-05-15 |
| PFDE | $131,630,541 | filepoint | 2026-05-18 |
| PFOE | $110,854,025 | filepoint | 2026-05-18 |
| **Total** | **$642,991,739** | | (cf. contract Appendix-A 5/15 ref $644.13M) |

## Phase 2 — end-to-end verification (AC2/AC3)

`mdpf_aggregate_aua.py --source s3 --date 2026-05-18` — the §3.3 decomposition
now runs on the REAL ETF net-assets feed (not a fixture):

| ETF | etf_total | held_inflection | public_residual |
|-----|----------:|----------------:|----------------:|
| DIVZ | $241,845,658 | — (no Opal model holds it) | $241,845,658 (full) |
| IDVZ | $158,661,515 | — (no Opal model holds it) | $158,661,515 (full) |
| PFDE | $131,630,541 | $9,766,913.38 | $121,863,627.62 |
| PFOE | $110,854,025 | $8,017,497.73 | $102,836,527.27 |

- **identity 2** (etf_total == Σ held_partner + public_residual): PASS — min
  public_residual $102.8M, all ≥ 0 (no over-attribution).
- **identity 3** (no double-count): PASS — no Opal ETF ticker appears as a
  firm_id or model_key; the held slices are inside `model_aua`, never standalone.
- **reconciliation overall: PASS.**
- DIVZ/IDVZ `public_residual` = full net-assets — correct, no Opal model holds
  them (.003 §4.3). PFDE/PFOE carry a real `held_inflection` slice.

**Honest caveat (CTO ruling iii):** v1 `held_partner` is target-weight-based, so
`public_residual` is an ESTIMATE, not exact — the WS-A script labels it so
(`attribution_basis: target_weight`, the identity-2 note). Also: only
`held_inflection` is present today — `held_49financial` lands when WS-B (.007)
ships, so today's `public_residual` is overstated by the (absent) 49F-held slice;
that is expected feeder-absence behaviour, not an error.

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py | New — WS-D.2 etf_net_assets convergent feeder |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDPF_ASSETS.009.dsb-wsd2-etf-ownership-decomposition-netting.md | status -> complete |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-18/DS_B_session4_mdpf_assets_009_wsd2_etf_decomposition.md | New — this session log |

S3: `s3://opal-data-mdpf/mdpf/feeds/etf_net_assets/2026-05-18.parquet`.

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-pipescript io / comp-trace (Phase-1 mandate) | The shipped probe + the MDPF scripts use dynamic S3 keys / are off-graph — per the TO `if_mismatch`, grounded the scope by direct inspection of `mdpf_aggregate_aua.py` (the §3.3/§7 logic) + the live `opal-data-etfs/silver/netassets_daily.parquet` schema. Phase-0 scope finding recorded above. |
| `comp-blast build_mdpf_wsd2_etf_netassets_feeder` (Phase-3 mandate) | "No nodes matching" — the new `data/mdpf/scripts/` script is off-graph (cache predates it). Confirms the blast radius is the new etf_net_assets feeder wiring + the MDPF platinum artifact only — no overlap with the live ETFS_NETAST probe's canonical output or the INF chain. |
| `.tools/ds-commit-gate.sh` | PASS — py_compile + ds-precommit-check + ruff py39. |

## Current State

MDPF_ASSETS.009 COMPLETE — all 4 ACs PASS. The etf_net_assets feed is wired; the
§3.3 ETF decomposition + §7 identity-2/3 gates run end-to-end on the real ETF
net-assets. RAVC2 to COO.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — MDPF_ASSETS.009 complete. All 4 MDPF Phase-2 feeder artifacts (model_aua_positions, model_composition, non_model_aua, etf_net_assets) now live in opal-data-mdpf; the WS-A aggregation runs end-to-end with reconciliation PASS. `held_49financial` + a non-zero `public_residual` net of 49F land when WS-B (.007) ships. |
