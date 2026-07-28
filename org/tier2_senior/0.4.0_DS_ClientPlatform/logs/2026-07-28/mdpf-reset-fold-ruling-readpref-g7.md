# 0.4.0_DS_ClientPlatform -- 2026-07-28 2306-2345Z -- reset-directive queue: fold ruling landed, read-pref removed, G7 + Finding-A mechanism traced

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, TRACE, VALIDATE, SCRIBE

Fresh session under the MDPF Reset Directive (org/critical_paths/MDPF_RESET_DIRECTIVE_20260728T2220Z.md,
all 5 amendments) + CTO spawn-queue 230625Z. Pre-2220Z inbox traffic drained, acted on nothing in it.
4 commits, 3 producer deploys (pre-freeze), ~5 MCP exchanges with CTO + 2 with AE. Nothing published;
serve untouched; chain untouched.

## Summary

| item | outcome |
|---|---|
| Item 1: global-fold carry ruling (CTO 230319Z) | LANDED @37ee77a; window CORRECTED @4ed8a19775 (CTO 233402Z); deployed, md5 == HEAD |
| Item 2: `_interpolated` read-preference removal | LANDED @314f864aa0 (separate commit); proven-consumed via histogram flip |
| Item 3: G7 review | COMPLETE @73bc18d4c7 -- 976-line gap = CRLF artifact; Finding-A mechanism source-confirmed |
| Headline observable | frontier 07-27 opal_aggregate = $1,950,519,805.86 (was $1,826,143,796.13 excluding cottonwood) |
| Deploy freeze (CTO 234057Z) | honoured -- all deploys predate it; pair merge + slice W-2b staged as post-fires work |

## 1. Item 1 -- carried-within-declared-cadence window

`dim_mdpf_aggregate_aua_timeseries.py`: cottonwood participates at frontier D iff trading-day
age(value_as_of, D) <= the roster-declared window. Window READ from partner_roster.json at runtime
(fail-closed if absent; resolver: script-adjacent [runner synced prefix] then repo-relative -- ONE
committed authority, no S3 fallback). Carry source = latest MEASURED covered date (a band estimate
under a carried_* label would launder the interpolation taint). VALUES carried, rosters/counts never.
Band folds under the SAME rule as the headline; cottonwood leg pin extended to carried vintages; every
provenance row now carries `as_of_by_partner`. Slot label exactly `carried_at_declared_cadence(as_of=...)`.

**Window correction (CTO 233402Z):** my first derivation composed cadence offset + max_lag = 5,
double-counting the cadence -- `per_partner_max_lag_trading_days` is measured from the offset-0
frontier and ALREADY CONTAINS it (the roster's own `_basis_note` warns of exactly this swap). Corrected
to max_lag alone (3); cadence stays derived-and-reported as provenance, never an addend. Boundary
tests re-cut: age 3 == window CARRIES, age 4 ABSENT (the age the loose window would have wrongly
carried). Tonight's output unchanged either way (ages 1-3).

## 2. Item 2 -- read-preference removal (hold conditions met)

`load_cottonwood_slice` now reads ONLY the canonical daily slice; the frozen 07-23 `_interpolated`
one-off is not even a fallback (a frozen stand-in would mask a dead daily producer). Proof of
consumption: cottonwood slot histogram 403 absent / 45 interpolated / 2 measured -> 445 / 0 / 2 + 3
carried. CONSEQUENCE surfaced same turn: the 45-date interpolated history no longer participates;
CTO RATIFIED on Andrew's ~2144Z verbatim ("absolutely no excuse for any kind of interpolation or
estimation when it comes to asset valuation") -- honest 2-firm history until the canonical lineage
produces real history.

## 3. Item 3 -- G7 + the Finding-A mechanism (deliverable: G7_COTTONWOOD_GENERATION_GAP_REVIEW_20260728.md)

- **"976-line generation gap" was a CRLF diff-instrument artifact.** Normalized: pair 26 lines / 2
  blocks (repo carries Andrew-direct two-source basis; deployed carries CTO tolerance recal -- UNION
  merge ruled); slice 80 lines (repo W-2b three-quantity vs deployed all-None totals -- substantive).
- **Finding-A root, measured on live parquets: a two-date fact on a one-date key.** dim partitions
  keyed by ASSIGNMENT date, values as-of `value_date` (both columns in the parquet). 07-21 + 07-22
  partitions BOTH carry value_date 07-20 (identical $125,618,015.02) -- the artifact's "measured"
  dates are forward-dated. 07-23..07-27 = the :523 IAM-outage hole. Tonight's only fresh partition
  (date=07-28, value 07-24, $126,377,399.72) is CLIPPED off the global axis (ends 07-27) -- invisible.
  IAM fix necessary, never sufficient: the directive's second branch, confirmed.
- One defect family with the DDB cottonwood 2-of-447 class (CTO's rhyme, confirmed) and Amendment 5's
  same-day-key-vs-D+2-data diagnosis one layer down.
- Fix design proposed (value_date re-key + collision dedup + W-2b in one slice edit + dim backfill +
  pair union) -- ALL post-fires, CTO gate. Baseline expectation for tomorrow's run stated in advance
  so the un-advanced slice frontier is not misread as a regression.

## Errors of mine this window

1. **Window double-count** (above): I read the roster's cadence + tolerance as addends when the
   tolerance's own provenance line ("3 = 2 + 1") and `_basis_note` said composed. Caught by CTO on my
   report; corrected same cycle. Banked: when a declared quantity names its basis, DERIVE from the
   basis statement, not from the ruling prose that references the quantity.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-pipescript io` | `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` (PATH form) | PASS | reads manifest + monolith silver reads before editing |
| `comp-grep` | fold/provenance/roster/calendar symbol location x4 | PASS | first call used escaped `\|` -- comp-grep WARNED (Python re literal) and I re-ran with bare pipe; the warning prevented a false 0-match |
| `comp-glob` | `partner_roster.json`, `build_cottonwood_mdpf*` | PASS | located roster + both generations incl. AE's staged/patched copies |
| `commit-gate.sh` | producer x3, tests x2 | PASS | clean each time |
| live primitives (stage-2 per standing order) | head-object, list-objects-v2 (silver partitions, gold tree, dim parquets), get-object reads, s3 cp + etag==md5 verify | PASS | deployed-copy verification by content hash, never rc |

**What worked:** comp-grep's escaped-pipe warning; comp-pipescript io's monolith-read listing.
**Gap (standing, re-confirmed):** `comp-pipescript deployed` still cannot see the mdpf tree (07-24 +
07-28 filings) -- deploy verification done by head-object md5 instead.

## Files Modified

`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` (@37ee77a, @314f864aa0, @4ed8a19775; S3
md5 6c16f86005ce3967c7cbca1abaa21ef3 == HEAD), `tests/test_global_fold_flag2.py` (11/11),
`deliverables/G7_COTTONWOOD_GENERATION_GAP_REVIEW_20260728.md` (@73bc18d4c7).

## Blockers

None. All three queue items closed on my side; pair merge + slice W-2b/value_date work is STAGED
post-fires behind CTO's deploy freeze + gate.

## Current State

- Producer deployed (md5-verified) with: carry window 3 (roster-read, fail-closed), daily-slice-only
  cottonwood read, as_of_by_partner provenance. Roster published by AE (ETag a22fc62b...) at the
  resolver's first-choice key; pickup confirmed by runner-layout simulation.
- Tomorrow 15:00Z scheduled fire = D2 evidence run; expected: carry from labeled 07-22, headline
  ~$1,950.5M at frontier; slice frontier will NOT advance (Finding-A defect, fix gated post-fires).
- Serve untouched; publisher is AE's WO-2; nothing I wrote publishes.

## Next Steps

1. **[0.4.0_DS_ClientPlatform]** post-fires + CTO gate: pair UNION merge; slice value_date re-key +
   W-2b alignment (one edit); support dim backfill sequencing.
2. **[1.0.0_SA_CTO]** gate the G7 fix design; sequence dim backfill with AE.
3. **[3.0.0_SA_CVO]** D1-D4 certification consumes tonight's evidence trail (PIN-1 enumeration is AE's
   post-WO-1 commit; my artifacts carry label-the-basis channels it can read).
