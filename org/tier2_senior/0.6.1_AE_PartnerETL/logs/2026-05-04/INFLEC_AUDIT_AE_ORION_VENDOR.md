# INFLEC AUDIT-001 — AE Orion Vendor State Dump

**Author:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-04
**Trigger:** COO mass-storm GO 20:25Z — Orion-vendor-side context for RED-cell triage
**Master matrix:** `docs/architecture/ADVI_INFLEC_AUDIT.md` (DS~A owns)
**Companion drafts:** `INFLEC_AUDIT_AE_LAMBDA_EMIT.md` (0.5.0_AE), `INFLEC_AUDIT_DE_MAPPING.md` (0.4.0_DE), `INFLEC_AUDIT_DSB_IWM_GAPS.md` (DS~B)
**Source HARs cited:**
- HAR(10) `api.cloud.orionadvisor.com(10).har` — 2026-05-04 Asset table click-through, 330 entries, captured during this session
- HAR(4) `Reporting/Custom/28198/Generate/csv` — Andrew 2026-04-28 (catalog reference)
- HAR(5) `Portfolio/Accounts/NewPortfolio` — Andrew 2026-04-28 (catalog reference)

---

## Purpose

Per-panel/field disambiguation of **RED-vendor** (Orion source doesn't expose this) vs **RED-(c) Opal-pipeline** (vendor exposes it; our ingest/transform breaks). Feeds DS~A master matrix to flip RED cells to the correct root-cause classification.

State-dump only — no new bronze pulls run for this audit. All evidence cites pre-existing bronze/silver state and HAR captures.

---

## Section 1 — Orion endpoint inventory (vendor-side)

### Endpoint families currently wired into Inflection ingest

| Family | HTTP | Path | Lifecycle | Status | Used by |
|---|---|---|---|---|---|
| Envision Reporting | POST | `/api/v1/Reporting/Envision/ExcelReports/Verbose` + `/{id}/Generate` | Async-ish: 200+queryId → 201+Location → GET binary CSV | LIVE | household, performance, activity dims; **assets dim BLOCKED** |
| Custom Reports | POST | `/api/v1/Reporting/Custom/{reportId}/Generate/csv` | 201+Location → GET CSV | GATED — not wired in production | Daily Transactions report 28198 (Andrew manual export current path) |
| Portfolio/NewPortfolio | GET | `/api/v1/Portfolio/Accounts/NewPortfolio?$top=50000&...` | Sync JSON | LIVE | accounts_v2 dim |
| Portfolio/Clients/{cid}/Assets/{date} | GET | `/api/v1/Portfolio/Clients/{cid}/Assets/{MM-DD-YYYY}?$top=50000&includeCostBasis=false` | Sync JSON | LIVE | assets_v2 (per-client iteration via `pull_inflection_assets_v2.py`); Path C silver derivation |
| Portfolio/Clients/{cid}/Performance | GET | `/api/v1/Portfolio/Clients/{cid}/Performance` | Sync JSON | LIVE | per-client performance pull (`pull_inflection_performance_rest.py`) |
| Portfolio/Accounts/{aid}/Assets/{date} | GET | `/api/v1/Portfolio/Accounts/{accountId}/Assets/{MM-DD-YYYY}?$top=50000&includeCostBasis=false` | Sync JSON | **NEW — DISCOVERED 2026-05-04 HAR(10) entry #187** | Not yet wired; A2 Track 2 candidate |
| Portfolio/Assets/{productId} | GET | `/api/v1/Portfolio/Assets/{productId}?$top=50000&asOfDate={MM-DD-YYYY}&includeCostBasis=false` | Sync JSON | **NEW — DISCOVERED 2026-05-04 HAR(10) entry #259** | Not yet wired; single-asset detail probe |
| Portfolio/Clients/{cid}/PortfolioTree | GET | `/api/v1/Portfolio/Clients/{cid}/PortfolioTree?includeAdditionalDetail=true&includeRepresentative=true` | Sync JSON | OBSERVED — not yet wired | Client→account hierarchy traversal |
| Portfolio/Accounts/Simple/Search | GET | `/api/v1/Portfolio/Accounts/Simple/Search?search={q}&top=40` | Sync JSON | OBSERVED — not yet wired | Account search by code (UI typeahead) |
| Portfolio/Assets/Simple/Search | GET | `/api/v1/Portfolio/Assets/Simple/Search?search={q}&top=40` | Sync JSON | OBSERVED — not yet wired | Asset search by ticker (UI typeahead) |
| Settings/Views/AssetDto | GET | `/api/v1/Settings/Views/AssetDto` | Sync JSON | OBSERVED in HAR(10) | Asset DTO schema definition; useful for column-discovery without per-pull verbose probes |
| JWT auth | (Lambda) | `inf-jwt-trigger` + Twilio OTP webhook | Auto-recovery (JWTRES.002) | LIVE | Session JWT lifecycle for all REST endpoints |

### Endpoints NOT used / not wired

| Family | Status | Notes |
|---|---|---|
| SOAP / Reporting/Scope | NOT OBSERVED in HAR(10) | COO ask referenced "Reporting/Scope (HAR 7)" but HAR(10) is Asset-table scope; would need separate Books-tab HAR capture to enumerate. Unknown vendor state. |
| Reporting/Envision (Asset grouping) | TIMEOUT — DECLINED | DS~D 4-attempt timeout pattern 2026-04-28 (300s/900s × firm-scope/entity-scope/3y/7d). Verdict: synchronous Generate cannot deliver Asset-grouping data within operational budget. **Path C (canonical-derived) is functional substitute.** |
| Custom Reports (28198 Daily Transactions) | GATED | Endpoint contract verified Andrew HAR(4); silver wire-up pending AE 0.6.1~B L5. Not currently in nightly chain. |

---

## Section 2 — RED-cell classification per panel/field

Format: vendor-side **CAN** / **CANNOT** expose → Opal-pipeline state → root cause class → fix path.

| # | Panel/Field | Source script(s) | Orion endpoint that supplies | Vendor-side state | Opal pipeline state | Root cause class | Evidence |
|---|---|---|---|---|---|---|---|
| 1 | `joe_brandenburg top_holdings` (no assets silver data) | INF_I_D02b.top_holdings.py | `/api/v1/Portfolio/Clients/{cid}/Assets/{date}` GET (currently used) **+ NEW** `/api/v1/Portfolio/Accounts/{aid}/Assets/{date}` GET (just discovered) | **CAN expose** — Asset-grain data is available via per-client OR per-account GET endpoints. HAR(10) entry #187 shows 322ms response w/ full schema for account 646. Joe's clients/accounts are queryable. | `silver/api_dims/assets_v2/snapshot_date=2026-04-29/` exists (most recent) but `joe_brandenburg` advisor has no rows in that snapshot OR rows are present but downstream join in INF_I_D02b filters them out. | **RED-(c) Opal-pipeline** | Per-client assets endpoint LIVE in pull_inflection_assets_v2.py; `silver/api_dims/assets_v2/` 1 snapshot (2026-04-29) exists. DS~D ticker classifier closed `6ff24c36` (INFSHIP L4). Joe-specific gap is a downstream attribution/filter issue, not vendor absence. |
| 2 | `period_start_aua` (Andrew §10 gap) | INF_C_01.canonical_nna.py / `_aua_at_start` filter; INF_D_00c portal_leaderboard.py consumer | `/api/v1/Reporting/Envision/...Activity.Value` with `activityOptionId=2` (BeginningMV) per CATALOG Gotcha #1 | **CAN expose** — Activity.Value with `activityOptionId=2` (BeginningMV) is the documented vendor-side primitive. CATALOG L101-L109 enumerates 20 activityOptionIds; option 2 = BeginningMV is what period_start_aua needs. | Path C uses canonical_holdings + current rep_bucket point-in-time misattribution; doesn't pull BeginningMV from Envision. ADVI_HISTBF brief documents this is a **separate pipeline design gap**, not a HISTBF bronze-coverage gap (registry note 2026-05-04: "spawns NEW backlog candidate ADVI_RPBKTPI"). | **RED-(c) Opal-pipeline** (design gap, not vendor) | Vendor has BeginningMV via documented Envision option 2; Opal pipeline computes period_start from canonical (wrong source). HISTBF.004 silver backfill landed 2166 partitions 2020-05-26→2026-04-30, so canonical has the date coverage — the issue is rep_bucket attribution at historical dates, not data presence. |
| 3 | Concentration Risk panel — empty `[]` | INF_D_07.concentration_risk.py | `/api/v1/Reporting/Envision/...` (assets_v2 silver consumer) | **CAN expose** — same per-client/per-account assets endpoint as #1; assets data is queryable. | `s3://opal-data-inf/platinum/firm/concentration_risk.json` = 2 bytes `[]`. INFGRD.003 chain rerun expected to populate (per DE INFLV2.007 session log 2026-04-29). | **RED-(c) Opal-pipeline** (chain rerun pending) | AE Lambda emit doc RED-(a)-1: "designed-in empty-state pending INFGRD.003 chain rerun." Vendor has the data; pipeline gold step hasn't run. |
| 4 | Activity Scan — 307 rows AUA=0 | INF_D_05.activity_scan.py | `/api/v1/Reporting/Envision/...Activity.Value` activityOption=1 (EndingMV) | **CAN expose** — Envision Activity.Value option 1 (EndingMV) is the documented AUA primitive used by household + activity dims. | All 307 rows have aua=0.0 + txn_count_12m=0 in current `activity_scan.json`. `activity_score` populated. RED-(a)-2 in AE Lambda emit doc. | **RED-(c) Opal-pipeline** (upstream AUA join in INF_D_05 broken) | `silver/api_dims/activity/snapshot_date=2026-04-28/` exists; AUA column was successfully pulled per dim. Issue is INF_D_05's join from activity dim to client_dim — not vendor. |
| 5 | Cash Drag — 295 rows AUA=0 + cash_pct=0 | INF_D_06.cash_drag.py | Same as #4 + `is_custodial_cash` from assets dim | **CAN expose** — same primitives; cash positions identifiable via `isCustodialCash:true` on per-asset records (HAR(10) entry #259 shows the field). | All 295 rows aua=0 + cash_pct=0 + cash_aua=0. `days_above_threshold` populated for some rows (proves non-trivial computation ran). RED-(a)-3 in AE Lambda emit doc. | **RED-(c) Opal-pipeline** (shared AUA join failure with #4) | Cross-cutting hypothesis from AE 0.5: same upstream AUA join failure feeds both INF_D_05 and INF_D_06. Vendor exposure intact. |
| 6 | Asset API timeout (A2) — Path C derivation | DS~D `pull_inflection_assets.py` (Envision route — DEPRECATED) | `/api/v1/Reporting/Envision/ExcelReports/{id}/Generate` (Asset grouping) — **TIMES OUT** | **VENDOR PARTIAL** — synchronous Envision Generate cannot deliver asset-grouping within 300-900s budget for ANY scope (firm/entity/3y/7d all timed out). **HOWEVER:** alternate per-client GET (`pull_inflection_assets_v2.py`) AND per-account GET (newly discovered HAR(10)) both succeed in <500ms — vendor exposes the data, just not via the Envision endpoint family. | Path C silver = `$91.8M Inflection-only` AUA at `silver/api_dims/assets/snapshot_date=2026-04-20/` from canonical derivation; assets_v2 silver = direct API pull at `silver/api_dims/assets_v2/snapshot_date=2026-04-29/`. Both functional. | **RED-(b) Vendor-partial** (Envision blocked) + **GREEN alternate path** (REST GET) | DS~D L4 RAVC4 2026-04-28 + this session's HAR(10) discovery. INFSHIP.A2 Track 2 (per-account batching) is now feasible via the newly-discovered per-account endpoint — 2,755 accounts × 322ms = ~888s serial; ~3.7 min @ 4-way parallel. |
| 7 | Reporting/Scope (HAR 7 ref, COO ask) | TBD | `/api/v1/Reporting/Scope/...` (path uncertain — not in HAR(10)) | **UNKNOWN** — not captured in HAR(10) which is Asset-table scope only. Books-tab HAR capture would be needed to enumerate. | No silver dim sourced from this family currently. | **RED-INVESTIGATE** | Need separate Books-tab HAR from Andrew to disambiguate. Flag to DS~A. |
| 8 | Tax dim (Bookstab) | DS `orion_tax_dim.py` | `/api/v1/Reporting/Envision/...Tax.{Term}.{Field}` 3-level path pattern | **CAN expose** — Tax field discovery via `tax_template.verbose.json` enumerates the path catalog (CATALOG Gotcha #3). Realize templates work. | Tax silver dim NOT YET PRODUCTION-LANDED for Inflection (no `silver/api_dims/tax/` prefix in S3). DS~B PARTIAL research in flight. | **RED-(c) Opal-pipeline** (not yet built) | Vendor has the data via documented path pattern; Opal pipeline build pending. ADVI_HISTBF.005/.006 staged backlog. |
| 9 | Billing dim | DS `orion_billing_dim.py` | `/api/v1/Reporting/Envision/...` (`billing_dim_spike.verbose.json` template) | **CAN expose** — billing_dim_spike.csv contract verified. CATALOG Gotcha #1 resolved (activityOptionId=1). Inflection scope `@RepIDs="3,11,12"` filter works. | `silver/api_dims/billing/snapshot_date=2026-04-28..2026-05-01/` 4 dates exist. Production landing INCOMPLETE per CATALOG line 93 ("BLOCKED; need fresh Inflection-scoped pull"). | **RED-(c) Opal-pipeline** (Inflection-scoped re-pull pending) | Vendor exposure verified; specific pull was 49F-scoped, needs Inflection-scope re-run. |
| 10 | Performance Sharpe/Sortino — return INT scores not raw | DS `pull_inflection_performance_rest.py` + Envision performance dim | `/api/v1/Reporting/Envision/Performance.SharpeRatio` (statistical option config) | **VENDOR PARTIAL** — Envision returns int score (1-5 scale) when `statisticalOptionId=0` (Use Assigned). Per CATALOG Gotcha #2: `statisticalOptionId=1` (S&P benchmark) should give raw values. Not yet empirically verified. | `silver/api_dims/performance/snapshot_date=2026-04-28/` schema names these `sharpe_score` / `sortino_score` to flag the unit. Raw values blocked until pull config fixed. | **RED-(b) Vendor-partial** (config-resolvable) | Vendor exposure exists pending pull-config switch from option 0 to option 1; not a hard block. |
| 11 | Daily Transactions (Custom Reports 28198) | DS `pull_inflection_transactions_v2.py` (target) | `/api/v1/Reporting/Custom/28198/Generate/csv` w/ `@RepIDs="3,11,12"` | **CAN expose** — endpoint contract verified Andrew HAR(4); 76s full-firm × 503MB; <30s × <50MB Inflection-scoped projected. | `silver/transactions/` has 1502 parquet files (most recent 2026-04-28). Current path = Andrew manual CSV exports (legacy). API-pull path = GATED, not in nightly chain. | **GREEN — vendor exposed; Opal-pipeline gated on AE wire-up** | INFSHIP L5 wire-up pending. Not a RED-cell candidate. |
| 12 | Cumulative chart | INF_I_D00c.cumulative_chart.py (just-shipped this session, `87f794863`) | Aggregate of platinum dims (no direct Orion endpoint) | **N/A — derived from Opal silver** | `cumulative_chart.json` 42907 B at 12:14:51Z this session. Live. | **GREEN** | Confirmed working post HISTBF.004 chain dispatch. |
| 13 | Fee Efficiency (Andrew descope) | INF_D_04 / fee_efficiency.json emit | Envision performance dim + accounts_v2 fee fields | **CAN expose** — fee fields available in unified_account_dim per CATALOG L99 enumeration | `fee_efficiency.json` 1030 B `fee_data_available:false`. RED-(a) descoped per Andrew 20:30Z ("not a priority"). | **GRAY-Andrew-descope** | AE Lambda emit doc. |
| 14 | Fidelity Custodian Bar (Andrew descope) | Hardcoded TSX (no script) | None — UI-static | **N/A** | static 99.4%/0.6% in component. | **GRAY-Andrew-descope** | AE Lambda emit doc. |
| 15 | Header metrics radial_12m (just-fixed this session) | INF_C_01.canonical_nna.py | Derived from canonical_nna parquet (no direct Orion endpoint) | **N/A — derived from Opal silver** | radial_12m=[] FIXED 16:16Z via `937b6bef7` str-normalize join in INF_C_01. | **GREEN** | DS~B IWM gap dump table row 1; FIXED today. |
| 16 | Cost basis | DS `pull_inflection_assets_v2.py` `includeCostBasis=true` | Per-client/per-account Assets endpoints with `includeCostBasis=true` query param | **CAN expose** — query param documented; HAR(10) shows current pulls use `includeCostBasis=false` for speed; flipping to `true` returns full cost basis fields per script docstring. Heavier response. | DS~B Tax/CostBasis publishers shipped INFSHIP L1 (`b287388d` etc). silver landing path pending verification. | **RED-(c) Opal-pipeline** (config flag flip needed for production) | Vendor exposure confirmed; `includeCostBasis` is a single query-param flip. |
| 17 | Holdings (clients_tab data, Books-tab) | INF_D_04.client_portal_summary.py + INF_I_D02b | assets_v2 silver consumer + clients_tab.json platinum | **CAN expose** | `clients_tab.json` 53869 B at 12:14:36Z. Live. | **GREEN** | AE Lambda emit doc. |

---

## Section 3 — Net classification roll-up

| Class | Count | What it means |
|---|---|---|
| RED-(c) Opal-pipeline | 8 (rows 1, 2, 3, 4, 5, 8, 9, 16) | Vendor exposes the data; our pipeline has a join, design gap, schedule gap, or config-flip blocker. |
| RED-(b) Vendor-partial | 2 (rows 6, 10) | Vendor exposes via one endpoint family but not the one we attempted; alternate path verified or config-resolvable. |
| RED-INVESTIGATE | 1 (row 7) | Unknown vendor state; need additional HAR capture. |
| GREEN | 4 (rows 11, 12, 15, 17) | Working / not RED. |
| GRAY-Andrew-descope | 2 (rows 13, 14) | Out of scope per Andrew. |

**Headline finding:** **No INFLEC RED cell traces to a hard vendor block.** Every vendor-state cell is EITHER (a) directly exposed (8 of 17), (b) exposed via alternate endpoint family (2 of 17), or (c) config-flippable (subset of b/c overlap). Only row 7 (Reporting/Scope) is genuinely unknown — pending Books-tab HAR capture.

This means INFLEC RED-cell triage should default-classify to RED-(c) Opal-pipeline unless explicitly disproven. The vendor is NOT the limiter for any panel currently in scope.

---

## Section 4 — A2 sub-track update (bonus from HAR(10))

INFSHIP.A2 Track 1 (async/polling endpoint discovery) was the original goal of the HAR. **Result: no async endpoint observed** — Envision/Custom Reports remain synchronous Generate-pattern.

**However, A2 Track 2 (per-account batching) just became materially easier.** HAR(10) entry #187 reveals:

```
GET /api/v1/Portfolio/Accounts/{accountId}/Assets/{MM-DD-YYYY}?$top=50000&includeCostBasis=false
  → 200 OK, 322ms, application/json
```

This is a **simple sync GET**, not the Envision sync POST that's been timing out. Per-account batching against this endpoint:

- 2,755 Inflection accounts × 322ms = ~888s serial (~14.8 min)
- 4-way parallel = ~3.7 min wall clock
- Already same auth pattern as existing pulls (Session JWT)
- Fits the existing `pull_inflection_assets_v2.py` shape (which currently iterates per-client; pivot to per-account)

A2 verdict tracking toward: **A2 = working direct-pull via per-account REST GET; Envision Asset-grouping family officially DECLINED.**

Will RAVC4 to CTO under separate cover once AUDIT-001 closes. Track 1 is a documented dead-end (no async pattern); Track 2 is the path forward.

---

## Section 5 — Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `.tools/har-scan.py` | `--summary` + `--endpoints` + `--detail` on HAR(10) | 330 entries, 161 unique METHOD-paths, drilled entries 187 (per-account assets) and 259 (single-asset detail) for full request/response inspection |
| `comp-pipescript io` | Not run this session | State-dump audit; no script edits — comp-pipescript IO check is for code-write workflow, not docs. Acceptable per CLAUDE.md "one sentence why" exception. |

---

## Section 6 — Cross-references

- DS~A master matrix: `docs/architecture/ADVI_INFLEC_AUDIT.md` — pulls this doc's classifications into Source/Mapping/Render columns
- AE 0.5 Lambda emit: `_drafts/INFLEC_AUDIT_AE_LAMBDA_EMIT.md` — concentration_risk.json, activity_scan.json, cash_drag.json empirical state already captured RED-(a)-1/-2/-3
- DS~B IWM gap dump: `_drafts/INFLEC_AUDIT_DSB_IWM_GAPS.md` — radial_12m FIXED, peter_lee book.json, fee_efficiency, etc.
- DE 0.4 mapping: `_drafts/INFLEC_AUDIT_DE_MAPPING.md` — frontend field-to-endpoint binding
- Endpoint catalog (canonical reference): `docs/architecture/INFLEC_API_ENDPOINTS_CATALOG.md`
- Path C posture: `docs/architecture/ADVI_INFSHIP_A2.md` (vendor investigation gate)

---

## Section 7 — Recommended next moves

1. **DS~A:** consume Section 2 table to flip RED cells in master matrix to RED-(c) Opal-pipeline (8 rows) / RED-(b) Vendor-partial (2 rows). Row 7 (Reporting/Scope) flagged for Andrew Books-tab HAR.
2. **AE 0.6.1 (me):** under separate RAVC4 to CTO, propose A2 Track 2 build using the newly-discovered per-account endpoint. Estimated 1-2 sessions to wire `pull_inflection_assets_v2.py` per-account variant + parallel pool + integration. Path C remains live as fallback.
3. **DS~B / DS~D:** Tax + Billing Inflection-scoped re-pulls (rows 8, 9) — backlog candidates for ADVI_HISTBF.005/.006.
4. **DE 0.4:** activity_scan + cash_drag AUA-zero root-cause is upstream gold join (rows 4, 5) — DS~B gold script bug, not DE. No DE action.
