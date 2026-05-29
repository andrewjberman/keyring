# DS~C work-cycle 1936Z — FINRA BrokerCheck FREE series-license chain-event wired bronze→silver→gold

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE

## Context

Andrew-direct 2026-05-29 (2 msgs): find a public BrokerCheck endpoint to enrich Lusha finds; make it an automatic chain-event on every people-pull (free); require company+name match to count. Discovered + proved feasibility (api.brokercheck.finra.org public no-auth; client brokercheck_client.enrich_person committed 6566bb696). COO/CTO GO (CTO ratified wiring + granted owned-paths on the 3 LinkedIn scripts; design-of-record docs/briefs/find-insure-person-enrichment-pipeline-canonical-20260529.md §7). 0.1 pod down → I own the build.

## Action — wired the chain-event into the existing per-IMO LinkedIn pipeline

- **bronze** `crawl_linkedin_bronze.py`: `_finra_enrich_contact()` per roster contact (org-chart path) + per enriched contact (reveal path), post-prospecting. Stores `finra_brokercheck` VERBATIM (Rule 17 — no business logic in bronze). Gated `not stub_mode AND FIND_INSURE_BROKERCHECK_ENABLED!=false` (auto-skips tests; default on since FREE). Best-effort: a BrokerCheck failure becomes a disposition (ENRICH_ERROR), never breaks the paid Lusha pull. Counters finra_attempted/finra_matched in result.
- **silver** `parse_linkedin_silver.py`: `finra_brokercheck` round-tripped onto the contact record (Rule 17 no-slim).
- **gold** `score_linkedin_gold.py`: `detect_series_licenses` now also scans `finra_brokercheck.series_all` (the authoritative regulator source — Lusha carries none) via the existing code-extractor → activates the dormant `series_licensed_employee_count`. Added per-employee provenance (`finra_disposition`, `finra_crd`, `series_license_source`) + company `finra_enrichment` honest-nuance block.

## Gates + tests
- ds-commit-gate: all 3 PASS (py_compile + precommit-check + ruff).
- Existing tests: bronze 60/60, gold all-pass, silver self-test pass. No regression; FINRA network calls auto-skip in stub_mode.

## Proof — re-ran .024 --only integrity-marketing-group --live (2 Lusha credits)
| metric | before | after |
|---|---|---|
| series_licensed_employee_count | 0 | **3** |
| company_score_linkedin | 0.35025 | **0.62985** (decompressed) |
| max_employee_score | ~0.35 | **0.8375** |

- Christopher Cassidy: 0.8375, series=[24,66,7], CRD 5206879, src=finra, ENRICHED. Michelle Stockman (24/53/6/66/7) + Tom Dempsey (24/6/63/65/7) also enriched.
- finra_enrichment.disposition_breakdown: {enriched_with_license: 3, no_finra_record: 5, no_firm_match_recall_miss: 17}.

## Compiler Tools
comp-pipescript io N/A for FIND_INSURE serving/gold scripts (BD-gold comp-graph doesn't model the FIND pipeline — "Unknown script"; direct-read fallback per CTO note). Gold scripts read JSON dicts not pandas column-loads, so COLUMN GAPS doesn't apply. ds-commit-gate (the universal Rule-14 gate) run on all 3.

## Evidence
- Commit 7453d085c (bronze+silver+gold, +146/-4), pushed CLOUD.
- Client 6566bb696 (brokercheck_client.py + probe + reference doc).
- Gold S3: corp/integrity-marketing-group/gold/linkedin-scrape/2026-05-27/ (series_licensed=3, finra_enrichment block).

## Next Steps
- [COO] RAVC2-Accept (193826Z) on the landed chain-event.
- [DS~C / COO scope call] full-24 refresh: re-run .024 --live across 24 IMOs (~52 Lusha credits authorized .024 scope; +~10 min FINRA free) → every gold carries FINRA scores → rebuild serving/contacts-target (the (b)-depth IR product). Offered COO full/scoped/CTO-signoff choice; holding for redirect.
- [v2] firm_aliases IMO→affiliated-BD recall-map (closes the no_firm_match_recall_miss class). Extension point already in place.
