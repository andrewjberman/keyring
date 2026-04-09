# Platinum Layer Architecture Strategy

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-08
**Status:** Architecture proposal -- pending Andrew approval
**Audience:** Pod 4 (0.4.0_DS, 0.4.0_DE, 0.4.0_DT), AE (0.6.0)

---

## The Problem

The portal's data-serving layer has no clean boundary between analytical computation
and portal presentation. Gold-layer scripts (Groups A-D) write to `gold/` under a
mix of paths (`gold/artifacts/`, `gold/entities/`, `gold/views/`, `gold/canonical/`),
and the portal reads from all of them through two different mechanisms:

1. **Direct S3** via CloudFront (`shared-advisor-router` rewrites URL to `gold/` key)
2. **Lambda proxy** (`opal-partners-data` reads `gold/` parquets and JSONs)

This creates several problems:

- **No serving boundary.** Group C scripts (C_06, C_08) write portal-facing JSON directly
  to `gold/`. The portal reads analytical artifacts that were never designed for
  browser consumption.
- **Over-fetching.** The Books tab fires 4 separate fetches at L3 (client drill),
  including pulling a full AUA timeseries just to sum 90 days into three numbers.
- **Scattered ownership.** Portal-facing files come from D_00, D_01, D_02, D_03, C_06,
  and C_08 -- six different scripts across two groups. No single script owns the
  portal contract for any given page.
- **No enforcement.** Nothing prevents a new Lambda route from reading any `gold/` file.
  The serving contract is implicit in code, not explicit in structure.

---

## The Solution: Platinum Layer

Introduce `platinum/` as the portal-serving prefix in S3. The rule:

> **`gold/` = analytical outputs.** Parquets, intermediate views, full-history
> timeseries, validation artifacts. Scripts read from other scripts here.
>
> **`platinum/` = portal-serving outputs.** Pre-computed, lightweight JSONs
> optimized for what the portal actually displays. CloudFront and Lambda
> read ONLY from `platinum/`.

Group D scripts become the **publishers** that read from `gold/` and write to
`platinum/`. No Group A/B/C script writes to `platinum/`. No portal component
reads from `gold/`.

---

## Migration Strategy

### Phase 0: Audit (current phase)

Map every portal page/tab to:
1. What data it fetches (API routes + S3 reads)
2. What gold/ files back those fetches
3. Which script produces each file
4. What the portal actually renders from that data (vs what it discards)

This audit exists for the Books tab (see Reference Documents below). It must be
repeated for every tab on the Advisor Intelligence page and every other portal
page that reads from `gold/`.

### Phase 1: Books Tab (D_04)

The first concrete deliverable. D_04 reads gold/ outputs from C_06, C_08, D_00,
D_02, D_03 and writes uniform `summary.json` files to `platinum/` at every
drill level (firm, advisor, client, account). The portal migrates Books tab
fetches to read from `platinum/` exclusively.

See: `docs/briefs/data-scientist-D_04-client-portal-summary-spec.md`

### Phase 2: Remaining Advisor Intelligence Tabs

Each tab on the Advisor Intelligence page needs the same treatment:

| Tab | Current Data Sources | Audit Status |
|-----|---------------------|-------------|
| Books | D_00, D_02, D_03, C_06, C_08 | **Done** (Phase 1) |
| Asset Overview | D_00, D_03 | Not started |
| NNA / Flows | D_00 | Not started |
| Partner Analytics | D_01 | Not started |
| Fee Efficiency | C_08, D_00 | Not started |
| Leaderboard | D_00 | Not started |

For each tab:
1. Read the page component (tsx) and trace every `useEffect` / data fetch
2. Map each fetch to the gold/ file it reads
3. Identify what the component actually renders vs what it discards
4. Design the platinum/ output that serves exactly what's rendered
5. Either expand D_04 or create new D_05+ scripts as publishers

### Phase 3: Non-Advisor-Intelligence Pages

Pages outside Advisor Intelligence that read from gold/:
- Model Portfolios (yang pipeline -- `opal-data-portal-v2/json/`)
- Market Overview (market-overview pipeline -- `opal-data-portal-v2/json-tiered/`)
- Portfolio Management (`opal-data-pm/`)
- SmartX AUM (smartx pipeline -- `opal-data-portal-v2/json/portfolios/`)

These are separate pipelines with their own S3 buckets. The platinum pattern
applies to them too, but they are lower priority because they already have
relatively clean serving paths (pipeline writes JSON, CloudFront serves it).

### Phase 4: Infrastructure Migration

Once all portal reads point to `platinum/`:
1. Update `shared-advisor-router` Lambda@Edge to rewrite to `platinum/` prefix
2. Update `opal-partners-data` Lambda to read from `platinum/`
3. Update API Gateway routes if path patterns change
4. Update CloudFront cache behaviors if origin paths change
5. Remove legacy gold/ reads from all Lambda functions
6. Add CI check: no portal code may reference `gold/` paths

---

## Audit Methodology (for each tab/page)

The pod needs to execute this process for every portal page. The output is a
table like the one produced for Books tab in Phase 1.

### Step 1: Trace the frontend

Read the page component (`.tsx`). For every `useEffect` that fetches data:
- What API endpoint does it call?
- What triggers it? (page load, drill selection, user action)
- What state does it set?
- What does the JSX render from that state?

### Step 2: Trace the API layer

For each API endpoint:
- Is it a direct S3 read (CloudFront path matched by `shared-advisor-router`)?
- Is it a Lambda proxy route (API Gateway -> `opal-partners-data` or other Lambda)?
- What S3 file(s) does it read?
- Does it transform the data or pass through?

### Step 3: Trace to gold/ source

For each S3 file:
- Which gold script produces it?
- What is its full schema/shape?
- How large is it (bytes, row count)?

### Step 4: Identify waste

Compare what the frontend renders vs what the file contains:
- Does the frontend use 10% of a 100KB file?
- Does it pull a full timeseries to compute a single number?
- Does it load data eagerly that could be deferred?

### Step 5: Design platinum output

Write a schema for the platinum file that serves exactly what the frontend needs.
No extra fields, no full histories when snapshots suffice, no arrays when
aggregates suffice.

---

## Platinum Folder Structure

```
platinum/
  firm/
    dashboard.json              # N1: leaderboard, headline, fee efficiency
    mix_summary.json            # N1: mix pie, quarterly bars, concentration
    timeseries_chart.json       # Asset Overview: firm AUA/NNA timeseries
    rolling_flows.json          # NNA/Flows: advisor rolling flows
    snapshots/
      aua_by_architect.json     # Asset Overview: snapshot tiles
      aua_by_state.json
      aua_by_tax_status.json
      aua_by_region.json
    filters/
      dimensions.json           # Shared: filter dropdown values
  advisors/
    {id}/
      summary.json              # L2: book, mix, composition, top holdings
  clients/
    {rel_id}/
      summary.json              # L3: detail, mix, composition, decomposition
  accounts/
    {acct_id}/
      summary.json              # L4: composition
  partner_analytics/
    header_metrics_quarterly.json
    header_metrics_monthly.json
    header_metrics_annual.json
```

This is the target state. Phase 1 (D_04) delivers `firm/`, `advisors/`, `clients/`,
`accounts/` for the Books tab. Subsequent phases fill in the rest.

---

## Auth / Serving Path (unchanged)

The platinum migration does NOT change the auth architecture:

```
Browser
  -> CloudFront (opalinvest.dev)
  -> auth-validator-edge (JWT validation, header injection)
  -> shared-advisor-router (rewrite /api/scoped/advisor-intelligence/* to S3 key)
  -> S3 opal-data-bd (platinum/ prefix instead of gold/)
```

The only infrastructure change is:
- `shared-advisor-router` rewrites to `platinum/` instead of `gold/`
- `opal-partners-data` Lambda reads from `platinum/` for all serving routes
- API Gateway routes and authorizer stay the same

---

## What Stays in gold/ (permanently)

| Path Pattern | Description | Why It Stays |
|---|---|---|
| `gold/dimensions/*.parquet` | Dimension tables (A_00-A_04) | Script-to-script input |
| `gold/timeseries/*.parquet` | Performance, positions, holdings | Analytical computation |
| `gold/canonical/*.parquet` | Holdings, lots, gains, performance, NNA | Core canonical stack |
| `gold/views/*.parquet` | Attribution, tax, team lookups | Intermediate views |
| `gold/validation/*.json` | AUA certification, validation | QA/audit |
| `gold/canonical/watermarks.json` | Pipeline state | Operational |
| `gold/entities/clients/{id}.json` | Full daily mix + concentration timeseries (C_06) | Analytical archive, future use |
| `gold/entities/clients/{id}_views.json` | Full period mix views (C_06) | Analytical archive |
| `gold/entities/clients/{id}/aua_timeseries.json` | Full AUA timeseries (D_02) | Analytical archive |

Group A/B/C outputs are never modified. Group D outputs continue writing to `gold/`
as before -- D_04+ reads them and publishes to `platinum/`.

---

## Roles

| Agent | Responsibility |
|-------|---------------|
| **0.4.0_DS** (this agent) | Design platinum schemas, write D_04 script, define data contracts |
| **0.4.0_DE** | Trace frontend components, map fetches to data sources, update portal API calls to read from platinum |
| **0.4.0_DT** | Deploy D_04 to gold runner, update shared-advisor-router, update opal-partners-data Lambda, CloudFront invalidation |
| **0.6.0_AE** | EC2 gold runner: add D_04 to dispatch chain, run full pipeline, verify platinum/ output |

---

## Reference Documents

These four documents form the complete reference chain for this initiative:

### 1. Gold Pipeline Script-to-File Flow
`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-08/gold_pipeline_script_file_flow.md`

Every gold script, its inputs, outputs (full S3 keys), downstream consumers,
execution order, and dependency DAG. Use this to understand what produces what
and what feeds what.

### 2. Portal Auth & Data Serving Flow
`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-08/portal_auth_and_data_serving_flow.md`

The two serving paths (direct S3 via CloudFront vs Lambda proxy), the full auth
chain (custom JWT at edge + custom API GW authorizer), all CloudFront path routing,
every API route mapped to its source S3 file, and infrastructure source file locations.

### 3. D_04 Books Tab Publisher Spec
`docs/briefs/data-scientist-D_04-client-portal-summary-spec.md`

The concrete Phase 1 deliverable. Current fetch map for every Books tab drill level,
target fetch map with platinum paths, JSON schemas for every output file, D_04
input/output summary, execution position in dispatch chain, and open questions.

### 4. Platinum Layer Architecture Strategy (this document)
`docs/briefs/data-scientist-platinum-layer-architecture-strategy.md`

The big-picture architecture: why platinum exists, the phased migration plan,
audit methodology for each tab, target folder structure, role assignments,
and what stays in gold permanently.

---

## Summary: The Big Picture

The work begins with a narrow, concrete deliverable: **D_04**, a new gold-layer
script that publishes pre-sliced, lightweight JSON artifacts for the Books tab
to `platinum/`. This eliminates the current pattern where the portal pulls full
analytical datasets just to render snapshots, and closes the C_06/C_08 leak where
Group C scripts write directly to portal-facing paths.

D_04 is Phase 1 of a broader architectural finalization. The platinum layer
establishes a clean, enforceable boundary between computation (gold/) and
presentation (platinum/). Every portal page will eventually read exclusively
from platinum/, with Group D scripts as the canonical publishers. The audit
methodology defined here -- trace frontend, trace API, trace to gold source,
identify waste, design platinum output -- must be applied to every tab on the
Advisor Intelligence page and eventually every page that reads pipeline data.

The sequence:
1. **D_04 (Books tab)** -- proves the pattern, delivers immediate performance win
2. **Tab-by-tab audit** -- DE traces every remaining tab's fetches and data paths
3. **D_05+ scripts** -- publish remaining tabs to platinum/ (or expand D_04)
4. **Infrastructure cutover** -- shared-advisor-router and Lambda reads point to platinum/
5. **Enforcement** -- CI check that no portal code references gold/ paths

The four reference documents linked above give the pod everything needed to
execute: what the scripts produce, how the data flows to the browser, what
the Books tab specifically needs, and how to repeat the process for every
remaining surface.
