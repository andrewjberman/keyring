# NFRA_GCONTR — SEV1 value-check results (3 rows), grounded against served artifacts

**Author (signature / lane):** `3.0.0_SA_CVO`
**Executed by (provenance, transparent):** `0.0.0_AB_MSTR`, under Andrew-direct instruction 2026-07-17 (*"value check it now"* + *"record it, write a brief about it, signing it as 3.0.0_SA_CVO"*), standing in for the CVO-owned `value_check` (PRD §9) because a fresh CVO instantiation was hanging. Recorded under the CVO signature per Andrew's instruction; the value_check is CVO's lane and this artifact belongs in it. No ratification is asserted here — the SEV1 sign is Andrew's and is separate.
**Date:** 2026-07-17 · **Contract set:** the 3 SEV1 rows (benchmark, headline, advisor_intelligence) · **PRD:** `docs/architecture/NFRA_GCONTR_PRD.md`

---

## ‼ DEPLOY HOLD — DO NOT LOAD ANY ROW UNTIL MDPF IS TOTALLY DONE ‼

**Andrew-direct 2026-07-17:** *"i dont want to deploy this until MDPF is totally done as we may need to adjust things."*

No `--load-contracts` on any GCONTR row until MDPF (the `model_portfolios.headline` = MDPF aggregate-AUA surface, and the broader OPAL_CONSOLIDATION MDPF work) is complete. The `headline` contract encodes MDPF convergence semantics; adjusting MDPF may change what the contract should assert. This brief RECORDS the value-check; it does not authorize a load. The sign-off state (Andrew signed headline + advisor_intelligence "SIGN BOTH" at f5cee1a8a ~1655Z) stands as sovereign record, but the LOAD is held.

---

## What was run, and against what

The CVO-owned `value_check` (PRD §3.3 / §9): run each row's `period_defs` / value assertion against the **served** artifact, independent of the writer. Grounded on live served state at 2026-07-17 ~19–20Z, exercised (not self-report). The live `globgrph.graph_contracts` table last-wrote **745h ago (2026-06-16)** — so headline + advisor_intelligence were **never loaded** (never signed until today); benchmark + peers + aum are the 3 live rows.

---

## ① `benchmark-model-portfolios` — VALUE-LIMB CLEAN; contract TEXT carries a known drift

**Exercised:** ran `org/tier1_exec/3.0.0_SA_CVO/contracts/value_check_benchmark_period_defs.py` (exit 0):
- SOURCE `benchmarks/data_20260717_v1.pkl` (via `LATEST.json`, producer-parity); served_as_of `2026-07-16` (T-1, healthy).
- **250/250 cells reproduce from the source PKL via the canonical transform; VIOLATIONS 0.**
- Detection power at this as-of: **1M `|Δ|=0.7200` and 1Q `|Δ|=7.8100` (tol 0.01) → DISCRIMINATING** (not a vacuous pass — the check has power today).

**FINDING (contract-text drift, forward-risk only):** `period_defs` declares `"1M": trailing-1-calendar-month` / `"1Q": trailing-3-calendar-months`. This **contradicts the methodology-of-record** — Andrew's ruling `631d8d0d9` (BMKAUD WS-3, 2026-06-01): trailing-**30 / 91 CALENDAR DAYS** (`lambda_function.py:445-455`, `:475-483`). The **served data is correct** (uses the 30/91d canonical transform); only the **contract text is wrong**. The live YAML carries a `!!! DRIFT — DO NOT LOAD THESE TWO LINES AS-IS` block (CVO `ec33fe59d`). This was **NOT** in the 1655Z "SIGN BOTH" (that was headline + advisor_intelligence). **Open decision for Andrew:** re-sign with the corrected text, or load-with-drift (advisory-WARN v1).

## ② `headline-model-portfolios` (MDPF aggregate AUA) — VALUE-CHECK CLEAN

**Exercised:** read served `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json`.
- value_check = *"convergence-gate honored: served as_of ≤ min(feeder as_of); no single-feeder advance past the gate."*
- **served `as_of_last = 2026-07-17`; `source_vintage_last.status = "current"`; `age_hours_at_generation = 18.7` (< 26h threshold); `lag_vs_as_of_days = 0`.** All vintage-bearing feeders (`model_aua_positions`, `non_model_aua` — 49financial + inflection) at **2026-07-17**. `etf_net_assets` (07-15/16) + `partner_held_etf` (RPS ~3d roll) are excluded from `overall` by design. **No single feeder advanced past the gate. CLEAN.**
- Caveat consistent with the hold: this row IS the MDPF surface; if MDPF changes, re-check.

## ③ `advisor-nna-canonical` (advisor_intelligence) — TWO FINDINGS

value_check = *"NNA canonical present + data_as_of fresh per firm; no silent bd-fallback."* Firm scope `{bd, inf, cot}`. bd read now permitted (07-14 sovereign-block lift). **Exercised** head+get on all three:

| firm | present | data_as_of | records | verdict |
|---|---|---|---|---|
| `inf` | YES | **2026-07-16** (T-1) | 5 | **CLEAN** |
| `bd` | YES (3.6MB, gzip-wrapped `.json`) | **2026-07-13** | 167 | **STALE — known cause** |
| `cot` | **NO** — artifact absent | — | — | **SCOPE FINDING** |

- **bd frozen at 07-13:** this is the **known bd-exporter allocations-outage freeze** (the 07-13→16 login-fail P1 Andrew deprecated). bd gold is gated on silver/allocations, so advisor_nna_canonical froze with the chain. Not a new defect — the same root cause, and the consolidation's freshness-gate re-key is the fix. The "fresh per firm" limb currently **fails for bd** until that lands.
- **cot artifact ABSENT:** `s3://opal-data-cot/platinum/firm/` serves 8 firm artifacts (leaderboard, dashboard, partner_analytics_annual, …) but **no `advisor_nna_canonical.json`.** The contract declares `{bd,inf,cot}`; cot's served reality does not match. **Open question:** is cot in-scope for advisor-NNA at all, or should the contract scope be `{bd,inf}` (or cot's NNA served at a different key)? A CVO/domain call, surfaced not adjudicated.

## Empty-hash / placeholder-invariant verify

- Live `graph_contracts` last-write 745h ago (06-16) ⇒ headline + advisor_intelligence never loaded (correct — unsigned until today). The 3 loaded rows carry real 16-char hashes (COO in-VPC `contract_engine` read, 150336Z). The YAML `ratified_at` fields are **all** stale `PENDING-*` proxies **by design** (the loader stamps the live table, never writes back). **No empty-hash-in-a-real-slot violation.** Ground ratification on the table, never the YAML (PRD Item-4).

## Disposition summary (for the eventual post-MDPF load)

| Row | value-check | on load-day (post-MDPF) |
|---|---|---|
| `headline` | CLEAN | loadable — re-check convergence at that day's as_of first |
| `advisor_intelligence` | cot-absent + bd-frozen | resolve cot scope; confirm bd freshness restored by the consolidation gate re-key; advisory-WARN v1 won't hard-block |
| `benchmark` | served CLEAN; text drift | Andrew re-sign (corrected text) or load-with-drift |

## Grounding (Rule 22a — desired / applied / exercised)

- **desired:** the TO-3 contract rows (`NFRA_GCONTR_TO3_contract_rows_20260626.md`) + the `!!! DRIFT` correction (`NFRA_GCONTR_SEV1_amendment_package_20260709.md`); §9 assigns `value_check` = CVO.
- **applied:** `comp-kuzu` provenance header — `graph_contracts` last-write 745.4h ago (= 06-16), confirming 2 rows unloaded; live table = 3/5 loaded (COO in-VPC read reference 150336Z).
- **exercised:** `value_check_benchmark_period_defs.py` (exit 0, 250/250, 1M/1Q discriminating); live GET on `aggregate_aua_timeseries.json` (as_of 07-17, convergence current); live head+GET on `advisor_nna_canonical.json` × {bd (07-13, 167, gzip-decoded), inf (07-16, 5)}; `s3 ls` on `opal-data-cot/platinum/firm/` (advisor_nna_canonical.json absent). Read-only throughout; no writes, no ad-hoc runs, no loads.

— signed `3.0.0_SA_CVO` (executed `0.0.0_AB_MSTR`, Andrew-direct 2026-07-17)
