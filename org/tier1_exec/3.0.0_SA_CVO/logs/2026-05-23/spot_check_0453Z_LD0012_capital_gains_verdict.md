# CVO Verify-Channel Verdict — LD-0012 — peter_lee `capital_gains_ttm` = -$54.8M — 2026-05-23 04:53Z

**Agent:** 3.0.0_SA_CVO | **Mode:** /verify-channel investigation per MSTR charter LD-0012 (`618c841aa`, Andrew-flagged D-001 PHASE 2 META trigger)
**Subject:** peter_lee `capital_gains_ttm = -$54,807,679` on Inflection ~$200M book — surfaced in DS VALFIN.001 Phase-1 session log `c02c9c1ed` Routing Ask #4

## VERDICT: YELLOW

The number is mechanically computable per the script's TTM-LOCKED 2026-05-12 spec, but **two distinct issues** require routing — one structural (semantic mislabel at the data layer; portal already patched but data layer didn't) and one substantive (magnitude warrants a forensic that DS's proposed plan can't actually deliver).

## MECHANICAL: PASS

DS session log `session_valfin_001_phase1_c07_to_d02.md` already validated INF_D_02 + book.json artifact 4-check (EXISTS/FRESH/SCALED/NOT-FROZEN PASS). The pipeline ran; the number landed where expected.

## NOVEL probe: source-traced the field

**Field definition** (`data/orion/scripts/gold/INF_D_02.advisor_client_detail.py:627-677`, `_compute_capital_gains_ttm_per_advisor`):

```python
ttm_end = pd.Timestamp(data_as_of)
ttm_start = ttm_end - pd.Timedelta(days=TTM_LOOKBACK_DAYS)  # 365d
end_rows = _nearest_date_row_per_account(perf, ttm_end)
start_rows = _nearest_date_row_per_account(perf, ttm_start)
...
merged['delta'] = merged['unreal_end'] - merged['unreal_start']
# Sum delta per advisor over their accounts
```

**Semantics**: `Σ_accounts (unrealized_gain_at_today - unrealized_gain_at_365d_ago)` over the advisor's accounts. The docstring is explicit: *"Semantics: change in cumulative unrealized capital gain over the trailing 365 days... Accounts that did not exist at the anchor contribute their full current unrealized_gain (treated as fully accumulated within the TTM window)."*

**This is NOT realized capital gains.** It is the **delta of mark-to-market unrealized gain** over the TTM window. Sister function `_compute_capital_gains_ttm_per_hh` at line 680 has the same semantics for households. Firm-scope sister in `INF_D_00.portal_aggregates.py:323-828` similarly logs `"firm capital_gains_ttm: ${...}M (12m delta unrealized)"`.

## Finding A — semantic mislabel at the data layer (P1)

The field name `capital_gains_ttm` naturally reads as "realized capital gains over the trailing twelve months" — which is what Andrew read, what DS effectively echoed in their session log ("capital_gains_ttm: separate computation within INF_D_02 (TTM rolling realized)" — DS line 148), and what surfaced to MSTR as a META trigger.

**The portal renamed this for display already** (`portal/src/pages/AdvisorIntelligence/_shared/panels/TaxCostBasisPanel.tsx:129-147`, INFFIN.019 Fix C):
- Display label: **"Unrealized P&L Change (TTM)"**
- Tooltip: *"Difference in mark-to-market unrealized gain over trailing 12 months. Does not reflect realized gains from closed positions."*

**BUT the underlying data field name persists** in every layer below the portal display:
- Script computation: `capital_gains_ttm` (`INF_D_02.advisor_client_detail.py:637`)
- book.json schema: `tax_exposure.capital_gains_ttm` (every advisor's platinum artifact)
- Portal TypeScript type: `capital_gains_ttm: number` (`types.ts:934` + `:1100`)
- Portal adapter: `capitalGainsTtm: bookData.tax_exposure.capital_gains_ttm` (`AdvisorBookView.tsx:571`, `ClientsTab.tsx:839`)

**This is exactly how Andrew encountered the misleading semantic** — via the raw field name in the DS Phase-1 session log, not through the portal where the rename + tooltip protect the reader. Anyone reading the data directly (analysts, agents in session logs, future debugging) hits the same mismatch.

**Fix (NOT my lane; routes to DS + DE):** rename the underlying field across all layers — script → JSON key → TypeScript type → adapter — to `unrealized_gain_change_ttm` (matches the INFFIN.019 portal-renamed display label). Backwards-compat shim if any external consumer reads the old key. Touches `data/orion/scripts/gold/INF_D_02.advisor_client_detail.py`, `INF_D_00.portal_aggregates.py`, `portal/src/pages/AdvisorIntelligence/_shared/types.ts`, both consumer adapters; ~1 small TO.

## Finding B — DS's proposed Phase-2 diagnostic plan is partially wrong (P1)

DS session log proposed two Phase-2 cross-checks (line 156-157):
> (a) Verify TTM window definition in INF_D_02 script
> (b) Cross-ref against `silver/api_dims/tax_realized/` period_start/end fields

**(a) is sound** — that's what this verdict just did. TTM window = `[data_as_of - 365d, data_as_of]`, "nearest date row" anchor strategy. Confirmed.

**(b) is INVALID — the source is wrong.** The `capital_gains_ttm` computation does NOT consume `silver/api_dims/tax_realized/` at all. It reads ONLY `perf.unrealized_gain` from `gold/timeseries/account_performance.parquet` (cross-referenced at script load_account_performance line 234-247) and `account_team` mapping. Cross-checking against `tax_realized` would diff two unrelated semantics and produce a misleading "discrepancy" that wouldn't actually be a defect.

**The right Phase-2 diagnostic** (which DS should run, scoped via COO):
1. Pull peter_lee's accounts' `unrealized_gain` time-series from `gold/timeseries/account_performance.parquet` for `[2025-05-22, 2026-05-22]`.
2. Decompose the per-account delta_unrealized contribution. Sort descending by magnitude.
3. Check for any single account contributing >$20M of the loss — that's the smoking gun (most likely cause).
4. If a single account dominates: check (a) whether it churned out of peter_lee's book during TTM (changes the math via the "accounts that did not exist at anchor contribute their full current" treatment line 633-635) or (b) whether the underlying position prices dropped (verify against position-level cost-basis / mark-to-market).
5. If the loss is broadly distributed across accounts: check (a) book turnover (positions sold, realizing gains out of the unrealized pool), (b) cash outflows (clients drew down), (c) a systematic data issue (perf table's unrealized_gain field has a bug).

The "fully accumulated" treatment for newly-onboarded accounts (line 633-635) is also worth Phase-2 inspection — it creates asymmetric accounting: new accounts add their FULL current unrealized as positive delta, but accounts that LEFT during TTM aren't subtracted symmetrically. peter_lee being a senior advisor with established book + recent churn could produce strongly-negative deltas under this asymmetry even with a fundamentally healthy book.

## META: under correct semantic, magnitude is unusual but not impossible

A -$54.8M delta_unrealized on a ~$200M advisor book over TTM = -27% in the unrealized-gain pool. Under the correct semantic (NOT realized losses), this is unusual but admits several plausible explanations even in a flat-to-positive market year:

- **Account churn** — a large account that joined more-than-365d ago and left within the TTM window subtracts its prior unrealized gain
- **Book turnover** — positions sold during TTM move from "unrealized" pool to realized (the unrealized gain disappears from the pool even though it's not a loss to the client; total wealth unchanged)
- **Cash outflows** — withdrawals reduce holdings without realizing market losses
- **The "fully accumulated" asymmetric treatment** (line 633-635) — described above, could amplify the negative figure in churned-book scenarios

A 2025-2026 market drop is NOT a plausible cause (markets have not dropped 27% in TTM). The magnitude is suspicious enough to warrant the Phase-2 forensic above, but not impossible enough to call RED on the script.

**Where META fails closed:** under the COMMON-SENSE reading of the field name (which Andrew applied, which DS effectively echoed, which MSTR surfaced as a meta-trigger) — i.e., "realized capital gains over TTM" — a -$54.8M figure on a $200M book IS implausible. **The semantic mislabel is what produced Andrew's "suspicious as hell" reaction, not the underlying number.** Finding A captures this directly; fixing the field name across the data layer prevents the recurrence.

## Findings → drivers (routing per charter)

- **For MSTR (0.0.0_AB_MSTR):** YELLOW verdict — see above. The META layer caught a real defect, but the defect is **structural (semantic mislabel at data layer) not numerical**. Andrew's reaction was correctly triggered by the field-name-vs-semantic mismatch; the underlying delta_unrealized number is plausible-not-implausible under the correct semantic. Fix routes to DS + DE via COO (field rename across all layers); the magnitude forensic routes to DS via COO (per Finding B — DS's proposed plan needs the source correction). No CVO-side fix attempted; verifier-not-fixer holds.

- **For COO (2.0.0_SA_COO, P1):** Two follow-ons to absorb / dispatch:
  1. **Field-rename TO** (Finding A) — `capital_gains_ttm` → `unrealized_gain_change_ttm` across script + JSON + TypeScript + adapter; backwards-compat shim if external consumers read the old key. Could fold into ADVI_VALFIN TO-5 (pipeline robustness) or be its own ADHC. ~1 day wall.
  2. **Phase-2 diagnostic re-scope** (Finding B) — when you dispatch the VALFIN.001 Phase-2 follow-on, fix DS's proposed cross-check (b): the right source for diagnosing the magnitude is `gold/timeseries/account_performance.parquet`'s `unrealized_gain` per-account time-series, NOT `silver/api_dims/tax_realized/`. Plan outline in this verdict's Finding B.

- **For DS (0.4.0_DS_ClientPlatform, P1):** Heads-up on the Phase-2 plan correction (cross-check (b) source-error). When you re-pick-up VALFIN.001 Phase-2, the magnitude forensic for peter_lee should pull the perf-table unrealized_gain per-account time-series, not the tax_realized silver dim — they're independent computations and diffing them yields a meaningless number. Also, your session log's line 148 "capital_gains_ttm: separate computation within INF_D_02 (TTM rolling realized)" — the "realized" word there is the same semantic confusion that misled the rest of the chain; the computation is delta-unrealized.

## What I did NOT do (scope limits)

- Did NOT pull peter_lee's `unrealized_gain` time-series from S3 myself — that's the Phase-2 forensic, which is DS's lane (the producer); CVO's role per /verify-channel discipline is source-trace + verdict + route, not full forensic dive.
- Did NOT propose a rename PR — author authority for `INF_D_02.advisor_client_detail.py` belongs to DS per the safe-deploy chain (CLAUDE.md Rule 13); CVO routes findings, doesn't push code.
- Did NOT charter fix-scope changes to my own /spot-check skill — Part 2 of LD-0012 charter is a separate item I ACK'd; will land the SPOT_CHECK.md substance-meta extension after this verdict.

## /spot-check Part-2 design call (LD-0012 §2 doctrine refinement)

Per ACK `20260523T045019Z`: extending the /spot-check SCAN scope to include substance-level meta-checks ("does this number make sense at this magnitude given context?") IS the right doctrine evolution — this verdict is the exemplar of what SCAN should catch automatically. FIX authority remains alignment-metadata-only per current scope; substance findings always route to the code-owner via the verify-channel pattern, exactly as this LD-0012 cycle exercised.

Concrete `SPOT_CHECK.md` updates I'll land in a follow-on commit:
- Add Step 2c.4: **Substance meta-check on numeric assertions surfaced in commit body / session log / changed artifact**. Apply quick heuristics: magnitude vs surrounding context (book size, prior values, asset-class typical ranges); sign expectations (a "growth" metric coming out negative warrants probing); naming-vs-semantic alignment (does the field name match what the code actually computes?).
- Add a new finding class to Step 2d: **Substance-meta finding** — always routes to code-owner + COO + MSTR via MCP per verify-channel pattern; never CVO-fixed directly.
- Add a META-CHECK HEURISTIC subsection to the charter's Fix-authority section so SCAN vs FIX separation is structurally documented.
- Add LD-0012 capital_gains_ttm as the worked-example reference so future cycles have a concrete template.

## Plumbing
Inbox empty; watcher tracked `bp71vipvx`; heartbeat refresh follows. Verdict log committed under CVO author line. MSTR + COO + DS messages follow.

— 3.0.0_SA_CVO
