# 49F GOLD ANALYTICS RUNNER -- GROUP B SPEC (HOLDINGS / VALUATION CANONICALS)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~0745Z** · **archetype:** IMPLEMENT (design)
**Commission:** @5e4b8dda98, sequential -- GROUP B, follows Group A @9c294bbf15. For CTO review.
**Schema grounding (live pulls, 07:3xZ, date=2026-08-07):** `dim_balance` 7,239 rows x 39 cols ·
`dim_position` 95,879 rows x 30 cols -- column names below are measured, not assumed.

---

## 0. WHAT GROUP B IS

Group B canonicalizes the VALUATION PLANE: sec3's fair-value portfolio valuations, on the
PREFERRED-INPUT branch the feasibility run @e323c1cfac proved ("an authoritative account-level
end-of-day total portfolio value" EXISTS -- `dim_balance.net_mv_plus_cash`, 7,239/7,239 populated,
525 daily partitions). **Group B computes NO returns and classifies NO flows.** It emits the
valuation series, the position canonical beneath it, the accrual decision, and the valuation-plane
integrity artifact that C's guards consume. Everything stamps `boundary_version` (A_02) and rides
the A_04 calendar -- a "missing" weekend partition is a calendar fact, never a gap (the T-1 law).

**The convention, chosen once (sec3 "consistent cutoff"):** valuation = Schwab EOD statement close
per `business_date` (T-1 delivery). No intraday marks exist in the estate, so exact-flow TWR
coincides with daily TWR (feasibility) -- C-group inherits this as a fixed fact, not a choice.

## 1. THE FOUR GROUP B ARTIFACTS

Home: `{PRODUCT_ROOT}/canonical/{artifact}/date={D}/` + manifests (atom 3), per the Group A
product-root decision (whatever CTO rules there binds here unchanged).

| # | Script | Inputs | Output | Contract |
|---|---|---|---|---|
| B_00 | `b00_canonical_valuation.py` (NEW, thin) | `dim_balance` + `dim_boundary` (A_02) + B_02's ruling | `canonical_valuation` -- grain (account_id, date) | **V(t) = `net_mv_plus_cash` AUTHORITATIVE** (sec3 preferred branch -- never reconstructed), carried WITH its measured decomposition: `mkt_value_long`, `mkt_value_short`, `net_mv_positions`, `cash_balance_settled_only`, `cash_margin_bal_settled`, `money_mkt_funds`, `bank_sweep_ibf`, `bank_cash`, `margin_balance`, `net_credit_debit` -- the sec2/sec3 cash-sweep-MM-margin-liability surface, content-named passthrough. Plus `accrued_income` (from B_02, 0.0-with-status until ruled) and `fair_value` = net_mv_plus_cash + accrued_income. boundary_version stamped |
| B_01 | `b01_canonical_positions.py` (NEW, passthrough + flags) | `dim_position` + `dim_security` (A_03) | `canonical_positions` -- grain (account_id, date, cusip, l_s) | Sec3's position fields, content-named: signed quantity (`quantity_settled_unsettled` with `l_s` as the SHORT sign carrier -- **`l_s` is POSITION SIDE, the same semantic the IC-row debit_credit trap taught @5bb3b2626d; never read it as direction**), `closing_price` + `closing_price_unfactored` + `factor` + `asset_backed_factor` (the factored-price pair kept TOGETHER -- a bare closing_price on ABS misprices), `market_value_settled_unsettled`, identifiers via A_03. **QUALITY FLAGS per row (sec9's "missing/stale/zero flagged"):** `price_stale_days` = business_date - `secprice_lstupdte` (the vendor's own stale-price indicator -- sec3 asks for exactly this and the estate HAS it), `zero_price_flag`, `zero_qty_nonzero_mv_flag` |
| B_02 | `b02_accrual_decision.py` (NEW -- a MEASUREMENT + a ruling surface, not a daily runner) | `dim_position` x A_03 rate-bearing set (112 of 2,313 assets by `interest_rate` nonzero) + `fact_sec` accrual inputs | `accrual_materiality.json` (versioned) + optionally `canonical_accrued_income` | **Feasibility cell 4 executed as designed: the materiality gate FIRST.** One weighted-position read: MV of rate-bearing positions / book fair value, printed with both denominators. IF material -> derive accrual from the vendor-shipped inputs (`interest_rate`, `1st_cpn_date`, `dividend_interest_frequency`, `next_pay_date`) into `canonical_accrued_income`, folded into B_00.fair_value. IF immaterial -> **DOCUMENTED-EXCLUSION** artifact (the measured number + the ruling) and B_00.accrued_income stays 0.0 with `accrual_status=EXCLUDED-IMMATERIAL` -- sec10's data-quality status carries it. **The gate's verdict is ANDREW/CTO-ruled on the measured number, not build-chosen** (sec8 policy class) |
| B_03 | `b03_valuation_integrity.py` (NEW; c04_recon_guard's valuation half EXTRACTS here) | B_00 + B_01 | `valuation_integrity` -- grain (account_id, date) | Sec9 bullet 1 computed WHERE valuations live: `recon_variance` = [SUM(qty x price x factor) + settled cash + MM + sweep + bank] - net_mv_plus_cash, per account per day, with `recon_status` (TIE / VARIANCE-EXPLAINED / VARIANCE-UNEXPLAINED at an ex-ante tolerance CTO sets at review). **This is a FLAG PLANE, not a gate** -- C's guards consume it; B never blocks on it (a valuation that fails its own tie still serves the C-group hard-stop sweep the truth) |

## 2. DESIGN RULES BINDING ALL FOUR

1. **Authoritative-over-reconstructed, verbatim from the standard:** "Cost basis, realized gain,
   or unrealized gain cannot substitute for fair value." B_00 never computes V(t) from positions;
   B_03 computes the position tie ONLY as validation. The reconstruction never serves.
2. **The daily-atomic grain rides the A_04 calendar** -- prev-partition resolution exactly as the
   existing c00_runner proved it (partition tree = trading calendar; REFUSE when no prior
   partition exists rather than fabricate a BMV; explicit override audited in the manifest).
   That period-resolution block is quality structure per instruction 4 -- EXTRACT it, one home.
3. **Backfill is a first-class mode:** all four artifacts are date-parameterized and idempotent
   over the full 525-partition history (2024-07-08..). The backfill IS the initial build; the
   daily run is the same code at date=T (atom: one runtime per leg).
4. **No silent column drops** (Rule 17 spirit at gold: B_00/B_01 are passthrough-plus-derivation;
   every dropped source column is a DECLARED exclusion in the manifest, not an omission).

## 3. DECISIONS-FOR-REVIEW (CTO at this group's review)

1. **The B_03 tolerance** (ex-ante, sec9): default proposal 1bp of fair_value per account-day,
   with the UNEXPLAINED census printed per run.
2. **B_02's ruling routing:** the materiality number goes to you+Andrew as one line with the
   derive-vs-exclude recommendation; the spec proceeds building the MEASUREMENT either way.
3. **Whether `dim_balance` monthly siblings (`fact_rly`/`fact_rty`, 37 month-ends) enter B as a
   monthly cross-check artifact or stay C-side validation inputs** (default: C-side, canonical
   decision 4 -- attribution family validates, never serves).

## 4. WHAT GROUP B DOES NOT DO

No flow ledger, no classification joins, no TWR math, no serving. `fact_trn` is untouched by B
(C's spine). The rl*/rt*/uln/upn attribution families stay out (validation inputs at C). No
alerting/monitoring machinery (the moratorium) -- B_03's flag plane is data, not an alarm.

## 5. ACCEPTANCE (machine-checkable)

- B_00: row count == boundary IN_CLIENT_BOOK count for the partition (denominators printed);
  fair_value == net_mv_plus_cash + accrued_income exactly (identity control); one KNOWN account's
  vintage spot-tie vs raw dim_balance (positive control).
- B_01: SUM(market_value_settled_unsettled) per account ties dim_balance.net_mv_positions within
  the B_03 tolerance on the sampled partition; flag columns present; zero rows silently dropped
  (in-count == out-count + declared-exclusion count).
- B_02: the materiality read prints BOTH denominators + the 112/2,313 census key; the artifact
  carries its ruling status; a mutated rate-bearing set flips the number (mutant control).
- B_03: recon_status census printed per run; determinism across two same-input runs; a poisoned
  price (mutant) lands VARIANCE-UNEXPLAINED, never TIE.
- All: provenance cols, manifests, boundary_version stamps, `from __future__ import annotations`.

-- 3.0.0_SA_CVO
