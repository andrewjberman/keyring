# FIND_INSURE Phase 2B job-board public-API survey-prep brief

| | |
|---|---|
| **Author** | 1.0.0_SA_CTO |
| **Date** | 2026-05-27 |
| **Status** | DRAFT — for COO decomposition into Phase 2B pre-authoring TO (DS~D lane) |
| **Lane** | DS~D 0.1.0_DS_MarketIntelligence~D — currently STANDBY-PURE awaiting Andrew HAR drop |
| **Parent PRD** | `docs/architecture/FIND_INSURE.md` v0.5 |
| **Authority** | Andrew direct sovereign 2026-05-27T~19:50Z verbatim: "ton of DS that have just been sitting there looping /work for hours... pick up throughput here" |

---

## 1. Why this brief exists

DS~D is STANDBY-PURE awaiting Andrew HAR captures for Phase 2B Stage Bα HAR-analysis (per PRD §9 Q6 + §4 Phase 2 Part B "Stage Bα HAR-analysis primary"). HARs are gated on Andrew availability + workflow.

This brief unblocks **parallel-active publicly-documented API survey** — DS~D audits the public-facing API documentation for each target job-board (Glassdoor / Indeed / LinkedIn Jobs / ZipRecruiter / Monster / SimplyHired) + pre-stages the manifest structure. When Andrew's HARs land, DS~D compares HAR-discovered endpoints vs documented endpoints + populates the full Stage Bα manifest in ~30-60min vs ~3-6h wall.

## 2. Scope

Survey publicly-documented API endpoints for each target job-board:

### 2.1 Target boards (initial set; per PRD §4 Phase 2 Part B Stage Bα/Bβ matrix)

- **Glassdoor** — primary target; has Indeed-owned API (Indeed acquired Glassdoor); document the relationship + auth
- **Indeed** — Indeed Publisher API (XML) + Indeed Search API (deprecated 2023); document current vs deprecated state
- **LinkedIn Jobs** — LinkedIn Talent Solutions API (auth-bound + partnership-gated); document access requirements
- **ZipRecruiter** — Job Search API + Publisher Program; document endpoints + auth
- **Monster** — Job Search API; document if still available
- **SimplyHired** — owned by Indeed; document if separate API exists or just Indeed-redirect

### 2.2 Per-board survey schema

For each board, document at `docs/briefs/find-insure-job-board-public-api-survey.md`:

```yaml
board: Glassdoor
documented_endpoints:
  - method: GET
    path: /api/jobs
    auth_required: yes_oauth2
    rate_limit_documented: 1000_requests_per_day
    response_format: json
    fields_available: [job_title, company_name, location, description, posted_date, salary_range_if_visible, source_url]
    public_documentation_url: https://...
    cost_model: free_with_partnership / paid_per_call / commercial_only
    known_blockers: cloudflare_bot_detection / captcha_class
  # ... more endpoints per board

documented_api_gaps_vs_PRD_v0.5_Phase2B_needs:
  - Glassdoor API doesn't expose: posting_age (only "posted recently" relative text)
  - Glassdoor API doesn't expose: full_description (only first 200 chars; need scrape for full)
  - ...

stage_balpha_feasibility_estimate_pre_HAR:
  verdict: LIKELY_FEASIBLE_BUT_AUTH_GATED  # one of: LIKELY_FEASIBLE / FEASIBLE_BUT_AUTH_GATED / LIKELY_INFEASIBLE_USE_BBETA / UNKNOWN_PRE_HAR
  rationale: "OAuth2 with API key obtainable via Glassdoor partnership program; rate limits compatible with 99-IMO universe sweep at depth 3 (~5-10 calls/IMO; 500-1000 total well under 1000/day cap)"
  bbeta_fallback_needed_if: "partnership unavailable OR rate limit hit OR fields-of-record gap (need scrape for full description)"
```

### 2.3 Comparative summary table

End of survey: comparative table across all boards on (a) endpoint feasibility (b) auth complexity (c) rate-limit envelope vs 99-IMO universe (d) cost model (e) field-coverage vs PRD Phase 2B `silver/job-posting-scrape/` schema needs (per PRD §3.2).

Per-board verdict: prefer Stage Bα (direct REST) vs Stage Bβ (Bright Data wrapper) at PRD §3.4 lifecycle decision matrix.

### 2.4 Public-documentation gap analysis

For each board, identify what public documentation does NOT cover that HARs would reveal:
- Internal/private endpoints used by their own UI (often higher-fidelity than public API)
- Hidden filter parameters
- Bulk-export endpoints
- Search-result ranking signals
- Per-job metadata not in API response (e.g., view-count, applicant-count)

This gap analysis IS the pre-staging for HAR-comparison: when Andrew supplies HARs, DS~D quickly identifies HAR-only endpoints + populates the Stage Bα feasibility manifest with empirical-anchored data.

## 3. Pre-authoring acceptance criteria (DS~D lane)

- **AC1**: Survey output shipped at `docs/briefs/find-insure-job-board-public-api-survey.md` covering all 6 target boards with per-board schema (§2.2)
- **AC2**: Comparative summary table populated (§2.3) — per-board pre-HAR feasibility verdict (Likely Feasible / Feasible-but-auth-gated / Likely-infeasible-use-Bβ / Unknown-pre-HAR)
- **AC3**: Public-documentation gap analysis (§2.4) — per-board, what HARs would reveal that documentation doesn't
- **AC4**: PRD §9 Q6 update: pre-HAR feasibility estimate + which boards likely-Bα vs likely-Bβ — feeds Phase 2B Lambda authoring sequencing
- **AC5**: Sister-coord with DS~C (Phase 2A lane) on shared utility opportunities — does Bright Data client utility for Phase 2B share structure with Lusha client utility for Phase 2A? If yes, route to `data/find/imo/scripts/_util/bright_data_client.py` (NEW) mirroring `lusha_client.py` (per Phase 2A brief §2.4) discipline.

## 4. Sequencing — fully parallel to Andrew HAR drop

- **NOW**: DS~D starts survey + comparative analysis upon TO dispatch from ws COO
- **Andrew HARs land** (whenever): DS~D compares HAR-discovered endpoints vs documented endpoints + populates `docs/briefs/find-insure-job-board-endpoint-manifest.md` (the canonical Stage Bα manifest per PRD §4 Phase 2 Part B deliverable 1)
- **Stage Bα Lambda authoring** (post-HAR + post-manifest): per-board `crawl_job_posting_bronze.py` Lambdas with endpoint-specific call structure per manifest

Net throughput gain: survey + gap analysis done pre-HAR; HAR-to-manifest cycle compresses to ~30-60min vs ~3-6h wall.

## 5. Routing

- **Primary**: COO TO decomposition for DS~D lane (suggested TO: `FIND_INSURE.016` job-board-public-api-survey + AC2/3/4 sub-AC structure; or split into 6 per-board TOs if COO prefers parallelizing within DS~D)
- **CC**: DS~D awareness via COO routing
- **CC**: DS~C — sister-coord on shared client-utility pattern (Phase 2A brief §2.4 + Phase 2B §2 §AC5)
- **CC**: Andrew — HAR drop still standing-by'd; this brief doesn't change that ask, just provides parallel-active substrate for DS~D

## 6. Why now

Andrew direct 19:50Z: DS lanes have been sitting STANDBY for hours; pick up the pace. DS~D has been STANDBY-PURE awaiting HARs that haven't landed; meanwhile publicly-documented APIs exist + are auditable independently. This brief unblocks DS~D for parallel-active survey work that materially advances Phase 2B even without HARs in hand.

— ws CTO 2026-05-27T~19:55Z
