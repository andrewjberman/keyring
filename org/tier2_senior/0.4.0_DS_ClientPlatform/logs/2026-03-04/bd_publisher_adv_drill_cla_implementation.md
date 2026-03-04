# A-Roll Task Orders — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-04
**Start Time:** session start
**End Time:** in progress

## Objective

Work through all A-roll task orders in sequence: ADVI-004 (adv_drill + cla in bd-portal-publisher
Lambda), ADVI-005 (stacked_bar + rolling_1y in gold script 10), A4 (script 09 bell curve
verification), A5 (opal-users-v2 advisor identity investigation). Also assessed DC task order
on startup.

---

## Work Completed

### 1. DC Task Order — Startup Assessment

Read `data_contract.md` task order. Status was already `complete` (issued 2026-03-02; baseline
contract creation). data_contract.xml at `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/`
was adequate to begin A1+A2: timeseries_chart.json Source 2 block existed but had no adv_drill
or cla entries. Those are added by A1+A2's own DC.1 requirement, not the DC task order.

### 2. ADVI-004 A2.0 Pre-Check: primary_city Confirmed in Script 04

Read `data/black_diamond/scripts/gold/04_build_client_dimension.py`.
- `primary_city` is defined in the schema comment at line 17.
- Written to output at lines 267-268 via `modal_value(grp['_city'])`.
- The Lambda's `load_all()` did NOT include `primary_city` in its cdim column prune.
- Conclusion: `cla.geo_city_drill` is a Lambda-only change — no gold-layer enhancement needed.
  This validates the CTO scope correction in the ADVI-004 task order.

### 3. ADVI-004 A1: adv_drill in bd-portal-publisher

Modified `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`.

Changes:
- Added constants `TOP_N_CLIENTS_PER_ARCH = 8` and `MAX_CLA_CITIES = 9`.
- Added `primary_city` to cdim column prune in `load_all()`.
- Expanded `perf_cohort` merge in `build_timeseries_chart()` to pull
  `relationship_name, primary_architect, primary_state, primary_city` from cdim
  (one merge serves all new views — no second parquet load).
- Added `adv_drill` computation block: iterates `adv_categories` (excl "Other");
  for each architect finds top 8 clients by latest-day AUA from `perf_cohort`;
  category key = `"{relationship_name} ({relationship_id})"` (collision-safe per contract).
- adv_drill keys match `adv.categories` strings exactly (portal drillParent lookup requirement).
- `adv_drill` added to result conditionally (omit if empty).

Contract ref: ADVI-004 Pattern 0 thread receipt, DS turn 7 (converge).

### 4. ADVI-004 A2: cla in bd-portal-publisher

Added `cla` dict to `build_timeseries_chart()` in same file.

Sub-views:
- `cla.total`: firm-wide NMNC/NMEC AUA; reuses `perf_cohort.cohort` already computed.
- `cla.geo_drill[state]`: per-state NMNC/NMEC AUA; keys match `geo.categories` exactly.
- `cla.adv_drill[arch]`: per-architect NMNC/NMEC AUA; keys match `adv.categories` exactly.
- `cla.geo_city_drill[state][city]`: NMNC/NMEC AUA per city using `cdim.primary_city`;
  top 9 cities per state by latest-day AUA. Optional — omitted if no city data.

NMNC/NMEC rule: trailing-12-month vintage (`months_since_first <= 12`), same formula
as the existing `aua` view in `build_timeseries_chart()`. No new classification introduced.

Helper `_cla_view(df_subset)` added to DRY the groupby/unstack pattern across all 4 sub-views.

Contract ref: ADVI-004 Pattern 0 thread receipt + CTO task order A2.0-A2.3.

### 5. ADVI-004 DC.1: data_contract.xml Updated

Added `adv_drill` and `cla` key definitions to the timeseries_chart.json Source 2 block in
`data_contract.xml`. Documented: structures, category key format, TOP_N_CLIENTS_PER_ARCH,
NMNC/NMEC rule with exact formula, sign conventions, source parquet references, primary_city
derivation with script 04 line citations, geo_city_drill feasibility basis.
Also updated `<date>` to 2026-03-04 and added source_note about the 2026-03-04 extensions.

Syntax verified: `ast.parse()` clean. Committed at `5f60d30e`.

### 6. DT Brief Written for Stream B1

Wrote `docs/briefs/devops-brief-advi-004-adv-drill-cla.md` for `0.4.0_DT_ClientPlatform`.
Covers: what changed, build-and-upload.sh command, terraform plan/apply sequence,
verification steps, next tag `bd-v2.15.0`. Committed at `f2e3c675`.

### 7. ADVI-005 A3.0 Pre-Check: Data History Confirmed

Could not query S3 directly (AWS CLI hanging in Git Bash on Windows). Resolved via session
log archaeology:
- `logs/sessions/2026-02-27/data_scientist/partner_analytics_09_script_implementation.md`:
  "client_performance has exact daily data back to 2020-06-30"
- `logs/sessions/2026-02-26/data_scientist/partner_analytics_new_script_design_task_order.md`:
  "for every day back to 2020-06-30"
- `nna_aua_by_advisor.parquet` is derived from same positions cube — same inception date.

Findings documented:
- Data inception: **2020-06-30**. Data range: ~5.5 years.
- First valid 1Y rolling point: ~2021-07-01 (after 1Y warmup).
- 3Y and Max stacked_bar coverage: **complete** — data exceeds required 4Y lookback.
- No history caveat needed; all 5 stacked_bar periods fully supported.

### 8. ADVI-005 A3.1: stacked_bar in script 10

Modified `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py`.

Added:
- `STACKED_BAR_PERIODS = ('qtd', 'ytd', '1y', '3y', 'max')` constant.
- `compute_stacked_bar()` function:
  - Computes period boundaries: qtd/ytd via `_get_period_boundaries()`;
    1y/3y via trailing Timedelta(365/1095 days); max via parquet inception date.
  - Calls existing `_compute_nna_for_range()` per period — no new data logic.
  - Returns `{period: [AdvisorBarEntry]}` for a single role.
  - `AdvisorBarEntry`: `{advisor_name, advisor_id, inflows, outflows, nna_net}`.
  - `outflows` positive magnitude. `nna_net` signed.
- Assembled into period-outer / role-inner structure per CTO task order A3.1 correction:
  `stacked_bar = { period: { 'architects': [...], 'implementors': [...] } }`
  Note: this differs from thread receipt (role-outer); task order is the binding spec.

### 9. ADVI-005 A3.2: rolling_1y in script 10

Added `rolling_1y` dict extracted from existing `compute_rolling_series()` 1Y window output.
- `rolling_1y.architects`: list of `{advisor_name, advisor_id, series: [{date, nna, inflows, outflows}]}`
- `rolling_1y.implementors`: same shape.
- Full history emitted; frontend slices x-axis by period toggle.
- No new rolling computation — reuses series['1Y'] already produced.
- Point fields `{date, nna, inflows, outflows}` match `Rolling1YDataPoint` contract exactly.

### 10. ADVI-005 A3.3: Backward Compatibility

All legacy keys (`generated_at`, `data_as_of`, `firm_id`, `summary`, `architects`,
`implementors` with 30d/90d/1Y windows) are unchanged. `stacked_bar` and `rolling_1y`
are additive top-level keys. Dry-run preview block updated to show both new keys.

### 11. ADVI-005 DC.1: data_contract.xml Updated

Replaced the thin Source 5 (advisor_rolling_flows) entry with a full documented block:
- Script source (EC2 gold script, not Lambda).
- Data history block: 2020-06-30 inception, 5.5Y range, first 1Y point ~2021-07-01, 3Y/Max complete.
- Legacy key schema for summary/architects/implementors.
- stacked_bar: full structure, AdvisorBarEntry fields, period boundary definitions, sign convention.
- rolling_1y: AdvisorRolling1YSeries structure, daily cadence, all 3 fields, rolling method.

Syntax verified. Committed at `c9b3ab76`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Expand perf_cohort merge (not a separate join) | One merge serves A1 + all CLA sub-views; no extra parquet load |
| _cla_view() helper | 4 CLA sub-views share identical groupby/unstack/fill pattern |
| Iterate adv_categories (not top_architects) for adv_drill | adv_categories is the portal's drillParent key source — must match exactly |
| adv_drill and geo_city_drill both conditional | Omit if empty, consistent with existing geo_drill pattern |
| Period-outer/role-inner for stacked_bar | CTO task order A3.1 explicitly overrides thread receipt (role-outer) |
| rolling_1y reuses series['1Y'] directly | No new rolling math needed; existing output matches contract exactly |
| Data history via session log archaeology (not live S3 query) | AWS CLI hanging in Git Bash on Windows; session logs have confirmed the 2020-06-30 date |
| A4: no patch needed — signed percentiles are intentional | `calculate_nna_distribution_stats()` docstring and bin design confirm signed distribution is correct; abs() is present where it matters (materiality filter, bin construction) |
| A4.2 confirmed from S3 | Live header_metrics.json shows non-degenerate signed distribution; p10=-$46K to p90=+$152K; OH net-outflow state correctly shows all-negative segment |
| A5: Scenario (c) — no mapping exists | No advisorId/advisorName field in opal-users-v2; architects have no portal accounts; email matching not viable (gold layer has no email); recommend `advisorKey` attribute at user creation |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py` | TOP_N_CLIENTS_PER_ARCH + MAX_CLA_CITIES; primary_city to cdim; expanded perf_cohort merge; adv_drill + cla blocks; adv_drill/cla added to result | Yes — `5f60d30e` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml` | adv_drill + cla doc in timeseries_chart.json Source 2; adv_rolling_flows Source 5 fully documented with A3 shapes | Yes — `5f60d30e`, `c9b3ab76` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI-004-adv_drill_cla.md` | Status: pending -> complete | Yes — `5f60d30e` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI-005-rolling_flows_data.md` | Status: pending -> complete | Yes — `c9b3ab76` |
| `data/black_diamond/scripts/gold/10_generate_advisor_rolling_flows.py` | STACKED_BAR_PERIODS constant; compute_stacked_bar(); rolling_1y extraction; both added to return dict; dry-run preview extended | Yes — `c9b3ab76` |
| `docs/briefs/devops-brief-advi-004-adv-drill-cla.md` | New — DT Stream B1 deploy instructions | Yes — `f2e3c675` |
| `docs/briefs/devops-brief-advi-005-rolling-flows.md` | New — DT Stream B2 EC2 deploy instructions | Yes — `75b3b83f` |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DT deploy — bd-portal-publisher (Stream B1) | `docs/briefs/devops-brief-advi-004-adv-drill-cla.md` | 0.4.0_DT_ClientPlatform |
| DT deploy — script 10 EC2 (Stream B2) | `docs/briefs/devops-brief-advi-005-rolling-flows.md` | 0.4.0_DT_ClientPlatform |

---

### 12. ADVI A4.1: Script 09 Bell Curve Code Verification

Read `data/black_diamond/scripts/gold/09_generate_partner_analytics.py`.

Note: the task order referenced `09_build_distribution_stats.py` — the actual filename is
`09_generate_partner_analytics.py`. The file contains the full partner analytics script
including distribution stats functions.

**A4.1 — Function located:**
- `calculate_nna_distribution_stats(nna_values: pd.Series)` — line 320
- This is the bell curve / distribution stats function for per-relationship period NNA

**abs() handling verified present:**

| Location | Line | Code | Purpose |
|----------|------|------|---------|
| Materiality filter | 332 | `vals = vals[vals.abs() >= NNA_MATERIALITY_THRESHOLD]` | Excludes sub-$1K NNA accounts (fees, dividends, rounding noise) |
| Bin max | 348 | `abs_max = float(vals.abs().max())` | Log-spaced bin upper bound from largest magnitude (pos or neg) |
| Bin min | 349 | `abs_min = max(float(vals.abs().min()), 1_000)` | Log-spaced bin lower bound floored at $1K |
| Symmetric bins | 353-357 | `neg_edges = -pos_edges[::-1]` mirrored around zero | Both inflows (positive) and outflows (negative) visible in histogram |

**Percentile design:** Percentiles at lines 374-380 are SIGNED (not abs()). This is
intentional — the function docstring states "signed, symmetric log bins." For a mixed
distribution: p10 reflects the 10th-percentile NNA value (could be large negative for
outflow-heavy segments); p90 reflects the 90th-percentile (typically positive inflow).
Signed percentiles correctly convey the shape of a bimodal inflow/outflow distribution.

**Commit attribution:** The abs() handling landed across two commits after 8247c6d0:
- `792b4e05`: Added `calculate_nna_distribution_stats()` with symmetric log bins + abs() for bin construction
- `9216c922` (2026-03-03): Added `NNA_MATERIALITY_THRESHOLD = 1_000` and abs() materiality filter

All three commits predating the A4 task order (2026-03-03). The fix is present in current CLOUD HEAD.

**A4.2 — S3 verification: BLOCKED**
Cannot read `s3://opal-data-bd/gold/partner_analytics/header_metrics.json` — AWS CLI
non-functional in Git Bash on Windows (hangs with "File association not found for extension .py").
Actual P10/P25/Median/P75/P90 threshold values not confirmed from live data.

**A4.3 — Assessment:** Code analysis confirms the abs() fix landed. No patch needed.
A4.2 remains open pending AWS CLI resolution.

---

### 13. A4.2: header_metrics.json NNA Distribution Verified from S3

AWS CLI issue resolved. Read `s3://opal-data-bd/gold/partner_analytics/header_metrics.json`.

**Total firm NNA distribution — current period:**

| Percentile | Value |
|-----------|-------|
| p10 | -$46,787.40 |
| p25 | -$9,066.01 |
| p50 | -$1,061.62 |
| p75 | +$19,760.20 |
| p90 | +$151,675.42 |

**Assessment:** Non-degenerate. ✓ Not all zero. ✓ Not symmetric. ✓ Signed distribution correctly
reflects real per-relationship period NNA. Median is -$1K (slightly negative — fee noise boundary).
p10 represents top-10% outflow clients; p90 represents top-10% inflow clients.

**Per-segment samples (selected):**

| Segment | Type | Count | p10 | p50 | p90 |
|---------|------|-------|-----|-----|-----|
| TX | state | 464 | -$45,336 | -$1,192 | +$134,753 |
| OH | state | 5 | -$855,614 | -$15,234 | +$10,052 |
| AL | state | 10 | -$3,798 | +$5,069 | +$109,539 |
| travis_penfield | arch | 37 | -$472,924 | -$4,976 | +$201,494 |
| chase_bertrand | arch | 38 | -$20,348 | +$2,766 | +$907,525 |
| 49f_house | arch | 399 | -$49,721 | -$1,258 | +$75,978 |

OH state (predominantly outflow): p10=-$855K, p50=-$15K, p90=+$10K — correctly shows a
net-outflow segment. Signed design is correct for this use case.

Materiality filter confirmed working: TX has 464 counts vs a larger total client base —
accounts with |NNA| < $1K excluded.

**Conclusion: A4.2 verified. No patch needed. Task order complete.**

---

### 14. A5.1+A5.2+A5.3: opal-users-v2 DynamoDB Investigation

**Table schema:**

| Key | Value |
|-----|-------|
| Table name | `opal-users-v2` |
| Partition key | `PK` (String) |
| Sort key | `SK` (String) |
| Item count | 34 |
| SSE | KMS enabled |

PK patterns:
- `USER#{userId}` — user profile records (SK=`PROFILE`)
- `FIRM#{firmId}` — firm records (SK=`META`, `CONFIG#defaults`, `MEMBER#{userId}`)

Fields present on USER#PROFILE items: `userId`, `email`, `name`, `role`, `tier`, `firmId`,
`passwordHash`, `status`, `createdAt`, `updatedAt`, `mustChangePassword`.
Optional legacy fields: `migratedFrom`, `migratedAt`.

Fields NOT present (searched explicitly): `advisorId`, `advisorName`.

GSIs:
- `firmId-index` (PK=firmId, SK=PK) — projects: role, email, name, tier, status
- `email-index` (PK=email, KEYS_ONLY)

**Advisor-tier user records (tier="advisor", firmId="49financial"):**

| userId | email | name |
|--------|-------|------|
| usr_6ad8541dd636 | dan.wohlgemuth@49financial.com | Dan Wohlgemuth |
| usr_dbd5ca809ff8 | lizah.okoniewski@49financial.com | Lizah Okoniewski |

Neither Dan Wohlgemuth nor Lizah Okoniewski appears in `gold/advisors/` prefix
(the canonical list of 60+ advisor slugs). They are 49financial staff with portal access
but are NOT financial architects/advisors in the BD gold data.

**Gold layer architect identifiers (sample from `gold/advisors/` prefix and partner_analytics):**
`travis_penfield`, `chase_bertrand`, `kyle_sims`, `david_farrell`, `ted_grant`,
`dean_dillenberg`, `greg_rosner`, `hunter_lloyd`, `josh_henson`, `matt_foxhall`, and ~50 more.

None of these architect names have any corresponding user account in opal-users-v2.

**Mapping scenario determination:**

```
Scenario: (c) — No existing mapping
```

Evidence:
1. No `advisorId` or `advisorName` field in any opal-users-v2 record.
2. The two advisor-tier 49financial users (Wohlgemuth, Okoniewski) do not correspond to
   any gold layer architect — they are ops/admin staff, not registered advisors.
3. The actual financial architects (Travis Penfield, Kyle Sims, etc.) have NO user accounts
   in opal-users-v2 at all. They cannot log in to the portal.
4. Email-based matching is not viable: the gold layer stores no email addresses for advisors —
   architect identity derives entirely from BD transaction data (first/last name, slugified).

**BLOCKER — escalated to COO and CTO (see Next Steps).**

The Books tab advisor identity resolution cannot be implemented until a mapping from
JWT userId to gold layer advisor slug is established.

**Recommended mapping approach:**

Add an optional `advisorKey` attribute to USER#PROFILE items (e.g., `advisorKey: "travis_penfield"`).
Populate this at advisor user account creation for `tier: "advisor"` accounts. Portal auth reads
this field from the JWT-resolved profile and uses it as the gold data lookup key.

This requires:
- DynamoDB schema extension (additive — no existing records broken)
- Admin onboarding flow: when creating a new advisor user, enter their `advisorKey` from the
  gold layer slug list (available from `gold/advisors/` prefix or architect_leaderboard.json)
- Portal auth middleware: when Books tab requested, verify `advisorKey` matches the requested
  advisor's data segment
- No EC2 or Lambda code changes until the mapping is confirmed populated for real users

**Task order A5 complete — findings documented. Blocker flagged below.**

---

### 15. Stream B2 DT Brief Written

Wrote `docs/briefs/devops-brief-advi-005-rolling-flows.md` for `0.4.0_DT_ClientPlatform`.
Covers: what changed (script 10 only, no infra changes), safe-ec2-deploy.sh command,
EC2 start command for incremental run, verification via S3 JSON key check, next tag `bd-v2.15.1`.
Notes: run_gold_layer.sh incremental mode runs 02-10 sequentially — only script 10 output changes.
Does NOT trigger pipeline-complete to re-run on its own; EC2 boot triggers the run automatically.
Committed at `75b3b83f`.

---

## Blockers

- **A5 BLOCKER — Books Tab Advisor Identity Mapping does not exist (Scenario c).**
  opal-users-v2 contains no `advisorId` or `advisorName` field on any record. The financial
  architects in the gold layer (Travis Penfield, Kyle Sims, etc.) have no user accounts in
  the portal auth system. JWT userId cannot be resolved to a gold layer advisor slug.
  The Books tab scoped access cannot be implemented until an `advisorKey` attribute is added
  to opal-users-v2 USER#PROFILE items and populated for advisor-tier accounts.
  **Escalated to COO and CTO — see Next Steps.**

---

## Current State

**Status:** ALL A-ROLL TASK ORDERS COMPLETE — Scenario (c) blocker flagged to COO + CTO
**Active branch:** `CLOUD`

All five task orders worked this session:
- **ADVI-004** (A1+A2 adv_drill + cla) — complete, committed `5f60d30e`
- **ADVI-005** (A3 stacked_bar + rolling_1y) — complete, committed `c9b3ab76`
- **A4** (script 09 bell curve verification) — complete: code verified + S3 live data confirmed
- **A5** (opal-users-v2 investigation) — complete: Scenario (c) BLOCKER documented

DT deploy briefs written and committed for both streams:
- Stream B1 (bd-portal-publisher Lambda): `docs/briefs/devops-brief-advi-004-adv-drill-cla.md`
- Stream B2 (script 10 EC2): `docs/briefs/devops-brief-advi-005-rolling-flows.md`

Pending: DT to execute both deploys. COO/CTO to resolve Books tab identity mapping gap.

---

## Next Steps

> Ordered by priority.

1. **[COO + CTO] BLOCKER — Books tab advisor identity mapping** (A5 Scenario c)
   No JWT userId → gold layer advisor slug mapping exists in opal-users-v2.
   Required action: add `advisorKey` attribute to USER#PROFILE items for advisor-tier accounts.
   Recommend: admin onboarding flow sets `advisorKey` = gold layer slug (e.g., `travis_penfield`)
   at advisor user creation. Portal middleware reads this field for Books tab scoped access.
   No auth implementation should proceed until this is confirmed populated for real users.
   Downstream affected: 0.4.0_DE_ClientPlatform (portal auth middleware), 0.4.2_RD_AdvisorIntelligence (Books tab).

2. **[0.4.0_DT_ClientPlatform] Deploy Stream B1 — bd-portal-publisher** (commit `5f60d30e`)
   Full instructions: `docs/briefs/devops-brief-advi-004-adv-drill-cla.md`.
   Next tag: `bd-v2.15.0`.

3. **[0.4.0_DT_ClientPlatform] Deploy Stream B2 — script 10 EC2** (commit `c9b3ab76`)
   Full instructions: `docs/briefs/devops-brief-advi-005-rolling-flows.md`.
   Next tag: `bd-v2.15.1`.

**Files to touch next:**
- None on DS side. Pending COO/CTO resolution of A5 blocker.

**Do NOT:**
- Re-enable `build_partner_analytics()` in bd-portal-publisher lambda_handler (DISABLED intentionally).
- Change stacked_bar nesting to role-outer/period-inner (thread receipt shape) — CTO task order is binding.
- Modify existing aua/nna/geo/adv/geo_drill keys in timeseries_chart.json.
- Run `02_build_positions_cube.py --start-date` (known to corrupt data; full rebuild only if needed).
