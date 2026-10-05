# ETFS_RIVALS -- DECOMPOSITION, ROUND 8 WORKSTREAM A (ENRICHMENT): the AI step never costs the page, one name in the AI prose, the render remainder, the census price repair, and the Bloomberg leg sized for the benchmarks

```json
{
 "project": "ETFS_RIVALS",
 "round": 8,
 "workstream": "A",
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.14 @4cc8e40575; ADMITTED 21:15:49Z, ratified-text re-signed by 3.0.0_SA_CVO~Z)",
 "prd_version": "v0.14",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round7.md@115645c4b4 (section 3, ENRICHMENT LIST items 1, 2, 4)",
 "authority": "org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261004_20xxZ_BUILD_ETFS_RIVALS_ROUND8_TONIGHT.md@0a4321b843",
 "draft_ref": "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round8/DECOMP_DRAFT.md@1b2d733c6d",
 "author": "2.0.0_SA_COO~RV",
 "cells": 5,
 "chains": 4,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "round7_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round7.md"
}
```

**Issuer:** `2.0.0_SA_COO~RV`, 2026-10-04 ~21:xxZ, FULL.

## Issuer rulings at this cut

1. **Andrew's word issues workstream A now** ("yes, build round 8 tonight", @0a4321b843). The round-7 analysis deferred the
   ONE issuance until after the 2026-10-05 grades; that deferral binds item 3 only, which becomes **workstream B** after the
   grades, together with the smoke items (record `cooRV_ANDREW_DIRECT_20261004_21xxZ_RIVALFUNDS_SIGNED_IN_SMOKE.md`
   @1c31a5f6ce, S2-S8). Two bounds ride every cell: **no merge into CLOUD before the 2026-10-05 07:00 ET vehicle pull has
   run** (the vehicle runs the CLOUD tree), and **no Lambda deploy before 3.0.0_SA_CVO~RV's 13:30Z grades**.
2. **The draft's rulings stand** (DECOMP_DRAFT.md @1b2d733c6d): U02 and U08 SUPERSEDED by Andrew's layout word; Z-S16 and
   Z-S17 not cut; D10 rolls off ~10-08; D07 upstream; D04/D05/D06/D11 read Monday; I-2's data acts follow lg-1.
3. **The D12/D13 split (lg-1):** D12 = the HOME entries' `pending_source_policy` (IDVZ, PFOE through Bloomberg, history from
   inception); D13 = the `"leg": "pending"` entries plus `pending_role` (ACWI and IWM join as the benchmarks, SCHY reads rival).
   This matches Andrew's smoke S1: "S-C-H-Y is not the benchmark. The benchmark is ACWI ... P-F-O-E, the benchmark is I-W-M".
4. **Cut by write set (C10):** one file set per chain, below. an-1 -> rw-1 share `render.py`, so they are one chain, one queue.

## Rulings reaching every cell

Rounds 1-7's rulings stand (`ETFS_RIVALS_DECOMP.round{1..7}.md`). CALL 5 holds: one AI run per page day; a FAIL is shown,
never re-rolled. The standing L5 rule (CTO round-7 ruling 4): every production outcome names its ORGANIC trigger.

## 3. THE CELLS

### `RIV-dt-1` -- the deadline-aware vendor timeout (W1-S46; CTO round-7 ruling 1; item 1)
- The worst case today: a vendor call starting near the AI deadline runs `ai_client.TIMEOUT_S` = 120 s, which leaves 30 s
  of the 150 s margin for a republish that takes ~68 s at p95 (publish-page Lambda, 14 days, n=29: p95 68.1 s, max 81.2 s;
  the act-3 publish with refresh_a1 took 117.5 s; the CVO measured ~88 s).
- Interface: `chat(timeout=)`; a deadline client hands each call min(TIMEOUT_S, the time left); `sweep.REPUBLISH_RESERVE_S`
  >= 88 s is subtracted from the remaining time. A planted slow vendor at the deadline still republishes: the account is
  recorded FAILED and the page publishes without it.
- Check: `dt-1.AC1`. Organic trigger: the 09:00 ET sweep.

### `RIV-an-1` -- the AI prose reads each security under the page's one name (item 2 + U14's AI-text residue)
- The 3 money-market keys (DGCXX x2, IJGXX) sit in the stored prose; 13 casing clashes in the opening lines, 26 in the full
  text.
- Interface: `render._rich` maps whole security keys and casing variants to `_NAMES`; a cash-like key reads
  "<TICKER> money market fund" with the original in a title; the stored row is unchanged; the `.rf-cite` citation list keeps
  its keys.
- Check: `an-1.AC1`. Organic trigger: the 07:00 ET marker publish and the 09:00 ET sweep publish.

### `RIV-rw-1` -- the render remainder (RFW-U07, U12, U18)
- U07: the trend caption reads the dates and trading days only; the unit moves off it (`rw-1.AC1`).
- U12: consecutive noted 0-trade windows collapse into one line, with the notes kept inside (`rw-1.AC2`).
- U18: an all-caps "CORP." ends a sentence, so the account's lead is two sentences (`rw-1.AC3`).
- Organic trigger: as an-1.

### `RIV-rp-1` -- the census price repair (row Z-S18 + the contradictory miss reason)
- Z-S18: `alias` comes from the wide g1w and `books` from the 14-day g1, so a CUSIP resolved only in an older report misses
  its holding-implied price (`rp-1.AC1`).
- A census price row that reads `missing` never claims the rankings price it (`gold_input_census.py` ~:183, 44 served rows)
  (`rp-1.AC2`).
- Organic trigger: the 07:00 ET marker publish.

### `RIV-lg-1` -- the Bloomberg leg carries index-control-sized holdings and switches D12 and D13 apart (row Z-S20)
- Measured 2026-10-03 for 2026-10-01: IDVZ 45 / PFOE 24 / ACWI 2,198 / IWM 1,979 rows. `excel_fetch` runs one query per
  date with max_rows=2000 and raises RuntimeError on overflow, which `_handler_entry` does not catch: the leg crashes. The
  gate `RIVALFUNDS_LEG_ENABLE` switches every pending key at once.
- Interface: an `index_control` fund is queried on its own per date under a cap >= 2,500 and < 50,000; the range read never
  truncates silently; an overflow is a per-name partial (PARTIAL, the fund named, the others land); `universe` reads
  `RIVALFUNDS_LEG_D12` and `RIVALFUNDS_LEG_D13` per ruling 3, `RIVALFUNDS_LEG_ENABLE=1` turns both on, all unset is today.
- Checks: `lg-1.AC1` (fetch), `lg-1.AC2` (gates). Organic trigger: the vehicle's 07:00 ET leg. Nothing here flips a gate:
  each gate flip and its backfill is an issuer act under its own never-widen pair after the merge.

## ISSUER ACTS (no worker; each under its own pair)
- After lg-1 merges (after the 10-05 07:00 ET pull): the D13 gate flip + the ACWI/IWM backfill from 2026-01-02, then the D12
  gate flip + the IDVZ/PFOE backfill to inception; each with its budget threshold named in the pair.
- After the 13:30Z grades: the round-8 Lambda deploy (NEVER-2 ledger entry).

## 4. DEPENDENCY EDGES AND CHAINS

| chain | cells (serial) | writes |
|---|---|---|
| `~1` | dt-1 | `ai_client.py`, `ai_stage.py`, `sweep.py` |
| `~2` | an-1 -> rw-1 | `render.py` |
| `~3` | rp-1 | `gold_input_census.py` |
| `~4` | lg-1 | `collector_bloomberg.py`, `universe.py` |

No join cell. No hookup in a shared file is expected; a report that names one gets it at the merge.

## 5. BATTERY

`deliverables/2.0.0_SA_COO~RV/round8/checks/`, dry-run at base CLOUD 1c31a5f6ce (the package equals the deployed pin
75ad1e4d2e). Each order's face names its checks; the issuance commit carries every base line.

## WORKSTREAM B (issued 2026-10-04 ~22:xxZ, same issuer, same round): Andrew's signed-in smoke on PRD v0.14

**Authority:** the smoke record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261004_21xxZ_RIVALFUNDS_SIGNED_IN_SMOKE.md`
@1c31a5f6ce (S2, S3, S7, S8) under "yes, build round 8 tonight" (@0a4321b843), against PRD v0.14 @4cc8e40575 (ADMITTED 21:15:49Z).
Measured inputs: `deliverables/2.0.0_SA_COO~RV/round8/WORKSTREAM_B_INPUTS.md` @7cc969288b. Item 3 of the round-7 enrichment list
(what the 10-05 grades leave open) is still cut after the grades. The same two bounds hold: no merge before the 2026-10-05
07:00 ET vehicle pull, no deploy before the 13:30Z grades.

**Issuer rulings (B):**
1. The rolling period is the last 30 TRADING days (v0.14 FWD-13/14/15/19; Andrew "the last 30 trading days"), in the rankings,
   the buying trend and the AI fact pack alike; the existing `R30` id is kept and its meaning moves from 30 calendar days.
2. A window clipped to a fund's first report says so ("Since first report") and is never labelled year/quarter/month to date
   (S3). The flag is produced by hc-1 (`period_clipped`, `period_nominal_start`) and read by rn-1.
3. The buying trend carries one block per period with a `period` column (bt-1); every reader of buying_trend that wants the
   year reads `period == "YTD"` when the column exists. The AI fact pack is such a reader (gc-1 owns that filter).
4. rn-1 builds on chain `~2` (render.py after an-1 and rw-1); its worktree is cut from branch `wk-ETFS_RIVALS-2`.
5. The interfaces between cells are prescribed in the checks, so the four cells build in parallel: rn-1 renders fixture rows in
   the hc-1/bt-1 shape, gc-1 reads the bt-1 shape.

### `RIV-gc-1` -- the grader attaches an uncited fund-pack fact, and the AI's last 30 days are trading days (S2, S7)
- Measured: IDVZ "The last 30 days" FAILED on "$1.6 million, $1.3 million"; both are real fact-pack trades (T7 1,564,110.98;
  T9 1,292,762.88) the model left out of `cited`; with them cited the grade PASSES. "$1.3 million" also matches T8.
- Interface: `ai_accounts.attach_uncited(body, facts, cited) -> (rows, notes)` (one uncited match -> its row attached with
  `auto_cited`; two or more -> no attach, one note naming the ids); `run_chain` calls it before `grounding_check` and an
  ambiguous note joins the FAIL reason. `fact_pack` keeps trades in the last 30 NYSE trading days, and reads the trend rows
  with `period == "YTD"` when the column exists.
- Checks: `gc-1.AC1`, `gc-1.AC2`. Organic trigger: the 09:00 ET sweep's AI step.

### `RIV-hc-1` -- the rankings' rolling period is 30 trading days, and every row says whether its window was clipped (S3, S7)
- Measured: `R30` starts 29 calendar days back (`gold_holding_contribution.py:123`); YTD is clipped to the first report
  (`:411`, `:417`) with no field saying so.
- Interface: `period_start("R30", day)` = the 30th NYSE trading day ending on `day`; every row carries `period_nominal_start`
  and `period_clipped`.
- Check: `hc-1.AC1`. Organic trigger: the 07:00 ET marker publish (the A1 producer step).

### `RIV-bt-1` -- the buying trend carries every period (S8; v0.14 FWD-15)
- Measured: `build` writes the year to date only (`gold_buying_trend.py:157`, `:210`).
- Interface: rows carry `period` in {R30, MTD, QTD, YTD}, each with its own window_start / window_end / n_trading_days;
  YTD rows are today's rows.
- Check: `bt-1.AC1`. Organic trigger: the 07:00 ET marker publish.

### `RIV-rn-1` -- the 30-trading-day default, the switch inside both components, and honest window labels (S3, S7, S8)
- Measured: `render.PERIODS` = MTD/QTD/YTD with YTD first and selected (~:806-813); the switch lives only at the top; the
  trend card reads "year to date" for every fund (~:1057); IDVZ's clipped window reads "Year to date (2026)".
- Interface: one `rf-period` radio group (R30 checked); the top switch reads R30, a `data-period-divider`, MTD, QTD, YTD;
  the rankings component and each trend card hold labels for the same four radios (any one moves all; no script); every rank
  and trend panel carries a `data-period-window` line (label, first and last date, trading days); R30 reads "Last 30
  trading days"; a clipped window reads "Since first report".
- Checks: `rn-1.AC1`, `rn-1.AC2`. Organic trigger: the 07:00 ET marker publish and the 09:00 ET sweep publish.

| chain | cells | writes |
|---|---|---|
| `~5` | gc-1 | `ai_accounts.py` |
| `~6` | hc-1 | `gold_holding_contribution.py` |
| `~7` | bt-1 | `gold_buying_trend.py` |
| `~2` (cont.) | rn-1 | `render.py` |

## WORKSTREAM C (2026-10-05, same issuer, same round): FWD-21, every security opens its modal

**Authority:** Andrew-direct ~03:3xZ 2026-10-05 (record @41158af7f9, item 2), PRD v0.16 @646ce7f4b8 FWD-21 (CTO~Z msg 29442).
Items 3-4 of that record (the ETFClassifier full backfill and its routine mechanism) are routed by CTO~Z to 1.0.0_SA_CTO
(MDPF_SECCLASS); ETFS_RIVALS supplies a published list of every security the rivals and the Opal ETFs hold (a later cell).
Andrew's 3-year lookback cap (@357e681ddf) bounds every backfill.

**Issuer ruling:** one dialog per security page-wide, keyed by its security key, reused by every mention (the page is 1.89 MB
of the 2.10 MB gateway cap, so dialogs per fund x mention cannot fit). fc-1 continues chain `~2` (render.py) after rn-1.

### `RIV-fc-1` -- every security named on the page opens its one modal (FWD-21)
- Interface: every security mention in the rankings, trend, trade log and AI text is a `<button data-sec="<key>"
  popovertarget="<id>">`; one `data-sec-dialog="<key>"` element per security; no history -> "History not yet backfilled"
  (`data-history="none"`); no script; DIALOG_SOFT_CAP and its fallback kept.
- Check: `fc-1.AC1` (FAIL 3 at the rn-1 build 280b8dc66a, control OK). Organic trigger: the 07:00 ET marker publish.

| chain | cells | writes |
|---|---|---|
| `~2` (cont.) | fc-1 | `render.py` |

## WORKSTREAM D (2026-10-05, same issuer, same round): the served security list

**Authority:** CTO~Z ruling msg 29426 ("ETFS_RIVALS supplies its input: a published list of every security the rivals and Opal
ETFs hold"); laptop 1.0.0_SA_CTO msg 105132 (MDPF_SECCLASS FWD-9/FWD-10 read it); Andrew-direct 3-year cap @357e681ddf.
The interim source until it lands is gold canonical_shape (answered to the laptop CTO, msg 29471).

### `RIV-su-1` -- one served list of every security held within 3 years (gold security_universe)
- Interface: `gold_security_universe.handler_entry` -> one object at `address("rivalfunds","etfs","gold","security_universe",
  "date=<as-of>","universe-<revision>.parquet")` (builder output, measured: no refusal); one row per security; no cash lines.
- Check: `su-1.AC1` (FAIL 3 at base, control OK). The `produce_a1` hookup is the issuer's at the merge.

| chain | cells | writes |
|---|---|---|
| `~8` | su-1 | `gold_security_universe.py` (new) |

