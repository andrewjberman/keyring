# ETFS_RIVALS -- DECOMPOSITION, ROUND 7 (ENRICHMENT): the sweep runs the AI step itself, runs carry their trigger, the census reads the rankings' classification, one name per security, and the page-walk remainder

```json
{
 "project": "ETFS_RIVALS",
 "round": 7,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.13 @b69262724d; ADMITTED)",
 "prd_version": "v0.13",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round6.md@94f682c868 (section 3, ENRICHMENT LIST)",
 "author": "2.0.0_SA_COO~RV",
 "cells": 8,
 "chains": 4,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "round6_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round6.md"
}
```

**Issuer:** `2.0.0_SA_COO~RV`, 2026-10-02 ~21:3xZ, FULL.
**Source:**
- The round-6 analysis section 3 (CTO~Z msg 28735). It lists six items: C-S24 (the lead), provenance, page-size headroom,
  the census's 33 GICS rows, the name tie-break, and the RFW remainder.
- The RFW register graded against the served page (rv-publish-1002r6, 21:0xZ): 14 REALIZED, 4 SUPERSEDED by Andrew's
  layout word, 3 PENDING-TRIGGER, 11 NOT-REALIZED, 1 out of scope. The 11 are cut below by write set.

## Issuer rulings at this cut

1. **The standing L5 rule from round 7 (CTO ruling 4):** every outcome that claims production names its ORGANIC
   trigger, and that trigger's own invocation is its evidence. A deliberate fire is the positive control only. Each cell
   below carries an `Organic trigger:` line.
2. **Analysis item 3 (page size) is REALIZED by existing code; no cell.** Check `round7/checks/ps-1.AC1.py` PASSES at base:
   - a heavy day refuses with nothing written and the prior page kept (`publish_page.py:719-721`);
   - a medium day publishes without holding dialogs (`render.py:1433-1443`).
   The served page is 1,833,385 B against the 2,097,152 B cap.
3. **Cut by write set (C10):**
   - `~1` sa-1 -> pv-1 -> cu-1: `sweep.py`, `ai_stage.py`, `publish_page.py`, the sweep schedule in `gen_policies.py` and
     its outputs;
   - `~2` rd-1: `render.py`;
   - `~3` nt-1 -> nm-2: the name maps in `gold_holding_contribution.py` and `gold_buying_trend.py`, `names.py`,
     `enrichment_bloomberg.py`;
   - `~4` cg-1 -> cs-1: `gold_input_census.py`.
4. **Workers never call a vendor, write S3, deploy or run Terraform.** The issuer's acts, each under its own pair:
   - the deploy with the regenerated schedule;
   - the deliberate invoke of the SWEEP Lambda with its own schedule payload (sa-1's positive control);
   - I-1 (W4-S9);
   - I-2 (the backfills: D12, D13);
   - the G5 replay (D10's residue).
5. **Acceptance (CTO ruling 2):** the organic 2026-10-05 09:00 ET sweep, with no seat act, writes that day's account and
   republishes.

## Rulings reaching every cell

Rounds 1-6's rulings stand (`ETFS_RIVALS_DECOMP.round{1..6}.md`). CALL 5 holds: one AI run per page day; a FAIL is shown,
never re-rolled.

## 3. THE CELLS

### `RIV-sa-1` -- the sweep runs the AI step itself, with a deadline, then republishes (C-S24; RFW-D08)
- `sweep.handler_entry` runs the AI step after `run_dag`, or after the `only` stages when they include publish-page. It runs
  only when `RIVALFUNDS_AI_ENABLE == "1"` and the day already holds a publish-page marker.
- Today `sweep.py:469-472` skips the publish whenever the marker exists, and the gateless morning publish always writes it,
  so no scheduled path reaches the AI stage.
- If the step ran (OK or FAILED), the sweep republishes through `publish_page.handler_entry` under a new batch id, passing
  the result as `event["ai_run"]`. publish-page makes NO AI call: it records `ai_run` as
  `a1_produced.research_hypotheses_run` `{status, reason, run_id, run_path}`.
- **Deadline:** event field `ai_deadline_s` (passed through by `trigger_event`), default constant `sweep.AI_DEADLINE_S`. The
  step never runs past the Lambda's remaining time minus `MARGIN_MS`. On an overrun:
  - no research_hypotheses object is written, now or later (no background writer);
  - the result is `{"status": "FAILED", "reason": "...deadline..."}`;
  - the page shows the failure.
- **One run per page day (CALL 5), OK or FAILED:** a later sweep makes no AI call. The cell records the attempt where the
  address builder says.
- **Gate unset:** the sweep writes nothing extra and does not republish.
- `ai_stage.run_for_day(sink_spec, day, run_path="ad_hoc", deadline_s=None, **kw)`.
- **Organic trigger:** the EventBridge sweep schedule (`etfs-rivalfunds-daily-lambda`, 09:00 ET trading days). Its
  invocation on 2026-10-05 is the acceptance.

### `RIV-pv-1` -- a run carries its trigger: `run_path` "scheduled" only from the schedule (CTO ruling 3)
- The sweep schedule's input in `gen_policies.py` gains `"run_path": "scheduled"`, regenerated into
  `generated.auto.tfvars.json`.
- The sweep stamps "scheduled" only for an event carrying that value and no `only`. Every other event stamps "ad_hoc":
  an `only` fire, or a hand-made event.
- `run_path` goes into each account row's `input_manifest` and into `research_hypotheses_run`.
- A seat replaying the schedule payload verbatim still stamps "scheduled", and the docstring says so.
- **Organic trigger:** the same schedule. Its payload is the evidence.

### `RIV-cu-1` -- the sweep continues every open G1 cursor (W4-S9, continuation half; found at I-1's measurement)
- Round 5 bounded a long G1 batch: `_budget_s` 600 s returns PARTIAL with a cursor and NO G1 marker, and `run_gold_chain`
  re-runs G1 once inside one invocation.
- The issuer's I-1 measurement (C:/tmp/r7i1/, batch d5-gqgu-03: 60 dates, PARTIAL, PARTIAL, OK) found that NOTHING continues an
  open cursor across invocations. The silver trigger fires only on a new marker, and the 09:00 ET sweep walks only its own
  page day, so a PARTIAL batch stays incomplete until a seat re-invokes it.
- The sweep continues every OPEN G1 cursor (a cursor object without its G1 marker), within a bounded lookback the cell
  states and within its budget. A cursor older than the lookback is reported in the sweep's detail, never silently dropped.
  With no open cursor, the sweep behaves exactly as today.
- **Organic trigger:** the 09:00 ET sweep schedule. A PARTIAL batch completes on the next scheduled sweep.

### `RIV-rd-1` -- the page-walk remainder in render.py (RFW-D12, U09, U13, U14, U16)
- **The name-map shadow (found at the cut):** a second `def _render_page` at `render.py:1457` replaces the wrapper at :1446.
  The wrapper fills `_NAMES`, so `render_page` never fills it. U14 (one display name per security) has been dead since
  95af466e67. Rename the body and keep the wrapper.
- D12: a buying-trend line built from ONE window reads "Single trade", not BET or TILT (`render.py` ~:970).
- U09: the account text's stored reading keys display as labels. That includes multi-word keys and bare family names
  (`fear_greed`, `"middle" east oil`; the label regex ~:1072). The face's vintage line shows no raw table names.
- U13: the holdings table reads plain words ("UNRESOLVED" ~:436, identifier types, "source policy ..." ~:399), each with
  its code in a title tooltip, as the trade log does.
- U14: the holdings-table name (~:438) reads through the page's one name map (no case-only clashes).
- U16: the buying trend's no-sector row becomes a footnote with its share, like the rankings' data-unclassified-share.
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep publish. The page they write is the evidence.

### `RIV-nt-1` -- one deterministic name pick (analysis item 5; RFW-U14 producer half)
- The newest-name map in `identity_maps` (`gold_holding_contribution.py` ~:140-165) and its use in `gold_buying_trend.py`
  (~:76-84) take `display_name(sorted(set(candidates)))` over the names on the key's newest named date. Older dates never
  compete. The row order changes nothing (today it moves 12 + 2 cells; TSM flips between two names).
- `hc.build` and `bt.build` keep their signatures, and a fund's own name still comes first in holding_contribution.
- **Organic trigger:** the A1 producers in the 07:00 ET publish.

### `RIV-nm-2` -- the CUSIP-keyed G4 request asks for a name (RFW-D11)
- The OFFLINE G4 plan (`enrichment_bloomberg.py` ~:103-114) requests a security-name field, and G4 rows carry it.
- The producers' name candidates include the G4 name, so `names.display_name` prefers it over a 30-character cut (IDVZ's
  "International Container Termin").
- The 2026-10-05 vehicle run does NOT fix these without this cell: the IDVZ CUSIP lines share no key with any named line.
- **Organic trigger:** the vehicle's 08:03 ET enrichment step. Its G4 object is the evidence.

### `RIV-cg-1` -- the census reads the rankings' GICS classification (analysis item 4; RFW-D14)
- All 33 understated rows (ETFT 9, PCLG 11, TSEL 9, WCMG 4) are a G4 DATE-SCOPE difference:
  - the census matches G4 on security_id plus the as-of date in the as-of partition only (`gold_input_census.py:87`, `:102`);
  - the rankings match G4's sector on security_id across their window (`gold_holding_contribution.py:636-639`,
    `_prices` `:217-228`).
- A second difference is latent: the census's other_fund rule matches the exact key within 14 days (`:56`, `:141`); the
  rankings' `_cross_sectors` (`:232-264`) match any shared identifier over the year to date.
- A GICS row the rankings classify reads `arrived`, or `covered_by_fallback` with `fallback` "other_fund" or a value
  beginning "g4" (e.g. "g4_prior"). `missing` only where the rankings say Unclassified. The rankings producer is unchanged.
- **Organic trigger:** the census producer in the 07:00 ET publish.

### `RIV-cs-1` -- the census and the header agree on freshness (RFW-D02)
- The header says "13 of 13 funds current" (a 1-trading-day allowance), while the census says "9 of 13 arrived, 4 missing"
  (the exact date) (`gold_input_census.py:109-113` against `render.py:508-510`).
- A holdings report inside the allowance reads covered, consistent with ic-2's states. A report outside it stays missing.
- **Organic trigger:** the census producer in the 07:00 ET publish.

## ISSUER ACTS (no worker; each under its own pair)

- **I-1 (W4-S9, CTO ruling 5, owed now):** one deliberate marker batch above 45 report dates (d5-gqgu-03, 60 dates)
  against the deployed canonical-shape Lambda; it must end PARTIAL-and-continued, never timed out. Measured: G1 writes 0;
  the publish leg rewrites the 10-01 page, so it runs under its own pair (COO half `round7/NEVER_WIDEN_HALF_COO_I1_W4S9_DISARM.md`).
- **The round-7 deploy:** five Lambdas + the regenerated schedule; then the deliberate SWEEP invoke with its own schedule
  payload (sa-1's positive control). The organic 2026-10-05 09:00 ET sweep is the acceptance.
- **I-2:** the IDVZ/PFOE trend from inception (D12) and the ACWI/IWM benchmarks (D13, the v0.8 leg's gate).
- **The G5 replay** for D10's six n/a cells in the 09-25 -> 09-30 windows. Otherwise they roll off around 2026-10-08.
- **Pending a trigger:** D04 and D05 (the 2026-10-05 vehicle run with the 601-security plan).
- **Out of scope:** D07 (upstream arrival: the TrueShares layout break is Andrew's/CRO~RV's call) and U19 (Andrew's
  signed-in walk).

## 4. DEPENDENCY EDGES AND CHAINS

| chain | cells (serial) | writes |
|---|---|---|
| `~1` | sa-1 -> pv-1 -> cu-1 | `sweep.py`, `ai_stage.py`, `publish_page.py`, `infra/aws/terraform/etfs-rivalfunds/{gen_policies.py, generated.auto.tfvars.json}` |
| `~2` | rd-1 | `render.py` |
| `~3` | nt-1 -> nm-2 | `gold_holding_contribution.py`, `gold_buying_trend.py`, `names.py`, `enrichment_bloomberg.py` |
| `~4` | cg-1 -> cs-1 | `gold_input_census.py` |

## 5. BATTERY

`deliverables/2.0.0_SA_COO~RV/round7/checks/`, dry-run at the base. Each order's face names its checks; the issuance commit
carries every base line.
