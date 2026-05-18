# Brief -- Inflection Model-Exposure: completing the Eclipse channel to platinum

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-18
**Issued to:** 2.0.0_SA_COO -- design spec for the build TO (CC CTO, DE 0.4)
**Origin:** Andrew-direct 2026-05-18 -- "work model ID into the inflection pipeline so we have
the option of easily porting in model-exposure in the portal at the client/account level ... this
join between orion and eclipse data should be done every day and measured in some
bronze/silver/gold/platinum channel of the greater inflection pipeline."
**Status:** Design only. No code written. Feeds the build TO.

---

## TL;DR

1. **The orion<->eclipse account/model join Andrew wants already runs daily through
   bronze->silver->gold** in the inf pipeline -- the ADVI_ECLDAT `eclipse` domain. The gap is the
   **platinum (portal-facing) tier**, which ADVI_ECLDAT Phase 5 deferred on 2026-05-15.
2. **The build is three items:** (1) a platinum publisher for the eclipse channel; (2) thread
   `model_id` onto the main account/client dimensions (`INF_A_00`/`INF_A_04`) so model-exposure
   rides the *existing* portal client/account pages; (3) widen `INF_E_00` from Opal-only (399
   accounts) to the full Inflection book so non-Opal accounts are tagged.
3. **Phase 1 = current-state model membership + value.** No model-assignment history (SCD) is
   needed for a live portal view. Phase 2 (ticker-level look-through) is additive and gated on
   WS-C's `holdings[]` pull -- no Phase-1 rework.

---

## 1. What exists today (verified against live S3, 2026-05-18)

The Eclipse model channel is already a daily b/s/g channel of the inf pipeline:

| Tier | Path | Producer | Content |
|---|---|---|---|
| bronze | `s3://opal-data-inf/bronze/eclipse/{date}/` | `pull_eclipse_portfolios.py` | Raw Eclipse pull -- portfolios, models, composition |
| silver | `s3://opal-data-inf/silver/eclipse/{date}/` | `convert_eclipse_portfolios_to_silver.py` | `portfolios_simple` (835 rows; `account_id -> model_id`), `portfolios_full`, `models`, `model_composition` |
| gold | `s3://opal-data-inf/gold/eclipse/{date}/` | `INF_E_00.eclipse_model_portfolios.py` | `model_portfolio_accounts` (399, account grain -- **`eclipse_model_id` joined next to `orion_current_value`**), `model_portfolio_households` (214), `model_portfolio_summary` (10) |
| **platinum** | -- | **none** | **MISSING -- this is the build** |

`INF_E_00`'s `model_portfolio_accounts.parquet` **is** the daily account-grain orion<->eclipse
join Andrew is describing -- it joins Eclipse silver to `silver/api_dims/accounts_v2/` and emits
the Eclipse model assignment alongside the Orion account value. It refreshed today
(`gold/eclipse/2026-05-18/`, `overall:success`, 399 accounts).

The channel runs daily as the dispatch `CHAIN_ECLIPSE` trio, also fired as a best-effort
post-sentinel block at the end of every full/incremental chain (so a new/untested Eclipse pull
can never gate the portal publish -- Andrew product invariant 2026-05-15, `415d8d121`).

---

## 2. The build -- three items

### Item 1 -- Platinum publisher (the missing tier)

A new publisher script in the eclipse `E` family (proposed `INF_E_01.model_exposure_platinum.py`)
that reads `gold/eclipse/{date}/model_portfolio_{accounts,households,summary}.parquet` and emits
portal-facing JSON. Proposed artifacts (final shape settled with DE 0.4 against the portal spec):

| Artifact | Grain | Content (Phase 1) |
|---|---|---|
| `platinum/firm/model_exposure_summary.json` | model | per model: `model_id`, `model_name`, `model_namespace`, `account_count`, `household_count`, `total_value`; firm rollup |
| `platinum/model_exposure/accounts.json` | account | per account: `account_id`, `account_number`, `household_id`, `eclipse_model_id`, `model_name`, `model_namespace`, `total_value`, `current_cash`, `as_of` |
| `platinum/model_exposure/households.json` | household | per household: model set + per-model value |

Runs as part of / immediately after the eclipse post-sentinel block. Every artifact carries an
explicit `as_of` date -- the channel is best-effort, so the portal must render staleness.

### Item 2 -- Thread `model_id` onto the main account/client dimensions

So model-exposure shows on the **existing** portal client/account pages, not only as a separate
fetch:

- `INF_A_00.accounts_dimension.py` -- left-join to add `eclipse_model_id` / `model_name` /
  `model_namespace` at account grain.
- `INF_A_04.client_dimension.py` -- roll the account-grain model assignment up to
  client/household (a client with accounts in two models shows both).
- The D-layer client/account publishers (`INF_D_02` client detail, `INF_D_04` client summary,
  `INF_D_02c` client directory) then carry the fields into their platinum JSON -- the portal
  field becomes wire-ready with no separate plumbing.

**Ordering nuance (must be in the TO `cross_domain_coordination`):** `INF_A_00` runs early in the
chain; the eclipse trio runs at the very end (post-sentinel). So `INF_A_00` must read the
**latest available** eclipse partition -- i.e. yesterday's `gold/eclipse/{date}/` (or
`silver/eclipse/`). A benign 1-day lag; model assignments do not change intraday. Do **not** move
the eclipse pull earlier -- that would make it chain-gating and break the 2026-05-15 invariant.

### Item 3 -- Widen `INF_E_00` to the full Inflection book

`INF_E_00` currently filters `simple.model_id.isin(OPAL_ECLIPSE_MODEL_IDS)` (line 161) -> 399
Opal-model accounts only. Widen to all 835 portfolios and add a **`model_namespace`** column
(`opal` / `iwm` / `unassigned`) so the portal can correctly show "in no Opal model" instead of a
blank. The silver `portfolios_simple` already carries all 835 -- small filter change.

**Care-point:** widening changes the row count of the existing `model_portfolio_*` artifacts and
the firm headline. Preserve the Opal-scoped figures -- recommend `model_portfolio_summary` keep a
clearly-flagged Opal-only subtotal alongside the full-book firm row, and the account artifact
carry `model_namespace` + an `is_opal_model` flag so existing-style consumers can filter. Do not
silently change the $93.6M Opal headline.

---

## 3. Phase boundary

| | Phase 1 (this TO) | Phase 2 (later) |
|---|---|---|
| Shows | Which model an account/client is in + dollar value | + securities/ETFs held *through* the model (PFDE/PFOE exposure) |
| Needs | Current `model_id` only -- no SCD/history | WS-C `holdings[]` (Orion `Trading/Models/{id}.items[]` pull) |
| Portal contract | `model` node per account/client | additive child `holdings[]` array under the same node -- no Phase-1 rework |

Phase 1 is current-state. A model-assignment **history** (SCD) is **not** needed for a live
portal view -- it matters only for *historical/transaction* attribution (the separate WS-H idea
from MDPF_ASSETS.006). Keep that decoupled; the standalone daily SCD-capture recommendation from
the .006 brief still stands independently and is cheap insurance.

---

## 4. Cross-domain coordination (for the TO)

- `INF_A_00`, `INF_A_04`, `INF_D_02/04/02c` are main-chain scripts -- **sequence the edits after
  INF chain #3** (the in-flight INFGRO.007/.009/BIWNDW.002 co-land).
- `INF_E_00` + the new `INF_E_01` platinum publisher are the ECLDAT eclipse `E` domain --
  single-owner (DS~C); no concurrent-edit hazard.
- The portal FE wire (rendering the `model` field) is DE 0.4 -- this was ADVI_ECLDAT Phase 5's
  original FE scope. The TO's job is to make the data wire-ready; the FE work is a separate DE TO.

## 5. Open scope calls for COO/CTO

1. **Project code:** recommend this be **ADVI_ECLDAT Phase 5** -- the platinum tier was always
   that project's deferred tail. Alternative: an MDPF_ASSETS workstream. COO call.
2. **Full-book widening (Item 3):** recommended (Andrew was told; can veto). Confirms the portal
   can show non-Opal accounts.
3. **Platinum artifact shape:** the section-2 shapes are a proposal -- final keys settled with
   DE 0.4 against the portal client/account page spec.

## 6. References

- MDPF_ASSETS.006 coverage brief: `docs/briefs/mdpf-assets-006-eclipse-inflection-model-tracking-coverage-20260518.md`
- WS-C feasibility: `docs/briefs/mdpf-eclipse-inflection-model-aua-feasibility-20260518.md`
- ADVI_ECLDAT: `org/projects/ADVI_ECLDAT.json`; ECLDAT.004 log
  `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-15/DS_A_session8_advi_ecldat_freshness_and_gold.md`
- Scripts: `data/orion/scripts/{bronze/pull_eclipse_portfolios,silver/convert_eclipse_portfolios_to_silver,gold/INF_E_00.eclipse_model_portfolios}.py`;
  `data/orion/scripts/gold/{INF_A_00.accounts_dimension,INF_A_04.client_dimension}.py`

---

**End of brief. -- 0.4.0_DS_ClientPlatform~C, 2026-05-18**
