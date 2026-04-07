# Project Registry

All active and completed projects. Each project has a project code, a macro code,
a JSON file, and a PRD set.

**Project code format:** `{MACRO}_{6CHAR}` (e.g., `ADVI_V1VERS`)
**Thread serials:** `{PROJECT_CODE}-{NNN}` (e.g., `ADVI_YANGV2-001`)
**Project JSON:** `org/projects/{PROJECT_CODE}.json`

Multiple projects can share the same macro code. The macro code identifies
the surface area; the project code identifies the specific initiative.

---

## Active Projects

| Project Code | Macro | Project Name | Phase | Pods | Blocking | PRDs |
|---|---|---|---|---|---|---|
| `DEBT_1STRUN` | `DEBT` | First Technical Debt Sweep | ON HOLD. P1: 21/27 scans. P2: .002-.004 done, .005 staged. | 0.1-0.4, 0.5-0.7 | On hold per Andrew. | — |
| `ADVI_REBORN` | `ADVI` | Advisor Intelligence Full Integration | WS1: E2E pipeline audit (DS+AE+DT+DE). WS2: Fee efficiency views — Option A (DS->DE->RD->DT). WS3: Books tab data freshness. WS4: Employee leaderboard. Absorbs NNAFEE. | 0.4, 0.6 | Pattern 0 thread -> DS .001 inventory -> parallel audit + fee work. | ADVI_REBORN_PRD.md, ADVI_NNAFEE_FEE_EFFICIENCY_VIEWS.md |
| `ADHC_DESIGN` | `ADHC` | Portal Design Normalization | Decomposed: 12 RD TOs STAGED. .001 Attribution critical path (holdings-shared.tsx). .002-.012 parallel. Phase 3 CTO. | 0.1-0.4 | .001 before .002. All others parallel. | PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md |
| `ADHC_TMSTEL` | `ADHC` | Teams Telemetry MCP Server | P0: PRD complete. Awaiting Azure AD app registration + COO decomposition. | 0.7 | Azure AD app registration (Andrew/IT). COO TOs. | ADHC_TMSTEL_PRD.md |
---

---

## Runtime Attribution Legend

`[*runtime]` in any Phase or Notes column means one or more workstreams were executed
by the ka_testing Docker runtime (org/ka_testing). Code produced by runtime agents
was verified and corrected by CTO before deployment but originated autonomously.
Never treat `[*runtime]` deliverables as fully human-reviewed without reading the
session log. Performance baseline: CLSUNI ~36% unedited, CLSPT2 ~67% unedited.

---

## Completed / Archived Projects

| Project Code | Macro | Project Name | Completed | Notes |
|---|---|---|---|---|
| `ADVI_NNAFEE` | `ADVI` | Advisor NNA & Fee Efficiency Dashboard | 2026-04-07 | Absorbed into ADVI_REBORN as WS2. Original 6 TOs superseded by REBORN .005-.008 + .011-.013. |
| `ADVI_GLDRST` | `ADVI` | BD Gold Layer S3 Restructure + Operational Readiness | 2026-04-07 | 19/22 TOs complete. Restructure fully landed (new S3 paths, A_00-E_19 taxonomy, gold_dispatch.sh). .014 validated by production. .010 old key cleanup deferred to AE ad-hoc. .019 Schwab RPS moved to backlog. |
| `ADVI_GLDOPS` | `ADVI` | Gold Layer Operations: Data Freshness + Market Growth | 2026-04-07 | All TOs complete. Superseded by operational state. Canonical stack (05 swap, 01b fees, 08c, 11a) shipped. Scripts renamed A_00-C_04. silver/fees delivered. |
| `ETFS_SECIDX` | `ETFS` | ETF Securities & Index Inventory Assessment | 2026-04-07 | P0 complete. 102 securities, 138 portal tickers audited, D4 recommendations delivered. 97.1% Massive API coverage. |
| `TAXX_TXSTRT` | `TAXX` | Tax SMA Trade Allocation Strategy | 2026-04-07 | P0 complete. DS gap analysis delivered (v1+v2 trade allocator review). |
| `AUTH_TFIMPT` | `AUTH` | Auth Infrastructure Terraform Import | 2026-04-06 | 3/3 TOs complete. CloudFront distribution imported, DynamoDB/SES/secrets imported (portal-auth-v1.11.0), shared-infra role ownership resolved (shared-infra-v1.6.0). |
| `ADVI_ANONYM` | `ADVI` | Advisor Intelligence PII Pseudonymization + RBAC | 2026-04-06 | P1-P5 complete. Pseudonymization, RBAC, Lambda PII handlers, authorizer passthrough, api/shared->scoped migration. 16 TOs total. PROD de62fde. JWT tier + partner migration deferred. |
| `ADHC_HISTRY` | `ADHC` | BD Transaction History Forensic Investigation | 2026-04-06 | All 8 TOs complete. AUA $1,582M (0.3% from silver). Phantom fix deployed. NNA rearch under GLDRST.017. Remaining: BD vendor ($259M) + Pathfinder weights (Andrew external). |
| `ADVI_TICKID` | `ADVI` | Ticker Resolution + Holdings Enrichment | 2026-03-26 | All 8 TOs complete (.001-.008). P1 resolution table + enrichment + DynamoDB backfill + detect enhancement. P2 feedback bridge + sweep-unlisted + silver AUA override + bond classifier. AE execution via combined GLDRST.002 gold run. |
| `ADVI_PRICES` | `ADVI` | BD Canonical Pricing and Valuation Reconciliation | 2026-03-27 | All 9 task orders complete. Phantom fix ($296M->-$57.7M). 32 ticker corrections. Backfill +143K rows. Canonical 16.6% yahoo. Scheduler fix deployed. AE .005 MBS fix + silver rebuild (gap 3.72%->0.169%). Post-completion (03-28): 754 YF_OVERRIDES, realized sell injection (51K phantoms), net gap +$8.5M (+0.53%). Awaiting gold rebuild. |
| `ADVI_GLDPRE` | `ADVI` | Gold Layer Pre-Run (4-Class + AUA Reconciliation) | 2026-03-25 | All task orders complete. Gold reruns verified. Portal-v2.1.17 live (52-commit merge 03-23). AUA recon: -3.6% structural. 4-class taxonomy end-to-end. |
| `ADVI_CLSPT2` | `ADVI` | BD Classification Phase 2 | 2026-03-25 | All 3 task orders complete. 3,855 securities classified. ETFClassifier in scripts 06b+12. Portal PROD deployed with taxonomy types. [*runtime ~67% unedited] |
| `ADVI_BKSCMP` | `ADVI` | Books Tab Per-Class Composition Artifacts | 2026-03-25 | All 4 task orders complete. Script 12 deployed to S3, gold run verified (03-25 incremental). partners-api-v1.5.0 deployed. Portal DEV->PROD merge tracked under GLDPRE.006. |
| `ADVI_MVP318` | `ADVI` | Advisor Intelligence MVP Finalization | 2026-03-20 | WS1-WS5 complete. bd-v2.19.0-v2.19.2, partners-api-v1.4.0 deployed. Gold rerun subsumed by GLDPRE. |
| `ADVI_MVPLVL` | `ADVI` | Advisor Intelligence MVP Polish | 2026-03-26 | Phase 1 (.001-.009) complete 03-20. Reopened 03-26 for .010 (L2 composition, Mix toggle, tax ghost exclusion). DS+DE .010 delivered. AE .010 gold rerun subsumed by GLDRST.002. Closed. |
| `ADVI_ADVTV2` | `ADVI` | ADV v2 — Architect Attribution | 2026-03-20 | DS 001 committed (8ef1da9b). EC2 deployed (72c03d2a). Gold rerun subsumed by GLDPRE. |
| `ADVI_MIXV2` | `ADVI` | Asset Mix View V2 | 2026-03-20 | All DS/DE/DT work done. AE 003 gold rerun subsumed by GLDPRE. partners-api-v1.3.0 deployed. |
| `DRFR_PTMCH` | `DRFR` | Portal Time Machine | 2026-03-20 | P1-P5 deployed (yang-v2.3.1, bd-v2.18.2, news-v2.7.0, data-refresh-v2.2.0). P6a deployed. P6b-d deprecated. |
| `ADVI_CLSUNI` | `ADVI` | BD Securities Classification Unification | 2026-03-19 | All WS deployed: shared-infra-v1.5.0 (bd-securities table + IAM), partners-api-v1.6.0 (etf_classifier.py in Lambda). Portal taxonomy (types.ts, ClientsTab.tsx) on portal DEV f0d9d01. 116 items seeded. [*runtime ~36% unedited.] |
| `ADVI_V1VERS` | `ADVI` | AdvisorIntelligence V1 Completion | 2026-03-05 | 8/8 task orders verified complete |
| `ADVI_YANGV2` | `ADVI` | AdvisorIntelligence Yang Feedback V2 | 2026-03-06 | All task orders delivered. Y14 deferred to 49FNV3. |
| `ADVI_NNAVAR` | `ADVI` | NNA Variance Optimization | 2026-03-09 | Investigation complete. Gap explained (Holding MV withdrawn = correct behavior). Scripts 05/05b deployed to S3. Rebuild deferred pending ADVI_49FNV3. |
| `ADVI_AUAVAR` | `ADVI` | AUA Variance Analysis | 2026-03-09 | Full $73.6M gap attributed. BKF fix deployed. Post-rebuild accuracy 99.1%. Rebuild deferred pending ADVI_49FNV3. |
| `ADHC_GPTCST` | `ADHC` | GPT Cost Audit and Optimization | 2026-03-10 | Caller inventory complete, Lambda optimizations deployed (news-v2.5.0), keyword cache fixed (news-v2.6.0 + market-overview-v1.6.0). |
| `ADVI_SNPLBK` | `ADVI` | Snapshot Lookback Regression Fix | 2026-03-10 | Frontend granularity mismatch diagnosed and fixed. Backend data confirmed intact. |
| `PFMG_VISPOL` | `PFMG` | Trade Engine Visual Polish | 2026-03-10 | All 13 visual polish items delivered and approved. |
| `SSCN_PORTAL` | `SSCN` | Security Scanner Portal Page | 2026-03-10 | Infra deployed (security-scanner-v1.0.0), portal DEV live, end-to-end validated. |
| `ADVI_APISCP` | `ADVI` | Scoped API Multi-Partner Routing Architecture | 2026-03-10 | Router v7 live. All Opal users patched. Firm picker gated. E2E verified. |
| `MDLP_WYNCHT` | `MDLP` | Model Portfolio Benchmark Screenshot Facsimile | 2026-03-11 | 4 HTML pages live on S3 (opal-313476888478-wyncht). PPTX delivered. All commits on CLOUD. |
| `ADVI_PSCFIX` | `ADVI` | AUA Certification and Static Lifecycle Definition | 2026-03-12 | All 5 task orders complete: A1 (cert script), A2 (publisher ea832f51+c3c8d072), A3 (script09 cert), B1 (portal schema), DT1 (bd-v2.18.3+v2.18.4). DE integration validated. |
| `ADHC_MKOVFX` | `ADHC` | Market Overview KI + Fear & Greed Fix | 2026-03-12 | KI bug fixed (news-v2.7.1). Fear & greed backend healthy. Root cause: GPT returning string instead of dict for signal_conflict. |
| `ADVI_49FNV3` | `ADVI` | AdvisorIntelligence 49Financial V3 | 2026-03-12 | All task orders complete: F1-F7 fixes, N1-N2 Books tab, thread 003/003b redesign, .007 (resolved by PSCFIX), .008 (05c deployed, 33-date backfill, root cause documented). |

---

## Adding a new project

1. Pick the macro code from `org/projects/MACRO_CODES.md` (or add one if the surface area isn't listed)
2. Choose a 6-char project suffix that abbreviates the initiative name
3. Project code = `{MACRO}_{6CHAR}`
4. Create `org/projects/{PROJECT_CODE}.json` (copy any existing project JSON as template)
5. Required fields: `project_code`, `macro_code`, `name`, `description`, `prds` (array),
   `status`, `phase`, `pods`, `blocking`, `created`, `thread_counter`, `threads`
6. Add a row to the Active Projects table above
7. Commit with: `org(1.0.0_SA_CTO): register project {PROJECT_CODE}`

## Closing a project

1. Set `status` to `"complete"` in the JSON
2. Move the row from Active to Completed/Archived in this table
3. PRDs stay in `docs/architecture/` -- do not archive active project PRDs

## Thread serial format

`{PROJECT_CODE}-{NNN}` where NNN is zero-padded to 3 digits.
Thread folder: `org/threads/{PROJECT_CODE}-{NNN}-{slug}/`
Receipt in agent folder: `{PROJECT_CODE}-{NNN}-{slug}_{other_serials}.md`

When creating a thread for a project, pass `--project {PROJECT_CODE}` to `create-thread.sh`.
The script auto-assigns the next serial and updates the project JSON.

## PRD location

All active PRDs live in `docs/architecture/`. Pre-org-system (v1 era) architecture docs
are archived to `docs/architecture/archive/` and are not referenced by any active project.
