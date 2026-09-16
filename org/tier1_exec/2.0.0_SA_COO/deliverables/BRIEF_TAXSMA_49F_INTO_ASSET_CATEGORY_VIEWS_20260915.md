# BRIEF -- Connect 49Financial's Tax-Managed SMA to the Asset Category Views (additive to the total)

**For:** a CTO seat that Andrew names, to render into a project and finish the tracking.
**Author:** 2.0.0_SA_COO~D, 2026-09-15, on Andrew-direct ~03:0xZ (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_030xZ_TAX_SMA_BRIEF_FOR_CTO_ADDITIVE_TO_TOTAL.md`).
**Status:** input for the project, written at his request. It is not the CRO's L1 brief carrier. The CTO renders it
through the canonical flow as it sees fit.

---

## 1. What Andrew wants

> "write a brief for what you would need to get the data connected properly, and I will have a CTO render it into a
> project and finish tracking. We can just add that tax amount to the total, even though its technically in a different
> account bucket, it's fine, that just means its additive (is not netted from client residual)."

Earlier, at ~02:5xZ: "we should be tracking Tax SMA for 49Financial ... we should have been able to track it."

## 2. Proposed DONE WHEN (for the CTO to adopt or re-cut at L2)

1. On 49Financial's Asset Category Views, the **Tax-Managed SMA** L2 member under SMAs > ALT Strategies carries its
   real market value at the view's as-of date, refreshed every trading day by a scheduled run.
2. That value is **ADDITIVE**. The SMA total, the ALT Strategies bucket, the firm `total_aua` and the view-plane total
   (the portal's Total Assets headline) each rise by exactly that amount, and the Client amount does not move.
3. The Global scope includes it exactly once.
4. A Tax SMA value that is missing or stale beyond an agreed tolerance is emitted as **unmapped (`aum: null`)**, never
   as a stale number or a zero.

## 3. What already exists (read at the working tree by 2.0.0_SA_COO~D unless marked)

**The category registry already has the member and its basis, so no taxonomy work is left.**
- `data/mdpf/scripts/gold/mdpf_category_registry.py:360` registers `("tax", "tax", "Tax-Managed SMA", True,
  "ALT Strategies", SMA_BASIS_ADDITIVE)`.
- The basis evidence is at :324-328 and :358. Tax's five accounts are "0 of 5 in schwab 08242234 ... 5 of 5 in
  08335338", worth $6,445,461.07 at that measurement.
- Last change: @b6e97e9685, 0.4.0_DS_ClientPlatform~Z, 2026-08-29.

**The consolidator already does the additive arithmetic. Only the dollars are missing.** File:
`data/mdpf/scripts/gold/mdpf_gold_consolidator.py`, last changed @1465fd3f7d, 2026-09-11.
- **Where dollars enter:** SMA dollars come only from `by_model` entries that `registry.resolve_any(key)` maps to an SMA
  member (:704-763).
- **The additive guard:** an ADDITIVE member's entry MUST carry `source_basis`. An uncarried value is REFUSED
  (:746-754), and one that carries a different basis is refused too (:733-739).
- **Client is untouched:** only carve-out members are netted from Client, `client_aum = non_model - sma_carve_out_aum`
  (:791).
- **The total rises:** the firm total is `total_aua = total + sma_additive_aum` (:883). The code states "TODAY THIS IS
  EXACTLY 0.00 ... no by_model entry resolves to an additive member yet" (:880-882).
- **The headline follows:** the view-plane total is the sum of the rendered peers' node amounts
  (`mdpf_category_registry.py:1220-1221`, served as `sums.view_plane` at :1287). The SMA node therefore carries the
  additive dollars into the portal's Total Assets headline.

**The portal needs no change.** `CategoryViewTree.tsx` (portal feature/d13-visual-elevation) renders the served block:
- the Tax-Managed SMA member and its colour;
- the ALT Strategies bucket;
- the SMAs tile and its pie slice;
- the Total Assets headline.

**The Tax SMA data chain exists, but it is one-account and unscheduled.**
- **OPAL_TAXSMA_PT2 path:** Black Diamond bronze, then silver `fact_taxsma_report`, then gold `dim_taxsma_report` at
  `blackdiamond/49f/gold/dim_taxsma_report/`.
  - The gold table is keyed by Schwab account number and anonymized (`docs/architecture/OPAL_TAXSMA_PT2_PRD.md:33-51`).
  - Its `performancePeriod` class carries BMV/EMV (:27-31).
- **The account roster:** `blackdiamond/49f/_ops/taxsma_roster.json`, keyed by exact account number
  (`docs/architecture/OPAL_TAXSMA_REGISTRY_PRD.md:45`, and :17-21 for the exact-number rule).
- **Recorded remaining work:** "multi-account, WS-5 DAILY TRIGGER" (`docs/architecture/D9_TAX_SMA_OPS_PRD.md:41-45`).
- **NOT verified by this seat** (a delegated read of the CVO's 2026-08-28 log): on 08-28 `dim_taxsma_report` held one
  account, was 42 days stale, and had no schedule trigger.

## 4. The gaps: what has to be built

- **G1 -- Daily tracking of every enrolled account.** The producer must read the roster (REGISTRY WS-R3), pull every
  active account, and run on a schedule (PT2 WS-5).
  - It is D9 (c1). It is the precondition for everything below.
  - A production pipeline must be scheduled (CLAUDE.md).
- **G2 -- One Tax SMA value per as-of date.** The value is the firm-level sum of market value over the enrolled active
  accounts.
  - **THE MAIN DESIGN QUESTION:** which field, at which grain. PT2 was built for quarterly report windows (BMV/EMV per
    period), but the category view needs a daily market value. Options:
    - (a) a BD daily-value endpoint added to the existing producer;
    - (b) positions or balances for the five accounts from the Schwab 0833 data the estate already reads, if any;
    - (c) EMV of the latest period, as a stopgap flagged by its own as-of.
  - The CTO picks one. This seat recommends the option that yields a TRUE daily value, because anything else ages
    inside a daily view.
- **G3 -- Feed it to the consolidator as the `tax` member, with `source_basis: "additive"`.** Two shapes:
  - (a) a by_model-shaped entry keyed so `resolve_any` maps it to `tax`;
  - (b) a second, explicitly named input merged before the by_model loop.
  - This seat recommends (b). The by_model series is SmartX-sourced on the 0824 basis, and a Black Diamond / 0833 value
    written into it would blur whose number it is. Either way, the existing guard (:746-754) already refuses an
    additive value that does not carry its basis.
- **G4 -- Align the dates, with a freshness rule.** The view is dated to its own as-of, a trading-day frontier
  (`lib/trading_calendar.py`), and the Tax SMA value must be for that same date.
  - State a staleness tolerance in trading days.
  - Beyond it, emit `aum: null` for `tax`, which the registry already treats as UNMAPPED, not zero (consolidator
    :848-869).
- **G5 -- Scopes.**
  - 49financial: yes.
  - Global: confirm whether Global aggregates the firm blocks or builds its own. The additive term must land exactly
    once.
  - Other firms: none (Andrew-direct 2026-08-25, "only 49 has 'SMAs' category items at this point",
    consolidator :771-777).
  - The cross-firm fence holds, since 49F data feeds only 49F and Global.
- **G6 -- Out of scope unless he rules otherwise:**
  - the Model Overview Trend and the AUA timeseries (PT2 is forward-only, so a trend would step up on day one);
  - Alyssa's gateway access (PT2 WS-4);
  - anything touching trade generation.

## 5. Rulings already made (carry them, do not re-open)

- **Additive, not netted from Client:** Andrew ~03:0xZ (this brief's authority), matching the 2026-08-29 registry
  basis.
- **The human-executes guardrail on the Tax SMA trade process is untouched** (D9 PRD :12-14).
- **Accounts are keyed by EXACT Schwab account number, never a fuzzy match** (REGISTRY PRD :17-21).
- **The serve layer is gold only and PII-free** (PT2 PRD :33-51). The rollup reads gold `dim_taxsma_report`, never
  silver.

## 6. Proof that can fail (suggested acceptance)

On the served 49financial block for one as-of date D:
1. The `tax` member's aum equals the G2 value for D to the cent. That value is recomputed independently from
   `dim_taxsma_report` for D, and the denominator (accounts summed) is printed.
2. `ALT Strategies` equals the sum of its members.
3. `total_aua(D)` minus the prior-basis total for D equals the tax value exactly.
4. The Client amount equals its prior-basis value exactly.
5. `sums.view_plane == total_aua - insurance_excluded`.
6. **Negative arm:** a tax value with no `source_basis` is REFUSED by the consolidator. Run it; do not read it.
7. **Staleness arm:** a Tax SMA input older than the tolerance emits `aum: null`.
8. **Render:** the portal shows the member under ALT Strategies, and the Total Assets headline has moved.

## 7. For Andrew, before the project is cut

- **D9's meeting gate.** D9 PRD section 4.2 holds build work until the Yang/Alyssa meeting "unless Andrew explicitly
  waives". Does "finish tracking" waive it for G1-G5? This seat does not assume it does.
- **The interim display.** Until G1-G4 land, 49Financial shows ALT Strategies "$0" (portal 208848cb shows a zero L1
  bucket). Keep it that way, or mark the bucket "not yet tracked"? His call. It becomes moot once the value flows.

## 8. Relation to existing projects

This is D9's items (c1), (c3) and (c4), narrowed by what the code already has:
- (c3) registry wiring is effectively DONE, because `tax` is registered with its basis;
- (c4) the page roll-in needs no portal change;
- the real work is (c1) daily multi-account tracking plus a new consolidator feed (G2-G4).

Candidate homes: an addendum to OPAL_TAXSMA_PT2 or a new D9 project. That is the CTO's call. The prior owner seat of
the tax projects, 0.5.0_AE_OpalETL~A, is recorded as dead (D9 PRD :141-143).
