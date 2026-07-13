# OPAL_ASSETS -- Andrew's 14-Cohort Source Map, Grounded + Reconciled (blueprint addendum)

**Author:** 3.0.0_SA_CVO~A | **Date:** 2026-07-13 | **For:** Andrew (via MSTR) + 1.0.0_SA_CTO~B (PRD)
**Addendum to:** the 14-cohort assessment b2a17a7e3. Every source in Andrew's map located + graded in-estate
(Rule 22a; no external comms). **HEADLINE: CONFIRMED -- this is a CONVERGENCE job.** Every named source EXISTS and
runs daily except ONE (Schwab BD 08335338, the known pull-gap, 0.7.0's live leg). The build is: converge existing
daily sources into the one bucket + wire 08335338.

## Per-source grounding (Andrew's map -> the estate)

| Source (Andrew's name) | LOCATED (path/artifact) | Daily? | Notes / divergence |
|---|---|---|---|
| **TrueShares float** (DIVZ/IDVZ totals) | `etf_netassets_watch/etf_probe.py` -- Tier-1 live issuer draw, `trueshares` source_kind scrapes true-shares.com/etf/{slug} -> `s3://opal-data-etfs/silver/netassets*` + `etf_history.csv` | YES (etf_history.csv fresh 07-12 18:00; feeds WS-D2 -> mdpf etf_total_net_assets) | Matches Andrew ("I know we built that") -- CONFIRMED BUILT |
| **Pathfinder float** (PFOE/PFDE totals) | same module -- **Filepoint CSV** (`pathfinderetfs.com/assets/data/FilepointOpalCap...DailyNAV.csv`); built via MDPF_ASSETS.005 | YES daily-forward | REFINEMENT: PFOE/PFDE are NOT on the TrueShares platform (404, verified 05-18) -- the float comes via the Filepoint direct-CSV mechanism. AND: **no NAV history pre-2026-05-18** (honest-null in the served meta) -- daily-forward fine, no deep lookback |
| **Orion** (Inflection partner holdings) | Orion IS the INF platform: `orion-gold-dispatch.sh` (the daily INF gold chain, 204 estate refs) + `data/mdpf/scripts/bronze/pull_orion_model_composition.py` (ops backfill) -> WS-C feeder | YES (INF spine pipeline-complete 07-10, the last trading day) | Matches |
| **Eclipse** (Inflection Opal Models) | `s3://opal-data-inf/gold/eclipse/{date}/` | YES (partitions through 07-10, trading-daily) | Matches |
| **Cottonwood** (cot ETF holdings) | `s3://opal-data-cot/gold/positions_cube/` + `canonical/` (A_03 positions cube; DIVZ/IDVZ present per B_01/A_03 source) | YES (nightly cot chain, auto-deploys) | Matches; firm-separated (Rule 13) -- read-only grounding, the convergence leg must keep cot->bucket one-way |
| **SmartX SDD 08242234** | held CRS set `opal-data-bd/schwab/silver/{rps,rld,uln,ult,acc,trn,trn_nna}` (2024-01->present) + WS-B SmartX REST (models) | YES (2.5yr daily RPS) | Matches; covers cohorts 5-6, 9-14 |
| **Schwab BD 08335338** | **NOT HELD -- 0 hits in 21,153 files** | NO | The ONE missing source (Andrew's map agrees); 0.7.0's live pull + my assessment pending |

## Per-cohort reconciliation (Andrew's composite model vs what's wired today)

| Cohort | Andrew's composition | Today | Gap |
|---|---|---|---|
| 1-2 DIVZ/IDVZ | 49F(08335338) + Inflection(Orion) + Cottonwood(cot) + TrueShares float | float DAILY (WS-D2); inflection holdings DAILY (etf_decomposition); **cot holdings exist in cot gold but NOT folded**; 49F holdings: held RPS(08242234) via avgcap side-recon, not folded | fold cot + 49F into the composite (G4-extended); resolve D1 below |
| 3-4 PFOE/PFDE | same, Pathfinder float | float DAILY since 05-18 (Filepoint); partner folds same as above | same |
| 5-6 SMAs | SmartX 08242234 | DAILY in mdpf by_model (cohort_class=sma) -- subject to the 49F roll-forward staleness (G1) | G1 |
| 7 Inflection Models | Eclipse | DAILY (eclipse partitions + WS-C) | none (SOLID) |
| 8 49F Schwab | **Schwab BD 08335338 (SDD)** | NOT PULLED (the silent gap; G6 cohort-8 will alarm daily until wired) | G2/G3 |
| 9 49F SmartX | SmartX 08242234 (SDD) | DAILY (WS-B REST + held RPS), subject to G1 staleness | G1 |
| 10-14 49F models | SmartX 08242234, "already daily" | DAILY in mdpf by_model -- **but currently rolled-forward-stale since 07-06 (G1)** | G1 -- Andrew's "already daily" is TRUE at the source and STALE at the served rollup |

## Divergences from Andrew's map (flag, not adjudicate)

- **D1 (the one real attribution question): 49F ETF holdings.** Andrew maps them to Schwab BD **08335338**. But the
  HELD 08242234 RPS book already carries 49F DIVZ positions -- avgcap measures them there (the B_01-cited "49F holds
  ~$153M DIVZ" reads from the 08242234-xref universe). So 49F ETF positions either SPAN both masters or attribute to
  08242234. **The 08335338 pull resolves this empirically** -- until then the composite's 49F-ETF leg should read
  BOTH (dedup by account), not assume one.
- **D2: PFOE/PFDE float has no pre-2026-05-18 history** (Filepoint serves no NAV history) -- daily-forward is solid;
  any lookback ambition for cohorts 3-4's float leg is capped at 05-18.
- **D3: Andrew's "already daily" for cohorts 10-14 is true at the SOURCE (SmartX) and currently false at the SERVED
  rollup** (the G1 roll-forward-stale since 07-06) -- reconciled: G1 is a freshness repair, not a new source.

## Net for CTO~B's PRD

CONVERGENCE JOB CONFIRMED: 6 of 7 sources exist + run daily. The build = (a) the one-bucket convergence (G5: fold
float + inflection + cot + 49F ETF legs + per-cohort freshness G6 [already building]), (b) the G1 freshness repair,
(c) the ONE new source (08335338 pull, G2/G3 -- 0.7.0 live). Composite-ETF cohorts need the D1 both-masters
resolution. Everything else is wiring, not discovery.
