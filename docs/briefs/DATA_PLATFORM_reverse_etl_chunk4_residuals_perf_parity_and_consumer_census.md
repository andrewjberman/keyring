# DATA_PLATFORM reverse-ETL — chunk-4 RESIDUALS closed: perf-parity (#1) + BD-analytic consumer census (#3)

**Lane:** 0.4.0_DS_ClientPlatform~B · **Lead/integrator:** 0.4.0_DS_ClientPlatform · **Directed by:** base-DS (the two no-crawl residuals I surfaced)
**Date:** 2026-06-24 · **Status:** both residuals GROUNDED (no-crawl); reinforce the chunk-4 DECISION-GRADE close. RAVC2 base-DS+COO+CTO (cc CVO)
**Scope:** the two no-crawl residuals on chunk-4 (perf-parity un-run; transitive consumer-census). cot/inf Orion/Eclipse projection HELD (Andrew risk-gate).

---

## RESIDUAL #1 — PERF-PARITY: RESOLVED feasibility-positive (BD delivers NO performance to parity against)

CVO's chunk-4 RECO: "confirm whether a BD-published-perf artifact is held — if yes run the diff; if not, Row 4A stays self-computable-CONFIRMED + parity-INFERRED." **Answer: NONE is held, and BD delivers none.**
- **File-level:** scanned opal-data-bd (forwardfill_v2 351 + bronze 70 + silver 7,644 objs) + opal-data-cot (447 objs) for perf/return/twr/dietz/irr/ror keys -> **ZERO hits.**
- **Delivery-level:** the BD DataMining feed is EXACTLY 5 prefixes — `forwardfill_v2/{allocations,assets,realized,transactions,unrealized}`. **No performance/returns export.**
- **Column-level:** the assets/qt1 export (31 cols: asset_class/segment, price, cusip, transaction_type) carries **no return/perf column**; the allocations/qt5 export (92 cols, chunk-2) carries benchmark *names* but no return.
- **Verdict:** BD delivers raw data, never computed performance. So the perf-parity diff (our C_03 vs BD-published) is **NOT achievable no-crawl** — there is no BD-perf artifact in the estate to diff against. This **RESOLVES the Row-4A INFERRED in the feasibility-positive direction**: it is the SUPPLY-side confirmation of chunk-4's DEMAND-side finding — C_00 ingests no BD-perf (demand) because **BD delivers none** (supply). There is no BD-performance dependency to match.
- **To fully close the parity (optional, gated):** the only BD-published perf lives in BD's own platform/statements -> a BD-platform crawl or a manual statement pull = **Andrew risk-gated** (out of no-crawl scope). NOT needed for the feasibility verdict; flagged as the one residual path.

## RESIDUAL #3 — BD-ANALYTIC CONSUMER CENSUS: NOTHING consumes a BD-computed analytic directly

Traced the full `advi-bd` thread (`pipescript advi-bd` — 19 threads, 15 in-scope). Transitive, not just the linear perf chain (CVO's belt-and-suspenders ask).
- **BD inputs are ALL RAW** (custodian feeds + firm config): bd-allocations (dimension), bd-asset-dim (positions/classification), bd-bronze-transactions, bd-fees (fee config = T2-HOST), bd-realized-gains + bd-unrealized-gains (lots). **No BD-computed analytic is delivered.** Even pricing is self-owned: bd-historical-prices = **yfinance** (not BD) + bd-canonical-prices = OUR maintainer.
- **ALL analytics are computed in OUR gold** (bd-gold-layer-pipeline, gold_dispatch.sh A_00..D_04): positions_cube, holdings_lots, account_gains, canonical_nna, canonical performance, client/advisor analytics, platinum/firm artifacts.
- **ALL frontend / mounted-reachable consumption = OUR gold outputs via OUR Lambdas:** bd-gold-layer-pipeline (gold/* + platinum/firm/* -> AdvisorIntelligence 49financial /api/scoped/*), bd-portal-publisher (gold/artifacts/* leaderboard/clients_tab/header_metrics/snapshots -> AdvisorIntelligence tabs), bd-client-detail-api (gold/clients/{relationship_id}.json -> client-detail drill). **No mounted-reachable path serves a BD analytic.**
- **Verdict:** **NOTHING consumes a BD-computed analytic directly** — there are none in our estate. This **HARDENS chunk-4's "no BD ingest"** transitively across the whole BD thread. The supplant surface for BD/49F = (a) replace BD's RAW-data delivery (custodian feeds — Schwab-DIRECT held for 49F) + (b) host the firm-config (T2-HOST: allocations dimension + fees). **No BD analytic to replace.**
- **Cross-ref (not mine):** the realized/unrealized LOT exports (bd-realized/unrealized-gains -> B_02/B_03) are the one place a BD *computation* might enter (FIFO lot reconstruction vs custodian-lot passthrough) — that is base-DS's **chunk-1 lot-diff**, explicitly NOT re-done here.

---

## NET (reinforces the chunk-4 DECISION-GRADE close)
Both no-crawl chunk-4 residuals are resolved: (1) BD delivers no performance -> no parity dependency exists (4A INFERRED resolved feasibility-positive, supply+demand both confirmed); (3) nothing consumes a BD analytic directly -> the "no BD-IP" close is transitive across the whole advi-bd thread, not just the perf chain. The BD/49F supplant surface = raw-data-delivery (Schwab-direct held) + firm-config-hosting (T2-HOST migrate-SoR). **Confidence:** 49F SOURCE-CONFIRMED; the only un-closeable-no-crawl item = BD-platform perf parity (Andrew-gated, not needed for feasibility). cot/inf HELD per gate.

## GROUNDING
comp-which (routing) -> pipescript advi-bd (the consumer census, full thread); live boto3 estate scan (perf-artifact existence, off-rail Rule-21 data-access). No raw repo-grep. Rule-22: residual #1 "could-not-diff" is a FINDING (no artifact exists), not a gap glossed; residual #3 is transitive-trace-confirmed.
