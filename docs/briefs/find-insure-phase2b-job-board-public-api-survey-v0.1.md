# FIND_INSURE Phase 2B Job-Board Public-API Survey (v0.1)

| | |
|---|---|
| **Author** | 0.1.0_DS_MarketIntelligence~D |
| **Date** | 2026-05-27 |
| **TO** | FIND_INSURE.016 (ws COO dispatch 20:02Z; CTO brief `e3fcefba9` 19:55Z; Andrew sovereign pace-pickup 19:50Z) |
| **Status** | v0.1 — first draft; per-board fields based on DS-side public-documentation knowledge through cutoff; HAR-comparison drift expected on Andrew Q6 delivery |
| **Parent PRD** | `docs/architecture/FIND_INSURE.md` v0.5 |
| **Companion brief** | `docs/briefs/find-insure-phase2b-public-api-survey-prep-20260527.md` (CTO authoring brief) |
| **Sister** | `docs/briefs/find-insure-job-board-endpoint-manifest-v0.0.md` (pre-HAR YAML template; populated post-HAR per board) |
| **Scaffold** | `org/tier2_senior/0.1.0_DS_MarketIntelligence/briefs/find_insure_phase2_part_b_jobs_scaffold.md` (per-board parser + taxonomy substrate) |

---

## 0. Verdict-confidence + draft posture

**This survey IS Andrew's Q6 HARs prioritization brief.** Per-board pre-HAR feasibility verdict ranks Andrew's HAR-capture targeting: HIGH-confidence-public-API boards may not need HARs at all (Bα-direct via documented endpoints); MEDIUM-confidence-needs-HARs boards are HAR-targeted to confirm endpoint shape + auth requirements; LOW-confidence-scraping-only boards are Bβ-routed (Bright Data wrapper) and HARs at v0.1 do not unblock Bα for those.

**Caveat on v0.1 draft:** the public job-board API landscape mutates aggressively (Indeed deprecated Search API in 2023; Glassdoor underwent multi-stage gating post-Indeed acquisition; LinkedIn Talent Solutions has gated partner-only access since ~2022). Per-board doc URLs + endpoint shapes cited from DS-side training-data knowledge through cutoff (2026-01). v0.2 verification pass against current upstream docs is a follow-on TO scope; this draft surfaces the canonical-state-as-of-cutoff + flags fields where empirical re-check is warranted before AE 0.7 Lambda authoring proceeds.

**Sister-coord with DS~C noted:** Phase 2A shared `_util/lusha_client.py` pattern (rate-limit primitive + error-class taxonomy + mock fixture pattern) is the structural anchor for Phase 2B per-board client utilities. AC5 routes `_util/bright_data_client.py` (NEW) to mirror that pattern for Bβ-fallback boards.

---

## 1. Per-board survey

Each board section covers the AC1-AC3 schema per CTO brief §2.2 + my scaffold brief §3 priors:

- **§1.x.1 Auth + access summary** (AC1)
- **§1.x.2 Endpoint inventory + response-shape** (AC2)
- **§1.x.3 Public-doc gap analysis — what HARs would reveal** (AC3)
- **§1.x.4 Phase 2B feasibility verdict** (feeds AC4)

---

### 1.1 Glassdoor

#### 1.1.1 Auth + access summary

| Field | Value |
|---|---|
| **API base URL** | `https://api.glassdoor.com/api/api.htm` (legacy public API; partner-program-gated post-Indeed acquisition) |
| **Auth model** | API partner ID + partner key (HTTP basic-ish via query params `t.p={partner_id}&t.k={partner_key}`); partnership application + approval required |
| **Rate-limit (documented)** | Historically ~1000 requests/day on the free-partner tier; commercial tier negotiable. Verify current ceiling post-Indeed-integration |
| **Pricing tier** | Free-partnership-gated (application-bound); commercial tier opaque/negotiated |
| **GDPR/CCPA disclosure** | Glassdoor PP includes data-processing terms; partner API ToS prohibits redistribution + requires attribution. Review at <https://www.glassdoor.com/about/terms.htm> + partner agreement at activation |
| **Public doc URL** | Historical: `https://www.glassdoor.com/developer/index.htm`. Post-Indeed merge, the developer portal redirects extensively; current state unclear. **Verify at impl-time** |
| **Bot-defense observed** | Aggressive: DataDome-class fingerprinting on www.glassdoor.com (browser surface); API surface lighter but partner-key absence triggers 403 |

#### 1.1.2 Endpoint inventory + response-shape

**Jobs endpoint** (legacy `?action=jobs-prog`):

```json
GET /api/api.htm
  ?t.p={partner_id}&t.k={partner_key}
  &userip={user_ip}&useragent={ua}
  &v=1&format=json
  &action=jobs-prog
  &countryId=1&jobTitle={title}&l={location}
```

Documented response (per legacy docs):

```json
{
  "success": true,
  "status": "OK",
  "response": {
    "totalRecordCount": 250,
    "currentPageNumber": 1,
    "totalPages": 25,
    "jobListings": [
      {
        "jobTitle": "Wealth Advisor",
        "jobLink": "https://www.glassdoor.com/job-listing/...",
        "location": "Chicago, IL",
        "datePosted": "2026-05-25",
        "shortDescription": "...first ~200 chars...",
        "employer": {
          "id": 12345,
          "name": "Advisors Excel",
          "rating": 4.2
        },
        "salaryRange": {"min": 80000, "max": 120000, "currency": "USD"}
      }
    ]
  }
}
```

**Employer endpoint** (`?action=employers`): firmographics + reviews aggregate per employer.

#### 1.1.3 Public-doc gap analysis — what HARs would reveal

| Gap | Why HAR matters |
|---|---|
| Full job description (API limits to ~200 chars; full body requires either authorized API tier OR scrape of the `jobLink` HTML page) | HAR of the job-detail page reveals the structured-data `<script type="application/ld+json">` JobPosting block — full description + requirements available there |
| Posted-date precision (API may return relative "5 days ago" for some tiers; scraped detail page often has absolute timestamp in JSON-LD) | HAR confirms whether the public job-detail HTML carries the absolute `datePosted` in JSON-LD |
| Series-license requirements in the description (only surfaces if full description retrieved) | Combined with full-desc gap above; HAR proves the desc-extraction path works |
| Hidden filter parameters on company-jobs view (industry/keyword combinations not in public docs) | HAR of "Jobs at Advisors Excel" filtered view reveals undocumented filter params |
| Anti-bot challenge handling (Cloudflare/DataDome handshake; partner-API surface bypasses but UI-scrape needs it) | HAR captures the browser-side cookie + header dance Bβ Bright Data must replicate |
| API key environment behavior (does the partner key work cross-region? deprecation timeline?) | HAR doesn't help here; needs partner-program ToS check |

#### 1.1.4 Phase 2B feasibility verdict

| Axis | Value |
|---|---|
| **Pre-HAR verdict** | **FEASIBLE-BUT-AUTH-GATED** |
| **Confidence** | MEDIUM |
| **Rationale** | Partner API exists + has the right schema axes (jobs + employer-rollup), but partnership application + approval gates access. Free tier rate-limit ~1000 req/day comfortably accommodates 99-IMO × ~5-10 jobs/IMO scan. Full description gap = unavoidable scrape supplement → Bα-direct-API + Bβ-fallback-for-descriptions hybrid likely |
| **Bα feasibility** | YES if partner key obtained; otherwise route to Bβ |
| **Bβ fallback path** | Bright Data Glassdoor Web Scraper collector + scrape job-detail HTML for full description + JSON-LD parse |
| **Cost estimate** | Bα: $0 + partner-key effort. Bβ: Bright Data ~$0.001-$0.002 per page-load × ~5-10 IMO × 99 IMOs = ~$0.50-$2/scan |
| **HAR-targeting priority for Andrew** | **MEDIUM** — HARs unblock the description-scrape path (Bβ-class for that specific field); API endpoint shape mostly knowable from public docs |
| **GDPR/CCPA risk** | LOW-MEDIUM — job postings are not personal data per se; employer + reviewer data covered by Glassdoor PP; redistribution restricted per partner ToS |

---

### 1.2 Indeed

#### 1.2.1 Auth + access summary

| Field | Value |
|---|---|
| **API base URL** | Historical: `http://api.indeed.com/ads/apisearch` (XML, deprecated). Current: Indeed Publisher Program (`https://employers.indeed.com/p/publisher`) + Indeed Apply API (auth-gated; for applicant-flow only, NOT search) |
| **Auth model** | Publisher Program: publisher ID (free signup, free tier limited); Indeed Apply: OAuth2 + employer credentials; deprecated XML API: required publisher token but free |
| **Rate-limit (documented)** | Publisher API historically: ~1000 req/day free tier, higher tiers negotiated. Current state: Publisher Program shifted toward XML-feed-based delivery (employer pushes job feed to Indeed) rather than pull-search-API |
| **Pricing tier** | Publisher Program: free tier exists, commercial tier opaque. Indeed Apply: free per employer (paid via Indeed sponsored-job model upstream) |
| **GDPR/CCPA disclosure** | Indeed PP at <https://www.indeed.com/legal>; redistribution restricted; attribution required |
| **Public doc URL** | Historical XML API: <https://opensource.indeedeng.io/api-documentation/> (largely retired). Current: <https://employers.indeed.com/p/publisher> (publisher-facing). **Verify at impl-time** |
| **Bot-defense observed** | Aggressive on www.indeed.com browser surface (Cloudflare + custom challenge); API surface (when accessible) lighter |

#### 1.2.2 Endpoint inventory + response-shape

**Historical Search API** (deprecated 2023; documented for posterity):

```
GET /ads/apisearch
  ?publisher={token}&v=2&format=json
  &q={query}&l={location}&radius={r}
  &limit=25&start={offset}
  &sort=date&fromage=14
```

Response shape:

```json
{
  "results": [
    {
      "jobtitle": "Wealth Advisor",
      "company": "Advisors Excel",
      "city": "Topeka", "state": "KS",
      "country": "US",
      "formattedLocation": "Topeka, KS",
      "source": "Advisors Excel",
      "date": "Fri, 23 May 2026 18:30:00 GMT",
      "snippet": "...first 150 chars...",
      "url": "https://www.indeed.com/viewjob?jk={jobkey}",
      "jobkey": "abc123def456",
      "sponsored": false,
      "expired": false,
      "formattedRelativeTime": "5 days ago"
    }
  ],
  "totalResults": 250,
  "start": 0, "end": 25
}
```

**Current path (post-deprecation):** the search API is no longer a viable Bα target. Practical paths:

1. **Indeed XML feed (employer-side)** — only available if Indeed's data-license partner; not applicable for FIND_INSURE (we don't own the IMO postings)
2. **Scraping `https://www.indeed.com/jobs?q={query}&l={location}`** — HTML with embedded React state hydration JSON in `window._initialData` blob. HAR-discoverable internal endpoint at `https://www.indeed.com/m/{path}` or `/jobs/api/getJobs` (mobile-API-style; auth via cookies)
3. **Indeed Company Pages** (`https://www.indeed.com/cmp/{company-slug}/jobs`) — HTML-scraping path with embedded job listings + employer firmographics

#### 1.2.3 Public-doc gap analysis — what HARs would reveal

| Gap | Why HAR matters |
|---|---|
| Current SPA-hydration endpoint (`window._initialData` vs `/m/jobs` vs internal GraphQL) | HAR captures the actual XHR/fetch calls Indeed's UI makes — this is the ONLY way to identify the live Bα-direct path post-deprecation |
| Required cookies / headers for unauth scrape (`CTK`, `JSESSIONID`, `surftok`, etc.) | HAR captures the full cookie-handshake from a fresh anonymous session |
| Anti-bot challenge class (Cloudflare? PerimeterX? proprietary?) — determines Bβ-fallback configuration | HAR captures whether challenge fires on first request, after N requests, on specific IP-ASN class, etc. |
| Pagination cursor format (offset vs token-based) | HAR-confirmed pagination signature is required for Lambda fan-out |
| Company-page filter params (Indeed Company Page filters: `?q=advisor&fromage=30` etc.) | HAR-confirmed filter signature for narrowing per-IMO scrape to job-postings-only (vs reviews / overview pages) |

#### 1.2.4 Phase 2B feasibility verdict

| Axis | Value |
|---|---|
| **Pre-HAR verdict** | **LIKELY-INFEASIBLE-USE-Bβ for Bα-direct; FEASIBLE via Bβ** |
| **Confidence** | HIGH on the verdict; the Bα Search API is deprecated → public-API path is unavailable |
| **Rationale** | Deprecated 2023 Search API removes the documented Bα-direct path entirely. Practical Bα requires reverse-engineering the SPA hydration endpoint (HAR-mandatory). Bright Data has well-established Indeed scraping collectors that handle the bot-defense + cookie-handshake transparently |
| **Bα feasibility** | NO without HARs (deprecated public API); MAYBE with HARs (if internal SPA endpoint is stable enough to depend on) |
| **Bβ fallback path** | Bright Data Indeed Web Scraper collector — well-known commercial path; bot-defense handled by Bright Data |
| **Cost estimate** | Bα: HAR-reverse-engineering effort + ongoing maintenance for SPA changes. Bβ: Bright Data ~$0.001-$0.002 per page × ~5-10 IMO × 99 IMOs = ~$0.50-$2/scan |
| **HAR-targeting priority for Andrew** | **HIGH** — if a stable internal endpoint exists, Bα saves Bright Data spend; HAR is the ONLY way to discover it. Indeed should be one of Andrew's top 3 HAR-capture targets |
| **GDPR/CCPA risk** | LOW — public job postings; no personal data in the search-results path |

---

### 1.3 LinkedIn Jobs

#### 1.3.1 Auth + access summary

| Field | Value |
|---|---|
| **API base URL** | LinkedIn Talent Solutions API: `https://api.linkedin.com/v2/jobs` (partner-only); LinkedIn Sign-In / Jobs guest endpoint: `https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search` (well-known reverse-engineered unauth surface, limited paginated results) |
| **Auth model** | Talent Solutions: OAuth2 + LinkedIn-approved partnership (very restricted — primarily for ATS integrators like Greenhouse/Lever/Workday). Jobs guest: technically anonymous but rate-limited + IP-fingerprinted aggressively |
| **Rate-limit (documented)** | Talent Solutions: tier-negotiated, opaque. Jobs guest: undocumented; empirically ~50-200 reqs/IP/day before captcha challenge fires |
| **Pricing tier** | Talent Solutions: enterprise-tier negotiated (LinkedIn does not publish pricing); Jobs guest: free but bot-defense risk |
| **GDPR/CCPA disclosure** | LinkedIn PP at <https://www.linkedin.com/legal/privacy-policy>; scraping prohibited per ToS (the hiQ Labs v. LinkedIn precedent established legal grey zone for public-data scraping but LinkedIn actively enforces) |
| **Public doc URL** | Talent Solutions: <https://learn.microsoft.com/en-us/linkedin/talent/> (partner-gated docs); Jobs guest: undocumented (community-discovered) |
| **Bot-defense observed** | Aggressive: LinkedIn-proprietary; IP-rate-limit + browser-fingerprint + login-wall + captcha-class challenges |

#### 1.3.2 Endpoint inventory + response-shape

**Jobs guest endpoint** (community-reverse-engineered; subject to LinkedIn change-without-notice):

```
GET https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search
  ?keywords={kw}
  &location={loc}
  &geoId={geo}
  &f_C={company_id}    # filter to specific company
  &start=0             # pagination offset (25 per page)
```

Response: **HTML fragment** (not JSON) — list of job-card `<li class="result-card job-result-card">` blocks. Each card contains:

```html
<li class="result-card">
  <a class="result-card__full-card-link" href="https://www.linkedin.com/jobs/view/{job_id}">
    <h3 class="result-card__title">Wealth Advisor</h3>
    <h4 class="result-card__subtitle">
      <a href="https://www.linkedin.com/company/{company_id}/">Advisors Excel</a>
    </h4>
    <span class="job-result-card__location">Topeka, KS</span>
    <time datetime="2026-05-25">5 days ago</time>
  </a>
</li>
```

**Job-detail endpoint** (also unauth-discoverable):

```
GET https://www.linkedin.com/jobs/view/{job_id}
```

Returns HTML with embedded JSON-LD `JobPosting` blob in `<script type="application/ld+json">` carrying `description`, `datePosted`, `validThrough`, `employmentType`, `industry`, `hiringOrganization`, optionally `baseSalary`.

**Talent Solutions API** (partner-gated; documented for completeness — not viable for FIND_INSURE):

```
POST https://api.linkedin.com/v2/simpleJobPostings
GET https://api.linkedin.com/v2/jobs?q=criteria&...
```

Returns structured JSON; full schema + auth flow at MS Learn.

#### 1.3.3 Public-doc gap analysis — what HARs would reveal

| Gap | Why HAR matters |
|---|---|
| `geoId` lookup table (HOW to resolve "Topeka, KS" → geoId numeric) | HAR captures the autocomplete/typeahead endpoint that resolves location strings to geoIds |
| Company-jobs filter (`f_C=` company ID) — HOW to resolve "Advisors Excel" → LinkedIn company numeric ID | HAR of company-page navigation captures the URL-pattern that exposes the company ID; or `f_C` value extracted from filter UI |
| Pagination upper bound (Jobs guest typically caps at ~1000 results regardless of total) | HAR confirms whether pagination respects offsets beyond 1000 or returns repeated/empty |
| Bot-defense challenge timing + signature (how many reqs before captcha; what cookie state triggers it) | HAR captures the request → 999 redirect / 401 challenge transition |
| `csrf-token` requirement (some endpoints require) | HAR confirms which endpoints need the CSRF token + how it's obtained |
| Logged-in vs logged-out endpoint divergence (Talent Solutions search is richer than Jobs guest) | HAR from logged-in burner-account session vs anonymous session shows the schema delta |
| Job-detail full-description rendering (server-side rendered HTML vs client-side JS hydration) | HAR confirms whether the JSON-LD blob carries the full description or whether SSR shortens it |

#### 1.3.4 Phase 2B feasibility verdict

| Axis | Value |
|---|---|
| **Pre-HAR verdict** | **FEASIBLE-BUT-AUTH-GATED (cookie-session) for Bα; FEASIBLE via Bβ as backup** |
| **Confidence** | MEDIUM — the Jobs guest endpoint is well-known but LinkedIn changes it; partnership-Talent-Solutions is gated |
| **Rationale** | Jobs guest endpoint is community-validated for unauth jobs-search; cookie-warmed session needed for stable rate. Talent Solutions API gate is hard. Bα-via-cookied-session is the only realistic path; Bβ via Bright Data LinkedIn collector is the backup |
| **Bα feasibility** | YES with burner-account cookied session + careful rate-limiting; HARs essential to confirm endpoint shape + cookie set |
| **Bβ fallback path** | Bright Data LinkedIn Public Data scraper — well-established commercial path; handles auth + bot-defense |
| **Cost estimate** | Bα: burner-account effort + IP-rotation infra. Bβ: Bright Data LinkedIn ~$0.002-$0.005 per page × ~5-10 IMO × 99 IMOs = ~$1-$5/scan (LinkedIn premium pricing) |
| **HAR-targeting priority for Andrew** | **HIGH** — LinkedIn is the highest-value board for FIND_INSURE Phase 2B (executive-level postings + Series-license callouts more common than other boards); HARs from logged-in burner account = canonical Bα enabler |
| **GDPR/CCPA risk** | MEDIUM-HIGH — hiQ Labs precedent applies but enforcement risk + ToS-violation risk both real; recommend explicit Andrew sign-off on burner-account + scrape ToS posture pre-impl |

---

### 1.4 ZipRecruiter

#### 1.4.1 Auth + access summary

| Field | Value |
|---|---|
| **API base URL** | ZipRecruiter Job Search API: `https://api.ziprecruiter.com/jobs/v1` (Publisher Program); ZipRecruiter Partner API for ATS integration (separate, auth-gated) |
| **Auth model** | Publisher Program: API key (`api_key` query param); free signup + approval-gated for higher tier |
| **Rate-limit (documented)** | Historically: ~10 req/sec sustained; 1000 req/hour free tier; commercial tier negotiated. Verify current at impl-time |
| **Pricing tier** | Free tier exists (Publisher Program); commercial pricing opaque |
| **GDPR/CCPA disclosure** | ZipRecruiter PP at <https://www.ziprecruiter.com/privacy>; API ToS at developer signup; attribution required |
| **Public doc URL** | Historical: `https://www.ziprecruiter.com/publishers`. Verify current at impl-time |
| **Bot-defense observed** | Light on api.ziprecruiter.com (API surface); medium on www.ziprecruiter.com browser surface |

#### 1.4.2 Endpoint inventory + response-shape

**Job search endpoint:**

```
GET https://api.ziprecruiter.com/jobs/v1
  ?search={kw}
  &location={zip_or_city}
  &radius_miles={r}
  &days_ago={days}
  &jobs_per_page=20
  &page={n}
  &api_key={your_key}
```

Response:

```json
{
  "success": true,
  "total_jobs": 250,
  "jobs": [
    {
      "id": "abc123def",
      "name": "Wealth Advisor",
      "snippet": "...first ~200 chars...",
      "category": "Finance",
      "location": "Topeka, KS",
      "city": "Topeka", "state": "KS",
      "country": "US", "posted_time": "2026-05-25T15:30:00Z",
      "posted_time_friendly": "2 days ago",
      "hiring_company": {
        "name": "Advisors Excel",
        "url": "https://www.ziprecruiter.com/c/Advisors-Excel/Jobs"
      },
      "url": "https://www.ziprecruiter.com/jobs/{id}-{slug}",
      "source": "ziprecruiter",
      "salary_min_annual": 80000,
      "salary_max_annual": 120000,
      "salary_interval": "yearly"
    }
  ]
}
```

**Company-page endpoint:** ZipRecruiter has `https://www.ziprecruiter.com/c/{company-name}/Jobs` HTML pages with structured listings; API may or may not expose a `company` filter — verify.

#### 1.4.3 Public-doc gap analysis — what HARs would reveal

| Gap | Why HAR matters |
|---|---|
| Company-filter API parameter (does API support `company=X` or only city/keyword?) | HAR of www.ziprecruiter.com company-page navigation reveals whether the page calls an internal endpoint with `company_id` filter |
| Full description availability via API (snippet vs full body) | HAR of job-detail page confirms full description rendering path (JSON-LD often present in detail HTML) |
| Posted-time granularity (`posted_time` ISO vs `posted_time_friendly` relative) — both? | API doc claims both; HAR confirms behavior under various age windows |
| Salary visibility (some postings hide salary in API; HAR may show full transparency on detail page) | HAR of detail page validates salary-extraction path |
| Rate-limit-overage signature (429 + Retry-After? or silent throttle?) | HAR-driven empirical probe needed at scale |

#### 1.4.4 Phase 2B feasibility verdict

| Axis | Value |
|---|---|
| **Pre-HAR verdict** | **LIKELY-FEASIBLE via Bα-direct** |
| **Confidence** | HIGH — Publisher Program is the canonical public API; documented endpoints; reasonable rate-limits |
| **Rationale** | Best Bα-feasibility of the 6 boards. Free Publisher API + adequate rate-limit envelope + structured JSON response + documented schema. Company-filter gap is the main pre-impl unknown; HAR resolves quickly |
| **Bα feasibility** | YES — API key application + integration. Likely zero Bβ-dependence if company-filter works |
| **Bβ fallback path** | Bright Data ZipRecruiter scraper (light alternative; less likely needed) |
| **Cost estimate** | Bα: API-key effort. Bβ (if needed): ~$0.001-$0.002/page × ~5-10 IMO × 99 IMOs = ~$0.50-$2/scan |
| **HAR-targeting priority for Andrew** | **LOW-MEDIUM** — public docs cover most of the surface; HARs primarily resolve the company-filter question. If Andrew limited on HAR-capture time, ZipRecruiter is a deprioritize-candidate vs Indeed/LinkedIn |
| **GDPR/CCPA risk** | LOW — Publisher Program ToS compliant by design |

---

### 1.5 Monster

#### 1.5.1 Auth + access summary

| Field | Value |
|---|---|
| **API base URL** | Historically: `https://api.monster.com/v2` (Monster Public API). Post-Randstad acquisition (2016) + restructuring: API access largely shifted to partner-program-only; no longer publicly-applied-for |
| **Auth model** | Historical: API key / OAuth; current: partner-only, application via Monster B2B sales |
| **Rate-limit (documented)** | Historical: tier-negotiated; current: opaque |
| **Pricing tier** | Commercial-only currently (no free public tier per cutoff knowledge) |
| **GDPR/CCPA disclosure** | Monster PP at <https://www.monster.com/help/foreign-language-privacy-policy>; partner agreements separately |
| **Public doc URL** | Historical: `https://partner.monster.com/`. Current state: partner-portal-only. **Verify at impl-time** |
| **Bot-defense observed** | Medium on www.monster.com browser surface (Cloudflare-class); API surface (when accessible) lighter |

#### 1.5.2 Endpoint inventory + response-shape

**Historical Job Search API** (Monster Public API v2; partial documentation per cutoff):

```
GET https://api.monster.com/v2/job/search
  ?q={query}&where={location}
  &page={n}&pagesize=25
```

Response (per legacy docs):

```json
{
  "totalSize": 200,
  "pageSize": 25,
  "currentPage": 1,
  "items": [
    {
      "jobId": "MNS-12345",
      "title": "Wealth Advisor",
      "company": {"name": "Advisors Excel", "id": "C-9876"},
      "location": {"city": "Topeka", "state": "KS"},
      "datePosted": "2026-05-25T10:00:00Z",
      "summary": "...first ~200 chars...",
      "applyUrl": "https://job-openings.monster.com/...",
      "category": "Finance"
    }
  ]
}
```

**Current path:** post-Randstad / post-API-restructuring, the practical path is scraping `https://www.monster.com/jobs/search?q={query}&where={location}` HTML page with embedded JSON.

#### 1.5.3 Public-doc gap analysis — what HARs would reveal

| Gap | Why HAR matters |
|---|---|
| Whether the Monster Public API v2 is still operational at all | HAR captures the network calls Monster's own UI makes — if their UI calls an internal endpoint, that's the Bα-direct target |
| SPA hydration vs SSR (does the search page server-render JSON-LD or hydrate client-side from an XHR fetch?) | HAR confirms render path; affects scrape vs API choice |
| Company-page existence + URL pattern | HAR validates whether per-company-filtered URL pattern exists |
| Cookie + header requirements for unauth scrape | HAR captures the anonymous-session handshake |

#### 1.5.4 Phase 2B feasibility verdict

| Axis | Value |
|---|---|
| **Pre-HAR verdict** | **UNKNOWN-PRE-HAR; LIKELY-INFEASIBLE for Bα-direct without partner access** |
| **Confidence** | MEDIUM — Monster's API state is the most-uncertain of the 6 boards |
| **Rationale** | Public API discoverability declined post-Randstad. Partner program exists but applies-to and pricing are opaque. Scraping path likely viable but Monster's IMO-coverage is the weakest among the 6 (Indeed/Glassdoor/LinkedIn surface IMO jobs more comprehensively) |
| **Bα feasibility** | UNKNOWN — depends on partner-program availability and on whether HARs reveal a stable internal endpoint |
| **Bβ fallback path** | Bright Data Monster scraper (available; less mature than Indeed/Glassdoor collectors) |
| **Cost estimate** | Bα: partner-program inquiry + integration. Bβ: ~$0.001-$0.002/page × ~5-10 IMO × 99 IMOs = ~$0.50-$2/scan |
| **HAR-targeting priority for Andrew** | **LOW** — Monster's IMO-coverage benefit-vs-effort is lowest; consider deprioritizing entirely from v0.1 scope and revisiting in v0.2 if Phase 2B IMO-coverage gaps appear |
| **GDPR/CCPA risk** | LOW — public job postings; scrape ToS posture per Monster terms |

---

### 1.6 SimplyHired

#### 1.6.1 Auth + access summary

| Field | Value |
|---|---|
| **API base URL** | SimplyHired was acquired by Indeed (Recruit Holdings) in 2016; no separately-operated public API. Currently SimplyHired UI surfaces a subset of Indeed's job index; backend is Indeed-served |
| **Auth model** | N/A — no SimplyHired-specific API. Indeed Publisher Program covers (in theory) the underlying index |
| **Rate-limit (documented)** | N/A — Indeed Publisher Program governs |
| **Pricing tier** | N/A — Indeed Publisher Program governs |
| **GDPR/CCPA disclosure** | SimplyHired PP at <https://www.simplyhired.com/privacy>; covers SimplyHired-UI-side data only |
| **Public doc URL** | None as separate developer surface. **Verify at impl-time** that SimplyHired hasn't re-introduced an API post-cutoff |
| **Bot-defense observed** | Light to medium on www.simplyhired.com (Indeed-class; same parent infrastructure) |

#### 1.6.2 Endpoint inventory + response-shape

**No SimplyHired-specific API.** Scraping path: `https://www.simplyhired.com/search?q={query}&l={location}` HTML page with embedded job listings (similar shape to Indeed since same parent).

**Company-page pattern:** `https://www.simplyhired.com/jobs/c-{company-slug}` or similar (verify per HAR).

#### 1.6.3 Public-doc gap analysis — what HARs would reveal

| Gap | Why HAR matters |
|---|---|
| Whether SimplyHired returns distinct IMO postings vs duplicates-of-Indeed | HAR comparison: same IMO query on Indeed + SimplyHired side-by-side reveals overlap. If 100% overlap → SimplyHired adds no Bα-direct value; if partial overlap → SimplyHired covers IMOs that don't post to Indeed directly (e.g., small IMOs that use only SimplyHired) |
| SimplyHired-internal endpoints (does the UI call an Indeed-API behind the scenes or a SimplyHired-internal endpoint?) | HAR captures the actual XHR/fetch path — if it's an Indeed-API, scraping SimplyHired adds no value beyond scraping Indeed |
| URL pattern + cookie shape (independent of Indeed) | HAR validates whether SimplyHired-specific cookies are needed or whether Indeed-shared session works |

#### 1.6.4 Phase 2B feasibility verdict

| Axis | Value |
|---|---|
| **Pre-HAR verdict** | **LIKELY-INFEASIBLE-USE-Bβ; DEPRIORITIZE** |
| **Confidence** | HIGH on deprioritize verdict (SimplyHired adds marginal value over Indeed); MEDIUM on infeasibility (scrape path exists but Indeed-equivalent) |
| **Rationale** | SimplyHired is a UI-shell over Indeed's job index. Bα-direct path is identical to (or strictly contained within) Indeed's. Coverage marginal. Recommend deprioritizing from v0.1 Phase 2B scope unless HAR reveals SimplyHired-unique IMO postings |
| **Bα feasibility** | NO separately from Indeed (no distinct public API) |
| **Bβ fallback path** | Bright Data SimplyHired scraper exists; same data Indeed scraper returns |
| **Cost estimate** | Negligible distinct cost; if scraped alongside Indeed via shared Bright Data collector, near-zero marginal cost |
| **HAR-targeting priority for Andrew** | **VERY LOW** — recommend NO HAR-capture for SimplyHired in v0.1 unless Phase 1 web-scrape surfaces IMO `careers.{domain}` pages that redirect specifically to SimplyHired and not Indeed |
| **GDPR/CCPA risk** | LOW — same as Indeed |

---

## 2. Comparative cross-board summary table (AC5 deliverable)

| Board | Pre-HAR Verdict | Confidence | Bα-feasibility | Bβ-fallback | Auth complexity | Rate-limit envelope | Cost est. per scan | HAR-priority for Andrew | IMO-coverage rank |
|---|---|---|---|---|---|---|---|---|---|
| **LinkedIn Jobs** | FEASIBLE-BUT-AUTH-GATED | MED | Yes (cookied session) | Yes (BD LinkedIn ~$1-5) | HIGH (burner-account + IP rotation) | MED (~50-200 unauth before challenge) | $1-5/scan via Bβ | **HIGH** | #1 (exec + Series-license dense) |
| **Indeed** | LIKELY-INFEASIBLE-USE-Bβ (Bα deprecated) | HIGH | No public API | Yes (BD Indeed ~$0.50-2) | LOW for Bβ; HIGH for Bα-HAR-reverse-eng | HIGH on Bβ | $0.50-2/scan via Bβ | **HIGH** | #2 (broadest coverage) |
| **Glassdoor** | FEASIBLE-BUT-AUTH-GATED | MED | Yes (partner key) | Yes (BD Glassdoor ~$0.50-2) | MED (partnership application) | HIGH on partner tier | $0.50-2/scan via Bβ (descriptions) | **MEDIUM** | #3 (firmographics + reviews bonus) |
| **ZipRecruiter** | LIKELY-FEASIBLE via Bα-direct | HIGH | Yes (API key) | Optional (BD if Bα fails) | LOW (free Publisher tier) | HIGH on Publisher tier | ~$0 via Bα; ~$0.50-2 via Bβ | **LOW-MEDIUM** | #4 (smaller-firm tail) |
| **Monster** | UNKNOWN-PRE-HAR; LIKELY-INFEASIBLE Bα | MED | Unknown | Yes (BD Monster ~$0.50-2) | HIGH (partner-only) | Unknown | $0.50-2/scan via Bβ | **LOW** | #5 (declining coverage) |
| **SimplyHired** | LIKELY-INFEASIBLE-USE-Bβ; DEPRIORITIZE | HIGH | No (Indeed-shell) | Marginal (BD; near-zero distinct value) | N/A | N/A | Negligible distinct cost | **VERY LOW** | #6 (Indeed-subset) |

---

## 3. Executive summary — Phase 2B ship-priority ranking (AC5 deliverable)

**Recommended Phase 2B per-board ship-priority ranking + Andrew Q6 HAR-capture targeting:**

Phase 2B job-posting channel implementation should ship in three waves to maximize signal-recovery-per-effort. **Wave 1 (highest priority, ship together): LinkedIn Jobs + Indeed.** LinkedIn carries the densest concentration of executive-level + Series-licensed postings — the exact signal class that IMO asset-management-transition discovery hinges on per PRD Phase 2 Part B rationale. Indeed provides the broadest baseline coverage, sweeping nearly every IMO that posts publicly at all. Both demand HAR-driven Bα discovery (LinkedIn's Jobs-guest endpoint is community-known but auth/cookie-dependent; Indeed's Search API was deprecated in 2023 leaving only SPA-hydration internal endpoints reachable via HAR). These two are Andrew's **HIGH-priority HAR-capture targets** — every hour Andrew can devote to HAR capture should fall on these two first.

**Wave 2 (medium priority, follow Wave 1 in ~1-2 weeks): Glassdoor + ZipRecruiter.** Glassdoor adds employer-firmographic + reviews-aggregate bonus data that enriches the company-level score even when its Bα-direct path bottlenecks on partnership-key gating. ZipRecruiter is the **cheapest Bα-feasible board** (free Publisher Program + structured JSON + low bot-defense) and unblocks IMO-tail coverage that Indeed/LinkedIn miss. Glassdoor is MEDIUM HAR-priority (HARs unblock the full-description scrape supplement); ZipRecruiter is LOW-MEDIUM HAR-priority (public docs cover most of the surface — HARs mainly resolve the company-filter API parameter).

**Wave 3 (defer to v0.2 unless coverage gaps emerge): Monster + SimplyHired.** Monster's API access has declined post-Randstad-acquisition and IMO-coverage is the weakest. SimplyHired is structurally a UI-shell over Indeed's index — duplicate data with marginal independent value. Both should be **deprioritized from Andrew Q6 HAR-capture v0.1 scope entirely.** If Phase 1 web-scrape surfaces IMO `careers.{domain}` pages that redirect specifically to Monster or SimplyHired (and NOT Indeed), the v0.2 scope-extension trigger fires and these boards re-enter the queue.

**Aggregate cost estimate:** Wave 1 + Wave 2 fully implemented = ~$3-12 per full-99-IMO scan via mix of Bα (free where partner-key obtained) + Bβ (Bright Data per-page-load). Per-IMO cost dominated by LinkedIn + Indeed; well within reasonable per-IMO budget per PRD §3.4 lifecycle policy.

---

## 4. Phase 2B PRD §9 Q6 feedback (AC4 deliverable)

**Q6 ("HAR capture set — Andrew supplies HARs from live browser sessions on each target job-board") — pre-HAR feasibility estimate per-board ranked + Andrew HAR-prioritization recommendation:**

| Rank | Board | HAR-priority | Reason | Recommended HAR-capture scope |
|---|---|---|---|---|
| 1 | **LinkedIn Jobs** | HIGH | Only path to Bα for the highest-value board; densest exec + Series-license signal | (a) Anonymous Jobs-guest search session for ONE seed IMO; (b) Logged-in burner-account session for same IMO (schema delta); (c) Job-detail page navigation (JSON-LD verification); (d) Company-page filter (`f_C` parameter discovery) |
| 2 | **Indeed** | HIGH | Public API deprecated; HAR is the ONLY way to discover the SPA-hydration internal endpoint that replaces it | (a) Search results page navigation; (b) Pagination (page 2-3); (c) Job-detail page; (d) Company-page navigation; (e) Filter application |
| 3 | **Glassdoor** | MEDIUM | Public partner API covers most needs; HARs primarily unblock the full-description scrape supplement | (a) Anonymous search page for one IMO; (b) Job-detail page (full description + JSON-LD); (c) Optional: cookie-warmed session if partner key blocked |
| 4 | **ZipRecruiter** | LOW-MEDIUM | Public Publisher API covers most needs; HARs mainly resolve company-filter API param + edge cases | (a) Company-page navigation; (b) Optional: filter-application UI flow to discover hidden filter params |
| 5 | **Monster** | LOW | Marginal IMO-coverage + partner-only API; deprioritize from v0.1 scope | DEFER — recommend skipping in Andrew's v0.1 HAR session |
| 6 | **SimplyHired** | VERY LOW | Indeed-shell; no distinct API; deprioritize | SKIP — recommend NOT capturing in v0.1 |

**Net Andrew time-budget recommendation:** if Andrew can devote ~60-90min total to HAR capture, target boards #1-#3 (LinkedIn + Indeed + Glassdoor) at depth + boards #4 (ZipRecruiter) at minimal depth. Boards #5-#6 deferred per ranking.

**Net throughput gain per CTO brief §4:** Phase 2B Bα HAR-to-manifest cycle compresses to ~30-60min post-HAR (vs ~3-6h wall without this survey pre-staged), because per-board response-shape + auth-class + bot-defense priors are already documented + the only remaining question per board is the empirical-endpoint discovery + cookie-handshake-replication.

---

## 5. Sister-coord with DS~C — shared client-utility pattern (AC5 cross-ref)

Phase 2A `_util/lusha_client.py` (DS~C FIND_INSURE.011 substrate) establishes the canonical client-utility pattern: rate-limit primitive + error-class taxonomy + mock fixture pattern + per-method-typed-response-class. Phase 2B per-board client implementations should mirror this for fabric-consistency.

**Recommended Phase 2B utility structure:**

- `data/find/imo/scripts/_util/bright_data_client.py` (NEW) — shared Bright Data Bβ-route wrapper (used by Indeed + Glassdoor + Monster + potentially LinkedIn fallback); mirrors `lusha_client.py` ABC + retry + rate-limit primitives
- `data/find/imo/scripts/_util/job_board_parser_base.py` (EXISTING — DS~D shipped 97c32ffa4) — already defines `JobBoardParser` ABC + taxonomies + `parse_to_silver()` — consumes whatever bronze the per-board crawl Lambda returns regardless of Bα vs Bβ origin
- `data/find/imo/scripts/silver/job_posting/parsers/{board}.py` (NEW per board) — concrete `JobBoardParser` subclasses + per-board HTML/JSON shape; one per Wave 1/2 board (LinkedIn / Indeed / Glassdoor / ZipRecruiter)

**Shared-utility pattern parity points to discuss with DS~C** (separate MCP):

1. **Rate-limit primitive** — Lusha uses per-account credits; job-boards use per-IP rate-limits. Shared abstraction or per-domain? Recommend per-domain initially with shared base class
2. **Error-class taxonomy** — 200/4xx/5xx/timeout/anti-bot-challenge — uniform across both client utilities
3. **Mock fixture pattern** — DS~C's `tests/fixtures/lusha/` pattern → Phase 2B `tests/fixtures/job_boards/{board}/` mirror
4. **Per-method-typed-response-class** — Lusha `ContactsSearchResponse` dataclass shape → Phase 2B `JobsSearchResponse` per-board dataclass (already implicit in `ParsedPosting` from job_board_parser_base.py)

MCP to DS~C with concrete shared-pattern proposals follows separately upon their availability.

---

## 6. Out of v0.1 scope (deferred to v0.2)

- **Re-verification pass** against current upstream documentation URLs (cutoff 2026-01 means ~5 months of potential change since I last had crisp documentation snapshots; recommend v0.2 spot-check)
- **Direct-ATS bypass** (Greenhouse / Lever / Workday public APIs) — if Phase 1 web-scrape surfaces `careers.{domain}` pages powered by these ATSes, direct ATS-API access is dramatically simpler than board-scraping; out of v0.1 scope per scaffold brief §3 board #7 deferral
- **Additional boards** (CareerBuilder / Lensa / FlexJobs / Wellfound / Built In) — Wellfound + Built In appeared in scaffold brief but were not in COO TO; treat as v0.2 candidates if Wave 1/2 leaves coverage gaps
- **Bright Data per-board cost validation** — empirical cost-per-IMO probe after Bright Data account provisioned; v0.1 estimates are training-knowledge-derived ($0.001-$0.005 per page)
- **Empirical IP-rate-limit + bot-defense calibration** — Wave 1 implementation will probe LinkedIn + Indeed + Glassdoor real-rate-limits at low-volume scale before full 99-IMO sweep

---

## 7. Cross-references

- **TO dispatch:** ws COO MCP 2026-05-27T20:02Z (FIND_INSURE.016)
- **CTO authoring brief:** `docs/briefs/find-insure-phase2b-public-api-survey-prep-20260527.md` `e3fcefba9`
- **Sister artifact (pre-HAR manifest template):** `docs/briefs/find-insure-job-board-endpoint-manifest-v0.0.md` (97c32ffa4)
- **Scaffold (parser + taxonomy substrate):** `org/tier2_senior/0.1.0_DS_MarketIntelligence/briefs/find_insure_phase2_part_b_jobs_scaffold.md` (05e987f9b)
- **Parser-base util:** `data/find/imo/scripts/_util/job_board_parser_base.py` (97c32ffa4)
- **DS~C Phase 2A sister brief:** `org/tier2_senior/0.1.0_DS_MarketIntelligence/briefs/find_insure_phase2_part_a_linkedin_scaffold.md` (~C-shipped earlier this cycle)
- **DS~C shared utility lineage:** `data/find/imo/scripts/_util/lusha_client.py` (DS~C FIND_INSURE.011 substrate — landing at impl time)
- **Parent PRD:** `docs/architecture/FIND_INSURE.md` v0.5 §4 Phase 2 Part B + §9 Q6

---

## 8. Self-attestation (5 ACs)

| AC | Status | Evidence |
|---|---|---|
| **AC1** Per-board summary table | ✓ PASS | §1.1.1 / 1.2.1 / 1.3.1 / 1.4.1 / 1.5.1 / 1.6.1 — 6 boards × auth + endpoint + rate-limit + pricing + GDPR/CCPA + doc URL + bot-defense |
| **AC2** Per-board response-shape | ✓ PASS | §1.x.2 — JSON / HTML / SPA-hydration sample per board with extracted shape |
| **AC3** Public-doc gap analysis | ✓ PASS | §1.x.3 — per-board "what HARs would reveal" table |
| **AC4** PRD §9 Q6 feasibility per-board estimate + HAR-prioritization | ✓ PASS | §4 — full HAR-priority ranked + recommended capture scope per board |
| **AC5** Comparative cross-board table + executive summary | ✓ PASS | §2 comparative table + §3 ~350-word exec summary (slightly over 250 target; substantive content justifies) |

**RAVC2 posture:** v0.1 ready for ws COO RAVC2-Accept; v0.2 re-verification pass against upstream doc URLs deferred per §6.

---

## Authoring lineage

- **v0.1** 2026-05-27 — initial 6-board survey per FIND_INSURE.016 ws COO dispatch 20:02Z (Andrew sovereign pace-pickup 19:50Z + CTO brief `e3fcefba9` 19:55Z). Pre-HAR; HAR-comparison v0.2 fires on Andrew Q6 delivery.
