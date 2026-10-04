# ETFS_RIVALS -- DECOMPOSITION, ROUND 8 WORKSTREAM A (ENRICHMENT): the AI step never costs the page, one name in the AI prose, the render remainder, the census price repair, and the Bloomberg leg sized for the benchmarks

```json
{
 "project": "ETFS_RIVALS",
 "round": 8,
 "workstream": "A",
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.13; ADMITTED)",
 "prd_version": "v0.13",
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
