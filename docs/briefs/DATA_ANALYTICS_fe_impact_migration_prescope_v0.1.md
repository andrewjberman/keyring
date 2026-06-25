# DATA_ANALYTICS — Schwab-raw-native rebuild: FE-IMPACT / MIGRATION PRE-SCOPE v0.1

**Author:** 0.4.0_DE_ClientPlatform (FE-lead) | **Date:** 2026-06-25 | **archetype:** EXPLORE
**For:** 2.0.0_SA_COO (fold into build-TO set on contract-lock) · 1.0.0_SA_CTO (arch-gate context) | **cc:** 0.4.0_DS, 3.0.0_SA_CVO
**Anchored to:** `DATA_ANALYTICS_unified_portal_contract_v1.0.md` (the served platinum keys, per partner). **Status:** pre-scope (ready to fold into FE build-TOs the moment the contract LOCKS).

---

## 0. Governing principle — the rebuild is CONTRACT-STABLE, so FE-impact is the EXCEPTION not the rule

The rebuild's spec IS the portal contract: it re-emits **exactly the same `platinum/` keys, same schemas** the FE already reads — produced from Schwab-raw instead of BD-reconciled silver. **If a platinum artifact's schema is held stable, the FE that reads it does not change at all.** So this pre-scope is NOT a portal rewrite — it's the targeted list of the THREE places FE-impact actually concentrates:

| Class | Definition | Default expectation |
|---|---|---|
| **T (Transparent)** | platinum key schema unchanged; only the *source* under it changes (BD→Schwab-raw) | **No FE change.** Validate by render-parity. The bulk of the surface. |
| **C (Cleanup)** | a FE adapter/patch exists ONLY to paper over a BD quirk the rebuild removes | FE simplification *opportunity* (not a break) — can defer or fold opportunistically |
| **X (Change-required)** | a field's POPULATION / MEANING / shape changes under Schwab-raw | the real FE work — scoped below |

**The hard contract for the rebuild (FE ask):** hold the platinum schemas byte-stable except where §2 (Class-X) explicitly calls a change. Every Class-X is a coordinated DS-emit + FE-consume change.

---

## 1. Class-C — FE adapters/patches that the clean rebuild lets us RETIRE (cleanup, not break)

These exist on the FE today purely to survive BD-pipeline quirks the Schwab-raw rebuild dissolves. Opportunistic removal, not blocking:

| FE site | What it papers over | Rebuild effect |
|---|---|---|
| `advisor-intelligence.ts` NaN/Infinity string-strip (`apiRequest`, `getFirmLeaderboard`, `getPlatinumFirmDashboard`) | Python `json.dumps` emitting `NaN`/`Infinity` from div-by-zero in AUA-weighted aggs | rebuild emits `allow_nan=False` at source → FE strip becomes dead belt-and-suspenders (keep until proven, then drop) |
| `extractChainTimestamp` multi-key reader (`data_as_of` / `as_of_date` / `snapshot_date`) | gold scripts using 3 different freshness field-name aliases | rebuild canonicalizes ONE `data_as_of` → multi-key reader collapses to single-key |
| Small-account em-dash / `SMALL_ACCOUNT_THRESHOLD_USD` handling | BD 90-day-flag / ghost-account artifacts surfacing tiny/aberrant accounts | aberration-excision at source → fewer FE em-dash special-cases |
| `ADHC_FECACHE_COHERENCE` interceptor (chain-coherence invalidation) | mixed-vintage platinum across views (18h staleness class) | daily-incremental + single chain-emit reduces (not eliminates) the cross-view-vintage risk |

## 2. Class-X — fields whose POPULATION/MEANING changes (the real FE work)

| # | Field / artifact | Component(s) affected | Change under Schwab-raw | FE action |
|---|---|---|---|---|
| X1 | **lots realized/unrealized** (`platinum/clients/{hh}/*`, account summary, `TaxCostBasisPanel`) | Books L3 client/account drill; `TaxCostBasisPanel`; `AdvisorBookView` | B_02 becomes **passthrough of custodian ULN/RLD** (retires FIFO reconstruction). Per-lot field set may differ (custodian lot shape vs reconstructed) | verify the per-lot fields the tax panels read still populate; adapt if custodian lot schema differs |
| X2 | **fees** (`fee_efficiency.json`, advisor/client `fee_summary`, `FeeEfficiencyPanel`/`FeeSummaryPanel`) | Books fee panels; AdvisorPublicProfile fee section; ClientsTab income/fees | **N1 non-custodian** — depends which fee-feed the rebuild sources (Schwab billing vs retained BD-fees) | gate on CTO's N1 fee-feed decision; FE field-shape may change if feed differs |
| X3 | **client_count / household grouping** (every `client_count` headline, `client_directory.json`, L3 drill) | PartnerAnalytics, ClientsTab, dashboard, ClientListPanel | **N2 SOVEREIGN — Andrew DEFERRED.** Grouping source unresolved (taxpayer 4,188 vs relationship 2,928) | **HOLD — no FE change until Andrew rules N2.** Contract flags it pending; nothing re-points yet |
| X4 | **`header_metrics_fresh.json`** (headline AUA tile) | PartnerAnalytics / ClientsTab headline | gap-4b: rebuild produces native daily-fresh AUA → bd/cot CAN emit a fresh-header (today INF-only) | **OPTIONAL new capability** — if Andrew wants the fresh tile on 49F/COT, wire `getHeaderMetricsFresh` for them (already coded; just needs the artifact). Net-new, not a break |

## 3. Per-partner FE migration sequencing

1. **49F FIRST** (the Schwab-raw target). Full panel set; single-`D_04` re-emit. FE validation = render-parity of every 49F panel against the re-emitted platinum (Class-T proof) + X1/X2 verification. This is the FE migration's proving ground.
2. **Cottonwood SECOND** (BD-native, same `D_00/D_00b/D_01/D_04` shape, reduced surface). Smaller surface (PartnerAnalytics+Distribution-geo); inherits 49F's Class-T proof. The 4a 404-gate (757f4d99) already hardens COT for the reduced surface.
3. **Inflection — SEPARATE TRACK** (Orion, ~20 `INF_D_0x`, not the Schwab-raw target). No FE migration under this rebuild; the INF static-S3 adapters + Insights panel stay as-is. Re-scope only if/when Inflection moves off Orion.

## 4. FE validation approach (per build-TO)
- **Class-T parity:** for each platinum key, diff the re-emitted artifact against the current served artifact (schema + spot values) → if congruent, the consuming component is verified no-change by construction. (DS-side artifact diff + my render smoke.)
- **Class-X:** targeted component render test against the new field shape (the X1/X2/X4 panels specifically).
- Tooling: `comp-transform schema-check <Component>` (FE contract intact) + data-injected render smoke per partner (the COT/INF go-live pattern already established this session's predecessors).

## 5. Status
Pre-scope ready to fold into the FE build-TO set on contract-LOCK (DS co-sign + CTO arch-gate + CVO cert; N2 deferred-held). Headline for the build-TO author (COO): **the FE migration is mostly Class-T (render-parity validation, no code change); the real FE code work is X1 (lots), X2 (fees, gated on N1), X4 (optional fresh tile); X3 (client_count) is HELD on Andrew's N2 deferral.** 49F-first, COT-follows, INF-separate.
