# Naming Placeholder Sweep (59 rows) + Seeder Attribute-Drop Fix -- 1.0.0_SA_CTO~X

**Date:** 2026-08-18 (~1750-1830Z)
**Task Order:** ad-hoc, Andrew-direct follow-up to the VUG naming fix ("Fix the 59 remaining
placeholder names and the seeder attribute-drop as well", then "/draw me the layers ... assess what is
redundant and ideally centralize ... canonize ... decommission the rest")
**Status:** COMPLETE (fixes); layers assessment DELIVERED in-chat + summarized here

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pulse (via safe-commit) | diff, per commit | PASS | risk reflex clean on both commits |

**What worked:** prior session's saved DDB scan doubled as the before-image for the
attribute-preservation diff -- no second baseline needed.
**What failed:** none.
**Gap found:** none -- this pass was named-file surgery on surfaces mapped last session.

---

## Work Completed (step by step)

### 1. Name sourcing, estate-internal, transcription-safe
The 59 placeholder tickers (60 measured minus VUG) all have canonical display names as inline comments
beside their `ETF_CLASSIFICATIONS` entries in `_shared/etf_classification.py` (100% coverage; 3 also in
`tickerRegistry.ts`, 1 benign variance -- HYG, fuller `_shared` form used). Names were extracted
PROGRAMMATICALLY and never hand-typed.

### 2. Repo canon updated (80494cab52)
The 59 generated entries inserted into `ETF_NAME_OVERRIDES` (7 -> 66) with a header comment naming the
placeholder mechanism (`seed-etf-classifications.py` writes `name=OVERRIDES.get(ticker, ticker)`).
Verified by import: 66 entries, 0 missing, 0 mismatched vs the extraction.

### 3. DynamoDB applied, condition-guarded
59 `update_item` calls, each conditioned on `name = :ticker` (still the placeholder) so any row that
moved since the scan fails loudly instead of being stomped. 59/59 applied, 0 failed.

### 4. Verified names-only delta
Full rescan vs the saved before-scan: 116/116 rows, membership identical, **0 placeholder/missing
names remain**; swept rows changed ONLY name/last_updated/updated_by; zero non-swept rows changed;
ACWI control confirms management_style/sector preserved.

### 5. Seeder attribute-drop: BOTH paths, not one (593eba688c)
Sampled `bd-securities` (400 rows): 392 carry `rationale` (LLM-classifier output), others
`firm_origin` -- attrs OUTSIDE the seeder's write-set, so the bd `put_item` had the same drop hazard as
the yang path (which measurably stripped VTV's management_style/sector on 2026-03-25). Both writes
converted to attribute-preserving `update_item` upserts; `name_aliases` absence now means leave-as-is;
docstring corrected.

### 6. Exercised on the real path, isolated fixtures
`ZZTESTCTOX` planted in BOTH live tables with foreign attrs; the real `seed(upload=True,
sync_yang=True)` run on a monkeypatched one-item list; foreign attrs survived, owned fields written,
fixtures deleted; `etf-classifications` count 116 unchanged.

### 7. Layers diagram + centralization assessment
Delivered in-chat per /draw house style. Surfaces measured this pass: `_shared` overrides 66 ·
generate-positioning inline overrides 29 · `tickerRegistry.ts` 129 · `ETF_NAME_FALLBACKS` 53 ·
Attribution `etf-categories.ts` 56 · Positioning `etf-categories.ts` 36. Recommendation (execution
awaits Andrew's GO -- it is a decommission program, not authorized by this log): CANON =
`_shared/etf_classification.py` (author-time) -> `etf-classifications` DDB (runtime), which its own
docstring already declares; DECOMMISSION-CANDIDATES in order: generate-positioning inline dict (route
through registry as holdings-attribution now does), the 2 byte-copies of
`etf_classifications_dynamodb.py` (one home), then the 3 page-scoped portal maps once a served vintage
proves every name/class arrives correct from the producers; `tickerRegistry.ts` either generated from
the registry at build time or ratified as a FE-projection with non-naming fields only. `bd-securities`
+ `CANONICAL_SECURITIES` are NOT redundant (different jobs: BD-firm classification with LLM rationale;
held-securities census) -- their NAME fields should derive from the canon, which the fixed seeder now
does safely.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Names from `_shared` inline comments, programmatically | estate's own record; kills transcription risk on 59 rows |
| Conditioned update-items, not a seeder run | preserves attrs; a moved row fails loudly (control on the retrieval) |
| Fixed BOTH seeder paths | bd path measured carrying the same hazard (392/400 rows with foreign attrs) |
| Fixture-exercised the seeder fix | dry-run cannot exercise a write path; isolated plant-verify-delete can |
| Decommission plan proposed, not executed | no-inferred-remediation; awaiting Andrew's GO on the sequence |
