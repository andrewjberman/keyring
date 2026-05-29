# ws-charter cycle — 2026-05-29 2008Z

**archetype:** TRACE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**CLASS:** NOVEL (Andrew-direct FIND_INSURE universe-coverage analysis + relationship-graph research)

## Inbox / direction (window since 1938Z)
- ANDREW_DIRECTION: (1) "how many of 99 have FINRA/SEC registration?"; (2) Clay API docs eval; (3) LinkedIn own-connections export (no-screenshot) feasibility. All NOVEL/research, Andrew-direct.
- DRIVE (COO): MDPF REOPENED (Andrew portal smoke, 3 FE defects); FIND_INSURE (b)-depth FINRA re-rank delivered. Both handled (concur-reopen + lesson memory; FINRA re-rank acknowledged).

## Actions
1. **registration_coverage_probe.py** (committed this tick): scans 99 source-list IMOs for SEC IAPD (RIA) + FINRA BrokerCheck (BD) firm registration, strong-match + otherNames-aware. RESULT: 46/99 RIA, 45/99 BD, 46 either, 45 both, 53 neither — HIGH-PRECISION FLOOR (no alias maps; PMA itself a false-negative → true count higher). ~half the universe is registered = the AM-transition filter for the whole list.
2. **Clay API eval** → recommend SKIP for the pipeline: Clay is no-code GTM orchestration (webhook-in/out + Clay-calls-your-endpoints), not a queryable data API; resells providers we already have free clients for (Lusha/FINRA/SEC). Doesn't solve the LI-connection-graph wall.
3. **LinkedIn own-connections export** → answered: Settings→Data Privacy→Get a copy of your data→Connections = free ToS-clean CSV (name+profile URL+company+title+connected-on), ~10min. 1st-degree only, email usually blank. This is the clean relationship-graph input: each IR member self-exports, intersect on linkedin_slug → 1st-degree warm-path map. 2nd-degree still needs Sales Nav TeamLink.
4. **FINRA re-rank validated** (DS~C 7453d085c/51af4d256, COO-accepted): series-license dimension activating de-compresses scores — PMA 0.39→0.858 (29 licensed), lincoln 0.33→0.793 (26), pure-annuity tail ~0.25 (0 licensed = correctly not-AM-transition). Surfaced the AUM-band-vs-license-count scoring tension to Andrew (big firms win license-count but bust the $6-10B ceiling → AUM band should be a soft-penalty in gold scorer; awaiting Andrew hard-filter-vs-soft-penalty call).
5. MDPF reopen: my close-concurrence was premature (data-gates passed, FE broken) → closure-discipline lesson banked (memory: portal projects need visual smoke gate). RD~B+DE dispatched, /frontend-dev visual close-gate.

## Follow-on / pending Andrew decisions
- AUM-band scoring: hard-filter vs soft-penalty (my lean: soft-penalty). Spec into gold scorer on his call.
- Relationship-graph module: connections-CSV ingestion + linkedin_slug intersection — offered to spec.
- DS~C Prudent Man deep-drill + investment-team BrokerCheck (with aliases) — in flight, RAVC2 to me.
- MDPF-FE visual-verified close (COO/RD~B/DE).
- ADVI_INFMVP: still Andrew-smoke-gated.

## Compiler Tools
ds-commit-gate on registration_coverage_probe.py (PASS) + secadv_client earlier. comp-* N/A (find/imo uninstrumented). Live public-API probes: SEC IAPD, FINRA BrokerCheck (firm+individual), Lusha, Bright Data.
