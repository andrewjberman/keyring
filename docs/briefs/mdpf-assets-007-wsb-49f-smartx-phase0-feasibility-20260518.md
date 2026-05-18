# MDPF_ASSETS.007 WS-B — 49F/SmartX Model-AUA Feeder: Phase-0 Feasibility

**Finding brief — Phase 0 (the gating feasibility assessment)**
**TO:** MDPF_ASSETS.007 (`dsa-wsb-49f-smartx-model-aua-feeder`) — WS-B, Cohort 1a
**Author:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**Contract:** `docs/architecture/MDPF_ASSETS_WSA_CONTRACT.md` (RATIFIED)

---

## Verdict — GO

**Per-account 49F model membership IS obtainable from SmartX.** The ratified contract's account-grain `model_aua_positions` is feasible — no STOP, no contract-downgrade question. WS-B proceeds to Phase 1.

The SmartX endpoint **`enterprises/allocations?modelid={modelId}`** returns a per-allocation roster — one row per client allocation to a model — carrying that allocation's market `value`. Filtered to `status=open` it reconciles to the validation reference within ~1%. PRD named-gap-2 ("49F model_aua is a SmartX scalar, not account-keyed") is closed: the scalar was just the wrong endpoint; the account-grain data exists.

---

## Phase-0 question (a) — does a per-account model-membership source exist? YES

Empirical probe 2026-05-18 (`.runtmp/mdpf007/wsb_phase0_probe.py`, read-only, ROPC JWT, Secrets Manager creds), two models:

| Model | `enterprises/allocations` rows | status=open Σ value | Validation ref (2026-05-15) | Delta |
|-------|-------------------------------:|--------------------:|----------------------------:|------:|
| Opal Ultra Short-Term (UST) | 384 (open 169 / close 214 / workingClose 1) | $52,253,628 | $52.70M | −0.85% |
| Opal Intermediate-Term (INT) | 2,142 (open 1,561 / close 569 / workingClose 12) | $282,957,029 | $283.22M | −0.09% |

The residual delta is the 3-day date offset (ref is 2026-05-15, probe 2026-05-18). **`enterprises/allocations` is account/allocation grain and reconciles** — this is the `model_aua_positions` source.

Per-row schema (probe-confirmed):
```
{ allocationId:str, status:str ("open"|"close"|"workingClose"),
  advisor:{id,name,crd}, model:{id,name}, value:float, openedDate:{timestamp,friendly} }
```

Maps onto the contract `model_aua_positions` (account grain) as:

| Contract column | SmartX source |
|-----------------|---------------|
| `firm_id` | constant `49financial` (every allocation's advisor = "49 Financial Group", crd 304569) |
| `model_key` | from `model.id` via the §2 registry |
| `account_id` | `allocationId` (the stable per-allocation key) |
| `model_value` | `value` — account-decomposable market value (contract ruling ii satisfied) |
| `as_of_date` | the daily pull date (SmartX `/allocations` is a current snapshot) |
| `household_id` | not exposed by SmartX — null (contract permits null) |
| `custodian` | not on the allocation row — 49F SmartX book is Schwab-custodied; emit `Schwab` as the known constant or null + document |
| `source_pipeline` | `smartx` |

### Critical Phase-0 findings for Phase 1

1. **Filter `status=open`.** `close` + `workingClose` allocations carry residual value that inflates the model total ~10% (UST: all-status $57.9M vs open-only $52.3M). `model_aua_positions` is `status=open` only. close/workingClose are excluded — they are wound-down allocations, not live model AUA.
2. **`models/{id}/statistics.value` is NOT per-model — do not use it.** It returned the identical value ($1,333,098,676.39) for UST *and* INT — it is an enterprise/aggregate figure, not the model total. The model total is `Σ (status=open) allocations.value`. (`enterprises/aum?modelid=` `closingEquity` is the alternative, but Σ open allocations is account-decomposable per ruling ii — use it.)
3. **`account_id` granularity.** `allocationId` is per-(account, model). A 49F client in two models = two allocation rows = two `model_aua_positions` rows — exactly the `(firm_id, model_key, account_id)` grain the contract wants. No deeper account id is exposed; `allocationId` is the canonical key.

## Phase-0 question — `model_composition` source

`reportedmodels/{reportedModelId}/holdings` (chain `models/{modelId}.reportedModelId`) returns the per-ticker composition:
```
{ symbol:{ticker,assetType,companyName,...}, quantity, price, marketValue, percentOfPortfolio }
```
- UST: 12 holdings, `percentOfPortfolio` sums to **0.978**. INT: 16 holdings, sums to **0.985**.
- **The weights do NOT sum to 1.0** — there is a ~1.5–2.2% implicit cash residual not returned as a holding row. **Phase-1 decision:** emit a synthetic `CUSTODIAL_CASH` composition row for the `1 − Σ` residual so `target_weight` sums to 1.0 per `model_key` (the contract §6 already names `CUSTODIAL_CASH` as the cash sentinel). Documented, not silently dropped.
- **Opal ETFs appear as line items** — INT holds **DIVZ, IDVZ, PFDE, PFOE** all four as explicit tickers; UST holds none. `is_opal_etf` flagging is a direct ticker match — the §3.3 no-double-count attribution is clean for the 49F side.

## Phase-0 question (b) — SmartX feeder state

- **SXPL_RESTIN.002 (the REST pull flow, AE 0.5.0) is dispatched-GO but NOT shipped** — no scheduled job, no production pull, no bronze landing in S3 (per `SXPL_RESTIN.json` + the TO-1 matrix brief). So there is **no SXPL_RESTIN pull output for WS-B to consume today.**
- The SmartX REST endpoints themselves are **proven and live** — TO-1 probed all 13 × 7 models 2026-05-15; this brief re-confirmed `enterprises/allocations` + `holdings` + `models/{id}` working 2026-05-18.
- The EC2 browser-exporter remains the canonical 49F source (decommission deferred indefinitely) and covers only 5 of the 7 models — it is **not** account-grain (per-model exports), so it cannot source `model_aua_positions` anyway.

**Scoping decision surfaced to COO:** the TO context says "WS-B consumes SXPL_RESTIN's pull output," but that output does not exist yet. WS-B Phase 1 will be a **self-contained feeder** — it mints the ROPC JWT and pulls `enterprises/allocations` + `holdings` directly (the proven endpoints), transforms to the convergent schema, writes the two artifacts. This gets Cohort 1a live now rather than blocking on SXPL_RESTIN.002. The pull layer is a clean seam: when SXPL_RESTIN.002's bronze lands, WS-B's read layer swaps to it. WS-B writes ONLY the `opal-data-mdpf` feeder prefix — never the canonical exporter path (soak-safety hold respected).

## Phase-0 question (c) — owned-paths / script home

**Resolved — no blocker.** The `data/smartx/` POD3 owned-paths registration is irrelevant to WS-B: WS-B is an MDPF feeder and lives in the **MDPF home `data/mdpf/scripts/`**, not `data/smartx/`. The WS-A commits (`7c09fccf1`) already landed under `data/mdpf/` cleanly — the lane is open to this DS lane. WS-B feeder script: `data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py`.

## Model registry alignment (contract §2 / ruling vii)

The 5 core 49F models map cleanly (the `49Fi…` shortName prefix marks them). The 2 extras need the registry's `smartx_name` confirmed:

| SmartX modelId | SmartX name | shortName | → `model_key` | Note |
|---|---|---|---|---|
| 0f76a5a0 | Opal Short-Term | 49FiLiSh000 | `opal_short_term` | clean |
| 729210dd | Opal Intermediate-Term | 49FiLiIn000 | `opal_intermediate` | clean |
| 74c119db | Opal Conservative Growth | 49FiLiCoGr000 | `opal_long_term_conservative` | name is "Conservative Growth", exporter tag LTC |
| 69cc5e3b | Opal Long-Term Aggressive | 49FiLiLoAg000 | `opal_long_term_aggressive` | clean |
| c000fe6a | Opal Ultra Short-Term Income | OpaGlUlShIn000 | `opal_ultra_short_term` | clean |
| 48af6559 | Opal Dividend Income | TitlDivGro000 | `opal_div_sma` | name "Dividend Income" vs registry "Dividend SMA" — **confirm** |
| 843d875b | Pathfinder Focused Opportunities | OpGEGTR000 | `opal_growth_sma` | shortName `OpGEGTR` = Opal Equity Growth, but display name "Pathfinder Focused Opportunities" — **mismatch, confirm with COO/CTO** |

Phase 1 updates `mdpf_model_registry.json` with the SmartX `modelId`s + confirmed names; the 843d875b name/shortName conflict is flagged to COO+CTO (it overlaps the SXPL_RESTIN TO-1 "2 unidentified models / product call" item).

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io` on a SmartX pipeline script (TO mandate phase 1) | N/A — no existing SmartX gold/silver script is consumed; WS-B is a new feeder reading the SmartX REST API directly. No IAM gap (creds are an existing Secrets Manager secret `smartx/credentials/*`; no new AWS API surface). |
| `comp-blast` (TO mandate phase 3) | Runs post-Phase-1-commit. Expected: blast radius = the new `opal-data-mdpf` feeder artifacts only; zero overlap with the SmartX EC2-exporter canonical path. |

## Recommendation

Proceed to Phase 1. WS-B feeder = self-contained `data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py`: pull `enterprises/allocations` (status=open) + `holdings` for the 7 models, emit `model_aua_positions` + `model_composition` (firm_id=49financial) to the `opal-data-mdpf` feeder prefix. Two items for COO: (1) the WS-B-pulls-directly scoping decision above; (2) the `843d875b` model-name conflict. Neither blocks Phase 1.
