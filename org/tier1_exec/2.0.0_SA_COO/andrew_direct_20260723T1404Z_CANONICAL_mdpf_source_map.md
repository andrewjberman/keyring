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

## SMARTX MODEL-LEG FEASIBILITY -- RESOLVED **YES** (DS grounded @152655Z/152742Z; COO BYTE-VERIFIED @~15:27Z)
**Andrew's crux (VERBATIM ~15:2xZ):** "The real question is if we can generate reliable daily model values from
SmartX going all the way back to whatever the start values we have for SmartX from opal-data-assets/smartx/
bucket... That is also why... the DDB being representative of the portal data (backwards)... because we were
concerned about not being able to reproduce that data."
**VERDICT: YES -- reliable daily per-model values ARE reproducible from `opal-data-assets/smartx/` back to each
model's SmartX inception. THE BACKWARDS DDB FLOW IS UNNECESSARY; normal silver->gold-DDB->portal works for BOTH legs.**
- **The "~10 dates" was an AXIS confusion (VERIFICATION-LAW-6):** `smartx/` pull-start is 2026-07-14 (10 run-date
  partitions), BUT each daily pull re-delivers each model's FULL per-day series; the model history lives in the
  `day` COLUMN inside each partition, not across run_date partitions.
- **COO BYTE-VERIFIED (not transcribed):** read `smartx/platform/silver/fact_model_aum_daily/date=2026-07-23/data.parquet`
  directly -- `day` range **2021-09-02 -> 2026-07-22, 1,226 distinct days, 4,326 rows**. Confirms DS's deepest model
  (ea6cbb22, 1,226 days from 2021-09-02) to the day. 5-core roster from 2024-08..11 (why the served axis starts 2024-11-01).
- **STAGED trio's model leg IS silver-sourced (DS @152742Z):** reads `fact_model_aum_daily` latest partition via
  `dim_mdpf_aggregate_aua_timeseries.py:309 load_aum_daily` @9bd23d904 (the F1 law) -- never the served aggregate,
  the DDB, or interpolation. So BOTH staged legs are silver-sourced (custody = `fact_rps_s2` C2; model = `fact_model_aum_daily`).
- **RELIABILITY CONTROL (run, not assumed):** 07-14 pull vs 07-23 pull on 4,270 common (model,day) cells -> 4
  restated (0.094%), ALL on the 07-14 pull's own T-1 frontier (2026-07-13) settling in the next pull; SETTLED
  history = ZERO restatements across the 9-day vintage gap.
- **HONEST BOUNDARIES (named):** (a) per-model AUM (closing_equity) reaches inception; per-ACCOUNT/holdings detail
  exists only from 07-14 forward (the sweep snapshots); (b) pre-inception days are the model's own start, not a
  gap; (c) pre-07-14 we hold no banked vintages -> non-restatement before then rests on the vendor series (from
  07-14 we detect drift daily; the control above IS that instrument, and the frontier-day settle is its signature).
- **UNBLOCKS:** 0.7.0's emitter re-source + full-lookback backfill -- both legs are silver-reproducible (custody
  `fact_rps_s2` to 2024-05-24, 541 partitions; model `fact_model_aum_daily` to inception 2021-09-02). Feasibility
  is no longer an open question; sequencing is.

## C2 RULING SUPERSEDES the 14:13Z "$1.64B repoint" GROUNDED RESULT above
The 14:13Z conclusion ("repoint 49-total to the DDB `49f_schwab_custody` $1,644,993,954.34 -> Global ~$1.9B") is
**SUPERSEDED by Andrew's C2 ruling (~15:12Z, "We want to keep cash, C2").** The DDB custody $1.64B is the LEGACY
positions-EX-cash (07-15-stale) quantity; **C2 = `fact_rps_s2.net_mv_plus_cash` (cash IN) = $1,689,302,889.53
@07-22 frontier / $1,665,338,126.76 @07-17 pin.** Current Global (C2) = **$1,951,676,164.42 (~$1.95B)** @07-22;
~$1.93B @07-17 pin. Same account (08242234), cash-in quantity. DS C2 reprocess @9bd23d904 = ZERO per-date churn
vs the prior staged trio (it was already `net_mv_plus_cash`). The "(BD)" tag is a meaningless display literal
(my "BD-priced" was a mislabel, retracted). Fee-basis ties to the cent (49F $1,689,302,889.53 + INF
$137,997,265.16 + COT $124,376,009.73 = $1,951,676,164.42).

## SERVE-SEQUENCING RULED @~15:4xZ (Andrew, via COO decision-prompt) = **HOLD FOR FULL BACKFILL**
Fork presented (SmartX feasibility resolved, staged trio served-window-complete): (1) serve-now-on-served-window
+ backfill behind w/ a byte-tie conformance proof [CTO+COO rec], vs (2) hold serve until the full-lookback
backfill lands + plumbing conformant end-to-end. **Andrew chose (2) HOLD** -- consistent with "full lookback as
a precursor / correct + complete over fast." Serve stays HARD-HELD through the backfill. CTO's serve-now rec +
the conformance-condition (first DDB-sourced rebuild must byte-tie the served artifact on the served window) is
recorded @153805Z and carries forward as the backfill's landing proof regardless.

## VARIANCE ANALYSIS ORDERED @~15:4xZ (Andrew-direct) -> DS (@ this turn), CC CTO -- GATES the backfill go
**VERBATIM:** "What id like to see is have DS do a variance analysis on the newly-produced smartx model backfill
overlaid with the backfill from smartx legacy method that is currently displaying so we can identify if there is
any obvious disparity." **TASK:** overlay NEW (silver-sourced fact_model_aum_daily day-series, F1/load_aum_daily
@9bd23d904) vs LEGACY (the method ACTUALLY serving the live portal model trend -- DS to identify against the
SERVED artifact, name source+commit; if same producer, disparity=0 by construction = the answer), per-date over
the common trading-day range, abs+% deltas per-date + per-model + aggregate model line, VERDICT on any obvious
disparity w/ grounded mechanism if material. Diagnostic, not a serve step. Result -> COO -> Andrew.

## VARIANCE VERDICT CONFIRMED + NEW METHOD **ACCEPTED** @~15:5xZ (Andrew)
DS delivered @154510Z (overlay committed @720433fb3). COO independently reproduced the load-bearing pieces (NOT transcribed):
- **Legacy (served) side byte-confirmed** (read opal-data-portal-v2/platinum/mdpf/aggregate_aua_timeseries.json):
  49financial model line @2025-01-30 = **$458,760,247.71** (DS's max-divergence served value, EXACT); model_aua ==
  5-core sum to the cent; `meta.backfill_methods` DECLARES the 3 rederived-estimate eras (029_v0_9_rps_calibrated /
  031_v0_9_2024depth / process_derived_v0_8) -- the legacy display SELF-DECLARES as a multi-era estimate.
- **FRONTIER TIE reproduced from the SOURCE parquet** (fact_model_aum_daily day=2026-07-17): new sum(closing_equity)
  = **$1,420,741,829.72** vs served 5-core+SMA **$1,422,045,203.59** = **-$1,303,373.87 (-0.09%)**, matching DS's
  -$1,303,699.58 within $326. Where the legacy is REAL (05-18+), the new method TIES it -> the new method is NOT
  mis-parsing/mis-calibrating the source.
- The +41.5% deep-history divergence ($458.76M served vs $649.13M new @2025-01-30) is the LEGACY ESTIMATE
  understating; divergence collapses EXACTLY at the legacy's own estimate->real boundary.
**ANDREW VERBATIM (~15:5xZ):** "No the new method is acceptable, I think it is more likely the old method was inexact,
I'm having DS analyze why the old and new methods converge, and having them read over the old methodology docs to try
and understand the historical divergence (as that divergence converged to being very close in more recent periods)."
**=> NEW METHOD ACCEPTED as the port target (port DIRECTION settled; serve TIMING unchanged = still HELD for full backfill).**
**FOLLOW-ON (DS, ANDREW-DISPATCHED):** analyze WHY old/new converge + read the old methodology docs to explain the
historical divergence. Result -> COO -> Andrew. **Honest boundary retained:** deep-history real values rest on the
vendor series (no 2nd independent real source pre-05-18; DS's 07-14-vs-07-23 0-restatement control = stability evidence);
closing_equity value-semantics still await Andrew's formal D1 ruling (the frontier tie corroborates the field).

**Delete/close when: every MDPF leg is sourced per this map, backfilled full-lookback, VARIANCE-VALIDATED (done, new method accepted), verified, and serving.**  -- `2.0.0_SA_COO`, updated ~15:5xZ (variance CONFIRMED + new method ACCEPTED)
