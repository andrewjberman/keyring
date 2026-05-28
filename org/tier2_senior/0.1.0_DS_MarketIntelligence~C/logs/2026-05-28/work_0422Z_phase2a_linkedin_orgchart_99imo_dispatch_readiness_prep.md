# /work — Phase 2A LinkedIn org-chart 99-IMO dispatch-readiness prep

**Agent:** 0.1.0_DS_MarketIntelligence~C
**Cycle:** /work substantive tick (~04:17Z → ~04:22Z, ~5min wall — fast on existing inputs)
**Archetype:** IMPLEMENT (STANDING-PARALLEL readiness scaffold)
**Trigger:** ws COO RAVC2-ACCEPT-CLOSE + DRIVE `20260528T0417Z` (FIND_INSURE.034 follow-on)

## Context

`.034` (Lusha org-chart-only narrowing) ACCEPTED 6/6, all 3 judgment calls ruled in favor (in-place config OK, COO authors TO-record, search-and-enrich v0.7.3-defer fine). COO DRIVE'd next /goal-advancing work: pre-stage the Phase 2A LinkedIn channel dispatch infra (channel #2 of Andrew's 297-cell matrix = 99 cells) so it fires instantly on GO — analog to AE 0.7~A's web-scrape Stage 2 prep.

## Deliverables (`.runtmp/find-insure-linkedin-stage2/` — scratch, ready-to-fire)

| Artifact | Content |
|---|---|
| `generate_linkedin_stage2.py` | Generator: reads 99-IMO source list → slug (canonical slugify) + bare-domain per IMO → emits manifest + payloads |
| `linkedin-stage2-manifest.json` | 99-IMO manifest + provenance + org-chart-only endpoint declaration + dispatch-gate doc + departments-narrowing option |
| `payloads/{slug}.json` × 99 | Per-IMO `crawl_linkedin_bronze` event (company_slug + domain + seniority_filter; run_date sentinel) |
| `dispatch_linkedin_orgchart.sh` | Gated dispatch: dry-run default; `--execute` hard-blocked behind `.PHASE2A_GO` marker + Lambda-deployed check; `--subset` for Andrew Q1 cut |

## Validation

- Generator: 99 payloads, **0 missing domains**, slugs match ws-CTO-RATIFIED validation subset exactly (cambridge-investment-research, d-a-davidson-co).
- Dispatch dry-run: 99 events staged, `run_date` sentinel → actual fire-date substituted, planned `aws lambda invoke` lines enumerated.
- Dispatch `--execute` without gate: **exits 3 BLOCKED** (missing `.PHASE2A_GO`) — gate works.
- Git-Bash-3.6.7-safe (Rule 16): bash/sed/find/jq/aws/date/tr only. Fixed a Windows-jq CRLF bug (`tr -d '\r'` on slug output).

## Org-chart-only discipline (per .034)

Payloads + dispatch exercise ONLY the 3 endpoints .034 left enabled: companies/search → companies/enrich → contacts/prospecting. contacts/enrich (reveal) deferred v0.7.3 — the crawl Lambda skips it automatically while `LUSHA_CONTACT_REVEAL_ENABLED=false`. Manifest declares this explicitly.

## Risks — one resolved, one flagged

1. **RESOLVED — linkedin_company_url resolution** (COO flagged as potential `[BLOCKED-ASK]`): not needed. The crawl Lambda resolves each company by **domain** (companies/search → companyId); Lusha returns the LinkedIn URL in companies/enrich firmographics. All 99 IMOs have a website_url in the source list → 0 missing domains. No separate LinkedIn-URL data source required.
2. **FLAGGED — LinkedIn crawl ToS/cost Andrew-gate**: prep is offline scaffold, so not triggered. Baked into the dispatch GATE doc + a `[BLOCKED-ASK]`-STOP instruction at dispatch time. This is a known pre-fire consideration, not yet a live blocker.

## Dispatch gate (documented in manifest + dispatch header)

Fires ONLY after: (1) Phase 1 web-scrape close (RAVC2-Accept) AND (2) Andrew Phase-2A GO (Q1 subset-cut). `--execute` requires `.PHASE2A_GO` marker (or audited `--force-gate-ack`) AND confirms the Lambda is deployed (AE 0.7 owns deploy via imo-pipeline-vX.Y.Z) before firing. Andrew Q1 subset-cut supported via `--subset <file>`.

## Discipline / scope note

Artifacts live in `.runtmp/` (gitignored scratch) per COO TO scope — ready-to-fire dispatch infra, not committed source. This log is the git-tracked audit record. No `.py`/gold-silver-bronze edits this cycle (generator is scratch tooling, not a pipeline script) → no ds-commit-gate needed on the scratch generator; this log committed via safe-commit.

## LD-0116 routing

RAVC2-Request → ws COO; CC ws CTO (Phase 2A design) + ws CVO. No MSTR direct.

## Next Steps

1. **[ws COO]** RAVC2-ACCEPT readiness-prep; note dispatch infra ready-to-fire on Phase-1-close + Andrew Phase-2A-GO.
2. **[Andrew Q1]** subset-cut decision feeds `--subset` (top-quintile + Series-license, ~15-30 IMOs) or full-99.
3. **[Andrew]** LinkedIn crawl ToS/cost gate — surface at GO if it's a distinct sovereign decision.
4. **[AE 0.7]** `find-insure-crawl-linkedin` Lambda deploy (imo-pipeline-vX.Y.Z) is the other half of fire-readiness.
5. **[~C self-loop]** /work cron next tick; .024 still held on Andrew Q1.

— 0.1.0_DS_MarketIntelligence~C 2026-05-28T04:22Z
