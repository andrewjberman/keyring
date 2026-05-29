# DS~C work-cycle 1954Z — full-24 FREE FINRA backfill + serving rebuild ((b)-depth delivered)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, SCRIBE

## Context
COO RAVC2-ACCEPT on the FINRA chain-event (7453d085c) + directive: prefer the FREE path (in-place backfill over existing .024 bronze, 0 Lusha credits) over a 52-credit re-pull. Confirmed feasible (enrich_person keys on name+firm, both verbatim in existing bronze) + GO.

## Action
- Authored `_meta/finra_backfill_existing_bronze.py` (idempotent/resumable: read bronze → enrich_person → rewrite finra_brokercheck verbatim Rule-17 → re-run silver → re-run gold). Gate-clean. Commit 51af4d256.
- Ran full-24 backfill (bg, ~8min, **0 Lusha credits**): 661 contacts, 636 newly-enriched, 76 firm+name matched, 73 series-licensed.
- Rebuilt `serving/contacts-target-2026-05-27.json` off enriched gold.
- Refreshed human brief `docs/briefs/find-insure-024-ranked-target-list-20260529.md` to the enriched ranking (supersedes pre-FINRA v1).

## Result — series-license ranking discriminates AM-transition firms
| IMO | pre-FINRA | enriched | licensed |
|---|--:|--:|--:|
| preferred-marketing-associates | 0.39 | **0.858** | 29 |
| lincoln-investment | 0.33 | **0.793** | 26 |
| integrity-marketing-group | 0.35 | 0.630 | 3 |
| gradient-financial-group | 0.26 | 0.563 | 6 |
| allianz-life | 0.32 | 0.466 | 4 |
Pure annuity/insurance tail (metlife/aig/lifepro/unkefer) unchanged ~0.25, 0 licensed = correctly NOT AM-transition.

Named licensed decision-makers now surfaced with CRDs (e.g. Brett Weeden S24/63/65/7 CRD 4913375 @ PMA; Nancy Heffner S24/6/63/65/7 CRD 1484471 @ lincoln-investment).

## Honest-nuance (per-company finra_enrichment.disposition_breakdown)
enriched_with_license / no_finra_record (genuine non-registered = true negative) / no_firm_match_recall_miss (IMO-name-vs-registered-BD gap = v2 firm_aliases target). v1 precision-first holds.

## Compiler Tools
N/A — backfill + serving are FIND_INSURE _meta/serving scripts (not in BD-gold comp-graph); ds-commit-gate run on the backfill script.

## Next Steps
- [COO] RAVC2-Accept (195458Z) on the (b)-depth serving table; relay to CTO/Andrew.
- [v2] firm_aliases IMO→affiliated-BD recall-map (closes no_firm_match_recall_miss tail; extension point in place).
