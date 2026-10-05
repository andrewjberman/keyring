# ETFS_RIVALS -- DECOMPOSITION, ROUND 9 (ENRICHMENT): the backfill made purely additive, the IDVZ/PFOE daily join, an incremental security list, AI-text links, real names for past holdings, a Bloomberg capacity budget, and the G5 drift read

```json
{
 "project": "ETFS_RIVALS",
 "round": 9,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.17 @43a5542d11; ADMITTED)",
 "prd_version": "v0.17",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round8.md@2097b5212b (section 4, ENRICHMENT LIST items 1-8)",
 "rulings": [
  "CTO~Z ruling (B) on row Z-S29 2026-10-05 16:22Z (G5 named-fund rebuild; gate file accepted)",
  "CTO~Z msg 29624 term 4 (security_universe incremental)"
 ],
 "draft_ref": "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round9/DECOMP_DRAFT.md",
 "author": "2.0.0_SA_COO~RV",
 "cells": 7,
 "chains": 6,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "round8_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round8.md"
}
```

## Rectangle (the round-8 analysis section 4, 8 items)

| item | cell | chain | risk |
|---|---|---|---|
| 1 G5 named-fund rebuild (then Step B, an issuer act) | RIV-nf-1 | ~1 | SERVED |
| 2 IDVZ/PFOE daily join via a gate file | RIV-gf-1 | ~2 | SERVED |
| 3 security_universe incremental | RIV-su-2 | ~3 | SERVED |
| 4 C-S35 AI-text links | RIV-ln-1 | ~4 | SERVED |
| 6 S24 capacity budget | RIV-cb-1 | ~5 (1 of 2) | SERVED |
| 5 C-S36 ticker-form names | RIV-nm-3 | ~5 (2 of 2; asks cb-1's budget) | SERVED |
| 7 G5 drift classification (read) | RIV-gd-1 | ~6 | LOCAL |
| 8 triage of the 8 stale rows | issuer act, done: deliverables/2.0.0_SA_COO~RV/round9/STALE_ROWS_TRIAGE.md @f70677780a | - | - |

Edges: RIV-cb-1 -> RIV-nm-3 (nm-3's production fetch asks bbg_budget). Write sets are disjoint; the shared-file hookups are the issuer's at the merge: collector_bloomberg import copies `rebuild_funds` onto its marker (for nf-1); `build-security-universe` in sweep.ONLY_STAGES, its runner and its call after publish-page (for su-2).

After the drain and the deploy (issuer acts, each under a never-widen pair): the D12 gate flip in leg_gates.json, then D12 Step B (the IDVZ/PFOE import) with its per-date census of 0 other-fund deltas in G1 and G5.

## Cells

### `RIV-nf-1` -- the trade schedule rebuilds only the named funds (row Z-S29; CTO~Z ruling B)
- Measured: `gold_trade_schedule.run_stage` builds one G5 object (and its G6) per report date from every fund's windows; the D12
  Step B mirror dry run re-derived every fund's trades on 189 dates with current code (confidence 176 dates, action 99, est
  price 99, discretionary_shares 43, income_funded 10, row counts 3); `hold_funds` leaves a fund OUT of the new object
  (`:95-101`), so it cannot keep a fund's prior rows.
- Interface: the stage event key `rebuild_funds` (a list of tickers). With it, for each scope date the new G5 object is the
  newest prior G5 object's rows for every fund NOT named (values unchanged) plus freshly inferred rows for the named funds; G6
  likewise from the newest prior G6 object. A date with no prior object builds every fund. Without the key nothing changes.
  `sweep.run_gold_chain` passes the batch's `rebuild_funds` (read from the fetch-bloomberg marker of the batch) to the
  trade-schedule stage.
- **Organic trigger:** the import batch's S3 marker event (canonical-shape Lambda -> run_gold_chain).

### `RIV-gf-1` -- a rivalfunds-owned gate file (CTO~Z ruling; Andrew-direct @33ff3bdac0)
- Measured: `universe.d12_enabled()` reads only the process environment (`universe.py:36-37`); the vehicle sets no D12 variable
  and its file `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` may not be edited.
- Interface: `data/etfs/scripts/rivalfunds/leg_gates.json` {"RIVALFUNDS_LEG_ENABLE", "RIVALFUNDS_LEG_D12", "RIVALFUNDS_LEG_D13":
  "0"|"1"}; a gate reads ON when the environment says "1" OR the file says "1" (one direction); `universe.GATES_FILE` names the
  file; the committed file ships every gate "0". The map cache stamp includes the file's gate state.
- **Organic trigger:** every process that reads the map (the vehicle's leg, every Lambda).

### `RIV-su-2` -- security_universe as its own incremental invocation (CTO~Z msg 29624 term 4)
- Measured: round 8's `gold_security_universe.handler_entry` rescans every G1 date of 3 years (504 on S3) and ran the publish
  Lambda into its 900 s timeout at 1024/1024 MB; its publish-path call was removed (b166e04416).
- Interface: `handler_entry({"date", "sink", "mode": "incremental"|"seed"})`: `incremental` reads the newest prior universe object
  dated before the as-of and the as-of date's canonical_shape ONLY and writes the merged list (new securities added, first_seen
  kept, last_seen advanced, funds and date counts merged); `seed` is today's full build; `incremental` with no prior object
  builds as `seed`.
- **Organic trigger:** the 09:00 ET sweep after publish-page (the issuer registers the stage at the merge).

### `RIV-ln-1` -- the AI-text name links (CVO C-S35)
- Measured on the served 10-05 page: 395 AI-text mentions of 43 securities that have a modal are plain text; in the page's render
  context 428 of 860 display names are carried by more than one key ('Enel SpA' <- 29265W207, ENEL_IM_Equity, 'ENEL IM Equity'),
  and `render._render_page` keeps a name in `_NAME_KEYS` only when ONE key carries it (render.py:1769).
- Interface: a page name whose keys include exactly ONE key with a dialog on the page links to that key; a name two
  dialog-bearing securities share links to the key the account's citation list names, else stays plain with both identifiers
  in its title; a one-key name links as today. The page stays under the gateway cap (2,097,152 B).
- **Organic trigger:** the 07:00 ET marker publish and the 09:00 ET sweep publish.

### `RIV-cb-1` -- the measured Bloomberg capacity budget (rows Z-S24, Z-C-S32)
- Measured 2026-10-05: about 175k BQL rows of local backfill (IDVZ+PFOE 12,820; ACWI+IWM 76,859 + 84,655; probes) between 05:30Z
  and 07:06Z exhausted the Terminal's daily capacity and blocked the 07:00 ET production pulls; nothing recorded the spend and
  nothing refused a pull before it ran.
- Interface: `rivalfunds.bbg_budget` (`CONFIG_PATH` -> `bbg_budget.json` {daily_ceiling_rows, production_reserve_rows,
  est_rows_per_fund_date}; ledger dir from RIVALFUNDS_BBG_BUDGET_DIR, one JSON-lines file per UTC day); `spent(day)`,
  `record(mode, rows, batch_id)`; `collector_bloomberg` records every capture's rows and REFUSES a backfill whose estimate
  passes ceiling - reserve (status "BUDGET", no fetch); `daily` (production) is never refused, only recorded.
- **Organic trigger:** every collector run on the terminal machine (the vehicle's daily leg records; an ad hoc backfill asks).

### `RIV-nm-3` -- real names for past holdings (CVO C-S36)
- Measured on the 10-05 render context: 135 keys carry a ticker-form name ('ATD CN Equity'); 0 of them sit in any fund's latest
  holdings; 128 were never in any G4 date and 7 sit in G4 with no name -- the G4 enrichment asks only for current holdings.
- Interface: `rivalfunds.security_names.handler_entry({"date", "sink"}, fetch=None)` reads the page day's newest
  holding_contribution, takes the keys with a blank or ticker-form name, drops the keys the newest `gold/security_names` object
  already names, asks `fetch(keys) -> {key: name}` for the rest (production: one LONG_COMP_NAME reference request, asked through
  `bbg_budget` first) and writes a new object with the prior names plus the new; `gold_holding_contribution` takes a key's name
  from it when G4 has none, before any G1 name. `enrichment_bloomberg --mode daily` runs it for the page day after its G4 lands.
- **Organic trigger:** the vehicle's 07:00 ET enrichment step (no vehicle file changes).

### `RIV-gd-1` -- the G5 history-drift classification (round-8 analysis item 7, row Z-S29)
- Measured by the D12 Step B mirror dry run: a G5 built by current code differs from the live G5 on most of 189 dates for the
  funds other than IDVZ/PFOE (confidence 176 dates, action 99, est price 99, discretionary_shares 43, income_funded 10, row count
  3; est_price_source and key_resolution new on 183).
- Interface: `data/etfs/scripts/rivalfunds/tools/g5_drift.py` (live S3 READ-ONLY; G5 rebuilt into a LOCAL sink) writes
  `deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json` (dates, rows_compared, rows_differing, classes [{name, columns, n_dates,
  n_rows, cause {commit, cell}, reader_visible}], unclassified_rows) and a one-page G5_DRIFT.md. No S3 write, no replay.
- **Organic trigger:** none; a one-off read for the CTO's ruling on the history.
