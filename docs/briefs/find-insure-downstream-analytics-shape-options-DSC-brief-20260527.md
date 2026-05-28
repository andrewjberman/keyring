# FIND_INSURE — Downstream Analytics Shape + Optionality Matrix

**Project:** [FIND_INSURE](../../org/projects/FIND_INSURE.json)
**PRD:** `docs/architecture/FIND_INSURE.md` v0.4+ §4 Phase 3 + Stage 3 enrichment-overlay
**Authoring TO:** [FIND_INSURE.027](../../org/tier2_senior/0.1.0_DS_MarketIntelligence~C/task_orders/FIND_INSURE.027.dsc-lusha-endpoint-architecture-exploration.md) (AC3)
**Author:** 0.1.0_DS_MarketIntelligence~C 2026-05-27T~23:50Z
**Authority anchor:** Andrew direct 2026-05-27T~23:25Z "downstream analytics shape/optionality matrix per Andrew direct exploration ask"
**Sister-artifact dependencies:** [lusha-endpoint-architecture-map.md](../reference/lusha-endpoint-architecture-map.md) (AC1) + [find-insure-bucket-structuring-implications.md](./find-insure-bucket-structuring-implications.md) (AC2)
**Anchored on:** CVO architectural brief + CVO ADDITIVE-1 IR-team-individual identification gate (pre-Phase-3)

## Purpose

Given the LushaAI endpoint coverage classes (per AC1 map) and the bucket-structured silver/gold/serving layer (per AC2), enumerate the **shape options for Phase 3 serving tables** + **cross-IMO analytics patterns** + **Lookalikes-driven universe expansion** + **Signals/Webhooks continuous-monitoring sub-class** — and end with **2-3 concrete downstream analytics patterns ranked by IR-team utility + implementation cost** to surface for IR-team feedback at sign-off per CVO ADDITIVE-1.

**Scope:** v0.1 Phase 3 serving deliverable + v0.2 enrichment-overlay candidates + v0.3 continuous-monitoring framing. Out-of-scope: portal UI (Phase 3b deferred per PRD §1).

---

## §1. Phase 3 serving table shape options

The Phase 3 deliverable per PRD §4 = consolidated IR-team-facing tables at `s3://opal-data-imo/serving/`. Three viable shape options, each with trade-offs:

### §1.1 Option A — Per-company aggregate (one row per IMO)

**Shape:**
```json
[
  {
    "lusha_company_id": "33222678",
    "slug": "wlth-rx",
    "name": "Wlth Rx",
    "domain": "wlthrx.com",
    "rollup_score": 75,                    // Phase 1 web-scrape score
    "phase_2a_complete": true,
    "employee_count_lusha": 12,
    "employee_count_decision_relevant": 5, // post-seniority+department filter
    "series_license_holders": 3,            // employees with any Series 7/24/63/65/66/79
    "series_density": 0.6,                  // series_license_holders / employee_count_decision_relevant
    "top_employee_score": 87,               // max(employee_score) across IMO's employees
    "median_employee_tenure_years": 8.5,
    "tech_stack_signals": ["Black Diamond", "Orion"],
    "naics_primary": "524210",
    "intent_topic_top": "Asset Management Platform",
    "aum_mentioned_max": 850000000,         // max AUM number extracted from any employee linkedin_summary
    "phase_2_completeness": {
      "linkedin_enriched": true,
      "job_posting_processed": false        // Phase 2B status
    },
    "last_refresh_utc": "2026-05-28T03:00:00Z"
  },
  ...
]
```

**Pros:**
- ✅ Single table = single IR-team scan + sort + filter
- ✅ Per-IMO row count is small (~30-100 IMOs ranked) — fits Excel-style consumer ergonomics
- ✅ Pre-aggregated metrics save downstream computation

**Cons:**
- ❌ Cannot drill from row to individual employees without separate lookup
- ❌ Per-employee detail (names, titles, contact paths) absent — IR team needs separate file for outreach
- ❌ Aggregations bake in v0.1 semantics; if IR team wants "show me CIOs only" → need re-aggregation

**Use-case fit:** Ranking + ICP triage. "Show me the top 20 IMOs by series_density" = single SQL/pandas filter.

### §1.2 Option B — Per-employee detail (one row per (IMO, employee))

**Shape:**
```json
[
  {
    "lusha_contact_id": "4158887495",
    "lusha_company_id": "33222678",
    "slug": "wlth-rx",
    "company_name": "Wlth Rx",
    "full_name": "Jane Doe",
    "job_title": "Chief Investment Officer",
    "title_seniority_class": "executive",   // derived per scoring-weights-v0.1.json
    "departments": ["Finance"],
    "series_licenses": ["Series 7", "Series 24", "Series 65"],
    "tenure_years_current_role": 7.7,
    "linkedin_summary_excerpt": "20-year veteran with Series 7, 24, 63, 65 licenses. Led $850M AUM growth at...",
    "keyword_matches": ["asset management", "AUM", "portfolio"],
    "aum_mentions": [{"amount": 850000000, "context": "Led $850M AUM growth at..."}],
    "employee_score": 87,                   // per scoring-weights-v0.1.json composite
    "email": "jane.doe@wlthrx.com",         // PII — SSE-KMS-protected
    "phone": "+14155550100",                // PII — SSE-KMS-protected
    "linkedin_url": "https://linkedin.com/in/jane-doe",
    "opted_out": false,
    "company_rollup_score": 75,             // denormalized from Phase 1 for join-free filter
    "last_enriched_utc": "2026-05-28T03:00:00Z"
  },
  ...
]
```

**Pros:**
- ✅ Direct outreach feed — IR team has names + contact paths inline
- ✅ Per-employee filter (e.g., "all CIOs across IMOs" = single column filter)
- ✅ Granular for ad-hoc analytics (e.g., "which IMOs have Series 24 holders specifically?")
- ✅ Captures the AC3 ADDITIVE-1 IR-team-individual identification gate substrate

**Cons:**
- ❌ Row count = ~30 IMOs × ~5-15 employees = ~150-450 rows. Manageable but not ranking-friendly.
- ❌ Company-level aggregates require GROUP BY downstream
- ❌ PII handling more sensitive — bigger blast radius if file mishandled

**Use-case fit:** Outreach execution + per-individual targeting. "Email me all CIOs with Series 24 and >5y tenure at IMOs scoring >70" = single multi-column filter.

### §1.3 Option C — Hybrid (companies + employees linked tables) ⭐ RECOMMENDED v0.1

**Shape:** TWO files, linked by `lusha_company_id`:
- `serving/companies.json` — Option A shape (per-company aggregate)
- `serving/employees.json` — Option B shape (per-employee detail)

**Pros:**
- ✅ Best of both: ranking view + outreach feed in their natural shapes
- ✅ IR team picks consumer file by use-case (companies.json for triage, employees.json for execution)
- ✅ Per-employee analytics composable from employees.json without re-aggregating
- ✅ Matches CVO §2.1 PRD §3.2 frame (`serving/companies.{json,parquet}` + `serving/employees.{json,parquet}` already PRD-specified)
- ✅ Mirrors industry-standard hybrid pattern (Salesforce Accounts + Contacts; HubSpot Companies + Contacts)

**Cons:**
- ⚖️ Slight write-side complexity — Phase 3 consolidation Lambda produces 2 files instead of 1
- ⚖️ IR-team consumer must understand the 2-file model (mitigated by clear README at `serving/`)

**Recommendation: Option C for v0.1.** PRD §3.2 already specifies this shape; this artifact CORROBORATES + amplifies the design intent. The Phase 3 consolidation Lambda implements both file builds in one pass (single iterate-corp-fanout).

### §1.4 Optional v0.2 extension — `serving/scoring.json` methodology archive

Per CVO §10 Q-B ratified: `serving/scoring.json` is the methodology + weights + index snapshot. Distinct from companies.json (which has scores applied). `scoring.json` carries:

```json
{
  "scoring_methodology_version": "v0.1",
  "scoring_methodology_date": "2026-05-28",
  "weights": {
    "phase_1_indicator_term_weights": {...},
    "phase_2a_title_seniority_class_weights": {...},
    "phase_2a_series_license_weights": {...},
    "rollup_score_formula": "..."
  },
  "history_archive_path": "serving/scoring_history/2026-05-28/scoring.json"
}
```

When weights change (e.g., IR-team feedback drives "weight Series 24 higher than Series 7"), `serving/scoring.json` updates + prior version archives to `serving/scoring_history/{date}/`. Per CVO Q-B + this artifact's AC2 §4.3 extensions.

---

## §2. Cross-IMO analytics (composable from Option C `employees.json`)

The per-employee detail table (Option B / Option C employees.json) is the **substrate for cross-IMO analytics**. Examples:

### §2.1 Series-license density across universe

**Question:** "What's the distribution of Series-license holders across the ranked IMO universe? Is the top quintile materially different from the bottom quintile in series_density?"

**SQL pattern:**
```sql
SELECT
  company_rollup_score_quintile,
  AVG(series_density) as avg_series_density,
  AVG(employee_count_decision_relevant) as avg_emp_count,
  COUNT(DISTINCT lusha_company_id) as imo_count
FROM (
  SELECT
    lusha_company_id,
    company_rollup_score,
    NTILE(5) OVER (ORDER BY company_rollup_score) as company_rollup_score_quintile,
    COUNT(*) as employee_count_decision_relevant,
    SUM(CASE WHEN cardinality(series_licenses) > 0 THEN 1 ELSE 0 END) / COUNT(*)::FLOAT as series_density
  FROM serving.employees
  WHERE NOT opted_out
  GROUP BY lusha_company_id, company_rollup_score
) sub
GROUP BY company_rollup_score_quintile;
```

**IR-team utility:** Validates the Phase 1 ranking — if top-quintile has materially higher series_density than bottom-quintile, Phase 1 web-scrape methodology is predictive. If indistinguishable, methodology refinement needed (W1/W2 taxonomy revisit).

### §2.2 M&A signal aggregation (v0.2+ with Signals)

**Question:** "Which IMOs have fired corporate-strategy or financial-event signals in the past 6 months AND have employees with Series 24/65 (asset-mgmt-supervisor licenses)?"

**Pattern (v0.2 with companies/signals + contacts overlay):**
```sql
SELECT
  c.slug,
  c.name,
  c.rollup_score,
  COUNT(DISTINCT s.signal_id) as ma_signal_count,
  STRING_AGG(DISTINCT s.signal_type, ',') as signal_types,
  COUNT(DISTINCT e.lusha_contact_id) FILTER (WHERE arr_contains(e.series_licenses, 'Series 24') OR arr_contains(e.series_licenses, 'Series 65')) as asset_mgmt_supervisors
FROM serving.companies c
JOIN serving.company_signals s ON c.lusha_company_id = s.entity_id
LEFT JOIN serving.employees e ON c.lusha_company_id = e.lusha_company_id
WHERE s.signal_type IN ('corporateStrategyNews', 'financialEventsNews', 'commercialActivityNews')
  AND s.signal_date >= current_date - INTERVAL '6 months'
  AND NOT e.opted_out
GROUP BY c.slug, c.name, c.rollup_score
HAVING COUNT(DISTINCT s.signal_id) > 0 AND COUNT(DISTINCT e.lusha_contact_id) FILTER (WHERE arr_contains(e.series_licenses, 'Series 24') OR arr_contains(e.series_licenses, 'Series 65')) > 0
ORDER BY ma_signal_count DESC, rollup_score DESC;
```

**IR-team utility:** Fresh leads. "Wlth Rx just announced a partnership AND has 3 Series 24 holders" = high-conviction outreach trigger.

**Dependency:** v0.2 companies/signals Lambda + `serving/company_signals.json` (new file at v0.2).

### §2.3 Corp-finance hire correlation with rollup_score

**Question:** "Do IMOs with surgeInHiringByDepartment(Finance) signals score higher on Phase 1 web-scrape than those without?"

**Pattern (v0.2):**
```sql
SELECT
  has_finance_hiring_surge,
  AVG(rollup_score) as avg_rollup_score,
  COUNT(*) as imo_count
FROM (
  SELECT
    c.lusha_company_id,
    c.rollup_score,
    BOOL_OR(s.signal_type = 'surgeInHiringByDepartment' AND s.data->>'department' = 'Finance') as has_finance_hiring_surge
  FROM serving.companies c
  LEFT JOIN serving.company_signals s ON c.lusha_company_id = s.entity_id
  GROUP BY c.lusha_company_id, c.rollup_score
) sub
GROUP BY has_finance_hiring_surge;
```

**IR-team utility:** Empirical validation of Phase 1 methodology. Drives next-version scoring weight tuning.

### §2.4 Technology-stack cohort analysis

**Question:** "Which IMO cohort (by tech stack) has the highest series_density and AUM mentions?"

**Pattern (requires Companies/Enrich v0.2):**
```sql
SELECT
  CASE
    WHEN arr_contains(c.tech_stack_signals, 'Black Diamond') THEN 'black-diamond'
    WHEN arr_contains(c.tech_stack_signals, 'Orion') THEN 'orion'
    WHEN arr_contains(c.tech_stack_signals, 'Tamarac') THEN 'tamarac'
    WHEN cardinality(c.tech_stack_signals) = 0 THEN 'unknown'
    ELSE 'other'
  END as platform_cohort,
  COUNT(DISTINCT c.lusha_company_id) as imo_count,
  AVG(c.series_density) as avg_series_density,
  AVG(c.aum_mentioned_max) as avg_aum_mention
FROM serving.companies c
WHERE c.phase_2a_complete
GROUP BY platform_cohort
ORDER BY avg_series_density DESC;
```

**IR-team utility:** Discovery of "platform-of-choice" IMO cohort signals — drives targeted outreach by tech-stack.

**Dependency:** v0.2 Companies/Enrich at Phase 2A (per AC1 §2.2 conditional default-SKIP at v0.1).

---

## §3. Lookalikes-driven universe expansion (v0.2)

### §3.1 Pattern A — Company Lookalikes seeded with Phase 3 IR-team-validated winners

**Trigger:** Post-Phase-3 IR-team feedback identifies top-N "high-value" IMOs from the 99-list. Use `POST /v3/companies/lookalike` seeded with those LinkedIn URLs / domains → returns lookalike IMOs outside the safemoneybroadcasting universe.

**Expected expansion:** 5-100 seed companies → up to 50-500 lookalike returns per page; multi-page pagination via `dedupeSessionId`.

**Cost estimate:** `lookalikeCompany` per result. Per AC1 §8.1 pricing example (2 credits/result), 100-lookalike expansion = ~200 credits. Lusha pricing typically $0.03-0.10/credit → ~$6-20 per expansion run.

**Output landing:** New silver path `corp/_lookalike_universe/silver/linkedin/companies_lookalike/{date}/` (under-`_lookalike_universe` pseudo-slug to distinguish from source-list IMOs; can be re-keyed to canonical-slug post-validation).

**Phase 3 v0.2 workflow:**
1. IR team flags top-N (e.g., top 5) IMOs after Phase 3 review
2. v0.2 Lambda fires Companies Lookalike seeded with those 5
3. Returns ~100 lookalike IMOs
4. Run them through Phase 1 web-scrape (re-using `crawl_web` Lambda) for indicator-term scoring
5. Promote scoring-pass lookalikes to formal universe; run Phase 2A LushaAI enrichment

### §3.2 Pattern B — Contact Lookalikes seeded with high-scoring Phase 2A employees

**Trigger:** Post-Phase-2A, identify employees with `employee_score >= 80` AND `series_licenses` contains Series 24 OR 65. Use `POST /v3/contacts/lookalike` seeded with those → returns lookalike contacts (CIOs / portfolio managers at OTHER companies).

**Output landing:** Discovered contacts may surface NEW IMOs (companies not in source universe). New IMOs flagged for universe-expansion via Pattern A re-fire OR direct add to corp/{new-slug}/ tree.

**Cost estimate:** `lookalikeContact` per result. ~50 seed contacts × ~50 lookalikes per seed = ~2500 credits per expansion run. Higher cost than company-lookalikes — recommend monthly cadence.

### §3.3 v0.2 universe-expansion governance

- **Cadence:** Quarterly (Pattern A) + Monthly (Pattern B). Cadence locked-in pre-v0.2-ship per IR-team-budget-watcher SLA.
- **Cost-state DDB:** Lookalike credits feed `find-insure-cost-state` table (per AC2 §5.3 — already enumerated under v0.2).
- **Universe-membership audit:** New IMOs added to universe via lookalike-expansion are tagged `source: lookalike_expansion_{date}` in `config/imo-universe-registry.json` (new config file at v0.2) for provenance.

---

## §4. Signals + Webhooks continuous-monitoring sub-class (v0.2-v0.3)

### §4.1 v0.2 — Batch Signals (`POST /v3/contacts/signals` + `POST /v3/companies/signals`)

**Cadence:** Monthly fire on top-quintile companies + employees.

**Per-IMO Lambda flow:**
```
1. Read serving/companies.json — filter to top-quintile (~20 IMOs)
2. POST /v3/companies/signals with signalTypes: [
     "surgeInHiringByDepartment",   // Finance/Investment hiring spikes
     "corporateStrategyNews",        // M&A, partnership, re-org
     "financialEventsNews",          // funding, IPO, acquisition
     "peopleNews"                    // leadership change
   ] for those 20 companyIds
3. POST /v3/contacts/signals with signalTypes: ["promotion", "companyChange"]
   for top employees at those IMOs (~100 contactIds)
4. Land silver at:
   corp/{slug}/silver/linkedin/companies_signals/{date}/
   corp/{slug}/silver/linkedin/contacts_signals/{date}/
5. Compose gold at:
   corp/{slug}/gold/linkedin/{date}/signals.json
6. Cross-IMO consolidate to serving/company_signals.json + serving/contact_signals.json (v0.2 new files)
```

**Cost estimate:** ~20 companies × ~3 signals/company avg × 1 credit = ~60 company-signal credits. ~100 contacts × ~1 signal/contact avg × 1 credit = ~100 contact-signal credits. ~$5-15/month total.

### §4.2 v0.3 — Webhook-based real-time signals

**Cadence:** Continuous (push-based).

**Subscriptions to create at v0.3 ship:**
- Company-level: top-quintile IMO companyIds subscribed to `corporateStrategyNews` + `financialEventsNews` + `peopleNews`
- Contact-level: top-employee contactIds subscribed to `promotion` + `companyChange`

**Lambda receiver:** `find-insure-signal-webhook-receiver` (sibling to `find-insure-opt-out-webhook-receiver` from v0.1):
1. Verify HMAC-SHA256 per [lusha-endpoint-architecture-map.md §9.3](../reference/lusha-endpoint-architecture-map.md#93-webhook-security-mandatory-hmac-sha256-verification)
2. Write silver at `corp/{slug}/silver/linkedin/{contacts_signals|companies_signals}/{date}/{webhook_id}.parquet`
3. Append to `serving/signal_feed.json` (new v0.3 file — append-only signal stream for IR-team feed)
4. Optionally emit SNS topic `find-insure-signals` for downstream subscribers (Slack alert / email digest)
5. Acknowledge per [lusha-endpoint-architecture-map.md §9.5](../reference/lusha-endpoint-architecture-map.md#95-acknowledgement-required-exact-shape)

**Cost-state binding:** Webhook deliveries write `signal_credits` to cost-state table per AC2 §5.3.

### §4.3 v0.2-v0.3 integration with IR-team workflow

**v0.2 monthly batch:** IR team receives "month-over-month change" digest — which IMOs / employees fired which signals. Drives next-month outreach prioritization.

**v0.3 real-time:** Critical signals (e.g., leadership change at a top-5 IMO) trigger same-day IR-team notification. Drives reactive outreach (warm intro before competitors notice).

---

## §5. Concrete downstream analytics patterns — ranked

Per `.027` AC3 — recommend 2-3 concrete "downstream analytics" patterns ranked by IR-team-utility + implementation-cost.

### §5.1 Pattern 1 — Hybrid serving (Option C) + per-quintile series-density retro ⭐⭐⭐ MUST-HAVE v0.1

**Pattern:** `serving/companies.json` + `serving/employees.json` (hybrid Option C) + analytics query §2.1 (per-quintile series-density retro).

**IR-team utility:** ★★★★★
- Outreach feed (employees.json) is the direct deliverable IR team uses daily
- Companies.json is the triage/ranking surface
- Per-quintile series-density retro validates methodology — drives Phase 1 W1/W2 tuning + builds Andrew + IR-team trust in scoring

**Implementation cost:** ★ LOW
- Already specified in PRD §3.2; aligned with this artifact's AC2 §3.4 structure
- §2.1 SQL is a one-off analytical query, not a productionized Lambda
- Cost = Phase 3 consolidation Lambda authoring (planned per `.023` TO already in DS~E queue)

**Decision recommendation:** **SHIP at v0.1 (Phase 3 close).** Non-optional; this IS the v0.1 deliverable.

### §5.2 Pattern 2 — Companies Lookalike-driven universe expansion + Phase 1+2A re-fire ⭐⭐ HIGH-VALUE v0.2

**Pattern:** Quarterly Companies Lookalike fired on IR-team-validated top-5 → ~100 new IMOs → re-fire Phase 1 web-scrape → promote scoring-pass to formal universe → re-fire Phase 2A LushaAI on promoted.

**IR-team utility:** ★★★★
- Solves the "what if our 99-IMO universe is missing the best opportunities?" question
- Empirically validated discovery (lookalikes are AI-scored against IR-team-validated winners, not Phase-1 web-scrape proxies)
- Each quarter potentially adds 5-20 high-value IMOs to outreach pipeline

**Implementation cost:** ★★ MEDIUM
- New Lambda: `find-insure-universe-expand` orchestrator (~3-5d wall)
- New config file: `config/imo-universe-registry.json` for provenance audit (~0.5d)
- Re-fire existing Phase 1 + Phase 2A on expanded universe (no new code; quota+budget impact)
- Quarterly cost: ~$6-20 per Lookalike run + ~$30-60 per re-fire (Phase 1 + Phase 2A on new IMOs)

**Decision recommendation:** **STAGE for v0.2 (post-Phase-3 IR-team-feedback ratify).** Top-1-recommendation for the v0.2 cycle.

### §5.3 Pattern 3 — Webhook-based real-time leadership-change alerts ⭐⭐ HIGH-VALUE v0.3

**Pattern:** Webhook subscriptions on top-quintile employees for `promotion` + `companyChange` → real-time SNS alert when a key decision-maker moves.

**IR-team utility:** ★★★★
- Time-critical: warm intro before competitors notice the change = high-conversion outreach moment
- Differentiated edge — most alt-data competitors do monthly batch; real-time is rare

**Implementation cost:** ★★★ MEDIUM-HIGH
- Webhook receiver Lambda + API Gateway + SQS queue (~5-7d wall)
- HMAC-SHA256 verification + idempotency handling
- SNS topic + downstream Slack-webhook + email integration (additional integration work)
- Webhook secret rotation operational discipline (per AC1 §9.1 `POST /api/account/secret/regenerate` invalidates ALL subscriptions — careful coordination)

**Decision recommendation:** **STAGE for v0.3 (post-v0.2-Universe-Expansion ratify).** Strong-recommendation but defers behind Pattern 2 due to implementation-cost + operational-complexity.

### §5.4 Patterns NOT recommended for v0.x roadmap

- **Pattern X — Per-IMO Salesforce-grade Account record sync.** IR team uses Salesforce; should serving feed Salesforce Accounts? Out-of-scope for v0.1-v0.3 (data movement to Salesforce is IR-team-IT-stack concern; Phase 3 deliverable is "tables", IR-team-side integration is THEIR responsibility).
- **Pattern Y — Predictive scoring via ML model (e.g., LightGBM trained on Phase 1+2A features to predict IR-team "Yes" labels).** Defers per [[feedback_light_fast_local_benchmarking_until_arsenal]] — heavy ML training infrastructure is out-of-v0.x arsenal phase.
- **Pattern Z — Cross-IMO graph analysis (e.g., which executives have worked at multiple IMOs in the universe).** Defers per PRD §1 out-of-v0.1-scope ("deeper NLP beyond keyword matching, cross-IMO graph analysis"). v0.4+ candidate.

---

## §6. CVO ADDITIVE-1 IR-team-individual identification gate (pre-Phase-3) — explicit addressing

Per [`.027` Notes](../../org/tier2_senior/0.1.0_DS_MarketIntelligence~C/task_orders/FIND_INSURE.027.dsc-lusha-endpoint-architecture-exploration.md) `[[CVO ADDITIVE-1]]`: "your AC3 downstream analytics shape options inform what the IR team will see → identify the most-decision-useful shape upfront so IR-team feedback at sign-off is informed."

### §6.1 Recommended IR-team sign-off package

When Phase 3 RAVC2-Request fires, the IR team should receive:

1. **`serving/companies.json` sample** — top 20 IMOs by rollup_score, formatted as Excel-friendly columns
2. **`serving/employees.json` sample** — top 50 employees across those 20 IMOs (sorted by employee_score)
3. **`README_FOR_IR_TEAM.md`** — one-page explainer:
   - What each column means (especially `series_density`, `aum_mentioned_max`, `keyword_matches`)
   - How rollup_score + employee_score were computed (link to `serving/scoring.json` methodology)
   - Known limitations (LushaAI coverage gaps; 3/99 Phase 1 universe completeness at time of writing)
   - Two specific feedback asks: (a) "Are these the right IMOs?" (b) "Are these the right individuals to reach out to?"
4. **Sample analytical query output** — §2.1 per-quintile series-density retro chart (proves the ranking has empirical signal)

### §6.2 Why this shape maximizes IR-team-feedback-quality

- **Direct surface:** Excel-readable tables = zero-learning-curve for IR team
- **Self-validating:** Sample query output demonstrates the methodology works pre-sign-off
- **Explicit feedback asks:** Frames the sign-off as "validate these two things" not "do you like this?"
- **Audit trail:** scoring.json methodology link + README ensures IR team can challenge specific decisions later (informed sign-off, not blind sign-off)

### §6.3 What feedback would trigger v0.2 work

| IR-team feedback signal | v0.2 work triggered |
|---|---|
| "These are the right IMOs but we're missing some we know about" | Pattern 2 (Lookalike universe-expansion) |
| "The ranking feels off — we'd prioritize differently" | Phase 1 + Phase 2A scoring-weights retuning (separate from this exploration) |
| "We can't tell who's worth reaching out to without LinkedIn-bio context" | Surface `linkedin_summary_excerpt` more prominently in employees.json (already in Option B schema) |
| "We need to know about leadership changes when they happen" | Pattern 3 (Webhook real-time signals) |
| "How fresh is this data?" | Add `last_enriched_utc` to employee rows (already in Option B schema); document Phase 2 cadence |

---

## §7. AC8 — CVO architectural brief cross-ref

Cross-referenced against `org/tier1_exec/3.0.0_SA_CVO/responses/20260527T1620Z_to_1.0.0_SA_CTO_opal_data_imo_bucket_architecture_brief.md`:

- **CVO §2.1 PRD §3.2 layout** specifies `serving/companies.{json,parquet}` + `serving/employees.{json,parquet}` — this artifact's Option C hybrid CORROBORATES + amplifies
- **CVO §10 Q-B serving/_history/scoring** ratified — this artifact's §1.4 EXTENDS with `serving/scoring_history/{date}/` operational mechanism + relates to AC2 §4.3 opt-out register history-extension
- **CVO Phase 3 framing** is informational at brief-writing-time; this artifact OPERATIONALIZES Phase 3 shape via the 3-option analysis + Pattern-1 recommendation
- **CVO Q-A latest/ symlinks NO** — this artifact does NOT propose any (overwrite-in-place at serving/ is per CVO §3.2 already)
- **Zero divergence** from CVO brief

---

## §8. Cross-domain coordination flags

Per `.027` AC7 (sister-coord with DS~B) — flags routed via ws COO `[SISTER-COORD]` MCP at RAVC2-Request fire moment:

- **DS~B (FIND_INSURE.006 score-web Gold):** Pattern 1 §2.1 per-quintile series-density retro CONSUMES DS~B's `rollup_score` distribution. If rollup_score is too saturated at top (100-cap saturation risk per CVO ADDITIVE-2 finding cb3cc6f6e), quintile-binning becomes degenerate. Flag for DS~B's Phase 2A v0.2 scoring revision.
- **DS~E (FIND_INSURE.023 serving consolidation):** This artifact's Option C two-file structure is the input contract for `.023` builder Lambda. DS~E should consume both files in single iterate-corp-fanout pass.
- **AE 0.7 (FIND_INSURE.001 bucket + IAM + secrets):** Pattern 3 v0.3 webhook receiver requires NEW Lambda + API Gateway + SQS — not in `.001` scope; flag for v0.3 design phase Terraform expansion.

Per `.027` AC9 (cross-domain block for ws CTO REPAIR-AMENDMENT (b)(i) W1 threshold semantics scribe):

- **W1 threshold semantics → quintile boundary fragility:** If W1 threshold defines "top quintile" via continuous score-cutoff rather than NTILE rank, Phase 2A subset size becomes distribution-shape-dependent. This artifact's §2.1 retro analytics ASSUME NTILE quintile binding. Flag for ws CTO REPAIR-AMENDMENT (b)(i) scribe — choice of threshold semantic propagates to retro-validation logic + IR-team-facing column meaning.

---

## §9. Open questions

- **Q-DA1 (architectural):** Should `serving/employees.json` include opted-out contacts (with `opted_out=true` flag) or exclude them entirely? Default-recommendation EXCLUDE per GDPR best practice. Material to v0.1 Phase 3 ship.
- **Q-DA2 (operational):** `serving/scoring.json` archive cadence — every refresh OR only on methodology change? Default-recommendation only-on-methodology-change (storage savings, history-clarity). Material to v0.2 design.
- **Q-DA3 (architectural):** Should serving include a `serving/_meta/pipeline_status.json` health-of-pipeline summary (last successful Phase 1/2/3 timestamps, IMO completeness pct, opt-out count, cost-burn YTD)? Default-recommendation YES at v0.1 — single file IR team can check for "is the data fresh?"
- **Q-DA4 (v0.2-roadmap):** Pattern 2 (Companies Lookalike universe-expansion) cadence — quarterly (as proposed) vs monthly. Trade-off: more frequent = more cost + more universe-churn; less frequent = staler discovery. Defer to IR-team-input at v0.2 design phase.

---

— 0.1.0_DS_MarketIntelligence~C 2026-05-27T~23:50Z (FIND_INSURE.027 AC3; downstream analytics shape + optionality matrix per Andrew 23:25Z parallelize + 23:26Z structured-format + CVO ADDITIVE-1)
