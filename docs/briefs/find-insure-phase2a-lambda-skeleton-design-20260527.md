# FIND_INSURE Phase 2A Lambda skeleton design brief

| | |
|---|---|
| **Author** | 1.0.0_SA_CTO |
| **Date** | 2026-05-27 |
| **Status** | DRAFT — for COO decomposition into Phase 2A pre-authoring TOs (DS~C lane) |
| **Lane** | DS~C 0.1.0_DS_MarketIntelligence~C — currently STANDBY-PURE since spawn ~16:50Z |
| **Parent PRD** | `docs/architecture/FIND_INSURE.md` v0.5 |
| **Authority** | Andrew direct sovereign 2026-05-27T~19:50Z verbatim: "we have a ton of DS that have just been sitting there looping /work for hours, and there is certainly a ton of work we need to do in FIND_INSURE, so let's figure out how to pick up throughput here" |

---

## 1. Why this brief exists

DS~C is STANDBY-PURE awaiting Phase 1 RAVC2-Accept + Andrew subset-cut decision (per PRD §4 Phase 2 subset gating). This brief unblocks **parallel-active Phase 2A Lambda authoring** against fixture JSON — code-skeleton + unit-tests can ship without live Lusha calls, leaving only the "wire-up + first-fire" step gated.

Sister-pattern to DS~A's parse-web silver scaffold (`92dfb70e3`) and DS~B's score-web gold scaffold (`877ca495d`) — both shipped against fixture JSON pre-`.004` empirical run + chain-fire when bronze landed.

## 2. Scope

3 Lambda skeletons + 1 shared Lusha client utility + 1 webhook-receiver scaffold + cost-gate integration. All STANDBY-PREP class: code + unit-tests against fixture JSON; live Lusha calls + SNS subscriptions + DDB writes GATED on (a) Phase 1 RAVC2-Accept (b) AE 0.7 `imo-pipeline-v0.X.0` KMS+DDB+SNS apply (c) Andrew subset-cut decision.

### 2.1 `data/find/imo/scripts/bronze/crawl_linkedin_bronze.py`

Per PRD v0.5 §4 Phase 2 Part A endpoint mapping:

1. **Lusha company search** (`POST /v3/companies/search`) — resolve each IMO's `domain` → Lusha `companyId`
2. **Lusha contact prospecting** (`POST /v3/contacts/prospecting`) — enumerate leadership-class contacts at `companyId` (filter `seniority` + `departments` + `existingDataPoints`)
3. **Lusha contact enrich** (`POST /v3/contacts/enrich`) — reveal emails+phones for high-score-title subset (cost-discipline gate per Q4)
4. **Lusha company enrich** (`POST /v3/companies/enrich`) — firmographics (size/revenue/year-founded/SIC/NAICS/tech/funding)

Bronze write target: `s3://opal-data-imo/corp/{slug}/bronze/linkedin-scrape/{YYYY-MM-DD}/{lusha_contact_id}.json` (per-contact granularity) + `s3://opal-data-imo/corp/{slug}/bronze/linkedin-scrape/{YYYY-MM-DD}/_company.json` (per-IMO company enrich result).

Cost-gate integration: check `find-insure-cost-state` DDB at function-init for per-IMO + global Lusha credit-burn vs `config/cost-budgets-v0.1.json` ceilings; soft-stop per Q-C3+Q-C4 disposition; SNS `find-insure-budget-alerts` publish on ceiling-hit.

KMS encryption: bronze/linkedin-scrape/ is KMS-scope per v0.4 §3.1; Lambda automatically gets KMS Decrypt grant via `find-insure-lambda-role` IAM (per v0.4 §3.5).

**Stub mode** (pre-Phase-1-RAVC2 + pre-KMS-apply): Lusha client utility (see §2.4) reads from fixture JSON instead of live API; Lambda unit-tests against fixtures; no DDB writes; no SNS publishes.

### 2.2 `data/find/imo/scripts/silver/parse_linkedin_silver.py`

Per PRD v0.5 §4 Phase 2 Part A deliverable 2:

- Read bronze contact JSONs + company JSON per IMO per run-date
- Structure each employee record (one row per employee): `{full_name, title, tenure_at_company, prior_titles[], location, linkedin_url, series_licenses_detected[], current_company_id, signal_dates[]}`
- Structure company record: `{company_id, company_name, domain, size, revenue_range, year_founded, primary_industry, sub_industry, sic_codes[], naics_codes[], technologies[], hq_location, funding_rounds[]}`
- Series-license detection — regex/NLP on Lusha bio/about/experience text per `feedback-series-license-detection-regex-pattern` (TBD by DS~C in this work; can mirror `score_web_gold.py` taxonomy approach from DS~B)
- Rule-17 silver-tier discipline: preserve all fields from bronze; NO field slimming; NO null-handling beyond schema type coercion; NO business-row filtering

Silver write target: `s3://opal-data-imo/corp/{slug}/silver/linkedin-scrape/{YYYY-MM-DD}/employees.parquet` + `_company.parquet`.

Schema version field: `schema_version: "v1.0"` per Q-S1 disposition.

### 2.3 `data/find/imo/scripts/gold/score_linkedin_gold.py`

Per PRD v0.5 §4 Phase 2 Part A deliverable 3:

Per-employee scoring axes:
- `tenure_at_company_years` (longer = more decision-power; weight 0.25 per DS~E `scoring-weights-v0.1.json`)
- `title_seniority_class` enum {C-suite / Director / Head-of / VP / Managing-Director / Founder / Owner / President / Other} (weight 0.25)
- `series_license_count_weighted` — sum of present licenses × per-license weights from `scoring-weights-v0.1.json` (e.g., Series 65=0.40, Series 66=0.40, Series 7=0.30, Series 24=0.30, Series 6=0.25, etc.; weight 0.30)
- `title_keyword_match` — title contains "Wealth" / "Advisory" / "Investment" / "Asset Management" / "Portfolio" / "Capital" (weight 0.20)

Per-company aggregate fields (rollup):
- `leadership_employee_count`
- `series_licensed_employee_count`
- `max_employee_score`
- `mean_employee_score_top5`
- `company_score_linkedin = f(max_employee_score, series_licensed_count, leadership_count)` — formula TBD by DS~C; document derivation

Gold write target: `s3://opal-data-imo/corp/{slug}/gold/linkedin-scrape/{YYYY-MM-DD}/employees_scored.parquet` + `_company_scored.parquet`.

### 2.4 `data/find/imo/scripts/_util/lusha_client.py` (NEW shared utility)

Single-source Lusha API client. All 3 Lambdas import from it. Implements:

- **Authentication**: read `find-insure/lusha-ai/api-key` from AWS Secrets Manager (per Lusha v3 §4 auth model); cache for Lambda lifetime
- **Endpoint methods** mirroring PRD v0.5 §4 Part A mapping table — one Python method per Lusha endpoint
- **Rate-limit awareness**: parse `x-rate-limit-*` + `x-minute-requests-left` response headers (per Lusha v3 §5); back off when low; raise `LushaRateLimitError` for caller-handling
- **Error handling**: HTTP 429 → exponential backoff (initial 1s, doubling, max 60s, max 5 retries); HTTP 5XX → same; HTTP 451 → raise `LushaGDPRBlockedError` + log entity-id (per Lusha v3 §6)
- **Cost-tracking hooks**: every call returns `(response_data, credits_charged_this_call)` tuple; caller responsible for DDB cost-state update
- **Stub mode**: env var `LUSHA_CLIENT_STUB=1` reads fixture JSON from `data/find/imo/scripts/_util/fixtures/lusha_responses/{endpoint}_{scenario}.json` instead of live API call; enables unit-tests + dev-loop without credit-burn

Pattern reference: mirror `data/orion/manual_api/jwt_freshness.py` Orion JWT pattern for the auth-state + fixture-mode discipline.

### 2.5 GDPR opt-out webhook receiver scaffolding

Per UNK-1 + Q-L3 PULL-FORWARD disposition (PRD v0.5 §3.5 KMS scope + Lusha v3 §9.6 GDPR opt-out):

- `data/find/imo/scripts/_meta/opt_out_webhook_receiver.py` — API Gateway → Lambda → SQS → silver writer
- HMAC-SHA256 signature verification per Lusha v3 §9.3
- Required ACK response shape per Lusha v3 §9.5 (`{received: true, timestamp, webhookId}` HTTP 201 within 10s)
- Silver writer: mark opted-out contact in `silver/linkedin-scrape/{slug}/{date}/employees.parquet` with `opt_out_at` timestamp + datapoint-specific suppression flags
- Propagate to `serving/employees.{json,parquet}` to mark row suppressed (Phase 3 serving-build picks up)
- Webhook secret read from `find-insure/lusha-ai/webhook-secret` (new sub-namespace per UNK-1 disposition)

**Scaffold-only at Phase 2A pre-execution** — do NOT subscribe to Lusha webhook topic until Phase 2A live-Lusha-call moment (avoids credit-overhead for delivered-but-unused webhook events per CTO Q-L3 disposition).

### 2.6 Unit-test discipline per Lambda

Each Lambda + utility module gets a matching `*_test.py` in same directory (or `_util/tests/`):

- Fixture JSON files at `data/find/imo/scripts/_util/fixtures/lusha_responses/{endpoint}_{scenario}.json` covering: happy-path / 429-rate-limited / 451-GDPR-blocked / 402-payment-required / 500-server-error / partial-result-with-canReveal-credits-zero
- Stub-mode Lambda invocation tests against each fixture
- Series-license regex/NLP coverage tests (manually-curated positive + negative LinkedIn bio examples; include false-positive class like "Series 7 (retired)" — should NOT trigger license-present)
- Cost-tracking hook tests (mock DDB; assert UpdateExpression ADD called with right credit-count per call class)

Target: 35-50 self-test cases per module (mirroring DS~A `parse_web_silver.py` 35/35 self-test discipline + DS~B `score_web_gold.py` taxonomy testing pattern).

## 3. Pre-authoring acceptance criteria (DS~C lane)

- **AC1**: `lusha_client.py` shipped with all 6 endpoint methods (companies/search + contacts/prospecting + contacts/enrich + companies/enrich + companies/lookalike + signals) + auth + rate-limit awareness + error handling + cost-tracking hooks + stub-mode env var
- **AC2**: `crawl_linkedin_bronze.py` Lambda skeleton shipped — stub-mode end-to-end pass against fixture JSON
- **AC3**: `parse_linkedin_silver.py` Lambda skeleton shipped — silver schema parses fixture bronze; Rule-17 preservation invariant verified
- **AC4**: `score_linkedin_gold.py` Lambda skeleton shipped — gold scoring against fixture silver; aggregate fields populated; sample IMO score calculated end-to-end
- **AC5**: `opt_out_webhook_receiver.py` scaffolded — HMAC-SHA256 signature verification path tested with mock signature; webhook ACK shape verified; SQS write stubbed
- **AC6**: Unit-test suite ≥35 cases per module; self-test exit 0 across all
- **AC7**: `ds-commit-gate.sh` exit 0 on all new `.py` files (py_compile + ds-precommit-check.py + ruff per Rule 14 + Rule 15 future-annotations check)

NO live API calls in scope. NO DDB writes in scope. NO SNS subscriptions in scope. NO Lambda deploys in scope (AE 0.7 lane). All AC pass against fixture JSON + stub-mode.

## 4. Sequencing — fully parallel to Phase 1 critical path

- **NOW (this brief landed)**: DS~C can start authoring immediately upon TO dispatch from ws COO
- **Phase 1 RAVC2-Accept lands**: DS~C scaffold + my v0.4 PRD KMS+DDB+SNS substrate + AE 0.7 v0.X.0 TF amendment all converge; live Lusha first-fire gated only on (a) Andrew subset-cut decision + (b) KMS+DDB+SNS apply + (c) Lusha + Bright Data secrets verified live
- **Phase 2A live-execution**: wire-up + first-fire ~5-15min wall instead of full-Lambda-authoring 1-3h wall

Net throughput gain: ~1-3h of pre-authoring done in parallel-active vs serial post-Phase-1-RAVC2.

## 5. Routing

- **Primary**: COO TO decomposition for DS~C lane (suggested TO IDs: `FIND_INSURE.011` lusha-client + `FIND_INSURE.012` crawl_linkedin_bronze + `FIND_INSURE.013` parse_linkedin_silver + `FIND_INSURE.014` score_linkedin_gold + `FIND_INSURE.015` opt_out_webhook_receiver; or single bundled TO `FIND_INSURE.011` per COO discretion)
- **CC**: DS~C awareness via COO routing
- **CC**: AE 0.7 awareness — your `imo-pipeline-v0.X.0` KMS+DDB+SNS apply remains the gate to live execution; nothing in this brief blocks your apply timing

## 6. Why now

Andrew direct 19:50Z: pick up PRD-writing pace + coordinate with COO on decomposition because "ton of DS that have just been sitting there looping /work for hours." DS~C has been STANDBY-PURE since ~16:50Z (~3h+ wall). This brief unblocks DS~C for parallel-active authoring that compresses Phase 2A wire-up to minutes-not-hours when upstream gates clear.

— ws CTO 2026-05-27T~19:55Z
