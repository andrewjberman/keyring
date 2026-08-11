# GIPS TRANSPOSITION MAP — Inflection (Orion) + Cottonwood (Black Diamond) against the 49F GIPS shape

**Author:** `4.0.0_SA_CRO~A` · 2026-08-11 ~0700-0715Z · **archetype:** TRACE + VALIDATE
**Authority:** Andrew-direct instruction 6 (verbatim in the ANDREW_DIRECT record; egress + endpoint
testing granted per-use both vendors) · **form per the shape-transposition vision @6e180df78e**
(49F field contract as rows; per-firm verdicts RAW-AVAILABLE / MANUFACTURABLE / ABSENT-with-shape).
**Reference standard:** the 49F GIPS run @e323c1cfac (Andrew's GPS-standard doc IS the spec;
cite-don't-re-derive) — its two deciding halves + refinement-cell fields are the row axis.
**Evidence:** at-rest reads this session (partitions counted, samples read, denominators printed);
the two cells no at-rest read can answer carry PROBE SPECS, not guesses.

---

## VERDICT IN TWO LINES

**INFLECTION: YES — daily-TWR tier, and STRONGER than the 49F baseline** (a seven-year 100%-raw
valuation series + a fully-dated 46-code ledger with explicit external/internal categories + a
vendor-computed TWR surface 49F lacks entirely).
**COTTONWOOD: YES-WITH-BACKFILL — the shape is fully manufacturable, but the at-rest history is
shallow (valuations 2 months, flows ~14-day rolling window); the manufacture is a NAMED, already-
exercised endpoint mechanism (BD Custom-window backfill), not creativity beyond the sanction.**

## THE TRANSPOSITION MAP

| 49F GIPS contract field (from @e323c1cfac) | INFLECTION (Orion) | COTTONWOOD (Black Diamond) |
|---|---|---|
| **H1 · daily per-account fair-value series** (the deciding half 1) | **RAW-AVAILABLE, deep:** `gold/canonical/holdings_{date}` — **2,450 daily partitions 2019-09-17→today**, position grain summing to account totals, **100% `source=pmv_only` in every sampled era (2020/2022/2024/2025/current)** — raw vendor positions-market-value; the interpolated price tier contributes ZERO rows to this series. | **RAW-AVAILABLE but SHALLOW + MANUFACTURABLE-deeper:** `blackdiamond/cottonwood/silver/fact_holdings` — 47 daily partitions 2026-06-09→08-07, per-position Market Value + Unaccrued MV + **Accrual (native!)**, 925 accounts. **History backfill = BD snapshot tables with Custom-window historical as-of — the exact mechanism the cot lag machinery exercises daily** (`cot_bronze_ingest.py` TABLE_DATE_MODE Custom + as-of lag). Shape of the pull: per historical date D, holdings snapshot as-of D → `HOLDINGS_DAILY_{D}` — the ingest already lands this form. |
| **H2 · classifiable external-flow ledger** (deciding half 2) | **RAW-AVAILABLE, deep:** `silver/transactions` snapshot — 1.43M rows ~2020-06→today, **transDate + transAmount 100% populated, 46-code transTypeId universe with ZERO nulls**, and `activityCategory` gives the external/internal split EXPLICITLY (Contributions 4,729 / Distributions 6,830 / Journal In-Out 2,637 / Merge In 7,577 = external; Trades, Dividends-and-Interest, Exchange In-Out = internal) + `orion_cashflow_taxonomy.yaml` + the 47-entry decode dict already in silver. | **RAW-AVAILABLE but WINDOWED + MANUFACTURABLE-deeper:** latest cot txn partition = 11,132 rows covering **2026-07-27→08-07 only** (a rolling restatement window; 64 sparse partitions at rest, gapped). Classification is CLEAN: `transaction_type` (14) × `transaction_sub_type` (21) with explicit Cash Withdrawal / contribution-class members. **Flow-history backfill = the SAME BD DataMining transactions query with Custom windows walked backward** (the 3-day-chunk machinery already proves arbitrary-window pulls). Shape: per window [start,end], the 71-col txn export as already landed. |
| **Vendor-computed return (the standard's canonical decision 1)** | **RAW-AVAILABLE forward, PROBE for history:** `silver/api_dims/performance` — account-grain TWR + risk metrics, **94 daily snapshots since 2026-04-28** (forward-accumulating). Historical as-of: the Envision Custom-window machinery stamps historical as-ofs for other dims daily; whether the PERFORMANCE option-set returns as-of-consistent values historically is **PROBE SPEC P1** (one Envision pull with a historical window; ~12s async; reference implementation exists). Even ungranted, decision-2 (compute) is fully supported — the vendor TWR is then the standard's VERIFICATION series, a luxury 49F does not have. | **UNKNOWN-CATALOG, PROBE:** the 5 pulled queryTypes carry no performance table, and the BD template roster endpoint returns persisted HISTORY, not the catalog (d2b catalog §3.2: "a query type with zero prior usage is invisible") — so BD MAY ship a performance queryType we have never pulled. **PROBE SPEC P2:** sweep candidate queryTypeIds via template-create validation on the cot account (the d2b doc's own probe pattern, queryTypeId=6 precedent) OR vendor docs. If absent: cot = computed-from-components exactly like 49F (instruction-5's granted class, same quality bar). |
| **Flow-timing convention (sec6)** | Choose-at-build, same as 49F (EOD valuations only). | Same. |
| **Transaction-code classification table + materiality gate** (49F refinement 1) | Mostly EXISTS: 47-entry dict + taxonomy yaml; residue = `Other` category **1,793 rows (0.12%)** — materiality gate = build task 1, same shape as 49F's 60-row residue. | Build over the 14×21 explicit universes — smaller than 49F's; the windowed sample shows no empty-category residue (full-series confirmation at build). |
| **Transfer both-sides linkage** (49F refinement 3) | Journal In 1,566 / Journal Out 1,071 / Exchange In-Out ~718K (share-class exchanges — internal) — pair-matching build task, same method as 49F's. | Merge/transfer classes present in sub_types; same pair-matching method. |
| **Accrued income** (49F refinement 4) | Orion positions are valued by the vendor (pmv) — accrual embedded in vendor marks; NO derivation needed (simpler than 49F). | **NATIVE COLUMN** — `Accrual` + `Unaccrued Market Value` ship on every holdings row (cot is the BEST of the three firms here). |
| **Account→household map** (49F refinement 2 / fact_fam) | RAW: `household_rep_mapping` + accounts_v2 household_id — landed daily, join proven (98.0% native, RECON-4). | RAW: Relationship ID on every custody row (relationship-grain native); the ADVI-spine join is the known open item (MEASURED-NO-DIRECT-JOIN → intermediary via rebalancer_accounts, RECON-5a). |
| **Reversal mechanism** | `backdated_date` column present in cot… (INF: transTypeId reversal codes in the 46-universe; specimen scan = build-time, same as 49F's cell 5). | `backdated_date` + `entry_date` NATIVE on every row — restatement machinery explicit (the 14-day window EXISTS because BD restates); better instrumented than 49F. |
| **FX boundary** | USD-only book (no FX columns in the 49-col silver) — same boundary note as 49F. | Same (USD custody). |
| **History floor** | **Valuations 2019-09-17 (~7y); flows ~2020-06 (~6y)** — the deepest of the three firms. | At-rest: valuations 2026-06-09, flows 2026-07-27 (rolling). **Post-backfill floor = wherever BD's Custom-window history bottoms out — PROBE P2b measures it** (one deep-window pull; the d2b probe pulled 05/09–07/08 cleanly). |

## INHERITED PRIORS (base CRO's task-1 method @a876ee6ae9 — the classification FORM both firms reuse)

The classification build for both firms follows the task-1 form (full-series code census →
first-match rule list → {EXTERNAL-in/out, INTERNAL, FEE, CONDITIONAL-BY-COUNTERPARTY, UNRESOLVED}
partition → dual materiality frames), with its generator's rule set swapped per vendor. Four
corrections inherited as priors: (1) find the vendor's REAL money column before summing (Schwab's
net_amount was $0.00 on 1.9M rows); (2) the vendor category axis MISCLASSIFIES at boundary — first
cut, never final; (3) **day/window samples undercount code universes massively (21 vs 157 at
Schwab) — ⚠ THIS MAP'S OWN COT CODE CELL (14×21) IS A WINDOW-SAMPLE COUNT and is hereby marked so;
the build-time census runs over the union of all 64 at-rest partitions + backfilled history, and
the INF 46-code figure (full 1.43M-row series) does NOT carry this caveat**; (4) empty-description
codes get INFERRED partitions with specimen-verify flags, never silent force-fits. The 49F
template's single conditional is CLEARED @a876ee6ae9 — the cited verdict is now unconditioned.

## THE TWO PROBE SPECS (the only cells at-rest data cannot close; egress granted, time-boxed)

- **P1 (Orion):** one Envision performance-dim pull with a historical Custom window (e.g. as-of
  2026-06-30) via the persisted-template machinery; PASS = returned metrics differ from current
  and are as-of-consistent. Upgrades decision-1-history from PLAUSIBLE-BY-PATTERN to MEASURED.
- **P2 (BD/cot):** queryType catalog sweep by template-create validation (the d2b §4 pattern) —
  does a performance queryType exist? **P2b:** one deep historical Custom-window pull to measure
  BD's history bottom. Both on the cot account under the standing firm-scoped lift.

## WHAT THIS MEANS FOR THE PROGRAM (one paragraph)

The GIPS shape TRANSPOSES to both firms. Inflection is immediately build-ready at a HIGHER tier
than 49F (deeper history, explicit flow categories, plus a vendor TWR verification series pending
P1). Cottonwood's contract is fully satisfiable with one honest qualifier: its historical depth is
a BACKFILL PROGRAM over already-exercised windowed endpoints, sized by P2b — the manufacture is
named, mechanical, and uses zero creativity beyond the sanction. No ABSENT verdict was needed
anywhere on either map: every 49F contract field is RAW or MANUFACTURABLE at both firms, and two
fields (accrual, restatement instrumentation) are BETTER at cot than at the archetype itself.
