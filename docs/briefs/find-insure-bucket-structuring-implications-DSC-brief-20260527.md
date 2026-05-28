# FIND_INSURE — Bucket Structuring Implications from LushaAI Endpoint Shape

**Project:** [FIND_INSURE](../../org/projects/FIND_INSURE.json)
**PRD:** `docs/architecture/FIND_INSURE.md` v0.4+ §3.1-§3.8 + §4 Phase 2A
**Authoring TO:** [FIND_INSURE.027](../../org/tier2_senior/0.1.0_DS_MarketIntelligence~C/task_orders/FIND_INSURE.027.dsc-lusha-endpoint-architecture-exploration.md) (AC2)
**Author:** 0.1.0_DS_MarketIntelligence~C 2026-05-27T~23:45Z
**Authority anchor:** Andrew direct 2026-05-27T~23:25Z "exploring lusha endpoint data structure and how this informs bucket structuring" + Andrew 23:26Z structured-format directive
**Sister-artifact dependency:** [lusha-endpoint-architecture-map.md](../reference/lusha-endpoint-architecture-map.md) (AC1) — coverage classes + response shapes
**Anchored on:** CVO architectural brief `org/tier1_exec/3.0.0_SA_CVO/responses/20260527T1620Z_to_1.0.0_SA_CTO_opal_data_imo_bucket_architecture_brief.md` (PRD v0.3-absorbed)

## Purpose

Derive bucket prefix conventions for the LushaAI channel from the per-endpoint response shapes documented in [lusha-endpoint-architecture-map.md](../reference/lusha-endpoint-architecture-map.md). Cover per-endpoint silver schema mapping (Rule 17 passthrough binding), cross-endpoint join + dedup strategy, bucket prefix structure (per-endpoint vs per-data-class), history-archive class assignment, and cost-state DynamoDB integration.

**Scope binding:** Operates within CVO brief §2 final layout (per-IMO grouping `corp/{slug}/{medallion}/{channel}/{date}/`) and PRD v0.4 §3.1 KMS scope (silver/linkedin + bronze/linkedin + serving/ are PII-scope SSE-KMS). This artifact does NOT propose root-level prefix changes; it specifies the **`linkedin/` channel sub-structure** within the CVO-ratified frame.

---

## §1. Per-endpoint silver schema mapping (Rule 17 passthrough binding)

**CLAUDE.md Rule 17 binding:** Silver tier conversions perform ONLY deduplication + type standardization. NO field-slimming, NO fillna, NO dropna, NO row-filtering by business semantic. Lusha response fields land in silver **strictly passthrough**; business-logic filtering happens at gold.

### §1.1 `POST /v3/companies/search` → silver schema

**Raw Lusha response shape** (see [lusha-endpoint-architecture-map.md §1.2](../reference/lusha-endpoint-architecture-map.md#12-post-v3companiessearch)):

```json
{
  "data": [{"id": "33222678", "has": [...], "name": "Wlth Rx", "domain": "wlthrx.com"}],
  "billing": {"creditsCharged": 1}
}
```

**Silver passthrough schema** (per-result row; one bronze JSON dump → N silver rows):

```python
{
    "lusha_company_id": str,        # response.data[i].id passthrough
    "has": list[str],               # response.data[i].has passthrough (preview-coverage flags)
    "name": str,                    # response.data[i].name passthrough
    "domain": str,                  # response.data[i].domain passthrough
    "_lookup_key": str,             # the request-side lookup key (domain | name | id) — provenance
    "_lookup_value": str,           # the request-side lookup value — provenance
    "_credits_charged": int,        # per-result share of response.billing.creditsCharged — Phase 2A cost retro
    "_request_ts_utc": str,         # ISO-8601 — when Lambda fired the request
    "_response_ts_utc": str,        # ISO-8601 — when response received
    "_run_id": str,                 # per-Lambda-invocation UUID — telemetry join key
}
```

**Provenance fields prefix `_`** — DS convention for "added at silver for traceability, not in source." Matches Phase 1 silver web-scrape precedent (`parse_web_silver.py` post-Rule-17-fix `3ee6ee869`).

**Dtype standardization (silver-permitted per Rule 17):**
- `lusha_company_id`: cast str (Lusha returns numeric string; pin str for consistent FK join)
- `_credits_charged`: cast Int64 (integer; allow NA for malformed responses)
- `_request_ts_utc` / `_response_ts_utc`: ISO-8601 string; downstream coerce to timestamp at gold

**NOT silver-permitted (gold business-logic):**
- Filtering out rows where `has` is empty (decision: is empty-coverage discardable?)
- Composing `_credits_charged` as fraction or aggregate
- Renaming `has` to `coverage_flags` (would bury upstream provenance)

### §1.2 `POST /v3/contacts/prospecting` → silver schema

**Raw response shape** (see [lusha-endpoint-architecture-map.md §4.1](../reference/lusha-endpoint-architecture-map.md#41-post-v3contactsprospecting)):

```json
{
  "data": [{"id": "4158887495", "has": [...], "canReveal": {...}, "fullName": "Jane Doe", "jobTitle": "CIO", "seniority": "C-Level", "departments": [...], "companyId": "33222678", "companyName": "Wlth Rx"}],
  "totalResults": 12,
  "currentPage": 1,
  "totalPages": 1,
  "billing": {"creditsCharged": 12}
}
```

**Silver passthrough schema** (per-result row; one bronze JSON → N silver rows):

```python
{
    "lusha_contact_id": str,            # response.data[i].id passthrough
    "has": list[str],                   # passthrough
    "can_reveal_credits": int,          # response.data[i].canReveal.credits — pre-Enrich cost gate
    "can_reveal_datapoints": list[str], # response.data[i].canReveal.datapoints — what unlocking would reveal
    "full_name": str,
    "first_name": str | None,           # passthrough (None when Lusha omits — Rule 17 NOT fillna)
    "last_name": str | None,            # passthrough
    "job_title": str,
    "seniority": str,                   # enum: C-Level/VP/Director/Manager/IC/Owner-Founder
    "departments": list[dict],          # passthrough — [{id: int, value: str}, ...]
    "lusha_company_id": str,            # response.data[i].companyId — FK to companies/search silver
    "company_name": str,                # passthrough — denormalized for read convenience
    "_filter_request": dict,            # full request filter object — provenance for re-runs
    "_total_results": int,              # response.totalResults — pagination signal
    "_current_page": int,
    "_total_pages": int,
    "_credits_charged": int,            # per-result share
    "_request_ts_utc": str,
    "_response_ts_utc": str,
    "_run_id": str,
}
```

**Note camelCase→snake_case translation:** silver uses snake_case per DS convention (matches `parse_web_silver.py` precedent). Rule 17 considers this "type standardization" (naming-convention standardization, no semantic change). The original camelCase is preserved in bronze JSON — silver's snake_case is a canonical dtype-class for downstream join consistency. **Token-level preservation** is the rule: `canReveal.credits` → `can_reveal_credits` (no abbreviation, no rename — `canReveal` stays as `can_reveal`).

### §1.3 `POST /v3/contacts/enrich` → silver schema

**Raw response shape** (see [lusha-endpoint-architecture-map.md §2.1](../reference/lusha-endpoint-architecture-map.md#21-post-v3contactsenrich)):

Largest response among Phase 2A endpoints — includes `linkedinSummary`, `skills[]`, `employmentHistory[]`, `education[]`, `emails[]`, `phones[]`.

**Silver passthrough schema** (per-result row; nested structures preserved as JSON-typed columns or struct fields):

```python
{
    "lusha_contact_id": str,
    "full_name": str,
    "first_name": str | None,
    "last_name": str | None,
    "job_title": str,
    "seniority": str,
    "departments": list[dict],
    "lusha_company_id": str,
    "company_name": str,
    "company_domain": str,
    "emails": list[dict],              # passthrough — [{address: str, type: str}, ...]
    "phones": list[dict],              # passthrough — [{number: str, type: str}, ...]
    "linkedin_url": str | None,
    "linkedin_summary": str | None,    # PII-adjacent free text — gold extracts Series-license + AUM tokens
    "skills": list[str],               # passthrough — Series-license token check at gold
    "employment_history": list[dict],  # passthrough — per-employer tenure
    "education": list[dict],           # passthrough — degree/institution
    "_revealed_datapoints": list[str], # the `reveal` field on request — provenance of what was charged
    "_credits_charged": int,           # sum of revealEmail + revealPhone for this contact
    "_revealed_for_free": bool,        # canReveal.credits was 0 at Search — flagged for cost retro
    "_request_ts_utc": str,
    "_response_ts_utc": str,
    "_run_id": str,
}
```

**Per Rule 17 strict-passthrough:**
- `emails` and `phones` are list-of-dict (NOT flattened to email-1, email-2, phone-1, phone-2). Each list MAY be empty.
- `employment_history` and `education` are list-of-dict preserved fully. Gold extracts current-employer-tenure separately.
- `linkedin_summary` raw text preserved; gold derives `series_licenses[]` + `aum_mentions[]` + `keyword_matches[]`.
- NO fillna on None fields (per AC.011 v0.1 silver fix `3ee6ee869` precedent).

### §1.4 `POST /v3/companies/enrich` → silver schema

**Silver passthrough schema** (per-result row):

```python
{
    "lusha_company_id": str,
    "name": str,
    "domain": str | None,
    "logo": str | None,
    "linkedin_url": str | None,
    "linkedin_followers": int | None,
    "description": str | None,         # free text — gold keyword-scans for asset-mgmt signals
    "founded": int | None,             # year
    "size": str | None,                # band string e.g. "51-200"
    "size_range": dict | None,         # {min: int, max: int}
    "revenue": str | None,             # band string e.g. "$10M-$50M"
    "revenue_range": dict | None,      # {min: int, max: int}
    "industries": dict | None,         # nested {primary, sub[], sic[], naics[]}
    "type": str | None,                # enum: Private/Public/Subsidiary/etc.
    "locations": dict | None,          # nested {headquarters, offices[]}
    "technologies": list[dict],        # passthrough — [{name, category}, ...]
    "funding_rounds": list[dict],      # passthrough
    "intent_topics": list[dict],       # passthrough — [{topic, score, trend}, ...]
    "social_links": dict | None,       # passthrough
    "_credits_charged": int,
    "_request_ts_utc": str,
    "_response_ts_utc": str,
    "_run_id": str,
}
```

**Note nested-dict preservation** (`industries`, `locations`, `social_links`): silver keeps these as JSON-struct fields rather than flattening. Gold may project specific paths (e.g., `industries.naics[0].code`) but does NOT modify the silver-level structure.

### §1.5 Signals endpoints → silver schema (v0.2+)

**Both `POST /v3/contacts/signals` and `POST /v3/companies/signals`** return per-entity arrays of signal events. Silver schema (per-signal row; one entity-with-N-signals → N silver rows):

```python
{
    "entity_type": str,                 # "contact" | "company"
    "entity_id": str,                   # lusha_contact_id OR lusha_company_id
    "signal_type": str,                 # enum from §5.1 or §5.2
    "signal_date": str | None,          # ISO-8601 date — when the signal fired upstream
    "data": dict,                       # full passthrough of signal-specific payload (varies by type)
    "_signal_query_start_date": str,    # request-side startDate filter — provenance
    "_credits_charged": int,
    "_request_ts_utc": str,
    "_response_ts_utc": str,
    "_run_id": str,
}
```

**`data` field passthrough is critical:** signal payloads vary by type (`promotion` has `previousTitle`/`currentTitle`; `surgeInHiring` has different fields; `corporateStrategyNews` has article URLs + summaries). Rule 17 forbids per-type flattening at silver. Gold derives normalized columns per consumer need.

### §1.6 Webhook payload (opt-out + signal subscriptions) → silver schema

**Opt-out webhook payload** (see [lusha-endpoint-architecture-map.md §9.6](../reference/lusha-endpoint-architecture-map.md#96-opt-out-subscription-gdpr--phase-2a-mandatory)):

```python
{
    "lusha_contact_id": str,            # from contactId field
    "full_name": str,
    "company_name": str,
    "job_title": str,
    "linkedin_url": str | None,
    "opt_out_at": str,                  # ISO-8601 from contactOptOutDate
    "exposure_at": str,                 # ISO-8601 from contactExposureDate
    "suppressed_datapoints": list[dict],# from datapoints[] — [{id, type}, ...]
    "partner_client_id": str | None,
    "_webhook_id": str,                 # inbound payload `id` — echoed in ack per §9.5
    "_signature_verified": bool,        # HMAC-SHA256 result — security audit field
    "_received_ts_utc": str,
    "_subscription_id": str,            # which subscription delivered this
}
```

**Signal webhook payload (v0.3)** — same shape as Signals silver (§1.5) plus `_webhook_id` + `_signature_verified` + `_received_ts_utc` provenance.

---

## §2. Cross-endpoint reconciliation (joins + deduplication)

### §2.1 Join graph

```
companies/search response → lusha_company_id ────────┐
                                                     │
                                                     ▼
contacts/prospecting request filter ── companyId ── companies/search row
contacts/prospecting response → lusha_contact_id + lusha_company_id (denormalized FK)
                                       │
                                       │
                                       ▼
contacts/enrich request → contactIds[]
contacts/enrich response → lusha_contact_id (PK) + lusha_company_id (FK)
                                       │
                                       │
                                       ▼
contacts/signals request → contactIds[]  (v0.2+)
contacts/signals response → entity_id (= lusha_contact_id)
                                       │
                                       │
                                       ▼
opt-out webhook → lusha_contact_id (suppression key)
```

**Primary keys:**
- `lusha_company_id` — PK for company-side tables (search, enrich, companies/signals)
- `lusha_contact_id` — PK for contact-side tables (prospecting, enrich, contacts/signals, opt-out)
- `(lusha_contact_id, lusha_company_id)` — composite for current-employment fact (handles job-change history)

**Foreign keys:**
- `contacts.*.lusha_company_id` → `companies.*.lusha_company_id`
- `companies/signals.*.entity_id` → `companies.*.lusha_company_id`
- `contacts/signals.*.entity_id` → `contacts.*.lusha_contact_id`
- `opt_out.*.lusha_contact_id` → `contacts.*.lusha_contact_id`

**Stable across endpoints:** Lusha guarantees `lusha_contact_id` + `lusha_company_id` stable identity across all endpoints (per [lusha-endpoint-architecture-map.md §13 Q-EM2](../reference/lusha-endpoint-architecture-map.md#13-open-questions-route-to-ws-cto--andrew-if-needed)). No re-keying needed.

### §2.2 Deduplication strategy (per-endpoint silver)

| Endpoint silver | Dedup key | Dedup semantic |
|---|---|---|
| `companies/search` | `lusha_company_id` + `_lookup_key` + `_lookup_value` | One row per (id, lookup-path). Allows multiple lookups of same company (by domain THEN by id) without losing provenance. |
| `contacts/prospecting` | `lusha_contact_id` + `_filter_request_hash` | One row per (contact, filter-context). Same contact returned by 2 different filter queries = 2 rows (provenance preserved). |
| `contacts/enrich` | `lusha_contact_id` + `_revealed_datapoints` + `_request_ts_utc` | One row per (contact, reveal-scope, request-time). Allows re-enrich for staleness without overwriting prior. |
| `companies/enrich` | `lusha_company_id` + `_request_ts_utc` | One row per (company, request-time). |
| `contacts/signals` | `entity_id` + `signal_type` + `signal_date` | Per Lusha guarantee §9.7 "each signal delivered + charged once" — naturally deduplicated at source; safe to use natural-key. |
| `companies/signals` | Same as contacts/signals | Same |
| Opt-out webhook | `lusha_contact_id` + `opt_out_at` | One row per (contact, opt-out-event). Re-deliveries (auto-retry on non-2xx) detect via `_webhook_id` for idempotent ack. |

**Silver dedup is the ONLY mutation Rule 17 permits beyond dtype-standardization.** Per CLAUDE.md Rule 17 explicit-permit-list: "deduplicate exact-row duplicates; standardize dtypes; coerce string→numeric on columns whose source is unambiguously numeric; flatten obvious encoding artifacts."

### §2.3 Gold-tier join discipline

**Gold is the structural-permitted layer for cross-endpoint composition.** Per CLAUDE.md Rule 17 ("Anything that requires judgment about *what fields matter*, *what null means*, or *which rows to drop* is business-logic and belongs in the **gold** tier."), gold composes:

- **`gold/linkedin/{date}/employees.json`** per `.024` AC6: LEFT JOIN `silver/linkedin/enrich/contacts/` on `lusha_contact_id` + filter to current-employment-row (via `_revealed_datapoints` recency); join LEFT to `silver/linkedin/prospecting/` for `seniority` + `departments`; join LEFT to `silver/linkedin/opt_out/` for opt-out suppression (rows where opt-out present are EXCLUDED from gold per AC9 GDPR + per `serving/` propagation).
- **`gold/linkedin/{date}/companies.json`** (v0.2 if companies/enrich enabled): JOIN silver companies/search ↔ companies/enrich on `lusha_company_id`; project decision-relevant subset (NAICS + tech-stack + industries.sub).
- **`gold/linkedin/{date}/signals.json`** (v0.2+): cross-join signals to current employment fact for "this CIO at this IMO had this promotion signal" enriched view.

**Gold-tier silver→gold transformations explicitly permitted by Rule 17:**
- Field selection / projection (gold IS the slim layer)
- Null filtering on required fields (e.g., drop employees with NULL `lusha_contact_id`)
- Filling defaults appropriate to business semantic (e.g., `series_licenses: []` for no-license-found, NOT `None`)
- Row filtering by business rule (e.g., drop opted-out contacts, drop pre-2018 employment history if "current employees only" is the gold semantic)
- Derived columns (e.g., `tenure_years` = today - employment_history.startDate where isCurrent=true)
- Aggregations (e.g., `series_density` = count(employees with series_licenses) / count(employees))

---

## §3. Bucket prefix recommendations (per-endpoint vs per-data-class)

### §3.1 Recommendation: **per-endpoint silver prefixes**, **per-data-class gold prefixes**

**Silver layer — recommend per-endpoint sub-prefix:**
```
corp/{slug}/silver/linkedin/{endpoint}/{date}/
```
where `{endpoint}` ∈ `{companies_search, companies_enrich, contacts_prospecting, contacts_enrich, contacts_signals, companies_signals, opt_out}`

**Gold layer — recommend per-data-class sub-prefix:**
```
corp/{slug}/gold/linkedin/{date}/{file}.json
```
where `{file}` ∈ `{employees, companies, signals}`

### §3.2 Rationale — why per-endpoint at silver

| Driver | Per-endpoint silver | Per-data-class silver |
|---|---|---|
| **Provenance audit clarity** | ✅ "Show me everything we got from Lusha contacts/enrich on 2026-05-28" = single subtree scan | ❌ Requires file-by-file inspection of `_endpoint_source` field |
| **Rule 17 passthrough discipline** | ✅ Each endpoint has its own schema; per-endpoint files match source faithfully | ⚠️ Mixed schemas in one prefix require schema-tagging at row level |
| **Cost retro per endpoint** | ✅ Sum `_credits_charged` across all rows in `silver/linkedin/contacts_enrich/` = total Enrich credit burn for date | ❌ Requires per-row filtering by endpoint |
| **Re-process granularity** | ✅ "Re-parse all contacts/enrich silver" = single subtree iterate | ❌ Re-parse must scan all silver for endpoint-tagged rows |
| **Storage cost** | ⚖️ Marginal — same total bytes; just split into more keys | ⚖️ Same total bytes; fewer keys, larger files |
| **Read patterns** | ⚖️ Cross-endpoint joins require multiple-subtree read | ⚖️ Cross-endpoint joins are single-subtree but need row-level filter |
| **Gold-build complexity** | ⚖️ Gold builder reads N subtrees by endpoint | ⚖️ Gold builder reads 1 subtree, filters by endpoint |

**Verdict:** **per-endpoint at silver** wins on 4-of-6 axes; tied on 2. Provenance-audit-clarity is load-bearing for Andrew-direct-ask "what data are we even pulling from Lusha?" use case + for CVO /verify-channel cycles.

**Aligned with CVO brief §2.2:** CVO brief specifies `corp/{slug}/silver/linkedin/{date}/` (channel-level). This artifact REFINES that one level deeper: `corp/{slug}/silver/linkedin/{endpoint}/{date}/`. No divergence — refinement within CVO frame.

### §3.3 Rationale — why per-data-class at gold

| Driver | Per-data-class gold | Per-endpoint gold |
|---|---|---|
| **Consumer simplicity** | ✅ "I want all employees" = `corp/{slug}/gold/linkedin/{date}/employees.json` (one file) | ❌ "I want all employees" = JOIN across 3 endpoint-files manually |
| **`.024` AC6 contract** | ✅ Spec is exactly `gold/linkedin/{date}/employees.json` with composed fields | ❌ Doesn't match AC6 |
| **Phase 3 serving build** | ✅ Serving consolidates from clean per-data-class gold | ❌ Serving has to re-join from endpoint-grouped gold |
| **Re-process per-data-class** | ✅ "Re-build gold employees" = single Lambda iterates corp/*/gold/linkedin/{latest}/employees.json producers | ⚖️ Same |

**Verdict:** **per-data-class at gold** is the natural fit. Gold IS the composition layer; gold files match consumer semantic (employees, companies, signals).

### §3.4 Concrete final structure

```
opal-data-imo/
  corp/{slug}/
    bronze/linkedin/
      {endpoint}/                              # raw Lusha JSON dumps per endpoint
        {date}/
          {run_id}.json                        # one file per Lambda invocation per endpoint
    silver/linkedin/
      companies_search/                        # per-endpoint silver (Rule 17 passthrough)
        {date}/
          {run_id}.parquet
      companies_enrich/
        {date}/
          {run_id}.parquet
      contacts_prospecting/
        {date}/
          {run_id}.parquet
      contacts_enrich/
        {date}/
          {run_id}.parquet
      contacts_signals/                        # v0.2+
        {date}/
          {run_id}.parquet
      companies_signals/                       # v0.2+
        {date}/
          {run_id}.parquet
      opt_out/                                 # webhook deliveries
        {date}/
          {webhook_id}.parquet
    gold/linkedin/
      {date}/
        employees.json                         # per-data-class gold (composed from silver)
        companies.json                         # v0.2 if companies/enrich enabled
        signals.json                           # v0.2+
  serving/
    employees.{json,parquet}                   # cross-IMO consolidated (per CVO §3.2 overwrite-in-place)
    employees_history/{date}/                  # v0.2 if history-class adopted (see §4 below)
    companies.{json,parquet}
    scoring.{json,parquet}                     # methodology-versioned, history-archived per CVO §10 Q-B YES
    scoring_history/{date}/
```

**Endpoint naming convention:** snake_case with underscore between resource and action (`companies_search`, `contacts_enrich`). Avoids hyphen-in-path (Lusha endpoint is `companies/search` → translated to `companies_search` subdir). Matches Python module-name convention (load-bearing for the Lambda Python code that writes these paths).

---

## §4. History-archive class assignment

### §4.1 CVO brief baseline (per §10 Q-B ruling)

CVO §10 Q-B ratified: **history-archive for `serving/scoring.json` only.** Rationale: "Scoring methodology changes are intentional and cite-able; companies+employees overwrites are routine."

### §4.2 LushaAI endpoints — which need silver-level history retention?

**Silver layer (per-endpoint sub-prefix) is ALREADY date-partitioned** per CVO §3.2 append-by-date semantic for `corp/{slug}/{medallion}/{channel}/{date}/`. So **silver retains all dated runs by default** — no separate history-archive needed. Date partitions provide lineage.

**Gold layer (per-data-class `corp/{slug}/gold/linkedin/{date}/`)** also date-partitioned per CVO. **No separate history-archive at gold either.**

### §4.3 Serving layer — extend Q-B to additional classes?

CVO Q-B baseline = `serving/scoring.json` history-only. **This artifact's recommendation for LushaAI integration:**

| Serving file | History-archive recommendation | Rationale |
|---|---|---|
| `serving/scoring.json` | **YES** (CVO Q-B ratified) | Methodology changes (scoring weight tuning) are intentional + cite-able |
| `serving/employees.json` | **NO at v0.1; YES at v0.2** for opt-out audit trail | Routine overwrite at v0.1; opt-out compliance audit at v0.2 requires being able to prove "we suppressed this contact within the legal window" → snapshot pre+post opt-out events |
| `serving/companies.json` | **NO at v0.1** | Routine overwrite per CVO baseline |
| `serving/opt_out_register.json` (NEW) | **YES** (immutable append-log semantic) | GDPR audit trail — every opt-out event captured, never modified or deleted |

**`serving/opt_out_register.json` is a NEW serving file** this artifact proposes for the v0.1 GDPR compliance surface. Distinct from the per-corp `silver/linkedin/opt_out/` (which is per-IMO-grouped per the medallion structure) — the serving register is **cross-IMO unified** for IR-team-wide opt-out lookup (a single contact may appear across multiple IMOs' employee lists; central register prevents per-IMO-silo drift).

Implementation: opt-out webhook Lambda writes to BOTH (a) per-corp `silver/linkedin/opt_out/{date}/{webhook_id}.parquet` (per-IMO lineage) AND (b) appends to `serving/opt_out_register.json` (cross-IMO authoritative register). Phase 2A `.024` AC9 pre-flight check reads (b).

### §4.4 Bronze retention (CVO §4 lifecycle)

CVO §4 lifecycle policy: `corp/*/bronze/*/*` → Standard-IA at 90d; Glacier Flexible Retrieval at 365d; Deep Archive at 730d; **NEVER expire**. This artifact CORROBORATES — Lusha bronze JSON dumps are forensic-class (LushaAI API responses are cost-bearing to re-fetch; preserve indefinitely on cold tier).

---

## §5. Cost-state DynamoDB integration

### §5.1 `find-insure-cost-state` table — purpose

Per PRD v0.4 §3.7 (KMS + cost-gate substrate per CVO §9): `find-insure-cost-state` DynamoDB table tracks per-IMO + per-day cumulative cost across Phase 1 (Bright Data) + Phase 2A (Lusha) + Phase 2B (job-postings) for cost-gate enforcement.

### §5.2 LushaAI endpoint contribution to cost-state

**Lambda-side responsibility:** Each per-IMO Lambda invocation that fires Lusha endpoints MUST update cost-state with the cumulative `_credits_charged` total **at end of run** (single atomic update, NOT per-call to avoid DDB write amplification).

**DDB schema (proposed):**

```
PK = "imo#{slug}"
SK = "lusha#{YYYY-MM-DD}"
attributes:
  credits_burned: int (atomic-add via UpdateItem ADD operation)
  api_search_credits: int
  reveal_email_credits: int
  reveal_phone_credits: int
  reveal_company_credits: int
  lookalike_credits: int
  signal_credits: int
  call_count: int
  last_run_ts_utc: str
  last_run_id: str
  cost_ceiling_hit: bool
```

**Daily-global cost-state row:**
```
PK = "GLOBAL"
SK = "lusha#{YYYY-MM-DD}"
attributes:
  total_credits_burned: int
  total_calls: int
  global_ceiling_hit: bool
  imos_completed: list[str]
  imos_aborted_at_ceiling: list[str]
```

### §5.3 Which endpoints feed cost-state

**ALL endpoints with `billing.creditsCharged > 0`** — i.e., all paid endpoints from [lusha-endpoint-architecture-map.md §10 matrix](../reference/lusha-endpoint-architecture-map.md#10-endpointphase-summary-matrix):

- `companies/search` → `api_search_credits`
- `contacts/search` → `api_search_credits`
- `contacts/prospecting` → `api_search_credits` (per-result; can be large per call)
- `companies/prospecting` (v0.2) → `api_search_credits`
- `contacts/enrich` → `reveal_email_credits` + `reveal_phone_credits`
- `companies/enrich` → `reveal_company_credits`
- `contacts/search-and-enrich` → `api_search_credits` + `reveal_email_credits` + `reveal_phone_credits`
- `companies/search-and-enrich` → `reveal_company_credits`
- `contacts/lookalike` (v0.2) → `lookalike_credits`
- `companies/lookalike` (v0.2) → `lookalike_credits`
- `contacts/signals` (v0.2) → `signal_credits`
- `companies/signals` (v0.2) → `signal_credits`
- Webhook signal deliveries (v0.3) → `signal_credits` (recorded at webhook receiver, not at outbound caller)

**Free endpoints (no cost-state contribution):**
- `GET /v3/account/usage`
- `GET /v3/contacts/prospecting/filters[/...]`
- `GET /v3/companies/prospecting/filters[/...]`
- `GET /v3/contacts/signals/types`
- `GET /v3/companies/signals/types`
- `GET /v3/companies/signals/filters[/...]`
- All webhook management endpoints (`POST/GET/PATCH/POST/POST` on `/api/subscriptions/*`)
- Webhook audit logs (`GET /api/audit-logs[/stats]`)
- Webhook secret management (`GET /api/account/secret` + `POST /api/account/secret/regenerate`)

### §5.4 Cost-gate enforcement flow

```
[Lambda invocation start]
  ↓
  GetItem(PK=imo#{slug}, SK=lusha#{today}) → check current per-IMO burn
  ↓
  GetItem(PK=GLOBAL, SK=lusha#{today}) → check daily-global burn
  ↓
  IF per_imo_burn >= per_imo_ceiling (default 50 per CVO §9) → ABORT this IMO + write telemetry
  IF global_burn >= global_ceiling (default 500 per CVO §9) → ABORT all remaining IMOs + sns:Publish alert
  ↓
[Per-call work — accumulate _credits_charged in local var]
  ↓
[Lambda invocation end]
  ↓
  UpdateItem(PK=imo#{slug}, SK=lusha#{today}, ADD credits_burned :local_total, ADD api_search_credits :local_search, ...)
  UpdateItem(PK=GLOBAL, SK=lusha#{today}, ADD total_credits_burned :local_total, ADD total_calls :local_calls)
  ↓
[Telemetry: write ndjson run record with full local cost breakdown]
```

**Why end-of-run atomic update vs per-call:**
- Per-call would create ~30-50 DDB writes per IMO × 30 IMOs = ~1500 DDB writes per Phase 2A run — adds latency + DDB cost
- End-of-run single UpdateItem with ADD operation is atomic on DDB side — concurrent IMO Lambdas don't conflict
- Trade-off: cost-gate check at START reads stale state (today's prior runs only, not concurrent runs) → soft-tolerance per PRD §3.8 (5% overshoot acceptable on EMPIRICAL-FIRST-RUN)

**Acceptable per PRD §3.8 overshoot-tolerance.** If tightening needed (post-empirical), upgrade to per-call atomic UpdateItem with conditional check; cost is ~$0.01 per 1K writes (negligible vs Lusha credit cost).

---

## §6. KMS scope reaffirmation

Per PRD v0.4 §3.1 — SSE-KMS scope = `silver/linkedin/`, `silver/job-posting/`, `bronze/linkedin/`, `bronze/job-posting/`, `serving/`. This artifact's `linkedin/` sub-structure inherits SSE-KMS at every level:

- `corp/{slug}/bronze/linkedin/{endpoint}/{date}/` ← SSE-KMS
- `corp/{slug}/silver/linkedin/{endpoint}/{date}/` ← SSE-KMS
- `corp/{slug}/gold/linkedin/{date}/` ← SSE-KMS (per PRD §3.1 gold/linkedin is PII-scope; consumer-readable summaries are derived but underlying data is PII-bearing)
- `serving/{employees,opt_out_register}.{json,parquet}` ← SSE-KMS

**Non-LushaAI artifacts continue under SSE-S3:**
- `corp/{slug}/{bronze,silver,gold}/web-scrape/` ← SSE-S3 (Phase 1; no PII)
- `corp/{slug}/{bronze,silver,gold}/job-posting/` ← unclear pre-Phase-2B (depends on whether job-postings surface PII like recruiter contact info; flag for Phase 2B design)
- `code/`, `config/`, `telemetry/`, `qa/`, `archives/` ← SSE-S3

`find-insure-lambda-role` already has `kms:GenerateDataKey` + `kms:Decrypt` per PRD §3.5. No IAM amendment needed for this artifact's prefix structure.

---

## §7. AC8 — CVO architectural brief divergence notes

Cross-referenced against `org/tier1_exec/3.0.0_SA_CVO/responses/20260527T1620Z_to_1.0.0_SA_CTO_opal_data_imo_bucket_architecture_brief.md`:

| CVO finding | This artifact response | Status |
|---|---|---|
| §2.1 PRD §3.2 per-IMO corp/{slug}/{medallion}/{channel}/{date}/ layout CORROBORATE | This artifact REFINES `linkedin/` channel sub-structure as per-endpoint at silver, per-data-class at gold | **Aligned — refinement within CVO frame** |
| §2.2 5 root prefixes (code/+config/+telemetry/+qa/+archives/) | This artifact does NOT touch root prefixes; operates within `corp/{slug}/linkedin/` channel scope | **Aligned — orthogonal scope** |
| §3.1 YYYY-MM-DD UTC date format | This artifact's `{date}` placeholder MUST be YYYY-MM-DD UTC | **Aligned** |
| §3.2 append-by-date for corp/medallion + overwrite-in-place for serving | This artifact CORROBORATES + extends with §4.3 history-archive recommendations for `serving/opt_out_register.json` (NEW) | **Aligned + extends** |
| §3.3 slug normalization via shared util | This artifact's `corp/{slug}/` paths inherit; no new convention | **Aligned** |
| §4 6-prefix lifecycle policy | This artifact CORROBORATES bronze NEVER-expire (Lusha re-fetch cost-bearing); proposes NO new lifecycle rules | **Aligned** |
| §5 IAM least-privilege with delete-restrict on gold/silver/serving/config/code | This artifact CORROBORATES — opt-out webhook receiver writes to silver but does NOT delete | **Aligned** |
| §9 cost-discipline gates (Lambda-side) with `config/cost-budgets-{version}.json` + per-IMO `lusha_credits_phase_2a: 50` | This artifact OPERATIONALIZES — §5 DDB cost-state schema is the read-side mechanism for the §9 budgets | **Aligned + operationalizes** |
| §10 Q-A NO latest/ symlinks | Not applicable (this artifact doesn't propose any) | **Aligned** |
| §10 Q-B YES serving/_history/scoring only | This artifact EXTENDS Q-B with `serving/opt_out_register.json` immutable-log + `serving/employees_history/` v0.2 candidate | **Extension recommendation** |
| §10 Q-C centralize config under root | This artifact's `cost-budgets-{version}.json` lives at `config/` root per CVO | **Aligned** |
| §10 Q-D SINGLE bucket | This artifact operates within single `opal-data-imo` bucket | **Aligned** |
| §11 banking observation #2 (`docs/templates/aws-bucket-greenfield.md` skeleton) | Not in scope of this artifact; FYI for future FIND_xxxxx | **Aligned — informational** |

**Net divergence: zero.** Two EXTENSION recommendations (Q-B → opt-out register + v0.2 employees_history) are additive to CVO baseline, not in conflict.

---

## §8. Open questions (route to ws CTO via COO if material)

- **Q-BS1 (extension):** Adopt `serving/opt_out_register.json` immutable append-log as NEW serving file? Default-recommendation YES per GDPR audit trail need. Material to v0.1 Phase 2A `.024` ACs — needs CTO ratify before opt-out-webhook Lambda hardcodes the write path.
- **Q-BS2 (extension):** Adopt `serving/employees_history/{date}/` at v0.2 for opt-out audit trail beyond just register? Default-recommendation YES at v0.2; flag at v0.1 ship.
- **Q-BS3 (operational):** Cost-state DDB write cadence — end-of-run atomic (this artifact's recommendation) vs per-call. Default-recommendation end-of-run for v0.1; tighten to per-call if empirical overshoot exceeds PRD §3.8 5% tolerance.
- **Q-BS4 (architectural):** Bronze JSON dump granularity — one-file-per-Lambda-invocation per endpoint (this artifact's recommendation) vs one-file-per-IMO-per-endpoint. Default-recommendation one-file-per-invocation for re-run isolation; consider per-IMO-rollup if S3 small-files cost becomes issue (~30 IMOs × 7 endpoints × daily = ~210 files/day — acceptable).

---

— 0.1.0_DS_MarketIntelligence~C 2026-05-27T~23:45Z (FIND_INSURE.027 AC2; bucket structuring implications per Andrew 23:25Z parallelize + 23:26Z structured-format)
