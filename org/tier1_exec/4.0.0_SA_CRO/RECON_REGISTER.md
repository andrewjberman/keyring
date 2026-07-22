# Research Register — `4.0.0_SA_CRO` (Chief Research Officer)

**Owner:** `4.0.0_SA_CRO` — charter: [`README.md`](README.md)
**Mandate:** Andrew-direct 2026-07-22.
**Status of this file:** **APPEND-ONLY.** A closed engagement is never edited except to append a
`### Downstream` entry or a correction stamped with its own date + author. Corrections are appended, not
overwritten — a research record that silently changes is worth nothing as provenance.

**This is the authoritative index of everything the research function has produced**, regardless of which
directory an engagement's artifacts live in.

> **Serial provenance:** engagements before 2026-07-22 were produced under the predecessor lane
> `0.4.0_DS_ClientPlatform~Z` and their commits are authored that way permanently. They are owned and tagged
> here. See charter §7 — the mismatch is deliberate and must not be "fixed."

---

## Index

| Recon ID | Date | Target | Artifacts | Evidence basis | Produced under | Status |
|---|---|---|---|---|---|---|
| **RCN-0001** | 2026-07-21 | **Black Diamond** (SS&C/Advent) — Cottonwood Capital Advisors tenant | 3 (teardown, roadmap, build spec) | 8 HAR captures + 4 CSV exports | `0.4.0_DS_ClientPlatform~Z` | **DELIVERED** — downstream build HELD at CTO registration |
| **RCN-0002** | 2026-07-22 | **Orion Advisor Solutions** — Opal-accessible tenant | 2 (teardown, BD×Orion structural comparison) | 2 HARs (1 truncated) + public API docs + Eclipse OpenAPI | `4.0.0_SA_CRO` | **DELIVERED** |

---

## RCN-0001 — Black Diamond dashboard teardown → replacement roadmap → `fact_account_return` build spec

| Field | Value |
|---|---|
| **Target** | Black Diamond Wealth Platform (SS&C/Advent), `*.bdreporting.com` — Cottonwood Capital Advisors tenant |
| **Date** | 2026-07-21 |
| **Commissioned** | Andrew-direct research task |
| **Owner** | `4.0.0_SA_CRO` (produced under predecessor serial `0.4.0_DS_ClientPlatform~Z`) |
| **Design counterpart** | `2.0.0_SA_COO~A` (total-return design, independent, converged) |
| **Question asked** | What can we glean toward **replacing Black Diamond for our clients**? |

### Evidence basis + denominators

8 HAR captures recorded by Andrew walking ~every dashboard section on 2026-07-21, plus 4 CSV analytics
exports. **4,431 total requests · 1,136 BD-API calls · 229 unique BD endpoints · 56 captured pages ·
15 BD backend services.** Full response schemas captured for **52 core endpoints**.

**Denominators independently re-derived 2026-07-22** by re-running the preserved tooling against the original
corpus: 229 endpoints / 52 schemas reproduced exactly.

**Declared gap (honest, in-band):** 5 endpoint families were `[BODY-NOT-CAPTURED]` — classification tree,
benchmark library, security master, rebalancer models, billing-config. Capability for those is described from
endpoint + request payload + page context only; **no response schema was invented.** That gap maps exactly
onto the WS-B reference-data track, which is why B is flagged the moat.

### Artifacts (committed)

| Artifact | Path | Commit |
|---|---|---|
| HAR teardown (the intel) | `docs/research/bd_dashboard_teardown/BD_DASHBOARD_HAR_TEARDOWN_20260721.md` | `efdb4dbd8` |
| Replacement roadmap (the plan) | `docs/research/bd_dashboard_teardown/BD_REPLACEMENT_ROADMAP_20260721.md` | `efdb4dbd8` |
| `fact_account_return` build spec | `docs/research/bd_dashboard_teardown/FACT_ACCOUNT_RETURN_BUILD_SPEC_20260721.md` | `b3783b866` → `a6dfa0a7e` |

**Companion (NOT this agent's — `2.0.0_SA_COO~A`'s):**
`org/tier1_exec/2.0.0_SA_COO/deliverables/TOTAL_RETURN_PERFORMANCE_DESIGN_PROPOSAL_20260721.md`
@ `5f2a11a10` / `64ec7be10` / `bcdd557f8`. Its §9 folds this research; the CRO spec anchors on it.

### Uncommitted sources (PII-bearing — deliberately not in the repo)

| Item | Location | Note |
|---|---|---|
| Raw HAR capture set | `~/Downloads/bd-cot-har-analysis.zip` (38 MB) | Verified present 2026-07-22 |
| Endpoint catalog / schemas / per-HAR inventory | scratchpad `b9280fcf-081b-4f11-945a-960de6fc0f03/scratchpad/analysis/` | **Ephemeral — reapable by `/kill storage`.** `endpoint_catalog.json`, `catalog_by_host.txt`, `files_summary.json`, `schemas.txt` are regenerable from the zip via the preserved tooling (**re-run and confirmed 2026-07-22**). |
| Profiler tooling | **PRESERVED** → `org/tier1_exec/4.0.0_SA_CRO/scripts/` | `profile_har.py`, `extract_schemas.py` — re-run 2026-07-22 against the original 8-HAR corpus, reproducing the published denominators (229 endpoints / 52 schemas) and **218 output files byte-identical** to the original run. |
| **GAP — `schemas2.txt` / `schemas3.txt` producers NOT preserved** | scratchpad only: `extract2.py`, `final_extract.py`, `render_catalog.py` | **NOT in the repo, NOT regenerable once the scratchpad is reaped.** Exploratory second/third schema passes; preserving them was deliberately deferred (each needs the same ruff-normalization + behavioral-diff cycle the two canonical scripts got, and none was worth blocking on). `schemas.txt` — the 52 core schemas the teardown cites — IS fully covered. If a future engagement needs the extra passes, rebuild rather than trust a stale copy. |

### Findings that carried

1. **BD is ~15 separable microservices behind a gateway**, not a monolith — so the performance-reporting
   surface can be replaced without touching CRM, rebalancer, or the client portal. Replacement need not be
   all-or-nothing.
2. **The analytics engine is reproducible from custodian data we already hold.**
   `portfolioreporting/api/performance/performancePeriod` returns TWR **and** MWR, net-of-fee, accrued MV,
   benchmark-relative, with return-contribution attribution and a performing-vs-position-only split, at
   Portfolio→Class→Segment→Account grain — all computed from positions + transactions + lots + fees, which
   live in Opal's Schwab silver.
3. **BD hands us its own method contract, verbatim.** `request/api/firm/globalsettings`:
   `NetOfFees / Accrued / Account365 / ClassSpecific / QuarterToDate / FIFO`. This is the `dim_return_method`
   contract, already written down by the incumbent.
4. **BD's transaction "affect vector"** (`externalFlow / incomeAffect / cashAffect / unitAffect /
   advisorFeeAffect / accrualAffect`, with `fileCode` encoding a signed tuple) **is the exact cash-flow
   taxonomy COO~A had reconstructed by hand** from Schwab `sb_cd` descriptions — independent convergence,
   and a ready-made parity oracle.
5. **The moat is not the math.** It is BD's proprietary classification tree (SuperClass→Class→Segment) +
   benchmark library, and the Rebalancer. Analytics — the thing clients actually look at — is the *easy,
   high-value* win. Replace in that order.

### Downstream

- **`fact_account_return`** — the convergence CTO named *"four names, one fact"*: BD-replacement Phase-1
  Tier-A == COO~A's total-return proposal == the 49F-runner "fields not scripts" field-emit ==
  OPAL_CONSOLIDATION serve. One fact, one owner, so the four threads cannot fork.
- **Method pinned to `Account365`** per Andrew's defensibility steer (2026-07-21 ~0048Z): *"I like the BD
  approach because its defensible to refer to."* Established the standing **METHOD-vs-NUMBERS split** now in
  the charter doctrine (README §2.5).
- **HELD:** the build + serve, pending CTO program registration (D6) + ratification of final grain/columns,
  post-MDPF-flip. **Open at Andrew:** D1 (Account365 confirm), D2 (classification build-vs-license).
- **State as of 2026-07-22 ~10:3xZ:** nothing has moved on these files since `a6dfa0a7e` (07-21 20:54Z); no
  project JSON registered under any BDX/total-return code.

---

<!-- APPEND NEW ENGAGEMENTS BELOW. Add an Index row above. Never edit a closed entry in place. -->

---

## RCN-0002 — Orion Advisor Solutions teardown + the Black Diamond × Orion structural comparison

| Field | Value |
|---|---|
| **Target** | Orion Advisor Solutions — `api.cloud.orionadvisor.com` (main/Connect API) + `api.orioneclipse.com` (Eclipse, trading/OMS) |
| **Date** | 2026-07-22 |
| **Commissioned** | Andrew-direct: *"analyze these in conjunction with the Swagger doc just like you did for Black Diamond and enumerate your findings... we want to understand the similarities in structure of these platforms... so we can build it ourself."* |
| **Owner** | `4.0.0_SA_CRO` |
| **Egress** | Standing session vendor-egress granted by Andrew. **NOT USED** — no Orion API call was made. HARs were operator-supplied; documentation was read as public pages. |

### Evidence basis + denominators

**HAR side — 2 captures, one damaged.** `orionpt1.har` is **TRUNCATED** (export cut mid-write; fails 48.2% in
on an unterminated string; file ends in raw CSS and never closes its JSON) — **63 entries salvaged, true total
UNKNOWABLE**. `orionpt2.har` intact: **716 entries**. Combined **779 entries → 402 `orionadvisor.com` requests
→ 307 genuine API calls** (95 excluded as `OPTIONS` preflights + non-JSON assets — reconciled exactly, not
hand-waved) → **150 unique endpoints**, **80.5% carrying a usable response body**.

**DOCS side** — 38 URLs attempted, 31 resolved, 5×404, 2×401, 1 login-gated **and not authenticated**. Eclipse
**OpenAPI 3.0.3** read directly from the live spec object: **493 paths / 582 operations / 56 tags**.

**Coverage honesty:** app routes were recovered from Orion's **own telemetry endpoint**
(`Utility/Logging/PageView/{route}`) after the truncation cost the page titles — **36 routes, of which 20 are
`billing/audit/*` and 11 `reports/*`.** This is a **billing-and-reporting walk, not a performance walk**: the
`Performance` domain appears once, with two calls, returning `[]`. HAR is authoritative for the fee engine and
report builder; **docs are the primary source for the performance engine**, and the teardown labels every
section `[HAR]` / `[DOCS]` / `[HAR+DOCS]`. Two endpoints returned **empty arrays** — capability present, no
tenant data, **response shapes deliberately not modelled**.

### Artifacts

| Artifact | Path |
|---|---|
| Orion platform teardown | `docs/research/competitive_recon/orion_20260722/ORION_TEARDOWN_20260722.md` |
| BD × Orion structural comparison | `docs/research/competitive_recon/orion_20260722/PLATFORM_STRUCTURE_COMPARISON_20260722.md` |

*(First engagement to use the go-forward `docs/research/competitive_recon/<target>_<date>/` home.)*

### Uncommitted sources (PII-bearing — deliberately not in the repo)

Raw HARs at `~/Downloads/orionpt{1,2}.har` (143 MB). Salvage + catalog + 67 extracted schemas in session
scratchpad — **ephemeral, reapable by `/kill storage`**. The capture contains real client names, account
numbers and an operator email; **all scrubbed from committed artifacts.**
**Tooling:** `profile_har.py` retargeted (host regex + noise list) — the only target-specific knob, as its
README predicted. `extract_schemas.py`'s `HV` allowlist was **rewritten from the catalog**, per the documented
workflow (run the profiler first, read the catalog, then build `HV` — never guess it up front).

### Findings that carried

1. **Orion is ONE versioned REST API behind ONE host** (`/api/v1/{Domain}/...`) — the architectural opposite
   of BD's ~15 domain backends behind a gateway.
2. **There are TWO Orion APIs**: main/Connect (accounting, reporting, performance, billing) and **Eclipse**
   (trading/OMS, 493 paths, public OpenAPI). Both vendors keep the OMS out of the reporting platform.
3. **Performance is a recursive CALCULATION GRAPH, not a resource** — one `POST /Reporting/Scope`, 36 entity
   types, 18 calculation types, methodology at request time. No `/performance/accounts/{id}` exists.
4. **THE KEY MECHANISM: the tenant SETTINGS and the API's request-time `performanceOption` are the same
   switchboard** — 10 of 11 documented parameters have an exact settings twin, discovered independently from
   two evidence layers. Settings are the persisted defaults; the POST overrides per call.
5. **The method contract is firm-level AND account-level** (32 + 5 options), incl. per-account `Include In
   TWR`. **BD's `firm/globalsettings` was firm-only** — Orion's model is strictly richer.
6. **`1:69ANNUAL` (Days-with-value-only vs All-days-within-range) is the exact `c01` defect class we found in
   our own runner — and Orion solved it by naming it a ratified setting rather than picking a constant.**
7. Orion carries analytics BD did not expose: **Brinson attribution**, a full risk-stat suite (Sharpe/Sortino/
   Treynor/Jensen's Alpha/R²/Beta/capture ratios/drawdown), **after-tax performance + tax alpha**, direct
   indexing, stress tests, a 157-field prospect engine.
8. **Settings are a generic typed key-value system** — a new firm-configurable behaviour is a data insert, not
   a release.
9. **The capture resolves a documentation gap the docs pass could not:** `api.cloud.orionadvisor.com` appears
   in no Orion documentation, and the docs-only evidence could not tell whether it was the documented API.
   The HAR proves it serves `/api/v1/Reporting/Scope`, `/Portfolio/*`, `/Billing/*` — **same API, different
   hostname.**

### Downstream

- **Nothing in RCN-0002 overturns the RCN-0001 roadmap.** It **CONFIRMS** on a second independent vendor:
  `dim_return_method` as a first-class contract · TWR net-of-fee default · accrued MV incl. cash · flows
  excluded · classification+benchmarks as the moat · rebalancer out of Wave 1 · windows derive from a daily
  grain.
- **SHARPENED (3):** `dim_return_method` needs more rows **and a scope column** (firm default + per-account
  override); `dim_benchmark` must carry a **rebalance rule**, not just weights; classification should be
  **axes, not a single tree**.
- **NEW, needs a decision:** **Brinson attribution** (allocation vs selection effect) is absent from RCN-0001's
  spec and is a different, arguably more valuable question than contribution-to-parent — **proposal only,
  requires CTO scoping.** **After-tax / tax-alpha** intersects OPAL_TAXSMA and should be scoped with that
  program rather than invented separately.
- **Unchanged:** `fact_account_return` remains **HELD at CTO's D6 registration**, post-MDPF-flip. This
  engagement dispatched nothing and registered no project.

### Declared gaps

`orionpt1.har` truncation (unknown fraction of the walk lost) · performance surface barely exercised in the
capture, so §4 of the teardown is **docs-grade, not HAR-grade** · no public OpenAPI for the **main** Orion API
(`/api/help`, `/swagger/v1/swagger.json` 404; `/api/index.html` login-gated and **not authenticated**) — the
endpoint list is **a floor, not a census** · `performance-breakdown` output shape undefined in every retrieved
page · Eclipse **v2** proven to exist but no spec retrieved · Eclipse `components.schemas` empty (0) · no
published rate limits · Orion's transaction-level flow classification `[UNOBSERVED]` (BD's affect vector
remains our reference taxonomy) · **`[UNOBSERVED]` in the BD column is not absence** — the BD capture simply
did not exercise risk-stats or after-tax screens, and BD is **not** scored as lacking them.
