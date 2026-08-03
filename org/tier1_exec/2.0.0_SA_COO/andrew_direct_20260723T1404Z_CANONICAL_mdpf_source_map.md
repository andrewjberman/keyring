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

## FULL-BACKFILL DIRECTIVE -- ALL CHANNELS + GLOBAL @~16:0xZ (Andrew-direct)
**VERBATIM:** "Ok I think we got the conclusion here correct. Let's make sure that we have full backfill for all
channels properly in the gold DDB, for 49 Inflection and Cottonwood, as well as Global Aggregate rows."
**=> EXPANDS the 49-leg backfill dispatch (CTO @142139Z) to ALL FOUR CHANNELS in the gold DDB opal-assets-daily-aua,**
full lookback, per this source map + the accepted silver-sourced method (custody fact_rps_s2 C2 + model
fact_model_aum_daily closing_equity; the analog per firm). SCOPE + the load-bearing constraints:
- **49Financial:** custody fact_rps_s2 C2 to 2024-05-24 (541 partitions) / model fact_model_aum_daily to inception
  2021-09-02. Validated (variance verdict, new method accepted).
- **Inflection:** orion (total) + eclipse (model) -- DS to GROUND the real source depth (do not assume a floor).
- **>> COTTONWOOD -- BINDING CONSTRAINT (Andrew-direct, LD prior):** COT is MID-MIGRATION into Black Diamond, so
  "full backfill" = whatever the blackdiamond source ACTUALLY holds, honest-absent before it. **NO synthesized rows,
  NO frozen backfill, NO HARDCODED SERIES START; the series must extend backward ON ITS OWN as the migration lands
  more history.** Anything that writes a value where real data will later arrive is a self-authored future
  contradiction. COT depth is NOT a ceiling and NOT a defect -- it is a migration in progress.
- **Global Aggregate rows:** business-logic sum per date (49-full fee_scope=full + INF-model + COT-model), with
  HONEST-ABSENT / LABELED constituents where one is missing -- the established pattern (global[2024-11-01] ==
  49custody+INFmodel == $795,389,602.69, cottonwood=absent). NO silent carry, NO fabrication (YANG_SITTW).
**SEQUENCING (serve still HELD):** DS per-channel derivation contracts -> 0.7.0 backfill (CTO's 6 conditions +
C2-tie control, per channel) -> CTO gate -> COO per-date byte-verify ACROSS CHANNELS (positive control per channel;
49[d]==silver, INF[d]==silver, COT[d]==blackdiamond-as-far-as-it-reaches, Global[d]==sum-of-present-legs) -> co-sign
-> DE renders -> CTO fires -> DT promotes. Routed to CTO (binds+coordinates) + 0.7.0 (executor, COT constraint
first-hand) + DS (contracts) @~16:0xZ.

## CONVERGENCE-WHY GROUNDED @160049Z (DS, Andrew-dispatched; delivered to Andrew direct, record copy to COO)
The two curves never measured the same thing: LEGACY = "what we knew on day D" (monthly-statement roll-forward,
made append-only/immutable after the 2026-01-21 retroactive-revision fix -- as-known-then values FROZEN by design);
NEW = "what SmartX retrospectively says D was worth" (daily closing_equity). Gap = information-lag x growth-rate.
DS's MEASURED decomposition of the pre-2026 ~12.6pt mean shortfall (sourced: SMARTX_BIBLE.md, CANONICAL_DATA_LOGIC.md
sec3, FIX_RETROACTIVE_AUM_SMOOTHING.md): (1) statement staleness ~3pt (re-align to prior month-end: ratio 0.874->0.904);
(2) DOMINANT ~10pt = the invisible newly-funded cohort -- legacy was NOT missing accounts (counted MORE than survive
today, 3,246 vs 2,962 @2025-01-15) but an intramonth-funded account carried $0 until its first month-end CSV; in the
$437M->$1.4B/20mo hyper-growth window that cohort was ~10% of the book, and the +41% peak (Jan-Feb 2025) sits exactly
there. Collapses to zero at the frontier BY CONSTRUCTION (append-only points now written at T-1 freshness). IMPLICATION:
the legacy is a valid as-known-then AUDIT ledger but structurally understates every fast-growth period as a
market-value history -- confirming Andrew's "old method was inexact" is a LAG, not an error. COO independently
confirmed the frontier tie (-0.09%) + the era-boundary collapse earlier; the ~3/~10pt split is DS's measured analysis.
**CRITICAL PATH MOVING:** DS handed 0.7.0 the 49 C2 derivation contract @160023Z. Expanded scope (all channels) =>
DS now owes INF/COT/Global derivation contracts next (routed @160159Z).

## DISPLAY-BASIS PRINCIPLE @~16:0xZ (Andrew-direct) -- resolves the D1 value-semantics
**VERBATIM:** "Yeah we dont care about 'as known at the time' we care about absolute reality."
**=> The MDPF display basis is ABSOLUTE REALITY (the retrospective true daily value), NOT the as-known-then ledger.**
This RESOLVES DS's open D1 value-semantics in spirit: closing_equity is the right field because it IS the retrospective
daily market value; the frontier tie (-0.09% where the legacy is real) already corroborates closing_equity == the real
value. GENERALIZES to ALL channels (every leg shows the true daily value, not an as-known-then estimate). CONSISTENT
with the COT no-synthesize rule: absolute reality = show the real value WHERE THE SOURCE HAS IT, honest-absent where it
doesn't -- never fabricate reality into a period a source hasn't reached (absolute-reality + YANG_SITTW are one
discipline). The legacy as-known-then series is a valid audit ledger but is NOT the display basis. Directed to CTO to
bind the FORMAL D1 value-semantics ruling (COO relays the principle; CTO binds; DS confirms closing_equity IS the field).

## SOURCE DEPTHS CONFIRMED @161643Z (DS, Andrew's ask) + COO BYTE-VERIFIED @~16:17Z
Per-leg real coverage (COO independently spot-verified the starred ones against live S3 listings):
- 49F custody 2024-05-24+ (541, gaps=0) / 49F model to inception **2021-09-02** (prior grounding).
- **INF total (orion)** s3://opal-data-assets/orion/inflection/silver/fact_assets/: **2020-04-28..2026-07-23, n=2,278, ZERO gaps** [*COO-verified: earliest 2020-04-28, count 2278*] -- deepest channel.
- **INF model (eclipse)** fact_portfolios_full: **launched 2026-05-15** (STRUCTURAL start, no Opal models before), first nonzero 2026-05-18; trading-axis 46 -> 40 covered + 6 NAMED gaps (05-21,06-01,07-01,07-13,07-14,07-15).
- COT total (blackdiamond fact_holdings): 2026-06-09+, n=35, trading-complete (BD DataMining ~T+1; unpriced=honest-absent never $0).
- **COT model (rebalance fact_model_*)**: **2026-07-21+, n=3** [*COO-verified: exactly 07-21/22/23*] -- migration-in-progress; interpolated band (labeled) behind it, self-extending under 0.7.0 run-time enumeration.
**INF-MODEL LEGACY-ESTIMATE CHECK (COO, proactive): CLEAN.** Served inflection.model_aua == $0.0 at 2024-11-01 / 2025-06-02 / 2026-05-14 / 2026-05-15; earliest nonzero **2026-05-18**. So NO SmartX-style as-known-then estimate hides in INF's deep history -- pre-launch is a true structural zero, and the pre-series control's "49custody+INFmodel" had INFmodel=0 (Global[2024-11-01]=49custody alone $795,389,602.69).
**GLOBAL COMPOSITION IMPLICATION (COO read):** Global = 49-full + INF-model + COT-model, and the two MODEL programs are recent -> going back: all-three at frontier -> 49+INF from 2026-05-18 -> **49's full book ALONE through deep 2024-2025**. Not missing data -- when each firm's model program began. legs_present label makes every row say which firms it contains.
**ALIGNMENT (CTO @161803Z, awareness):** Andrew stated a broader end-state to CTO directly = server-side JSON generation off the gold DDB for the FULL /portfolios surface (radial+bell+AUA-trend+period-end, all 4 splits). CTO bound+routed (DE enumerate read-surface -> DS generation contracts -> generator ownership later); the 4-channel backfill is the FOUNDATION, proceeds unchanged; COO per-date counter-sign extends to the generated artifacts. No COO action; serve hold unchanged.

## 49 SOURCING BOUNDARY -- 0824 vs 0833 CONFIRMED @~17:45Z (Andrew-direct + COO decision-prompt)
Andrew-direct: "we're moving to do everything for 49 off schwab 0833 and BD will completely not matter for 49
Financial aside from the METATABLE for advisor/fee info" + "we dont need certified_aua moving forward, that is
going to be deprecated." COO confirmed the SCOPE via decision-prompt -- **Andrew ruled: MDPF STAYS ON 0824.**
=> **MDPF (Model Portfolios) 49 leg = Schwab 08242234 (0824), UNCHANGED** (per his earlier 08242234 ruling; the
live walk continues, no repoint). **0833 (08335338) is the consolidation for the 49 FIRM-AUA / ADVISOR-INTELLIGENCE
side** (replacing the BD-sourced certified_aua). **BD -> metatable-only for 49 (advisor/fee info); certified_aua
DEPRECATED.** This is CONSISTENT with the 0824/0833 business-purpose split (each surface on its OWN master), NOT a
substitution -- so the never-substitute gate is honored. **COO actions taken:** BD-vendor allocations-stall question
DROPPED (moot); certified_aua freeze + 08-01 cliff escalation WITHDRAWN (deprecating; interim exposure only if the
0833 migration lands after 08-01 -- flagged once to Andrew, not re-raised). ADVI-49->0833 migration is a SEPARATE
workstream (not MDPF, not tonight's chain).

## COUNTER-SIGN EARNED ITS KEEP @~17:46Z: COO finding + 0.7.0 sweep = one CLASS fix (@8a330f9d4)
COO's ultra_short_term circular-residue finding MERGED with 0.7.0's independent sweep finding (same architecture,
opposite directions): (1) pre-inception model legs now DISCOVERED-INCEPTION structural-zeros (no by_model text on
ANY path); (2) 0.7.0's sweep caught that the override only emitted where a SERVED body existed -> **132 of 541
custody dates were value-ABSENT (incl. 3 of 7 contract pins) + the deep model history was missing entirely** --
exactly the walls COO's Tier-B would have hit. FIX: skeleton rows from the cohort spec on no-body dates (every
re-sourced cohort emits on every axis date). FULL RE-WALK running (~6min, idempotent). partial_2_of_3 @2024-11-01
CONFIRMED as DS's design (known-zero = presence). COO re-verifies Tier-A/B against the RE-WALKED table, not the in-flight one.

## >>> COUNTER-SIGN STOPPED THE LINE @~18:0xZ -- SERVE-BLOCKING COT-MODEL DEFECT (source-confirmed) <<<
COO full co-sign against the re-walked table caught it in the SERVED WINDOW, PRE-SERVE: **cottonwood_bd_models @07-22
= $458,178,642.78 = the TOTAL HOLDINGS (~~$458,189,558.77~~ [SUPERSEDED 2026-08-03 @387fa87c90 by 0.4.0_DS per ADHOC.0722-tie TO: the figure is the naive double-counted sum, +$205,070.77 relationship-grain; collapsed truth $457,984,488.00 -- the COMPARISON this line makes still holds, the anchor value itself must not be cited as verified]), not the model overlay (~$124M).** Global inflated to
**$2,285,478,797.47 (~$2.29B)** -- the entire +$333.8M jump from ~$1.95B is this ONE leg. MECHANISM (source-confirmed,
I read the DDB source_field + both parquets): the emitter's `fact_model_assignment JOIN fact_holdings on
externalId==AccountID` was UNFILTERED -- all 911 rebalancer accounts (incl. an "Implementation Default Account"),
summing to ~total. COO filter-test proved NO assignment flag discriminates the subset (is_managed/discretionary/
is_in_rebalance_group/is_sma all uniformly False; can_rebalance=$176M). **CTO RULED THE FIX (@180247Z):** DS states the
co-signed PAIR's model-overlay predicate at source (it already yields $124.4M -- the definition exists, the emitter
didn't inherit it); 0.7.0 transplants it VERBATIM (one-derivation law); **$124,376,009.73 is the CONTROL not the
target** (bend-to-target guard, same class as the afternoon's bend-to-$1.64B). Mutants: Implementation Default excluded
+ an is_managed=False account. Blast radius ~2 dates (COT overlay 07-21+); COT-model + global rows re-derive, 49F/INF
untouched. **THE SYSTEM WORKED: wrong number lived ~40min in a STAGING table, caught by the bytes-first counter-sign
before any serve; the served Global will be the ~$1.95B-class number Andrew's arithmetic predicted.** Line resumes at
COO clean re-verify (COT leg to the cent + full grid). Serve fires on COO counter-sign + DE renders, unchanged.
**SERVED-WINDOW OTHERWISE CLEAN (pre-COT-catch):** A2 no-circular PASS 4 dates; C2 pin ties to the cent
(49f_schwab_custody @07-17 = $1,665,338,126.76); 132-missing-dates fix confirmed (seams populated).

**Delete/close when: every MDPF leg (49/INF/COT + Global) is full-lookback backfilled in the gold DDB per this map, per-date verified, and serving.**  -- `2.0.0_SA_COO`, updated ~18:0xZ (COT-model serve-block caught + fix ruled)
