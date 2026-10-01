# ETFS_RIVALS -- DECOMPOSITION, ROUND 4 (ENRICHMENT): own-prior-date trades, one revision contract, per-source identity floors, GQGU

```json
{
 "project": "ETFS_RIVALS",
 "round": 4,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.7 @01114ae8a8)",
 "prd_version": "v0.7",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round3.md@d4a1e22801",
 "author": "2.0.0_SA_COO~RV",
 "cells": 6,
 "chains": 3,
 "join_cells": 1,
 "frozen": true,
 "revision": "1.0 at L5",
 "round3_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round3.md (blob 9d6c95dbc9)"
}
```

**Issuer:** `2.0.0_SA_COO~RV`, 2026-10-01 ~12:xxZ. **Source:** the CTO's message 27810 and the round-3 analysis section 3 (items
1-4, fan-out cap 3), with rulings 1-4.

**Input state:**
- Round 3 is CLOSED.
- The page for 2026-10-01 is published with 12 of 13 funds updated. GQGU has no reader yet.
- The ledger `etfs-rivalfunds-round3` is CLOSED.
- Code is at CLOUD 48ec92238a.

## Issuer rulings at this cut

1. **Cut by write set (C10).**
   - All four items touch the same G1/G5 files (`gold_canonical_shape.py`, `gold_trade_schedule.py`). They are serialised on
     slot `~1`: t-5, then v-2, then i-2. Each is handed after its predecessor is MERGED.
   - GQGU's collector and silver (q-1, `~2`) and the per-source floors (f-3, `~3`, `guardrails.py` only) are disjoint.
   - GQGU's G1 read is per fund, and it is part of v-2's revision contract: newest PER (fund, date).
   - Fan-out: 3 of 3 chains, cap 3.
2. **One revision module.** v-2 adds `data/etfs/scripts/rivalfunds/revision.py` with `newest(uris)`.
   - Every reader of a multi-object date calls it: G1's issuer, Bloomberg and G4 picks; G5's G1 pick; the page's G1/G5/G6 picks.
   - Ordering: newest is the latest CAPTURE time, read from the object's revision. A hash never decides.
   - An object whose provenance is `import:` never outranks a live one for the same date.
   - New object names carry their capture time. Existing objects are read through the same function: their revision's
     leading timestamp, plus the provenance column for G4.
3. **The identity floor is per source** (ruling 3; the CTO's key-4 refusal):
   - `guardrails.py` grades issuer, Bloomberg and home funds (by name: IDVZ, PFOE) against their own `min_resolved_fraction`.
   - RIV-d-5 measures each floor from that source's newest served reports, rounded DOWN.
   - The test override is the environment variable `RIVALFUNDS_GUARDRAILS_OVERRIDE`, read by `guardrails.load_config()`, so
     `publish_page.py` stays v-2's alone.
4. **GQGU via the issuer route; no vendor word** (ruling 4).
   - The adapter is a second entry beside BASG's: SEI filepoint `gqg.filepoint.live/assets/data/SEI_GQG_Tradedate_Holdings_<MMDDYYYY>.txt`,
     with the same column set.
   - RIV-d-5 imports the 305 archived days (`.runtime/amgt-reconn-daily-census-20260929/gqgu/`) as QA-class issuer bronze with
     provenance. The daily `fetch-holdings` fetches both funds.
5. **W1-S27 is FIRST (ruling 1).** It is the first cell on `~1`, and it reaches served data only through RIV-d-5's pair.
   - Until then COO~RV holds the disarm: the page's "updated" means freshness, not trade completeness.

## Rulings reaching every cell

Rounds 1-3's rulings stand (`ETFS_RIVALS_DECOMP.round{1,2,3}.md`, "Rulings reaching every cell"):
- builder-only addresses;
- markers;
- real data on the seam;
- the Positioning pull is READ, never edited (Andrew-direct);
- no Bloomberg call by a build worker;
- no notifier.

New this round:
- the G5 matching key stays window-stable (RIV-i-1 amendment 2);
- the issuer-side retain stands (RIV-r-3).

## 1. THE DOMAIN, BY SUBTRACTION

Domain = the enrichment list's 4 items. Printed denominator: **4**.

| item | ruling | cell(s) | residue |
|---|---|---|---|
| 1 W1-S27 own-prior-date pairing | 1 | RIV-t-5 (code), RIV-d-5 (served) | 0 |
| 2 one revision contract | 2 | RIV-v-2 | 0; W1-S11 absorbed |
| 3 per-source identity floors and BASG issuer-only identity | 3 | RIV-f-3 (floors), RIV-i-2 (BASG alias), RIV-d-5 (measured values) | 0 |
| 4 GQGU via the issuer route | 4 | RIV-q-1 (collector + silver), RIV-v-2 (per-fund G1 read), RIV-d-5 (import of 305 days) | 0 |

**Not this round:**
- rulings 6-7 (W3-S15, S7, W2-S7, the W1-S5 PRD line, W3-S11, W3-S12, W5-S21);
- FWD-6, -7, -10 and -11.

## 2. THE RECTANGLE -- 6 cells

| cell | serves | status at the cut (check dry-run at base 48ec92238a) | risk | class |
|---|---|---|---|---|
| `RIV-t-5` | FWD-5 | ABSENT: t-5.AC1 FAILs; a daily G5 gives TXUE no window when its own prior date differs from the global one | LOCAL | worker |
| `RIV-v-2` | FWD-3/4/5 | ABSENT: v-2.AC1 FAILs (2026-09-29 G1 reads the QA import afcd903ad844); v-2.AC2 FAILs (a later-named second issuer fund displaces BASG, 0 of 35 rows) | LOCAL | worker |
| `RIV-i-2` | FWD-4/5 | ABSENT: i-2.AC1 FAILs (BASG 2026-09-30 resolves 0 of 33; 2026-09-28 resolves 34 of 34) | LOCAL | worker |
| `RIV-q-1` | FWD-1/3 | ABSENT: q-1.AC1 FAILs (`land_bronze` has no `fund`) | LOCAL | worker |
| `RIV-f-3` | FWD-9 | ABSENT: f-3.AC1 FAILs (the override is ignored; one floor over every source) | LOCAL | worker |
| `RIV-d-5` | the live join of 1-4 | ABSENT: d-5.AC1-AC3 FAIL (no act record; `revision` absent) | WORLD | worker |

## 3. THE CELLS -- 6 (round 4)

### `RIV-t-5` -- the daily trade schedule pairs each fund with ITS OWN prior report date (row W1-S27)

`gold_trade_schedule.run_stage` (daily and backfill): for each fund with G1 rows on a scope date, also load the G1 object of THAT
FUND's previous report date. Pair within the fund, exactly as a replay does. A fund with no earlier date is `no_prior_report`.
Replay behaviour is unchanged.

### `RIV-v-2` -- ONE revision contract for G1, G4 and the trade schedule (rows W4-S5, W1-S11, W1-S19, W1-S25)

`revision.py` (new):
- `capture_time(uri_or_revision)` and `newest(candidates)`, where a candidate is a URI or a {uri, provenance} record;
- newest = latest capture time;
- an `import:` provenance never outranks a live object of the same date;
- a hash never orders.

Every multi-object reader uses it:
- `gold_canonical_shape`: issuer silver PER FUND (the issuer prefix holds `basg-*` and, after RIV-q-1, `gqgu-*` objects), Bloomberg
  silver per fund, and the G4 pick;
- `gold_trade_schedule`: the G1 pick per date and its own G5/G6 objects;
- `publish_page`: the G1/G5/G6 picks;
- `enrichment_bloomberg`: new G4 objects named with their capture time.

The G1 revision forms of W1-S19 and W1-S25 (the `h`/`j` letter suffixes) are replaced by the contract. A reader of an existing
object keeps working.

### `RIV-i-2` -- BASG's issuer-only report dates resolve through a measured alias (row W4-S2; ruling 3)

`identity.py` and `gold_canonical_shape.py`: a CUSIP joined to a Bloomberg key on an earlier co-held date (RIV-i-1's join) keeps
that key on a later issuer-only date:
- `resolution_method = 'issuer-alias'`, with the date the alias was measured in `resolution_note`;
- the latest such join wins;
- a CUSIP never joined stays UNRESOLVED;
- a same-day join outranks an alias.

### `RIV-q-1` -- GQGU's issuer collector and silver (rows Z-S5/Z-S6; ruling 4)

- `adapters/gqgu.py`: the SEI filepoint URL, and a fetch identical in shape to BASG's.
- `collector_issuer.land_bronze(..., fund="BASG")`: bronze stem `<source>-<requested_date>-<ts>-<sha12>` per fund. The daily mode
  fetches every issuer-route fund of the map.
- `silver_issuer`: per fund. Objects are `<source>-<capture_id>.parquet`, rows typed from that fund's file. BASG is unchanged.

### `RIV-f-3` -- per-source identity floors (ruling 3)

- `guardrails.identity_coverage(reports, cfg, source)`.
- `guardrails_config.json`: `min_resolved_fraction` per source {issuer, bloomberg, home_producer} (home funds by name). Values
  stay PROVISIONAL here; RIV-d-5 sets the measured ones.
- `guardrails.load_config()` merges the JSON in `RIVALFUNDS_GUARDRAILS_OVERRIDE` when it is set.
- The reason string names the source and its floor. `evaluate_fund` already receives `source`.

### `RIV-d-5` -- the live join of round 4 (WORLD)

Under a NEVER-2 ledger entry `etfs-rivalfunds-round4` and a never-widen pair signed by `1.0.0_SA_CTO~Z` and this seat. The issuer
writes the pair at d-5's cut, after cells 1-5 are merged, with the served delta MEASURED per fund by
`round3/served_delta_r3.py`, widened to GQGU.
1. Update the five Lambdas in place.
2. Import the 305 archived GQGU days as issuer bronze, QA-class with provenance; silver and G1 follow by marker.
3. Set the per-source floors in `guardrails_config.json` from each source's measured newest reports, rounded down. Record them.
4. Replay G1, G5 and G6 over the window the served-delta names; publish the page.
5. Read it back and record `d5_live.json`.

Acceptance is the next trading day's 07:00 issuer fetch for both funds, the 08:03 leg and the 09:00 sweep, read at the close.

## 4. DEPENDENCY EDGES AND CHAINS

```
~1  RIV-t-5 --> RIV-v-2 --> RIV-i-2 --+
~2  RIV-q-1 --------------------------+--> ~4 RIV-d-5 (join, WORLD)
~3  RIV-f-3 --------------------------+
```

**Write sets**, disjoint across concurrent orders:

| cell(s) | writes |
|---|---|
| t-5, v-2, i-2 (`~1`, serial) | `gold_trade_schedule.py`, `gold_canonical_shape.py`, `revision.py`, `publish_page.py`, `enrichment_bloomberg.py`, `identity.py` |
| q-1 | `collector_issuer.py`, `adapters/`, `silver_issuer.py` |
| f-3 | `guardrails.py`, `guardrails_config.json` |
| d-5 | infra, the source map, the ledger, the floor values in `guardrails_config.json` (after f-3 merges) |

## 5. BATTERY

- **comp-schedule (RUN):** no armed gate names this project's surfaces.
- **comp-iam:** no IAM change in a build cell. d-5's plan names the fetch-holdings role's GQGU fetch (an egress URL, not IAM) and
  any new read.
- **comp-adversary:** DECLARED on RIV-v-2. It is the contract every reader rides; its check plants the measured case.

## 6. RULE 24

- **`resolution_method` gains `issuer-alias`.**
  - (i) MECE: it applies only on a same-day miss and needs a prior measured join.
  - (ii) Per row. (iii) One intent.
  - (iv) A new same-day join moves a row from `issuer-alias` to `issuer-bloomberg-join`. Nothing moves a never-joined CUSIP.
- **`min_resolved_fraction` per source {issuer, bloomberg, home_producer}.**
  - (i) Total over G1's `source_used`.
  - (iv) A source change moves the floor, never the measurement.

## 7. GATES AND THE CLOSE RUN

- **Build orders carry at most three criteria.** The suite runs at each drain.
- **12 issuer checks under `deliverables/2.0.0_SA_COO~RV/round4/checks/`.** All FAIL at base 48ec92238a.
- **The close run:**
  - the served page shows 13 of 13 funds, GQGU with issuer data;
  - TSEL's and WCMG's served windows pair with their own prior dates;
  - G1 2026-09-29 reads the live G4;
  - BASG's newest date resolves.

## 8. WHAT THIS DOES NOT CLAIM

- GQGU's archive covers 2025-07-14..2026-09-28 only. Days after that come from the daily fetch.
- No floor value is claimed before d-5 measures it.
- No FWD-6/-7/-10/-11 value is claimed.
