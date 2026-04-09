# GRO and NNA Calculation Status Post-GLDOPS.003

**Date:** 2026-04-06
**Author:** 0.4.0_DS_ClientPlatform

---

## Purpose

Document the current state of the GRO (market growth) and NNA calculation
pipeline after the GLDOPS.003 edits. This is a reference for anyone verifying
portal numbers after the next gold rebuild.

---

## GRO: How Market Growth Is Now Calculated

### The Identity (script 05, per relationship per day)

```
delta(total_aua) = delta(nna) + market_growth + synthetic_correction
```

Rearranged:

```
market_growth = delta(total_aua) - delta(nna) - delta(synthetic_aua)
```

Where:
- `total_aua` = sum(units * canonical_price) across all positions in the relationship,
  aggregated from the positions_cube. **No silver override applied.** The only corrections
  applied to AUA are bond face-value detection (Yahoo equity price applied to face-value
  bond units, >50% divergence from proportional silver) and ghost account exclusion
  (manually curated closed accounts).
- `nna` = cumulative (inflows - outflows) from BD transactions, subject to the outflow
  caps described below.
- `synthetic_aua` = AUA attributable to RPS-injected synthetic positions. Computed from
  `synthetic_positions_index.parquet` (written by script 02 during Schwab RPS injection)
  priced against canonical_prices. When the index is absent, synthetic_aua = 0 and
  market_growth = delta(total_aua) - delta(nna).

### What Changed (commit `8a6fef07`)

`SILVER_OVERRIDE_ENABLED` set to `False` in script 05.

Previously: for every (account, date) where |gold_aua - silver_aua| / silver_aua > 20%,
all position market_values in that account were uniformly scaled so the account total
matched silver (BD's allocation report). This was introduced pre-RPS to handle accounts
where gold's units * price was unreliable (insurance annuities, donor advised funds,
missing transactions). Post-RPS, gold AUA is within 0.3% of silver at the firm level.
The override was actively clipping legitimate market appreciation -- any day where gold
grew faster than silver (which is most days, since silver is a lagging custodian snapshot),
the override pulled gold back down.

Effect on GRO: the override was the primary cause of GRO showing ~1% for 2025 instead
of the actual ~10-12%. With it disabled, total_aua now reflects true positions * prices,
and market_growth captures actual price movement.

### Publisher Alignment (commit `e419d83b`)

The publisher Lambda (`bd-portal-publisher`) produces `growth_decomposition` in
`timeseries_chart.json` -- the data behind the portal's GRO view.

Previously: publisher recomputed `market = delta(AUA) - delta(NNA)` from raw columns
in client_performance.parquet. This formula has two problems post-RPS:
1. It used silver-overridden AUA (now fixed by disabling override)
2. It conflated synthetic_correction with market growth (synthetic injection changes
   AUA without being NNA, so the residual incorrectly attributed it to market)

Now: publisher reads `market_growth` and `synthetic_correction` columns directly from
client_performance.parquet. Monthly aggregation:

```
market    = sum(market_growth) across all relationships and days in month
synthetic = sum(synthetic_correction) across all relationships and days in month
nna       = nna(month_end) - nna(prior_month_end)   [cumulative endpoint diff]
total     = market + nna + synthetic
```

The `total` should equal `aua(month_end) - aua(prior_month_end)` within floating point
tolerance. If it doesn't, that's a signal of a data integrity issue.

Graceful fallback: if the parquet was produced before GLDRST.017 and lacks the
decomposition columns, the publisher reverts to the old `delta(AUA) - delta(NNA)` formula.
This is temporary -- after the next gold rebuild with the updated script 05, the columns
will be present.

### GRO Output Schema (growth_decomposition in timeseries_chart.json)

```json
{
  "period":    "2025-06",
  "market":    12345678.90,
  "nna":       2345678.90,
  "synthetic": -456789.12,
  "total":     14234568.68
}
```

`synthetic` is new. The portal frontend currently reads only `market`, `nna`, `total`.
The `synthetic` field is available for future display (e.g., separating "organic growth"
from "RPS correction" in the GRO chart). Until DT wires it, the portal will show
`market` and `nna` as before -- but now `market` is accurate.

---

## NNA: How Net New Assets Are Calculated

NNA is computed in `lib/nna_flows.py` and consumed by script 05. The pipeline has
not changed in this session, but it is documented here for completeness since GRO
depends on it.

### Transaction Loading

Source: `silver/transactions/` (daily parquet partitions from BD SFTP).

Steps:
1. Load all partitions in parallel (128 threads)
2. Deduplicate by `transaction_id` (first pass -- removes BD re-deliveries)
3. Composite dedup by (account_id, trade_date, transaction_type, |market_value|)
   (second pass -- catches same event stored with different IDs or sign-flipped values)

### NNA Classification

Only four transaction types count as NNA:
- **Inflows:** Cash Deposit, Transfer In
- **Outflows:** Cash Withdrawal, Transfer Out

Everything else (buys, sells, dividends, rebalances, fees, corporate actions, journals)
is excluded. This is definitionally correct -- NNA measures external cash movement into
and out of the platform, not internal portfolio activity.

### NNA Exclusions (non-NNA events that masquerade as Cash/Transfer types)

Applied before classification:
- `JNL - LONG` / `JNL - SHORT` (action field) -- internal position journals between
  BD accounts, not real custodial transfers
- Description contains `TRF BTWN SCH ACCTS` -- Schwab-to-Schwab internal transfers
- Description contains `TO SEP ACCT MGR` -- operational sweeps (~$207 avg)
- Description contains `TRANSFER FUNDS TO SCHWAB BANK` -- FDIC bank sweeps

### Outflow Caps (3 layers)

These caps reduce outflows, which inflates NNA, which depresses GRO. They exist to
protect against BD data quality issues in the `market_value` field on transactions.
RPS injection corrects *position units*, not transaction dollar amounts, so these
guards are still necessary.

**Layer 1: Per-event $50M cap** (`FLOW_CAP` in nna_flows.py)
- Any single inflow or outflow event exceeding $50M is clipped to $50M
- Catches extreme garbage (e.g., $3.6B phantom withdrawal on a $2M account)
- Direction: understates both inflows and outflows, but in practice almost all
  capped events are outflows (BD's garbage is predominantly on the withdrawal side)

**Layer 2: AUA-based daily outflow cap** (script 05, `AUA_OUTFLOW_CAP_ENABLED`)
- Per relationship per day: total outflows cannot exceed prior-day total_aua
- Rationale: you cannot withdraw more than what was in the portfolio yesterday
- Post-GLDOPS.003: the AUA ceiling is now raw gold AUA (no silver override).
  Previously the ceiling was silver-overridden AUA, which was lower for divergent
  accounts, meaning the cap was tighter than it should have been.

**Layer 3: Velocity cap** (script 05, `VELOCITY_CAP_ENABLED`)
- Per relationship over trailing 90 calendar days: cumulative outflows cannot exceed
  100% of average AUA over that window
- Catches churn patterns where each daily event passes the AUA cap but cumulative
  effect produces outsized outflows
- Post-GLDOPS.003: same improvement as Layer 2 -- uses unclamped gold AUA.

### NNA Output

Script 05 produces per (date, relationship_id):
- `cum_inflows` -- cumulative inflows from inception
- `cum_outflows` -- cumulative outflows from inception
- `nna` = cum_inflows - cum_outflows

The publisher and portal consume NNA as cumulative values. Period-level NNA is
computed by endpoint differencing (e.g., monthly NNA = nna(month_end) - nna(prior_month_end)).

---

## What Still Uses Silver

After disabling the override, only one mechanism in script 05 still reads silver
allocations: **bond face-value detection**. This operates at the individual position
level for fixed_income assets only, correcting positions where gold market_value
diverges >50% from the position's proportional share of silver account AUA. This is
a narrow, targeted correction for a known pricing source bug (Yahoo returns equity
prices for bond CUSIPs where units represent face value), not a broad AUA clamp.

The AUA/velocity outflow caps reference `total_aua` from the gold computation, not
silver directly. Pre-GLDOPS.003 they indirectly consumed silver through the override;
now they use pure gold AUA.

---

## Verification Checklist (after next gold rebuild)

After DT pushes CLOUD, AE uploads scripts, and gold rebuild completes:

1. **Firm-level GRO 2025:** Should be ~10-12% (was ~1%)
   - `sum(market_growth)` for all 2025 dates / AUA at 2025-01-02
2. **Identity check:** For any month, `market + nna + synthetic` should equal
   `aua_end - aua_start` within $1 tolerance
3. **Silver override count:** Should be 0 in gold run log (confirms override is off)
4. **Outflow cap impact:** Monitor "AUA-BASED OUTFLOW CAP" and "VELOCITY CAP" lines
   in gold run log -- if the capped amounts are large relative to total NNA, that
   warrants investigation
5. **Travis Penfield AUA alignment:** Headline, asset mix sum, and tax status sum
   should all show ~$367M (from prior GLDRST.017 + canonical AUA alignment work)
