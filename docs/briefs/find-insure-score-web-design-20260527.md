# FIND_INSURE Phase 1 `score-web` Lambda — Design Brief (STANDBY-PREP draft)

**Status:** STANDBY-PREP pre-TO; silver→gold contract LOCKED v0.2 per ~A `[SILVER-SCHEMA]` 17:10Z. Refines on FIND_INSURE.006 GO.
**Authored:** 2026-05-27T~17:05Z by 0.1.0_DS_MarketIntelligence~B (v0.2 update 17:15Z post sister-coord LOCK)
**Anchor:** FIND_INSURE PRD v0.3 §4 Phase 1 deliverable 3
**Spawn:** MSTR SPAWN-WITH-DIRECTION 2026-05-27T16:49Z per Andrew sovereign 16:46Z peak-priority + ws COO /allocation #3 brief
**Sister:** 0.1.0_DS_MarketIntelligence~A — `parse-web` Lambda (silver tier); parse-web design brief `752b1fcee` at `org/tier2_senior/0.1.0_DS_MarketIntelligence/briefs/find_insure_parse_web_design_20260527.md`

## 1. Purpose

Scan per-IMO silver-tier structured-content output for asset-management-transition indicator terms; emit per-match and per-IMO scored output to gold tier. The first programmatic signal that ranks the 100-IMO universe for the Phase 1 -> Phase 2 cut decision.

## 2. Inputs (silver-tier contract — LOCKED v0.2 per ~A `[SILVER-SCHEMA]` 17:10Z)

Reads from `s3://opal-data-imo/corp/{slug}/silver/web-scrape/{YYYY-MM-DD}/{url_hash}.json` (flat per-page layout; `url_hash = sha256(url)[:16]`).

**Per-page silver record** (all fields preserved per CLAUDE.md Rule 17 + ~A v0.2):

| Field | Type | Score-web use |
|---|---|---|
| `url` | string | per-match `page_url` |
| `url_hash` | string | per-match join key to silver (replaces fragile URL string keying) |
| `fetched_at` | ISO-8601 UTC | per-match `crawl_ts` |
| `http_status` | int | filter for skip / blocked classification |
| `content_type` | string | filter (only `text/html`-class scanned) |
| `bronze_key` | string | provenance pass-through (optional in gold) |
| `content_hash` | string | provenance pass-through (optional in gold) |
| `page_text` | string \| null | BODY scan source (location_class=`body`); `null` = blocked-page skip |
| `title` | string \| null | TITLE scan source (location_class=`title`, multiplier 3.0) |
| `meta_tags` | dict (no whitelist) | scan `description`, `og:title`, `og:description`, `keywords` (per location_multiplier table) |
| `headings` | dict {h1..h6: list[str]} | per-level scan (location_class=`h1`..`h6`) |
| `links_internal` / `links_external` | list[{href, absolute_url, anchor_text, rel}] | ANCHOR_TEXT scan (location_class=`anchor_text`) |
| `contact_blocks` | dict {addresses, emails, phones} | ADDRESS_BLOCK scan (location_class=`address_block`) |
| `structured_data` | dict {json_ld, schema_org} | SCAN as additional high-signal class (location_class=`structured_data`, multiplier ~2.0 — schema.org markup often declares Organization roles + services) |

**Blocked-page record** (`page_text = null`, `blocked_reason` set): score-web emits ZERO matches for that page; OPTIONAL counter row in `summary.json.skipped_pages_by_reason` for audit completeness.

## 3. Outputs (gold-tier contract)

Writes to `s3://opal-data-imo/corp/{slug}/gold/web-scrape/{YYYY-MM-DD}/` (per PRD v0.3 §3.2 `corp/{slug}/{medallion}/{channel}/{date}/` convention).

### 3.1 `matches.json` (or `.parquet` — defer to AE 0.7 on format pref)

One record per term-match:

```json
{
  "slug": "advisors-excel",
  "page_url": "https://www.advisorsexcel.com/about",
  "url_hash": "a1b2c3d4e5f6a7b8",
  "term": "Series 65",
  "term_class": "licensure",
  "match_type": "regex",
  "context_window": "...our advisors hold Series 65 licenses and...",
  "location_class": "body",
  "location_multiplier": 1.0,
  "class_weight": 4.0,
  "score_contribution": 4.0,
  "crawl_ts": "2026-05-27T16:00:00Z",
  "taxonomy_version": "0.1.0"
}
```

`url_hash` added per ~A suggestion — fragile-URL-string-key avoidance for silver↔gold rejoin.

### 3.2 `summary.json`

Per-IMO rollup:

```json
{
  "slug": "advisors-excel",
  "run_date": "2026-05-27",
  "total_score": 187.5,
  "page_count_scanned": 23,
  "page_count_with_matches": 14,
  "match_count_total": 89,
  "by_class": {
    "transition_signal": {"score": 50.0, "match_count": 10, "unique_terms": 5},
    "licensure": {"score": 64.0, "match_count": 16, "unique_terms": 8},
    "aum_vehicles": {"score": 33.0, "match_count": 11, "unique_terms": 7},
    "fiduciary_regulatory": {"score": 24.0, "match_count": 6, "unique_terms": 4},
    "advisory_vocabulary": {"score": 12.0, "match_count": 6, "unique_terms": 3},
    "org_structure": {"score": 0, "match_count": 0, "unique_terms": 0},
    "platform_partnership": {"score": 4.5, "match_count": 1, "unique_terms": 1}
  },
  "skipped_pages_by_reason": {"robots": 0, "http_4xx": 2, "http_5xx": 0, "rate_limit": 0, "non_html": 1, "parse_error": 0},
  "top_terms": [
    {"term": "Series 65", "class": "licensure", "count": 6},
    {"term": "fiduciary", "class": "fiduciary_regulatory", "count": 5},
    {"term": "AUM", "class": "aum_vehicles", "count": 4}
  ],
  "taxonomy_version": "0.1.0",
  "scored_at": "2026-05-27T17:30:00Z"
}
```

## 4. Term taxonomy

Source: `data/find/imo/scripts/gold/term_taxonomy.json` v0.1.0 (drafted parallel to this brief).

7 classes (`transition_signal` 5.0 / `licensure` 4.0 / `fiduciary_regulatory` 4.0 / `org_structure` 3.5 / `aum_vehicles` 3.0 / `platform_partnership` 2.5 / `advisory_vocabulary` 2.0); ~80 terms total. PRD §4 17-seed list fully covered; ~63 adjacent regulatory + asset-mgmt vocabulary terms added per spawn-msg direction.

**Versioning:** taxonomy emitted to `s3://opal-data-imo/config/term-taxonomy-v0.1.json` at deploy time (mirrors PRD v0.3 `config/` prefix convention). Gold output records `taxonomy_version` for reproducibility.

## 5. Scoring algorithm

```
for each silver record (page):
  for each text region (title, h1-h6, meta_description, anchor_text, body_text, address_blocks):
    for each term in taxonomy:
      matches = find_matches(region_text, term)  # word/phrase/regex per term.match
      for each match:
        location_mul = location_multipliers[region_class]
        contribution = term.class_weight * location_mul
        emit match record to matches.json
        accumulate per-class + per-IMO summary

per_imo_summary:
  total_score = sum(all match score_contribution)
  by_class = {class: {score, match_count, unique_terms}}
  top_terms = highest-count terms across all classes
  emit summary.json
```

**Term-match implementation:**
- `match=word`: word-boundary anchored regex `\bTERM\b`, case-insensitive
- `match=phrase`: word-boundary anchored regex `\bTERM\b` with internal whitespace normalized, case-insensitive
- `match=regex`: explicit pattern field from taxonomy

**Context window:** ~80 chars before + 80 chars after match position; clipped at sentence boundaries where possible.

## 6. Lambda architecture (sketch)

- **Runtime:** Python 3.9 (matches existing Opal Lambda baseline; from-future-import annotations per CLAUDE.md Rule 15)
- **Trigger:** EventBridge fan-out (per PRD §3.4 Phase 1 fan-out diagram); one invocation per `{slug}` per run-date
- **Memory / timeout:** TBD per CLAUDE.md Rule 5 — initial sizing 512 MB / 5 min (silver-side I/O bounded; term-match CPU bounded by page count, expected <500 pages/IMO); refine post-first-end-to-end-run
- **Layer:** Python stdlib only for v0.1 (re module + json + boto3 from Lambda default layer); no new layer
- **IAM:** read silver/web-scrape + config/, write gold/web-scrape, CloudWatch Logs
- **Input handler:** event = `{"slug": "advisors-excel", "run_date": "2026-05-27"}` or S3 PutObject event with prefix-pattern
- **Idempotence:** re-running for same `{slug, run_date}` overwrites gold output deterministically; matches.json + summary.json fully derived from silver + taxonomy

## 7. Acceptance criteria (proposed — TO authoring will finalize)

- **AC1:** `score_web.py` Lambda authored under `data/find/imo/scripts/gold/` per PRD path convention + Rule 13 DS-owned cycle
- **AC2:** `term_taxonomy.json` v0.1.0 shipped at canonical path; ≥30 terms across ≥5 classes; PRD §4 17-seed list fully included
- **AC3:** Self-test cases: ~5 hand-curated silver records produce expected gold output (including: zero-match record, single-class record, multi-class record, regex-class record)
- **AC4:** End-to-end run against full Phase-1 universe (downstream of AE 0.7 `crawl-web` + ~A `parse-web`) produces gold/web-scrape/{slug}/{run-date}/ for ≥90% of source-list IMOs
- **AC5:** Sample manual review of 10 IMOs — term-detection logic agrees with human reading on direction (does this site read as asset-mgmt-transition-signaling, yes/no, vs the score)
- **AC6:** Taxonomy version pinned in gold output; bumping taxonomy version doesn't silently re-score historical run-dates

## 8. Risk / open questions

- **Q1: per-page vs per-IMO silver records** — proposed per-page per §2; defer to ~A schema decision
- **Q2: dedupe-per-page** — same term same page counts once? Default: yes, dedupe per (term, page) before summing
- **Q3: false-positive filter** — common terms like "wealth management" appear on most IMO sites; the `advisory_vocabulary` class is weighted lowest (2.0) to compensate; v0.2 candidate = IDF-like discrimination
- **Q4: term-list extensibility** — taxonomy version-pinned; new terms = v0.2; documented in `_meta.draft_status` lineage
- **Q5: timezone in run_date** — UTC per PRD v0.3 §3 `YYYY-MM-DD UTC` partition format pin
- **Q6: Lambda concurrency cap** — should we throttle? 100 IMOs * ~30s each = ~50min serial; concurrent = ~1-2min. Defer to AE 0.7 on orchestration sizing.
- **Q7: regex compilation** — pre-compile all taxonomy regexes at Lambda cold-start; cache in module-level dict; ~80 terms compile in <100ms

## 9. Implementation plan (post-TO GO)

1. ~~Confirm silver schema with ~A~~ — **DONE 17:10Z via `[SILVER-SCHEMA]` LOCK**; §2 + §3 + §4 reflect v0.2 contract
2. **Author `score_web.py`** — Lambda handler + scoring core + S3 IO (consumes `corp/{slug}/silver/web-scrape/{date}/*.json`; writes `corp/{slug}/gold/web-scrape/{date}/*.json`)
3. **Author `score_web_test.py`** — AC3 self-test with hand-curated silver fixtures (per-page + blocked-page + multi-class)
4. **Pre-commit gate** — `.tools/ds-commit-gate.sh data/find/imo/scripts/gold/score_web.py` (Rule 14)
5. **Commit** — `.tools/safe-commit.sh` per Rule 14a; commit-tag `work-cycle:N`
6. **Push to CLOUD** — pre-push hook fires `.tools/safe-deploy.sh` (Rule 13)
7. **S3 artifact upload** — DS owns full commit→QA-deploy cycle for `data/*/scripts/gold/*.py` (Rule 13)
8. **`comp-pipescript deployed score_web` MATCH** — pre-dispatch gate
9. **SSM dispatch** — QA-tier end-to-end (post-AE 0.7 .004 crawl-web + ~A parse-web ship)
10. **`comp-validate score_web --artifact <gold-path>`** — exit-0 all-pass before RAVC2 signal
11. **RAVC2-Request to ws COO + CC ~A** — Phase 1 RAVC2 (PRD §4 deliverable 4) is a separate downstream gate that runs after all three Lambdas (crawl + parse + score) chain end-to-end

## 10. Dependencies / standing posture

- **Upstream blocker:** ~A `parse-web` silver schema (sister-coord opened 17:00Z) — non-blocking for taxonomy + this brief; blocking for §5 scan loop final
- **Parallel:** AE 0.7 firing FIND_INSURE.001 (bucket + IAM + secrets) + .003 (comp-graph) per /allocation #3; AE 0.7 will ship `.004 crawl-web` Lambda after Phase 1 design from ~A/~B converges per /allocation #3 brief
- **TO arrival expected:** ws COO cron #171 ~17:05Z 2026-05-27 dispatches FIND_INSURE.006 score-web GO

## 11. Cross-references

- PRD: `docs/architecture/FIND_INSURE.md` v0.3 §4 Phase 1
- /allocation #3 brief: `org/tier1_exec/2.0.0_SA_COO/briefs/allocation_20260527T1647Z_find_insure_peak_priority.md`
- Slugify util: `data/find/imo/scripts/_util/slugify.py` (FIND_INSURE.002b shipped)
- Source-list extractor: `data/find/imo/scripts/_meta/extract_source_list.py` (FIND_INSURE.002 shipped `9aaa1459d`)
- Sister-coord MCP: `0.1.0_DS_MarketIntelligence~A` inbox 20260527T170013Z `[SISTER-COORD]`

— 0.1.0_DS_MarketIntelligence~B 2026-05-27T~17:05Z
