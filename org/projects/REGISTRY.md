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
| `ADVI_ROLLUP` | `ADVI` | ADVI Master Rollup — Post-Presentation Edit Queue | **33/41 TOs complete. W0/W1/W4/W5 structurally COMPLETE.** Pending: CP-DS1 (B_01 cusip/RPS cutover) + SL-P1 (sleeve shadow). Staged: CP-VETO-AUTH, CP-WP5, RA-P1c, SL-P2, SL-P3, CP-MAP. **2026-04-17 B_01 cap saga shipped:** bond-100x convention fix `d45fc0dc` + share-class ticker `178d0cce` + tiered cap `cb6d78e2` (Run 11 $3.587B -> $1.758B; firm post-cap $1,646.4M vs silver $1,694.6M = -2.9% residual; 916 bond lots repriced; market_value_uncapped col shipped). **C_08 silent-wrongness recovery (Andrew flagged):** quick-patch `9e537f9f` then real fix `cd177553` (CANONICAL_NNA_ATOMIC_PREFIX -> CANONICAL_NNA_PREFIX swap on C_08+D_00b+D_01+D_04 per DS decision matrix; D_04 'Unknown' state silent-fill caught — BDPL_NNA.S1 schema-alignment TO drafted). **CP-DS1 in-flight stack:** PIVOT 5 (`7e57576f`) + PIVOT 6 (`c693d5a3`->`d39c4dff`) + Gate 3 silent-close (`cd00ff2c`) + Gate 1 cusip-keyed veto fix (`c4ebde9a`) + runtime CUSIP enrichment (`f5f19e77`) + (account_id, cusip) re-key (`1db831aa`) + snapshot_date from latest silver (`ec2c1efc`). **C_03 phantom outflow** fix (`85bb2daa`). **D_03 step 6b** composition.json for non-architect (`09ac915b`). **Schwab ULN -> silver/ULN/** ingestion (`6c80c5ed`). CP-AE1 backfill audit 1,520 partitions (`0830bae7`). bd-gold-layer-runner deploy `cb6d78e2` (`88fd8d1c`). DH-2 wrapper fix `8e3176a1` verified Run 11. AE SSM d83a1d11 (C_08->D_04 re-run on bd-gold-qa-runner) fired late 2026-04-17. RPS feed dead since 2026-04-08 — tactical compensation via tiered cap. | 0.4, 0.6, 0.7 | (1) CP-DS1 stabilization — final cap target $1.66B (cohort <50 per `965d81ad`); awaiting Andrew sign-off on cap-timing-rule disposition (CTO MCP 20260417T174410Z). (2) AE SSM d83a1d11 completion report. (3) Weekend nightly verification (Fri->Mon). (4) SL-P1 shadow first-fire evidence. (5) DS BDPL_NNA.S1 schema-alignment TO draft. (6) Asset_class join hardening TO. (7) Top Positions 'Opal models only' filter TO. SL-P2/P3 staged on SL-P1. AE Wave 3 B-series post-rerun validator evidence. ADVI_PROFAU.006 PROD D_04 for W3 B1 rerun. | ADVI_ROLLUP.md (+ absorbed child PRDs) + INCREMENTAL_RUNS_DESIGN.md |
| `COMP_LEARNS` | `COMP` | Autoresearch-Style Compiler Bootstrap Pipeline | Phase 2 — architectural expansion. New PRD `COMP_LEARNS_ARCHITECTURE.md` shipped v1/v2/v3 2026-04-16 (`eb3b01fd`/`c963ced5`/`8df31d86`) formalizing 6-concern structural-inference system. Wave .011-.019 v3 sweep in flight on COO~B — 7/11 swept at midday; .015/.016/.017/.021 pending. COO lane split locked (`f168c172`): COMP_LEARNS routes to `2.0.0_SA_COO~B`, ADVI_ROLLUP to base COO. ADVI_49EXEC.003 anthropic-sdk layer (`c0a00bcc`) clears .015 Phase 2 external block. | 0.4, 0.7 | COO~B finish v3 sweep + operator + validator + MCP report-back; CTO .016 httpx gold authoring (Steps 2-7); crash/concurrent/kill dry-run tests on Linux. | COMP_LEARNS_PILOT.md + COMP_LEARNS_ARCHITECTURE.md |
| `ADHC_ROUTER` | `ADHC` | Compiler Feature Routing / Corpus-Driven Test Pass | Phase 1 COMPLETE 2026-04-15 — all 4 TOs closed. 4 compiler patches shipped (`d1d6920b` T1 reverse-edge regression, `70c8399d` T2 AWS_UNREACHABLE, `614d4c28` T3 empty-vs-broken footer, `3c921e08` T4 proposal E pass-through). Phase 2 backlog 10 items post-2026-04-21 joint audit (T3 findings + AE 0.6 feedback + external-Lambda comp-* invisibility + MSYS URL path-mangling). | 0.4 | Phase 2 pickup when lanes idle. Priority: .sh indexing highest (PROD-incident root cause); syntax warning is free. | docs/briefs/compiler-tools-engineer-onboarding-2026-04-15.md |
| `ADVI_49EXEC` | `ADVI` | Advisor Profile AI Executive Summary v1 | Phase 0 — PRD shipped 2026-04-15 (`docs/architecture/ADVI_49EXEC.md`). 7 TOs scoped: DS template-library + LLM-prose + leaderboard prior-week rotation; AE anthropic-sdk layer; DT generator-lambda terraform + EventBridge wiring; DE SummaryCard rebrand to "Executive Summary" + bullets-with-icons. Nightly batch (Lambda + Anthropic Claude Sonnet 4.6) → S3 `platinum/advisors/{id}/exec_summary.json` → existing CF `*.json -> S3` behavior + shared-advisor-router scoping. v2 admin text-to-SQL + v3 SFDC outbound deferred. New `exec-summary` micro-pipeline. | 0.4, 0.7 | COO TO authoring against PRD compiler-mandate matrix. AE 0.6 confirmation of gold-chain-complete EventBridge signal format (gates TO 7). comp-pii audit on platinum/advisors/* + platinum/leaderboards/* (gates TO 1 LLM prompt). | ADVI_49EXEC.md |
| `ADHC_DSFLOW` | `ADHC` | DS Gold-Script Commit→Deploy Flow Hardening | **Phase 0 — PRD v1 shipped 2026-04-21** (`docs/architecture/ADHC_DSFLOW.md`). Response to 2 latent-bug PROD crashes in 2 days (D_02 035352c3 KeyError + B_00 081223b5 NameError). Scope: mandatory pre-commit gate (`py_compile` + 25-line AST undefined-name scan catching the 081223b5 class — verified statically) + enforce DS end-to-end deploy ownership (committed-ref S3 upload, QA-runner SSM, `comp-pipescript deployed` MATCH) per existing `feedback_ds_commits_ae_deploys.md` which has not been consistently executed (yesterday DT uploaded all 4 scripts per Andrew override, 4+h after DS commits). 3 TOs scoped: DS precommit-gate tool, COO org-docs updates (CLAUDE.md + XXX.md + DS README + memory), passive training-run on next gold-script commit. DT/AE infra + PROD + multi-pipeline authority unchanged. Pilot scope Pod 0.4; cross-pod expansion follow-up. | 0.4, 2.0 | COO TO authoring. DS IAM verification on `s3:PutObject opal-bd-gold-code/gold/*` (AE 0.7 micro-TO if gap). Andrew answers to §11 open questions (git hook vs startup reminder; historical backfill; contract-drift follow-up; cross-pod expansion). | ADHC_DSFLOW.md |
| `TRSB_TFIMPT` | `TRSB` | Trade Pipeline Terraform Import + Code Reclamation | **Phase 0 — PRD v1 shipped 2026-04-21** (`docs/architecture/TRSB_TFIMPT.md`). Three P1 integrity gaps on the trade-pipeline subsystem (console-managed `opal-trade-submissions` DDB + 11 Lambdas on external code + API GW not in TF). Three-wave scope: W1 DDB import + IAM ARN fix (target tag `trade-pipeline-v1.3.0`), W2 Lambda code reclamation (v1.4.0), W3 API GW import + route-trace wiring (v1.5.0). AE 0.7 primary; DT 0.3 paired review on W2 authorizer triplet. Pattern inheritance from AUTH_TFIMPT + CDRS_TFIMPT. Compiler tools returned "no match" for every trade Lambda / route — invisibility is itself PRD evidence (documented in §2 Compiler Tools). | 0.7, 0.3 | COO TO authoring against PRD compiler_tools_mandate triads. Andrew answers to §8 open questions (sequencing pressure, W2 scope for recon quartet, partner expansion outlook, W2 smoke-test trade fixture). | TRSB_TFIMPT.md |
| `ADVI_STAUDT` | `ADVI` | ADVI Portal State Audit — Wed→Mon Reconstruction | Phase 2: FIX wave PROD-shipped + BD-anchor pivot. Layers A/B/C COMPLETE (`0d34f025`/`fd857154`/`b687ff47`). FIX wave PROD via SSM `3e06059f` 2026-04-20 19:49Z clean — FIX2/FIX3A/FIX5/FIX6/FIX7 complete; FIX3B cancelled (Phase 0 parquet verify); INV4 deferred. **User-visible win: firm NNA chart $330M→$1.649B.** Watchdog incident RCA closed (`9a700351`+`d9a419aa`, PROD live-patch `910c0fbb`); Q4 coverage test + Q6 process-tagging staged for AE this week. BFIX1+BFIX2 code shipped (`081223b5`) awaiting DT upload + combined PROD. **BFIX3/BFIX4 CANCELLED** per Andrew 2026-04-20 PM "we don't track that" decision — 654 accts / $52M structurally BD-excluded (SLATs/DAFs/HSAs/corp entities), injecting black-box AUA worse than omitting. CTO brief `docs/briefs/aua_active_account_filter_redesign.md` proposes multi-signal active detector to recover ~$41M of currently-dropped active cohort. Post-fix firm AUA -284bps → -160bps vs BD silver (~$20.8M BFIX1+2 recovery). | 0.4, 0.6, 0.7 | Andrew review of CTO AUA active-filter brief before COO decomposition. DT upload of `081223b5` + qa-runner --group ABCD + combined PROD. KPI/CONS Phase 1 pending COO GO. B_00 mini-PRD (untracked cohort documentation). AE Q4 watchdog coverage test + Q6 process-tagging. | ADVI_STAUDT.md + docs/briefs/aua_active_account_filter_redesign.md |

---

## Inactive / On Hold

| Project Code | Macro | Project Name | Held Since | Reason |
|---|---|---|---|---|
| `ADHC_TMSTEL` | `ADHC` | Teams Telemetry MCP Server | 2026-04-13 | Awaiting Azure AD app registration (Andrew/IT). Reactivate when credentials are available. |

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
| `ADHC_DESIGN` | `ADHC` | Portal Design Normalization | 2026-04-21 | Closed at 28/32 effective (87.5%). All 4 pods (0.1/0.2/0.3/0.4) Phase 2 complete. 8 DE TOs + 20 RD TOs shipped. Pod 0.4 wrap `3096108` (.028 RechartsTooltip→DataTooltip + lint guard) + `f3274f3` (.032 react-hooks cleanup). 4 orphan TOs CANCELLED per Andrew 5-item walkthrough 2026-04-21 PM (CTO session log `org/tier1_exec/1.0.0_SA_CTO/logs/2026-04-21/session36_five_item_decisions.md` §4, commit `0a37d545`): Attribution .001/.015/.024 (0.2.2_RD_Attribution never spawned) + Valuation .007 (0.2.4_RD_Valuation never spawned). Attribution + Valuation are legacy low-traffic ADVI sibling surfaces with no product driver; no dedicated RD agents justified. 16 residual react-hooks warnings deferred as standing backlog .033 (low priority). |
| `ADVI_ROLGAT` | `ADVI` | Advisor Role Gating + Data Tier Transmission | 2026-04-17 | All 3 TOs complete. DT1 portal-auth-v1.13.0 (`8ce0bbca`) + partners-api-v1.16.1 (`3a186703`): advisorRole JWT claim + 4-role tier enforcement at auth-validator-edge v12 + shared-advisor-router v13 + opal-partners-data v2.11 with implementor payload strip + 4-row 49financial backfill + 21/21 smoke PASS. DE1 portal DEV `c0b1dae`: Claims advisorRole + 5 helpers + AdvisorIntelligence tab restructure + devBypass role picker. RD1 drill gates + role constitutions. L1 scope fixup `295c617b`. Permission groups rubric + click matrix shipped (`53c43049` + `0de257e0`). Portal-v2.1.58 PROD ship 2026-04-20 `c7a7d11e` includes DE1 for production. Pod-driven (DE 0.4.0 ran point per Andrew). Registry row moved 2026-04-21 joint CTO+COO audit (was missed in earlier sweep). |
| `ADVI_PROFAU` | `ADVI` | Advisor Profile + Book Data Gap Audit | 2026-04-21 | All 6 authored TOs complete 2026-04-14 (.001/.003/.004/.005/.006/.007 — .002 never authored, 6 of 6 expected against 6-gap PRD). Portal shipped in W4 batch (portal-v2.1.42 → portal-v2.1.58 `c7a7d11e`). D_02 per-role canonical NNA (`d51e44ef`) rode 2026-04-15 full A→D rerun + nightly cycles. Final mechanical deploy (PROFAU.006 D_04 gold redeploy) lands automatically with `cf5bd5ad` chain-full recovery run 2026-04-21. Closed per Andrew done-or-superseded sweep 2026-04-21. |
| `ADVI_INCMTL` | `ADVI` | Gold Pipeline True Incremental Processing | 2026-04-21 | COMPLETE-AS-SUPERSEDED. Original P0 briefing `GOLD_PIPELINE_INCREMENTAL_BRIEFING.md` (2026-04-09). Scope absorbed into ADVI_ROLLUP: **IN-1** feasibility-survey + **IN-2** design-PRD + 3 IN-2.W0 sub-TOs (W0.002 watermark-helper-lib, W0.003 comp-incrparity-tool, W0.004 weekly-parity-eventbridge) — all COMPLETE. Watermark infra + parity tool + EventBridge weekly monitor all shipped. Future incremental-pipeline work = new TOs on ADVI_ROLLUP or successor. Closed per Andrew done-or-superseded sweep 2026-04-21. |
| `CDRS_TFIMPT` | `CDRS` | Cloud Resources Terraform Import — CloudFront + Identity Tables | 2026-04-15 | All 7 TOs complete. Phase 1: 5 CloudFront imports (analytics-dashboard-v1.0.0, trade-pipeline-v1.1.0/v1.2.0, market-overview-v1.8.0, public-api-cdn-v1.0.0). Phase 2: .006 opal-users-v2 DynamoDB import (20acf679, shared-infra-v1.7.0) + .007 partner-firm TF module + shared-lib + auth-handler generalization (7e673244, partner-firms-v1.0.0). Phase 0 firmRole framework shipped DT-side prior (portal-v2.1.51, auth Lambda e7b78cf9). AE 0.7 + DT 0.4 lane. Post-sprint AE follow-ups (JWT drift trade-pipeline, market-data-v2 bucket_policy) carried as standing backlog. |
| `ADVI_FNTEND` | `ADVI` | ADVI Full-Surface Frontend Correctness | 2026-04-15 | Merged into `ADVI_ROLLUP` as Wave 3. At merge: FE B1-B6/B8 DEV, D7 complete, DS B1-B8 code-shipped awaiting nightly gold artifact. TO filenames preserved. |
| `BDPL_CNPRCS` | `BDPL` | BD Canonical Prices + Classification Refactor | 2026-04-15 | Merged into `ADVI_ROLLUP` as Waves 0 + 2. At merge: tactical 3-bond held by AUA freeze, WP-4..WP-9 TOs staged on DS queue. TO filenames preserved. |
| `BDPL_ASTDIM` | `BDPL` | BD Asset Dimension Pipeline | 2026-04-15 | Merged into `ADVI_ROLLUP` as Wave 1. At merge: W1-W6 complete (`bd-v2.24.0`), W7 scheduled-run verification only remaining. TO filenames preserved. |
| `ADVI_NNAFEE` | `ADVI` | Advisor NNA & Fee Efficiency Dashboard | 2026-04-07 | Absorbed into ADVI_REBORN as WS2. Original 6 TOs superseded by REBORN .005-.008 + .011-.013. |
| `ADVI_GLDOPS` | `ADVI` | Gold Layer Operations: Data Freshness + Market Growth | 2026-04-07 | All TOs complete. Superseded by operational state. Canonical stack (05 swap, 01b fees, 08c, 11a) shipped. Scripts renamed A_00-C_04. silver/fees delivered. |
| `ETFS_SECIDX` | `ETFS` | ETF Securities & Index Inventory Assessment | 2026-04-07 | P0 complete. 102 securities, 138 portal tickers audited, D4 recommendations delivered. 97.1% Massive API coverage. |
| `TAXX_TXSTRT` | `TAXX` | Tax SMA Trade Allocation Strategy | 2026-04-07 | P0 complete. DS gap analysis delivered (v1+v2 trade allocator review). |
| `ADVI_OFFICE` | `ADVI` | Office Analytics for Segment Analytics | 2026-04-14 | portal-v2.1.44. OFC cohort toggle (donut, NNA, continuous AUA, bell curve, advisor list). All 9 addendum fixes shipped W6-W9. |
| `ADVI_REBORN` | `ADVI` | Advisor Intelligence Full Integration | 2026-04-14 | All waves complete. W6-003 (1d70ecaf D_00c role_combination_breakdown), W6-004 (0225d359 — existing W6-005 split-allocated approach satisfies 4-cell matrix; no new code). Four-cell matrix validated on live platinum artifact. |
| `ADVI_OTHDED` | `ADVI` | Distribution Tab Dual-Other Dedupe | 2026-04-13 | Frontend enforceTop9Other regex fix shipped `801349d`, PROD via `4575a1c`. Eliminates dual-Other in city/client drills. |
| `ADVI_HDRSPL` | `ADVI` | ADVI Header Split + PageSurfaceControl Primitive | 2026-04-13 | All 3 waves complete. Primitive `2b5b0ec`, header restructure + Segment Analytics local toggles `4cb34a2`, PROD via `4575a1c`. Reusable high-contrast control primitive established for silver-bg pages. |
| `DEBT_1STRUN` | `DEBT` | First Technical Debt Sweep | 2026-04-13 | P1 27/27 scans + P2 .002-.005 complete (HEAD 66af3ad5). 4 Dynamo + 7 IAM imported, 3 TF modules on S3 backend, EC2 manifest synced. Dynamo coverage 47→60%, IAM 49→58%. Residuals (non-blocking): 4 IAM roles flagged for ownership, ec2-auto-shutdown-enforcer drift, 9 EC2 manifest schema gaps, test-Lambda deletion runbook awaiting Andrew. |
| `ADVI_PROFIL` | `ADVI` | Advisor Profile + Book Architecture | 2026-04-11 | 10/10 TOs complete. All waves shipped, `.004c` E2E validated 8/8, `.008` DE visual test passed. Portal-v2.1.39 PROD deployed (d2e78631). Edge portal-auth-v1.11.8→v1.11.11. |
| `ADVI_49PUSH` | `ADVI` | Platinum Serving Layer -- 49F Push | 2026-04-11 | All TOs closed out. bd-v2.23.0 + partners-api-v1.15.6. Post-mortem fix stack shipped (D_00 client_city, D_00c role split, D_00c fee-bucket, D_00b TOP_N 9, D_04 GRO floor, B_00 hybrid price fill). TO_COMPILER_GATE.md published. |
| `ADVI_GLDRST` | `ADVI` | BD Gold Layer S3 Restructure (+ v2 canonical_prices) | 2026-04-11 | Original restructure 19/22. Reopened for v2: .021 shipped (source-tag + diff-before-ship, 9b4f7a77), .022 silver-prep chain in gold_dispatch (8c801923 + 29a831ae). AE cron/IAM/Job 1 deprecation carried forward as ops follow-ups. |
| `MKOV_TRENDS` | `MKOV` | Trending Topics Quality Overhaul | 2026-04-08 | All 6 TOs complete. DS scoring/images, DT Lambda deploy (news-v2.7.5), RD portal rendering, DT PROD deploy. |
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
