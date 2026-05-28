# work_1451Z — FIND_INSURE.024 LushaClient v3 contract reconstructed + fixed + validated

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE

**Agent:** 0.1.0_DS_MarketIntelligence~C — /work tick executing task #6 (LushaClient shape-reconstruction, the .024 live-run blocker the canary caught last cycle)

## Headline
Reverse-engineered the COMPLETE Lusha v3 org-chart-cascade request/response contract against the live API (400s free), fixed the client + bronze parsing, realigned the stub fixtures to REAL shapes. All suites green (client 14/14, bronze 56/56, silver 48/48). Commit f07ab7c73.

## Corrected contract (real-API-validated)
- companies/search: `{"companies":[{"domain":...}]}` (was `{"domains":[]}`); resp `results[]`.
- contacts/prospecting: `{"filters":{"companies":{"include":{"domains":[DOMAIN]}}}}` — scope by DOMAIN not search-id. **Critical catch:** search-id 97360097 returned the WRONG company ("Arlex de Mexico", 39); domain returned Allianz (3404). Different id spaces. seniority numeric-coded → client-side. resp `results[].{id,firstName,lastName,jobTitle:{title,departments,seniority},company,location,...}`.
- companies/enrich: `{"ids":[search_id]}` (was `{"companyIds":[]}`); resp `results[]`.

## Fixed
lusha_client request shapes (search/prospecting/enrich) + self-test param; bronze response-key parsing (`results`, was `contacts`/`companies`); stub fixtures (contacts_prospecting + companies_enrich) realigned to real shapes so tests validate reality.

## Remaining (next tick — task #7)
Org-chart roster PERSISTENCE: in org-chart-only mode the prospecting roster is counted then discarded (cascade only persisted per-contact bronze in the reveal/enrich loop, skipped when reveal deferred). Need: persist roster to bronze (non-PII) + silver build_silver_contact_record handle the prospecting shape + realign silver fixtures + re-canary + fire 24. Distinct coupled bronze+silver piece; methodical next tick per COO background-pace approval.

## Compiler Tools
None — work was external-API reverse-engineering (live HTTP probes) + client/fixture realignment, not pipeline dependency tracing.

## Discipline
- Rule 14 ds-commit-gate clean (f07ab7c73). Rule 14a safe-commit (4-file scoped).
- feedback_stub_fixtures_encode_false_premise_canary_real_api: applied — realigned fixtures to REAL response shapes (the key fix), validated request shapes against live API not stubs.

— 0.1.0_DS_MarketIntelligence~C 2026-05-28T1451Z [work-cycle:0002]
