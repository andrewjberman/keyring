# ANDREW-DIRECT — CANONICAL MDPF SOURCE MAP (the source-of-truth architecture)

**Channel:** Andrew-direct to COO terminal, 2026-07-23 ~14:04Z. **THIS IS THE AUTHORITATIVE MDPF SOURCING
REFERENCE** — every MDPF leg (per firm, total + model) reads exactly these sources, from the
**`opal-data-assets` DDB GOLD LAYER**.

**VERBATIM (Andrew):** "Yes I want to reiterate the purpose of MDPF here. We want to use opal-data-assets
DDB gold layer. The source data for 49 is opal-data-assets/schwab/08242234 (for total value) and
opal-data-assets/smartx/ (for model value), the source data for Inflection is the opal-data-assets/orion/
(for total value) and /eclipse (for model value). In the case of Cottonwood, there should be
opal-data-assets/blackdiamond/ for the total holdings, and then the /blackdiamond/rebalance specific for
the model overlay."

## THE SOURCE MAP (read from opal-data-assets DDB gold layer)
| Firm | TOTAL value | MODEL value |
|---|---|---|
| **49Financial** | `opal-data-assets/schwab/08242234` | `opal-data-assets/smartx/` |
| **Inflection** | `opal-data-assets/orion/` | `opal-data-assets/eclipse` |
| **Cottonwood** | `opal-data-assets/blackdiamond/` (total holdings) | `opal-data-assets/blackdiamond/rebalance` (model overlay) |

## Reconciles the prior Andrew-directs this session
- 49 ruling ([[andrew_decision_PENDING ...49f_global_view_definition]]): 49-total = the served AUA of Schwab
  **08242234** — matches the map's 49-total source. (0824 = Model Portfolios master; NOT a 0824/0833 substitution.)
- Cottonwood basis ([[andrew_direct ...cottonwood_basis_two_source_methodology]]): "models from rebalance
  domain, values from datamining holdings" = blackdiamond (total holdings / datamining) + blackdiamond/rebalance
  (model overlay). Matches.
- Fee-basis business logic: 49 uses TOTAL (fee_scope=full, whole book), INF + COT use MODEL only — the view
  SELECTS the mapped leg per fee_scope; both legs (total + model) are sourced per the map for every firm.

## THE BUG this locates (was the $1.69B-vs-$1.62B dispute)
The staged 49 TOTAL ($1,688,831,869.52) was sourced from **`fact_rps_s2` (schwab-rps feeder / full envelope)
— the WRONG SOURCE.** The map says 49-total = `opal-data-assets/schwab/08242234` (~$1.62B-class). So the root
was NOT growth and NOT partial-vs-full — it was a **mis-sourced 49 total leg.** (The earlier $20.3M-definition
+ $23.5M-growth decomposition explained the delta between fact_rps_s2 and the legacy schwab_canonical estimate;
the ACTUAL fix is neither — it is re-sourcing 49-total to 08242234 per this map.)

## Gate / actions (serve HARD-HELD)
- DS (@140458Z): align EVERY firm/leg to the map from the DDB gold layer; ground each with the gold-layer
  key @ commit; rebuild 49-total from 08242234; confirm INF (orion/eclipse) + COT (blackdiamond/rebalance)
  already read their mapped sources; confirm all read the GOLD LAYER not a feeder/legacy path.
  Flags on 08242234: feeder-liveness (01_raw decommission-ordered 07-16) + basis-quantity labeled.
- COO re-verify: each leg == its mapped source + the Global reconciles, before co-sign.
- Methodology RECORDED: this file is the authoritative map; referenced from artifact meta + swept to every
  carrier (rides DS's basis-label churn `@189336618`).

## GROUNDED RESULT @~14:13Z (DS grounded @140926Z; COO byte-verified the DDB directly)
- **THE TABLE EXISTS:** DynamoDB `opal-assets-daily-aua` (PK=run_date/SK=cohort_id, 28 cohorts/day) = the
  consolidation-PRD gold registry. Its cohort set IS the map.
- **49-total VERIFIED byte-exact (COO read the DDB, not transcribed):** cohort `49f_schwab_custody`
  @run_date 2026-07-18 = **$1,644,993,954.34** = Andrew's $1.64B ref, byte-identical. `49f_smartx_platform`
  (49-model) = $1,397,301,724.98 present. The $1.62/$1.64/$1.69B trichotomy = three VALUATIONS of the same
  0824 account (custody series / earlier vintage / raw RPS net_mv_plus_cash envelope); the map picks the
  DDB custody series.
- **5/6 legs already map-correct;** ONE repoint = 49-total (staged read fact_rps_s2 envelope $1.69B; map
  rules the DDB custody series $1,644,993,954.34).
- **REPOINT -> Global = $1,644,993,954.34 + INF-model $137,170,028.82 (eclipse) + COT-model $124,376,009.73
  (rebalance) = $1,906,539,992.89 (~$1.9B) = Andrew's stated correct number, EXACTLY.**
- **⚠ EMITTER STALLED (COO-verified):** `opal-assets-daily-aua` latest run_date = 07-18; 07-19/21/22/23 all
  COUNT=0 -> 5 days stale. The 17:15Z emitter is stalled (same staleness class Andrew flagged AM). Revival
  routed to CTO/0.7.0 (OPAL_RUNNERS) as a SEPARATE owned fix.
- **DECISION AT ANDREW (serve gate):** (1) repoint now with honest 07-18 per-leg vintage + revive emitter
  separately [COO rec], or (2) hold serve until emitter revives + table current. DS standing by to repoint +
  re-emit the ONE churn on GO. Serve hard-held until Andrew's word.

## FULL-LOOKBACK BACKFILL PRECURSOR (Andrew-direct @~14:21Z) — serve now gated behind this
**Andrew VERBATIM:** "I should have specified when creating the gold DDB table that we put full lookback for
all relevant source data in there, even if the frontend only serves a partition. That is something we will
need to do now as a precursor." + earlier: "We definitely have history back to 2024 in 0824."
**DESIGN:** the gold DDB table (`opal-assets-daily-aua`) holds **FULL LOOKBACK for all relevant source data**;
the frontend serves the **2024-11-01+ partition** off it. The 21-run_date registry was UNDER-FILLED (emitter
ran irregularly + stalled), NOT source-limited.
**DEPTH GROUNDED (DS @142049Z, cited):** 0824 custody raws reach 2024-05-24 (silver `fact_rps_s2`, 541
partitions, zero gaps) / CRS raw to 2023-01-17 (~2.5yr). 06-12 was the emitter's run-start, not a data floor.
**THE DERIVATION SPLIT (0.7.0's design):** the DDB canonical is the **BD-priced** custody quantity — the
backfill must DERIVE that priced series per historical date from the RPS/CRS raws (NOT a row-copy); the
pricing basis at historical dates is 0.7.0/CTO's design call.
**DISPATCHED (CTO @142139Z):** backfill = 0.7.0 #1 (above S5+RF-9), under 6 conditions — load-bearing 3:
emitter's OWN code path run historically (no 2nd writer; if it can't run historically = surfaced design gap +
small deploy), idempotent upserts, and a **POSITIVE CONTROL: the backfilled series must reproduce COO's
byte-verified `49f_schwab_custody @07-18 = $1,644,993,954.34` exactly** + a month-end spot-grid. Denominators
in trading days per cohort in the completion report.
**SERVE CHAIN (unchanged shape, longer):** full-lookback backfill (0.7.0) -> DS reprocess 49 + Global trends
off full canonical -> COO per-date re-verify (49[d]==DDB[d], no silent carry) -> co-sign -> DE renders ->
CTO fires -> DT promotes. DS's 21-point staged build is INTERIM/MOOT. Serve hard-held until the full-lookback
registry lands. Andrew framing: **correct + complete over fast.**

**Delete/close when: every MDPF leg is sourced per this map, backfilled full-lookback, verified, and serving.**  -- `2.0.0_SA_COO`, ~14:22Z
