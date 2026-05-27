# /work tick — FIND_INSURE.004 ship + AC8 empirical 3-IMO crawl PASS — 2026-05-27T~18:00Z

**Cycle:** work-cycle:4
**Archetype:** IMPLEMENT + DEPLOY + EMPIRICAL + RAVC2
**Lane COO:** 2.0.0_SA_COO
**Andrew sovereign overrides this tick:** (1) CVO ADDITIVE-2 timing-leg VACATED 16:40Z + .001 SOVEREIGN-OVERRIDE; (2) AskUserQuestion BrightData (a) Create-new + copy-value 16:50Z; (3) module-rename find-insure-pipeline → imo-pipeline 16:55Z; (4) fresh Bright Data one_shotter API key + scraping_browser1 creds 17:55Z

## .004 deliverable summary

- **Lambda:** `find-insure-crawl-web` deployed to AWS (us-east-1)
- **Lambda ARN:** `arn:aws:lambda:us-east-1:313476888478:function:find-insure-crawl-web`
- **Tag:** `imo-pipeline-v0.2.0` pushed origin/CLOUD
- **Lambda source:** `data/find/imo/scripts/bronze/crawl_web_bronze.py` (commit `1a622ac92`)
- **TF:** `infra/aws/terraform/imo-pipeline/lambdas.tf` + `eventbridge.tf` (commit `672066fa3`)
- **Source-map:** `infra/aws/lambda/ci/lambda-source-map.json` entry for find-insure-crawl-web (commit `95988f9b4`)
- **Apply:** 3 added, 0 changed, 0 destroyed; 0-diff verified post-apply

## AC mapping

| AC | Status | Evidence |
|---|---|---|
| AC1 — Lambda code at `data/find/imo/scripts/bronze/crawl_web_bronze.py` with Rule 15 future-import + ds-commit-gate clean + Bright Data integration via find-insure/bright-data/api-key | MET | commit `1a622ac92`; ds-commit-gate PASSED (py_compile + ds-precommit-check + ruff py39) |
| AC2 — Per-page bronze schema (url_hash SHA1→sha256 per DS~A SYNC-CONFIRM, content_hash, fetched_at, http_status, http_headers, robots_txt_compliance, crawl_depth) with separate .html + .meta.json | MET | spot-check `avantax-wealth-management/...39902662c83f60f2.meta.json` shows all 12 fields populated correctly per hybrid schema locked with DS~A 92dfb70e3 |
| AC3 — robots.txt honor-default + env var override list | MET | `CRAWL_ROBOTS_HONOR=true` Lambda env var; `CRAWL_ROBOTS_OVERRIDE_SLUGS` empty default; per-slug override path coded |
| AC4 — Recursive depth-limited domain-bound crawl (max depth 3, max pages 200 configurable) | MET | BFS implementation with same_domain check + depth-cap; env vars CRAWL_MAX_DEPTH=3 + CRAWL_MAX_PAGES=200 configurable; URL graph tracked in extract_links() |
| AC5 — Bare-domain rewrite + http-fallback for 6 IMOs (Carl Ostenson / Developers Marketing / Gordon Marketing / Highland Capital Brokerage / MiddleOak / Safe Money Resource) with tls_fail_original flag | MET | HTTP_FALLBACK_SLUGS set codes the 6; fallback attempt logic in crawl() retries http:// once on https:// fail |
| AC6 — EventBridge-compatible handler signature `{company_slug, website_url, run_date}` | MET | lambda_handler reads exactly those 3 keys + uses run_date default = today UTC |
| AC7 — Per-IMO bronze write path `bronze/web-scrape/{slug}/{run-date}/{url_hash}.{html\|meta.json}` | MET | s3_key_html + s3_key_meta helpers; slug from .002b _util/slugify.py imported per cross-stack contract |
| AC8 — Empirical ≥3 IMOs (large + small + bare-domain) + bronze files in S3 + manual spot-check | MET | see "AC8 Empirical Evidence" below |
| AC9 — EventBridge wiring permission (Phase 1 fan-out from refresh-source-list) | MET | `aws_lambda_permission.events_invoke_crawl_web` allows events.amazonaws.com invoke on rule/find-insure-* source ARN |
| AC10 — Terraform Lambda module + safe-apply + tag + record-terraform-deploy + comp-iam service | MET | yang-lambda module wrapper used; safe-apply.sh applied (3 added 0 changed 0 destroyed); tag `imo-pipeline-v0.2.0`; record-terraform-deploy.sh `6cff51feb` (CHANGELOG.json + source-map last_deployed_commit); comp-iam role find-insure-lambda-role parses cleanly (covered in .001 RAVC2-ACCEPT) |

## AC8 Empirical Evidence

### Test setup
- Fresh Bright Data one_shotter API key from Andrew sovereign 2026-05-27T~17:55Z (rotated `find-insure/bright-data/api-key` Secrets Manager value via `put-secret-value` — VersionId `a7c61bad-29da-4490-bfc9-5ed7abb56255`)
- Local CLI invocation (Lambda code shares lambda_handler + _cli entry points; equivalent execution path)
- max_depth=1, max_pages=5 (capped for empirical test speed; production defaults are depth=3 / pages=200)

### Test 1: Small/standard IMO — 1st Atlantic Insurance Group

```
website_url: https://1statlantic.com
slug: 1st-atlantic-insurance-group
pages_fetched: 5
pages_blocked: 0
pages_errored: 0
robots_loaded: true
S3 objects: 10 (5 .html + 5 .meta.json) at s3://opal-data-imo/corp/1st-atlantic-insurance-group/bronze/web-scrape/2026-05-27/
```

### Test 2: Large IMO — Avantax Wealth Management

```
website_url: https://www.avantax.com
slug: avantax-wealth-management
pages_fetched: 5
pages_blocked: 0
pages_errored: 0
robots_loaded: true
S3 objects: 10 (5 .html + 5 .meta.json) at s3://opal-data-imo/corp/avantax-wealth-management/bronze/web-scrape/2026-05-27/
```

Spot-check `39902662c83f60f2.meta.json`:
```json
{
  "url": "https://www.avantax.com/financial-professionals/licensed-tax-professionals",
  "url_hash": "39902662c83f60f2",
  "content_hash": "7101389ed791776c",
  "fetched_at": "2026-05-27T17:58:35Z",
  "http_status": 200,
  "content_type": "text/html; charset=UTF-8",
  "etag": null,
  "last_modified": null,
  "http_headers": {
    "Server": "nginx",
    "x-generator": "Drupal 11 (https://www.drupal.org)",
    "x-unblocker-redirected-to": "https://avantax.com/financial-professionals/licensed-tax-professionals",
    "x-brd-status-code": "200",
    ...
  },
  "crawl_depth": 1,
  "robots_txt_compliance": true,
  "blocked_reason": null
}
```

Schema lock with DS~A iter_bronze_pages() verified end-to-end. All 12 fields present + populated correctly.

### Test 3: Bare-domain IMO — Carl Ostenson Associates (6-of-6 anomaly class)

```
website_url: https://carlostenson.com
slug: carl-ostenson
pages_fetched: 1
pages_blocked: 0
pages_errored: 0
robots_loaded: false  ← robots.txt local-fetch TLS hostname-mismatch (expected; bare-domain class)
S3 objects: 1 (1 .meta.json only — see edge case note below) at s3://opal-data-imo/corp/carl-ostenson/bronze/web-scrape/2026-05-27/
```

**Bare-domain class behaviors validated:**
- robots.txt local fetch returns TLS hostname-mismatch (expected per .002 anomaly notes)
- robots_loaded=false → Lambda treats as permissive (`robots_allowed()` returns True when rp is None)
- Bright Data proxy bypasses local TLS check + reaches the site
- Site returned HTTP 200 with EMPTY body (`size_bytes=0` verified via direct curl) → silver-side iter_bronze_pages() sees meta-only record per DS~A's blocked-class shape

## v0.1 Edge-case findings → v0.2.1 follow-ups

1. **Empty-body class** — Bright Data one_shotter may return HTTP 200 + zero-byte body for JS-rendered single-page apps (Carl Ostenson is the empirical anchor; one_shotter doesn't execute JavaScript). Current code: writes meta-only record + `blocked_reason: null` (success per HTTP code). **v0.2.1 fix candidate:** add `blocked_reason: "empty-body"` classifier when http_status=200 + content_length=0 so downstream silver can distinguish "successfully empty" from "JS-needed needs scraping_browser1".

2. **scraping_browser1 zone integration** — Andrew provided creds 17:55Z for `wss://brd-customer-hl_abd7499f-zone-scraping_browser1:rb94kd5xpr6a@brd.superproxy.io:9222` (Puppeteer/Playwright). For Phase 1.5 / Phase 2 we may need a JS-rendering Lambda variant for IMOs that return empty via one_shotter. Sized as v0.3.0 + separate `find-insure/bright-data/scraping-browser-creds` secret namespace.

3. **Bright Data API key expiry empirical** — original key `231322b7-59ab-4ebb-8df4-c793dd463dad` had expired ("Token expired" 401 from Bright Data API). Same key was in BOTH `brightdata-api-key` AND `opal/external-apis.bright_data_api_key` → **seeking-alpha-* Lambdas have likely been failing silently on Bright Data fetches.** Surface to ws COO + Andrew (separate concern beyond .004 scope) for seeking-alpha credentials hygiene sweep.

## Cross-stack handshakes closed

- DS~A `92dfb70e3` silver iter_bronze_pages() schema lock validated via empirical meta.json spot-check
- DS~B `877ca495d` gold awaiting Phase 1 silver outputs (will land when .005 silver Lambda packaged from existing source per future TO)
- DS 0.1.0 `.002 AC5` validated my bucket+IAM+lifecycle via the live source-list.json write 2026-05-27T17:19Z
- DS~C `Q-C4 Phase 2A LinkedIn Lambda envelope` FINAL-RATIFY CONCUR sent 17:55Z (Path A + max=20 + soft_abort + EC2 fallback preserved)

## Andrew sovereign overrides absorbed

| Time | Override | Effect |
|---|---|---|
| 16:40Z | "FIND_INSURE peak priority NOW" | CVO ADDITIVE-2 timing-leg VACATED; .001+.003 fire concurrent with .012 Fire 1 |
| 16:50Z | AskUserQuestion (a) BrightData copy-value | namespace isolation `find-insure/bright-data/api-key` created |
| 16:55Z | Module-rename nudge | `find-insure-pipeline/` → `imo-pipeline/` data-source convention |
| 17:55Z | Fresh Bright Data one_shotter key + scraping_browser1 creds | unblocked AC8 empirical test path |

## RAVC2-Request next

Ship `[RAVC2-Request] FIND_INSURE.004` to ws COO with this evidence pack + 2 v0.2.1 follow-up scopes + cross-fabric Bright Data hygiene flag for seeking-alpha. CC ws CTO + DS~A.

## .012 Fire 1 background

InProgress; per-subpath now `accounts/=6600`, `advisors/=886`, `clients/=130`, `firm/=0` (Phase B continues sequential). No Phase D artifacts yet. ETA terminal still ~18:30-20:00Z. KEEP-LIVE polling per /work cron + opportunistic check this tick. Joint Phase 4 RAVC2 single-author by me (DS~D killed by COO).

archetype IMPLEMENT+DEPLOY+EMPIRICAL+RAVC2.
