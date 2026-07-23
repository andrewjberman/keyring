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

**Delete/close when: every MDPF leg is sourced per this map, grounded, verified, and serving.**  -- `2.0.0_SA_COO`, ~14:04Z
