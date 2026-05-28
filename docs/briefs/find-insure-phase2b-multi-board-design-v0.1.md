# FIND_INSURE Phase 2B Multi-Board Parser System Design

| | |
|---|---|
| **Author** | 0.1.0_DS_MarketIntelligence~D |
| **Date** | 2026-05-27 |
| **TO** | FIND_INSURE.028 AC2 (ws COO dispatch 23:28Z) |
| **Parent PRD** | `docs/architecture/FIND_INSURE.md` v0.7 §4 Phase 2 Part B |
| **Sister artifacts** | `docs/reference/job-board-channel-architecture-matrix.md` (AC1) · `docs/reference/find-insure-phase2b-stage-routing-matrix.md` (AC3) · `docs/briefs/find-insure-phase2b-cross-board-analytics-v0.1.md` (AC4) |
| **Existing substrate** | `data/find/imo/scripts/_util/job_board_parser_base.py` (DS~D `97c32ffa4`) — `JobBoardParser` ABC + taxonomies + `parse_to_silver()` |

---

## 0. Scope + framing

This document formalizes the **per-board parser system design** for Phase 2B job-postings channel — the canonical pattern for ingesting job postings from N job-board sources into a uniform bronze → silver → gold pipeline with cross-board deduplication.

The design rests on a **two-tier abstraction**:

1. **HAR parser tier** (`har_parser_base.py` + `har_parser_{board}.py`) — extracts board-specific API request/response pairs from Andrew-supplied HAR captures, emits per-board bronze records. **NEW abstraction** (AC5 of this TO).
2. **Job-board parser tier** (`job_board_parser_base.py` + `parsers/{board}.py`) — already shipped DS~D `97c32ffa4`; consumes already-extracted payloads (from HAR parser OR live Lambda fetch), emits silver rows.

Both tiers share the canonical taxonomy already locked in `job_board_parser_base.py`: `INVESTMENT_TITLE_TERMS`, `INVESTMENT_DESCRIPTION_TERMS`, `ANTI_SIGNAL_TERMS`, `SERIES_LICENSE_NUMS`, `CREDENTIAL_TOKENS`, `ROLE_CLASSES`. Per-board parsers MUST NOT redefine these — they consume the shared taxonomy at import time.

---

## 1. Two-tier parser architecture

```
                  +---------------------------------------+
  Andrew HAR  --> | har_parser_base.HarParser (ABC)       |
  capture file    |   .extract_api_responses(har_dict)    |
                  |   .iter_postings_payload()            |
                  +---------------------------------------+
                                  |
                                  v  (per-board subclass)
                  +---------------------------------------+
                  | har_parser_{board}.py                 |
                  |   class {Board}HarParser(HarParser)   |
                  |   URL_PATTERNS = (...)                |
                  |   def extract_postings(payload, url)  |
                  +---------------------------------------+
                                  |
                                  v  (bronze emit; one .json per posting)
                  +---------------------------------------+
                  | s3://opal-data-imo/corp/{slug}/bronze/|
                  |   job-postings/{board}/{run-date}/    |
                  |   {posting_id}.json                   |
                  +---------------------------------------+
                                  |
                                  v
                  +---------------------------------------+
  Lambda fetch -> | job_board_parser_base.JobBoardParser  |
  (Bα live HTTP   |   (ALREADY SHIPPED `97c32ffa4`)       |
   or Bβ BD)      |   .parse_payload(payload, source_url) |
                  |   .parse_to_silver(...)               |
                  +---------------------------------------+
                                  |
                                  v  (silver emit; Rule 17 strict passthrough)
                  +---------------------------------------+
                  | s3://opal-data-imo/corp/{slug}/silver/|
                  |   job-postings/{run-date}/{post}.json |
                  +---------------------------------------+
                                  |
                                  v
                  +---------------------------------------+
                  | data/find/imo/scripts/gold/           |
                  |   score_jobs_gold.py                  |
                  |   (cross-board score normalization +  |
                  |    per-IMO rollup + Phase 3 emit)     |
                  +---------------------------------------+
                                  |
                                  v
                  +---------------------------------------+
                  | s3://opal-data-imo/corp/{slug}/gold/  |
                  |   job-postings/{run-date}/            |
                  |   aggregate.json                      |
                  +---------------------------------------+
```

**Why two parser tiers (not one):** HAR-tier and live-fetch-tier produce identical bronze payload shapes after extraction. The HAR tier exists to support Andrew-supplied capture as the Bα-discovery path; the live-fetch tier supports the post-discovery Lambda invocation. Same per-board parser class can consume payloads from either tier — uniform downstream pipeline.

---

## 2. `har_parser_base.py` — HAR parser ABC (AC5 design substrate)

**Purpose:** extract per-board API request/response pairs from Andrew-supplied HAR files; emit structured per-posting bronze records.

**File:** `data/find/imo/scripts/_util/har_parser_base.py` (AC5 of this TO; canonical scaffold)

**Interface (canonical design):**

```python
"""FIND_INSURE Phase 2B HAR parser abstract base class.

Per FIND_INSURE PRD v0.7 §4 Phase 2 Part B Stage Bα. Andrew supplies HAR
captures from live browser sessions on target job-boards; this base class +
per-board concrete subclasses extract the board-specific API request/response
pairs and emit structured per-posting bronze records.

Sister to JobBoardParser (data/find/imo/scripts/_util/job_board_parser_base.py)
which handles already-extracted payloads. HarParser is the layer ABOVE: it pulls
the payloads OUT of the HAR file so JobBoardParser can then parse them.

HAR file format: standard Chrome DevTools / Charles Proxy HAR (HTTP Archive)
JSON. Top-level structure:

    {"log": {"version": "1.2", "entries": [...]}}

Each entry carries:
    {"request": {"method": "GET", "url": "...", "headers": [...], ...},
     "response": {"status": 200, "content": {"text": "...", "mimeType": "..."}, ...},
     "startedDateTime": "2026-05-27T...", ...}

HarParser scans entries for board-specific URL patterns + emits the matched
response bodies for downstream extraction. Pure file I/O + JSON parsing; no
network calls.
"""
from __future__ import annotations

import json
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class HarEntry:
    """One HTTP request/response pair extracted from a HAR file."""
    url: str
    method: str
    status: int
    mime_type: str
    response_text: str
    started_at: str
    request_headers: dict[str, str]


@dataclass(frozen=True)
class ExtractedPosting:
    """One job posting extracted from a HAR response body.

    Shape mirrors `ParsedPosting` (job_board_parser_base.ParsedPosting) so
    HAR-extracted postings flow into the same downstream silver pipeline as
    live-fetch postings. The `raw_response_excerpt` field carries the
    HAR-source response excerpt for forensic re-parsing if extraction logic
    needs to be revised.
    """
    posting_id: str
    job_title: str
    full_description: str
    posted_date_relative_raw: str
    location_raw: str
    source_url: str
    raw_response_excerpt: str
    salary_min: float | None = None
    salary_max: float | None = None
    salary_currency: str | None = "USD"


class HarParser(ABC):
    """Abstract base for per-board HAR parsers.

    Subclasses set BOARD_SLUG + URL_PATTERNS + implement extract_postings().
    Base class provides load_har() + iter_matching_entries() + emit_bronze().

    Concrete example:

        class GlassdoorHarParser(HarParser):
            BOARD_SLUG = "glassdoor"
            URL_PATTERNS = (
                re.compile(r"^https://api\\.glassdoor\\.com/api/api\\.htm"),
                re.compile(r"^https://www\\.glassdoor\\.com/job-listing/"),
            )

            def extract_postings(self, entry):
                # board-specific response-shape extraction
                if entry.mime_type.startswith("application/json"):
                    data = json.loads(entry.response_text)
                    for j in data.get("response", {}).get("jobListings", []):
                        yield ExtractedPosting(
                            posting_id=str(j["jobLink"].split("/")[-1]),
                            job_title=j["jobTitle"],
                            full_description=j.get("description", ""),
                            posted_date_relative_raw=j.get("datePosted", ""),
                            location_raw=j["location"],
                            source_url=j["jobLink"],
                            raw_response_excerpt=json.dumps(j),
                        )
                # else: HTML detail page -- JSON-LD extraction, etc.
    """

    BOARD_SLUG: str = ""
    URL_PATTERNS: tuple[re.Pattern[str], ...] = ()

    def load_har(self, har_path: Path) -> dict[str, Any]:
        """Load a HAR file and return parsed JSON.

        Defensive: tolerates malformed HAR (returns empty {"log": {"entries": []}}
        + emits a warning record via parse_errors_{board}.json).
        """
        try:
            with open(har_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            return {"log": {"entries": []}, "_parse_error": str(e)}

    def iter_matching_entries(self, har: dict[str, Any]) -> Iterable[HarEntry]:
        """Yield HAR entries whose request URL matches any URL_PATTERN."""
        for entry in har.get("log", {}).get("entries", []):
            request = entry.get("request", {})
            url = request.get("url", "")
            if not any(p.search(url) for p in self.URL_PATTERNS):
                continue
            response = entry.get("response", {})
            content = response.get("content", {})
            yield HarEntry(
                url=url,
                method=request.get("method", "GET"),
                status=response.get("status", 0),
                mime_type=content.get("mimeType", ""),
                response_text=content.get("text", ""),
                started_at=entry.get("startedDateTime", ""),
                request_headers={
                    h.get("name", ""): h.get("value", "")
                    for h in request.get("headers", [])
                },
            )

    @abstractmethod
    def extract_postings(self, entry: HarEntry) -> Iterable[ExtractedPosting]:
        """Yield ExtractedPosting records from one matched HAR entry.

        Board-specific response-shape parsing lives here. Subclasses handle
        JSON / HTML / JSON-LD / GraphQL response classes per the board's
        actual surface (per docs/reference/job-board-channel-architecture-matrix.md).
        """
        raise NotImplementedError

    def parse_har(self, har_path: Path) -> list[ExtractedPosting]:
        """Top-level: load HAR + iterate matching entries + extract postings.

        Returns deduped list (postings appearing in multiple HAR entries
        deduped by posting_id; first-wins for response_excerpt).
        """
        har = self.load_har(har_path)
        seen: set[str] = set()
        postings: list[ExtractedPosting] = []
        for entry in self.iter_matching_entries(har):
            for posting in self.extract_postings(entry):
                if posting.posting_id in seen:
                    continue
                seen.add(posting.posting_id)
                postings.append(posting)
        return postings
```

**Per-board concrete subclass pattern (canonical):**

```python
# data/find/imo/scripts/_util/har_parser_linkedin_jobs.py
"""LinkedIn Jobs HAR parser -- concrete HarParser subclass."""
from __future__ import annotations

import json
import re
from typing import Iterable

from har_parser_base import ExtractedPosting, HarEntry, HarParser


class LinkedInJobsHarParser(HarParser):
    """LinkedIn Jobs HAR parser.

    Targets:
      - Jobs-guest search endpoint (HTML fragment with job-card LI blocks)
      - Job-detail page (HTML with embedded JSON-LD JobPosting blob)
      - Internal voyager API endpoints (if logged-in HAR includes them)
    """

    BOARD_SLUG = "linkedin-jobs"
    URL_PATTERNS = (
        re.compile(r"^https://www\.linkedin\.com/jobs-guest/jobs/api/seeMoreJobPostings"),
        re.compile(r"^https://www\.linkedin\.com/jobs/view/\d+"),
        re.compile(r"^https://www\.linkedin\.com/voyager/api/jobs/"),
    )

    def extract_postings(self, entry: HarEntry) -> Iterable[ExtractedPosting]:
        # ... per-LinkedIn-shape extraction; see AC1 matrix §1.1 for schema
        ...
```

**Why a separate HarParser ABC (not subsumed into JobBoardParser):** HAR processing is one-shot file I/O against an Andrew-supplied static artifact. Live Lambda fetch is per-IMO recurring network I/O. Different sourcing modes; same downstream payload contract. Separating the ABCs keeps each concern crisp: HarParser owns HAR extraction; JobBoardParser owns payload-to-silver transform.

---

## 3. `job_board_parser_base.JobBoardParser` — already-shipped substrate

**Already-shipped file:** `data/find/imo/scripts/_util/job_board_parser_base.py` (`97c32ffa4`)

**ABC interface:** subclasses set `BOARD_SLUG` + implement `parse_payload(payload: bytes, source_url: str) -> Iterable[ParsedPosting]`. Base class provides `parse_to_silver(payload, source_url, imo_slug, imo_canonical_name, bronze_path, har_endpoint_class) -> list[dict]` which:

1. Calls `self.parse_payload(payload, source_url)` to yield ParsedPosting objects
2. Attaches shared post-parse derivations: `role_class` (via `classify_role_class()`), `series_licenses_required/preferred` (via `extract_series_licenses()`), `credentials_required/preferred` (via `extract_credentials()`), `investment_title_hits/description_hits/anti_signal_hits` (via `extract_investment_hits()`), `job_title_normalized`, `posted_date` (resolved via `parse_relative_date()`), `description_word_count`
3. Attaches lineage fields: `imo_slug`, `imo_canonical_name`, `source_board`, `bronze_path`, `har_endpoint_class`, `fetched_at`
4. Returns list of silver-row dicts matching the canonical silver schema

**Existing taxonomies (NOT to be redefined by per-board parsers):**

- `INVESTMENT_TITLE_TERMS` — 22 title-class hits (HIGH signal in title)
- `INVESTMENT_DESCRIPTION_TERMS` — 27 description-class hits (MED signal in body)
- `ANTI_SIGNAL_TERMS` — 7 anti-signals (REDUCE score when present without investment-class)
- `SERIES_LICENSE_NUMS` — Series 7/63/65/66/24/6/79/82/51/52/53/22/26
- `CREDENTIAL_TOKENS` — CFA/CFP/ChFC/CPWA/CIMA/AIF
- `ROLE_CLASSES` — investment-professional/corporate-finance/technology/operations/compliance/sales/legal/other
- `_ROLE_CLASS_RULES` — title-keyword classification (first-match-wins; investment-professional tested first per "Director of Investment Operations" disambiguation)

**Per-board concrete subclass pattern (canonical):**

```python
# data/find/imo/scripts/silver/job_posting/parsers/linkedin_jobs.py
"""LinkedIn Jobs JobBoardParser -- payload to silver transform."""
from __future__ import annotations

import json
import re
from typing import Iterable

from data.find.imo.scripts._util.job_board_parser_base import (
    JobBoardParser, ParsedPosting,
)


class LinkedInJobsParser(JobBoardParser):
    """LinkedIn Jobs payload parser.

    Consumes payloads from either (a) live Lambda fetch of jobs-guest endpoint
    OR (b) HAR-extracted response bodies from LinkedInJobsHarParser. Identical
    payload shape; uniform parsing.
    """

    BOARD_SLUG = "linkedin-jobs"

    def parse_payload(self, payload: bytes, source_url: str) -> Iterable[ParsedPosting]:
        # LinkedIn Jobs-guest returns HTML fragment with <li class="result-card"> blocks
        # AND job-detail page has embedded JSON-LD JobPosting blob
        # Distinguish by source_url; parse accordingly
        text = payload.decode("utf-8", errors="replace")
        if "/jobs/view/" in source_url:
            yield from self._parse_detail_page(text, source_url)
        else:
            yield from self._parse_search_page(text, source_url)

    def _parse_search_page(self, html: str, source_url: str) -> Iterable[ParsedPosting]:
        # BeautifulSoup parsing of <li class="result-card"> blocks
        # Each posting: title + company + location + posted-date + detail-URL
        ...

    def _parse_detail_page(self, html: str, source_url: str) -> Iterable[ParsedPosting]:
        # JSON-LD <script type="application/ld+json"> extraction
        # Full description + datePosted + employmentType + hiringOrganization
        ...
```

---

## 4. Bronze schema (cross-board universal)

**Path convention:** `s3://opal-data-imo/corp/{slug}/bronze/job-postings/{board}/{run-date}/{posting_id}.json`

**Universal bronze record schema** (one record per posting; cross-board uniform with per-board metadata extension):

```json
{
  "posting_id": "linkedin-jobs:3724891234",
  "board": "linkedin-jobs",
  "imo_slug": "advisors-excel",
  "imo_canonical_name": "Advisors Excel",
  "fetched_at": "2026-05-27T18:30:00Z",
  "source_url": "https://www.linkedin.com/jobs/view/3724891234",
  "har_endpoint_class": "B-alpha-direct",
  "har_capture_id": "linkedin-jobs-2026-05-28.har",
  "raw_payload": {
    "_format": "html | json | json-ld",
    "_excerpt": "...first ~50KB of the raw response body...",
    "_full_path": "s3://.../bronze/job-postings/linkedin-jobs/2026-05-28/raw/3724891234.html"
  },
  "extracted_fields": {
    "job_title": "Wealth Advisor",
    "full_description": "...",
    "posted_date_relative_raw": "5 days ago",
    "location_raw": "Topeka, KS",
    "salary_min": null,
    "salary_max": null
  },
  "board_specific_metadata": {
    "_format": "per-board JSON blob; not silver-projected",
    "linkedin_company_id": "12345",
    "seniority_level": "Senior",
    "employment_type": "Full-time",
    "industries": ["Financial Services"]
  }
}
```

**Per-board metadata extension** (Rule 17 binding — preserved in bronze but NOT pruned at silver):

| Board | Board-specific extension fields (preserved in bronze + silver passthrough) |
|---|---|
| LinkedIn Jobs | `linkedin_company_id`, `seniority_level`, `employment_type`, `industries[]`, `applicant_count_visible` |
| Indeed | `jobkey`, `sponsored_flag`, `expired_flag`, `formatted_relative_time`, `source_employer_name_match` |
| Glassdoor | `employer.id`, `employer.rating`, `employer.review_count`, `salaryRange.{min,max}`, `currency` |
| eFinancialCareers | `specialism`, `specialism_subcategory`, `keyword_tags[]`, `seniority_level` |
| InsuranceJobs.com | `required_licenses[]` (STRUCTURED — surfaces Series + state-insurance explicitly), `specialty`, `jobType` |
| WealthManagementJobs.com | `AUM_band` (UNIQUE structured), `required_credentials[]`, `jobFunction` |
| ZipRecruiter | `category`, `salary_min_annual`, `salary_max_annual`, `salary_interval`, `posted_time_iso` |
| Built In | `tech_stack[]`, `industry_tags[]`, `salary_range`, `equity_range`, `remote_flag` |
| Wellfound | `company.{valuation, funding_stage, employee_count, industries[]}`, `equity_range`, `skills[]`, `experience_level` |

---

## 5. Silver schema (Rule 17 strict — preserves all bronze fields + adds canonical derivations)

**Path convention:** `s3://opal-data-imo/corp/{slug}/silver/job-postings/{run-date}/{posting_id}.json`

**Silver row schema** (single canonical schema produced by `JobBoardParser.parse_to_silver()` — already shipped in `97c32ffa4`):

```json
{
  "posting_id": "linkedin-jobs:3724891234",
  "imo_slug": "advisors-excel",
  "imo_canonical_name": "Advisors Excel",
  "source_board": "linkedin-jobs",
  "source_url": "https://www.linkedin.com/jobs/view/3724891234",
  "job_title": "Wealth Advisor",
  "job_title_normalized": "wealth advisor",
  "full_description": "...",
  "description_word_count": 487,
  "posted_date": "2026-05-22",
  "posted_date_relative_raw": "5 days ago",
  "fetched_at": "2026-05-27T18:30:00Z",
  "location_raw": "Topeka, KS",
  "location_city": "Topeka",
  "location_state": "KS",
  "location_remote_flag": false,
  "role_class": "investment-professional",
  "series_licenses_required": ["65"],
  "series_licenses_preferred": ["7", "66"],
  "credentials_required": [],
  "credentials_preferred": ["CFP"],
  "investment_title_hits": ["wealth advisor"],
  "investment_description_hits": ["asset management", "investment advisory", "ria"],
  "anti_signal_hits": [],
  "salary_min": null,
  "salary_max": null,
  "salary_currency": "USD",
  "salary_period": null,
  "har_endpoint_class": "B-alpha-direct",
  "bronze_path": "corp/advisors-excel/bronze/job-postings/linkedin-jobs/2026-05-28/3724891234.json",

  "board_specific_metadata": {
    "linkedin_company_id": "12345",
    "seniority_level": "Senior",
    "employment_type": "Full-time",
    "industries": ["Financial Services"]
  }
}
```

**Rule 17 binding:** `board_specific_metadata` field carries the bronze per-board extension as-is at silver. **No silver-side projection / slimming / null-handling.** Gold layer chooses what to consume from `board_specific_metadata`; silver preserves it intact.

---

## 6. Cross-board deduplication (THE per-IMO joining problem)

**Problem statement:** the same job posting often appears on 3+ boards. LinkedIn-Jobs / Indeed / Glassdoor frequently syndicate the same employer's job, sometimes with slight wording differences. Naïve scoring would triple-count a single hire — overcounting hiring velocity + investment-keyword density.

**Dedup composite-key approach** (recommended; deterministic):

```
dedup_key = sha256(
  normalize(job_title)
  + "|" + imo_slug
  + "|" + posted_date.isoformat()
  + "|" + (location_city or "") + "," + (location_state or "")
)
```

**Key fields:**

- `normalize(job_title)` — lowercase + collapse whitespace + strip punctuation (via existing `normalize_title()` helper in `job_board_parser_base.py`)
- `imo_slug` — single-source-of-truth slug per `slugify.py` shared util
- `posted_date` — absolute UTC date resolved via `parse_relative_date()`; cross-board postings have same posted_date when canonical
- `(location_city, location_state)` — handles "remote" vs city-specific listings without conflating

**Deduplication policy:**

| Scenario | Disposition |
|---|---|
| Same `dedup_key` across N boards (true syndication) | **Keep ONE silver row + emit `cross_board_observation_count = N` field + populate `seen_on_boards = [...]` array.** Counts as 1 posting; signal weighting reflects multi-board visibility. |
| Same `dedup_key` but different `posted_date` (delayed syndication) | Keep separate rows; the time-staggered postings are independent observations of the same role being reposted. |
| Different `job_title` normalizations but same `imo_slug + posted_date + location` (rephrased title) | **NEEDS HUMAN REVIEW.** Tag as `dedup_ambiguous = true`; gold layer treats as separate; v0.2 follow-on adds fuzzy-match heuristic. |
| Same `dedup_key` but different `full_description` (board-snippet vs full-text difference) | **Keep the row with longer `description_word_count`** (richer signal); attach `description_provenance = "longest-of-N"` field. |

**Cross-board signal weighting (downstream gold-tier consumer):**

A posting visible on 3+ boards gets a `cross_board_visibility_score = log2(seen_on_boards.length + 1)` boost — reflects the hiring intensity signal (employer is willing to pay for / coordinate multi-board distribution).

**Where dedup runs:** gold-tier step, BEFORE rollup. Silver retains all per-board observations (Rule 17). Gold computes dedup-collapsed view + rollup at IMO level.

---

## 7. Gold scoring pattern (cross-board score normalization)

**File:** `data/find/imo/scripts/gold/score_jobs_gold.py` (per `.025` TO AC6)

**Per-job rollup_score formula** (v0.1; tunable post-empirical):

```
rollup_score =
    w_investment_title    × count(investment_title_hits)
  + w_investment_desc     × count(investment_description_hits)
  + w_series_required     × count(series_licenses_required)
  + w_series_preferred    × count(series_licenses_preferred) × 0.5
  + w_credentials_required × count(credentials_required)
  + w_credentials_preferred × count(credentials_preferred) × 0.5
  + w_role_class           × role_class_weight[role_class]
  + w_cross_board          × cross_board_visibility_score
  + w_recency              × recency_damping_factor(posted_date, run_date)
  - w_anti_signal          × count(anti_signal_hits)
```

**Per-IMO aggregate.json schema** (per `.025` AC7):

```json
{
  "imo_slug": "advisors-excel",
  "imo_canonical_name": "Advisors Excel",
  "run_date": "2026-05-28",
  "job_postings_count": 17,
  "job_postings_count_deduped": 12,
  "boards_observed_on": ["linkedin-jobs", "indeed", "efinancialcareers", "insurancejobs-com"],
  "total_score": 487.3,
  "role_class_distribution": {
    "investment-professional": 8,
    "corporate-finance": 2,
    "technology": 1,
    "operations": 1
  },
  "series_licenses_required_aggregate": {"65": 6, "7": 3, "66": 3, "63": 1},
  "credentials_required_aggregate": {"CFP": 2, "CFA": 1},
  "investment_keyword_density": 0.42,
  "AUM_band_observed": "$500M-$1B AUM",
  "top_job_signals": [
    {"posting_id": "...", "title": "Senior Wealth Advisor", "score": 47.2},
    {"posting_id": "...", "title": "Portfolio Manager", "score": 41.8}
  ],
  "aggregated_hiring_signal_class": "high-conviction-buildout",
  "hiring_velocity_30d": 4,
  "hiring_velocity_90d": 11,
  "hiring_velocity_180d": 17,
  "tech_hire_forward_signal_count": 1,
  "corp_finance_forward_signal_count": 2
}
```

**`aggregated_hiring_signal_class`** enum (feeds Phase 3 `serving/scoring.json` `hiring_signal_class` field per CVO ADDITIVE-1):

- `high-conviction-buildout` — >= 5 investment-professional postings OR >= 3 with Series-65/66 required
- `medium-conviction-growth` — 2-4 investment-professional postings OR forward-signal (corp-finance/tech-hire) >= 2
- `low-signal-baseline` — 0-1 investment-professional postings AND <= 1 forward-signal
- `quiet` — 0 job-postings observed across all boards

---

## 8. Per-board test-fixture pattern

**File convention:** `data/find/imo/tests/fixtures/phase2b/{board}/`

**Per-board fixture suite** (mirrors DS~C `tests/fixtures/lusha/` pattern):

```
data/find/imo/tests/fixtures/phase2b/
  linkedin-jobs/
    har/
      linkedin-jobs-2026-05-28-sample.har         # sanitized synthetic HAR (no PII)
    search_page_response.html                    # raw HTML from search endpoint
    detail_page_response.html                    # raw HTML from job-detail page
    expected_postings.json                       # canonical ExtractedPosting list
    expected_silver_rows.json                    # canonical silver-row list post parse_to_silver()
  indeed/
    har/
      indeed-2026-05-28-sample.har
    spa_hydration_response.json
    detail_page_response.html
    expected_postings.json
    expected_silver_rows.json
  ... (one per board)
```

**Per-board test pattern:**

```python
# data/find/imo/tests/test_parser_linkedin_jobs.py
def test_linkedin_jobs_har_extraction():
    parser = LinkedInJobsHarParser()
    postings = parser.parse_har(Path("tests/fixtures/phase2b/linkedin-jobs/har/linkedin-jobs-2026-05-28-sample.har"))
    expected = json.load(open("tests/fixtures/phase2b/linkedin-jobs/expected_postings.json"))
    assert len(postings) == len(expected)
    for got, exp in zip(postings, expected):
        assert got.posting_id == exp["posting_id"]
        assert got.job_title == exp["job_title"]
        # ... per-field assertion

def test_linkedin_jobs_silver_transform():
    parser = LinkedInJobsParser()
    with open("tests/fixtures/phase2b/linkedin-jobs/search_page_response.html", "rb") as f:
        payload = f.read()
    silver_rows = parser.parse_to_silver(
        payload=payload,
        source_url="https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Wealth+Advisor&f_C=12345",
        imo_slug="advisors-excel",
        imo_canonical_name="Advisors Excel",
        bronze_path="corp/advisors-excel/bronze/job-postings/linkedin-jobs/2026-05-28/sample.json",
        har_endpoint_class="B-alpha-direct",
    )
    expected = json.load(open("tests/fixtures/phase2b/linkedin-jobs/expected_silver_rows.json"))
    assert silver_rows == expected
```

**Minimum per-board test coverage (v0.1):**

- 1× HAR extraction test (validates URL_PATTERNS match + extract_postings produces expected count + per-field values for ≥1 posting)
- 1× silver transform test (validates parse_to_silver produces expected canonical row including taxonomy-derived fields)
- 1× malformed-HAR graceful-degradation test (load_har returns empty result + parse_errors emit)
- 1× cross-board dedup test (synthetic 3-board overlap → single deduped silver-row with `cross_board_observation_count = 3`)

---

## 9. Per-board parser implementation roadmap

| Board | HAR parser path | JobBoardParser path | Lambda fetch path | Est. impl effort |
|---|---|---|---|---|
| LinkedIn Jobs | `_util/har_parser_linkedin_jobs.py` | `silver/job_posting/parsers/linkedin_jobs.py` | `bronze/crawl_job_posting_linkedin_jobs_bronze.py` | ~2h (HTML + JSON-LD hybrid) |
| Indeed | `_util/har_parser_indeed.py` | `silver/job_posting/parsers/indeed.py` | `bronze/crawl_job_posting_indeed_bronze.py` | ~2h (SPA hydration extraction) |
| Glassdoor | `_util/har_parser_glassdoor.py` | `silver/job_posting/parsers/glassdoor.py` | `bronze/crawl_job_posting_glassdoor_bronze.py` | ~1.5h (partner-API JSON + scrape supplement) |
| eFinancialCareers | `_util/har_parser_efinancialcareers.py` | `silver/job_posting/parsers/efinancialcareers.py` | `bronze/crawl_job_posting_efinancialcareers_bronze.py` | ~1h (clean internal endpoint) |
| InsuranceJobs.com | `_util/har_parser_insurancejobs.py` | `silver/job_posting/parsers/insurancejobs.py` | `bronze/crawl_job_posting_insurancejobs_bronze.py` | ~1h (RSS + light scrape; structured required_licenses) |
| WealthManagementJobs.com | `_util/har_parser_wealthmanagementjobs.py` | `silver/job_posting/parsers/wealthmanagementjobs.py` | `bronze/crawl_job_posting_wealthmanagementjobs_bronze.py` | ~1h (structured AUM_band) |
| ZipRecruiter | `_util/har_parser_ziprecruiter.py` | `silver/job_posting/parsers/ziprecruiter.py` | `bronze/crawl_job_posting_ziprecruiter_bronze.py` | ~45min (clean Publisher API JSON) |
| Built In | `_util/har_parser_builtin.py` | `silver/job_posting/parsers/builtin.py` | `bronze/crawl_job_posting_builtin_bronze.py` | ~1h (HTML + structured tech_stack) |

**Wave 1 ship effort:** ~7.5h (LinkedIn + Indeed + eFinancialCareers + InsuranceJobs.com)
**Wave 2 ship effort:** ~3.5h (Glassdoor + WealthManagementJobs.com + ZipRecruiter)
**Wave 3 ship effort:** ~2h (Built In + others as needed)

**Parallel feasibility:** per-board parser ships are mechanical-fill once HAR is in hand; ws COO can spawn additional tilde-lanes for parallel ship if Andrew HAR supply is bulk-delivered. Recommended: single DS~D lane for Wave 1 (preserves cross-board consistency review at ship-time); parallelize Wave 2 across 2 lanes if capacity allows.

---

## 10. Cross-references

- **AC1 board architecture matrix:** `docs/reference/job-board-channel-architecture-matrix.md` (sister this TO)
- **AC3 Stage Bα/Bβ routing matrix:** `docs/reference/find-insure-phase2b-stage-routing-matrix.md` (sister this TO)
- **AC4 cross-board analytics framework:** `docs/briefs/find-insure-phase2b-cross-board-analytics-v0.1.md` (sister this TO)
- **AC5 har_parser_base.py scaffold:** `data/find/imo/scripts/_util/har_parser_base.py` (sister AC5 of this TO)
- **JobBoardParser base ABC (already shipped):** `data/find/imo/scripts/_util/job_board_parser_base.py` (DS~D `97c32ffa4`)
- **Pre-HAR manifest template:** `docs/briefs/find-insure-job-board-endpoint-manifest-v0.0.md` (DS~D `97c32ffa4`)
- **Phase 2B Lambda scaffold (AE 0.7~B side):** `docs/briefs/find-insure-phase2b-per-board-lambda-scaffold-v0.0.md` (`33d6bcc1f`)
- **`.025` HAR parser execution TO:** `org/tier2_senior/0.1.0_DS_MarketIntelligence~D/task_orders/FIND_INSURE.025.dsd-phase2b-stage-ba-har-parser.md`
- **CLAUDE.md Rule 17 (silver passthrough discipline):** `CLAUDE.md` §17
- **CLAUDE.md Rule 14 + 14a (commit gates):** `CLAUDE.md` §14, §14a
- **CVO ADDITIVE-1 (hiring-signal-class):** Phase 3 serving consolidation FIND_INSURE.023
- **Parent PRD:** `docs/architecture/FIND_INSURE.md` v0.7 §4 Phase 2 Part B

---

## 11. Authoring lineage

- **v0.1** 2026-05-27 — initial multi-board parser system design per FIND_INSURE.028 AC2 ws COO dispatch 23:28Z. Formalizes two-tier abstraction (HarParser + JobBoardParser) building on already-shipped `job_board_parser_base.py` (DS~D `97c32ffa4`). Defines cross-board dedup composite-key + per-board test-fixture pattern. v0.2 follow-on on first-empirical run will calibrate role_class weights + cross-board visibility multiplier + recency damping + fuzzy-match heuristic for ambiguous-title dedup.
