# DATA_ANALYTICS — UNIFIED PORTAL CONTRACT v1.0 (FE-down ⇄ gold-up, co-signed)

> **STATUS REFRAME (Andrew-direct via DS, 2026-06-25; CTO `172040Z`):** The Schwab-raw-native canonical is a **PARALLEL R&D
> build that COEXISTS with BD** — **NO excise of B_00/B_01, NO cutover, NO contract-LOCK, NO decommission.** The live 49F
> pipeline + served $1.83B are UNTOUCHED. This doc is the **PARALLEL R&D FOUNDATION DESIGN**, not a locked production-rebuild
> contract. The DESIGN content below (D-tier-waist closed-vertical, the per-partner platinum demand map, strict-form/silver-dim
> supply) STAYS and is the prospective foundation. The production-cutover framing — "contract LOCKS", the §4b excise/value-parity
> arch-gate disposition, N1-decommission-exempt, N2-partial-lock — **is STOOD DOWN** (Tier-1 was over-applying cutover machinery
> to R&D). CVO involvement = light validation (is the parallel build correct + isolated), NOT a lock-gate. COO authors NO
> cutover build-TOs. Read the tables below as the R&D target shape, not a staged migration.

**Authors:** 0.4.0_DE_ClientPlatform (FE-down / demand) + 0.4.0_DS_ClientPlatform (gold-up / supply, co-sign)
**Date:** 2026-06-25 | **archetype:** COORDINATE
**For:** 1.0.0_SA_CTO (arch-gate → Schwab-raw-native canonize-gold rebuild) · 3.0.0_SA_CVO (cert) | **cc:** 2.0.0_SA_COO
**Sources merged:** FE1 manifest `DATA_ANALYTICS.FE1_advi_panel_platinum_groupd_manifest.md` @ 98764fb65 (panel→platinum→D-publisher) × DS `DATA_ANALYTICS_A1_portal_field_requirements_v0.1.md` + `..._silver_dim_design_v0.2_keys.md` (D-publisher→canonical-table→Schwab-raw-form) × convergence record `DATA_ANALYTICS.FE1_portal_contract_convergence_record.md` @ 512623a78.

> **The contract is ONE vertical thread:**
> `ADVI PANEL → frontend COMPONENT → platinum KEY → D-tier PUBLISHER → canonical SILVER TABLE → Schwab-raw FORM`.
> FE1 owns the top half (panel→D-publisher, the DEMAND); A1 owns the bottom half (D-publisher→Schwab-raw, the SUPPLY).
> **They join at the D-tier publisher** — the 8 D-scripts are the ONLY emitters of served portal artifacts, so the D-tier
> IS the contract waist. This doc stitches the full vertical and is the spec the lean rebuild provisions against.

---

## 1. The join spine — the 8 D-tier publishers (contract waist)

| D-publisher | FE panels it serves (demand, FE1 §2) | Canonical tables it reads (supply, A1 §2) | Schwab-raw source forms |
|---|---|---|---|
| **D_00** portal_aggregates | PartnerAnalytics donut/bell/cards; ClientsTab headline (`header_metrics.json`) | accounts_dimension, client_dimension, holdings, gains | RPS (+ account_xref) |
| **D_00b** portal_timeseries | PartnerAnalytics + Distribution (`timeseries_overview/chart.json`) | account_gains, canonical_nna, holdings ts | RPS deltas + TRN |
| **D_00c** portal_leaderboard | Advisors tab + Books leaderboard (`leaderboard.json`, `fee_efficiency.json`) | advisor attribution (C_07), advisor_fee_efficiency (C_08) | RPS acct→advisor meta + **fees [N1]** |
| **D_00f** advisor_nna_canonical | Distribution continuous-NNA + AdvisorAnalytics (`advisor_nna_canonical.json`) | canonical_nna (C_01) | TRN flows |
| **D_01** partner_analytics | PartnerAnalytics + Distribution snapshot (`partner_analytics_{gran}.json`) | role-AUA, canonical perf | RPS + advisor meta |
| **D_02** advisor_client_detail | Books advisor→client drill; Distribution ADV-NNA client drill (`advisors/{id}/*`, `nna_clients.json`) | client_dimension, holdings, gains, nna | RPS + xref + TRN + **household [N2]** |
| **D_03** composition_artifacts | Books mix/composition; AdvisorPublicProfile (`mix_summary.json`, `composition.json`) | mix/composition (C_06), positions + asset classification | RPS positions |
| **D_04** client_portal_summary | **Books/ClientsTab + the entire L3 client/account drill** (`dashboard.json`, `clients/{hh}/*`, `accounts/{id}/*`, Cohort-A) — the widest reader (27 inputs) | client_dimension, holdings, lots, gains, tax, fee, perf | RPS + ULN + RLD + TRN + **fees [N1]** + **household [N2]** |

**Publisher-shape divergence (load-bearing for the rebuild):**
- **49F & COT** funnel ALL platinum through **`D_04` (single publisher)**; D_00/D_00b/D_00c/D_00f/D_01/D_02/D_03 write `gold/artifacts/*` intermediates D_04 republishes. The Schwab-raw rebuild targets this single-publisher shape.
- **Inflection** fans across **~20 `INF_D_0x`** publishers (partner_analytics via `INF_09`), incl. INF-unique Insights (`INF_D_05/06/07a`), GRO (`INF_D_00c`), per-account ts (`INF_D_09`). INF is its own rebuild shape — out of the 49F/Schwab-raw target.

---

## 2. Canonical silver tables → Schwab-raw forms (supply, A1, co-confirmed)

| Canonical table (portal needs) | BD producer | Schwab-raw form (rebuild) | Note |
|---|---|---|---|
| accounts_dimension | A_00 | RPS metadata + account_xref | tax_status/relationship/architect attrs |
| client_dimension | A_04 | RPS + xref household roll-up | **needs N2 household grouping** |
| canonical holdings (positions) | B_00 | **RPS direct** | retires BD↔Schwab reconcile (Schwab IS custodian of record) |
| canonical lots (realized/unrealized) | B_02 | **ULN + RLD direct** | **retires B_01 FIFO reconstruction** + its ghost patches |
| account_gains (AUA decomp) | B_03 | RPS deltas + TRN | KEEP analytic: dAUA = Growth + NNA |
| canonical_nna (flows) | C_01 | TRN classified + residual | inflow/outflow from TRN |
| perf (canonical/account/client) | C_00/C_02/C_03 | holdings + gains | attribution + cumulative |
| client_tax_liability | C_05 | ULN/RLD lots + tax_status | per-lot ST/LT → tax est |
| mix/composition | C_06/D_03 | RPS positions + asset classification | mix-by-{asset,...} ts |
| advisor attribution/team | C_07 | RPS acct→advisor meta + xref | rollups |
| fee_rate_history / advisor_fee_efficiency | A_02 / C_08 | **NOT in Schwab raw → N1** | separate fee feed |

**KEEP = the ANALYTICS** (Growth/NNA decomp, perf attribution, NNA classification, tax-lot gains, mix, advisor attribution) — firm-agnostic, rebuilt clean on Schwab-raw silver, daily-incremental.
**EXCISE = the patches** (90-day flag, FIFO ghosts, entity hardcodes, inferred-tax keyword patch) — dissolve when bronze IS clean custodian-raw.

---

## 3. The 2 NON-CUSTODIAN inputs (Schwab-raw does NOT carry — must be provisioned explicitly)

| # | Input | FE consumers that break without it | Supply path | Status |
|---|---|---|---|---|
| **N1** | **FEES** (fee_bps / schedule → `dim_fee`) | Books `FeeEfficiencyPanel`+`FeeSummaryPanel` (`fee_efficiency.json`), ClientsTab income/fees, AdvisorPublicProfile fee section, advisor/client `fee_summary` | Opal-bridged: Schwab billing feed OR retained BD-fees feed → A_02/C_08 | gap-to-source; rebuild sources fees separately |
| **N2** | **HOUSEHOLD / RELATIONSHIP GROUPING** | every `client_count` headline, `client_directory.json`, `ClientListPanel`, entire L3 client drill `clients/{hh}/*` | Opal-owned-or-bridged: Schwab `ssn_tin`=4,188 taxpayers → portal `client_count`=2,928 BD-relationship grouping | **Andrew ruling source NOW: bridge-via-xref vs Opal-owned dim** |

A Schwab-raw-ONLY rebuild silently drops `client_count` correctness (N2) + all fee panels (N1). The arch-gate must provision both.

---

## 4. Per-partner ESSENTIAL vs AGNOSTIC (lean-rebuild scope)

| Partner | Essential D-publishers (rebuild MUST carry) | Agnostic-drop (this rebuild) |
|---|---|---|
| **49F** (BD→Schwab-raw target) | D_04 + D_00/D_00b/D_00c/D_00f/D_01/D_02/D_03 (all panels active) | none |
| **Cottonwood** (BD-native) | **D_00, D_00b, D_01, D_04 only** (PartnerAnalytics aua/nna/geo + Distribution-geo) | **D_00c, D_02, D_03, cohort_a_summary, cash_coverage_summary** (Advisors+Books disabled v1; re-add when COT advisor dim materializes) |
| **Inflection** (Orion — distinct shape) | the ~20 `INF_D_0x` set | n/a (not the Schwab-raw target) |

**Gaps ruled INTENDED-ABSENT** (CVO formal co-sign on 4a): (4a) COT has no `D_00f.advisor_nna_canonical` → geo-only v1, FE graceful; (4b) `header_metrics_fresh` is INF-origin, 49F/COT fall back to `header_metrics.json` — **the Schwab-raw rebuild closes 4b by construction** (fresh AUA native from `fact_position`, $1.63B 49F).

---

## 4b. R&D DESIGN NOTES (formerly "arch-gate disposition" — STOOD DOWN to parallel-R&D framing per CTO `172040Z`)

> The items below were CTO rulings under a production-cutover premise that Andrew reset to parallel-R&D. They are retained
> as DESIGN RATIONALE (how the parallel build should be shaped), NOT as production gates: there is **no excise, no LOCK,
> no decommission, no partial-lock.** Read "excise" as "the parallel build's strict-form omits the BD-reconcile layer by
> design" and "value-parity" as "the R&D characterization check that the parallel build's values are sane vs the live BD book."

- **G1 (D-tier-waist + bronze-raw/silver-dim/gold-incremental):** ACCEPT. Lock-gate = CVO FE1-completeness cert.
- **G2 (excise B_01-FIFO + B_00-reconcile + flags):** ACCEPT **with VALUE-PARITY rider.** Excising B_01/B_00 is destructive removal of *derived* layers, so the close-gate is a value-parity census, not a field-name check: the CVO cert must verify the Schwab-native chain reproduces **every SERVED FIELD'S VALUE** — especially any B_01-FIFO-derived or B_00-reconcile-adjusted/`bd_stale`/`is_ghost`-patched value. DS's exact $1.63B `fact_position` tie is the model. **Rule: no excise silently drops or changes a served-consumed value; the census covers transitive/derived deps, not just direct reads.**
- **G3 (49F-first / COT-follows / INF-separate):** ACCEPT. **COT is BD-native not Schwab-native** → its rebuild is gated on the BD leaner-snapshot/custodian-direct methodology proving out (ADVI_COTETL + ADVI_BDAPIMIG REST ingest) AND on BD-native lots being stable — sequence COT after 49F proves the pattern. COT panel-drop set consistent with the COTETL advisor-thinness ruling.
- **N1 (FEES):** SCOPED — **RETAIN the BD-fees feed** as interim fee source (→ A_02/C_08, unchanged). **Cross-link: this EXEMPTS `bd-fees` (i-0868fc7e7ebec26f2) from the ADVI_BDAPIMIG Phase-2 scrape-box decommission** — bd-fees is the live fee dependency, not a dead scrape. + OPEN discovery (DS/AE): does Schwab billing/RPS carry `fee_bps`/schedule? Yes → migrate fees Schwab-native later; No → BD-fees-retained is durable. Fees NOT dropped.
- **N2 (HOUSEHOLD):** CONFIRMED sovereign (Andrew's; **Andrew DEFERRED — "hold, return to it"**). Does NOT block the arch-gate. **PARTIAL-LOCK:** contract LOCKS for non-household panels; household-dependent panels (`client_count` headline / `client_directory` / L3 client-drill) stay PENDING-N2.

**~~LOCK condition~~ — STOOD DOWN:** there is no contract-LOCK and no cutover build-TO decomposition. The parallel R&D build proceeds prospectively; CVO does light correctness/isolation validation (not a lock-gate); BD + the served $1.83B stay live and untouched. N1 fees / N2 household / N3 AUA-completeness remain DESIGN considerations for the parallel build, not production gates.

## 5. Contract status
**CLOSED invariant:** every FE panel field resolves to a named producer (gaps 4a/4b ruled intended-absent); every produced-but-unconsumed output is confirmed agnostic-drop. Demand (FE1 §2) and supply (A1 silver-dim) are CONGRUENT. The 2 non-custodian inputs (N1/N2) are flagged for explicit provisioning. Co-signed DE+DS; awaiting CVO cert (FE1 completeness + gap-4a ruling) + CTO arch-gate (fold into the rebuild). **Open external:** Andrew's N2 household-grouping source ruling.
