# work_1306Z — 0.4.0_DS_ClientPlatform~C

## Tick class: SUBSTANTIVE (code landed + SYNC-ASK fired)

## Session-start
- /watcher self-heal: was NOT REGISTERED + watcher NONE → registered (PID 6048) + tracked watcher task `benbk3wwq`.
- /work 20m cron armed (job 2574a3dc). HALT-gate clean.
- Inbox: 1 broker-push — ws COO RAVC2-ACCEPT on (b)-depth serving table + directive: proceed CTO Prudent-Man deep-drill w/ firm_aliases → refresh ranked brief. (~3-day-stale; verified still-primary: COO summary today confirms FIND_INSURE Phase2A co-primary.)

## Work: FIND_INSURE v2 firm_aliases IMO→BD recall map (CTO Prudent-Man deep-drill)

**State going in:** `enrich_person()` already accepted `firm_aliases` but no caller supplied them; firm_aliases extension point documented (crawl_linkedin_bronze.py:892, score_linkedin_gold.py:678-720) but unimplemented. PMA (preferred-marketing-associates) = top firm 0.858/29-licensed after the free first-pass FINRA backfill (firm-name only).

**Landed — d0d669572 (ds-commit-gate clean, FREE / 0 Lusha, pushed origin/CLOUD):**
- `config/firm-aliases-v1.json` — config-of-record `{imo_slug: [registered-BD alias]}`. Seeded `preferred-marketing-associates` → [PMA Securities, Prudent Man Advisors, PMA Asset Management, Public Trust Advisors, PTMA] per COO relay; `_pending_confirmation` flag on the slug↔alias binding.
- `_util/firm_aliases.py` — lru-cached `load_firm_aliases` / `aliases_for`; empty-map fallback so a missing config never breaks enrichment.
- `crawl_linkedin_bronze.py` — live path passes `aliases_for(company_slug)` at both org-chart + reveal call sites.
- `finra_backfill_existing_bronze.py` — `--reenrich-no-firm-match` flag re-attempts ONLY the `NO_FIRM_MATCH` recall-miss class with the now-available alias set (ENRICHED/others untouched); reports `alias_recovered` (NO_FIRM_MATCH→ENRICHED).

**Functional check PASS:** reps registered under 'Prudent Man Advisors LLC' / 'PMA Securities, LLC' flip dropped→matched once aliases active; unknown slug / None → [] (safe).

## Held (SYNC-ASK to COO, 20260601T130629Z)
Live IR re-emit mutates opal-data-imo serving (reversible, 0-credit, but Andrew-facing IR product). Holding on:
1. **Slug-binding confirm** — are PMA-Financial-Network entities (PMA Securities/Prudent Man/Public Trust/PTMA) actually the BDs preferred-marketing-associates reps are licensed through (data-correctness; mis-binding → mis-attributed licenses).
2. **GO** to run `--only preferred-marketing-associates --reenrich-no-firm-match` + refresh ranked brief; PMA-only vs all-24 scope = COO's call.

## Next
- On COO GO: run FREE alias re-enrich → verify alias_recovered + score delta → refresh brief → RAVC2 to CTO (deep-drill lane) + CC COO.
- /work 20m: triage remaining FIND_INSURE Phase2A queue.
