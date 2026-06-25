# DATA_ANALYTICS A1 -- PORTAL FIELD / TRANSFORMATION REQUIREMENTS (v0.1)

**Purpose (Andrew-direct 2026-06-25, the strategic reframe):** because we are cutting the Black Diamond / Orion MIDDLEMEN data vendors, the canonical data structure gets built on **Schwab RAW data directly** (we hold it end-to-end; total 49F Schwab AUA = **$1.63B** @06-18 straight from RPS -- BD is not needed to know what 49F holds). The PRIMARY job of the A1 gold-walk is therefore LESS "fix the BD gold" and MUCH MORE **"identify the fields + transformations the portal actually needs"** -- which become the spec for the Schwab-raw-native rebuild:
> **Bronze** = Schwab (then Fidelity) FULL RAW downloads -- every form (RPS / ULN / RLD / TRN / ...), untouched.
> **Silver** = dimensionalized, PURPOSE-BUILT tables -- tight, only the fields the portal needs (THIS doc's output).
> **Gold** = JOINS + ANALYTICS, **daily-incremental** (no full recompute).

**Author:** 0.4.0_DS_ClientPlatform, 2026-06-25 (A1 walk, reframed). **Status:** v0.1 = TABLE-level backbone from the D-tier io map; field-level (exact emitted columns per publisher) + the final Schwab-raw form mapping are the next-depth pass.

---

## 1. The D-tier IS the portal contract (work backward from here)

The 8 D-tier publishers are the ONLY gold scripts that emit the served portal artifacts (`platinum/*`, `gold/artifacts/*`, `gold/entities/*`). So the portal's true field requirements = the union of what the D-tier consumes + emits. The publishers:

| Publisher | Serves (portal artifact) |
|---|---|
| D_00 portal_aggregates | firm header_metrics, clients_tab, AUA-by-{architect,region,state,tax_status} aggregates |
| D_00b portal_timeseries | timeseries_chart (AUA/growth/NNA over time) |
| D_00c portal_leaderboard | employee_leaderboard (advisor rankings) |
| D_00f advisor_nna_canonical | advisor-level NNA |
| D_01 partner_analytics | partner/firm header metrics + role-AUA |
| D_02 advisor_client_detail | advisor -> client drill-down |
| D_03 composition_artifacts | firm/advisor MIX + composition |
| D_04 client_portal_summary | the client-tab summary (the widest reader: 27 inputs) |

## 2. The canonical tables the portal REQUIRES (union of D-tier reads) -> current producer -> Schwab-raw source

| Canonical table (portal needs) | Current producer | Schwab-raw source form (rebuild) | Transformation needed |
|---|---|---|---|
| accounts_dimension | A_00 | RPS account metadata + the account_xref | dimensionalize account attributes (tax_status, relationship, architect/team) |
| client_dimension | A_04 | RPS + xref (household roll-up) | relationship/household aggregation |
| fee_rate_history | A_02 | (BD Fees feed -- NOT in Schwab RPS/ULN/RLD/TRN; **a gap to source** -- fees may stay a separate feed or come from Schwab billing) | SCD fee-rate periods |
| canonical holdings (positions) | B_00 | **RPS directly** (the custodian positions -- no FIFO, no bd reconcile needed) | dedup/normalize positions per account per date |
| canonical lots (realized/unrealized) | B_02 | **ULN (unrealized) + RLD (realized) directly** -- custodian lots; RETIRE B_01 FIFO reconstruction | passthrough/normalize custodian lots |
| account_gains (AUA decomposition) | B_03 | computed from RPS holdings deltas + TRN flows | Growth/NNA decomposition (dAUA = Growth + NNA) -- KEEP (the analytics) |
| canonical_nna (flows) | C_01 | TRN (transaction-classified flows) + the residual | inflow/outflow classification from TRN; residual cross-check |
| canonical/account/client_performance | C_00/C_02/C_03 | computed from holdings + gains | relationship/account performance attribution + cumulative |
| client_tax_liability | C_05 | ULN/RLD lots (gains) + tax_status | per-lot ST/LT gain -> tax estimate |
| mix/composition (C_06/D_03) | C_06/D_03 | RPS positions + asset classification | mix-by-{asset,sector,...} timeseries |
| advisor attribution / team (C_07) | C_07 | RPS account->advisor metadata + xref | advisor/team rollups |
| advisor_fee_efficiency (C_08) | C_08 | fee_rate + AUA + NNA | fee/AUA efficiency |
| the gold/views/* + snapshots (nna_aua_by_*, rel_architect_lookup, aua_by_*) | external/silver + C_07 | derived from the above | the pre-aggregated cuts the portal reads |

## 3. The headline rebuild implications (what this changes vs the BD gold)

1. **Holdings + lots come custodian-DIRECT** (RPS / ULN / RLD) -- this RETIRES the heaviest + patch-laden machinery: the B_01 FIFO reconstruction (and its `bd_stale`/`is_ghost` patches dissolve), and the B_00 BD<->Schwab reconciliation collapses to "read RPS" (Schwab IS the custodian of record -- the reconcile always picked Schwab anyway, B_00 L565). The whole bd-vs-custodian reconcile layer is unnecessary when bronze IS the custodian raw.
2. **The KEEP set is the ANALYTICS, not the ingest:** the genuinely-valuable transformations are the AUA decomposition (Growth/NNA, B_03), performance attribution (C_00/C_02/C_03), NNA-flow classification (C_01), tax-lot gains (C_05), mix/composition (C_06/D_03), advisor attribution (C_07). These are firm-agnostic analytics -- they get rebuilt clean on the Schwab-raw silver, daily-incremental.
3. **The EXCISE set (patch register):** the 90-day flag, the FIFO ghosts, the entity hardcodes, the inferred-tax keyword patch -- all dissolve when bronze is clean custodian-raw + the aberration-excision (the curated-list-then-rules step, Andrew-steered) runs at the source.
4. **fee_rate_history is the one non-custodian gap:** fees aren't in RPS/ULN/RLD/TRN -- the rebuild must source fees separately (Schwab billing feed, or a retained fee feed). Flagged.

## 4. Next-depth pass (what makes this v1.0)
- Per-publisher FIELD-level extraction: the exact emitted columns of each D-tier portal artifact (read the publisher output schemas) -> the precise field list the silver purpose-built tables must carry (drop everything the portal never reads -- the "tight + effective" cut).
- Finalize the Schwab-raw FORM -> silver-table mapping (which RPS/ULN/RLD/TRN columns feed each purpose-built silver table).
- Fold the patch-register excisions in (so the rebuild spec carries none of them).
- Confirm the fee feed sourcing (the one gap).
- C-tier deep reads (C_02..C_08) feed the transformation detail.
