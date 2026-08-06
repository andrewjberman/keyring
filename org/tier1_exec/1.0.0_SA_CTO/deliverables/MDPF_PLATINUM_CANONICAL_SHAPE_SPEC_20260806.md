# MDPF PLATINUM — CANONICAL SHAPE SPEC (12 files)

**Author:** `1.0.0_SA_CTO~Z` · 2026-08-06 ~2240Z
**Basis:** Andrew-direct at the CTO~Z terminal, 2026-08-06 (per-scope ruling @0caf2e907 + the semantics
clarification recorded verbatim in §1).
**Issued to:** `2.0.0_SA_COO~Z` (decomposition) · `0.4.0_DS_ClientPlatform~Z` (producers) ·
`0.7.0_AE_CloudOps~Z` (publisher/IAM) · `3.0.0_SA_CVO~Z` (verification) · `0.0.0_AB_MSTR~Z`.

---

## 0. THE PREMISE — READ THIS BEFORE ANY ROW BELOW

> **Andrew-direct, VERBATIM:** *"We actually are doing this currently, everything I'm describing right now
> is being depicted properly in the Portal PROD environment. **What we are discussing here is simply
> rendering canonically-shaped jsons for platinum, that is all.**"*

**THE BUSINESS LOGIC IS CORRECT AND LIVE. THIS IS A SHAPE PROJECT, NOT A DATA-CORRECTNESS PROJECT.**

⛔ **Therefore: a number that differs from your intuition is NOT a finding.** The semantics in §1 are
ruled, live, and rendering correctly in PROD today. **Do not "fix" them.** The only defects in scope are
**shape** divergences — a field present on one scope and absent on its siblings, or a value the producer
never emits.

*This clause exists because I made exactly that error an hour before writing this: I surfaced Global's
non-model excluding Inflection and Cottonwood (~$409mm) as "a consequence worth seeing," when it is the
ruled, correct, intended semantic. **Treating a correct number as a finding is how a working pipeline
gets "fixed."** — CTO~Z*

---

## 1. THE SEMANTIC INVARIANTS — RULED, LIVE, DO NOT CHANGE

> **Andrew-direct, VERBATIM:** *"on the matter of 'what non-model assets to count' in Global, yes we only
> count non-model assets as the non-model total for the Global aum-metrics and Global
> aggregate-aua-timeseries metrics. We do not count the non-model assets of Inflection or Cottonwood in
> those views. However, we still WANT TO INCLUDE THAT DATA in the Inflection and Cottonwood artifacts,
> regardless of whether Global uses them for its own aggregate. Also, we want to use the total model
> holdings counts (excluding the unfunded is fine) for Global aggregate scope in the account-distribution."*

**I-1 · GLOBAL NON-MODEL IS 49F-ONLY.** In **both** `aum-metrics` and `aggregate-aua-timeseries` at
`global`, the non-model total counts **only** 49 Financial. Inflection's and Cottonwood's non-model are
**not** summed in.

> **THE MECHANISM IS ALREADY DECLARATIVE IN THE ARTIFACT — use it, do not re-derive it.** Global's
> `aum-metrics.meta.fee_basis_components` carries `49financial: fee_scope "full"` vs
> `inflection: fee_scope "model"` and `cottonwood: fee_scope "model"`. **Non-model folds into Global
> exactly for `fee_scope: full` firms.** So I-1 is not a hardcode to preserve — it is a *config-driven
> rule already expressed in the data*, and the canonical builder should read it rather than special-case
> 49F by name. Prior grounding: `dim_mdpf_aggregate_aua_timeseries.py:1826` (Andrew-direct 2026-07-22,
> basis B) + the leg pins at `:1538-1569` that already assert both legs.

**I-2 · EACH FIRM'S OWN ARTIFACT CARRIES ITS OWN NON-MODEL — INDEPENDENT OF I-1.** Inflection's non-model
belongs in Inflection's files; Cottonwood's in Cottonwood's. **I-1 governs what Global folds; it does not
govern what a firm publishes about itself.** These are two different questions and conflating them is the
error this invariant exists to prevent.

**I-3 · GLOBAL `account-distribution` USES TOTAL MODEL HOLDINGS COUNTS across firms**, excluding unfunded.
Measured live and correct: `account_count 7,925` / `active_accounts_count 7,974` / `excluded_unfunded 49`.

---

## 2. THE TARGET — 12 FILES

`s3://opal-data-portal-v2/platinum/mdpf/{scope}/` for `scope ∈ {global, 49financial, inflection, cottonwood}`
× `{aggregate-aua-timeseries, aum-metrics, account-distribution}.json` — **every single day** (@0caf2e907).

> **`aum-metrics` IS ALREADY CANONICALLY SHAPED — USE IT AS THE REFERENCE PATTERN.** Measured: all four
> scopes carry an identical `total` key set (`account_count, aum, model_aum, non_model_aum, q0..q3,
> series_start`) plus `scope`, `period`, `dates`, `by_model`, `meta`, `_provenance`, `last_updated`.
> **Zero shape divergence across scopes.** It is the existence proof that the other two can be uniform,
> and the shape to converge them toward.

---

## 3. MEASURED SHAPE DIVERGENCES — THE ACTUAL WORK

All measured 2026-08-06 ~2235Z from the **served bodies** (`s3 cp` per key, not `LastModified`).

### 3a · `account-distribution`

| field | inflection | 49financial | cottonwood | global |
|---|---|---|---|---|
| `basis` | ✓ `schwab-rps` | ✓ `schwab-rps` | ✓ `bd-rebalancer-models + bd-datamining-values` | ⛔ **`null`** |
| `source` | ✓ | ✓ | ✓ | ⛔ **`null`** |
| `firm_id` / `firm_name` | ✓ | ✓ | ✓ | ⛔ **absent** |
| `meta` | ✓ | ⛔ **absent** | ✓ | ✓ |

**S-1 (global):** the fold drops `basis`/`source` to null and omits `firm_id`/`firm_name`. Decide the
canonical global form — a scope identifier plus a *composite* basis/source naming the contributing legs
is the shape-consistent answer; **null is not.**
**S-2 (49financial):** alone lacks `meta`. The other three carry `meta.account_count_by_model_key`.

### 3b · `aggregate-aua-timeseries`

| field | inflection | 49financial | cottonwood | global |
|---|---|---|---|---|
| `account_count_total` | ✓ | ✓ | ⛔ **absent** | ✓ |
| `count_provenance` | ✓ | ✓ | ⛔ **absent** | ✓ |
| `source_vintage_last` | ✓ | ✓ | ⛔ **absent** | ✓ |
| `non_model_aua` populated | 431/437 | 437/437 | ⛔ **8/446** | 431/455 |

**S-3 (cottonwood) — the largest gap.** Three fields the other three scopes carry are **never emitted**.
Root cause is structural, not a bug: **cottonwood is built by a different script in a different tree**
(`data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`) from 49F/inflection
(`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`). The one firm-parameterized path
(P1-1) is what closes this — it is the consolidation's whole point, arriving as a shape requirement.

**S-4 (cottonwood non-model) — I-2's live gap.** 8 of 446 dates populated. **Not a defect in the
derivation:** the slice builder derives `non_model = partner_custody_total − model_aua` and holds
*honest-None* when custody is absent, with a W-2b identity gate (`:744`) that refuses a fabricated
balance. **The last two dates ARE populated (~$346mm)** — the custody leg only recently began landing.
**Per I-2 this data belongs in Cottonwood's own artifact**, so the requirement is coverage, not a new
mechanism. ⚠ **Never close this by relaxing the honest-None rule** — a populated-but-wrong non-model is
worse than None, and the identity gate is the control preventing it.

**S-5 (global, shape question — not a defect):** global carries `inflection_non_model_aua`, a
**firm-named field at global scope**, marked audit-only in source. Under I-2 that data is canonically
Inflection's and already lives there (431/437). **Question for the spec, not an assumption:** does the
canonical global shape retain a firm-named audit series? *Do not delete it on this document's authority
— it is referenced by `route_bindings.yaml:101-103` and by the leg pins.*

**S-6 (global-only fields):** `opal_aggregate_aua`, `point_class`, `account_count_total_raw`,
`count_as_of`, `count_basis` exist only at global. Some are legitimately global-only
(`opal_aggregate_aua` is the headline identity's left side). **Classify each as canonical-global vs
residue before P1-1 freezes the shape.**

### 3c · Data-adjacent observations — VERIFY, DO NOT ASSERT

Per §0 these are **not** filed as defects. Flagged only so the canonical builder reproduces intended
behaviour rather than silently changing it.

- **Global count is HELD at a 2026-07-22 vintage** — `count_basis` tail is all `held`, `count_as_of` ends
  `2026-07-22`, while `model_aua` runs to `2026-08-03`. The field is **honestly labelled**; confirm the
  hold is intended before the canonical builder reproduces or refreshes it.
- **Firm-sum 7,926 vs global 7,925**, and `meta.cottonwood_fold.accounts_folded 295` vs cottonwood's own
  `294`. Plausibly an intended dedup. **Confirm intended; do not "correct" it.**
- **Mixed vintage in the global fold** — global stamps `period 2026-08-04` while folding cottonwood's
  `2026-08-03`. Consistent with per-feed cadences (Rule 1); confirm the stamp convention is intended.

---

## 4. ACCEPTANCE

Per the standing governing criterion — **assert the OUTCOME, never the intervention**:

1. **12 objects exist** at the 12 canonical paths for the day *(EXISTENCE — never reported as freshness)*.
2. **Per artifact type, the key set is IDENTICAL across all four scopes**, modulo an explicitly declared
   and justified global-only set (S-6). A field present on one scope and absent on a sibling is a
   **failure**, not a warning.
3. **I-1 holds and is CONFIG-DRIVEN**: global non-model equals the sum over `fee_scope: full` firms —
   asserted against `fee_basis_components`, **not** against a literal `49financial`.
4. **I-2 holds**: each firm artifact carries its own non-model; Cottonwood's coverage is measured and
   reported as a ratio with its denominator printed.
5. **I-3 holds**: global `account-distribution` counts total model holdings excluding unfunded.
6. **Byte-comparison against today's served artifacts** for every field NOT named in §3 — the shape
   changes; the business payload does not. **A diff outside §3 is a regression.**

---

## 5. WHAT THIS SPEC DOES NOT AUTHORIZE

- **No served key moves.** `json/mdpf/*` untouched; the hyphenated legacy `account-distribution.json`
  bell does not move.
- **No semantic change.** §1 is ruled and live. A builder that changes a §1 number has failed, not fixed.
- **No deletion.** S-5/S-6 are classification questions; deletion of a served field is NEVER#3 and
  Andrew's.
- **The 12-vs-14 question stays open** — `cottonwood/account-units` and `global/non-model-assets` are
  live (measured in today's 13:50:50Z cycle) and outside these 12 pending Andrew's word.
