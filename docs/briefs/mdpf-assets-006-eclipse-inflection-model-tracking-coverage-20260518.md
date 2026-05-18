# Brief -- MDPF_ASSETS.006: Eclipse/Inflection Model-Asset Tracking Coverage Map

**Project:** MDPF_ASSETS (Opal Aggregate AUA) -- WS-C (Inflection model AUA = Cohort 2a/2b)
**TO:** MDPF_ASSETS.006 (Eclipse/Inflection model-tracking coverage audit)
**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-18
**Issued to:** 2.0.0_SA_COO (RAVC2) -- feeds the WS-C Phase-2 build TO scoping
**Status:** Coverage verified against live S3 artifacts. Read-only investigation -- no pipeline producer modified.

> **Note on numbering:** "Q1"-"Q6" throughout this brief mean Andrew's six numbered
> *questions* from the MDPF_ASSETS.006 task order -- they are NOT calendar quarters.
> Question 4 (Q4) = "transactions vs model distribution," the deep-dive.

---

## TL;DR

1. **The 5/15 work (ADVI_ECLDAT Phases 1-4) covers model-asset *value* tracking well.** As of the
   live `2026-05-18` partition: 399 accounts / 214 households / 9 Opal models, account-grain,
   `overall:success`, refreshed daily by the gold chain. Q1/Q2/Q3/Q5/Q6 are **covered** -- the
   .003 feasibility brief is confirmed against live artifacts.

2. **Question 4 (Q4) -- transactions vs model distribution -- is the genuine gap, and it is
   bigger than "not built yet."** Inflection transactions ARE fully ingested (738,451 rows on the 398 model
   accounts, 6-year history, 398/398 coverage). But the transaction schema carries **no model
   dimension at all** -- the one model/sleeve-like column, `registrationSleeveStrategyName`, is
   **100% NULL across all 1.3M silver rows**. There is **no model-distribution / rebalance /
   model-reassignment event type**, and `blockId` / `tradeOrderId` / `orderId` are **100% NULL**,
   so a rebalance batch cannot even be grouped.

3. **The mass move into Opal models IS in the transaction data -- as unlabeled Buy/Sell
   Exchange rows.** 389 of 399 accounts were rebalanced into Opal models on **2026-05-13/-14/-15**;
   Buy/Sell Exchange transactions on the model accounts spike to ~25K each in 2026-05 vs a
   ~3-4K/month baseline. The event exists physically; it is not *marked* as a model event.

4. **Transaction-to-model attribution is feasible only FORWARD from ~2026-05-13, and only as a
   point-in-time `accountId -> model_id` join.** What breaks it: (a) no model-assignment history
   anywhere -- Eclipse carries only the *current* `model_id`; (b) Eclipse partitions exist only
   from 2026-05-15 (3 partitions), so history cannot be reconstructed from snapshots; (c) >99% of
   the model accounts' transaction history *predates* the Opal-model assignment entirely -- those
   accounts were not on Opal models before ~5/13, so retroactive attribution is not merely
   imprecise, it is **structurally meaningless**.

5. **Recommendation:** the transaction-model dimension is **its own workstream, not WS-C scope.**
   WS-C (model AUA) closes the already-known `holdings[]` gap and ships a point-in-time value
   rollup -- it does not need transactions. A transaction-model-attribution capability is a
   separate, forward-looking build that first needs a product decision (does Opal need
   transaction-level model attribution at all, and from what date) plus a new model-assignment
   history (SCD) dimension. Details in section 6.

---

## 1. Method

Read-only. Inspected: the 3 shipped Eclipse scripts (`bronze/pull_eclipse_portfolios.py`,
`silver/convert_eclipse_portfolios_to_silver.py`, `gold/INF_E_00.eclipse_model_portfolios.py`);
the 3 shipped INF transaction scripts (`manual_api/pull_inflection_transactions_rest.py`,
`silver/convert_transactions_to_silver.py`, `gold/INF_A_-1.materialize_txn_cache.py`); the
dispatch catalog (`orion-gold-dispatch.sh`); and the **live S3 partitions** `gold/eclipse/2026-05-18/`,
`silver/eclipse/2026-05-18/`, `silver/transactions/2026-05-18.parquet`. Probe scripts:
`.runtmp/mdpf006_probe.py`, `.runtmp/mdpf006_probe2.py`. No API call made -- every question was
answerable from artifacts. Builds on (does not redo) the MDPF_ASSETS.003 feasibility brief and the
2026-05-14 Eclipse feasibility brief.

---

## 2. Coverage table (AC1)

| Data element | Grain | Status | Storage location (S3 path / producing script / chain) |
|---|---|---|---|
| Model AUM / value | account / household / model / firm | **COVERED** | `gold/eclipse/{date}/model_portfolio_{accounts,households,summary}.parquet` -- `INF_E_00.eclipse_model_portfolios.py` -- `CHAIN_ECLIPSE` + post-sentinel block |
| Account -> model assignment | account | **COVERED** | `silver/eclipse/{date}/portfolios_simple.parquet` (`model_id`) -- `convert_eclipse_portfolios_to_silver.py` |
| Per-portfolio value detail (cash, managed, rebalance date) | portfolio | **COVERED** | `silver/eclipse/{date}/portfolios_full.parquet` (57 cols) |
| Household -> model membership | household | **COVERED** | `gold/eclipse/{date}/model_portfolio_households.parquet` (`model_count`, `models`) |
| Model catalog / metadata | model | **COVERED** | `silver/eclipse/{date}/models.parquet` (18 rows) |
| Model composition (Security-Set tree) | model | **PARTIAL** | `silver/eclipse/{date}/model_composition.parquet` -- stops at opaque Security Set; no ticker grain |
| Model composition (ticker-level `holdings[]`) | model x security | **GAP (known, .003)** | NOT ingested -- Orion `GET /Trading/Models/{id}.items[]`; WS-C build adds it |
| Person/client -> model membership | individual | **GAP** | Eclipse model data stops at `household_id` + account; no client/person id on any Eclipse row |
| Inflection transactions | transaction | **COVERED** | `bronze/transactions/{date}.parquet`, `silver/transactions/{date}.parquet` -- `pull_inflection_transactions_rest.py` / `convert_transactions_to_silver.py` -- `CHAIN_FULL`/`CHAIN_INCREMENTAL` |
| Transaction -> model tag/dimension | transaction | **GAP (new, this audit)** | Does not exist -- no model field in the 48-col transaction silver schema |
| Model-distribution / rebalance / reassignment EVENT | event | **GAP (new, this audit)** | Does not exist -- no event type; rebalances manifest only as untagged Buy/Sell Exchange |
| Model-assignment HISTORY (SCD: when an account joined/left a model) | account x time | **GAP (new, this audit)** | Does not exist -- Eclipse carries only the current `model_id`; partitions start 2026-05-15 |

---

## 3. Andrew's six questions, answered with evidence (AC2)

### Q1 -- What the 5/15 work covers + partition cadence

**COVERED.** ADVI_ECLDAT Phases 1-4 (shipped 2026-05-14/15) deliver a bronze->silver->gold Eclipse
pipeline. Live `gold/eclipse/2026-05-18/_meta/gold_complete.json`: **399 accounts, 214 households,
9 models**, `overall:success`, firm `total_value_eclipse` $93,603,064.81 / `orion_current_value`
$93,603,056.57 (8-cent agreement). Three gold artifacts at account / household / model+firm grain.

**Cadence -- corrected from the .003 "sparse" flag.** Live partitions exist for **2026-05-15, -17,
-18** (`{bronze,silver,gold}/eclipse/`). The 5/16 gap is a *whole-chain* gap -- `silver/transactions/`
also skips 5/16 -- not Eclipse-specific. The Eclipse trio (`INF_ECLIPSE_PULL` / `INF_ECLIPSE_SILVER` /
`INF_E_00`) runs on **every** full/incremental chain as a **best-effort, post-sentinel block**
(`orion-gold-dispatch.sh` lines 232-240; the trio is deliberately *not* inside `CHAIN_FULL` so a
new/untested Eclipse pull can never gate the portal publish -- Andrew product invariant 2026-05-15,
commit `415d8d121`). `gold/eclipse/_meta/dispatch_eclipse_status.json` confirms today's run:
`{overall:ok, INF_ECLIPSE_PULL:ok INF_ECLIPSE_SILVER:ok INF_E_00:ok, chain:full, chain_exit:0}`.

> Doc-drift note: `org/projects/ADVI_ECLDAT.json` `blocking` item (1) states the trio was
> "appended to CATALOG + CHAIN_FULL + CHAIN_INCREMENTAL." The live dispatch script has it in a
> separate `CHAIN_ECLIPSE` + a post-sentinel best-effort block, **not** in `CHAIN_FULL`/
> `CHAIN_INCREMENTAL` (decoupled by `415d8d121`). Minor -- worth a one-line ECLDAT.json correction.

### Q2 -- Household-level model membership

**COVERED at household + account grain; GAP at person grain.** `model_portfolio_households.parquet`
(214 rows) carries `household_id`, `account_count`, `model_count`, and `models` (a
semicolon-joined list -- e.g. household 226: "Opal Intermediate Growth; Opal Long Term"). So a
household *can* span multiple models, and that is captured. `model_portfolio_accounts.parquet`
gives the per-account `household_id` + `eclipse_model_id`.

What it does **not** reach: the individual person/client. No Eclipse row carries a client/person
id -- the finest identity is `household_id` plus a free-text `account_name` ("Ganje, David & Erika_48").
The transaction pipeline *does* carry `clientId` (296 distinct), so person-grain model membership
is derivable only by joining `account_id -> clientId` via `accounts_v2` / transactions -- it is not
in the Eclipse data itself. State precisely: **model membership is known per account and per
household; not per person.**

### Q3 -- Account-level granularity

**COVERED.** `model_portfolio_accounts.parquet`: 399 rows, 21 columns, one row per Opal-model
account. Each row carries `eclipse_account_id`, `account_number`, `eclipse_model_id` + `model_name`,
`total_value` / `managed_value` / `excluded_value` / `current_cash`, `household_id`,
`representative_name`, `custodian`, `orion_current_value`, `last_rebalanced_on`, `portfolio_status`.
**One account = one model: confirmed empirically** -- `groupby(eclipse_account_id).eclipse_model_id.nunique()`
yields 0 accounts spanning >1 model (398 distinct accounts; the 399th row is the 1 portfolio
unjoined to `accounts_v2`, per `gold_complete.json accounts_unjoined_to_accounts_v2:1`). An account
belongs to exactly one Opal model at a time.

### Q4 -- Transactions vs model distribution (THE DEEP-DIVE)

See section 4 -- this is the substance and is treated in full there.

### Q5 -- Classification

**Two distinct mechanisms; only one exists.**

- **Account/asset -> model classification: EXISTS.** An account is classified into a model by the
  Eclipse `portfolios_simple.model_id` assignment. The Opal-model subset is the hardcoded
  `OPAL_ECLIPSE_MODEL_IDS = [3,5,6,7,8,9,10,28,29]` (identical literal in all three Eclipse
  scripts -- bronze line 66, silver line 55, gold line 54). `INF_E_00` filters
  `simple.model_id.isin(OPAL_ECLIPSE_MODEL_IDS)` to get the 399 Opal accounts. Classification is
  a static membership test against a current `model_id` field -- no judgment, no derivation.
- **Transaction/flow -> model classification: DOES NOT EXIST.** No transaction is classified by
  model. `registrationSleeveStrategyName` (the only model/sleeve-named column in the schema) is
  100% NULL. There is no model-aware bucketing of transactions anywhere in bronze, silver, or the
  gold txn cache.

### Q6 -- Storage / pipeline location

**Everything is in the one `s3://opal-data-inf/` bucket -- the INF pipeline. Eclipse and
transactions are sibling prefixes in the same pipeline, not separate stores.**

| Artifact | S3 path | Grain | Producing script | Chain |
|---|---|---|---|---|
| Eclipse bronze | `bronze/eclipse/{date}/` (portfolios_simple/full, models, model_composition_{id}) | portfolio / model | `pull_eclipse_portfolios.py` | `CHAIN_ECLIPSE` + post-sentinel |
| Eclipse silver | `silver/eclipse/{date}/` (4 parquet) | portfolio / model | `convert_eclipse_portfolios_to_silver.py` | same |
| Eclipse gold | `gold/eclipse/{date}/` (3 parquet) | account / household / model+firm | `INF_E_00.eclipse_model_portfolios.py` | same |
| Transactions bronze | `bronze/transactions/{date}.parquet` | transaction | `pull_inflection_transactions_rest.py` | `CHAIN_FULL` / `CHAIN_INCREMENTAL` |
| Transactions silver | `silver/transactions/{date}.parquet` | transaction | `convert_transactions_to_silver.py` | same |
| Transactions gold cache | `/tmp` (ephemeral, in-chain) | transaction | `INF_A_-1.materialize_txn_cache.py` | A-layer |

Both live in the INF gold pipeline. They are **not joined anywhere today** -- there is no artifact
that carries both a transaction and its model.

---

## 4. Question 4 (Q4) deep-dive -- transactions vs model distribution (AC3)

### 4.1 Are Inflection transactions ingested? YES -- fully.

`pull_inflection_transactions_rest.py` pulls the Orion account-level endpoint
`GET /api/v1/Portfolio/Accounts/{accountId}/Transactions` for the entire Inflection account
universe (`accounts_v2` silver -- the custodian+rep-filtered Inflection book). Daily incremental
(7-day trailing window) + a Sunday full-history backstop. Live `silver/transactions/2026-05-18.parquet`:
**1,300,879 rows, 48 columns, 835 distinct `accountId`, transDate 2020-05-26..2026-05-15.**

**Coverage of the model accounts is complete: all 398 Eclipse Opal-model accounts appear in
`silver/transactions` -- 398/398, zero missing.** Those accounts carry **738,451 transactions**
spanning 2020-2026. The transaction pipeline covers Cohort 2a (Opal-model) and 2b (IWM/non-model)
alike, since `accounts_v2` is the full Inflection book.

### 4.2 Do transactions carry, or join to, a model dimension? NO.

The 48-column silver schema (31 bronze passthrough + 6 metadata + 11 Custom-Report join columns)
contains **no model field.** The only model/sleeve/strategy-named column,
`registrationSleeveStrategyName`, is **NULL on all 1,300,879 rows** -- it is a dead column from the
Orion REST payload. There is no `model_id`, no `modelAggId`, no sleeve tag.

A transaction *can* be joined to a model only indirectly: `txn.accountId -> Eclipse
portfolios_simple.model_id` (or `INF_E_00 model_portfolio_accounts.eclipse_model_id`). That join
is not performed by any current script.

### 4.3 Is there model-distribution / rebalance / reassignment event tracking? NO.

The 47-entry `transTypeId` universe (`TRANS_TYPE_DESC`) has **no rebalance, no model-assignment,
no model-distribution event type.** The mass move of Inflection assets into Opal models is in the
data -- but only as ordinary, untagged Buy/Sell Exchange rows:

- **Model-assignment timing (proxy: `last_rebalanced_on`):** 207 accounts rebalanced 2026-05-13,
  148 on 05-14, 34 on 05-15 -- **389 of 399 (97%) on 5/13-5/15/2026.** This is Andrew's "~109M
  transfer" into Opal models.
- **The rebalance in the transaction stream:** Buy Exchange (tid 10) + Sell Exchange (tid 53) on
  the model accounts spike to **25,161 / 25,158 in 2026-05** vs a ~2.4-3.8K/month baseline
  (Jan-Apr 2026). ~50K exchange transactions in May = the physical rebalance. Nothing labels them
  as a model event.
- **No batch grouping:** `blockId`, `tradeOrderId`, `orderId` are **100% NULL** on all 738,451
  model-account transactions. A rebalance batch cannot even be reconstructed by grouping -- the
  account-level REST endpoint does not populate trade-order/block identifiers.

### 4.4 How would transaction-to-model attribution work, and what breaks it?

**The only feasible method:** a point-in-time join `transaction.accountId -> model_id`, using the
Eclipse account->model assignment as of the transaction date.

**What breaks it -- three structural defeaters, in increasing severity:**

1. **No model-assignment history.** Eclipse `portfolios_simple` carries only the *current*
   `model_id`. There is no SCD / effective-dated record of when an account entered or left a
   model. A point-in-time join can only ever use *today's* assignment.
2. **Eclipse partitions start 2026-05-15.** Only 3 partitions exist (15/17/18). Even reconstructing
   an assignment history forward from daily snapshots has nothing before 5/15 to work with.
3. **>99% of the transaction history predates the model assignment.** The 398 accounts hold
   738K transactions back to 2020, but 97% were placed on Opal models only on 5/13-5/15/2026.
   Before that, those accounts were **not on Opal models at all** (they were on Inflection's own
   IWM models or unassigned). Attributing a 2023 transaction to "Opal Intermediate Growth" is not
   imprecise -- it is **factually wrong**: the account was not in that model in 2023.

**Consequence:** transaction-to-model attribution is meaningful **only forward from ~2026-05-13**,
and even forward it requires a new model-assignment-history dimension to stay correct as accounts
are reassigned between models. Retroactive (pre-5/13) attribution should be treated as
**out of scope / not possible**, not as a hard problem to solve.

---

## 5. Gap list (AC4)

| # | Gap | New or known | Severity |
|---|---|---|---|
| G1 | Ticker-level model composition (`holdings[]`) | **Known** (.003 brief section 3-4) | WS-C build scope -- the planned Orion `Trading/Models/{id}.items[]` pull |
| G2 | Transaction schema carries no model dimension | **New (this audit)** | Blocks any transaction-model reporting |
| G3 | No model-distribution / rebalance / reassignment event type | **New (this audit)** | Rebalances are invisible as events; only inferable from Buy/Sell Exchange volume |
| G4 | No model-assignment history (SCD) -- only current `model_id` | **New (this audit)** | Breaks point-in-time attribution the moment an account is reassigned |
| G5 | No batch/order grouping (`blockId`/`orderId`/`tradeOrderId` 100% NULL) | **New (this audit)** | A rebalance batch cannot be reconstructed from transactions |
| G6 | No person/client-grain model membership (Eclipse stops at household + account) | **New (this audit)** | Minor -- derivable via `account->clientId` join through `accounts_v2` |

G1 is the only gap WS-C (model AUA, point-in-time value) needs to close. G2-G5 are all on the
transaction-attribution side and are **not** required for the WS-C model-AUA rollup.

---

## 6. Recommendation -- WS-C scope vs own workstream (AC4)

**WS-C stays as scoped by MDPF_ASSETS.003: a point-in-time model-AUA rollup that closes G1
(`holdings[]`) only.** It does not need transactions, events, or assignment history. Do not widen
WS-C to absorb the transaction-model work -- that would couple a ready-to-build value rollup to an
unscoped, product-decision-gated capability.

**The transaction-model dimension should be its own workstream (proposed "WS-H -- Inflection
transaction-model attribution"), and it is gated on a product decision before any build:**

1. **Product question for Andrew/CTO first:** does Opal actually need transaction-level model
   attribution -- and if so, for what (model-level flows/NNA? rebalance cost analysis? per-model
   performance attribution?) and **from what date** (the honest answer is "forward from ~5/13/2026
   only"). The answer determines whether WS-H is worth building at all.
2. **If GO, the build is:** (a) a new **model-assignment-history (SCD-2) dimension** -- snapshot
   `portfolios_simple.model_id` per Eclipse partition into an effective-dated table so future
   reassignments are captured; (b) a gold join `transaction.accountId x transDate -> model_id`
   against that SCD dimension; (c) accept that pre-5/13/2026 transactions are unattributable and
   mark them so. None of this is hard once the SCD dimension exists -- but the SCD dimension does
   not exist and must be started now (every day without it is history permanently lost).
3. **One time-sensitive sub-recommendation regardless of the WS-H decision:** start **persisting
   the Eclipse model-assignment snapshot into an append-only history** immediately. Today only the
   latest `model_id` is knowable; once an account is reassigned, the prior assignment is gone
   forever. Even if WS-H is deferred, capturing the assignment history daily is cheap insurance
   and preserves the option. This is a small, standalone item -- recommend it be dispatched
   independent of the WS-H product decision.

---

## 7. Findings for COO / CTO

1. **WS-C is unchanged and unblocked** -- model AUA rollup + the G1 `holdings[]` pull, per .003.
   This audit confirms the .003 brief against live artifacts; no new WS-C blocker.
2. **Q4 answer: transactions are fully ingested but carry zero model signal**, and retroactive
   model attribution is structurally impossible (history predates the assignment). The
   transaction-model dimension is a **separate workstream (WS-H)**, product-decision-gated.
3. **Time-sensitive:** an Eclipse model-assignment-history (SCD) capture should start now,
   independent of the WS-H decision -- model reassignments are lost permanently otherwise. Small
   standalone TO.
4. **Doc-drift:** `org/projects/ADVI_ECLDAT.json` `blocking` (1) wrongly says the Eclipse trio is
   in `CHAIN_FULL`/`CHAIN_INCREMENTAL`; it is a decoupled post-sentinel block (`415d8d121`).
   One-line correction.
5. Person-grain model membership (G6) is a minor derivable gap -- note it for the WS-C build but
   it is not a blocker.

---

## 8. References

- TO: `MDPF_ASSETS.006.dsc-wsc-eclipse-inflection-model-tracking-coverage-audit.md`
- Prior: `docs/briefs/mdpf-eclipse-inflection-model-aua-feasibility-20260518.md` (.003, DS~B);
  `docs/briefs/data-scientist-eclipse-ingestion-feasibility-20260514.md` (DS~A);
  `org/projects/ADVI_ECLDAT.json`;
  `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-15/DS_A_session8_advi_ecldat_freshness_and_gold.md`
- Scripts: `data/orion/scripts/{bronze/pull_eclipse_portfolios,silver/convert_eclipse_portfolios_to_silver,gold/INF_E_00.eclipse_model_portfolios}.py`;
  `data/orion/manual_api/pull_inflection_transactions_rest.py`;
  `data/orion/scripts/{silver/convert_transactions_to_silver,gold/INF_A_-1.materialize_txn_cache}.py`;
  `data/orion/scripts/gold/orion-gold-dispatch.sh`
- Live artifacts: `s3://opal-data-inf/{bronze,silver,gold}/eclipse/2026-05-18/`,
  `s3://opal-data-inf/silver/transactions/2026-05-18.parquet`
- Probes: `.runtmp/mdpf006_probe.py`, `.runtmp/mdpf006_probe2.py`

---

**End of brief. -- 0.4.0_DS_ClientPlatform~C, 2026-05-18**
