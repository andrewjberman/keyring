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
| `ADVI_GLDPRE` | `ADVI` | Gold Layer Pre-Run (4-Class + AUA Reconciliation) | Phase 3: WS1+WS2+WS3 code COMPLETE. Lambda deployed (partners-api-v1.8.0). Portal DEV fixes committed (types.ts + 4-class + ClientsTab.tsx). Phase 4 (full gold rerun) pending AE execution. | 0.4, 0.6 | AE GLDPRE.005 Phase 4 (full gold rerun). DT GLDPRE.006 (portal merge, gated on gold rerun). | GLDPRE PRD |
| `ADVI_BKSCMP` | `ADVI` | Books Tab Per-Class Composition Artifacts | DS .001 COMPLETE. RD .002 COMPLETE (6266d17). DT .003 COMPLETE (partners-api-v1.5.0). AE .004: script 12 S3 upload folded into GLDPRE.005 Phase 2. | 0.4, 0.6 | AE: script 12 upload + gold run validation (via GLDPRE.005). | Books Composition PRD |
| `ADVI_CLSPT2` | `ADVI` | BD Classification Phase 2 | DS .001 COMPLETE (OpenAI impl). AE .002 COMPLETE (3,855 securities classified, up from 116). DS .003 COMPLETE (script 12 ETFClassifier migration). [*runtime] | 0.4, 0.6 | AE: gold rerun to validate classification parity. | BD Classification Phase 2 PRD |
| `ADVI_GLDRST` | `ADVI` | BD Gold Layer S3 Restructure | Phase 0: CTO approved (2026-03-19). DS Condition 2 resolved (Option B). | 0.4, 0.6, 0.7 | COO task order issuance. | Gold Layer Restructure Proposal |

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
| `ADVI_MVP318` | `ADVI` | Advisor Intelligence MVP Finalization | 2026-03-20 | WS1-WS5 complete. bd-v2.19.0-v2.19.2, partners-api-v1.4.0 deployed. Gold rerun subsumed by GLDPRE. |
| `ADVI_MVPLVL` | `ADVI` | Advisor Intelligence MVP Polish | 2026-03-20 | All task orders complete (.007 delivered under MVP318.001, .008 at 14b3be3d). 5 threads complete. |
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
