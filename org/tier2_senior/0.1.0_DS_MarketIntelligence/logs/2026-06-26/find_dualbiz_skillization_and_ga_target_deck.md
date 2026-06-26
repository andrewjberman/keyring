# FIND_DUALBIZ skillization + GA target enrichment + deck

**archetype:** IMPLEMENT
**secondary_archetypes:** EXPLORE, COORDINATE

**Agent:** 0.1.0_DS_MarketIntelligence
**Date:** 2026-06-26
**Window:** session start (2026-06-26, first log of session) -> now

## Summary

Andrew-direct live session. Audited the FIND_INSURE (deprecated) + FIND_DUALBIZ (live)
pipelines for modularity, then built the missing modular substrate and a Claude-operated
skill set to run the dual-business producing-agency discovery pipeline a-la-carte, and
drove a full GA lead cycle end to end: discover -> score -> qualify -> enrich (Lusha) ->
one-slide-per-firm deck.

## What shipped (chronological)

1. **S2 registry** (`registry.py`, `9d4725b4a`) -- the canonical candidate registry the
   design doc specified but was never built; replaced the `glob(serp-harvested-*.json)`
   hack. Bootstrap consolidated 477 raw -> 315 canonical candidates.
2. **Case query layer** (`cases.py`, `75a66c4ae`; region presets in `df5b8734b`; `--xlsx`
   in `b1834b771`) -- Jim Reed Case A/B/C (from his Teams thread, screenshot-supplied) +
   geo/state/region filter + CSV + formatted XLSX export.
3. **Skills** -- `/find-dualbiz` (`0919da613`) then split/renamed per Andrew to **`/find`**
   (recall->score->filter->ranked card display) + **`/target`** (Lusha: company org-chart
   cheap / person reveal full) (`df5b8734b`, `8a3a2ced2`). `target.py` Lusha driver wraps
   the INSURE-tree `lusha_client.py`; STUB default, `--live`/`--reveal` gated; Step-0
   free-WebSearch identity-confirm before any credit.
4. **Recall** -- fixed stale BrightData token (synced `find-insure/bright-data/api-key` to
   the valid token from `brightdata-api-key`); GA-laser + AmeriLife(Brookstone/FormulaFolios)
   + provider-agnostic disclosure-anchor sweeps (`73d4a7aa7`, `5a7e825bc`, `0052299dd`).
   Registry 315 -> 595 scored.
5. **Scorer fix** (`978f08d31`, `1aad88ff6`) -- phrasemine.py (data-driven n-gram fingerprint)
   showed `advisory services offered through` (66%) under-detected; added a core disclosure
   pattern + `pipeline.py --rescore`. Re-grade: Case B 215->238, A 123->100. Denylist
   cleanup (+TLD screen) + aggregator-term strengthen.
6. **GA lead cycle** -- `/find` GA (91 firms) -> canonical XLSX (Desktop) -> `/target` batch
   on top-15 Case-B (11 enriched, 4 Lusha-NOT_FOUND, **118 Lusha credits**, ~1085 left) ->
   one-slide-per-firm deck via deck_generation composer (12 slides, 0 lint, 11/11 coverage,
   visual-QA passed) -> `GA_DualBiz_Targets.pptx` on Desktop.

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| (none new this window) | -- | deck/xlsx delivered direct to Desktop; skills are self-documenting |

## Compiler Tools

| Tool | Result | Note |
|------|--------|------|
| `ds-commit-gate.sh` | PASS (all) | py_compile+ruff on every .py before each commit; caught E702/extraneous-f |
| `safe-commit.sh` | PASS | scoped commits; owned-paths guard correctly BLOCKED a deck_generation/ commit (DECK lane, not DS) |
| `comp-*` (graph/pipescript) | not run | FIND_DUALBIZ is a local non-Lambda pipeline not in the pipescript/graph estate; work was new-script authoring + local .runtmp medallion, no served-artifact/IAM/route surface to check |

**What worked:** ds-commit-gate caught every lint issue pre-commit; the owned-paths guard
correctly enforced the DECK lane.
**What failed:** none.
**Gap found:** `pipeline.py` reads candidates via `discover.py`'s `serp-harvested-*.json`
glob, NOT the new S2 registry -- so a discarded casec sweep still leaked into the serving
table via the glob. Registry is built + merged but not yet the pipeline's read-source
(wiring it is the open follow-on).

## Files Modified

See commit messages: `9d4725b4a 75a66c4ae 0919da613 73d4a7aa7 5a7e825bc df5b8734b 8a3a2ced2 1aad88ff6 978f08d31 0052299dd b1834b771`.
Deck tooling (`deck_generation/dev/scripts/ga_prep.py`, `ga_dualbiz_build.py`) authored
but NOT committed -- DECK-macro lane (RD/CTO/DT/AE), DS not permitted; left local. Revealed
contact PII (enriched JSON / .deck.md / pptx / pngs) deliberately uncommitted, Desktop-only.

## Blockers

None.

## Current State

- **Pipeline** `data/find/dualbiz/scripts/`: `registry.py` (S2, `config/candidates.json`
  = 595 candidates), `serp.py` (recall: provider strings + `--discover <geo>` anchor +
  brightdata serp_opal), `casec.py` (parked), `phrasemine.py`, `pipeline.py`
  (`--rescore`/`--reserve`), `cases.py` (`--case/--state/--region/--csv/--xlsx`),
  `target.py` + `batch_target.py` (Lusha). Scorer config
  `config/fingerprint-v1.json` has the new `advisory_services_offered` core pattern.
- **Serving** `.runtmp/dualbiz/2026-06-26/serving/dualbiz-targets-2026-06-26.json` (595
  firms; GA=91 B57/A21/C13).
- **Skills:** `.claude/skills/find/`, `.claude/skills/target/` (find-dualbiz removed).
- **Lusha** key `find-insure/lusha-ai/api-key` VALID, premium, ~1085 credits remaining.
- **Deliverables on Desktop:** `FIND_DUALBIZ-Georgia-2026-06-26.xlsx`,
  `dualbiz-FL-2026-06-26.csv`, `dualbiz-Southeast-2026-06-26.csv`, `GA_DualBiz_Targets.pptx`.
- **Memory:** `project_find_dualbiz_alacarte_skill_and_jim_reed_cases.md` (updated).

## Next Steps

1. [0.1.0_DS_MarketIntelligence] Wire `pipeline.py`/`discover.py` to read the S2 registry
   (close the glob-leak gap) -- pending.
2. [0.1.0_DS_MarketIntelligence] Optional: add the 4 Lusha-NOT_FOUND firms to the deck via
   website-signal-only cards or websearch domain-rescue (Andrew's call).
3. [0.4.2_RD] If wanted upstream: the DECK-lane owner may commit
   `deck_generation/dev/scripts/ga_{prep,dualbiz_build}.py` (DS cannot -- lane guard).
4. [0.1.0_DS_MarketIntelligence] Case-C producing-agency lever remains unsolved -- no real
   Case-C cohort exists in the footnote-recruited universe; needs an insurance-directory
   seed before phrasemine can characterize it.
