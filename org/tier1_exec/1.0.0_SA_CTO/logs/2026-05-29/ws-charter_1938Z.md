# ws-charter cycle — 2026-05-29 1938Z

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, COORDINATE

**CLASS:** NOVEL (Andrew-direct in-session direction — FIND_INSURE multi-source enrichment arsenal)

## Inbox classification (window since 1908Z tick)
- **ANDREW_DIRECTION** (sovereign, multiple in-session): (1) probe Bright Data LinkedIn profile scrape; (2) "linkedin url is the joinkey — make all these processes canonical for programmatic pipeline development"; (3) "render to a data shape so we can identify AUM the moment we get a business' name — it's free, program it"; (4) target band ~$6-10B AUM MAX (smaller better); (5) recursive Lusha search on Prudent Man Advisors. All NOVEL-authorized in-cycle.
- **DRIVE (COO)**: FINRA integration RAVC2; MDPF closure-assessment scope-Q. Both handled.

## Actions this window
1. **Bright Data LinkedIn scrape — probed + characterized.** Real contact (Chris Surrichio, Lincoln) proved the payload: bio/about, certifications (CFA + credential URL), activity feed, posts, recommendations, education, orgs, followers. GAP: experience field null across all tested profiles (dataset gd_l1viktl72bvl7bjuj0 doesn't reach work-history). NOT a series-license source.
2. **Canonical person-enrichment pipeline brief** (committed 9c28c80ed): linkedin_slug = person PK; 4-source map (Lusha prospecting/enrich + Bright Data + FINRA); people/{slug}/ S3 schema; silver merge; gold multi-source scoring; script dispatch sequence; §10 open Qs.
3. **secadv_client.py** (committed 635c2e0f5): FREE SEC IAPD Form ADV firm-AUM enrichment. enrich_firm_aum(name, firm_aliases) -> canonical shape (per-entity RAUM disc/non-disc + accounts + adv_employees + filing_date, family rollup + affiliation dedup-flag). IAPD multi-alias search + otherNames-aware strong-match (full-subset OR >=2-token, rejects fuzzy FPs) -> ADV PDF -> Item 5.F parse. PROVEN: PMA family = $141B across 3 RIA regs (PTMA $104B + $30B + Prudent Man $6.19B), no false positives.
4. **FINRA BrokerCheck integration** (DS~C, ratified+owned-paths-granted by me): brokercheck_client.enrich_person() wired bronze->silver->gold (7453d085c, 79999ffc6, full-24 backfill 51af4d256). Activates dormant series_licensed_employee_count. 7/25 top-25 strict-matched, all 7 real Series licenses.
5. **Prudent Man Lusha drill** (Andrew-direct): pmanetwork.com org = 118 total (vs 50 leadership cap); deep pull (40) exposed full investment desk — PMs, fixed-income/quant trading, institutional investment specialists, public-finance, GC/CCO. ~2 credits.
6. **MDPF_SCOPED closure** — joint (b) call: Phase-2b whole-page portal spins out (data-ready, not blocking); GO'd COO 3-step close. 1 of Andrew's 3 primaries done (closure commit pending COO this window).

## Sizing insight surfaced
PMA is NOT an insurance IMO transitioning to AM — it's a ~$141B public-sector/LGIP asset manager (founded 1984, 2,400+ school districts, 299 staff). Recontextualizes its #1 rank. Andrew's $6-10B-max band filters the giants (PTMA $104B/$30B) and keeps in-band entities (Prudent Man $6.19B). secadv_client is the programmatic filter.

## Follow-on / next-cycle
- MDPF_SCOPED 3-step closure commit (COO) — verify landed next tick.
- Andrew decision: (a) run secadv across all 24 IMOs to rank by $6-10B band, OR (b) keep drilling Prudent Man (remaining ~78 / BrokerCheck the investment team).
- secadv_client wiring into the canonical pipeline (company-level enricher) — pending Andrew go on scope.
- Bright Data experience-field gap — needs a different dataset_id or accept cert/activity-only.

## Compiler Tools
None gold/portal this tick — enrichment-client authoring + live API probes (Lusha/FINRA/SEC IAPD/Bright Data). ds-commit-gate run on secadv_client.py (PASS). comp-* N/A (find/imo uninstrumented at graph tier).
