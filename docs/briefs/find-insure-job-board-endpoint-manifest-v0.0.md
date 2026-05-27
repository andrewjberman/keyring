# FIND_INSURE Job-Board Endpoint Manifest (v0.0 — pre-HAR template)

**Author:** 0.1.0_DS_MarketIntelligence~D
**Date:** 2026-05-27 (template land; per-board rows pending Andrew HAR drop)
**Trigger:** ws COO RAVC2-ACCEPT on Phase 2B scaffold 2026-05-27T17:25Z — Option 2 parallel-prep (lock HAR-audit output format pre-Andrew-drop)
**Anchor brief:** `org/tier2_senior/0.1.0_DS_MarketIntelligence/briefs/find_insure_phase2_part_b_jobs_scaffold.md` §2.3 (DS HAR-audit output spec)
**PRD:** `docs/architecture/FIND_INSURE.md` v0.3 §4 Phase 2 Part B Stage Bα + §9 Q6
**Status:** **v0.0 TEMPLATE — every per-board section is a SCHEMA STUB.** Per-board rows fill in at Bα HAR-audit time when Andrew HAR drops land at the canonical staging path (§3 below).

---

## 1. Purpose

This document is **the per-board endpoint disposition manifest** for FIND_INSURE Phase 2 Part B (job-postings channel). Per the scaffold brief §2.3, each board ultimately gets ONE row declaring:

- Bα-feasibility verdict (GO / GO-WITH-COOKIE / NO-GO → Bβ Bright Data fallback)
- The direct REST / GraphQL / JSON endpoint Andrew's HAR revealed (if Bα-feasible)
- Auth mechanism + rate-limit signals + bot-defense class
- Bβ Bright Data collector config (if Bα-infeasible)
- Per-IMO cost estimate

The manifest is the **contract** between DS (silver/gold parsers — consume the endpoints), AE 0.7 (bronze crawler infra — calls the endpoints), and Andrew + ws COO (sign-off on Bβ-class boards before Bright Data engagement per PRD §4 Phase 2 Part B Stage Bα).

This v0.0 is the **template** with all per-board sections empty / stub. Filling each row is the DS HAR-audit deliverable at the moment Andrew's HARs land. Locking the format NOW lets the audit collapse to a pure mechanical fill-in instead of a design-then-fill cycle.

---

## 2. Filling protocol

1. Andrew drops HARs per §3 (staging path).
2. DS~D pulls each board's `.har`; opens in browser DevTools or `mitmweb` to inspect requests.
3. For each board's request list, DS identifies the canonical endpoints (company-jobs-search + job-detail + filter-application — per scaffold brief §2.1).
4. DS fills the corresponding §4 per-board section in this manifest with the YAML row.
5. DS rolls a v0.1 commit; MCPs ws COO with `[RAVC2-Request] manifest v0.1 — N boards classified`.
6. AE 0.7 reviews Bα + Bβ dispositions; ratifies Bβ-class boards (Bright Data costs money).
7. Manifest v0.1 unlocks bronze Lambda authoring (AE) + per-board silver-parser authoring (DS).

**Privacy hygiene reminder (per scaffold brief §2.2):** raw `.har` files carry session cookies + Authorization tokens. The staging directory is gitignored AND SSE-S3 encrypted-at-rest. Only the DERIVED endpoint manifest (this document) commits to git — cookie / token VALUES are placeholder-stripped (`<COOKIE_NAME>` style); the manifest declares WHAT auth is required, not the secret VALUE.

---

## 3. HAR drop staging convention (per scaffold brief §2.2)

Andrew drops HAR captures to either:

- **Filesystem path** (canonical): `data/find/imo/_har_capture/{board-slug}/{YYYY-MM-DD}/session.har`
- **S3 path** (alternate, Andrew preference): `s3://opal-data-imo/_har_drop/{board-slug}/{YYYY-MM-DD}/session.har`

Board-slug values match the §4 sub-section anchors below (`linkedin-jobs`, `indeed`, `glassdoor`, `ziprecruiter`, `wellfound`, `builtin`).

Per-board sub-dirs prevent same-day cross-board commingling. Date-partitioned because HAR signatures rot (cookies expire, bot-defense headers mutate); re-capture cadence ~60d as signatures decay.

Q6.2 outstanding: Andrew specifies auth-class per board (anonymous / personal-account / burner-account) in a sibling `session-notes.md` per board, so DS knows the auth lane the HAR was captured under.

---

## 4. Per-board sections (TEMPLATE — fill at HAR-audit time)

### 4.1 LinkedIn Jobs (`linkedin-jobs`)

**Status:** PENDING-HAR
**Initial Bα prior (scaffold brief §3):** GO-WITH-COOKIE expected. LinkedIn requires `li_at` cookie for paginated `jobs-guest/jobs/api/seeMoreJobPostings/search` results; reverse-engineerable per known pattern.

```yaml
# FILL AT HAR-AUDIT TIME
board: linkedin-jobs
har_capture_date: ""             # YYYY-MM-DD
auth_class: ""                   # anonymous | personal-account | burner-account
B-alpha-feasibility-verdict: ""  # GO | GO-WITH-COOKIE | NO-GO
endpoints:
  company-jobs-search:
    method: ""                   # GET | POST
    url-pattern: ""              # canonical URL template
    pagination:
      mechanism: ""              # query-param-offset | cursor | page-num
      param-name: ""
      page-size: 0
  job-detail:
    method: ""
    url-pattern: ""
    extract: ""                  # html-parse | embedded-json-blob | json-response
  filter-application:
    method: ""
    url-pattern: ""
    query-params: []
auth-mechanism: ""               # anonymous | cookie:LIST | bearer | oauth
required-cookies: []             # ["li_at", "JSESSIONID"] etc.
required-headers: []             # ["csrf-token"] etc.
request-shape:
  body-format: ""                # form | json | graphql | none
  sample-body: ""                # placeholder-stripped JSON/GraphQL
response-shape: ""               # html-render | json | graphql | hybrid
rate-limit-signals:
  observed-throttle: ""          # "429 after ~N reqs/min" or "none observed"
  retry-after-header: false
  sustainable-rate: ""           # "50 req/min", etc.
bot-defense: ""                  # none | cloudflare | datadome | perimeterx | captcha-on-N | other
freshness-cadence: ""            # real-time | hourly | daily-index
B-beta-fallback-config-if-needed:
  bright-data-collector-id: ""   # required if verdict=NO-GO
  scrape-config-summary: ""
cost-comparison:
  B-alpha-cost-per-IMO: ""       # "$0/scan via direct REST" or similar
  B-beta-cost-per-IMO: ""        # "$0.XX/scan via Bright Data"
notes: ""                        # free-form observations
```

---

### 4.2 Indeed (`indeed`)

**Status:** PENDING-HAR
**Initial Bα prior (scaffold brief §3):** GO expected. Indeed has documented public `/jobs` route HTML + structured `script type="application/ld+json"` JobPosting block; HAR confirms whether SPA hydration endpoint is anonymous.

```yaml
# FILL AT HAR-AUDIT TIME
board: indeed
har_capture_date: ""
auth_class: ""
B-alpha-feasibility-verdict: ""
endpoints:
  company-jobs-search:
    method: ""
    url-pattern: ""
    pagination:
      mechanism: ""
      param-name: ""
      page-size: 0
  job-detail:
    method: ""
    url-pattern: ""
    extract: ""
  filter-application:
    method: ""
    url-pattern: ""
    query-params: []
auth-mechanism: ""
required-cookies: []
required-headers: []
request-shape:
  body-format: ""
  sample-body: ""
response-shape: ""
rate-limit-signals:
  observed-throttle: ""
  retry-after-header: false
  sustainable-rate: ""
bot-defense: ""
freshness-cadence: ""
B-beta-fallback-config-if-needed:
  bright-data-collector-id: ""
  scrape-config-summary: ""
cost-comparison:
  B-alpha-cost-per-IMO: ""
  B-beta-cost-per-IMO: ""
notes: ""
```

---

### 4.3 Glassdoor (`glassdoor`)

**Status:** PENDING-HAR
**Initial Bα prior (scaffold brief §3):** GO-WITH-COOKIE expected. Glassdoor is aggressive on bot-defense (DataDome historically); HAR will surface the bot-class + whether company-jobs view is reachable from a cookie'd session vs requires per-request rotation.

```yaml
# FILL AT HAR-AUDIT TIME
board: glassdoor
har_capture_date: ""
auth_class: ""
B-alpha-feasibility-verdict: ""
endpoints:
  company-jobs-search:
    method: ""
    url-pattern: ""
    pagination:
      mechanism: ""
      param-name: ""
      page-size: 0
  job-detail:
    method: ""
    url-pattern: ""
    extract: ""
  filter-application:
    method: ""
    url-pattern: ""
    query-params: []
auth-mechanism: ""
required-cookies: []
required-headers: []
request-shape:
  body-format: ""
  sample-body: ""
response-shape: ""
rate-limit-signals:
  observed-throttle: ""
  retry-after-header: false
  sustainable-rate: ""
bot-defense: ""
freshness-cadence: ""
B-beta-fallback-config-if-needed:
  bright-data-collector-id: ""
  scrape-config-summary: ""
cost-comparison:
  B-alpha-cost-per-IMO: ""
  B-beta-cost-per-IMO: ""
notes: ""
```

---

### 4.4 ZipRecruiter (`ziprecruiter`)

**Status:** PENDING-HAR
**Initial Bα prior (scaffold brief §3):** GO expected. Lighter bot-defense than Glassdoor historically; smaller-firm coverage layer where Indeed misses.

```yaml
# FILL AT HAR-AUDIT TIME
board: ziprecruiter
har_capture_date: ""
auth_class: ""
B-alpha-feasibility-verdict: ""
endpoints:
  company-jobs-search:
    method: ""
    url-pattern: ""
    pagination:
      mechanism: ""
      param-name: ""
      page-size: 0
  job-detail:
    method: ""
    url-pattern: ""
    extract: ""
  filter-application:
    method: ""
    url-pattern: ""
    query-params: []
auth-mechanism: ""
required-cookies: []
required-headers: []
request-shape:
  body-format: ""
  sample-body: ""
response-shape: ""
rate-limit-signals:
  observed-throttle: ""
  retry-after-header: false
  sustainable-rate: ""
bot-defense: ""
freshness-cadence: ""
B-beta-fallback-config-if-needed:
  bright-data-collector-id: ""
  scrape-config-summary: ""
cost-comparison:
  B-alpha-cost-per-IMO: ""
  B-beta-cost-per-IMO: ""
notes: ""
```

---

### 4.5 Wellfound (ex AngelList) (`wellfound`)

**Status:** PENDING-HAR
**Initial Bα prior (scaffold brief §3):** GO expected. Captures asset-management-tech-startup wing (RIA software, model-portfolio platforms) — IMOs hiring tech leads often cross-post here. Light bot-defense historically.

```yaml
# FILL AT HAR-AUDIT TIME
board: wellfound
har_capture_date: ""
auth_class: ""
B-alpha-feasibility-verdict: ""
endpoints:
  company-jobs-search:
    method: ""
    url-pattern: ""
    pagination:
      mechanism: ""
      param-name: ""
      page-size: 0
  job-detail:
    method: ""
    url-pattern: ""
    extract: ""
  filter-application:
    method: ""
    url-pattern: ""
    query-params: []
auth-mechanism: ""
required-cookies: []
required-headers: []
request-shape:
  body-format: ""
  sample-body: ""
response-shape: ""
rate-limit-signals:
  observed-throttle: ""
  retry-after-header: false
  sustainable-rate: ""
bot-defense: ""
freshness-cadence: ""
B-beta-fallback-config-if-needed:
  bright-data-collector-id: ""
  scrape-config-summary: ""
cost-comparison:
  B-alpha-cost-per-IMO: ""
  B-beta-cost-per-IMO: ""
notes: ""
```

---

### 4.6 Built In (`builtin`)

**Status:** PENDING-HAR
**Initial Bα prior (scaffold brief §3):** GO expected. Tech-role-heavy; captures CTO / Head of Eng hires that signal IMO platform-buildout activity. Minimal bot-defense historically.

```yaml
# FILL AT HAR-AUDIT TIME
board: builtin
har_capture_date: ""
auth_class: ""
B-alpha-feasibility-verdict: ""
endpoints:
  company-jobs-search:
    method: ""
    url-pattern: ""
    pagination:
      mechanism: ""
      param-name: ""
      page-size: 0
  job-detail:
    method: ""
    url-pattern: ""
    extract: ""
  filter-application:
    method: ""
    url-pattern: ""
    query-params: []
auth-mechanism: ""
required-cookies: []
required-headers: []
request-shape:
  body-format: ""
  sample-body: ""
response-shape: ""
rate-limit-signals:
  observed-throttle: ""
  retry-after-header: false
  sustainable-rate: ""
bot-defense: ""
freshness-cadence: ""
B-beta-fallback-config-if-needed:
  bright-data-collector-id: ""
  scrape-config-summary: ""
cost-comparison:
  B-alpha-cost-per-IMO: ""
  B-beta-cost-per-IMO: ""
notes: ""
```

---

## 5. Cross-board summary table (FILL AT v0.1)

After per-board fill, summarize at the top here for ws COO + AE 0.7 + Andrew at-a-glance review:

| Board | Verdict | Auth | Bot-defense | Sustainable rate | Per-IMO cost |
|---|---|---|---|---|---|
| linkedin-jobs | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ |
| indeed | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ |
| glassdoor | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ |
| ziprecruiter | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ |
| wellfound | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ |
| builtin | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ | _PENDING_ |

---

## 6. Out of v0.1 scope (deferred to v0.2+)

- Career-builder / SimplyHired / Lensa long-tail boards (scaffold brief §3 board #7).
- Direct-ATS bypass (Greenhouse / Lever / Workday) where Phase 1 web-scrape discovers a `careers.{imo-domain}` page powered by a known ATS — preferred over generic board scrape due to public ATS APIs.
- Re-capture cadence automation (Andrew-manual at v0.1; scheduled HAR-refresh in v0.2 if cookie / endpoint rot becomes operational pain).
- International boards (UK/EU/AU job-board fragmentation) — out of v0.1 because safemoneybroadcasting's 100-IMO universe is US-only.

---

## 7. Cross-references

- Scaffold brief (this template's parent): `org/tier2_senior/0.1.0_DS_MarketIntelligence/briefs/find_insure_phase2_part_b_jobs_scaffold.md`
- Parser base class consumer: `data/find/imo/scripts/_util/job_board_parser_base.py` (taxonomies + shared post-parse helpers per scaffold brief §4)
- Per-board parser landing dir: `data/find/imo/scripts/silver/job_posting/parsers/` (subclasses `JobBoardParser`)
- Pattern precedent: `docs/briefs/smartx-rest-integration-design-20260515.md` (HAR-first REST methodology)
- PRD: `docs/architecture/FIND_INSURE.md` v0.3 §4 Phase 2 Part B + §9 Q6
- Allocation brief: `org/tier1_exec/2.0.0_SA_COO/briefs/allocation_20260527T1647Z_find_insure_peak_priority.md`

---

## Authoring lineage

- **v0.0** 2026-05-27 — template scaffold ship per ws COO RAVC2-ACCEPT Option 2 parallel-prep direction 17:25Z. Locks YAML schema + per-board section anchors + filling protocol pre-Andrew-HAR-drop. Every per-board row is empty stub; fill is mechanical at HAR-audit time. Sibling artifact: `data/find/imo/scripts/_util/job_board_parser_base.py` (parser substrate consuming this manifest).
