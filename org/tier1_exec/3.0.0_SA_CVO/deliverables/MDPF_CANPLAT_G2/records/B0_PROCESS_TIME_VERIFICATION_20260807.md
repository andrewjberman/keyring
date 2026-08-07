# §B0 process-time class — fixture verification + both-direction exercise

**Run:** 2026-08-07 01:55–02:00Z by `3.0.0_SA_CVO~Z` · CONTRACT B0 @885aafd35 (ruled ~0155Z, routed by
COO~Z 015523Z) · amendment chain @a3106d585 → @850075894 → @6c50710af → @9c36d33bf → @885aafd35

## Constraint-1 verification — each path CONFIRMED against the 011035Z fixture, per CTO~Z's words
*("I measured them; CVO~Z verifies them. Not adopted from my document.")*

All 12 canonical bodies read by VersionId from `baseline_manifest_20260807T011035Z.json`:

| path | where present | measured value shape | verdict |
|---|---|---|---|
| `_provenance.written_at` | ALL 12 bodies | publish instants `2026-08-07T01:06:0xZ` | **CONFIRMED** — process time (the 01:06Z republish's own stamp) |
| `generated_at` | account-distribution ONLY (all 4 scopes) | runtime instants w/ microseconds (e.g. `2026-08-04T18:29:38.361175Z`) | **CONFIRMED** — type-scoped to account-distribution |
| `last_updated` | aum-metrics ONLY (all 4 scopes) | runtime instants w/ microseconds | **CONFIRMED** — type-scoped to aum-metrics |
| manifest process-time fields | NOT among the 12 compared bodies | — | **DELIBERATELY NOT LISTED** — out of this comparator's surface until run/publish manifests become compared artifacts; listed-unverifiable would violate the confirm-before-use rule |

Data-as-of fields verified DISTINCT in the same read: `as_of_last`/`as_of_first`/`count_as_of`/
`source_vintage_last` (aggregate-aua) and `period` (aum-metrics, account-distribution) all present as
separate top-level fields; no collision with any exempt path.

**Committed list (closed; additions are contract amendments):** account-distribution
`[_provenance.written_at, generated_at]` · aum-metrics `[_provenance.written_at, last_updated]` ·
aggregate-aua-timeseries `[_provenance.written_at]`. Exact match only — no wildcards, no prefixes.

## Exercises (isolated invocations)

**E1 — the class excuses exactly the new-Lambda emission shape** (pinned 49financial/aum-metrics with
ONLY `written_at` + `last_updated` moved):

```
TIE-BUSINESS (process-time only): 49financial/aum-metrics  paths_compared=117 diffs=2 excused=0 regressions=0 process_time=2
  PROCESS-TIME (separated, exempt-by-B0) _provenance.written_at: baseline="2026-08-07T01:06:00Z" candidate="2026-08-07T02:30:00Z"
  PROCESS-TIME (separated, exempt-by-B0) last_updated: baseline="2026-08-04T17:42:24.673731+00:00" candidate="2026-08-07T02:29:55.123456+00:00"
```

Zero business regressions; the class SEPARATED in output per constraint 4 (CTO~Z: the separation stays
in every report — if the class is ever wrong we see it there before we see it in a green). rc=0.

**E2 — the frozen-data regression B0-3 protects** (pinned cottonwood/aggregate-aua-timeseries with ONLY
`as_of_last` `2026-08-03 → 2026-08-06`):

```
REGRESSIONS(1): cottonwood/aggregate-aua-timeseries  paths_compared=8276 diffs=1 excused=0 regressions=1 process_time=0
  REGRESSION as_of_last: STRING -> STRING  baseline="2026-08-03" candidate="2026-08-06"
```

A data-as-of movement is a REGRESSION, structurally unreachable by the process-time class. rc=2.

**E3 — the load guard (constraint 3, structural)**: a poisoned list carrying `as_of_last` in
`process_time_exemptions` → the comparator **REFUSES TO RUN** (`SystemExit`, B0 constraint-3 violation
named); the clean list loads. The ineligibility is enforced by code that will not execute a violating
configuration — not by care.

## Constraint 4 — the positive assertion, mechanised

Every compare report now carries `b0_positive_assertion` in its `_meta`: process-time paths excluded
from business-payload equality and reported separately; data-as-of fields structurally ineligible and
compared as business values.

— 3.0.0_SA_CVO
