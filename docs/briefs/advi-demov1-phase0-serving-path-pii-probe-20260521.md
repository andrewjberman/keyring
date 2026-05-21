# ADVI_DEMOV1 Phase 0 — Serving-Path + PII Verification Probe

**TO:** ADVI_DEMOV1.000 (`2.0.0_SA_COO~C`)
**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-21
**Type:** Read-only verification probe — ships no code, creates no infra
**Feeds:** the CTO PRD (`docs/architecture/ADVI_DEMOV1.md`) risk section

---

## 0. Verdict summary

| Item | Result |
|---|---|
| §3.2 static-platinum serving mechanism | **RESOLVED** — Lambda@Edge `shared-advisor-router` runtime origin-mutation, driven by `FIRM_CONFIG` |
| Demo-firm serving go/no-go | **GO** — multi-tenant routing was purpose-built for firm onboarding |
| Dynamic server topology | `opal-partners-data` is the sole dynamic server; portal is **NOT** strictly platinum-only (see §4) |
| PII leak surface | Larger than the ADVI_ANONYM map — **7 DEMOV1-ONLY field classes** + S3-key slugs + free-text narrative (see §3) |
| Lambda pseudonymizer | **RETIRED 2026-04-15** — `needs_pseudonymization()` returns `False`; real PII is served cleartext |
| Firm-specific code branches a `demo` firm trips | **2 required portal changes** (`firmAccess.ts`, `_partners/`); the rest behave correctly (see §5) |

---

## 1. §3.2 LINCHPIN — static-platinum serving mechanism (DEFINITIVE)

The `/api/scoped/advisor-intelligence/platinum/**` routes are served by:

**CloudFront distribution `EVTSA9VEHNZVH`** → behavior `/api/scoped/advisor-intelligence/*`
→ S3 origin, gated by **two Lambda@Edge functions**:

1. **`auth-validator-edge`** (viewer-request) — validates the Cognito JWT, injects
   `X-Firm-Id` + `X-Advisor-Role`/`X-Advisor-Id`/`X-User-Role`/`X-User-Tier`/`X-User-Type`
   headers. Source: `infra/aws/lambda-edge/auth-validator-edge/index.mjs`.
2. **`shared-advisor-router`** (origin-request) — **runtime origin-mutation**: reads
   `X-Firm-Id`, resolves the target bucket, and mutates `request.origin.s3.domainName`
   **in place** (object identity preserved so OAI auth survives). Source:
   `infra/aws/lambda-edge/shared-advisor-router/index.mjs`.

### Bucket resolution — three branches (`shared-advisor-router/index.mjs:183-205`)

| Branch | Condition | Bucket |
|---|---|---|
| Internal staff | `X-Firm-Id === "opal-capital"` | reads `?firm=<slug>` query param → `opal-data-${slug}`; missing → HTTP 400 |
| Mapped partner | `firmId ∈ FIRM_BUCKET_MAP` | `FIRM_BUCKET_MAP[firmId]` (full bucket name) |
| Unmapped fallback | else | `opal-data-${firmId}` (intentional; CI-sentinel-tested) |

**`?firm=` is consumed ONLY for `opal-capital` internal staff** proxying into a
partner view. Partner firms (49financial, inflection) route purely by the
JWT-derived `X-Firm-Id` header.

`FIRM_BUCKET_MAP` derives from **`FIRM_CONFIG`** — the single-source module
`infra/aws/lambda-edge/_shared/firm-config.mjs` (ADVI_FIRMSEP.03), consumed by
*both* edge functions. Current entries:

```
49financial → opal-data-bd   "49 Financial"
inflection  → opal-data-inf  "Inflection Wealth Management"
mockadv     → opal-data-bd   "Mock Advisor (test account)"
```

`mockadv` is an existing **non-real test-account firm** — direct precedent for a
demo firm entry.

### URI rewrite (`index.mjs:208-256`)

`platinum/*` paths pass through directly to `/{suffix}` S3 keys — **except**
`platinum/{advisors,clients}/{id}/summary.json`, which return **HTTP 401**
("must be accessed through the API"): those carry client-name PII and are routed
through the `opal-partners-data` Lambda instead.

Origin auth is **OAI `E139998VWH0PD`** (not OAC — OAC breaks with Lambda@Edge
dynamic origin mutation, per ADVI_APISCP.002). Both `opal-data-bd` and
`opal-data-inf` bucket policies grant this OAI principal + the `EVTSA9VEHNZVH`
distribution SourceArn (`firm-bucket-cross-ref.tf`).

### §3.2 → Phase-1 routing recommendation

**GO.** Recommended approach — **explicit `FIRM_CONFIG` entry**:

1. Add `'demo': { bucket: 'opal-data-demo', displayName: '<fake firm>' }` to
   `FIRM_CONFIG` in `_shared/firm-config.mjs` — one line, single source for both
   edge functions. Prefer this over the unmapped-fallback (explicit > implicit).
2. Flip the CI sentinel `shared-advisor-router/test/firm-routing.spec.mjs` in the
   **same commit** (deploy gate enforces this).
3. Rebuild + redeploy **both** Lambda@Edge functions.
4. **HARD requirement:** the `opal-data-demo` bucket policy must grant CloudFront
   OAI principal `E139998VWH0PD` + the `EVTSA9VEHNZVH` distribution SourceArn
   (per-bucket, no wildcard). Without it: HTTP 403 on every demo static fetch.
5. Follow `ADVI_FIRMSEP_ONBOARDING_PLAYBOOK`; `ADVI_FIRMSEP.10` (Cottonwood
   onboarding) is the working template.

**Architectural note for the PRD:** runtime origin-mutation is the *universal*
partner-routing mechanism (49financial, inflection, mockadv all use it) — it is
not inflection-specific debt. (COO~C has flagged this to CTO re: PRD ruling R3.)

---

## 2. Live platinum manifest (refreshes proposal §2.2)

`s3://opal-data-bd/platinum/` — **22,253 objects, ~4.70 GB** (probe-time count).

| Scope | Prefix | Pattern | Count |
|---|---|---|---|
| Firm | `platinum/firm/` | 14 `*.json` | 14 |
| Firm (namespaced) | `platinum/49financial/` | `ownership_map.json` | 1 |
| Advisor | `platinum/advisors/{name-slug}/` | 6 files × 168 | ~1,008 |
| Client | `platinum/clients/{z-id}/` | 5 files × 2,962 | ~14,810 |
| Account | `platinum/accounts/{z-id}/` | 1 file × 6,548 | ~6,548 |

- **Firm files (14):** `dashboard`, `mix_summary`, `fee_efficiency`,
  `header_metrics`, `clients-tab-slim`, `leaderboard`, `leaderboard.prior_week`,
  `employee_leaderboard`, `timeseries_overview`, `timeseries_chart` (35 MB),
  `cumulative_chart` (4.5 MB), `partner_analytics_{quarterly,monthly,annual}`
  (~4.6 MB each).
- **Advisor files (6):** `summary`, `timeseries` (~780 KB), `mix`, `nna_clients`,
  `positions`, `exec_summary`. (No `book.json` at the platinum tier — the
  `/advisors/{id}/book` route is Lambda-served from gold.)
- **Client files (5):** `summary`, `concentration`, `mix_timeseries`,
  `composition`, `views`.
- **Account files (1):** `summary`.

---

## 3. PII field inventory — independent walk, reconciled vs ADVI_ANONYM

**ADVI_ANONYM map** (from `pseudonymizer.py._transform_field`): the field keys it
treats as PII — `relationship_name`, `client_name`, `label` (client-context),
`book_name`, `account_id`, `relationship_id`, `client_key`, `key`
(client-context), `city`, `state`.

> **The pseudonymizer is RETIRED.** `needs_pseudonymization()` returns `False`
> (Andrew, 2026-04-15) — the map is a *field-classification reference only*; no
> serve-time masking runs. Real 49F PII is served cleartext, gated solely by
> firm-scoped authorization. **Consequence for DEMOV1: there is no serve-time
> safety net — the demo bucket must be 100% fake at rest.**

### Reconciliation table

| Field / locus | Scope | Sample value | vs ANONYM |
|---|---|---|---|
| `client_name` | advisor.summary, client.summary | `Jones, Pamela` | **MATCH** |
| `client_key` | advisor.summary `book/clients[]` | `z08324782` | **MATCH** |
| `relationship_id` | client.summary, composition `scope` | `z08103151` | **MATCH** |
| `account_id` | client.summary, account.summary | `z0812152081` | **MATCH** |
| `book_name` | advisor.summary `book` | `Abby Horton` | **MATCH** |
| `label`/`key` (client-context) | partner_analytics `…/segments[]/clients[]` | `Chan, William & Shelley` / `z08327149` | **MATCH** |
| `firm_id` | nearly every file | `49financial` | **DEMOV1-ONLY** |
| `firm_name` | partner_analytics_* | `49 Financial` | **DEMOV1-ONLY** |
| `advisor_id` | leaderboard, ownership_map, exec_summary | `erick_webb` (slug) **and** `Patrick Mundlin` (display name) | **DEMOV1-ONLY** |
| `name` | leaderboard `entries[]` | `Erick Webb` | **DEMOV1-ONLY** |
| `display_name` | client.summary `team_attribution[]`, advisor.nna_clients `clients[]` | `Patrick Mundlin`, `Wolfram, Charles & Wolfram, Kimberly` | **DEMOV1-ONLY** |
| `rel_id` | advisor.nna_clients `clients[]` | `z08377380` | **DEMOV1-ONLY** (naming variant of `relationship_id`) |
| `adv_drill` **object keys** + `categories[]` **list-strings** | cumulative_chart | key `Travis Penfield`; `"Chan, William & Shelley (z08327149)"` | **DEMOV1-ONLY** — ANONYM's `_walk` transforms neither object keys nor bare list-strings |
| **S3 key slugs** | `advisors/{slug}/`, `clients/{z-id}/`, `accounts/{z-id}/` | `abby_horton` | **DEMOV1-ONLY** — ANONYM is a serve-time *response-body* transformer; never touches keys |
| free-text narrative | advisor.exec_summary | LLM-generated (`model: claude-sonnet-4-6`) | **DEMOV1-ONLY** — may name clients/advisors in prose; needs substring replacement, not keyed-field replacement |

### Critical transform-design finding — context-dependent fields

`label` / `key` / `display_label` are **NOT universally PII**:

- In `concentration/items[]`, `top_holdings[]`, `mix[]` → they carry **tickers**
  (`QQQ`, `IEFA`) and asset-class labels (`Equities`) — **SAFE, keep verbatim**
  (public securities; keeping them is what makes the demo realistic).
- In `partner_analytics …/segments[]` → advisor names; in `…/clients[]` and
  `cumulative_chart.adv_drill` → client names — **PII**.

A blind key-name pseudonymizer (the ANONYM model) is **wrong** here — it would
either corrupt tickers or miss the list-string client names. **The DEMOV1
transform must be JSON-path-context-aware, not field-name-driven.** This is the
§6 belt-and-suspenders caveat made concrete and is the highest-risk item for the
Phase-2 engine.

### Clean (no PII): `clients-tab-slim.json` (firm_id + timestamps only).

---

## 4. Dynamic-serving topology + platinum-only question

- **`opal-partners-data` is the sole dynamic server** — all
  `/api/scoped/advisor-intelligence/*` and `/api/scoped/partners/books/*` API
  Gateway routes target it; it resolves the firm bucket from DynamoDB
  `opal-users-v2` (`FIRM#{id}/META.s3Bucket`). `comp-blast` returns no downstream
  consumers (it is a serving leaf).
- **The portal is NOT strictly platinum-only.** `handle_client_detail` (the L3
  `/clients/{id}/detail` route, used by `getClientDetail`) reads
  **`gold/entities/clients/{client_key}/detail.json`** — a `gold/` key — from the
  firm-resolved bucket. **DEMOV1 scope must therefore include
  `gold/entities/clients/{id}/detail.json`, not `platinum/**` alone** — OR DE
  confirms `getClientDetail` is fully superseded by `getPlatinumClientSummary`
  (`platinum/clients/{id}/summary.json`). **Open item for the PRD.**
- **Risk #6 as worded is moot:** the `bd-client-detail` Lambda
  (`INPUT_BUCKET=opal-data-bd` hardcoded) is a *pipeline-time generator* invoked
  by `bd-portal-advisor-publisher` — it is **not in the portal serving path**. The
  real platinum-only gap is the `gold/entities/clients/` read above.

---

## 5. Firm-specific code-branch audit (a new `demo` firm)

| Branch | Location | Demo trips it? | Action |
|---|---|---|---|
| `FIRM_ALLOWED_PATHS` per-firm allowlist | `portal/src/lib/firmAccess.ts` | **YES — fails closed.** Unknown firmId = deny-all; demo sees no pages. | **REQUIRED:** add a `'demo'` entry (mirror the `49financial` path set). Portal/DE. |
| `_partners/{firm}/` tenant layout dir | `portal/src/pages/AdvisorIntelligence/_partners/{49financial,inflection}/` resolved via `useTenantLayout` | **YES — likely.** Demo has no `_partners/demo/`. | **REQUIRED:** add `_partners/demo/` (mirror `49financial/`) or a `useTenantLayout` default. Portal/DE. |
| `firmOverride === 'inflection'` → static adapter | `advisor-intelligence.ts:956` | No — demo falls to the Lambda path (like 49financial). Correct. | None |
| `firmId === 'opal-capital'` (internal) | `AuthContext.tsx`, `firmAccess.ts`, `permissionGroups.ts` | No — demo is an external partner firm. Correct. | None |
| `firm_id == 'inflection'` observability sentinels | `opal-partners-data` `:1810/1818` | No — `_assert_inflection_envelope` is inflection-gated. Correct. | None |
| `pseudonymizeChildLabel(…, firmOverride === 'inflection')` | `DistributionTab.tsx` (×7) | No — portal-side pseudonym is inflection-only; demo mirrors 49F (none). Correct. | None |
| `ROUTER_FIRM_SUFFIX` (`49financial→bd`, `inflection→inf`) | `advisor-intelligence.ts:88` | Partial — demo not mapped; `bucketSuffix('demo')` falls through returning `'demo'`. | Benign (`?firm=demo` is opal-capital-only); add `'demo':'demo'` for cleanliness. |

**Net: 2 required portal changes** (`firmAccess.ts`, `_partners/demo/`), both
DE-owned. The remaining branches behave correctly because a `demo` partner firm
is structurally treated like `49financial`.

---

## 6. Demo-firm requirement checklist (feeds PRD phase plan)

| # | Requirement | Owner | Phase |
|---|---|---|---|
| 1 | `opal-data-demo` bucket + policy granting OAI `E139998VWH0PD` + dist `EVTSA9VEHNZVH` SourceArn | AE | 1 |
| 2 | `FIRM_CONFIG` `'demo'` entry in `_shared/firm-config.mjs` + CI-sentinel flip + redeploy both edge fns | AE | 1 |
| 3 | DynamoDB `opal-users-v2` `FIRM#demo/META` with `s3Bucket=opal-data-demo` (dynamic API path) | DS / auth | 3 |
| 4 | Demo Cognito user, `firmId=demo` / `allowedFirmIds=demo` | auth | 3 |
| 5 | `firmAccess.ts` `FIRM_ALLOWED_PATHS['demo']` entry | DE | 1/3 |
| 6 | `_partners/demo/` tenant-layout dir (or `useTenantLayout` default) | DE | 1/3 |
| 7 | Transform: clone `platinum/**` **and** `gold/entities/clients/{id}/detail.json` | DS | 2 |
| 8 | `opal-partners-data` IAM role: read on `opal-data-demo` | AE | 1 |

---

## 7. PRD risk-section inputs (Phase 0 deltas to the proposal)

1. **Pseudonymizer is retired** — proposal §3.1/§4 said the Lambda "applies PII
   pseudonymization." It does NOT (retired 2026-04-15). No serve-time net — the
   demo bucket must be fully fake at rest. Requirement-5 (own-firm exemption) is
   moot.
2. **Not platinum-only** — the L3 client-detail route reads
   `gold/entities/clients/{id}/detail.json`. Transform scope widens (§6 #7).
3. **Context-dependent `label`/`key`** — the transform must be JSON-path-aware,
   not field-name-driven (§3). Highest Phase-2 risk.
4. **`adv_drill` object-keys + list-string client names** — a PII class the
   ANONYM serve-time model structurally cannot reach. Each is a real leak vector.
5. **Free-text exec_summary narrative** — needs substring replacement; keyed-field
   mapping alone misses it.
6. **2 required portal changes** — `firmAccess.ts` + `_partners/demo/` (DE).
7. **Origin-mutation is universal**, not inf-specific — bears on PRD R3 (COO~C
   already flagged to CTO).

---

## 8. Compiler Tools

| Tool | Result |
|---|---|
| `comp-routes trace getPlatinumFirmDashboard` | Resolved the static path: CF behavior `/api/scoped/advisor-intelligence/*.json` → S3 origin `S3-opal-data-bd`, edge JWT YES, API GW no, Router `shared-advisor-router`. This named the linchpin component and drove §1. |
| `comp-blast opal-partners-data` (Phase 1 baseline) | `No downstream consumers found` — serving leaf. |
| `comp-pii audit` | 11 ADVI components scanned; ClientsTab 3 PII refs (modelled "hashed"), all others clean; "0 S3-direct PII (no server-side pseudonymizer)". **Divergence noted:** comp-pii is a portal-*component* model and reflects field-name classification, not runtime — it does not walk the S3 platinum tree and its "hashed" label is stale vs the retired pseudonymizer. Used as one input only; §3 is the independent file-tree walk per the TO. |
| `comp-blast opal-partners-data` (Phase 3) | `No downstream consumers found` — **identical to baseline**; read-only probe confirmed, nothing mutated. |

---

## 9. Acceptance

All eight TO acceptance criteria addressed: §1 (AC2/AC3), §2 (AC7), §3 (AC4),
§4 (AC5), §5 (AC6), §8 (AC8); this brief committed to CLOUD satisfies AC1.
Phase 0 closes the linchpin and produces a definitive demo-firm requirement set.
**Recommend GO to Phase 1** on PRD ship + COO~C decomposition.
