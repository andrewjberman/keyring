# PRD — Model Portfolios "unfunded holdings excluded" footer: lineage + Inflection grain-mismatch fix

**Author:** 1.0.0_SA_CTO · **Trigger:** Andrew-direct 2026-06-01 (footer counts under the Account Distribution bell curve in Model Portfolios → Portfolio Analytics; Inflection's number is "not calculated with the correct intent") · **Decompose:** 2.0.0_SA_COO → TOs · **Owners:** DS (grain/producer) + RD (FE calc); DE/CVO verify.
**Status:** DRAFT for COO decomposition.

## 1. The symptom
Footer beneath the Account Distribution bell curve (Portfolio Analytics panel), per firm:
- **Global:** "Excludes **14** newly opened holdings with $0 balance (unfunded). … included in time series metrics once funded."
- **49 Financial:** "Excludes **201** …"
- **Inflection:** "Excludes **6639** …"  ← nonsensical vs 14 / 201; not the correct intent.

## 2. LINEAGE — how each number is computed (traced)
The count is computed **in the FE**, not the backend — it's a SUBTRACTION of two source counts:
- `portal/src/pages/ModelPortfolios.tsx`:
  - **Total footer (L1043):** `totalUnfundedCount = (metricsData?.total?.account_count ?? 0) − (activeDistribution.total.account_count ?? 0)`
  - **Per-model footer (L1009):** `modelUnfundedCount = (selectedModelMetrics?.account_count ?? 0) − (modelDistribution.account_count ?? 0)`
- **Intent (L966):** the bell curve shows **FUNDED accounts only** ("distributed by dollar value across open and pending positions"); the daily metrics carry **ALL** accounts; the **difference** is meant to be the newly-opened-$0-unfunded accounts excluded from the curve.
- Inputs: `metricsData` ← the daily-AUA metrics feed (`*.account_count`); `activeDistribution`/`modelDistribution` ← the bell-curve distribution feed (`partner_analytics … distribution.total.account_count`), produced by `data/orion/scripts/gold/09.generate_partner_analytics.py` (49/Global) and **`INF_09.generate_partner_analytics.py` (Inflection — separate producer)** off the positions cube (`A_03`/`INF_A_03.positions_cube.py`, `B_00.canonical_holdings.py`).

**CORRECTION (DS~B empirical 2026-06-01):** the distribution feed the footer actually reads is `json/mdpf/{firm}/account-distribution.json`, produced by `data/smartx/scripts/compute_per_firm_account_distribution.py` (49F+inflection) + `data/smartx/scripts/compute_account_distribution.py` (global) — sourced off eclipse `model_portfolio_accounts`. The `09/INF_09.generate_partner_analytics.py → partner_analytics.json` trace above is a DIFFERENT artifact (NNA, opal-data-inf) and is NOT the footer's source. Use the `compute_*_account_distribution.py` producers for the durable fix (§5/AC3).

So: number = (metrics account_count) − (bell-curve funded account_count). Valid ONLY if both are the same grain.

## 3. ROOT CAUSE — SCOPE mismatch (global metrics − per-firm distribution); grain secondary (DE TO-A verified, 1d3df59f3)
The DOMINANT bug is **SCOPE, not grain**. The metrics numerator (`metricsData.total.account_count`) is **GLOBAL** (7039; there is NO firm_id / no per-firm account_count in the metrics feed); the distribution denominator is **PER-FIRM**. So every per-firm footer computes **global_metrics − firm_distribution**. Reproduced to the integer: **Inflection 6639 = 7039 (global metrics) − 400 (Inflection distribution)**.
- The grain issue (Inflection distribution = CLIENT count, not accounts; `DistributionTab.tsx:175`) is REAL but **secondary/compounding** (it shrinks Inflection's denominator further → larger residual).
- REFINED vs first draft: **only Global's 14 is genuinely correct** (global − global). **49's 201 is ALSO wrong** (global 7039 − 49 6838) — coincidentally-plausible ONLY because 49 ≈ 97% of global, so it's **MASKED**, not a true per-firm count. The scope bug affects **ALL per-firm footers**, not just Inflection — Inflection is merely the most visible (smallest, client-grained denominator).
- Same per-firm-scope / Inflection-separate-grain class as today's cohort issues.

## 4. CORRECT INTENT
The footer should report the number of **genuinely newly-opened-AND-unfunded ACCOUNTS excluded from the bell curve**, computed **consistently at the accounts grain across all firms** — never a cross-grain subtraction. (Global ~14, 49F ~201 are the right order of magnitude; Inflection's true number should be similarly small.)

## 5. FIX OPTIONS (DE TO-A determined (b) is NECESSARY, not just preferred)
- **(a) Align grains — INSUFFICIENT (ruled out as a standalone fix).** Per DE: there is NO per-firm accounts-grain count in ANY served feed (metrics is global-only; per-firm aggregate-aua has no account count). A scope-fix has nothing to substitute as the per-firm numerator — so aligning grains alone cannot produce a correct per-firm count.
- **(b) Producer emits the count DIRECTLY at the per-firm accounts grain — NECESSARY (validated on Inflection 2026-06-01).** Compute the newly-opened-$0-unfunded **account** count per firm in the producer (`INF_09` + `09.generate_partner_analytics`, off the positions cube / canonical_holdings) and emit it as an explicit field the FE renders verbatim — eliminating the global-minus-per-firm subtraction for every firm. DE handed DS~B the exact emit-target. **PRODUCER CORRECTION (DS~B empirical 2026-06-01; supersedes the §2 09/INF_09 trace):** the footer reads `json/mdpf/{firm}/account-distribution.json`, produced by **`data/smartx/scripts/compute_per_firm_account_distribution.py` (49F + inflection)** + **`data/smartx/scripts/compute_account_distribution.py` (global)** — NOT `09/INF_09.generate_partner_analytics.py` (those publish `partner_analytics.json` (NNA) on opal-data-inf, a different artifact). **PROVEN-OUT:** DE TO-B verify — `compute_per_firm_account_distribution.py` now emits `total.excluded_unfunded_count` (Inflection=5 vs the buggy 6639; 49F=2), accounts-grain (Inflection: active 405 = funded 400 + excluded 5; total accounts 405). AC2 MET for Inflection + 49F (total footer).
  - **`by_model` field is REQUIRED in scope (CTO ruling 2026-06-01, 201804Z).** The field must be emitted at BOTH the firm-`total` grain (covers L1043 total footer) AND the `by_model` grain (covers the **per-model footer L1009** = `selectedModelMetrics.account_count − modelDistribution.account_count`) — in BOTH producers (`compute_per_firm_account_distribution.py` (49F+inf) + `compute_account_distribution.py` (global)). Rationale: L1009 is the SAME cross-grain subtraction bug class as L1043, compounded for Inflection where model-level distribution is CLIENT-grained (`DistributionTab.tsx:175`); leaving `by_model` unfixed = a known-identical latent defect one model-selection away. The durable fix is coherent only when EVERY place that renders this footer reads the emitted field, not a subtraction.
  - **Emit status:** `compute_per_firm_account_distribution.py` total = DONE+verified for Inflection (excl=5) + 49F (excl=2); GLOBAL total (`compute_account_distribution.py`) = blocked on AE smartx-202606 $0-regression restore (COO-escalated); `by_model` (all firms, both producers) = REMAINING (DS~B post-respawn).
- **(c) FE guard (stopgap) — covers ALL per-firm footers, not just Inflection.** Since every per-firm footer is the buggy global−firm subtraction (49's 201 is masked-wrong too), the stopgap must suppress/relabel the per-firm footers (49 + Inflection) until (b) lands; Global's footer (global−global) is the only correct one and can stay.
Plan: ship (c) fast (kill the visible 6639 + the masked-wrong 49 number) → (b) as the durable per-firm grain-safe emitted count.

## 6. FIRST TO — lineage verification (gate before fix)
Confirm empirically: the EXACT grain of `metricsData.total.account_count` vs `activeDistribution.total.account_count` for Inflection (accounts / clients / holdings), reproduce 6639 = (X − Y), and identify which feed is the wrong grain (the `INF_09` distribution per the documented note, or the metrics source). Then implement (b)+(c). DS owns the producer/grain; RD owns the FE calc + guard; DE/CVO verify the corrected count is plausible + consistent.

## 7. Acceptance criteria
- AC1: lineage documented end-to-end (FE subtraction → both source feeds → producers + grains), Inflection 6639 reproduced + attributed to the grain mismatch.
- AC2: Inflection footer shows a plausible small newly-opened-unfunded **account** count (same intent/scale as 14/201), computed at the accounts grain.
- AC3: the count is computed consistently across Global/49/Inflection (same grain, same definition) — verified per-firm AND per-model. SUBCRITERIA: (3a) `compute_account_distribution.py` emits `total.excluded_unfunded_count` (+ `active_accounts_count`) at accounts grain for GLOBAL (mirror the Inflection/49F emit already in `compute_per_firm_account_distribution.py`); (3b) `by_model` carries `excluded_unfunded_count` in BOTH producers (`compute_per_firm` 49F+inf + `compute_account_distribution` global) so the per-model footer (L1009) reads it verbatim; (3c) FE reads the emitted field for BOTH L1043 (total) and L1009 (per-model), subtraction dropped entirely. Status: `compute_per_firm` total = DONE for Inflection (excl=5) + 49F (excl=2); 3a (global total, AE-data-blocked) + 3b (by_model) + 3c (FE) remaining.
- AC4: stopgap (c) prevents a wrong cross-grain number from rendering until the durable fix lands; durable fix (a/b) verified by DE/CVO.
- AC5: visual confirm (Andrew or /frontend-dev) the footer reads correctly per firm post-fix.
