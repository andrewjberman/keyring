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
| **RCN-0003** | 2026-07-23 | **arxiv.org** — CS paper harvest surface (NFRA_AKPIPE) | 1 (teardown + build spec) | 3 HARs (2 md5-identical) + 1 sample paper; HTML bodies [BODY-NOT-CAPTURED] | `4.0.0_SA_CRO` | **DELIVERED** — build HELD at CTO program registration |
| **RCN-0004** | 2026-08-03 | **The Opal repo itself** — Repo Coherence Graph (NFRA_REPOCOHERENCEGRAPH): knowledge-plane debt cleanout spec | 1 (implementation PRD) + project registration | Andrew's RCG proposal docx (326 paras) + the NFRA_VELOCITY record (program, 2 PRDs, type dictionary, constitution, contracts folder, 3 CVO logs) + repo census (25,273 tracked files) + 4 Andrew design rounds | `4.0.0_SA_CRO` | **DELIVERED** — spec staged for Andrew review; build HELD at CTO arch-gate + COO decomposition |
| **RCN-0005** | 2026-08-05 | **Opal MDPF portfolio ontology** -- five-category taxonomy, Model lifecycle, Client Mandates, Sleeves, selection/advisory axes, and fee basis | 2 (research/design specification + visual ontology diagram) | MDPF_GLOBAL PRD + Andrew recording + MDPF_3FIRMS PRD + live crosswalk source + Andrew/Yang direction + 5 Andrew/CRO design rounds + exact-contract repo scan across 5 roots | 4.0.0_SA_CRO | **RATIFIED** -- Andrew-direct 2026-08-06 (CRO terminal), VERBATIM: *"it is already ratified i worked on that"* -- superseding the STAGED-FOR-REVIEW state this row carried; he worked the spec himself. Still no build/serve mutation from this row -- build authorization flows through CTO/COO as ever |
| **RCN-0006** | 2026-08-07 | **The Opal ontology itself** — a proposed "Script I/O" (S-layer) for line-level field flow, Python + React/JS | 5 (spec REV1-3, axis field test, disposition, Python feasibility, **`LAYER_FIELD_ANATOMY.md`**) | live `comp-kuzu` graph (20,585 nodes / 41,144 edges @2026-08-07T00:32Z, HEAD current) + 8 first-party extractor surfaces read at source + 2 hand-classified code samples + an exercised SDK run (CVO~C) + 4 non-held-out tree censuses | `4.0.0_SA_CRO` | **DELIVERED — CONCLUSION IS A NEGATIVE.** The S-layer is **DISSOLVED**: all 7 specified capabilities already exist on live D1 edges. Real gap = D1 field grain has **no Python producer**. Build LEFT the CRO lane → CTO~D PRD |
| **RCN-0007** | 2026-09-03 | **`.tools/comp-read` itself** — instrument misattachment: four measured instances in one exchange where the tool was correct and the answer was attached to a different question | 1 (brief) | 9 comp-read calls across 2 modes over 3 files at stated vintages (`.tools/deploy_ledger.py` @`79c0e68071` clean, `.tools/comp-read` 1250 ln, `INVESTIGATION_v1.md`) + 3-seat round trip (`0.0.0_AB_MSTR~Z`, `3.0.0_SA_CVO~Z`) | `4.0.0_SA_CRO~Z` | **DELIVERED — PROPOSALS ONLY, none dispatched.** 5 changes proposed, suggested owner the CVO lane (authorship-measured). P5 marked UNTESTED for feasibility; P3's contrast is n=2 and no threshold is proposed |
| **RCN-0008** | 2026-09-09 | **Investor Reporting & Data Unification** — Andrew's proposal docx → the L1 BRIEF for the D14 directive (wraps D1/D2/D3; the client workflow leaves Advisor Intelligence) | 3 (brief, citable source text, Andrew-direct record) | Andrew's proposal (80,251 B docx, sha256 `db4168a6…f0e8`, 450 blocks extracted) + directives board (13 live) + registry (355 JSONs / 48 open / 86 open TOs) + 6 PRD §1–§2 reads + 5 comp-find censuses over 152,3xx files + `comp-trigger --list` (142 rules + 19 schedules) + `comp-schedule` (26 gates) + 1 `comp-read` | `4.0.0_SA_CRO` | **DELIVERED at L1** — consumer `1.0.0_SA_CTO` `/endpoint --forward`. Nothing dispatched, no register row written (D14 is MSTR's cell). ADVI_PERFRP read to its header only (standing 08-24 restriction names this seat; surfaced, not adjudicated) |
| **RCN-0011** | 2026-09-19 | **`_authz` LAYER design fork** (IRPT) -- answered empirically for `1.0.0_SA_CTO`: no layer for fork prevention | 1 (`deliverables/RCN-0011_AUTHZ_LAYER_FORK_RESEARCH_20260919.md` + addendum) | `holdings/lambda.tf` read; 7 routes | `4.0.0_SA_CRO` (base, CLOUD fabric) | **DELIVERED** -- POINTER ROW ONLY, added 2026-09-22 by `4.0.0_SA_CRO~F` after an id collision; the section is the base seat's to write |
| **RCN-0012** | 2026-09-22 | **Claude for Financial Services** -- Anthropic's open-source FSI plugin marketplace + the LLY pack Yang built with it, and how its channels thread into AMGT_RESAPP | 2 briefs + 1 evidence folder (endpoint discovery card + JSON) | repo @574ed36 (19 entries, 5 `.mcp.json`, 3 SKILL.md); LLY pack 58 files (README/SOURCES in full, 3 xlsx, 2 docx); 12 of 12 MCP servers probed unauthenticated; 9 public doc pages; CTO~W card 1 | `4.0.0_SA_CRO~F` | **DELIVERED as CTO intake -- PROPOSAL ONLY, nothing dispatched.** Plugin = files not access (12 OAuth-gated vendor servers); LLY pack built from PUBLIC sources; core `.mcp.json` malformed at that vintage; 4 open calls at Andrew |
| **RCN-0014** | 2026-09-23 | **`opal_ai`** -- the Opal Analyst as a microproduct: one agent + one indexed MCP in three slices (Opal -> Template -> Clients), tying Opal Analyst, D6 GraphQL, NFRA_OPLGTW, NFRA_MCPINDEX, the vendor-access paths and The Walk into one repo | 1 L1 brief (`docs/briefs/opal-ai-microproduct-repo-brief-20260923.md`) | repo reads only @`1b1244cecf`: 3 PRDs + 2 briefs + the 09-22 assessment; gateway code layout; the BG seat's prompt/refs/fence; 3 vendor designs-of-record + 2 standards; RCN-0001/0002 tooling; comp-which + its harness; RCN-0012 | `4.0.0_SA_CRO~X` | **DELIVERED as CTO intake -- nothing dispatched.** 12 outcomes, candidate thread = one Teams question answered through the MCP; 8 calls at Andrew (one repo vs the 09-22 `opal_analyst` naming; slice-first layout; the monitor conflict in the Third-Party Standard) |
| **RCN-0015** | 2026-09-23 | **The GitOps split of `opal_ai` from `ajb_workspace`** -- portal-shaped (contained, separate, tooled), and what the portal's current wiring does and does not give a nested repo | 1 L1 brief (`docs/briefs/opal-ai-gitops-split-brief-20260923.md`) | local git + repo reads @`bd282e03e9`: `.gitmodules`, gitlinks, portal hooks/CI/branches, the owned-paths hook, safe-commit/safe-merge, wk-provision, both EC2 deploy scripts + manifest, the gateway's parent reaches, the launcher and parent `.claude` | `4.0.0_SA_CRO~X` | **DELIVERED as CTO intake -- nothing dispatched.** The portal is a nested clone + gitlink, not a submodule; its commits skip every parent git gate; installing the lane hook there without a lane file would block every commit (fail-closed by default -- CORRECTED from "fails open", msg 25107); both deploy guards read the parent; 24 work items, 8 calls |
| **RCN-0016** | 2026-09-24 | **The fabric's own process architecture** -- where verification and process management (bureaucracy) slow progress; whether RAVC still earns its keep; holes, contradictions, keep / refine / cut, implementation and upkeep (Andrew's "report 3") | 1 brief (`docs/briefs/process-architecture-verification-bureaucracy-brief-20260924.md`) + Andrew-direct record + re-runnable census (`scripts/process_census/`) | 33,482 non-merge CLOUD commits Jun 1 - Sep 24 classified by path; 181 portal commits; 1,053 cells; `org/mcp/broker.db` read-only (4,170 msgs since 09-14) + archive (89,885); rail, lane and override audit logs; 237 surprise-channel files, 1,447 dispositions; law-file size history | `4.0.0_SA_CRO~B` | **DELIVERED as a brief -- proposals only, nothing dispatched, no law, gate or skill edited.** Product-touching commits fell from 16-25% (June) to 6-9% (Sep); the spine re-measures one fact 3-4 times; L4-R and the row-disposition precondition carry most of the churn; RAVC's core is sound but its document is stale; fix = a `<risk>` class the gates read, not a rule to read |
| **RCN-0017** | 2026-09-24 | **The canonical flow and the closer flow** -- where canonical still spends its time, how heavy the task orders are, which model the workers should run, a FAST closer mode, `/closer-drive`, and a mode lease to switch between them (Andrew's "report 2"; RCN-0016 is `4.0.0_SA_CRO~B`'s report 3) | 1 brief (`deliverables/REPORT2_CANONICAL_AND_CLOSER_FLOWS_SPEED_MODE_AND_SWITCH_20260924.md`) + Andrew-direct record | 12 h window 02:40Z-14:40Z: 29 task orders / 4 issuances / 2 projects (DSGN_IRPTV1 r1-2, AMGT_RESAPP r37-38) on all refs; 68 worker commits (trailers); 602 workspace + 90 portal commits by seat; `org/mcp/broker.db` read-only (714 msgs); seat logs and surprise rows at the bytes | `4.0.0_SA_CRO~A` | **DELIVERED as CTO intake -- proposals only, nothing dispatched.** Canonical is slow in execution, not hand-offs; orders median ~220 product lines inside an 11.8 KB wrapper, 31% hit a check defect mid-round; workers already run Sonnet 5 high; nine changes C1-C9 and six calls at Andrew |

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
- **DOWNSTREAM (2026-07-22 ~22:5xZ) — Cottonwood daily-model backfill mechanism sweep.** Andrew-direct extension
  of the RCN-0001 BD-surface analysis: a full-estate hunt for a dated per-model allocation backfill mechanism.
  Result: exactly one live path (a past-window run of DataMining `qt5 allocations`, whose account-strategy
  dimension is already selected — no re-persist); every other surface measured-dead (rebalancer date-injection,
  sessions/blotter empty for cot) or lower-odds-unprobed (Surface-B account/audit/timeline). Carries the full
  temporal-vs-current verdict (CTO v1.21) with an explicit window-integrity control; HELD on a fresh cot-BD
  session. Brief: `briefs/COTTONWOOD_BACKFILL_MECHANISM_CAMPAIGN_20260722.md`; ready-to-fire harness:
  `scripts/cot_qt5_temporal_probe.py`. Companion build (the forward series this would backfill into): the
  daily-snapshot append spec, accepted as build TO 3F-G8b.

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

### Downstream append — 2026-08-11, RECON-6 (`4.0.0_SA_CRO` base) — endpoint-inventory delta for goal 2b

**Commission:** `ANDREW_DIRECT_20260811_COLLECTIVE_ATOMDECOMP_RECON_FOR_Q3Q4_GOALS.md` #6 — "Eclipse endpoint
coverage + a 'every single endpoint (documented)' completeness check against RCN-0001+RCN-0002." First pass;
bounded, read-only, no vendor credentials used throughout (public documentation pages only, same class as the
original RCN-0002 engagement's "documentation was read as public pages, not egress").

**Method note (in-band, not a silent choice):** confirmed `api.orioneclipse.com/doc/` reachable and live
(V1 title, no `v2` link surfaced on the landing page itself), then attempted one plausible raw-spec path
(`/doc/swagger.json`) to re-derive the full 493-path/56-tag census beyond RCN-0002's top-5-tag summary — it
returned **401 Unauthorized**. **I deliberately did not continue guessing further candidate paths against the
live vendor host** — one known-public page read is documentation-reading (RCN-0002's precedent); iterating
undocumented paths against a vendor's production API starts to read as probing, which sits closer to the
vendor-egress boundary (README §3) than this delta census needs to cross without a fresh per-use word. **This
is a self-imposed stop, not a vendor-side finding** — the 401 on one guessed path says nothing about whether
the actual spec URL used in RCN-0002 (never recorded verbatim — a preservation gap, noted below) is still live.

**Findings:**
1. **Eclipse doc portal CONFIRMED STILL LIVE, unauthenticated, 2026-08-11** (`api.orioneclipse.com/doc/`,
   title "Orion Eclipse API V1") — the RCN-0002 basis has not gone dark.
2. **Orion main/Connect API developer portal CONFIRMED STILL LOGIN-GATED** (`developers.orionadvisor.com`) —
   RCN-0002's declared gap ("no public OpenAPI for the main API") re-verified, not stale, 20 days later.
3. **BD/Advent has NO public API reference to reconcile RCN-0001's 229-endpoint HAR census against.** Public
   material is marketing-only ("accessible developer platform," no endpoint list). One candidate third-party
   source (`supergood.ai/docs/ss-c-advent-api`) fetched and **DISCARDED as evidence** — it explicitly
   self-labels "an independent design exercise... nothing on this page describes an existing SS&C Advent
   product," 6 hypothetical endpoints, not real. **Conclusion: RCN-0001's 229 remains the estate's only
   denominator for BD; there is no independent total to complete the census against.** This closes half of the
   "completeness check" ask with a real (negative) answer rather than leaving it silently open.

**Still open (named, not absorbed):**
- The exact URL/method RCN-0002 used to retrieve Eclipse's "live spec object" was **never recorded verbatim**
  in the committed teardown or preserved scripts (`scripts/` has no Eclipse-specific fetcher) — a minor
  provenance gap; closing it would let a future pass re-derive the full 493-path census without re-guessing.
- **Eclipse's full 493-path / 56-tag breakdown remains at RCN-0002's original depth** (top-5 tags + 4 prefix
  groups only, ~234-434 of 493 accounted for depending on which grouping) — not completed this pass.
- **Eclipse v2**: still unconfirmed whether a retrievable spec exists; the `/doc/` landing page surfaced no
  v2 link on read.
- **Whether the original RCN-0002 Eclipse spec URL still resolves at all** is genuinely unknown — the one path
  I tried was a guess, not a re-run of the original method.

**Recommend, not ruled:** if a full Eclipse census is load-bearing for goal 2b's build (not just a nice-to-
have denominator), the clean next step is Andrew's per-use word to re-open the standing session vendor-egress
channel already granted for RCN-0002 (README §3 — availability is not authorization; this specific channel was
granted once for this specific target, not standing forever) and log in to `/doc/` directly rather than
continuing to guess unauthenticated raw-spec paths.

---

## RCN-0003 — arxiv.org CS-paper harvest surface teardown → NFRA_AKPIPE build spec

| Field | Value |
|---|---|
| **Target** | `arxiv.org` / `export.arxiv.org` — Computer Science paper listing, abstract, full-text (html/pdf/src), and search surfaces |
| **Date** | 2026-07-23 |
| **Commissioned** | Andrew-direct: register NFRA_AKPIPE — a daily arxiv scraper + contact-ID + ontology-relevance ranking pipeline |
| **Owner** | `4.0.0_SA_CRO` |
| **Egress** | **STANDING arxiv-scoped daily-egress grant, cloud-only** (Andrew-direct verbatim, spec §0): the daily pull runs as a Lambda in Opal's cloud writing to S3 — never an agent/CLI. NOT a blanket vendor lift. The inputs analyzed here (HARs + PDF) were operator-supplied — not egress. |

### Evidence basis + denominators

**3 HAR captures → 2 unique.** `arxiv.org.har` == `arxiv.org2.har` (md5 `663682cc51f0b016c6bb34ea7a7ba7be`, 223 entries). `arxiv.org3.har` distinct (md5 `8ed54cf8f7427bbc9adc02c6521f1a31`, 165 entries). **1 sample paper** `2606.07297v1` (SWE-Explore, cs.SE, 20 pp) — the stated high-relevance exemplar + scoring positive control.

**MARKED CAPTURE GAP (doctrine rule 2):** the HARs retained **ZERO HTML response bodies** — only PDF bytes (`bodies_present=1`/HAR, sole mime `application/pdf`; all 12/9 HTML documents empty). So the HARs ground the **surface topology** (endpoints, params, nav path, content-types, sizes) but **NOT** the HTML field-schema of `/abs`, `/list`, `/html`, `/search`. No DOM parse specified off an endpoint name; schema grounding comes from the official OAI-PMH/Atom API instead (the correct harvest backbone regardless).

### Artifacts

| Artifact | Path |
|---|---|
| Teardown + build spec (RCN-0003) | `org/tier1_exec/4.0.0_SA_CRO/briefs/NFRA_AKPIPE_BUILD_SPEC_20260723.md` |
| Project record | `org/projects/NFRA_AKPIPE.json` + REGISTRY row |
| HAR profiler (arxiv-adapted) + PDF extract | scratchpad `arxiv_har_profile.py`, `arxiv_har_docs.py`, `paper_2606.07297v1.txt` — **ephemeral, reapable by `/kill storage`**; the profiler is a light adaptation of `scripts/profile_har.py` (host filter + arxiv path-normalizer), regenerable from the spec |

### Findings that carried

1. **The harvest backbone is the official API, not the HTML pages.** OAI-PMH (`export.arxiv.org/oai2` `ListRecords` `from/until&set=cs`) is the exhaustive, lossless daily-delta mechanism (resumptionToken paginates; structured authors/dates/categories/abstract/doi). The 2.7 MB `/list/cs/new` HTML page is brittle by comparison; the Atom API is the keyword overlay.
2. **`/html/{id}` (LaTeX→HTML render) is the cheap clean full-text source**; `/src/{id}` tarball is the richest author/affiliation parse; `/pdf/{id}` is the fallback. HAR 3 proved all three exist.
3. **This is a content-class problem the estate already designed for.** NFRA_AKPIPE's NLP ranking CONVERGES with `infra/system/ontology/CONTENT_MODULE_DESIGN.md` (RRF over BM25/Potion, materialized substrate, deterministic-pinned, ablate-don't-fuse, decoy-null threshold) — the external/arxiv instance of that module, not a parallel stack. "Four names, one fact": CTO ratifies the convergence at registration.
4. **Contact-ID is feasible from body** — the sample carries the corresponding-author email inline; names/ids come structured from OAI metadata.
5. **Recency is submission-date decay, NOT trading-day T-1** — CONTENT_MODULE_DESIGN §9 carries this exact caution; importing the pipeline T-1 basis would false-alarm on old-and-correct preprints.

### Downstream

- **NFRA_AKPIPE registered** (`org/projects/NFRA_AKPIPE.json`, active, phase = spec-landed pre-build). Build/deploy **HELD at CTO program registration + arch-gate**; COO staffs the cloud + content/NLP lanes. CRO proposes owners, dispatches nothing.
- **Broadcast** to CTO + COO + MSTR 2026-07-23 ~19:16Z (the Andrew-direct decisions verbatim + the standing egress grant).
- **Dependency exercised:** the `.owned-paths` 4.0.0 project-registration grant (LD-0331, line 556 — org/projects/*.json + REGISTRY, scoped) — first use.

---

## RCN-0005 -- Opal MDPF Portfolio Ontology and Sleeve Attribution specification

| Field | Value |
|---|---|
| **Target** | The proposed MDPF_GLOBAL product taxonomy and the missing client-level portfolio-construction substrate |
| **Date** | 2026-08-05 |
| **Commissioned** | Andrew-direct CRO discussion, subsequently amended from Andrew/Yang working-session direction: establish Models, Strategy, Alternative, Client, and Insurance; Primary/Custom Model lifecycle; nullable advisory and fee inclusion states |
| **Owner** | `4.0.0_SA_CRO` |
| **Status** | Proposal staged for Andrew review; no project registration, build dispatch, deploy, or served-output change |

### Evidence basis + denominator

Read at source: `MDPF_GLOBAL_PRD.md`, its Andrew voice-recording transcript,
`MDPF_3FIRMS_PRD.md` A4/per-firm contract, the live MDPF model crosswalk, and the
`MDPF_GLOBAL` project record. Five Andrew/CRO design rounds, including Andrew/Yang working-session
direction, established the substantive definitions.
An exact-contract scan across five repo roots (`org`, `data`, `portal`, `infra`, `docs`) found
`segment_v1`/four-term contract identifiers only in the PRD and project/registry records, with zero
producer or served-schema implementation hits.

### Artifact

`org/tier1_exec/4.0.0_SA_CRO/briefs/MDPF_PORTFOLIO_ONTOLOGY_AND_SLEEVE_ATTRIBUTION_SPEC_20260805.md`

`org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_PORTFOLIO_ONTOLOGY_DIAGRAM_20260805.svg`

### Findings that carried

1. The successor mutually exclusive categories are Models, Strategy, Alternative, Client, and
   Insurance. SMA is not a category because every account in the population is inherently an SMA.
2. Models require an effective-dated `primary|custom` class. The five archetypal ETF Models are
   Primary; `fixed_income` is the initial Custom example; promotion preserves stable `model_id`.
3. Strategy drilldown is `divz|idvz|pfoe|muni|tax`; Strategy accounts are individual-security-focused
   and cannot contain Model references.
4. Alternative separates product identity from `private_equity|private_credit|hedge_fund|real_asset`;
   the initial example is `aqr` plus `hedge_fund`. Client and Insurance are unforked.
5. `selection_origin`, `advisory_scope`, and `fee_basis` remain independent axes. Advisory scope is
   `advised|excluded|null`; fee-basis status is `included|excluded|null`; null displays as Unknown.
6. Fee basis is governed by an effective-dated client/household Fee Arrangement, resolved through
   account/mandate applicability and optional sleeve overrides, then materialized at the leaf.
7. `non_model` becomes compatibility arithmetic, not business ontology.
8. The larger opportunity is an Opal Portfolio Blueprint backed by an effective-dated Sleeve
   Attribution Ledger.
9. The v0 `segment_v1` identifier is retired for the successor contract. The current target emits
   `schema_id = portfolio_classification_v1` and carries an explicit no-blind-cast migration map.

### Downstream

- Andrew review/ratification of the ontology and open decisions.
- If ratified, the owning exec lanes decide whether this becomes an MDPF_GLOBAL amendment or a sibling
  project; CTO gates architecture/serving and COO owns decomposition/staffing.
- The first proposed execution is representative-client discovery and source/authority census, not a
  global chart or subtraction formula.

---

## RCN-0004 — The Opal repo itself: Repo Coherence Graph implementation spec (NFRA_REPOCOHERENCEGRAPH)

| Field | Value |
|---|---|
| **Target** | The ajb_workspace repo (knowledge plane) — 25,273 tracked files at commissioning |
| **Date** | 2026-08-03 |
| **Commissioned** | Andrew-direct at the CRO terminal, four design rounds, culminating: *"please write a detailed spec that covers the final version of what we have designed here including an implementation schedule that feeds into and informs the NFRA_VELOCITY project"* |
| **Owner** | `4.0.0_SA_CRO` |
| **Source document** | `C:\Users\AndrewBerman\Downloads\Repository Coherence Graph Proposal.docx` (Andrew, 2026-08-03; 326 paragraphs extracted) |

### Evidence basis + denominators

The proposal docx (full extraction, scratchpad) · the NFRA_VELOCITY record read at source
(PROGRAM + CORE/ESTATE PRDs + TYPE_DICTIONARY + INTENT_DENOMINATOR_SYNCHRONIZATION + the
core_nfra_velocity contracts folder + CVO logs @e2218a106f @fa505d4cff @e661f608cc) · live repo
census (git ls-files, per-root counts printed in the PRD §0) · prior-art absence measured
("coherence graph"/"behavioral fingerprint"/"Repository Coherence" = 0 hits, 24,715 of 26,710
files scanned, comp-grep on-rails).

### Artifacts

| Artifact | Path |
|---|---|
| Implementation PRD (staged for CTO landing) | `org/tier1_exec/4.0.0_SA_CRO/briefs/NFRA_REPOCOHERENCEGRAPH_PRD_20260803.md` |
| Project record | `org/projects/NFRA_REPOCOHERENCEGRAPH.json` + REGISTRY row |

### Findings that carried

1. **The RCG proposal and NFRA_VELOCITY are the two halves of Andrew's own INTENT/FRICTION
   ruling arriving from opposite directions** — RCG is a friction/discovery instrument with no
   intent side; VELOCITY is an intent/adjudication system starved on discovery over the
   uncontracted complement. Composed, each covers the other's named gap.
2. **ACTIVE is a computation, RELEVANT is a judgment** — mark-and-sweep GC over a typed
   reference graph (with governance citations as first-class edges: prose is runtime in this
   org) computes ACTIVE exactly; ML is spent only on the RELEVANT margin, with Andrew's cohort
   ratifications as the only label source and the ratified active core as the semantic anchor.
3. **The 2x2's off-diagonals are where the risk lives:** ACTIVE+NOT-RELEVANT (load-bearing
   legacy — migrate, never archive) and NOT-ACTIVE+RELEVANT (doctrine/logs/rollback levers —
   the quadrant mechanical cleanup destroys). Only NOT-ACTIVE+NOT-RELEVANT is cleanup.
4. **RCG dispositions reuse VELOCITY's ratified `lifecycle_class`** — the spring cleaning IS the
   type system's first mass population; a parallel vocabulary would commit the forked-vocabulary
   class the VELOCITY record itself names as instrumentless.

### Downstream

- **NFRA_REPOCOHERENCEGRAPH registered** (active, P0 = spec staged, awaiting Andrew review + GO).
  Build HELD at CTO arch-gate + COO decomposition; CRO proposes owners, dispatches nothing.
- **NFRA_VELOCITY suspension (temporary, On-Hold + open-work ledger) triggers at RCG P0** —
  Andrew-direct; execution of the suspension record is CTO/COO's.
- **The VELOCITY granular redesign is explicitly downstream** of the RCG hand-off (Andrew: *"we
  will cover that after"*).

---

## RCN-0006 — Script I/O "S-layer" → **dissolved into an existing rail** → the C/D layer field anatomy

**Date:** 2026-08-07 · **Produced under:** `4.0.0_SA_CRO` · **Commissioned:** Andrew-direct 2026-08-06
**Team:** CRO driving · `3.0.0_SA_CVO~C` (review + the only exercised evidence) · `1.0.0_SA_CTO~D` (arch)

### The ask

Design a "script io" ontological layer — line-level inputs/outputs for field-level dependency and
flow, Python and React/JS — as the precursor to *project coherence*, of which `ATOM_DECOMP` is the
base. Mid-engagement correction (Andrew, VERBATIM): *"we probably need to enhance this somehwat with
more classifications than simply input and output. need to figure out how to reconcile this layer
with D1 and C1."*

### The result — A NEGATIVE, AND IT IS THE DELIVERABLE

**There is no S-layer and there never needed to be one.** Seven capabilities were specified across
three revisions; **seven already exist on live D1 edges** — including an `observer` field added in
REV 3 on a reviewer's finding, which `resolution` already was.

```
identity/rename -> srcField/dstField/rename    direction -> srcField->dstField
condition       -> condition + kind            grain     -> D1.grain_axis
resolution      -> resolution                  S0 site   -> via  (a FILE:LINE, on the edge)
```

**The one thing absent everywhere is a Python-side producer** — and that zero has a MECHANISM (every
field-grain emitter is a `.ts` extractor, `comp_recognizers_tsx.py`, or `cse_schema.py`), so it holds
at any graph vintage. **Andrew's one-sentence question — "wouldn't that sit at D1 anyway?" —
dissolved the design.** Two reviewers had been reviewing *inside the frame*; the question came from
outside it.

### Artifacts

| artifact | commit | note |
|---|---|---|
| `deliverables/SCRIPT_IO_ONTOLOGY_SPEC_20260806.md` | REV1 `72279a7c2` · REV2 `785ed481f` · REV3 `2d40590fa` · banner `cd7edf830` | **HISTORY, NOT A DESIGN.** Superseded by the disposition |
| `deliverables/SCRIPT_IO_AXIS_FIELD_TEST_01_20260807.md` | `2bfcc9e7e` | 8 site shapes hand-classified; 4 did not fit |
| `deliverables/SCRIPT_IO_S_LAYER_DISPOSITION_20260807.md` | `118fb1585` · `7280b1790` · `939014043` | **THE CLOSING RECORD** |
| `deliverables/PYTHON_FIELD_GRAIN_FEASIBILITY_20260807.md` | committed 2026-08-07 | ruled (b)+(c)-as-policy by CTO~D |
| **`infra/system/ontology/LAYER_FIELD_ANATOMY.md`** | `015877662` → `1ee776148` | **8 layers (5 C-rungs + 3 D-rails).** Andrew-direct placement; now indexed in the ontology README |

### Evidence basis + its bounds

Live `comp-kuzu` (20,585 nodes / 41,144 edges, built 2026-08-07T00:32Z, Nessie HEAD current);
8 first-party extractor surfaces read at source; the SDK **exercised** by CVO~C (engine runs, `Site`
populates, loci verified against **re-opened source**); 4 non-held-out tree censuses.

**BOUNDS:** `FLOWS_TO`+`PROP_PASSES` census, **`RENDERS`/`READS_FIELD`/`HAS_FIELD` UNSWEPT**; Python
probes on 4 trees only, **`bd`/`cot`/`mdpf`/assets-monolith UNSWEPT**; subscripts are **not** the only
column carrier. **Held-out fence honoured — shaping corpus declared positively (spec §8.0); no
`ATOM_DECOMP/case_study/` file read for design input.**

### Findings that outlive the engagement

1. **`via` (file:line) + `resolution` (method) on 961/961 `FLOWS_TO`** — but **0 of 1,382
   `PROP_PASSES`**, so field-flow locus is **41%**, not 100%.
2. **Portal locus precision is 9 of 14** (negative-controlled) — strong where the S-layer was
   redundant, weak exactly where it claimed its value.
3. **A declaration naming a MANDATORY field holds trivially; one naming an OPTIONAL field goes
   silently unpopulated while its COUNT stays true.** (`condition`: exact count 482, present 4.8%.)
4. **`Coverage` measures what was DISPATCHED, never what was WANTED** — a fully-filtered run is
   byte-identical to nothing-to-find. Gate the precondition.
5. **The resolved tier is MODULE-grain, not VALUE-grain** — climbing tiers buys cross-file folding
   nothing.
6. **Python has no TypeChecker analogue.** `df["col"]` and `cfg["key"]` are the same AST node; base
   naming discriminates **14.2%** even in a 75%-pandas tree.
7. **THE BUILD LADDER APPLIES TO SCHEMA, NOT ONLY TO CODE** — rung 2 was run against *extraction*
   twice and never against the *ontology slot*. Raised as a law-surface finding by CTO~D, CRO
   co-signed.

### Downstream

- **PRD → `1.0.0_SA_CTO~D`** (pure build, a TO not a naming act); **TOs → COO**; **verification →
  `3.0.0_SA_CVO~C`**. **Research proposes; it does not staff.**
- **Held-out fence question RULED by Andrew 2026-08-07** — *"its just an obvious thing and dont need
  more noise about it."* **The fence is NOT discharged**; he rejected expanding it.
- **OPEN AT ANDREW:** placement of artifacts into `projects/ATOM_DECOMP/` (lane `TIER0_MSTR`), and
  whether the atom_decomp step is authorized. **Deliberately not self-inferred.**
- Side findings routed, not adopted: 4 `CloudNode` DDLs in 3 shapes (→ `0.7.0_AE_CloudOps`);
  ontology README indexed no canonical docs (→ CVO, **fixed 3/3**); `comp-which` has **no curated
  rule** for field-shape questions (→ tool lane).

#### Downstream append — 2026-08-07, the atom_decomp continuation

**PLACEMENT RESOLVED, and it was never a placement question:** the directory already existed and was
lane-locked `TIER0_MSTR`. Andrew: *"seems like a formality that doesn't really matter."* Grant landed
by `1.0.0_SA_CTO~D` as grantor (SoD — the CRO did not self-land). **No project code minted** — he
floated one and then said it was *"not really necessary at this point."*

> ⚠ **THE atom_decomp WORK WAS BEGUN ON THE CRO'S OWN READING of the proceed-condition, surfaced
> TWICE and UNANSWERED. It is not a granted authorization.** Bounded to unwind cleanly: no project
> registered, PROPOSAL banners on every artifact, and nothing permitted to depend on it.

**Produced** (`projects/ATOM_DECOMP/`): `04` precursor outcome · `05` corroboration + 3 candidate
extensions · `06` **coherence base v0.4** · `07` retro-test (**PARTIAL**).

**The method's own laws were independently re-derived FOUR TIMES, unstaged** — its spec §5 *asserts*
generalization and proposes forward-testing; nobody staged this and it held.

**The base was applied THREE times, twice by an independent seat under a rule fixed and published
BEFORE the draw.** Results, including against it:
- **The fires-on-everything hypothesis is DEAD** — C4 fired on a 2-segment/4-pod program and returned
  **proportionately unremarkable** on a 1-pod one. *(Bounded at scoring: establishes NON-OVER-FIRING;
  the predictive claim rests on the segment-independent draw.)*
- ⛔ **The four structural rows are VERTICAL-dependent and FAIL TOGETHER.** `comp-estate` cannot be
  entered for a **cross-cutting** project — so standards/naming/governance work is a class the base
  **cannot reach**, and one dependency failing **looks like four independent gaps.**
- ⛔ **An empty cell is ambiguous** across correctly-empty / unreachable / not-looked-at, **and
  correctly-empty READS AS UNDERSTANDING.** The CRO's own v0.2 line licensed it; v0.4 requires the
  cell to declare which — **fix untested.**
- **It types POSITION, never INSTRUMENT HONESTY: of five errors in RCN-0006, it catches ONE.**

**ROUTED 2026-08-07 to `1.0.0_SA_CTO~A`** (method owner per the spec header) **for an adoption
decision — with the failure modes in the routing message, not appended after.** Recommended: take the
corroboration (free, theirs); weigh the rest on merit. **Adopted: nothing.**

**STILL OPEN AT ANDREW:** whether the proceed-condition reading stands, and `NFRA_PYFIELD` **Q1 —
build or defer** (both lanes recommend **DEFER**; no named consumer, no statable acceptance bar).

### Correction stamped in-band — 2026-08-07, `4.0.0_SA_CRO`

**This row was appended LATE.** All five artifacts were committed before the register was touched,
and **none carries an in-band `Recon ID:` tag** as charter §4 requires. It was found only when the
CRO tested its own claim that a file was "referenceable" — **the same discoverability gap it had
raised against another seat's index hours earlier, while its own register listed none of this.**
Recorded rather than quietly backfilled: an append-only register whose rows arrive after the fact is
a weaker instrument than one written at delivery, and saying so is the only thing that keeps the next
row honest. **The in-band `Recon ID:` tags on the five artifacts remain OWED, not done.**

---

## RCN-0007 -- `.tools/comp-read` itself: instrument misattachment, four instances in one exchange

| Field | Value |
|---|---|
| **Target** | `.tools/comp-read` (1250 lines, HEAD @`dc944897c5`), the estate's mandated default single-file read instrument |
| **Date** | 2026-09-03 |
| **Commissioned** | Andrew-direct at the CRO~Z terminal, VERBATIM: *"write a brief about this and commit it"*, following *"is there an obvious way to make this tool better from this?"* |
| **Owner** | `4.0.0_SA_CRO~Z` |
| **Question asked** | Is a comp-read `--for` output useful, is it too much, and is it more effective than a handful of greps -- then: why does `--for` exist at all if `--enumerate` is available? |

### Evidence basis + denominators

**9 comp-read invocations, 2 modes, 3 subject files, every figure re-run at a stated vintage rather
than recalled.** `.tools/deploy_ledger.py` 1328 lines / 43 sections @`79c0e68071` with
`git status --porcelain` EMPTY on both this seat's and the peer's runs (blob confirmed identical
across both HEADs by `0.0.0_AB_MSTR~Z`). `.tools/comp-read` 1250 lines / 32 sections.
`INVESTIGATION_v1.md` 1969 lines here against 2017 at the peer -- **a vintage skew this seat did not
detect at the time and which contributed to instance 1.4.**

### The finding

**Four errors, one class: the instrument was CORRECT in all four, the answer was attached to a
DIFFERENT QUESTION, and no output disclosed the gap.** One `--for` failure (a ranker served the limb
the file's commentary talked about most) and **three `--enumerate` failures** (wrong token for a
concept; a probe aimed at bracket-access read as a predicate census; a false absence keyed on the
asker's vocabulary rather than the row's).

**Load-bearing negative result: defaulting to `--enumerate` would have prevented ONE of the four and
CAUSED THE OTHER THREE.** The modes fail in opposite directions -- `--for` toward false completeness,
`--enumerate` toward false absence -- and `--enumerate` requires the vocabulary you do not have when
you open an unfamiliar file. They are SEQUENTIAL, not alternatives.

### Artifact (committed)

| Artifact | Path |
|---|---|
| The brief | `org/tier1_exec/4.0.0_SA_CRO/briefs/COMP_READ_INSTRUMENT_MISATTACHMENT_BRIEF_20260903.md` |

### Disposition

**PROPOSALS ONLY. Nothing dispatched, nothing staffed, no code written** (charter s.3: research
proposes on the build side). Five changes proposed; suggested owner the CVO lane with CloudComp
second, from measured commit authorship over the last 12 commits, not from assumption.

### Declared gaps, in-band

- **P5 (`--schema` mode) is UNTESTED FOR FEASIBILITY** -- comp-read's AST backend was not read to
  confirm it can enumerate dict literals by binding.
- **P3's contrast is n=2 and directional only.** Two authoritative-ratio points exist (3 of 18 on the
  read that missed, 8 of 18 on one that landed). **No threshold is proposed and none should be
  inferred** -- a band minted from two points is an unmeasured exact constant.
- **Nothing was measured on a second device.**

### Provenance

**Three of the four instances were found by a peer, not by the seat that made them.** Instances 1.3
and 1.4 were caught by `0.0.0_AB_MSTR~Z` auditing this seat's work; the better half of 1.2 by that
seat against its own instruction; the control-selection sentence in s.1.4 is `3.0.0_SA_CVO~Z`'s
formulation of this seat's finding. **Recorded because the method rests on it: the round trip is what
produced the result, and a register row that took sole credit would misdescribe how it was obtained.**

### Downstream (NOT part of this engagement)

The eight sites defining "open leg" in `deploy_ledger.py` -- seven predicates plus the renderer at
`:211` -- belong on NFRA_OPSEC202609 row **Z-S47** (`3.0.0_SA_CVO~Z`, confirmed by that seat as the
standing carrier). The INSTANCE is that project's r2b ledger; **the CLASS is a fabric item on the
deploy-ledger contract and closing NFRA_OPSEC202609 would not close it.**

---

## RCN-0008 -- Investor Reporting & Data Unification: Andrew's proposal -> the L1 brief for the D14 directive

| Field | Value |
|---|---|
| **Target** | Andrew's strategic product proposal `Opal_Capital_Investor_Reporting_Unification_Proposal_Clean.docx` (Desktop; 80,251 B; sha256 `db4168a65ef0afe2c7e8436ca9be8e2ee5776d35e6d5ae2cf4df769ff61ef0e8`) -- a dedicated advisor-first Investor Reporting product on a common data foundation, three capabilities (performance report + PDF, sensitivity analysis + PDF, Opal model-allocation visibility) on the firm -> advisor/book -> relationship -> account spine |
| **Date** | 2026-09-09 |
| **Commissioned** | Andrew-direct ~17:1xZ + ~17:2xZ at this terminal, VERBATIM in `deliverables/ANDREW_DIRECT_20260909_171xZ_INVESTOR_REPORTING_BRIEF_CREATE_WRAPS_D1_D2_D3_ESTABLISHES_D14.md` |
| **Owner** | `4.0.0_SA_CRO` |
| **Egress** | NONE. No vendor call. The docx was read locally; every other read was repo, register, or the estate's own AWS plane via `comp-trigger --list` (read-only, operational). |

### Evidence basis + denominators
The proposal, extracted to 450 blocks (styles + 20 tables preserved) and read entire. Directives board: 13 live
(D0-D12), 1 retired, neither D13 nor D14 in either register file (0/481 and 0/44 lines). Registry: 355 project JSONs,
48 open, 86 open TOs. PRD SS1-SS2 reads: D1, D2, D3, D6, D8, D10, MDPF_CHANNEL_INDEPENDENCE, PORTAL_AUTHHARD, ADVI_ROLGAT;
ADVI_PERFRP header only. Censuses (`comp-find`, corpus=all, ~152,38x files): `supervis` 12,243 hits (DEF 10);
`billable` 1,078 (DEF 6); stress-scenario tokens 103 (DEF 0); PDF libraries 143 (DEF 13, all puppeteer `.mjs`).
Gold script listing: 208 `.py` across 6 trees. Live triggers: 142 EventBridge rules + 19 Scheduler schedules.
`comp-schedule`: 26 armed gates. `comp-read` on `data/cot/scripts/gold/D_05.supervised_split.py` (account grain,
current-flags caveat).

### Artifacts (committed)
| Artifact | Path |
|---|---|
| The brief (L1) | `docs/briefs/investor-reporting-unification-brief-20260909.md` |
| Citable source text | `docs/briefs/sources/INVESTOR_REPORTING_UNIFICATION_PROPOSAL_20260909_extracted.txt` |
| Andrew-direct record | `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_171xZ_INVESTOR_REPORTING_BRIEF_CREATE_WRAPS_D1_D2_D3_ESTABLISHES_D14.md` |

### Findings that carried (the brief's Part IV, compressed)
1. Three legacy routes live, no Investor Reporting route -- the product surface is greenfield (F-A).
2. Gold is 208 scripts across 6 per-firm/per-domain trees with THREE bucket generations live; "same gold contract
   across partners" is the D10 direction, measured on 49F only (F-B).
3. Supervision/billing exist as per-firm gold FIELDS at account grain with a current-flags caveat (cot), not as a
   two-axis cohort dimension (F-C).
4. Tenant isolation measured sound at 07-20 (edge JWT + `X-Firm-Id` injection + ownership-map + ROLGAT) -- a reuse (F-D).
5. The performance method is further along than the proposal says: Account365 PINNED (Andrew 07-21), contract
   WRITTEN (RCN-0001/0002), `fact_account_return` HELD since 07-22, TWR engine LIVE (ADVI_49F), parity harness LIVE
   (ADVI_BDPARITY); the open question is the HOME (ADVI Books tab per ADVI_PERFRP vs Investor Reporting per SS06 D01) (F-F).
6. Sensitivity/stress is GREENFIELD (0 DEF hits); PDF-as-client-artifact is GREENFIELD (F-G, F-H).
7. Scheduling is two mechanisms (142 UTC-cron rules + 19 schedules incl. `-et` ones); event-driven silver->gold
   exists for cot and inf; SS14 restates the 2026-07-24 channel-independence rulings and the D8 frozen-payload incident (F-I).
8. The path manifest was attempted per partner (NFRA_PPL49F/INF/COT) and is dormant at Phase 0 since 07-10 (F-J).

### Downstream
- **Consumer:** `1.0.0_SA_CTO` at L2 (`/endpoint --forward`). Twelve outcomes O1-O12 cut for a person to do; O12 is
  horizon-bearing and flagged as a constraint, not a build.
- **Register act named, not taken:** D14 row = `0.0.0_AB_MSTR`'s cell; member re-homing = CTO at L3.
- **Surfaced for Andrew:** the ADVI_PERFRP 08-24 distribution restriction naming this seat (stand / lift / scope).
- **Declared not chased:** why NFRA_PPL* stalled; INF cohort semantics; silver column retention; live bucket reads.

### Downstream append -- 2026-09-09 ~18:2xZ, the YCharts field scrape (Andrew-direct, same terminal)
Andrew: *"do a fine-toothed scrape of the various fields in this document and include it as a json file addition to CTO,
because this is the information that the current YCharts solution provides"* -- one YCharts portfolio-vs-Opal-model comparison
report (33 pp, sha256 `dc824eac…68a90`, client-named, kept in Downloads, NOT committed). Delivered
`docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`: 33 sections / 176 catalog rows / 125 distinct
fields / 1,359 numeric values / 46 glossary terms; 33 of 33 pages text-extracted (pypdf), 33 of 33 rendered (PyMuPDF), 7 chart
pages viewed. PII scrubbed: client name, advisor contact, client-portfolio inception date, Opal compliance contact. Brief
amended with finding F-M + non-claim 13. Findings: hypothetical weighted-blend calculation, not account performance; four
as-of clocks in one report; ~half the fields are look-through classification (the RCN-0001 moat); alpha/beta benchmark unnamed;
**no stress scenario anywhere in the artifact**. No vendor egress.

### Correction append -- 2026-09-09 ~18:4xZ, Andrew-direct, same terminal, VERBATIM
*"THe YCharts artifact is not a performance reporting product, that is a sensitivity analysis. The performance reporting asset
is product 1, this is a sample of 1 of 3 varietals for product 2."* The downstream entry above framed the artifact against
product 1 (performance reporting); that framing was this seat's and is WRONG. The artifact is PRODUCT 2 (sensitivity
analysis, brief O4 / Capability 2), varietal 1 of 3; the remaining two varietals are uncaptured. What stands: no
historical-scenario replay in THIS varietal. Corrected in the brief (F-M, non-claim 13) and in the JSON
(`_meta.classification_correction`, `what_this_report_is`); the 18:2xZ entry above is left as written per this file's
append-only law. Record: `deliverables/ANDREW_DIRECT_20260909_184xZ_YCHARTS_ARTIFACT_IS_PRODUCT_2_SENSITIVITY_1_OF_3_VARIETALS.md`.

### Placement append -- 2026-09-09 ~21:0xZ, Andrew-direct, same terminal, VERBATIM
*"its ok I think we can basically wrap that whole function into D9 Opal Workflows, because it effectively is going to be a
bunch of middlemanning ops that pulls data from some vendor, runs it through some AI/pipeline processes, and becomes a flow on
the dashboard."* Supersedes the ~17:2xZ "dedicated D14" placement this engagement was cut under. Brief re-pointed (title,
Part II, F-K, Part V.1, REFS); outcomes O1-O12 unchanged. No register row written by this seat (D9 member set = MSTR's).
Record: `deliverables/ANDREW_DIRECT_20260909_210xZ_INVESTOR_REPORTING_WRAPS_INTO_D9_OPAL_WORKFLOWS_NOT_A_NEW_D14.md`.

### Pilot append — 2026-09-10, 4.0.0_SA_CRO — one project, four workstreams

Andrew commissioned a lightweight /brief-create using vendor reports and existing silver caches, then clarified ONE umbrella project with FOUR workstreams, potentially coordinated across COO lanes. His full wording and clarification are preserved in `deliverables/ANDREW_DIRECT_20260910_0919ET_LIGHTWEIGHT_INVESTOR_REPORTING.md` (initial record `822f3d7519`). D9 placement stands; the September 9 broader brief is preserved.

Artifacts:
- `docs/briefs/investor-reporting-lightweight-brief-20260910.md` — six person-action outcomes; four workstream boundaries; WS1 explicitly owns discovery/entitlement as well as the page; no orphaned shared substrate.
- `docs/briefs/investor-reporting-lightweight-design-20260910.md` — page shape, partner identity/cache methodology, performance normalizer, YCharts routing/capture requirements, holdings/model normalizer, common report/PDF lifecycle.
- `docs/briefs/sources/INVESTOR_REPORTING_LIGHTWEIGHT_EVIDENCE_20260910.json` — 31 source fingerprints with targeted-read scope; three registry client firms.

Findings: existing 49F BD performance request builder; Orion on-demand response gap versus an existing saved-query pull; 49F Schwab/BD/SmartX key distinctions; INF household/representative mapping with some legacy-bucket inputs; COT relationship membership grain and incomplete segmentable advisor model; existing YCharts transport is not proof of report-generation routing. Current live joins, freshness and timing remain unmeasured. YCharts analyst transcripts/generation HAR and two remaining sensitivity varietals are pending evidence. No vendor egress, live S3 read, implementation, deployment, project registration or task-order issuance. Consumer: CTO L2. Push state LOCAL at delivery; origin hash carried in the delivery receipt.

### Performance follow-up — 2026-09-10, 4.0.0_SA_CRO — Andrew-directed WS2 review

Andrew supplied three HARs and four screenshots and expressly authorized current-use Black Diamond/Orion performance egress; exact direction in `deliverables/ANDREW_DIRECT_20260910_0947ET_PERFORMANCE_ENDPOINT_EGRESS.md` (7775dd14ea, subsequently published). Inventory: 487 HAR entries; all four screenshots viewed; targeted performance/search/membership bodies inspected. Nine HTTP requests: two initial BD 401s, then seven 200s including normal session-token renewal; six successful report calculations. BD period/series parity confirmed for one account. Orion one household/two accounts, three period summaries and 92 daily factors per group in one 119,975-byte response; linked factors match provider summary in 3/3 groups. Cumulative=true experiment returned 5.3 MB and repeated date pairs, rejected for the proposed chart. Orion `startValue + valueChange` failed three of nine explicit valuation comparisons, so no certified dollar chart is claimed from that shortcut. No new return engine, production implementation, scope-exclusion proof, 49F live tenant proof or endpoint ratification.

Delivered: `docs/briefs/investor-reporting-performance-review-20260910.md`; `docs/briefs/sources/INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json`; reusable bounded `docs/research/investor_reporting_performance_20260910/probe_performance.py`; synthetic interactive `presentation-review.html`. Proposed core: beginning/ending value, period return, cumulative-return chart, periods and account detail; optional verified benchmark/cash/value-history sections. WS1 seam records cached per-firm/advisor autosuggest followed by explicit authorized account resolution. Raw captures, live responses and credentials remain outside committed artifacts. Also qualified the L1 coordination sentence: Tier-2 one-project-per-instance law exists; the Tier-1 COO workstream boundaries do not waive it (COO correction 95189). Consumer: Andrew selective design review; CTO/COO informed as consumers, no task issuance.

### Governance wording correction — 2026-09-10, COO message 95226

The preceding entry and WS2 delivery used the ambiguous phrase “Tier-1 COO workstream boundaries do not waive it.” Replace that reading with the precise scope: **the one-project-per-instance rule exists and is enforced for Tier-2 seat instances; its application to Tier-1 lanes is an open question held by `1.0.0_SA_CTO`. Amended Rule 27 binds the round, not the project, so Andrew's four-workstream split stands as described.** The L1 coordination paragraph now states this explicitly. The preceding register entry remains as history under the append-only rule; it is not authority for a settled Tier-1 binding.

### Operative scope ruling — 2026-09-10, CTO message 95229

CTO resolved the meaning of the preceding “open question”: **the Tier-2 seat-instance rule does not apply to Tier-1 today or unless Andrew extends it.** Whether Andrew wants a future extension is the only open question; nothing waits on it. Andrew's four-workstream split across COO lanes proceeds under amended Rule 27, one issuer per round. The L1 paragraph now records this operative state. The existing Tier-2 gate remains in force; any refusal involving a Tier-1 serial routes to CTO without override. Prior register entries remain historical and do not establish a pending prerequisite.

### Branded export and narrative arc — 2026-09-10, 4.0.0_SA_CRO — Andrew-directed WS1–WS2 extension

Andrew requested a standard performance PDF using the deck-generation Opal guidelines, optional advisor identity/high-definition logos that he will provide, and a full-width performance narrative page. Dashboard remains the default. Verbatim direction: `deliverables/ANDREW_DIRECT_20260910_PERFORMANCE_EXPORT_NARRATIVE.md`, committed `bb9bc792c2` and broadcast before research. This adds O7 to the existing umbrella brief and extends O3; four workstreams remain. WS1 owns branding/options/rendering and export lifecycle; WS2 owns measured events, dated market evidence and narrative validation.

Inspected BD part 3: 139 HAR entries and all 15 supplied PDF pages. The selected nine-design template POST returns HTTP 200, package status Queued, 0% complete, size 0 and sharing disabled in this specimen. Supplied PDF filename matches package ID; captured completion/poll/download chain is absent, so byte-equivalence is not claimed. No package-generation or sharing operation was replayed. All 13 Opal guideline pages were text-read, with logo/color/typography pages viewed; actual logo/spec and PPTX font-enforcement code were inspected.

Historical source finding: dated Trending Topics rows are written to `opal-news-trending-daily`; Topic Cloud's producer archives timestamped reports in `opal-data-news-v2/trending_reports/YYYY/MM/DD/` before final display filtering. The archive is not automatically an exact record of the displayed cloud. Current 14-day keyword snapshots, present-day fallback values and categorical ±0.6 display scores cannot substitute for dated source evidence. Historical coverage, final-cloud fidelity and optional indicator/ranking vintage remain unmeasured. The narrative uses measured drawdown/movement events followed by time-bounded topic/article evidence; coincident context is not client-specific causal attribution.

Delivered specification: `docs/briefs/investor-reporting-export-narrative-spec-20260910.md`; evidence: `docs/briefs/sources/INVESTOR_REPORTING_EXPORT_NARRATIVE_EVIDENCE_20260910.json`; reusable offline capture profiler and synthetic PDF builder under `docs/research/investor_reporting_export_20260910/`; four-page `performance-export-review.pdf`. Checks cover a hand-calculated drawdown/recovery, flat/rising/unrecovered/tied-peak cases, invalid inputs, four-page rendering with embedded Lato and loaded Opal logo, page/footers fitting, and three-page performance-only export with narrative references removed. All four prototype pages were viewed; after fixing the narrative footer spacing and date ticks, the changed narrative page and performance-only methods page were viewed again. Performance figures and themes are fictional. Raw HAR/PDF bodies and local renders stay outside committed artifacts; font license is retained with the embedded-font PDF. Current follow-up made no vendor or live AWS-history calls; public egress obtained official Google Fonts Lato assets only. No production generator, portal integration, historical census, report distribution or task-order issuance. Consumer: Andrew design review; CTO/COO carry the extension through the existing project boundary.

### YCharts intake and serving — 2026-09-10, 4.0.0_SA_CRO — WS3 child brief

Andrew supplied `Desktop/YCharts Transcripts` and requested a new brief under the existing Investor Reporting umbrella, with explicit generation/retrieval instructions and email ingestion. Direction record `deliverables/ANDREW_DIRECT_20260910_YCHARTS_INTAKE_AND_SERVING.md` began at 76b2f37152 and carries his subsequent clarifications: every day, actual holdings attachments, mutual session eviction accepted, exact BDAPI/Kimi runner style and no OTP stage. Password values are omitted. No new project registration or task issuance.

Artifacts: `docs/briefs/investor-reporting-ycharts-brief-20260910.md` (six local person-action outcomes under parent O4); `docs/briefs/investor-reporting-ycharts-design-20260910.md` (cloud mailbox intake, input/revision contract, BDAPI runner adaptation, explicit three-variant vendor retrieval, encrypted records, section rendering/review/export and dependency sequence); two `INVESTOR_REPORTING_YCHARTS_*_EVIDENCE_20260910.json` manifests; reusable offline `docs/research/investor_reporting_ycharts_20260910/profile_handoff.py`. Parent brief/design now link this dated evidence extension while preserving their original-cut qualifications.

Measured supplied evidence: six transcripts, request manifest, 26 ZIP manifest files all matching SHA/size; three slim HARs with 220/403/462 entries (1,085 total), six report POST 201 responses paired by exact returned URL to six PDF GET 200s. All three report routes occur in the August HAR; PDF bodies are absent. Report rendering is a synchronous slow POST returning the URL; portfolio calculation is the polling stage. July HAR 03 supplies upload response row fields and `model_portfolio_id`, closing gaps in the August response bodies. The newest-list-row fallback is explicitly rejected. Newer capture/analyst fee is 0.003 annually, not the July 0.01 setting. No new custom-scenario API is inferred from null/empty fields.

Cloud/source findings: old `ycharts/credentials` contains cookies, while the existing session/current resource had no AWSCURRENT value. At Andrew's explicit request, created and read-back verified `ycharts/login/credentials` in us-east-1; legacy cookies untouched, secret values absent from committed artifacts. At 15:41:51 UTC, the requested `opal-data-ycharts` bucket returned 404/NoSuchBucket; no bucket deployment occurred. Inspected the exact BDAPI Node/Playwright/Kimi runner, wrapper and scoped IAM; its OTP-dependent success predicate must be replaced for YCharts. CTO Base 95295/95301 supplies source/deployment pointers with explicit graph-snapshot vintage; this seat's compiler graph read failed through the AWS shim and is not independent measurement.

Mailbox proposal: requests@ forwarder to internal opalbloomberg@ mailbox, quarter-hour daily intake 08:00–23:45 America/New_York, Graph delta/attachment reads with scoped cloud identity and durable checkpoints. That cadence is not scheduled vendor login. No live YCharts call, mailbox read, forwarder setup, runner deployment, production UI or distribution was performed. Remaining evidence: representative forwarded request/attachment, cloud mailbox binding, upload request/error body, actual PDFs and section fidelity across all three variants. Child status NOT-OUTCOME-BEARING. Consumer: Andrew review; CTO/COO umbrella boundary; MSTR publication.

Publication terminology correction: the relevant shared publication ref is **origin/CLOUD**, not origin/main. Earlier main-ref observations do not establish publish status. CTO Base 95286 also confirmed the separate numbering spaces: parent O3 maps to FWD-3 and parent O7 to FWD-8; local child outcome numbers do not replace those permanent endpoint IDs.

### WS3 review correction — 2026-09-10, CTO Base 95318

CTO identified that carrying the recorded analyst queue into every release would silently add a staffing dependency despite Andrew's wish for an entirely programmatic flow. Revised the child brief's face, O2/O4/O5/O6, lifecycle and diagram: proposed default is automatic serving of complete validated requests, with human correction for unresolved exceptions. Explicitly asked Andrew whether he instead wants universal analyst approval; neither policy is enabled in production. The recordings' ambiguity/substitution examples and the manifest's object/session incidents are evidence of specific failure classes, not a measured blanket claim that unattended inference is unreliable. Unique supported mappings, reconciled inputs and certified output checks identify when a class of request can proceed automatically.

CTO reports FWD-4's original HAR/transcript handoff qualification discharged and reserves its endpoint amendment to L2. This is his disposition, not this seat's endpoint edit. Paired PDFs, missing upload multipart and native section/export parity remain explicit in both WS3 and the shared export specification. Also checked the root manifest's source/output references and exact basenames within the supplied inputs; neither referenced artifact was present there. The existing shared merge continued to defer pathspec commit without staging this seat's files.

### Holdings and model overlay — 2026-09-10, 4.0.0_SA_CRO — WS4 child brief

Andrew requested the final tab's /brief-create: advisor-keyed current holdings, model percentages and existing Asset Category taxonomy with pie/radial drilldowns; no time-series view in v1. His verbatim direction is `deliverables/ANDREW_DIRECT_20260910_HOLDINGS_MODEL_OVERLAY_V1.md`, committed `f9761f444f` and broadcast before research. This is the fourth workstream in the existing D9 Lightweight Investor Reporting umbrella, not a separate registration. The proposed default preserves the shared selected client inside the advisor's authorized account set; an optional question about opening on the advisor's full book was still unanswered at drafting.

Delivered research: `docs/briefs/investor-reporting-model-overlay-brief-20260910.md` (six local person-action outcomes under parent O5 / permanent FWD-5); `docs/briefs/investor-reporting-model-overlay-design-20260910.md` (three adapters, account/model/position grains, observed versus assigned/target attribution, taxonomy/radial semantics, source selection and gold/platinum serving seams); `docs/briefs/sources/INVESTOR_REPORTING_MODEL_OVERLAY_EVIDENCE_20260910.json`; offline profiler and source-read list under `docs/research/investor_reporting_model_overlay_20260910/`. Parent brief/design link the dated child while preserving the original-cut qualifications.

Measurements: six named `opal-data-assets` silver roots listed at 17:27:01 UTC; 19 selected Parquet datasets profiled at 17:28:57 UTC; four legacy identity tables profiled at 17:36:14 UTC. Offline replay verifies all 23 private objects, totaling 15,753,977 bytes, against recorded SHA-256/size. Selection is latest independently observed dated partition on or before September 10, not proof of common completed snapshot/trading alignment. No raw client rows, private local paths or holdings amounts are committed.

49F: September 9 Schwab 08335338 holdings contain 104,807 rows/6,237 holding accounts. September 10 SmartX map has 7,453 rows; 7,431 join 5,856 custody accounts. All joined allocations have valuations, 7,402 have positions; the separate account-allocations table is empty. SmartX intraday value clocks differ from custody. Existing b04 advisor aggregation is unavailable; the inspected legacy August 18 group/account bridge has 29,907 rows and no populated is_primary. This is a bounded source-home finding, not estate-wide absence.

INF: September 10 Orion has 35,974 positions/953 accounts; its parallel assets feed matches on five identity/value/share fields and must not be summed again. Eclipse simple has 845 portfolios, 790 populated account IDs all joining holdings; 658/663 populated model assignments resolve only when the two catalogs are combined with declared integral-ID normalization. Five remain unresolved; 13 full-only multi-account portfolios need explicit membership. The inspected legacy account dimension covers 874 holding accounts with current-roster representatives and household IDs; 79 holding accounts lack that inspected identity row. Login entitlement and constituent/value parity remain untested.

COT: September 9 holdings contain 18,917 rows/18,817 unique account-asset keys; 100 duplicated keys agree on market value. August 30 Rebalancer assignment/roster/blend/definition is the newest observed source set. 946/950 assignment rows join holdings, 23 holding accounts lack assignments, all 464 named assignments resolve uniquely to the roster. Existing recursive calculation multiplies custody account value by target weights: assigned model mix, not observed sleeve valuation. Preserve residuals, newer Cottonwood SMA membership, per-source clocks and taxonomy unknowns without turning them into Client assets.

Source/prior-art review covers D1 Asset Category Views, D3 Account Model Overlay, current registry and partner runners, plus existing portal category/donut components. No app was run, monetary reconciliation certified, cloud data changed, new API deployed or task order issued. Source compiler graph omitted an existing runner and the freshness compiler declined held configuration; no override or freshness-grade inference was made. Subsequent runtime/permission/classification validation belongs to the implementation proof described in the brief.

CTO Base 95374 was read, ACKed, its stamped endpoint consulted and the exact inbox file archived after acting. It reports all eight parent FWD outcomes ratified and permanent, terminated clients visible under entitlement, and no logo prerequisite. These boundaries are carried in the WS4 brief; no endpoint was edited. Its narrow Tier-2 seating ruling discharges the earlier standing ASK; prior register entries remain historical. Publication is measured against origin/CLOUD in the delivery receipt.


### Investor Reporting split into IR FE and IR BK - 2026-09-10, 4.0.0_SA_CRO

Andrew requested two project briefs consolidating all four source briefs and five supporting documents. Delivered `docs/briefs/investor-reporting-ir-fe-brief-20260910.md` (six local outcomes, entire client-facing product and shared presentation/render package) and `docs/briefs/investor-reporting-ir-bk-brief-20260910.md` (seven local outcomes, ingestion, current firm/advisor/account authorization, identity/cache, provider retrieval, model joins, narrative evidence, export jobs and ETL operations). Each contains all nine source mappings, exact functional paths, explicit counterpart ownership and the shared producer/consumer contracts. Local O-n labels do not replace FWD-1 through FWD-8; CTO retains formal ACCEPT assignment.

Authority: exact-seat split record initially 6226b4a680, subsequent priority/laptop direction c0f5ed8163, IRPT/D9 naming 1f0f1dd3f6, and whole-D9 laptop move 4ff4abd9a4. Exact records read and relevant inbox messages acknowledged, acted on and archived. No directive/project register edits or other-project closures by this seat. The prior single-project organization is superseded with one dated notice in each of the nine sources; source bodies preserved.

Validation: evidence `docs/briefs/sources/INVESTOR_REPORTING_FE_BK_SPLIT_EVIDENCE_20260910.json` records all nine before/after hashes, authority hashes, two brief hashes, 83 distinct inline repository paths (78 existing, five explicitly proposed), 53 local links, all 31 initial design source-index paths carried, seven Parts in each brief and 11 shared contract names. The initial path comparison reported one false missing path because a relative Markdown link was not normalized; canonical resolution corrected the checker, and all 31 are carried. No source body change beyond the organization notices. Narrow credential-signature scan found no key/bearer/Cookie headers in the two briefs and split record; this is not a universal secret scanner. No fresh AWS/vendor/UI/authentication measurements this consolidation; dated source limitations retained. Pathspec commit and origin/CLOUD publication are reported separately on delivery.


## RCN-0009 -- MDPF_CANON as the first /legacy-transform subject: the engine emits NAME and POSITION, never DEPENDENCY

**Date:** 2026-09-18 ~17:1xZ-18:0xZ . **Commissioned:** 1.0.0_SA_CTO msg 98014 (research ask, relaying Andrew's
described flow: /legacy-transform -> NAME, POSITION, DEPENDENCY -> LGIC_NAMING desired table -> migration plan ->
/canonical-flow). **Artifact:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/LGCTFM_SUBJECT_ANALYSIS_MDPF_CANON_AS_FIRST_LEGACY_TRANSFORM_20260918.md`.

Three answers by measurement. Q2: DEPENDENCY is ABSENT from the contract -- six `current.*` cells on 184 of 184
(49F) and 15 of 15 (mdpf) rows, no relating field; `edges` 0 in 6 of 6 runs and the only writer is forks'
REPLACES; plan.json `dependencies` is the R19 step chain (895 of 895 same-row, 0 cross-row); plan order = tension
rank x R19 step. Q1: the engine types every tension A3/GRAMMAR/R1 by module constants (`lib/opal_lgctfm.py:571-573`
@af794c77e3), so 49F reads 179 of 179 one class and mdpf 10 of 10; structurally five classes are 49F-only (R9
re-land, whole-bucket retire, new-bucket mint, identity-spine multi-spelling cutover, router map flip) and three
are MDPF-only (FORK fired today, dedicated runner, Scheduler-heavy triggers). Q3: same-subject non-mutating
dry-runs transferred 3 of 3 read; stand-in / pre-canon / never-ran did not, 3 of 3; the real subject has already
been walked five times. Instrument read: one engine run over `mdpf` rooted in the session scratchpad (run-id
20260918T174353Z-685dc7e), repo run home and registries untouched, not committed. Five proposals (P1-P5), none
dispatched. No recommendation on ADVI_FIRMBKTS sequencing or on the subject choice, which is Andrew's.


## RCN-0010 -- The start-to-finish walk of the model-portfolio pipeline, and the ruleset for compiling it (the LGIC_LGCTFM pipeline-walk brief)

**Date:** 2026-09-18 ~18:4xZ-19:4xZ . **Commissioned:** Andrew-direct ~18:2xZ and ~18:3xZ at this terminal (records
@28a8ae74e3, @c9e54d5c0f). **Artifacts:** the walk
`org/tier1_exec/4.0.0_SA_CRO/deliverables/LGCTFM_PIPELINE_WALK_MDPF_START_TO_FINISH_20260918.md`; the brief
`docs/briefs/d14-lgctfm-pipeline-walk-brief-20260918.md` (midstream, for the CTO's /endpoint --forward). Binding
requirement: 1.0.0_SA_CTO R-81 @4443e7308e.

Answer to Andrew's question: NO such walk is established in /legacy-transform (bucket-seeded, no edges, no consumer
hop). The walk with the comp-tools that exist found on the model-portfolio subject: 7 triggers with targets (one
CROSS-SYSTEM: mdpf-feeder-accelerator fires on opal-data-inf's sentinel, a bucket ADVI_FIRMBKTS retires), 6 Lambdas +
1 EC2 runner (absent from EC2_MANIFEST.json; started by the two trigger Lambdas holding ec2:StartInstances), 13 roles,
11 policies, 3 alarms, 6 log groups, an SSM parameter and a secret path outside the 33-type vocabulary, 17 packaged
scripts, ~30 storage locations, 3 routes, 1 component; record scans 128 of 831 change-management records and 884 of
6,068 log files with every off-plane name classified (mdpf-daily-trigger RETIRED 2026-08-07 by record); four sibling
platinum keys written in the same second carry four viewer verdicts (VISIBLE / consumed-by-field route-unresolved /
routed field-use-unmeasured / NO-ROUTE). Ruleset W1-W13 in the brief's Part V; eight outcomes O1-O8. Two static
instruments disagree on one script's writes (union rule). Nothing moved; no applied-plane GET exercised; the
integration carrier is the CTO's.


## RCN-0012 -- Claude for Financial Services: the plugin's structure and data shapes, and the RESAPP threading proposal

**Date:** 2026-09-22 ~14:5xZ-15:5xZ. **Produced under:** `4.0.0_SA_CRO~F` (site Z). **CORRECTION 2026-09-22 ~15:4xZ (`4.0.0_SA_CRO~F`):** this engagement was first stamped RCN-0011 in commit 621cecb40a and in msgs 24296-24298; that id was already used on 2026-09-19 by the base seat's `_authz` layer-fork research (deliverable on disk, unregistered here), so it is RENUMBERED RCN-0012 and a pointer row for RCN-0011 is added to the index above. **Commissioned:** Andrew-direct at this
terminal ~14:5xZ, verbatim in `deliverables/ANDREW_DIRECT_20260922_145xZ_CLAUDE_FOR_FINANCE_RESAPP_RESEARCH_PROJECT.md`
@c23d5f7dc0 (three sequenced steps; two briefs). **Artifacts:** `briefs/CLAUDE_FSI_PLUGIN_STRUCTURE_AND_DATA_SHAPES_BRIEF_20260922.md`
(teardown, CAPABILITY); `briefs/RESAPP_CLAUDE_FSI_THREADING_PROPOSAL_20260922.md` (PROPOSAL, nothing dispatched);
`deliverables/CLAUDE_FSI_RECON_20260922/` (endpoint discovery card + raw JSON).

**Evidence basis:** `anthropics/financial-services` @574ed36 (2026-09-21) cloned and read (19 marketplace entries, 10 agent
plugins, 6 verticals, 2 partner, 10 cookbooks; 5 `.mcp.json`, 3 SKILL.md, 2 agent prompts, 1 agent.yaml); the LLY pack in the
synced SharePoint library (58 files; README + SOURCES in full; 3 xlsx / 13 sheets; 2 Opal-branded docx); 12 of 12 declared MCP
servers probed unauthenticated (well-known metadata + `initialize`); public docs (platform MCP-connector page, two Anthropic
announcements, Daloopa x3, Kensho x2, the install tutorial); the CTO~W card 1 @5007337353. `[BODY-NOT-CAPTURED]` for every
vendor tool body (no token); Yang Liu's session not read.

**Findings:** (1) the plugin is files (prompts, skills, twelve HTTP MCP URLs), not access -- every connector is OAuth 2.1
against the vendor's own authorization server and presupposes a subscription; (2) the LLY pack was built from PUBLIC sources
only (EDGAR + StockAnalysis + Fintel + press) because, per its own README, every configured connector needed an OAuth grant a
non-interactive session could not complete -- the "API access" Andrew described did not run for it; (3) the core plugin's
`.mcp.json` at the cloned vintage is malformed JSON (zero connectors would load); (4) MT Newswires 404s at its declared path,
Chronograph publishes no RFC 9728 metadata; (5) Daloopa is the one vendor with a published datapoint shape, and it types onto
the model block's `(security_key, fiscal_year, mnemonic)` grain with a filing citation ours lacks. Proposal: three threading
options (skill-as-producer, MCP-in-our-producers, vendor REST as a harvest channel); recommended path with no new subscription
= extend the filings channel to the quarterly event (8-K/10-Q/DEF 14A), derive consensus revisions from Bloomberg `bestdata`
bronze vintages, lift the skills' METHODS as specs, transcripts through AMGT_HARVST; vendor REST channel only after Andrew's
subscription word. Six substrate cards named with owners; four open calls to Andrew. **Egress:** one public `git clone` and
one credential-free discovery handshake, both under step 1 of the verbatim instruction; no vendor data API called, no Opal
data sent. Nothing installed on this box.

### Downstream (2026-09-22 ~17:3xZ, `4.0.0_SA_CRO~F`)
Andrew read both briefs at this terminal and gave the design in four messages (record
`deliverables/ANDREW_DIRECT_20260922_17xxZ_CLAUDE_ANALYSIS_LAYER_PLATINUM_DESIGN.md`) plus a 6m34s voice memo relayed from the
laptop fabric on his word (`deliverables/ANDREW_VOICE_MEMO_20260922_HARVEST_INFRA_OVERVIEW_TRANSCRIPT.md`): the Claude API is an
ANALYSIS LAYER on top of harvest data, platinum per security inside `opal-data-harvest`, the equity-research skill lifted, the
SharePoint earnings-report corpus as the format authority and backfill source, sector KPI/model templates, and a V2 sprint
(flags, the Opal Analyst in Teams, the earnings calendar) named but not cut. The proposal brief is SUPERSEDED by the L1 brief
`docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md` (MIDSTREAM on AMGT_RESAPP, eleven outcomes O1-O11, for
`1.0.0_SA_CTO~Z`'s `/endpoint --forward`). On Andrew's word at ~17:3xZ no site-Z seat is notified yet; he carries the brief to
the CTO himself.

## RCN-0013 -- AMGT current state and a direct closer program for MVP

**Date:** 2026-09-23. **Produced under:** `4.0.0_SA_CRO~Z`, device OPAL_BLOOMBERG, SITEZ.
**Commissioned:** Andrew-direct at this terminal; verbatim record
`deliverables/ANDREW_DIRECT_20260923_AMGT_CURRENT_STATE_AND_CLOSER_MVP_PLAN.md` @`58bfd6f882`.
**Package:** [AMGT measured state and MVP program](deliverables/AMGT_MVP_RESEARCH_20260923/README.md).
Four end-to-end pipeline briefs, CLOUD precedent index, proposed shared-surface closer contract,
dependency schedule, 21-row gap register, timestamped measurements, complete S3 metadata inventory,
source hashes and read-only reproduction instruments. **Status: DELIVERED research / PROPOSED execution;
no closers seated, orders issued, vendor/model calls, deployments, source-library writes or push.**

**Evidence:** source baseline `5deabdefa9`, portal DEV `b3d5f59b45`, fetched CLOUD `365ab567ba`;
all three canonical AMGT homes and anchored task-status census (RESAPP 191: 181 complete, 8 superseded,
1 withdrawn, 1 pending; HARVST 18 complete; CORPUS 10 complete / 1 pending); all 2,277 current objects
in opal-data-harvest; selected retained-object hashes/Parquet counts; actual Lambda ZIP/code comparison
(44/48 inspected API members match local), role policies, 16 deployed AMGT routes, AWS/local schedule
configuration and local library metadata (93 folders / 351 files). CTO message 24746 supplies a clearly
attributed outstanding-review correction; current path-rule definitions were independently read.

**Conclusion:** landed components and closed task orders do not establish the full report. No platinum
objects exist in the measured bucket; corpus currently retains 123 files across 33 resolved names with
60 folders unresolved; the deployed Chatter path remains legacy despite landed gold; refresh declares
its carrier without enqueuing; recent API fixes are not yet deployed. Proposed four direct closers:
security data/filings, publications/chatter, corpus, report/page/export, with sole shared integration
owners and independent acceptance. Preserve pre-implementation schema/denominator checks, L4-R,
never-widen and specific external operating bounds while removing repetitive routine recutting.
The first representative report and full-population MVP have separate milestones; timing is explicitly
an initial conditional estimate. Authenticated live browser/export, fresh vendor/model runs and full
outcome acceptance were not exercised by this research. LOCAL; origin/SITEZ measured `95be3bc7a9`.

## RCN-0014 -- `opal_ai`: the Opal Analyst as a microproduct in three slices

**Date:** 2026-09-23. **Produced under:** `4.0.0_SA_CRO~X`, SITEZ. **Commissioned:** Andrew-direct at this terminal
~18:5xZ; verbatim record `deliverables/ANDREW_DIRECT_20260923_185xZ_OPAL_AI_MICROPRODUCT_REPO_BRIEF.md` @`6ae5ab5fd3`.
**Package:** the L1 brief `docs/briefs/opal-ai-microproduct-repo-brief-20260923.md`, for `1.0.0_SA_CTO~Z`'s
`/endpoint --forward`. **Builds on** `4.0.0_SA_CRO~Z`'s 09-22 templating assessment @`20de682ede` (seven recs approved).

**Finding in one line:** the three things he named are already one stack -- a Claude seat whose only external surface is
the Opal Gateway MCP, and an index layer being built inside that gateway -- so `opal_ai` gathers existing prior art into one
repo; nothing in it is a new product. The template's MCP half is extracting configuration into one instance manifest; its
vendor half is the ratified Third-Party Standard plus the documented access paths (official REST; cookie-riding REST with an
EC2 re-auth box; standing session box; file delivery; rendered page last); The Walk is RCN-0001/0002's HAR profiler; the
client slice is Andrew's own 08-19 client data-access design. Two conflicts are named, not resolved: the 09-22
`opal_analyst` naming versus today's single `opal_ai` repo, and the Third-Party Standard's alarm step versus the monitor
moratorium. **Status: DELIVERED as CTO intake. Nothing dispatched, no repo created, no project registered. Repo reads only
-- no AWS, gateway, Teams or GitHub read.**

## RCN-0015 -- the GitOps split of `opal_ai`: portal-shaped, done properly

**Date:** 2026-09-23. **Produced under:** `4.0.0_SA_CRO~X`, SITEZ. **Commissioned:** Andrew-direct at this terminal
~22:0xZ; verbatim record `deliverables/ANDREW_DIRECT_20260923_220xZ_OPAL_AI_GITOPS_SPLIT_SPEC.md` @`bd282e03e9`.
**Package:** `docs/briefs/opal-ai-gitops-split-brief-20260923.md`, for `1.0.0_SA_CTO~Z`. Companion to RCN-0014.

**Finding in one line:** "the same structure as the portal" gives a nested repo containment and separation but only part
of the tooling. The portal is a nested clone plus a gitlink, with `.gitmodules` at 0 bytes. It has 0 active git hooks,
so no parent git gate grades its commits. The lane hook, if installed there without a lane file, would EXIT 1 on
every commit, because block mode is its default. (This line first said it "WARNs and skips", read from one line
short of the mode branch; corrected on `1.0.0_SA_CTO~Z`'s ruling, msg 25107, and re-verified at the bytes.) Both EC2 deploy guards read the
parent's git, so a nested source would pass the clean-tree check over uncommitted edits and record the wrong commit.
The brief recommends a real submodule and names 24 items that make it "tooled" as well. **Status: DELIVERED as CTO
intake. Nothing created, moved or dispatched. Local reads only -- no GitHub read, nothing deployed.**

## RCN-0017 -- Report 2: the canonical flow and the closer flow, a FAST mode, `/closer-drive`, and the switch

**Date:** 2026-09-24. **Produced under:** `4.0.0_SA_CRO~A`, laptop. **Commissioned:** Andrew-direct at this terminal
~14:3xZ; verbatim record `deliverables/ANDREW_DIRECT_20260924_143xZ_REPORT2_CANONICAL_AND_CLOSER_FLOWS_AND_THE_SWITCH.md`.
**Package:** `deliverables/REPORT2_CANONICAL_AND_CLOSER_FLOWS_SPEED_MODE_AND_SWITCH_20260924.md`, for `1.0.0_SA_CTO`.
Companion to report 1 (`deliverables/BRIEF_CANONICAL_FLOW_SPEED_CLOSER_FLOW_SKILLS_PARITY_20260923.md`) and to
`4.0.0_SA_CRO~B`'s RCN-0016 (report 3, process debt), which it cites instead of re-measuring.

**Finding in one line:** canonical is slow in execution, not in hand-offs (the slug-to-next-cut takes about 30 minutes).
The rounds' 3-6 hours go to a fabric-wide usage stall, chains queued on shared files, check defects in 9 of 29 orders,
and merge lag. The orders are light-to-moderate: median about 220 product lines inside an 11.8 KB order that is a
quarter build instruction. Workers already run Sonnet 5 at high effort (68 of 68 commits), and the spine's "Opus" line
is stale. One screenshot of the real page caught what every fixture check passed. The canonical and closer seats edited
the same 5 files of one page in the same 12 hours. Proposal: one driver per project chosen by a timed MODE LEASE,
FAST (`/closer-drive`, Andrew present) or FULL (`/canonical-drive`, the fail-closed default), plus seven smaller cuts.
**Status: DELIVERED as CTO intake -- proposals only; nothing dispatched, no skill, spine or hook edited; six calls at
Andrew. Repo, git and read-only broker reads only; no AWS, no vendor.**

## RCN-0016 -- Report 3: process architecture, verification and process bureaucracy

**Date:** 2026-09-24. **Produced under:** `4.0.0_SA_CRO~B`, laptop. **Commissioned:** Andrew-direct at the `~B` terminal
~14:46Z; verbatim record `deliverables/ANDREW_DIRECT_20260924_144xZ_PROCESS_ARCHITECTURE_BRIEF.md` @2b16316b41.
**Package:** `docs/briefs/process-architecture-verification-bureaucracy-brief-20260924.md`; re-runnable census in
`scripts/process_census/`. Companion to RCN-0017 (report 2, flow mechanics), whose section 4.4 items it cites.

**Finding in one line:** commits that touch product code fell from 16-25% of the workspace's output in June to 6-9% in
September while volume rose to ~570 a day; the cause is structural (the spine re-measures one fact 3-4 times, a PRD
wording edit re-opens a two-seat sign-off the gate still enforces, every row blocks the close, the CTO routes every
ruling), so Rule 22 cannot fix it by being read. Proposal: a `<risk>` class on every order that decides mechanically
which limbs engage, four waves of gate fixes and deletions, byte budgets on auto-loaded carriers, and one weekly
efficiency number. RAVC: keep its three evidence rules, delete the rest.
**Status: DELIVERED -- proposals only; nothing dispatched; no law, gate, skill or memory edited. Repo, git, read-only
broker and audit-log reads only; no AWS, no vendor.**
