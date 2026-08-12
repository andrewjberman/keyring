# 0.4.0_DS_ClientPlatform~O -- OPAL_BRDSEP.T1 Opal asset base by segment (1815-1900Z)

**archetype:** MEASURE
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Window summary

Lane's first session. Startup clean, zero TOs held, awaited direction as instructed; CTO issued
OPAL_BRDSEP.T1 at 1814Z and Andrew's two open confirms landed at 1817Z mid-flight and folded with no
rework. Measured the four-segment Opal asset base 2026-04-01 -> 2026-08-11 for the September board
update. Delivered @7d46e2d79d. Proof-of-spec VALID, 0 violations. Both mutants fired.

## What the measurement changed about the question

**The issuance named three hazards. Measurement resolved all three and found a fourth of the same
class that was on nobody's list.**

1. **The April-1 ETF baseline partly EXISTS.** The pre-issuance enumeration reported no source under
   `opal-data-etfs` reaching 2026-04-01 and named four prefixes. `silver/netassets/` -- 353 partitions,
   2025-05-30..2026-08-11 -- covers both endpoints. The enumeration had seen its sibling
   `silver/holdings/` (60 partitions, from 2026-05-18). **Finding it did not end the question, it split
   it per ticker:** DIVZ/IDVZ have an April-1 value that is INTERPOLATED (`msn_anchored_interpolated`),
   with a genuine issuer month-end anchor one day earlier at 2026-03-31; PFDE/PFOE have nothing.
2. **The naive ETF delta is +98.55% and it is false.** PFDE/PFOE were **incepted 2025-12-30** -- three
   months before the window opened -- and entered our measurement 2026-05-18. Subtracting the two
   totals counts a coverage onset as growth, $257,769,042.00 of it. Like-for-like is +$116.8M (+30.74%).
   Grounded at source: `docs/briefs/mdpf-pfde-pfoe-etf-netassets-feasibility-20260518.md:23-24,60,84`.
3. **Cottonwood carries the identical defect and was on no hazard list.** `point_class` at 2026-04-01 is
   `absent` -- **absent, not zero**; `first_tracked_date` 2026-07-20; 12 measured dates of 451; the
   sanctioned backfill reaches only to 2026-05-28. Same shape as the ETF trap, $136.5M of it.
   **I found it only because the producer writes `absent` rather than `0.0`.** A producer that had
   written a zero there would have put a false zero into a board number with nothing to catch it.
4. **Inflection's zero is real but BASIS-SCOPED.** The pre-grounded 0 -> $144,978,896.75 reproduces
   exactly. But Orion silver `fact_positions` shows **$914,144.89 across 17 accounts / 4 clients in
   Opal-NAMED models on 2026-04-01**. Both instruments are right about different bases -- Eclipse
   crosswalk vs Orion display names. 0.63% of the segment. Reported both, adjudicated neither; the
   framing is Andrew's.

## Controls -- both mutants FIRED

| mutant | mutated result | correct result | verdict |
|---|---|---|---|
| drop cohort-matching from the ETF delta | +$374,593,187.70 (+98.55%) | +$116,824,145.70 (+30.74%) | FIRED, 2.2x apart |
| drop name-normalization from the Cottonwood reconciliation | 4 of 18 report MISSING | 0 (EMPTY) | FIRED, 4 false findings |

**Mutant 2 came in harder than I predicted.** I wrote "1-2 false NOT-FOUNDs" into the deliverable from
estimate; the measurement said **4** (`Anna *9238`, `Moderate Income Portfolio`, `Opal - Beecherl Legg`,
`Opal - Income`, all present on the roster). Corrected the deliverable to the measured figure before
commit. **The flagged hazard was that a name scan DROPS 3 strategies; the symmetric hazard -- that name
matching INVENTS missing ones -- was the larger of the two and nobody had named it.**

Determinism: extraction run twice, byte-identical, 0 differing lines of 514. STABLE.

## Cottonwood live sweep -- reused the estate's own, did not duplicate it

Andrew asked for a live current sweep of the Black Diamond Rebalance endpoint. `cot-rebalancer-runner`
pulls exactly that endpoint daily and **landed today at 02:00Z** -- 63 of 63 strategies, single page. I
reconciled against that landing (the sanctioned raw-vendor path) and corroborated it against the
independent 62/62 live scan of 2026-08-07, zero drift. **Build-ladder rung 2: the estate already had it.**
No vendor call made; the standing lift is cot-BD only and I did not need to spend it.

**Stated limit rather than implied completeness:** composition is pulled under
`MODEL_DETAIL_SCOPE=opal_closure`, which seeds only on names containing "opal" -- 29 of 63 landed (46%).
So my found-not-on-list set is complete for NAME-based discovery and structurally cannot be complete for
COMPOSITION-based discovery from bronze alone. The 08-07 full scan closes that axis and found the only
non-Opal-named Opal-composed strategies to be the two Annas, both already on Andrew's 18.

## Headline figures

| Segment | Start | End | Delta |
|---|---:|---:|---:|
| 49 Financial (Schwab 08242234) model AUA | $1,212,782,514.51 (04-01) | $1,451,519,328.79 (08-11) | +$238,736,814.28 |
| Inflection model AUA | $0.00 (04-01) | $144,978,896.75 (08-10) | +$144,978,896.75 |
| Cottonwood model AUA | NO BASELINE | $136,530,322.99 (08-10) | UNCOMPUTABLE |
| ETF Float | NO BASELINE | $105,976,737.76 (08-11) | UNCOMPUTABLE |

Total Opal asset base at window end **$1,839,005,286.29** (mixed as-of 08-10/08-11). No single headline
growth rate computed -- TO section 6 reserves that framing to Andrew.

Counts: 49F accounts 6,683 -> 7,189 (+506), clients 4,020 -> 4,268 (+248). Inflection Opal-model
accounts 17 -> 600, clients 4 -> 266.

## Compiler Tools

| tool | call | result | note |
|---|---|---|---|
| `comp-which` | ETF source routing | near-tie 3 of 75 | declined to guess; routed to comp-estate |
| `comp-estate` | `etfs` -> REJECTED, then `etf-reports` | PASS after correction | named the 9 producers; its C0 roster self-labels "not a census denominator" so I did not use it as one |
| `comp-find` | `PFDE` | PASS -- 1,843 hits / 26,096 files | **the finding of the session** -- HEAD band put the inception brief on page 1 |
| `comp-find --name` | `rebalance` | PASS -- 17 of 17 | found the existing BD pipeline + both prior scans; saved a duplicate vendor call |
| `comp-to` | `OPAL_BRDSEP.T1` | PASS | race-free per-session TO context |
| `commit-gate.sh` | extraction script | PASS | "All checks passed!" |
| `proof-of-spec-check.py` | instance + 9 expected ids | **VALID, 0 violations** | coverage checked against the TO's minted set, not just row quality |

**What worked:** `comp-find`'s BAND classification. `PFDE` returned 1,843 hits; HEAD=58 put the one
document carrying the inception date at the top of page 1. That single fact is what separated
"two ETFs launched in-window" from "two ETFs entered our measurement in-window" -- a $257.8M difference
in the board number.
**What failed:** nothing failed, but my own estimate did -- I wrote a predicted mutant magnitude into
the deliverable instead of measuring it first, and it was wrong by 2x in the direction that understated
the hazard. Measured and corrected pre-commit.
**Gap found:** `comp-estate` has no `etfs` vertical though `opal-data-etfs` is canonical with 695
objects and 9 producers; it is spelled `etf-reports`. The obvious question does not route on the
obvious name. Surfaced to CTO, not chased.

## Current State

- **OPAL_BRDSEP.T1 measurement COMPLETE.** Deliverable + re-runnable extraction @7d46e2d79d;
  proof-of-spec VALID @this commit. Changes no served artifact; nothing written under `platinum/`.
- TO `<status>` left at `pending` for CTO to flip -- the deliverable is theirs to accept.
- One surprise-channel item open at CTO: Inflection's 08-11 ETF ownership appears carried forward from
  08-10 (identical to the cent on all 4 tickers while NAVs moved). Bounded, order $0.1M on the float.

## Next Steps

- [1.0.0_SA_CTO] Accept or rework the deliverable; three framing choices are named in section 6 and all
  three are Andrew's, not mine: 49F model-vs-total-custody, Cottonwood growth-vs-coverage-onset, and
  Inflection $0-vs-$914,144.89.
- [1.0.0_SA_CTO / whoever owns it] The Inflection 08-11 carry-forward. Not chased per surprise-channel
  discipline.
- [unowned, surfaced not claimed] A Cottonwood BD historical backfill into
  `blackdiamond/cottonwood/silver/fact_holdings` covering 2026-04-01 would convert this TO's single
  largest UNCOMPUTABLE into a measured number. The pipeline shape already exists; only the historical
  range is missing.
