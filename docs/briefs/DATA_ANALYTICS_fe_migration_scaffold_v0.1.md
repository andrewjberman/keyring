# DATA_ANALYTICS — FE-MIGRATION SCAFFOLD (Schwab-raw-native rebuild, FE build-lead) v0.1

**Author:** 0.4.0_DE_ClientPlatform (FE build-lead) | **Date:** 2026-06-25 | **archetype:** COORDINATE
**For:** 2.0.0_SA_COO (converts to the FE build-TO set on contract-LOCK) | **cc:** 0.4.0_DS (gold-name mapping align), 1.0.0_SA_CTO, 3.0.0_SA_CVO
**Builds on:** unified portal contract v1.0 + FE1 manifest (panel→platinum) + D→A lineage v1.0. **Status:** ready-to-convert; each FE-TO stub below becomes a real TO the instant the contract LOCKS.

> **Drive posture:** pre-staged downstream of DS's about-to-ship rebuild (universal silver contract v1 + non-reductive silver
> rework). Low re-work risk — the contract STRUCTURE is settled (49F single-`D_04`, COT agnostic-drops, INF separate-track);
> only the N-deps + CVO cert are pending. This scaffold scopes the FE leg so it converts to TOs with zero re-derivation.

> **PIVOT RESOLVED (DS, 2026-06-25):** PLATINUM keys + field shapes **HOLD STABLE**. The universal-silver-contract remaps
> raw→canonical at the silver/gold-INTERNAL tier ONLY (e.g. `fact_position` carries raw RPS `ticker_symbol`/`quantity`); the
> gold publisher RE-EMITS the SAME platinum contract by construction — the FE never sees silver-internal names. **→ LIGHT path
> CONFIRMED: render-parity validation + the 3 Class-X items. FE-TO-0 (re-point contingency) DROPS — not needed.** The only
> platinum changes are ADDITIVE/non-breaking and map to the 3 Class-X exactly: X1 richer lots/tax (`fact_lot_*` non-reductive),
> X2 fees restored (`fact_billing`/`dim_fee`), X4 native fresh-AUA tile. They ADD fields/keys; they don't break existing ones.

---

## 0. THE PIVOT QUESTION for DS (determines whether this is a validation sweep or a code migration)

The unified contract's whole premise: the rebuild **re-emits the SAME platinum keys/shapes** the panels already read (contract-anchored) → FE is **transparent** by construction. DS's "universal silver contract v1" remaps raw→canonical **at the gold/silver tier**. **The single thing that decides FE scope:**

> **Does the universal-silver-contract change any PLATINUM key NAME or field SHAPE (the FE boundary), or only silver/gold-INTERNAL names (FE-invisible)?**

- **If platinum boundary HELD STABLE** (the contract intent) → FE migration = a **render-parity VALIDATION sweep** + the 3 Class-X code items below. No mass re-pointing.
- **If platinum keys/shapes SHIFT** → each shifted key adds an endpoint-layer re-point (`advisor-intelligence.ts`) + consumer re-test. **Scoped as FE-TO-0 contingency.**

**ACTION (cc DS):** confirm the platinum boundary is held stable. The endpoint layer (`src/api/endpoints/advisor-intelligence.ts`) is the FE's only binding to platinum keys — if those keys/shapes don't move, the panels don't move.

---

## 1. FE-TO scaffold (49F-first per arch-gate G3; each row = a future build-TO)

| FE-TO | Scope | Components / file | Platinum keys | Change-class | Re-test |
|---|---|---|---|---|---|
| ~~FE-TO-0~~ (DROPPED) | ~~Endpoint re-point if platinum shifts~~ — **DS confirmed platinum stable; not needed** | — | — | — | — |
| **FE-TO-1** | 49F render-parity VALIDATION sweep (the bulk; Class-T) | all 49F panels (PartnerAnalytics, Distribution, Advisors, Books, Profile, Cohort-A) | all 49F platinum | **T** | render-smoke each panel vs re-emitted platinum + DS value-diff. **N3: `total_aua` parity = FULL-BOOK $1.83B, NOT Schwab-only $1.63B** (see N3 below) |
| **FE-TO-2** | 49F LOTS / TAX panels (the B_01-FIFO excise risk) | `TaxCostBasisPanel`, `AdvisorBookView` L3 client/account drill | `clients/{hh}/*`, `accounts/{id}/summary` | **X1** | **VALUE-parity** (CTO G2 target): verify tax/lot fields tie post-B_02-direct (FIFO retired) |
| **FE-TO-3** | 49F FEE panels (N1, retain-bd-fees) | `FeeEfficiencyPanel`, `FeeSummaryPanel`, AdvisorPublicProfile fee, ClientsTab income/fees | `fee_efficiency.json`, advisor/client `fee_summary` | **X2** (likely T — bd-fees retained) | verify fee fields unchanged (A_02/C_08 retained per CTO N1) |
| **FE-TO-4** | header_metrics_fresh tile (optional new capability) | PartnerAnalytics / ClientsTab headline (`getHeaderMetricsFresh` already coded) | `header_metrics_fresh.json` | **X4** (net-new) | only if Andrew wants the 49F/COT fresh tile + DS emits it |
| **FE-TO-5** | COT render-parity sweep (AFTER 49F proves + COTETL/BDAPIMIG) | COT consumed panels (PartnerAnalytics geo/aua/nna, Distribution-geo) | COT essential keys (`D_00/D_00b/D_01/D_04`) | **T** | inherits FE-TO-1 method; smaller surface; 4a-gate (757f4d99) already hardens COT |
| *(no FE-TO)* | Inflection | — | — | **separate track** | INF is Orion, not Schwab-raw target — no migration under this rebuild |
| *(HELD)* | client_count / household panels | PartnerAnalytics/ClientsTab/dashboard client_count, `client_directory`, L3 drill | household-dependent | **X3 — PENDING-N2** | partial-lock; do NOT migrate until Andrew rules N2 |

## 1b. N3 — AUA-COMPLETENESS dependency (DS-raised; a value-parity finding, NOT an FE-code issue)

DS ground-truth: the Schwab-raw **$1.63B is only the SCHWAB PORTION** of 49F; **~$200M is non-Schwab (Fidelity) 49F accounts that BD currently aggregates**. The served `header_metrics.total_aua` is the COMPLETE book (~$1.83B). So:

- **The platinum key/shape is stable (no FE change)** — but the served `total_aua` VALUE depends on the full book, not just Schwab.
- **A Schwab-only interim rebuild would FAIL `total_aua` value-parity by ~$200M** ($1.63B vs $1.83B). This is exactly the "no excise silently drops a served value" rule (CTO G2) applied to the firm headline number.
- **N3 is a RETAINED-SOURCE dependency, sibling to N1 fees:** the rebuild must keep the non-Schwab (Fidelity) slice supplied — via BD-aggregate (interim) or a Fidelity-raw feed (durable) — or the firm AUA reads low. Schwab-raw-direct is necessary-but-not-sufficient for the complete `total_aua`.
- **FE impact: NONE on code** (key/shape stable); **the impact is on the value-parity CERT** — CVO's `total_aua` parity check must target the FULL-BOOK number, and the rebuild build-TO must explicitly retain/source the Fidelity slice. Flagged to CTO/COO as a G2 parity input.

## 2. Migration sequence (49F-first)
1. **FE-TO-0** resolve the pivot with DS (gate everything else's classification).
2. **Wave 49F:** FE-TO-1 (parity sweep) ∥ FE-TO-2 (lots/tax value-parity, the real work) ∥ FE-TO-3 (fee verify). FE-TO-4 only on Andrew's fresh-tile call.
3. **Wave COT:** FE-TO-5, after 49F proves the pattern + BD-native lots stable (COTETL/BDAPIMIG).
4. **INF:** untouched (separate track).
5. **X3 household panels:** unblock only on Andrew's N2 ruling (partial-lock until then).

## 3. Per-panel re-test method (the FE validation contract)
For each panel: (a) `comp-transform schema-check <Component>` — FE type-contract intact; (b) data-injected render smoke per partner (the COT/INF go-live pattern) — pixels render; (c) **value-parity diff** on the FE-TO-2 set specifically (CTO G2: served field VALUE reproduced, not just present). Class-T panels pass on (a)+(b); Class-X panels require (c).

## 4. Status
Scaffold ready to convert to FE build-TOs on contract-LOCK. Re-work risk LOW (structure settled). The one open input is the FE-TO-0 pivot (DS platinum-boundary stability) — everything else is pre-classified. On LOCK: COO authors the build-TO set from this scaffold; I execute the FE leg, 49F-first.
