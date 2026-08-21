# Addendum 1705-1730Z -- P4R-4 stopped the cutover one step from PROD

**archetype:** VALIDATE
**secondary_archetypes:** BUILD, SCRIBE
**serial:** 0.4.0_DE_ClientPlatform (base)
**window:** 2026-08-21 ~1705Z -> ~1730Z (delta since `addendum_capture_1645-1705Z.md`)

## What happened

P4R-4 ("before/after deltas per key, NAMED, never blended") was the last criterion I owed, and it only became measurable once the flip existed. Measuring it stopped the promote.

The flip carries **three separable components**, and a single "repoint landed, DELTA=0, certified" verdict would have been true on the route plane and silent on the rest:

1. **ROUTE-MOVE** — DELTA=0 by construction, CVO-certified.
2. **CONTENT-REFRESH** — `data_as_of` 08-19 → 08-20, one trading day.
3. **DOMAIN TRUNCATION + DIMENSION COLLAPSE** — neither route nor refresh, and user-visible.

## The escalation, and my own error inside it

I reported the headline before the deliverable because DT was mid-promote. MSTR held the push; DT held the merge; COO and CTO ruled option (b) — ship four "clean" keys, hold two.

**But COO's GIVEN was conditional on my figures, and I had not finished testing it.** My first pass compared **top-level shapes only**, at which grain `leaderboard` and both `partner_analytics` read "identical both sides." That is what I reported, and the GIVEN rested on it. A recursive diff found the collapses one and two levels down:

- **`views.ofc`** — "AUA by Office" donut: nine offices → a single `'other'` at 100%
- **`views.geo`** — "AUA by State": `unassigned` 0.069% → **100%**; donut segments **48 → 1**
- **`leaderboard`** — 163 → 146 entries in every window; **20 named advisors** absent
- **`mix_summary`** — `mix_periods` 5 quarters → 1

I declined to land the ruled edit and said so, because executing would have shipped exactly what the deciders' own condition excluded. Both halves were then withdrawn on all six and the promote stood down.

## The complete pass (DT's challenge, and it was right)

DT observed that my figures were *a second pass, not an exhaustive one* — nobody had said the recursive diff covered all ten. Run across all ten certified keys:

**Nine of ten carry material regressions. Exactly one — `clients-tab-slim` — is clean.**

Newly surfaced: **`ownership_map`** — 198 arrays shrunk, 48 keys dropped, per-advisor accounts roughly halved (`kyle_sims` 844 → 352). It had escaped every prior check for the same reason it escaped P4R-1: **no portal reader.**

That number changed the framing — not per-key bad luck, but the canonical plane's extent showing through every key that carries history, geography, office, or population. Consistent with CVO's mechanism read: 529 partitions from 2024-07-08, eleven dims and none geographic. **Not port defects.** A source-readiness finding whose remedy is a program.

## Final state

`6d0403a5` (six held) then `bdc68376` (final three) — **flip 1 / held 13 / structural 1**, verified independently by CVO at HEAD. `ADVI_ROUTE_LIVE` stays `true`: the determination lives in the per-key registry, not the flag, so the stand-down is **structural** rather than a config someone could flip back by accident.

Andrew closed the DEV-exposure question directly: *"DEV is fine dont worry about it thats purely local on my device"* — I stopped that line on his word. My CI read had already run before the relay arrived and corroborates; recorded as corroboration, not spent further.

## My errors today, as one pattern

Four times I measured at one grain or plane and asserted at another:

| # | what I measured | what I claimed |
|---|---|---|
| 1 | law commit in HEAD | "both surfaces satisfied" (never checked push state) |
| 2 | read sites **exist** at `:409`/`:300` | live consumers (never checked reachability for this tenant) |
| 3 | artifact-level `geo_drill` loss | user-visible (renderer never references it) |
| 4 | **top-level** shapes identical | four keys "clean" (collapses were two levels down) |

Every one produced a confident, well-formed, wrong answer, and every one was caught by a control or a challenge rather than by care. Worth naming as *my* characteristic failure rather than four incidents.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `aws s3 cp` + recursive diff | all 10 twins vs all 10 legacy at their correct prefixes (incl. `platinum/49financial/` and the gold plane) | the 9-of-10 finding |
| `comp-find` | renderer tracing (`ContinuousChartView`, `chartData.geo`, `mix_periods`), `barChart.stacked` per tenant | the render path, and the `geo_drill` correction against myself |
| `bunx tsc -b` | after each held edit, **mutant control first** | rc=0 both times; mutant rc=2 both times |

## Blockers

None. Nothing pends at this seat.

## Current state

Portal DEV `bdc68376`. `origin/PROD` untouched at `8a96c916`. Consumer-visible flips = **0**; every portal-reachable key resolves to legacy. **The cutover is STAGED, NOT LANDED.** Route act, registry, certs, pins and oracle table all stand — re-flipping a key as its gap closes is one word.
