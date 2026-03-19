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
| `ADVI_CLSPT2` | `ADVI` | BD Classification Phase 2 | Phase 2: ALL CODE COMPLETE + DEPLOYED (2026-03-19). partners-api-v1.7.0 live. ETFClassifier active in _classify_holding(). classify_bd_securities.py + detect_new_securities.py committed. [*runtime: DS WS1-WS3 produced by runtime agent with manual syntax fixes; DT WS4 deploy sequence runtime-executed, source-map manual restore] | 0.4, 0.6 | AE: run classify_bd_securities.py on EC2 to enrich bd-securities beyond 116 items. | BD Classification Phase 2 PRD |
| `ADVI_BKSCMP` | `ADVI` | Books Tab Per-Class Composition Artifacts | Phase 1: 4 task orders issued (2026-03-19). DS writing script 12 + Lambda v2.8. RD parallel (types + holdings adapter). DT gates on DS WS2. AE gates on DS WS1. | 0.4, 0.6 | DS BKSCMP.001 (script 12 + Lambda routes). | Books Composition PRD |
| `ADVI_MVP318` | `ADVI` | Advisor Intelligence MVP Finalization | Phase 3: WS1-WS5 COMPLETE. bd-v2.19.2, partners-api-v1.4.0 deployed. WS6 (portal DEV->PROD merge) is the only remaining gate. | 0.4, 0.6 | DT: portal DEV->PROD merge + deploy-manual.sh. | ADVI MVP Finalization PRD |
| `DRFR_PTMCH` | `DRFR` | Portal Time Machine | P1-P5 COMPLETE (all backend + frontend delivered). P6a COMPLETE. Portal DEV not yet pushed/merged to PROD. P6b-d pending. | 0.3, 0.5 | Portal DEV push + PROD merge. P6b-d implementation. | Portal Time Machine PRD, Canon Interlock PRD |
| `ADVI_MVPLVL` | `ADVI` | Advisor Intelligence MVP Polish | ConsolidatedOverviewPanel live on portal DEV (62143e7). Two new DS task orders pending: MVPLVL.007 (advisor timeseries endpoints for L2 quarterly bar) + MVPLVL.008 (open_lots field names). DE ADVI_MVP318 WS5 (chart windows) also pending before portal merge. | 0.4, 0.6 | DS MVPLVL.007+.008 + MVP318 WS5 (DE chart windows) + DT portal DEV->PROD merge. | ADVI MVP Polish PRD |
| `ADVI_ADVTV2` | `ADVI` | ADV v2 — Architect Attribution | DS committed (8ef1da9b). EC2 deploy done (72c03d2a). DT gold layer run + verification pending. | 0.4 | DT: confirm FULL gold run complete, rel_architect_lookup verified (task order 002). | — |
| `ADVI_MIXV2` | `ADVI` | Asset Mix View V2 | DS 001+002 COMPLETE. DE 005 COMPLETE (portal DEV). DT 004 COMPLETE (partners-api-v1.3.0). AE 003 pending (06b EC2 + gold run). Portal DEV->PROD merge pending. | 0.4, 0.6 | AE 003: 06b EC2 deploy + gold run. DT portal DEV->PROD merge (shared gate with ADVI_MVPLVL). | Asset Mix View V2 PRD |

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
| `ADVI_CLSUNI` | `ADVI` | BD Securities Classification Unification | 2026-03-19 | All WS deployed: shared-infra-v1.5.0 (bd-securities table + IAM), partners-api-v1.6.0 (etf_classifier.py in Lambda). Portal taxonomy (types.ts, ClientsTab.tsx) on portal DEV f0d9d01. 116 items seeded. [*runtime: AE_CloudOps WS1, DS WS2, RD WS7, DT WS8 — partial corrections applied by CTO. ~36% unedited.] |
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
