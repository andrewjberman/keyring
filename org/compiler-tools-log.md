---
name: Compiler Tools Rolling Log
type: aggregate
maintained_by: all agents (append after each session)
reviewed_by: 1.0.0_SA_CTO
---

# Compiler Tools Rolling Log

One entry per session, appended by the agent that ran the session.
CTO reviews this periodically to identify recurring failure patterns and new gaps.

**Format (one line per tool used):**
```
DATE | AGENT | TO | TOOL | COMMAND | RESULT | NOTE
```

Results: PASS | PARTIAL | FAIL | SKIPPED | WARN
- PASS: output was accurate and useful
- PARTIAL: output was present but incomplete or noisy
- FAIL: wrong output, crash, or silent failure
- SKIPPED: decided not to run (explain in NOTE)
- WARN: empty result with correct WARN message (valid signal)

---

## 2026-04-09 — Initial Survey (1.0.0_SA_CTO)

| Date | Agent | TO | Tool | Command | Result | Note |
|------|-------|----|------|---------|--------|------|
| 2026-04-09 | DS~A | ADVI_49PUSH various | comp-pipescript io | io D_03, D_04, D_00 | PASS | Instant, accurate, replaced 1500-line file read |
| 2026-04-09 | DS~A | ADVI_49PUSH.010 | comp-pipescript consumers | consumers D_00 | PASS | Confirmed dead code accurately |
| 2026-04-09 | DS~A | ADVI_49PUSH various | comp-platinum reverse | reverse platinum/firm/mix_summary.json | PASS | Traced to D_04 in one call |
| 2026-04-09 | DS~A | ADVI_49PUSH various | comp-blast | blast gold/artifacts/advisor_fee_efficiency.json | PASS | Confirmed single consumer |
| 2026-04-09 | DS~A | ADVI_49PUSH various | comp-trace | trace advisor_rolling_flows | FAIL->FIXED | Was exit 1; fixed to exit 0 in e50ccedf |
| 2026-04-09 | DS~A | ADVI_49PUSH various | comp-pipescript io | io B_01b | WARN->FIXED | Was silent empty; now emits WARN in e50ccedf |
| 2026-04-09 | DS~B | ADVI_49PUSH.045 | comp-pipescript io | io C_08, D_02 | PASS | FUNC annotation on keyed outputs useful |
| 2026-04-09 | DS~B | ADVI_49PUSH.045 | comp-transform fields | fields FeeEfficiencyPanel | FAIL->FIXED | r() accessor pattern; fixed in 78feb216+4670baaa |
| 2026-04-09 | DS~B | ADVI_49PUSH.045 | comp-platinum reverse | reverse platinum/firm/fee_efficiency.json | PARTIAL | Correct answer present via fallback; 5 noisy siblings |
| 2026-04-09 | DS~C | ADVI_49PUSH.018 | comp-pipescript io | io D_02, D_04 | PARTIAL | D_04 WRITES showed ? for f-strings; fixed in e50ccedf |
| 2026-04-09 | DS~C | ADVI_49PUSH.018 | comp-routes auth-map | auth-map | PASS | Perfectly accurate for auth layer mapping |
| 2026-04-09 | DS~C | ADVI_49PUSH.018 | comp-routes behaviors | behaviors | PASS | Authoritative 23-behavior listing |
| 2026-04-09 | DS~D | ADVI_49PUSH various | comp-routes | trace platinum paths | FAIL->FIXED | Stale cache; was already correct, run comp-build first |
| 2026-04-09 | DE~A | ADVI_49PUSH various | comp-transform schema-check | schema-check DistributionTab | PASS | No crash after resp_type NameError fix (e50ccedf) |
| 2026-04-09 | DE~B | ADVI_49PUSH various | comp-transform schema-check | schema-check DistributionTab | PASS | |
| 2026-04-09 | DE~C | ADVI_49PUSH various | comp-transform schema-check | schema-check DistributionTab | PASS | Note: --pending mode still needed for optional fields |
| 2026-04-09 | DE~D | ADVI_49PUSH various | comp-transform schema-check | schema-check FeeEfficiencyPanel | PASS | |

---

<!-- AGENTS: append new entries below this line, one row per tool per session -->
<!-- Do NOT edit existing entries -->
<!-- Format: | YYYY-MM-DD | {serial} | {TO_id} | {tool} | {command} | PASS/FAIL/etc | {note} | -->
| 2026-04-09 | 0.4.0_DT_ClientPlatform | ADVI_49PUSH.048 | grep | grep -n get_firm_bucket lambda_function.py | PASS | Confirmed 1 def, 2 call sites, cache dict at line 76 |
| 2026-04-09 | 0.4.0_DT_ClientPlatform | ADVI_49PUSH.048 | py_compile | python -m py_compile lambda_function.py | PASS | No syntax errors |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-build | comp-build | PASS | 68 FETCHES, 48 READS_S3, 46 TRIGGERS, 119 WRITES_S3 |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-blast | comp-blast AdvisorPublicProfile | PASS | 2 endpoints + 1 Lambda; no hidden deps |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-blast | comp-blast portal/src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx | PASS | 5 endpoints + 3 Lambda edges; drove .004b/.004c split (ownership map) |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-blast | comp-blast AdvisorsTab | PASS | 1 endpoint (getFirmLeaderboard), caching fix self-contained |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-routes | comp-routes trace getPlatinumAdvisorSummary | PASS | /api/scoped/partners/* -> APIGateway-portal, edge+API GW auth |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-routes | comp-routes trace getPlatinumAdvisorTimeseries | PASS | S3-direct via shared-advisor-router; edge-only control point |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-routes | comp-routes trace getPlatinumAccountSummary | PASS | S3-direct, account id path — ownership-map required |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-routes | comp-routes trace getPlatinumClientSummary | PASS | API GW, relationship id path — ownership-map required |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-trace | comp-trace getPlatinumAdvisorDrilldownSummary --direction both | PARTIAL | No route row; grep confirms same URL as getPlatinumAdvisorSummary, one backend path |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-cache | comp-cache collisions | PASS | 1 shared key (firm-leaderboard) — deliberate; no accidental collisions |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-transform | comp-transform schema-check AdvisorBookView | PASS | 17 fields / 2 direct / 12 panel-flow — expected; .005 must re-run post-lift |
| 2026-04-10 | 1.0.0_SA_CTO | ADVI_PROFIL (PRD) | comp-transform | comp-transform fields AdvisorPublicProfile | PASS | 9 fields across entry/summary/timeseriesResp — matches arch |
| 2026-04-10 | 2.0.0_SA_COO | ADVI_PROFIL.004 decomposition | SKIPPED | comp-routes / comp-blast at TO-writing time | FAIL | Transcribed scoping rule from RD briefing §5.2 without running comp-routes first. CTO caught the mix of advisor-id vs account-id/relationship-id path keys + two CloudFront behaviors, drove .004a/.004b/.004c split. Corrective: feedback_coo_compiler_mandatory_before_task_orders.md + prompt.md compiler mandate strengthened. |
2026-04-10 | 0.6.0_AE_PartnerETL | ADVI_GLDRST.022 Phase 1 | comp-blast bd-gold-trigger, comp-trace bd-gold-trigger --down | No down connections (known graph gap: lambda->EC2/lambda-to-lambda/eventbridge-reverse not indexed). Fell back to terraform plan 0-diff + aws events/lambda CLI verification. | bd-v2.22.0
| 2026-04-10 | 2.0.0_SA_COO | ADHC NNA canonical TOs | comp-pipescript io | io D_04 | PASS | Confirmed D_04 reads TIMESERIES_CHART (D_00b) + HEADER_METRICS (D_00) but NOT canonical_nna directly; DS TO must add new input or consume pre-aggregated upstream data |
| 2026-04-10 | 2.0.0_SA_COO | ADHC NNA canonical TOs | comp-blast | D_04.client_portal_summary | WARN | Zero downstream edges (platinum/* keys are terminal in graph) — known coverage gap |
| 2026-04-10 | 2.0.0_SA_COO | ADHC NNA canonical TOs | comp-platinum reverse | platinum/firm/timeseries_overview.json | PASS | Producer D_04, served via S3-direct /api/scoped/advisor-intelligence/*.json shared-advisor-router edge auth, consumer PartnerAnalytics only |
| 2026-04-10 | 2.0.0_SA_COO | ADHC NNA canonical TOs | comp-transform fields | DistributionTab | PASS | 5 fields used; nna_geo/nna_adv/nna_geo_drill/nna_adv_drill in PlatinumCumulativeChartResponse type but flagged as unused at top level |
| 2026-04-10 | 2.0.0_SA_COO | ADHC NNA canonical TOs | comp-transform schema-check | DistributionTab | PASS | 12 unused fields on PlatinumCumulativeChartResponse; all rendered fields match types |
| 2026-04-10 | 2.0.0_SA_COO | ADHC NNA canonical TOs | comp-transform fields | PartnerAnalytics | PASS | Confirmed timeseriesData?.nna?.[auaGranularity] access pattern matches DS brief extension target |
| 2026-04-10 | 2.0.0_SA_COO | ADHC NNA canonical TOs | comp-cache collisions | all keys | PASS | Only ['firm-leaderboard', firmOverride] shared (intentional); no collision on ['advisor-intelligence','timeseries-overview',firmOverride] |
| 2026-04-10 | 2.0.0_SA_COO | ADHC NNA canonical TOs | comp-pipescript io | io D_00b, io D_00 | PASS | Both D_00 and D_00b read CANONICAL_NNA_PREFIX directly — candidates for pre-aggregation upstream if DS prefers layered approach |
2026-04-10 | 0.7.0_AE_CloudOps | ADVI_PROFIL.004a Phase 1 | comp-routes trace getPlatinumAdvisorSummary + getPlatinumAdvisorTimeseries + getPlatinumAdvisorDrilldownSummary, comp-blast shared-advisor-router | confirmed two-behavior split; shared-advisor-router only sees S3-direct path (architectural mismatch in TO — flagged to DT)
| 2026-04-10 | 0.4.0_DS_ClientPlatform | D_00c role_breakdown NNA fix | comp-pipescript io | io D_00c | PASS | Confirmed READS include CANONICAL_NNA_PREFIX and ADVISOR_FEE_DETAIL_PREFIX (both sources the fix reconciles); WRITES EMPLOYEE_LEADERBOARD -> D_04 unchanged |
| 2026-04-10 | 2.0.0_SA_COO | ADHC role-composition NNA TO | comp-platinum reverse | reverse employee_leaderboard.json | WARN | Graph has no route/producer/consumer for this platinum artifact (coverage gap, same pattern as other platinum JSONs). Not blocking -- grep confirms RoleDonut reads role_breakdown[r].nna directly |
| 2026-04-10 | 2.0.0_SA_COO | ADHC role-composition NNA TO | comp-transform fields | AdvisorPublicProfile | PASS | Confirmed entry.role_breakdown + entry.roles at top level; matches RD brief's "no required FE changes" claim |
| 2026-04-10 | 2.0.0_SA_COO | ADHC role-composition NNA TO | comp-pipescript io | io D_00c | PASS | D_00c reads CANONICAL_NNA_PREFIX + ADVISOR_FEE_DETAIL_PREFIX + ACCOUNT_TEAM + REL_ARCHITECT_LOOKUP; writes EMPLOYEE_LEADERBOARD. Matches DS fix scope |
2026-04-10 | 0.7.0_AE_CloudOps | ADVI_PROFIL.004a deploy | comp-routes trace + comp-blast on Lambda@Edge, verified opal-partners-data firm-scoping via is_authorized() / computeAllowedFirms() | architectural correction (shared-advisor-router -> auth-validator-edge), Option 3 admin semantics, deployed portal-auth-v1.11.8 + v1.11.9
2026-04-10 | 0.4.2_RD | ADVI_PROFIL.005 | schema-check AdvisorBookClientDetail+AdvisorBookAccountDetail clean, comp-cache map no-collision, comp-blast ClientsTab confined, tsc+eslint green, 8 new files + 2 modified
2026-04-10 | 0.4.2_RD | ADVI_PROFIL.007+.006 | isFirmAdmin gate broadened (internal || isAdmin), My Profile button on BooksTab N1 gated on claims.advisorId, L3+L4 gcTime:0 applied in both paths (AdvisorBookView + ClientsTab), tsc+eslint green, schema-check ClientsTab PASS
2026-04-10 | 0.4.0_DS_ClientPlatform | ADVI_PROFIL.004b | D_00 ownership_map: comp-pipescript io/consumers, comp-routes (platinum behavior), py_compile, synthetic + live dry-run (162 advisors 377KB), etag parity on S3 upload
2026-04-10 | 0.4.0_DS_ClientPlatform | ds-advi-nna-canonical-source | comp-pipescript io/consumers D_04, grep (nna_geo/nna_adv producers), py_compile, live dry-run 5.8M canonical_nna rows / 2290 dates / 109 entries x 2 cohorts all sum-invariants hold, etag parity
2026-04-10 | 0.7.0_AE_CloudOps | ADVI_PROFIL.004c deploy + validate | comp-build, manual cross-read of auth-validator-edge + ownership_map + D_00 source + iam.tf, CloudWatch structured log query via PowerShell wrapper | shipped portal-auth-v1.11.10 + v1.11.11, 8/8 curl matrix GREEN, 2 CloudWatch rule=004c denial events confirmed, all 5 new event types wired (advisor_scoping_denied rule=004c, advisor_not_in_ownership_map, ownership_map_schema_mismatch, ownership_map_fetch_failed)
2026-04-10 | 0.4.2_RD | rd-advi-nna-frontend-migration + bundled sweep | baseline: schema-check DistributionTab clean, fields(DT)=5 fields(PA)=9 1 shared cache key. After: schema-check clean + new getTimeseriesOverview entry, fields(DT)=7 fields(PA)=unchanged (constraint #2), 2 shared cache keys (new: ['advisor-intelligence','timeseries-overview',firmOverride] PA L163 + DT L537 byte-identical). 8 commits: NNA canonical-source migration + fallback path, outflow sign normalization, bell curve log-tick ceiling, NNA donut signed sort at all drill levels, VIBGYOR palette reorder CITY/CLIENT, 'Other' canonicalization + dedup, AdvisorsTab cursor cleanup, Fee-Paying/role-filter nested bucket fix, AdvisorPublicProfile header Identity dedup (Andrew-authored bundled). tsc+eslint green throughout.
2026-04-13 | 0.5.0_AE_OpalETL | DEBT_1STRUN.005 | N/A (IAM/Dynamo imports; coverage proxy: Dynamo 47%->60%, IAM 49%->58%)

## 2026-04-13 — 2.0.0_SA_COO — ADVI_OTHDED.001 TO authoring
- `comp-blast DistributionTab.tsx` — PASS. 6 downstream nodes; endpoints getPlatinumCumulativeChart / getPlatinumAdvisorNnaClients / getTimeseriesOverview via opal-partners-data Lambda. Frontend-only fix confirmed — no Lambda/gold-script crossing.
- `comp-transform schema-check DistributionTab` — PASS. All rendered fields match response types. 12/17 cumulative-chart fields unused (unrelated to fix; segments path is from getTimeseriesOverview -> partner_analytics_monthly.json).
- Re-verified CTO PRD evidence block before TO issuance; no skipped compiler runs.

## 2026-04-13 — 0.4.0_DE_ClientPlatform — ADVI_OTHDED.001 implementation
- `comp-transform schema-check DistributionTab` — PASS. Rendered field set unchanged by the sentinel-regex + multi-Other merge edit.
- Raw S3 inspect `s3://opal-data-bd/platinum/firm/partner_analytics_monthly.json` — PASS. 28 states emit `other_{state}` (al ar az ca co fl ga ia il ks la md mi mn mo ms nc nj ny oh ok or pa sc tn tx va wa). TX: 10 cities, `other_tx` AUA $416,516,783.03 / 1,795 acct (matches TO).
- ADV `other_{architect}` probe — NOT EMITTED. D_01 currently does not produce that pattern on the architect path; sentinel regex is forward-compatible if it ever does. Acceptance criterion #3 → N/A (documented in session log).
- `comp-blast DistributionTab.tsx` — PASS. No new downstream impact.
- `tsc --noEmit` — clean.
- `eslint DistributionTab.tsx` — 0 errors, 10 warnings (all pre-existing `react-hooks/set-state-in-effect`, unrelated).

## 2026-04-13 — 2.0.0_SA_COO — ADVI_HDRSPL.001-003 TO authoring
- `comp-blast PartnerAnalytics.tsx` — PASS. 2 downstream (getTimeseriesOverview / opal-partners-data). Safe to internalize timeWindow + granularity.
- `comp-blast AdvisorIntelligence.tsx` — PASS. 3 downstream (getPlatinumPartnerAnalytics + getFirmLeaderboard / opal-partners-data). Page-root state moves are scoped.
- `comp-transform schema-check PartnerAnalytics` — PASS. 4/7 rendered, no waste. Prop-shape change safe.
- Frontend-only scope confirmed across all three waves. No Lambda/gold/auth crossing.

## 2026-04-13 — 0.4.0_DE_ClientPlatform — ADVI_HDRSPL.001 implementation
- Grep `portal/src/components/` primitives — PASS. Existing pattern: cva + tailwind + cn(clsx+twMerge). Created `portal/src/components/ui/` subdir to host the primitive.
- In-panel control metric recon: `px-3 py-1.5 text-xs rounded-md` with selected-state `bg-[hsl(var(--primary))] text-white`. Matched exactly in PageSurfaceControl.
- `tsc --noEmit` — clean.
- `eslint` on `PageSurfaceControl.tsx` + demo — 0 errors, 0 warnings.
- `/frontend-dev` WCAG numeric — OUTSTANDING (requires dev-server + demo route).

## 2026-04-13 — 0.4.0_DE_ClientPlatform — ADVI_HDRSPL.002 + .003 implementation (bundled)
- Grep `timeWindow`/`granularity`/`selectedFirmId` across `portal/src/pages/AdvisorIntelligence/` — confirmed page-root ownership (AdvisorIntelligence.tsx:144,156 per CTO PRD).
- Read `PartnerAnalytics.tsx` + `DistributionTab.tsx` prop usage — verified scoped internalization is safe.
- `tsc --noEmit` — clean.
- `eslint` on 3 changed files (AdvisorIntelligence.tsx, PartnerAnalytics.tsx, DistributionTab.tsx) — 0 errors, 10 pre-existing warnings (react-hooks/set-state-in-effect; same count as pre-change).
- `/frontend-dev` closed-loop pass — OUTSTANDING (requires submodule bump to 4cb34a2).
## 2026-04-13 â€” 1.0.0_SA_CTO â€” ADVI_REBORN leaderboard fees x roles fix
- `python -m org.modules.graph.cli build` â€” PASS. Graph rebuilt: 655 nodes, 293 edges.
- `python -m org.modules.graph.cli trace employee_leaderboard --direction both --all` â€” PASS. Producer is `D_00c.portal_leaderboard:build_employee_leaderboard`; artifact is `gold/artifacts/employee_leaderboard.json`.
- `python -m org.modules.graph.cli blast build_employee_leaderboard` â€” PASS. Blast radius is the leaderboard artifact.
- `python -m org.modules.graph.routes_cli trace getEmployeeLeaderboard` â€” PASS. Serving route resolves to `/api/scoped/advisor-intelligence/artifacts/employee_leaderboard.json` via `shared-advisor-router` to S3 key `gold/artifacts/employee_leaderboard.json`.
- Manual code confirmation after compiler pass â€” `D_00c` already emits nested `role_breakdown.fee_paying/no_fee`; `D_04` trims them via `_LEADERBOARD_ROLE_FIELDS`; `AdvisorsTab.tsx` falls back with `(data[feeView] ?? data)`. Result: backend-serving contract gap plus frontend unsafe fallback. DS then DE sequence written into PRD addendum.

## 2026-04-13 — 2.0.0_SA_COO — ADVI_REBORN.W6-001 + W6-002 TO authoring
- `comp-pipescript io D_04` — PASS. Confirmed `platinum/firm/leaderboard.json` is a terminal write of D_04. DS scope contained to D_04.
- `comp-blast AdvisorsTab.tsx` — PASS. 1 downstream (`getFirmLeaderboard`). Frontend-only.
- CTO PRD evidence block re-verified: comp-trace employee_leaderboard + comp-routes getEmployeeLeaderboard confirm the serving path is CloudFront `/api/scoped/advisor-intelligence/artifacts/*` -> shared-advisor-router -> S3.

## 2026-04-13 — 0.4.0_DE_ClientPlatform — ADVI_REBORN.W6-002 implementation
- Grep `?? data` / `feeView` / `role_breakdown` in AdvisorsTab — PASS. Single site identified at line 287.
- S3 inspect `s3://opal-data-bd/platinum/firm/leaderboard.json` — PASS. Travis role entries carry fee_paying + no_fee sub-objects.
- `comp-transform schema-check AdvisorsTab` (via tsc) — PASS. No prop-shape regression.
- `tsc --noEmit` — clean.
- `eslint src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` — 0 errors.
- Grep `?? data` post-edit — PASS. Zero silent fallbacks remain.
- Four-cell audit (Travis Penfield) — 3/4 cells match; 4th deviates from TO ceiling (actual 365.55M vs TO <=341M). Structural fix correct; data expectation disagreement raised with DS.

## 2026-04-13 — 0.4.0_DE_ClientPlatform — Advisor profile/book input mapping audit
- comp-platinum page AdvisorPublicProfile / AdvisorBookView / ClientDetailPage — full-stack traces captured.
- comp-platinum tab-audit — confirmed origin/auth/transforms per tab fetch.
- comp-transform schema-check on 7 surfaces — flagged 12/13 unused fields on AdvisorDrilldownSummary, 13/19 on PlatinumAdvisorSummary (with TYPE-DRIFT noted), 6/13 on PlatinumClientSummary, 1/6 on PlatinumAccountSummary.
- comp-transform fields on AdvisorBookView/TaxCostBasisPanel/CanonicalBookView — confirmed which props feed which UI slots.
- Output: docs/audits/advisor-profile-book-input-mapping-2026-04-13.md (DE column complete; awaiting RD source-of-truth column).
2026-04-13 | 0.4.2_RD_AdvisorIntelligence | none run | UX polish (FeeEfficiency table + BETA badge + Firm dropdown redesign) — no data/field surface changes, edits local to page dir, no shared-component modifications; comp-* would not have added signal.
2026-04-13 | 0.4.0_DS_ClientPlatform | ADVI_PROFAU.001 | comp-pipescript io D_00c (confirmed leaderboard artifact chain); comp-pipescript io D_04 (confirmed 21 platinum writes, client_detail_key in read set); comp-trace employee_leaderboard --direction both --all (D_00c->leaderboard->D_04->platinum/firm/leaderboard.json, terminal); comp-transform schema-check AdvisorBookView (PlatinumAdvisorSummary 19/3 rendered, PlatinumClientSummary 13/5, PlatinumAccountSummary 6/3); comp-transform schema-check AdvisorPublicProfile (AdvisorDrilldownSummary 13/1, SCHEMA MISMATCH: timeseriesResp not declared). Phase 2 greps: capital_gains/cost_basis absent from D_04 advisor builder; is_fee_paying absent from D_02; fee_summary LIVE in D_04 line 687+516; total_market_value LIVE in D_04 line 888; D_02 line 960 fee_earning_mask = total_split_pct>0 (no billability gate). Output: org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/profau_gap_audit_response.md.

2026-04-13 | 1.0.0_SA_CTO | ADVI_OFFICE PRD | comp-blast D_01.partner_analytics (no downstream tracked -- D_04 pass-through is hardcoded, isolated blast); comp-blast DistributionTab (8 downstream: 4 endpoints x opal-partners-data, all additive -- OFC adds new field, no breakage); comp-pipescript io D_01 (confirmed reads: account_team, canonical_nna, acct_dim -- all available for office dim); comp-pipescript io D_04 (confirmed pass-through model for partner_analytics artifact -- no D_04 changes needed); manual read D_01 build_adv_view L889-1069 (schema template for build_ofc_view); manual read D_01 build_nna_adv_view L1391-1480 (schema template for build_nna_ofc_view); comp-transform schema-check DistributionTab (N/A -- tool found DistributionTab in blast, schema-check not applicable to non-component; confirmed CohortOption/GrainView/COHORT_OPTIONS from direct file read).

2026-04-13 | 2.0.0_SA_COO | ADVI_OFFICE TO issuance | comp-pipescript io D_01 (PASS -- reads account_team+canonical_nna+acct_dim, writes partner_analytics artifacts; dim_advisor_office dynamic S3 read not graph-tracked, expected); comp-pipescript io D_00b (PASS -- reads account_team+client_performance, writes timeseries_chart.json; OFC adds office grouping to existing C_07/C_02 reads); comp-blast DistributionTab (PASS -- 8 downstream nodes, 4 endpoints all via opal-partners-data Lambda, OFC additive, no blast radius change); comp-transform schema-check DistributionTab (PASS with note -- chartData at L658/L687/L859 and analyticsData at L606/L687/L841 are pre-existing destructure aliases not in TypeScript types; not introduced by OFC; captured in W3 DE TO context for awareness). All 4 runs confirmed PRD claims; no new blockers or cross-domain conflicts discovered.
2026-04-14 | 0.6.0_AE_PartnerETL | phase3_v2_vs_job1_diff.py --fetch+diff 2026-04-13 | 10,100 Sunday-only rows missing from v2 (design gap: spine ends at tx_date_max); 0 price/source violations on 10.6M overlap rows; S_00 confirmed running (hotfix 2a6136e4 effective)

2026-04-14 | 2.0.0_SA_COO | ADVI_PROFAU .004+.005 TO authoring | comp-transform schema-check AdvisorBookView (PlatinumAdvisorSummary: 21 UNUSED confirmed -- 7 fee/tagged book fields + role_breakdown missing from declared type; PlatinumClientSummary: fee_summary UNUSED confirmed; PlatinumAccountSummary: OK 4/6 rendered); comp-blast AdvisorBookView (4 downstream nodes -- 3 endpoints + opal-partners-data Lambda, isolated, no cross-component impact); comp-routes trace getPlatinumAdvisorSummary (/api/scoped/partners/books/advisor/{id}/platinum-summary -- CloudFront /api/scoped/partners/*, components: AdvisorBookView + ClientsTab). All 3 runs confirmed .004 type scope and .005 render scope; blast radius isolated; Q1+Q2 correctly deferred (.003 QA gate + DS Q2 TO gate).
2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W3 | comp-transform schema-check DistributionTab (PASS -- alias pattern chartData/analyticsData confirmed, all rendered fields match types); comp-cache collisions (PASS -- 3 shared keys intentional, no new conflicts); S3 spot-check platinum/firm/partner_analytics_quarterly.json (PASS -- views.ofc 10 offices live); S3 spot-check platinum/firm/timeseries_chart.json (PASS -- ofc + nna_ofc top-level keys, 2291 rows); comp-transform fields DistributionTab (PASS -- analyticsData.views.ofc accessed); comp-blast DistributionTab (PASS -- 8 downstream nodes 4 endpoints UNCHANGED); bun build (PASS -- 0 TypeScript errors). Portal DEV commit 7dd0a7e.
2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.004 verification | comp-transform schema-check AdvisorBookView (PASS -- 27 fields, 21 UNUSED, all fee/tagged fields already declared in PlatinumAdvisorSummary.book, role_breakdown at top level; bun build PASS -- 0 TypeScript errors; getPlatinumAdvisorDrilldownSummary input confirmed typed as PlatinumAdvisorSummary at api.ts L717; commit 0050c05)
2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.005 verification | comp-blast AdvisorBookView (PASS -- 3 endpoints + 1 Lambda, isolated); comp-transform schema-check AdvisorBookView (PARTIAL -- fee_summary still UNUSED on PlatinumClientSummary due to alias-tracking gap: clientSummary.fee_summary->l3ClientDetail->feeSummaryByAccount->FeeSummaryPanel is confirmed live by code trace but not followed by tool; total_market_value confirmed rendered at L4 in AdvisorBookAccountDetail L104-106; bun build PASS; commit d1f9747)
2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_REBORN.W6-004 verification | comp-transform schema-check AdvisorsTab (PASS -- getFirmLeaderboard -> PlatinumLeaderboardResponse, all rendered fields match types; UNUSED: available_windows, windows -- expected container fields); comp-blast AdvisorsTab (PASS -- 1 downstream endpoint getFirmLeaderboard, blast radius UNCHANGED from baseline); bun run build (PASS -- 0 TypeScript errors); S3 artifact spot-check platinum/firm/leaderboard.json Travis Penfield QTD (PASS -- role_combination_breakdown present with 5 combo keys; role_breakdown fee_paying/no_fee sub-buckets confirmed split-allocated via W6-005). Four-cell matrix verified: Fee-Paying+all=340.5M (canonical), Fee-Paying+impl-off=307.9M (<=341M, not 394M). No code changes needed -- W6-005 approach already satisfies all W6-004 acceptance criteria.
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_OFFICE.W1 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_OFFICE.W1 | comp-blast | comp-blast DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_OFFICE.W1 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_OFFICE.W1 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DT_ClientPlatform | ADVI_OFFICE.W4 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DT_ClientPlatform | ADVI_OFFICE.W4 | comp-blast | comp-blast DistributionTab | PASS |
| 2026-04-14 | 1.0.0_SA_CTO | ADVI_OFFICE_gap_analysis | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 1.0.0_SA_CTO | ADVI_OFFICE_gap_analysis | comp-routes | comp-routes trace getPlatinumPartnerAnalytics | PASS |
| 2026-04-14 | 1.0.0_SA_CTO | ADVI_OFFICE_gap_analysis | comp-routes | comp-routes trace getPlatinumCumulativeChart | PASS |
| 2026-04-14 | 1.0.0_SA_CTO | ADVI_OFFICE_gap_analysis | comp-transform | comp-transform fields DistributionTab | PASS |
| 2026-04-14 | 1.0.0_SA_CTO | ADVI_OFFICE_gap_analysis | comp-platinum | comp-platinum page DistributionTab | PASS |
| 2026-04-14 | 1.0.0_SA_CTO | ADVI_OFFICE_gap_analysis | comp-pipescript | comp-pipescript io D_00b --no-portal | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_01 --no-portal | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.006 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.006 | comp-blast | comp-blast AdvisorBookView | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.006 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.006 | comp-blast | comp-blast AdvisorBookView | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.006 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-14 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-blast | comp-blast DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-blast | comp-blast DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-pipescript | comp-pipescript io D_02.advisor_client_detail.py | FAIL |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_OFFICE.W6 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-14 | 2.0.0_SA_COO | ADVI_PROFAU.007 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-14 | 2.0.0_SA_COO | ADVI_PROFAU.007 | comp-blast | comp-blast AdvisorBookView | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.007 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_PROFAU.007 | comp-blast | comp-blast AdvisorBookView | PASS |
| 2026-04-14 | 2.0.0_SA_COO | ADVI_OFFICE.W9 | comp-pipescript | comp-pipescript io D_00b.portal_timeseries.py | FAIL |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_OFFICE.W9a | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-14 | 0.4.0_DT_ClientPlatform | ADVI_OFFICE.W8 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DT_ClientPlatform | ADVI_OFFICE.W8 | comp-blast | comp-blast DistributionTab | PASS |
| 2026-04-14 | 2.0.0_SA_COO | adv-donut-account-count | comp-pipescript | comp-pipescript io D_01.partner_analytics_artifacts.py | FAIL |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | adv-donut-account-count | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | adv-donut-account-count | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-14 | 1.0.0_SA_CTO | (no-TO) | comp-blast | comp-blast convert_fees_to_silver | PASS |
| 2026-04-14 | 1.0.0_SA_CTO | (no-TO) | comp-blast | comp-blast ETFClassifier | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-validate | comp-validate --help | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-validate | comp-validate --list | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_04.client_portal_summary.py | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript --help | PASS |
| 2026-04-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_FNTEND.B0.rd-fe-trivial-sweep | comp-transform | comp-transform schema-check CanonicalBookView | PASS |
| 2026-04-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_FNTEND.B0.rd-fe-trivial-sweep | comp-transform | comp-transform schema-check ConsolidatedOverviewPanel | PASS |
| 2026-04-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_FNTEND.B0.rd-fe-trivial-sweep | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | 3-bond-phantom-scoped-exceptions | comp-pipescript | comp-pipescript io inject_scoped_overrides.py | FAIL |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | 3-bond-phantom-scoped-exceptions | comp-pipescript | comp-pipescript consumers canonical_prices | FAIL |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | 3-bond-phantom-scoped-exceptions | comp-transform | comp-transform ternary-audit DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-platinum | comp-platinum page AdvisorBookView | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-transform | comp-transform schema-check DistributionTab --feature snapshot | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-blast | comp-blast DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-transform | comp-transform schema-check RelationshipFlowsSummary | FAIL |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-transform | comp-transform schema-check AccountsTable | FAIL |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-transform | comp-transform schema-check ClientsTable | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-transform | comp-transform schema-check AuaDecompositionPanel | FAIL |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-transform | comp-transform schema-check ClientsTable --feature windowTrio | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-14 | 0.4.0_DS_ClientPlatform | ADVI_FNTEND.B2 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.D7 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.D7 | comp-platinum | comp-platinum page PartnerAnalytics | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B2 | comp-transform | comp-transform schema-check ClientsTable | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B2 | comp-cache | comp-cache collisions | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-blast | comp-blast D_02 | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-blast | comp-blast D_00c | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-blast | comp-blast role_breakdown | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-blast | comp-blast leaderboard | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-blast | comp-blast architect_aua | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-blast | comp-blast tagged_aua | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-blast | comp-blast EMPLOYEE_LEADERBOARD | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-pipescript | comp-pipescript consumers EMPLOYEE_LEADERBOARD | FAIL |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-blast | comp-blast ADVISOR_FEE_EFFICIENCY | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-platinum | comp-platinum reverse platinum/firm/leaderboard.json | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-platinum | comp-platinum reverse platinum/advisors/{id}/timeseries.json | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-platinum | comp-platinum reverse platinum/advisors/{id}/summary.json | PASS |
| 2026-04-14 | 0.4.0_DE_ClientPlatform | ADVI_FNTEND.B1 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-15 | 1.0.0_SA_CTO | (no-TO) | comp-blast | comp-blast D_02 | PASS |
| 2026-04-15 | 1.0.0_SA_CTO | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-04-15 | 1.0.0_SA_CTO | (no-TO) | comp-blast | comp-blast C_01 | PASS |
| 2026-04-15 | 1.0.0_SA_CTO | (no-TO) | comp-blast | comp-blast D_00c | PASS |
| 2026-04-15 | 1.0.0_SA_CTO | (no-TO) | comp-blast | comp-blast D_01 | PASS |
| 2026-04-15 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-15 | 1.0.0_SA_CTO | ADVI_ROLLUP.small-account-count-addendum | comp-transform | comp-transform schema-check FeeEfficiency | PASS |
| 2026-04-15 | 1.0.0_SA_CTO | ADVI_ROLLUP.small-account-count-addendum | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/C_08.advisor_fee_efficiency.py | FAIL |
| 2026-04-15 | 1.0.0_SA_CTO | ADVI_ROLLUP.small-account-count-addendum | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04.client_portal_summary.py | FAIL |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-blast | comp-blast _compute_window_decomposition | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-blast | comp-blast _compute_window_flows | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse rfs.decomposition_max.nna | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse rfs.decomposition_ytd.nna | PASS |
| 2026-04-15 | 2.0.0_SA_COO | ADVI_ROLLUP.RF01 | comp-pipescript | comp-pipescript io D_04 | PASS | 21 reads/21 writes; portal consumers AdvisorBookView + AdvisorPublicProfile confirmed |
| 2026-04-15 | 2.0.0_SA_COO | ADVI_ROLLUP.RF01 | comp-blast | comp-blast _compute_window_decomposition | EMPTY | internal helper not a graph node — expected; fallback to grep -n in TO Phase 1 |
| 2026-04-15 | 2.0.0_SA_COO | ADVI_ROLLUP.RF01 | comp-blast | comp-blast _compute_window_flows | EMPTY | same |
| 2026-04-15 | 2.0.0_SA_COO | ADVI_ROLLUP.RF01 | comp-platinum | comp-platinum reverse rfs.decomposition_max.nna | EMPTY | nested key not indexed — TO falls back to portal grep for consumer enumeration |
| 2026-04-15 | 2.0.0_SA_COO | ADVI_ROLLUP.RF01 | comp-platinum | comp-platinum reverse rfs.decomposition_ytd.nna | EMPTY | same |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io bd_price_update | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io inject_scoped_overrides | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript postdeps build_canonical_prices | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-blast | comp-blast silver/transactions | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01.ds-d04-window-nna-delta-fix | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | BDPL_CNPRCS.WP-11+3-bond-phantom | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | BDPL_CNPRCS.WP-11+3-bond-phantom | comp-platinum | comp-platinum reverse role_aua | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-platinum | comp-platinum reverse nna_atomic | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript postdeps build_canonical_prices | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-blast | comp-blast silver/unrealized | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io A_00.accounts_dimension | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io inject_scoped_overrides.py | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io A_01.advisor_assignments | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-transform | comp-transform schema-check TaxCostBasisPanel | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io A_02.fee_rate_history | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io A_03.positions_cube | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io A_04.client_dimension | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io B_00.canonical_holdings | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io B_01.holdings_lots | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io B_01b.classify_new_securities | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io B_02.canonical_lots | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io B_03.account_gains | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io C_00.canonical_performance | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io C_01.canonical_nna | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | BDPL_CNPRCS.WP-10b | comp-pipescript | comp-pipescript io C_02.client_performance | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io silver/transactions | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_03.account_performance | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_04.validate_aua | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_05.client_tax_liability | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_06.client_mix_timeseries | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_07.advisor_attribution | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_08.advisor_fee_efficiency | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00.portal_aggregates | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00b.portal_timeseries | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00c.portal_leaderboard | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript deployed bd_price_update.py | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_01.partner_analytics | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript deployed inject_scoped_overrides.py | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_02.advisor_client_detail | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript --help | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_03.composition_artifacts | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_04.client_portal_summary | FAIL |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_02 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_04 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-blast | comp-blast platinum/accounts/{*}/summary.json | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_02 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_01 | PASS |
20260415T162721Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-pipescript io D_04 | PASS | WRITES + PORTAL CONSUMERS confirmed
20260415T162722Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-pipescript deployed D_04 | TOOL_ERROR (aws PATH); manual etag parity PASS
20260415T162723Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-blast platinum/accounts/*/summary.json | NO_NODES; manual blast unchanged
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_04 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-15 | 0.6.0_AE_PartnerETL | BDPL_CNPRCS.WP-3 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P0 | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P0 | comp-blast | comp-blast _compute_window_decomposition | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P0 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P0 | comp-platinum | comp-platinum reverse nna_atomic | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P0 | comp-blast | comp-blast _compute_window_flows | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast diag_phantom_valuations | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast C_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_00 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-platinum | comp-platinum reverse rfs.decomposition_max.nna | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_00b | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-platinum | comp-platinum reverse rfs.decomposition_ytd.nna | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_00c | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast _window_nna_delta | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_00c | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast D_00b | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast C_08 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-platinum | comp-platinum reverse rfs | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-iam | comp-iam gaps | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-platinum | comp-platinum reverse role_aua | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-platinum | comp-platinum page AdvisorPublicProfile | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-iam | comp-iam --help | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-iam | comp-iam stats | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-iam | comp-iam services | PASS |
20260415T163423Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-blast _compute_window_decomposition | NO_MATCH (tool limit: no function-level nodes)
20260415T163423Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-blast _compute_window_flows | NO_MATCH (tool limit)
20260415T163423Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-platinum reverse rfs.decomposition_max.nna | EMPTY (tool limit: no nested-key index)
20260415T163423Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-platinum reverse rfs.decomposition_ytd.nna | EMPTY (tool limit)
20260415T163423Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-blast _window_nna_delta | NO_MATCH (tool limit)
20260415T163423Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-blast D_04 | PASS (terminal, no downstream)
20260415T163424Z | 0.4.0_DS_ClientPlatform~A | ADVI_ROLLUP.RF01 | comp-platinum page AdvisorPublicProfile | PASS — rfs.decomposition_* not in rendered fields (Wave C staged)
20260415T163500Z | 2.0.0_SA_COO | corpus-signal | comp-pipescript deployed silver-layer | FAIL — tool scans code/gold/ only; misses silver enforcer scripts (bd_price_update.py, inject_scoped_overrides.py). CTO-directed extension TO authored and routed to 1.0.0_SA_CTO (blame owner). WP-11 Phase 2 retroactively auditable post-fix.
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate --help | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate nna_atomic --schema | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate role_aua --schema | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate --list | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate --help | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate --list | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate nna_atomic | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate role_aua | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate --list | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript deployed bd_price_update.py | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript deployed inject_scoped_overrides.py | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast role_aua_schema_doc | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast diag_gold_silver_recon | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast gold_silver_recon_manifest | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript deployed C_08 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast advisor_fee_efficiency | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast C_08.build_scorecard | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | comp-pipescript-silver-ext | comp-pipescript | comp-pipescript deployed bd_price_update.py (post-fix) | PASS -- [SILVER] MATCH (was: empty/Unknown script) |
| 2026-04-15 | 0.7.0_AE_CloudOps | comp-pipescript-silver-ext | comp-pipescript | comp-pipescript deployed D_04 (regression check) | PASS -- [GOLD] MATCH preserved |
| 2026-04-15 | 0.7.0_AE_CloudOps | comp-pipescript-silver-ext | comp-pipescript | comp-pipescript deployed inject_scoped_overrides.py | PASS -- [SILVER] MATCH |
| 2026-04-15 | 0.7.0_AE_CloudOps | comp-pipescript-silver-ext | comp-pipescript | comp-pipescript deployed (full sweep) | PASS -- 38 MATCH (gold+silver), surfaced [GOLD] C_08 STALE (DS) and [SILVER] upload_bd_assets_backfill.py MISSING_ON_S3 |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript deployed C_08 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate D_04 --artifact /tmp/z0820265531_summary.json | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate D_04 --artifact /tmp/travis_summary.json | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-iam | comp-iam service bd-transactions-trigger | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast silver/transactions | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate D_04 --artifact /tmp/firm_leaderboard.json | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-iam | comp-iam --help | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-iam | comp-iam services | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-validate | comp-validate C_08 --artifact /tmp/afe2.json | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-blast | comp-blast account_id | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P0 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | ADVI_ROLLUP.B9 | comp-transform | comp-transform schema-check FeeEfficiencyPanel | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | ADVI_ROLLUP.B9 | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | ADVI_ROLLUP.B9 | comp-transform | comp-transform schema-check FeeEfficiencyPanel | PASS |
20260415T172228Z | 0.4.0_DS_ClientPlatform~A | ofc-l2-advisor-distribution | comp-pipescript io D_03 | PIVOT (D_03 does not write summary.json; chose D_04)
20260415T172228Z | 0.4.0_DS_ClientPlatform~A | ofc-l2-advisor-distribution | comp-pipescript io D_04 | PASS (summary.json in WRITES)
20260415T172229Z | 0.4.0_DS_ClientPlatform~A | ofc-l2-advisor-distribution | py_compile D_04 | PASS
20260415T172231Z | 0.4.0_DS_ClientPlatform~A | ofc-l2-advisor-distribution | comp-blast D_04 | PASS (terminal)

## 2026-04-15 - Gap Resolutions (1.0.0_SA_CTO)

| Gap | Tool | Observed | Impact | Candidate Fix |
|-----|------|----------|--------|---------------|
| Function-level Python helpers were invisible to graph blast queries | `comp-blast` | `comp-blast _compute_window_decomposition` and `_compute_window_flows` returned `NO_MATCH` despite live callsites in `D_04.client_portal_summary.py` | RF01 and similar TO audits had to fall back to grep, losing caller/downstream artifact visibility | Add top-level Python function nodes plus local caller/callee edges, including reverse caller edges so helper blast walks outward to callers and downstream outputs |
RESOLUTION: fixed in `0324142a` (`compiler-tools: add function blast, dotted reverse, and honest deployed timeouts`)

| Gap | Tool | Observed | Impact | Candidate Fix |
|-----|------|----------|--------|---------------|
| Nested payload field paths had no reverse index | `comp-platinum reverse` | `comp-platinum reverse rfs.decomposition_max.nna` and `.ytd.nna` returned `EMPTY` with no producer, route, or consumer | TO mandate runs could not enumerate ownership of specific platinum subfields and had to fall back to portal grep | Extend reverse lookup to accept dotted payload paths and resolve them through transform field usage back to artifact, producer, route, and consuming component |
RESOLUTION: fixed in `0324142a` (`compiler-tools: add function blast, dotted reverse, and honest deployed timeouts`)

| Gap | Tool | Observed | Impact | Candidate Fix |
|-----|------|----------|--------|---------------|
| Deployed-check runtime failures were ambiguous after AWS subprocess launch | `comp-pipescript deployed` | Prior code fixed PATH lookup, but runtime hangs still surfaced as unhelpful failures and misleading summary text; matched scripts could still end with `No scripts matched filter` | Operators could not distinguish tooling defects from AWS/session defects, and manual diagnosis cost was too high | Forward a controlled AWS env into the subprocess, default `AWS_EC2_METADATA_DISABLED=true`, and emit explicit `TIMEOUT` plus AWS guidance instead of silent or misleading output |
RESOLUTION: fixed in `0324142a` (`compiler-tools: add function blast, dotted reverse, and honest deployed timeouts`)
| 2026-04-15 | 0.7.0_AE_CloudOps | CFIMPT_REST.001 | comp-validate | comp-validate | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CFIMPT_REST.001 | comp-pipescript | comp-pipescript io D_04.client_portal_summary.py | FAIL |
| 2026-04-15 | 0.7.0_AE_CloudOps | CFIMPT_REST.001 | comp-transform | comp-transform schema-check AdvisorPublicProfile | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CFIMPT_REST.001 | comp-iam | comp-iam services | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CFIMPT_REST.001 | comp-cache | comp-cache collisions | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CFIMPT_REST.001 | comp-iam | comp-iam stats | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~A | ADHC_ROUTER.T1.ds-a-test-comp-blast-function-level-vs-rf01 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~A | ADHC_ROUTER.T1.ds-a-test-comp-blast-function-level-vs-rf01 | comp-blast | comp-blast _compute_window_decomposition | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~A | ADHC_ROUTER.T1.ds-a-test-comp-blast-function-level-vs-rf01 | comp-pipescript | comp-pipescript deployed bd_price_update.py | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADHC_ROUTER.T4 | comp-blast | comp-blast _compute_window_flows | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADHC_ROUTER.T4 | comp-pipescript | comp-pipescript deployed inject_scoped_overrides.py | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-pipescript | comp-pipescript deployed bd_price_update.py | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-blast | comp-blast _window_nna_delta | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-pipescript | comp-pipescript deployed inject_scoped_overrides.py | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-pipescript | comp-pipescript io bd_price_update.py | FAIL |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse rfs.decomposition_max.nna | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse nna_atomic | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-validate | comp-validate nna_atomic --schema | FAIL |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse rfs.decomposition_ytd.nna | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse role_aua | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse advisor_fee_efficiency | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse small_account_count | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-blast | comp-blast C_08 | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-blast | comp-blast C_08.build_scorecard | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-validate | comp-validate nna_atomic --schema | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-validate | comp-validate role_aua --schema | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-validate | comp-validate D_04 --list | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-validate | comp-validate --list | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-validate | comp-validate bogus --whatever | FAIL |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse gold/artifacts/advisor_fee_efficiency.json | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse role_aua | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse advisor_fee_efficiency | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse small_account_count | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-build | comp-build | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-blast | comp-blast _window_nna_delta | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-blast | comp-blast _compute_window_decomposition | PASS |

## 2026-04-15 - ADHC_ROUTER.T4 Resolution (0.4.0_DS_ClientPlatform~D)

| Gap | Tool | Observed | Impact | Candidate Fix |
|-----|------|----------|--------|---------------|
| Standalone validators unreachable from `comp-validate` CLI | `comp-validate` | `comp-validate role_aua --schema` and `nna_atomic --schema` failed in argparse with `unrecognized arguments` despite standalone validators existing on disk | Agents running locked-discipline Phase-1/2 mandates had to fall back to direct `python validate_*.py` invocation, blurring "bad output" vs "tool could not route" in corpus rows | `parse_known_args()` + subprocess dispatch to `data/black_diamond/scripts/validators/validate_{id}.py` with all trailing flags forwarded; config-backed targets unchanged |
RESOLUTION: pass-through half fixed in `3c921e08` (`ADHC_ROUTER.T4 + comp-validate pass-through dispatch (proposal E partial)`) -- proposal E ACs #1-#4 closed; coverage-audit half (ACs #5-#8) remains open. Corpus-to-patch loop validated: DS ~D hit the gap during CN-P0 (commit 93b70620), flagged it explicitly, then closed it during ADHC_ROUTER.T4.
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse rfs.decomposition_max.nna | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-platinum | comp-platinum reverse rfs.decomposition_ytd.nna | PASS |
| 2026-04-15 | 0.7.0_AE_CloudOps | CDRS_TFIMPT.002 | comp-pipescript | comp-pipescript deployed D_04 | PASS |

## 2026-04-15 - ADHC_ROUTER.T1/T2/T3 Resolutions

| Gap | Tool | Observed | Impact | Candidate Fix |
|-----|------|----------|--------|---------------|
| 0324142a function-blast reverse-edge contamination | `comp-blast` | `comp-blast _window_nna_delta` returned 85-node blast (effectively all of D_04) instead of 1-node reachability — CALLS + CALLED_BY both indexed on source in the forward index, causing walks to explode through callers→co-callees | Stress test revealed a regression in the shipped function-blast feature; real audit use would produce runaway false-positive blast radii and masked real impact | Separate reverse-edge traversal direction so downstream walk doesn't follow CALLED_BY edges as forward edges |
RESOLUTION: fixed in `d1d6920b` (`compiler patches ADHC_ROUTER.T1 (function blast + dotted reverse)`) -- ADHC_ROUTER stress test caught a subtle regression in the shipped 0324142a feature; exactly the corpus-to-patch loop outcome the test pass was designed to produce.

| Gap | Tool | Observed | Impact | Candidate Fix |
|-----|------|----------|--------|---------------|
| AWS credential/network errors misclassified as MISSING_ON_S3 | `comp-pipescript deployed` | Broken AWS_PROFILE or expired token produced `MISSING_ON_S3` with no signal parity was unverifiable; agent would chase a phantom upload path | Correctness defect: tool claims S3 404 when it actually couldn't reach S3; an agent running against bad creds would ship a bogus upload to fix a non-existent gap | Add AWS_UNREACHABLE status gated by stderr allowlist (`Unable to locate credentials`, `ExpiredToken`, etc.); separate bucket in summary + remediation footer pointing at `aws sts get-caller-identity` |
RESOLUTION: fixed in `70c8399d` (`ADHC_ROUTER.T2 -- comp-pipescript deployed AWS_UNREACHABLE status`) -- distinguishes credential/network errors from real 404s; structural follow-up to switch to `--output json` + parse error code is backlogged.

| Gap | Tool | Observed | Impact | Candidate Fix |
|-----|------|----------|--------|---------------|
| Empty-vs-broken indistinguishability on reverse lookup | `comp-platinum reverse` | `role_aua` (genuine empty), `advisor_fee_efficiency` (mis-routed), and `small_account_count` (indexer gap) all produced byte-identical empty output | UX-severity correctness defect: agents like RA-P0 passed on "empty as expected" via side-knowledge, not tool signal. Equivalent to the Rule 7 acceptance-flex risk category but at the tool layer | Diagnostic footer on empty output with 4-case disambiguation [genuine / mis-routed / stale / extractor gap]; artifact-stem auto-probe to route bare names; SPECULATIVE MATCH label on directory-prefix fallback |
RESOLUTION: fixed in `614d4c28` (`comp-platinum reverse empty-vs-broken disambiguation + artifact-stem auto-probe`) -- reveals 3 additional out-of-scope findings: FIELD index suspiciously small (40 paths), function-level blast nodes missing, route.s3_key unset on CF-rewrite routes. Backlogged.
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P2.ds-nna-atomic-d02-consumer-cutover | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P2.ds-nna-atomic-d02-consumer-cutover | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P2.ds-nna-atomic-d02-consumer-cutover | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0 | comp-blast | comp-blast silver/unrealized | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0 | comp-pipescript | comp-pipescript io silver/unrealized | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0 | comp-pipescript | comp-pipescript io holdings_lots | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0 | comp-trace | comp-trace silver/unrealized --direction both | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P2 | comp-routes | comp-routes trace getPlatinumPartnerAnalytics | PASS |
| 2026-04-15 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0.ds-sleeve-discovery | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0.ds-sleeve-discovery | comp-blast | comp-blast silver/unrealized | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0.ds-sleeve-discovery | comp-pipescript | comp-pipescript io holdings_lots | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.SL-P0.ds-sleeve-discovery | comp-pipescript | comp-pipescript io D_02.advisor_client_detail | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.RA-P3+CN-P3 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.RA-P3+CN-P3 | comp-blast | comp-blast D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P2 | comp-pipescript | comp-pipescript io D_02 | PASS | role_aua in READS (RA-P1 shadow live); confirmed both callsites L1277/L1632 |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P2 | aws s3 ls | aws s3 ls s3://opal-data-bd/gold/canonical/role_aua/ | WARN | Single 2026-04-13.parquet only -> triggered Rule 7 ACCEPTANCE FLEX preflag, L1632 deferred to RA-P2b |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P2 | py_compile | python -m py_compile D_02 | PASS | Pre-commit gate, exit 0 |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.RA-P2 | comp-blast | comp-blast D_02 | WARN | Script-node lookup empty (per memory: use fn name); no new reader introduced confirmed by code review |
| 2026-04-15 | 0.4.2_RD_AdvisorIntelligence | ADVI_FNTEND.B0 | comp-validate | comp-validate sleeve_cohort --artifact /tmp/sleeve_cohort_2026-04-13.parquet | PASS |
| 2026-04-15 | 0.4.2_RD_AdvisorIntelligence | ADVI_FNTEND.B0 | comp-blast | comp-blast D_00c | PASS |
| 2026-04-15 | 0.4.2_RD_AdvisorIntelligence | ADVI_FNTEND.B0 | comp-blast | comp-blast build_employee_leaderboard | PASS |
| 2026-04-15 | 0.4.2_RD_AdvisorIntelligence | ADVI_FNTEND.B0 | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-15 | 0.4.2_RD_AdvisorIntelligence | ADVI_FNTEND.B0 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-platinum | comp-platinum reverse views.geo | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-platinum | comp-platinum reverse views.aua | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript feeds D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io S_00 | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io A_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-validate | comp-validate D_01 --artifact /tmp/btab/header_metrics_quarterly.json | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-transform | comp-transform schema-check AdvisorPublicProfile | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-platinum | comp-platinum page AdvisorPublicProfile | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-cache | comp-cache collisions | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-blast | comp-blast SummaryCard | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-routes | comp-routes auth-map | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.D01-T1 | comp-pipescript | comp-pipescript io D_01 | PASS | nna_aua_by_geography in READS, partner_analytics in WRITES; producer confirmed |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.D01-T1 | comp-platinum | comp-platinum reverse views.geo | PASS | D_04 (passthrough D_01) producer + portal route confirmed |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.D01-T1 | comp-platinum | comp-platinum reverse views.aua | PARTIAL | sub-key not indexed individually; expected |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.D01-T1 | grep | grep -nE 'state\|geo' D_01 | PASS | state filter at L758-763 located + quoted (notna + != '' + != 'Unknown') |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.D01-T1 | py_compile | python -m py_compile D_01.partner_analytics.py | PASS | exit 0, pre-commit gate |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-blast | comp-blast D_00c | PASS |
| 2026-04-15 22:08 | 1.0.0_SA_CTO | ADVI_49EXEC PRD | comp-transform schema-check | `comp-transform schema-check AdvisorPublicProfile` | 13 type fields on AdvisorDrilldownSummary, 12 UNUSED on this surface | OK to add new AdvisorExecSummary type |
| 2026-04-15 22:08 | 1.0.0_SA_CTO | ADVI_49EXEC PRD | comp-platinum page | `comp-platinum page AdvisorPublicProfile` | Existing fetches via APIGW (drilldown) + S3 (timeseries via shared-advisor-router); pattern for new fetch confirmed | Picked S3-direct endpoint for new artifact |
| 2026-04-15 22:08 | 1.0.0_SA_CTO | ADVI_49EXEC PRD | comp-cache collisions | `comp-cache collisions` | 3 existing collisions on page (timeseries-overview, firm-leaderboard, partner-analytics) all deliberate | New key 'advisor-exec-summary' chosen unique; per-TO mandate added |
| 2026-04-15 22:08 | 1.0.0_SA_CTO | ADVI_49EXEC PRD | comp-blast | `comp-blast SummaryCard` | No nodes (inline component) | Blast on parent AdvisorPublicProfile instead; documented PRD limitation |
| 2026-04-15 22:08 | 1.0.0_SA_CTO | ADVI_49EXEC PRD | comp-routes auth-map | `comp-routes auth-map | grep advisor` | /api/scoped/advisor-intelligence/*.json -> S3-opal-data-bd (existing) | No new CloudFront behavior needed |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_00.canonical_holdings.py | FAIL |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.D00c-T1 | comp-pipescript | comp-pipescript io D_00c | PASS | account_team + advisor_fee_detail + role_aua reads; employee_leaderboard.json write |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.D00c-T1 | comp-blast | comp-blast D_00c | WARN | Script-node lookup empty; no new reader (path b doc-only) |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.D00c-T1 | aws s3 ls/cp | folder list + missing advisor summary spot-check | PASS | 11 missing classified (4 sentinels + 7 zero-current); confirmed tagged_aua=0 |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-1.ds-incremental-feasibility-survey | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | ADVI_49EXEC.006 | comp-cache | comp-cache collisions | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | ADVI_49EXEC.006 | comp-transform | comp-transform schema-check AdvisorPublicProfile --feature exec | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | ADVI_49EXEC.006 | comp-pipescript | comp-pipescript deployed D_01 | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | ADVI_49EXEC.006 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-15 | 0.4.0_DE_ClientPlatform | ADVI_49EXEC.006 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-15 | 0.4.0_DT_ClientPlatform | ADVI_ROLLUP.IN-2.W0.002 | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-04-15 | 0.4.0_DT_ClientPlatform | ADVI_ROLLUP.IN-2.W0.002 | comp-transform | comp-transform fields AdvisorPublicProfile | PASS |
| 2026-04-15 | 0.4.0_DT_ClientPlatform | ADVI_ROLLUP.IN-2.W0.002 | comp-transform | comp-transform schema-check AdvisorPublicProfile --feature exec | PASS |
| 2026-04-15 | 0.4.0_DT_ClientPlatform | ADVI_ROLLUP.IN-2.W0.002 | comp-pipescript | comp-pipescript deployed C_08 | PASS |
| 2026-04-15 | 0.4.0_DT_ClientPlatform | ADVI_ROLLUP.IN-2.W0.002 | comp-cache | comp-cache collisions | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_FNTEND.B1.fix | comp-incrparity | comp-incrparity --help | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_FNTEND.B1.fix | comp-incrparity | comp-incrparity ALL --mode quick | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_FNTEND.B1.fix | comp-incrparity | comp-incrparity C_06 --mode quick | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_FNTEND.B1.fix | comp-incrparity | comp-incrparity C_06 --mode deep | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_FNTEND.B1.fix | comp-incrparity | comp-incrparity ALL --mode quick | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_FNTEND.B1.fix | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-15 | 0.4.0_DS_ClientPlatform~B | ADVI_FNTEND.B1.fix | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | deployment_map | comp-platinum | comp-platinum reverse top_gain_positions | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ROLLUP.DH-3 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ROLLUP.DH-3 | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ROLLUP.DH-3 | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-platinum | comp-platinum reverse top_gain_positions | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-build | comp-build | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-platinum | comp-platinum reverse gold/entities/advisors | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.D02-T2 | comp-pipescript | comp-pipescript consumers D_02 | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ROLLUP.DH-7 | comp-iam | comp-iam service bd-gold-layer-runner | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ROLLUP.DH-7 | comp-iam | comp-iam | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ROLLUP.DH-7 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P1b.ds-nna-atomic-historical-backfill | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P1b.ds-nna-atomic-historical-backfill | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-2 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.IN-2 | comp-blast | comp-blast silver/unrealized | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | ADVI_49EXEC.004 | comp-iam | comp-iam service exec-summary-generator | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~C | COMP_LEARNS.006 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~C | COMP_LEARNS.006 | comp-validate | comp-validate holdings_lots_shadow --artifact /tmp/holdings_lots_shadow_dryrun_2026-04-... | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~C | COMP_LEARNS.006 | comp-validate | comp-validate holdings_lots_shadow --artifact /tmp/holdings_lots_shadow_dryrun_2026-04-... | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~C | COMP_LEARNS.006 | comp-validate | comp-validate holdings_lots_shadow --artifact /c/tmp/holdings_lots_shadow_dryrun_2026-0... | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~C | COMP_LEARNS.006 | comp-validate | comp-validate holdings_lots_shadow --artifact /c/tmp/holdings_lots_shadow_dryrun_2026-0... | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~C | COMP_LEARNS.006 | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | SL-AE1 | comp-blast | comp-blast canonical_nna | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | SL-AE1 | comp-blast | comp-blast nna_atomic | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | SL-AE1 | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | SL-AE1 | comp-pipescript | comp-pipescript deployed run_gold_layer | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P2 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P2.ds-nna-atomic-d02-consumer-cutover | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.CN-P2.ds-nna-atomic-d02-consumer-cutover | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-16 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-blast | comp-blast D_02 | PASS |
| 2026-04-16 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-validate | comp-validate nna_atomic --artifact /tmp/nna_atomic.parquet | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | (no-TO) | comp-blast | comp-blast D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P3.ds-nna-atomic-d00c-leaderboard-cutover | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P3.ds-nna-atomic-d00c-leaderboard-cutover | comp-blast | comp-blast D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P3.ds-nna-atomic-d00c-leaderboard-cutover | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P3.ds-nna-atomic-d00c-leaderboard-cutover | comp-routes | comp-routes behaviors | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.RA-P1b.ds-role-aua-historical-backfill | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~D | ADVI_ROLLUP.RA-P1b.ds-role-aua-historical-backfill | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-iam | comp-iam service bd-gold-qa-runner | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-pipescript | comp-pipescript deployed D_02.advisor_client_detail.py | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-pipescript | comp-pipescript deployed D_02.advisor_client_detail | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-pipescript | comp-pipescript deployed --list | FAIL |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-blast | comp-blast D_00c | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-16 | 0.7.0_AE_CloudOps | ADVI_ROLLUP.IN-2.W0.004 | comp-iam | comp-iam gaps | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-iam | comp-iam gaps | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript deployed D_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast D_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast D_00b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast D_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast D_04 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast timeseries_chart | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast role_aua | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript deployed D_00b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript deployed C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-platinum | comp-platinum reverse role_aua | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-platinum | comp-platinum reverse nna_atomic | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-platinum | comp-platinum reverse role_aua | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-platinum | comp-platinum reverse nna_atomic | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check AdvisorPublicProfile | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check AdvisorPublicProfile | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check AdvisorPublicProfile | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-blast | comp-blast D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check AdvisorsTab | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check FeeSummaryPanel | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check FeeSummaryPanel | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript deployed C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check FeeSummaryPanel | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check FeeEfficiencyPanel | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-transform | comp-transform schema-check FeeEfficiencyPanel | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript deployed C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_00.canonical_holdings | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_01.holdings_lots | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_01b.classify_new_securities | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_02.canonical_lots | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_03.account_gains | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io build_canonical_prices_v2 | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_01b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_04 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io build_canonical_prices_v2 | FAIL |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_01b | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_04 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io A_02 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.CN-P4 | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed C_08.advisor_fee_efficiency | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed C_08 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ARTREF.dispatch-bcd-qa-runner | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ARTREF.dispatch-bcd-qa-runner | comp-pipescript | comp-pipescript deployed C_00 | PASS |
| 2026-04-16 | 0.4.0_DS_ClientPlatform~A | C_08.L429.WAR_ROOM | py_compile | python -m py_compile C_08.advisor_fee_efficiency.py | PASS | exit 0, session H verify-deploy |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ARTREF.dispatch-bcd-qa-runner | comp-pipescript | comp-pipescript io D_02.advisor_client_detail | FAIL |
| 2026-04-16 | 0.6.0_AE_PartnerETL | ADVI_ARTREF.dispatch-bcd-qa-runner | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed D_00b.portal_timeseries.py | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed D_00c.portal_leaderboard.py | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed D_01.partner_analytics.py | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed D_02.advisor_client_detail.py | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed D_00b | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed D_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed C_00 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed data/black_diamond/scripts/gold/B_01.holdings_lots.py | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-16 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | POLARS_INSTALL_RUNNERS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | COUNCIL_C_RPS_FORENSICS | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | COUNCIL_C_RPS_FORENSICS | aws s3 ls | schwab/bronze/ | PASS | last=CRS20260407.RPS, feed-outage confirmed |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | COUNCIL_C_RPS_FORENSICS | aws s3 ls | schwab/silver/rps/ | PASS | last=date=20260407, silver outage confirmed |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~D | COUNCIL_D_SYNTHESIS_2026-04-17 | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/B_01.holdings_lots.py | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~D | COUNCIL_D_SYNTHESIS_2026-04-17 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~D | COUNCIL_D_SYNTHESIS_2026-04-17 | comp-blast | comp-blast B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~D | COUNCIL_D_SYNTHESIS_2026-04-17 | comp-pipescript | comp-pipescript overlap B_01 B_02 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~D | COUNCIL_D_SYNTHESIS_2026-04-17 | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript io merge-daily-incremental | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-PREFLIGHT-BLAST | comp-blast | comp-blast B_01.holdings_lots | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-blast | comp-blast B_01.holdings_lots | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-blast | comp-blast build_holdings_lots_snapshot | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-blast | comp-blast holdings_lots | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-blast | comp-blast _apply_rps_lot_corrections | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-blast | comp-blast save_lots | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-pipescript | comp-pipescript io B_01.holdings_lots | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-pipescript | comp-pipescript consumers B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-blast | comp-blast holdings_lots_key | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-platinum | comp-platinum reverse gold/timeseries/holdings_lots/2026-04-15.parquet | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-DS1 | comp-pipescript | comp-pipescript consumers B_02 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-validate | comp-validate --help | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-validate | comp-validate --list | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | CP-DS1-VALIDATE-GATE | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | ADHOC.nna-overlay-account-modal | comp-transform | comp-transform schema-check AdvisorBookAccountModal | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | ADHOC.nna-overlay-account-modal | comp-transform | comp-transform schema-check AdvisorBookAccountModal | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | ADHOC.nna-overlay-account-modal | comp-blast | comp-blast AdvisorBookAccountModal | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-routes | comp-routes trace getPlatinumAccountSummary | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-platinum | comp-platinum reverse platinum/accounts/{account_id}/summary.json | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-pipescript | comp-pipescript io D_04.client_portal_summary.py | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-transform | comp-transform schema-check AdvisorBookAccountModal | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-pipescript | comp-pipescript io C_03.account_performance.py | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-blast | comp-blast C_03.account_performance | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-pipescript | comp-pipescript consumers C_03 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-pipescript | comp-pipescript deployed C_03 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~E | ADVI_ROLLUP.CP-DS1.ds-b01-cusip-rps-cutover | comp-pipescript | comp-pipescript deployed C_03 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-routes | comp-routes auth-map | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check AdvisorIntelligence | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-blast | comp-blast AdvisorIntelligence | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHOC_RPS_REPRICE | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHOC_RPS_REPRICE | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHOC_RPS_REPRICE | comp-transform | comp-transform schema-check AdvisorsTab | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHOC_RPS_REPRICE | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-17 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-routes | comp-routes auth-map | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-routes | comp-routes behaviors | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-iam | comp-iam service opal-partners-data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-blast | comp-blast lambda:opal-partners-data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-iam | comp-iam service opal_partners_data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-blast | comp-blast lambda:opal_partners_data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-build | comp-build | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-iam | comp-iam --help | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-iam | comp-iam gaps | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1 | comp-blast | comp-blast lambda:opal-partners-data --direction both | FAIL |
| 2026-04-17 | 0.4.0_DE_ClientPlatform | ADVI_ROLGAT.DE1.de-tab-restructure-and-claims-extension | comp-transform | comp-transform schema-check AdvisorIntelligence --feature advisorRole | PASS |
| 2026-04-17 | 0.4.0_DE_ClientPlatform | ADVI_ROLGAT.DE1.de-tab-restructure-and-claims-extension | comp-transform | comp-transform ternary-audit AdvisorIntelligence | PASS |
| 2026-04-17 | 0.4.0_DE_ClientPlatform | ADVI_ROLGAT.DE1.de-tab-restructure-and-claims-extension | comp-blast | comp-blast component:portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx | PASS |
| 2026-04-17 | 0.4.0_DE_ClientPlatform | ADVI_ROLGAT.DE1.de-tab-restructure-and-claims-extension | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-04-17 | 0.4.0_DE_ClientPlatform | ADVI_ROLGAT.DE1.de-tab-restructure-and-claims-extension | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DE_ClientPlatform | ADVI_ROLGAT.DE1.de-tab-restructure-and-claims-extension | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-routes | comp-routes auth-map | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-routes | comp-routes behaviors | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-iam | comp-iam service opal-partners-data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-blast | comp-blast lambda:opal-partners-data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-blast | comp-blast opal-partners-data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-iam | comp-iam service partners-data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-blast | comp-blast partners-data | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-iam | comp-iam services | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-transform | comp-transform schema-check AdvisorIntelligence --feature advisorRole | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-transform | comp-transform ternary-audit AdvisorIntelligence | PASS |
| 2026-04-17 | 0.4.0_DT_ClientPlatform | ADVI_ROLGAT.DT1.dt-auth-claim-and-tier-enforcement | comp-blast | comp-blast component:portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | ADVI_ROLGAT.RD1 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | ADVI_ROLGAT.RD1 | comp-transform | comp-transform fields AdvisorBookView | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | ADVI_ROLGAT.RD1 | comp-iam | comp-iam gaps | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | ADVI_ROLGAT.RD1 | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-17 | 0.4.2_RD_AdvisorIntelligence | ADVI_ROLGAT.RD1 | comp-transform | comp-transform ternary-audit AdvisorBookView | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-iam | comp-iam gaps | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-routes | comp-routes auth-map | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-blast | comp-blast B_01.holdings_lots | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript io D_03.composition_artifacts.py | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript postdeps D_03 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript deployed D_03 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript deployed D_03 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript io C_08.advisor_fee_efficiency | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~XYZ | ds-brief-xyz-undershoot-tapering | comp-platinum | comp-platinum reverse aua_current | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-pipescript | comp-pipescript io C_08.advisor_fee_efficiency | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-pipescript | comp-pipescript deployed C_08 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-pipescript | comp-pipescript deployed C_08 D_00b D_01 D_04 D_00 D_00c D_02 | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-validate | comp-validate --help | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-validate | comp-validate B_01 --artifact .runtmp/holdings_lots_2026-04-15.parquet | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-validate | comp-validate D_04 --artifact /tmp/cs.json | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-validate | comp-validate B_01.holdings_lots | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-validate | comp-validate D_04 --artifact /tmp/afe.json | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-validate | comp-validate B_01.holdings_lots --artifact /tmp/hl.parquet | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | COO_GO_C08_aua_current_growth_backfill | comp-validate | comp-validate D_04 --artifact /tmp/lb.json | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_02.advisor_client_detail | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00c.portal_leaderboard | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04.client_portal_summary | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHC_DIAG.firm-nna-historical-overshoot | comp-platinum | comp-platinum reverse firm/timeseries | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHC_DIAG.firm-nna-historical-overshoot | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/D_00b.portal_timeseries.py | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHC_DIAG.firm-nna-historical-overshoot | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/C_01.canonical_nna.py | FAIL |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHC_DIAG.firm-nna-historical-overshoot | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-17 | 0.4.0_DS_ClientPlatform | ADHC_DIAG.firm-nna-historical-overshoot | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-20 | 1.0.0_SA_CTO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-20 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py | FAIL |
| 2026-04-20 | 1.0.0_SA_CTO | (no-TO) | comp-platinum | comp-platinum reverse platinum/firm/leaderboard.json | PASS |
| 2026-04-20 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-20 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-20 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-build | comp-build | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-build | comp-build | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-build | comp-build | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-build | comp-build | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-build | comp-build | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io merge-daily-incremental | FAIL |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-build | comp-build | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast C_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-build | comp-build | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-build | comp-build | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast D_00c | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast D_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast C_08 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast employee_leaderboard | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast platinum/firm/leaderboard.json | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast _weighted_aua | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-trace | comp-trace tagged_aua --direction both | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast A_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast A_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast A_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-platinum | comp-platinum reverse tagged_aua | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-platinum | comp-platinum reverse fee_breakdown.no_fee.aua | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-platinum | comp-platinum reverse aua_growth_pct | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast accounts_dimension_latest | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast advisor_assignments_history | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast client_dimension | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-cache | comp-cache collisions | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-transform | comp-transform schema-check AdvisorsTab | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-transform | comp-transform schema-check AdvisorIntelligence | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast C_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast C_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.B | comp-blast | comp-blast C_08 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-build | T0 544877cc | 1162 nodes/940 edges | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-build | T1 f177240b | 1162 nodes/940 edges | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-build | T2 ae759bbb | 1162 nodes/940 edges | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-build | T3 cd177553 | 1162 nodes/940 edges | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-pipescript io | T0 A_00 | no COLUMN GAPS; READS(1) WRITES(1) | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-pipescript io | T0 A_01 | no COLUMN GAPS; READS(1) WRITES(1) | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-pipescript io | T0 A_02 | no COLUMN GAPS; READS(0) WRITES(1) | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-pipescript io | T0 A_03 | no COLUMN GAPS; READS(0) WRITES(2) | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-pipescript io | T0 A_04 | no COLUMN GAPS; READS(1) WRITES(1) | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-pipescript io | T3 A_00-A_04 | IDENTICAL to T0 — confirmed no change | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.A | comp-blast | T0 accounts_dimension_latest | 4 downstream nodes | orientation |

## 2026-04-20 — ADVI_STAUDT.C Layer C Audit (0.4.0_DS_ClientPlatform~C)

| Date | Agent | TO | Tool | Command | Result | Note |
|------|-------|----|------|---------|--------|------|
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | git worktree add | T0-T3 (544877cc/f177240b/ae759bbb/cd177553) | PASS | 4 worktrees at C:/tmp/staudt_layerC_T{0-3} |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | comp-build | T0 worktree | PARTIAL | 1162 nodes / 940 edges — caches to main repo root regardless of worktree CWD; graph identical at all 4 checkpoints |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | comp-build | T1/T2/T3 worktrees | PARTIAL | Same limitation — T3 graph cache used for all; node/edge count correct (1162/940 uniform) |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | comp-pipescript io | C_01 T0/T1/T2/T3 | PARTIAL | Returns cached T3 graph regardless of checkpoint; supplemented with direct source grep per worktree |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | comp-pipescript io | C_00 T0/T1 | PARTIAL | Same T3 cache limitation; IO confirmed identical via source diff (no IO change in polars port) |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | comp-pipescript io | C_03 T2/T3 | PARTIAL | T3 cache; per-checkpoint IO confirmed identical via source diff (computation change only) |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | comp-pipescript io | C_08 T0/T1/T3 | PARTIAL | T3 cache; NNA path diff (nna/ vs nna_atomic/) captured via direct source grep on each worktree |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | comp-blast | C_00/C_01/C_03/C_08 | FAIL | All returned "No downstream consumers" — blast requires function node name, not script name; script nodes have no edges in graph |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | aws s3 ls | nna/ nna_atomic/ role_aua/ partition counts | PASS | 2297 / 2296 / 2295 partitions; Apr 14 gap confirmed in nna_atomic/ and role_aua/ |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.C | aws s3api list-object-versions | account_performance.parquet | PASS | Pre-fix (vKXe5n7FVfVR, Apr 15 14:48 ET) and post-fix (BUUH_GmTJcuc, Apr 17 15:43 ET) retrieved; confirmed S3 versioning enabled on opal-data-bd |
| 2026-04-20 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript io D_00c.portal_leaderboard | FAIL |
| 2026-04-20 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-20 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-20 | 0.6.0_AE_PartnerETL | ADVI_STAUDT.INV1 | comp-pipescript | comp-pipescript io C_01.canonical_nna | FAIL |
| 2026-04-20 | 0.6.0_AE_PartnerETL | ADVI_STAUDT.INV1 | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-20 | 0.6.0_AE_PartnerETL | ADVI_STAUDT.INV1 | comp-pipescript | comp-pipescript io D_00c.portal_leaderboard | FAIL |
| 2026-04-20 | 0.6.0_AE_PartnerETL | ADVI_STAUDT.INV1 | comp-blast | comp-blast _compute_split_weight | PASS |
| 2026-04-20 | 0.6.0_AE_PartnerETL | ADVI_STAUDT.INV1 | comp-blast | comp-blast _weighted_aua | PASS |
| 2026-04-20 | 0.6.0_AE_PartnerETL | ADVI_STAUDT.INV1 | comp-pipescript | comp-pipescript deployed C_01.canonical_nna | PASS |
| 2026-04-20 | 0.6.0_AE_PartnerETL | ADVI_STAUDT.INV1 | comp-pipescript | comp-pipescript deployed C_01 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast D_04 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast timeseries_chart | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam --help | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service exec-summary-generator | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam roles | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_00c --artifact /tmp/leaderboard.json | FAIL |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_00c --artifact /tmp/leaderboard.json | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py | FAIL |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_00c --artifact C:/Users/ANDREW~1/AppData/Local/Temp/elb.json | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_00c --artifact C:/Users/ANDREW~1/AppData/Local/Temp/elb_fresh.json | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/Users/ANDREW~1/AppData/Local/Temp/pl_lb.json | FAIL |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check AdvisorPublicProfile | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-20 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.FIX2 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.FIX2 | comp-validate | comp-validate D_00c --artifact /tmp/lb_post_fix1_2026-04-20.json | FAIL |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.FIX2 | comp-validate | comp-validate D_00c --artifact data/black_diamond/diagnostics/STAUDT/FIX2/lb_post_fix2_... | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.FIX2 | comp-validate | comp-validate D_00c --artifact data/black_diamond/diagnostics/STAUDT/FIX2/lb_post_fix2_... | PASS |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | comp-blast | comp-blast B_00 | PASS |
| 2026-04-20 | 1.0.0_SA_CTO~Z | COMP_LEARNS.016 | comp-pipescript | comp-pipescript io build_canonical_prices_v2 | FAIL |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.KPI | comp-platinum | comp-platinum reverse aua.monthly | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.KPI | comp-platinum | comp-platinum reverse aua_current | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.KPI | comp-platinum | comp-platinum reverse timeseries_chart | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.KPI | comp-platinum | comp-platinum reverse canonical_nna | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.KPI | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.KPI | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~C | ADVI_STAUDT.KPI | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed D_02.advisor_client_detail.py | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript io D_02.advisor_client_detail.py | FAIL |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed D_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed D_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript deployed D_02 | PASS |

| 2026-04-20 | 0.4.2_RD_AdvisorIntelligence | multi-loop | comp-pipescript | deployed D_01 | MATCH | disproved deploy-gap hypothesis for partner_analytics donut.total cohort inconsistency |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | adhoc_iefa_idvz_top_holdings_pct | comp-pipescript | comp-pipescript deployed D_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-blast | comp-blast holdings_lots | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-blast | comp-blast gold/holdings_lots/*.parquet | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-blast | comp-blast holdings_lots_key | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-blast | comp-blast gold:holdings_lots | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-blast | comp-blast --help | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-pipescript | comp-pipescript deployed D_00 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-20 | 0.4.0_DS_ClientPlatform~A | STAUDT.HLOT1_phase0_frontrun | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-blast | comp-blast holdings_lots | PASS |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-blast | comp-blast gold:holdings_lots | PASS |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-blast | comp-blast B_01 | PASS |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-transform | comp-transform schema-check FirmOverviewTab | FAIL |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-platinum | comp-platinum reverse platinum/firm/firm_composition.json | PASS |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-transform | comp-transform schema-check BooksTab | FAIL |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-transform | comp-transform schema-check FirmOverview | FAIL |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-platinum | comp-platinum reverse firm_composition | PASS |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-cache | comp-cache collisions | PASS |
| 2026-04-21 | 2.0.0_SA_COO | ADVI_STAUDT.HLOT2 | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.HLOT2 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.HLOT2 | comp-platinum | comp-platinum reverse platinum/firm/firm_composition.json | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~A | ADVI_STAUDT.HLOT2 | comp-cache | comp-cache collisions | PASS |
| 2026-04-21 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-platinum | comp-platinum page MarketPerformance | PASS |
| 2026-04-21 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-21 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-blast | comp-blast holdings_lots | PASS |
| 2026-04-21 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-04-21 | 1.0.0_SA_CTO | TRDP_CLEANUP_PRD | comp-iam | comp-iam service trade-submission-handler | PASS |
| 2026-04-21 | 1.0.0_SA_CTO | TRDP_CLEANUP_PRD | comp-iam | comp-iam service trade-workflow-handler | PASS |
| 2026-04-21 | 1.0.0_SA_CTO | TRDP_CLEANUP_PRD | comp-iam | comp-iam gaps | PASS |
| 2026-04-21 | 1.0.0_SA_CTO | TRDP_CLEANUP_PRD | comp-routes | comp-routes trace trade-submission-handler | PASS |
| 2026-04-21 | 1.0.0_SA_CTO | TRDP_CLEANUP_PRD | comp-blast | comp-blast trade-submission-handler | PASS |
| 2026-04-21 | 0.1.0_DS_MarketIntelligence | MKOV_CLOUD.001.daily-cloud-fix | comp-blast | comp-blast news-trending-analysis | PASS |
| 2026-04-21 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-21 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace opal-portal-data-proxy | PASS |
| 2026-04-21 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-21 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-21 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W1 | comp-iam | comp-iam service trade-submission-handler | PASS |
| 2026-04-21 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W1 | comp-routes | comp-routes trace /api/general/trades/submit | PASS |
| 2026-04-21 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W1 | comp-routes | comp-routes behaviors | PASS |
| 2026-04-21 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W1 | comp-routes | comp-routes trace trade-submission-handler | PASS |
| 2026-04-21 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W1 | comp-blast | comp-blast lambda:trade-submission-handler | PASS |
| 2026-04-21 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W1 | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-21 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W1 | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | (no-TO) | comp-pipescript | comp-pipescript io B_02 --no-portal | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | (no-TO) | comp-pipescript | comp-pipescript io A_03 --no-portal | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | (no-TO) | comp-pipescript | comp-pipescript io B_00 --no-portal | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | (no-TO) | comp-pipescript | comp-pipescript io D_01 --no-portal | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | (no-TO) | comp-pipescript | comp-pipescript io B_03 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-xref | comp-xref comp/framework/compiler_contract.py | FAIL |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-xref | comp-xref --help | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-blast | comp-blast --help | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-blast | comp-blast comp/framework/compiler_contract.py | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-blast | comp-blast comp/framework/extractor_interface.py | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-xref | comp-xref | FAIL |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io B_02 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io B_03 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io B_00 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io D_01 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io D_04 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io D_01 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io B_02 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io B_03 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io B_00 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-pipescript | comp-pipescript io D_01 --no-portal | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-xref | comp-xref comp/ir/schema.py | FAIL |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.011.module-skeleton-core-contracts | comp-blast | comp-blast comp/framework/extractor_interface.py | PASS |
| 2026-04-21 | 1.1.0_DS_CompLearns | COMP_LEARNS.012.python-parser-libcst | comp-xref | comp-xref | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-xref | comp-xref comp/bench/mutations/ | FAIL |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-xref | comp-xref mutations | FAIL |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-xref | comp-xref comp.bench.mutations | FAIL |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-build | comp-build | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-xref | comp-xref harness | FAIL |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-xref | comp-xref --help | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-xref | comp-xref | FAIL |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-pipescript | comp-pipescript deployed C_01 | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.021.mutation-engine | comp-pipescript | comp-pipescript deployed C_01 | PASS |
| 2026-04-21 | 1.1.0_SA_CTO | (no-TO) | comp-xref | comp-xref comp/compiler_subtypes/imports.py | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | (no-TO) | comp-xref | comp-xref --help | PASS |
| 2026-04-21 | 1.3.0_DS_CompLearns | COMP_LEARNS.014.graph-builder | comp-xref | comp-xref --json | PASS |
| 2026-04-21 | 1.3.0_DS_CompLearns | COMP_LEARNS.014.graph-builder | comp-xref | comp-xref | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-build | comp-build | PASS |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref comp/bench/ab.py | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref comp.bench.ab | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref comp/bench/selectors/ | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref --help | PASS |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref comp/graph_builder/build.py | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref build | FAIL |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref --help | PASS |
| 2026-04-21 | 1.1.0_SA_CTO | COMP_LEARNS.020.cto-selector-benchmarking-harness | comp-xref | comp-xref | PASS |
| 2026-04-21 | 1.1.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript deployed B_00 B_01 | FAIL |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.CHART-ALIGN | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.CHART-ALIGN | comp-blast | comp-blast D_00c | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.CHART-ALIGN | comp-blast | comp-blast comp/targets/httpx/compiler.py | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.COHORT-A | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.COHORT-A | comp-blast | comp-blast D_04 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.COHORT-A | comp-platinum | comp-platinum reverse cohort_a_summary | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-routes | comp-routes auth-map | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-routes | comp-routes trace bd-portal-publisher | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-routes | comp-routes trace bd-portal-advisor-publisher | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.D | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.026 | comp-iam | comp-iam service opal-portal-data-proxy-api | PASS |
| 2026-04-21 | 1.4.0_DS_CompLearns | COMP_LEARNS.026 | comp-iam | comp-iam service opalinvest-auth-handler | PASS |
| 2026-04-21 | 1.3.0_DS_CompLearns | COMP_LEARNS.025.compare-explainability-and-cache-provenance | comp-blast | comp-blast ratchet | PASS |
| 2026-04-21 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-21 | 2.0.0_SA_COO | (no-TO) | comp-blast | comp-blast opalinvest-auth-handler | PASS |
| 2026-04-21 | 2.0.0_SA_COO | (no-TO) | comp-blast | comp-blast auth-validator-edge | PASS |
| 2026-04-21 | 2.0.0_SA_COO | (no-TO) | comp-blast | comp-blast shared-advisor-router | PASS |
| 2026-04-21 | 2.0.0_SA_COO | (no-TO) | comp-blast | comp-blast opal-partners-data | PASS |
| 2026-04-21 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-21 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript deployed C_01 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed C_01 | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-21 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed gold_dispatch.sh | PASS |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed B_00 B_01 C_01 D_00 D_00b D_00c D_02 D_04 | FAIL |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed C_01 | PASS |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_00 | PASS |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-21 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-21 | 0.4.0_DE_ClientPlatform | ADVI_STAUDT.CHART-ALIGN-FE.de-caveat-removal | comp-pipescript | comp-pipescript deployed gold_dispatch.sh | PASS |
| 2026-04-21 | 0.7.0_AE_CloudOps | ADVI_INFLEC.W1.2.ae-terraform-workspace-inf-pipeline | comp-transform | comp-transform schema-check AdvisorIntelligence | PASS |
| 2026-04-21 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W1.8.dt-partner-schema-inflection-doc | comp-transform | comp-transform fields AdvisorIntelligence | PASS |
| 2026-04-21 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W1.8.dt-partner-schema-inflection-doc | comp-iam | comp-iam gaps | PASS |
| 2026-04-21 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W1.8.dt-partner-schema-inflection-doc | comp-transform | comp-transform schema-check AdvisorIntelligence | PASS |
| 2026-04-21 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W1.8.dt-partner-schema-inflection-doc | comp-iam | comp-iam service opalinvest-auth-handler | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check AdvisorIntelligence | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-blast | comp-blast AdvisorIntelligence | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check AdvisorIntelligence | FAIL |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check --list | FAIL |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-iam | comp-iam service inf-portal-publisher | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-iam | comp-iam service inf-portal-advisor-publisher | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-iam | comp-iam service inf-client-detail | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-iam | comp-iam service opalinvest-auth-handler | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed C_01.canonical_nna.py | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed C_01 | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_00c D_00 D_03 | FAIL |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_00 | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_03 | PASS |
| 2026-04-21 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed I_00 | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-validate | comp-validate I_09 --artifact /tmp/partner_analytics.json | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed C_01 | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform ternary-audit AdvisorIntelligence | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform ternary-audit PartnerAnalytics | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform ternary-audit AdvisorsTab | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check AdvisorIntelligence | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check --list | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform list | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check AdvisorIntelligencePage | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check advisor-intelligence | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform stats | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check AdvisorsTab | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform ternary-audit DistributionTab | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform ternary-audit AdvisorsTab | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check AdvisorIntelligence | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check InflectionAdvisorIntelligence | FAIL |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check AdvisorsTab | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.AUAGAP.001 | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~D | ADVI_STAUDT.AUAGAP.001 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-22 | 1.1.0_SA_CTO | COMP_LEARNS.032.pilot-wave-execution | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-22 | 1.1.0_SA_CTO | COMP_LEARNS.032.pilot-wave-execution | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-22 | 1.1.0_SA_CTO | COMP_LEARNS.032.pilot-wave-execution | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-22 | 1.1.0_SA_CTO | COMP_LEARNS.032.pilot-wave-execution | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-22 | 1.1.0_SA_CTO | COMP_LEARNS.032.pilot-wave-execution | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | schwab-rps-backfill-2025 | comp-pipescript | comp-pipescript deployed gold_dispatch.sh | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed B_00.canonical_holdings | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed C_03 D_00b D_00c D_02 D_04 | FAIL |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed C_03 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed D_00b | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed B_03 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed C_03 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | HOTFIX_GOLD_GATE | comp-pipescript | comp-pipescript deployed C_03 | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed B_03 | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed C_02 | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed C_03 | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-validate | comp-validate C_03 | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-validate | comp-validate C_03 --artifact /tmp/account_performance.parquet | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed C_00 | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed data/orion/scripts/gold/build_canonical_prices_inf.py | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed news-trending-analysis | PASS |
| 2026-04-22 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-pipescript | comp-pipescript deployed news-layer3-curation | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript deployed gold_dispatch.sh | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-blast | comp-blast partner-firm | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-blast | comp-blast opal-users-v2 | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace getPositioningData | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace getMacroData | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace getCMAAssumptions | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace /v1/positioning/data | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace Positioning | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check CapitalMarketAssumptions | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check Positioning | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check Macroeconomics | PASS |
| 2026-04-22 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.W8.1 | comp-transform | comp-transform schema-check CapitalMarketAssumptions | PASS — 0 MISSING |
| 2026-04-22 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.W8.1 | comp-transform | comp-transform schema-check Positioning | PASS — 0 MISSING |
| 2026-04-22 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.W8.1 | comp-transform | comp-transform schema-check Macroeconomics | PASS — 0 MISSING |
| 2026-04-22 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.W8.1 | comp-cache | comp-cache collisions | PASS — no new collisions added by 3 pages |
| 2026-04-22 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.W8.4 | manual-ddb-scan | aws dynamodb scan opal-partner-inflection | PASS — 2 real-identity rows (1 admin + 1 user) |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.3 | comp-routes | comp-routes behaviors | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.3 | comp-routes | comp-routes auth-map | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.3 | comp-transform | comp-transform schema-check Macroeconomics | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-pipescript | comp-pipescript consumers B_01 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-pipescript | comp-pipescript consumers B_01.canonical_holdings | FAIL |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-pipescript | comp-pipescript feeds B_01.canonical_holdings | FAIL |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-pipescript | comp-pipescript consumers B_01.holdings_lots | FAIL |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-pipescript | comp-pipescript deployed B_01.holdings_lots.py | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-validate | comp-validate B_01 --artifact C:/Users/AndrewBerman/AppData/Local/Temp/gold_hl_0420.par... | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-build | comp-build | PASS |
| 2026-04-22 | 0.6.0_AE_PartnerETL | AUAGAP.002-ae-d-chain-backfill | comp-build | comp-build | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-RES20 | comp-build | comp-build | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-RES20 | comp-pipescript | comp-pipescript io D_04.client_portal_summary | FAIL |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.CP-RES20 | comp-platinum | comp-platinum reverse cash_coverage_summary | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-blast | comp-blast D_04.client_portal_summary | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.HLOT2b | comp-pipescript | comp-pipescript deployed B_01.holdings_lots.py | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.HLOT2b | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.HLOT2b | comp-validate | comp-validate D_04 --artifact C:/Users/AndrewBerman/AppData/Local/Temp/cash_coverage_su... | FAIL |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.HLOT2b | comp-validate | comp-validate --list | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.HLOT2b | comp-validate | comp-validate cash_coverage_summary --artifact C:/Users/AndrewBerman/AppData/Local/Temp... | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~B | ADVI_STAUDT.HLOT2b | comp-validate | comp-validate cash_coverage_summary --artifact C:/Users/AndrewBerman/AppData/Local/Temp... | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-routes | comp-routes auth-map | PASS |
| 2026-04-22 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 1.0.0_SA_CTO | startup-reconciliation | N/A (startup scan, no PRD authored) | N/A | N/A — reconciliation session, comp-* mandated at PRD authoring |
| 2026-04-22 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-22 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-22 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.2.dt-frontend-dev-cross-firm-pages | comp-routes | comp-routes behaviors | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.2.dt-frontend-dev-cross-firm-pages | comp-blast | comp-blast B_01.holdings_lots.py | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.2.dt-frontend-dev-cross-firm-pages | comp-routes | comp-routes behaviors | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-blast | comp-blast B_01 | PASS |
| 2026-04-22 | 0.6.1_AE_PartnerETL | (no-TO) | comp-blast | comp-blast holdings_lots | PASS |
| 2026-04-22 | 2.1.0_SC_CompLearns | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-22 | 2.1.0_SC_CompLearns | (no-TO) | comp-blast | comp-blast build_holdings_lots | PASS |
| 2026-04-22 | 2.1.0_SC_CompLearns | (no-TO) | comp-platinum | comp-platinum reverse price_quality | PASS |
| 2026-04-22 | 0.4.0_DE_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/Users/AndrewBerman/AppData/Local/Temp/cohort_a_summary... | FAIL |
| 2026-04-22 | 0.4.0_DE_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript consumers B_01 | PASS |
| 2026-04-22 | 0.4.0_DE_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact C:/Users/AndrewBerman/AppData/Local/Temp/coho... | PASS |
| 2026-04-22 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.W3.1.ds-silver-schema-scoping | comp-platinum | comp-platinum reverse gold/timeseries_chart.json | PASS |
| 2026-04-22 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io I_00 | FAIL |
| 2026-04-22 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io C_01b | PASS |
| 2026-04-22 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript deployed C_01c | PASS |
| 2026-04-22 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript deployed C_01c | PASS |
| 2026-04-22 | 0.7.0_AE_CloudOps | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.2 | comp-routes | comp-routes behaviors | PASS — 2 custom error responses: 403→200/index.html + 404→200/index.html; documented in all constitutions |
| 2026-04-22 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.2 | comp-cache | comp-cache collisions | PASS — 4 pre-existing collisions in AdvisorIntelligence (firmOverride-scoped, intentional); zero new collisions on /cma /positioning /macro |
| 2026-04-22 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate --list | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pipescript | comp-pipescript deployed inf-gold-dispatch | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-build | comp-build | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-validate | comp-validate --help | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-validate | comp-validate --list | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pii | comp-pii audit platinum/advisors/* | FAIL |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pii | comp-pii --help | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pii | comp-pii audit --help | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pii | comp-pii audit | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-platinum | comp-platinum reverse leaderboards.prior_week | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-blast | comp-blast template_library | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-blast | comp-blast A_00 | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-validate | comp-validate C_01c --artifact /tmp/role_aua_sample.parquet | FAIL |
| 2026-04-24 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.W4.13 | comp-validate | comp-validate C_01c --artifact C:/tmp/role_aua_sample.parquet | FAIL |
| 2026-04-24 | 1.0.0_SA_CTO | (startup) | N/A — CTO ground-truth reconciliation; compiler tools mandated at PRD authoring, not startup | PASS |
| 2026-04-24 | 0.5.0_AE_OpalETL | TRSB_TFIMPT.W2 | comp-build | comp-build | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-iam | comp-iam service trade-parquet-batch-export | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-iam | comp-iam service trade-parquet-batch-export | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-iam | comp-iam service trade-dashboard-api | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-build | comp-build | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-iam | comp-iam service trade-parquet-batch-export | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-iam | comp-iam gaps | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-pipescript | comp-pipescript deployed convert_orion_to_silver | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-platinum | comp-platinum reverse platinum/advisors/*/positions.json | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-pipescript | comp-pipescript consumers D_04 | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-platinum | comp-platinum page AdvisorPublicProfile | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-platinum | comp-platinum reverse platinum/advisors/*/summary.json | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-platinum | comp-platinum reverse platinum/advisors/*/positions.json | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-24 | 1.0.0_SA_CTO | ADVI_49EXEC.PRD-amend | comp-platinum reverse | comp-platinum reverse 'platinum/advisors/*/positions.json' | PASS (surfaced empty producer, confirming COO's pre-TO study; drove PRD §4.5 amendment) |
| 2026-04-24 | 1.0.0_SA_CTO | ADVI_49EXEC.PRD-amend | comp-pipescript io | comp-pipescript io D_04 | PASS (confirmed D_04 reads holdings_lots + account_team + accounts_dimension; producer recommendation for new positions.json artifact) |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-platinum | comp-platinum reverse platinum/advisors/*/positions.json | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-blast | comp-blast D_04.client_portal_summary | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-validate | comp-validate D_04 --artifact C:/tmp/positions_sample_travis.json | FAIL |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-validate | comp-validate D_04_positions_output --artifact C:/tmp/positions_sample_travis.json | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-platinum | comp-platinum reverse cost_basis | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-platinum | comp-platinum reverse is_opal_model | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-platinum | comp-platinum reverse top_positions | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-routes | comp-routes behaviors | PASS |
| 2026-04-24 | 0.7.0_AE_CloudOps | TRSB_TFIMPT.W2 | comp-routes | comp-routes auth-map | PASS |
| 2026-04-24 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.3 | comp-routes | comp-routes behaviors | PASS — 2 custom error responses (403+404 -> 200/index.html); informed curl pass criterion (JSON CT required, HTML body = FAIL regardless of HTTP 200) |
| 2026-04-24 | 0.4.0_DT_ClientPlatform | ADVI_INFLEC.W8.3 | comp-routes | comp-routes auth-map | PASS — /api/general/* confirmed EDGE JWT + API GW AUTHORIZER; no-auth baseline 401 verified |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-blast | comp-blast orion-bronze-runner | PASS |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript io convert_orion_to_silver | FAIL |
| 2026-04-24 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-24 | 1.0.0_SA_CTO | (no-TO) | comp-blast | comp-blast B_01 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.ASSETCLASSc | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_ROLLUP.ASSETCLASSc | comp-blast | comp-blast B_01 | PASS |
| 2026-04-24 | 2.1.0_SC_CompLearns | COMP_LEARNS.060 | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-24 | 2.1.0_SC_CompLearns | COMP_LEARNS.060 | comp-blast | comp-blast C_01 | PASS |
| 2026-04-24 | 2.0.0_SA_COO | /loop ADVI wake 1 | comp-pipescript io C_01 | READS: ACCOUNTS_DIMENSION/CANONICAL_NNA_PREFIX/etc; WRITES: canonical_nna_atomic_key (already in production CN-P1) | PASS — nna_atomic key exists, no collision | CANNNA Phase 0/1 confirmed complete; project JSON corrected |
| 2026-04-24 | 2.0.0_SA_COO | /loop ADVI wake 1 | comp-blast C_01 | No downstream consumers for C_01.canonical_nna | PASS — shadow artifact, terminal | Phase 2 TOs safe to issue without blast-radius conflict |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-blast | comp-blast B_01 | PASS |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-transform | comp-transform schema-check AdvisorsTab | PASS |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-transform | comp-transform schema-check AdvisorIntelligence | FAIL |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-24 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-blast | comp-blast B_01 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript deployed | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript postdeps D_04 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-blast | comp-blast holdings_lots | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-validate | comp-validate D_04 --artifact C:/Users/ANDREW~1/AppData/Local/Temp/cohort_a_summary.json | FAIL |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-validate | comp-validate --help | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-validate | comp-validate cohort_a_summary --artifact C:/Users/ANDREW~1/AppData/Local/Temp/cohort_a... | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-blast | comp-blast D_04 | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-validate | comp-validate gold_silver_recon --artifact C:/Users/ANDREW~1/AppData/Local/Temp/cohort_... | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-validate | comp-validate gold_silver_recon --artifact C:/Users/ANDREW~1/AppData/Local/Temp/gold_si... | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADHC_DSFLOW.004 | comp-pipescript | comp-pipescript deployed I_C00 | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_STAUDT.COHORT-A | comp-platinum | comp-platinum reverse cohort_a_summary | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_STAUDT.COHORT-A | comp-transform | comp-transform schema-check FirmOverview | FAIL |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_STAUDT.COHORT-A | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_STAUDT.COHORT-A | comp-cache | comp-cache collisions | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_STAUDT.COHORT-A | comp-blast | comp-blast AdvisorIntelligence | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.002 | comp-pipescript | comp-pipescript deployed data/orion/scripts/gold/I_D00c.portal_leaderboard.py | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.002 | comp-pipescript | comp-pipescript deployed data/orion/scripts/gold/I_D04.client_portal_summary.py | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.002 | comp-platinum | comp-platinum page AdvisorPublicProfile | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.004 | comp-cache | comp-cache collisions | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.004 | comp-iam | comp-iam service exec-summary-generator | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.004 | comp-pii | comp-pii audit | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.004 | comp-cache | comp-cache collisions | PASS |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | ds-commit-gate | ds-commit-gate config.py | PASS | py_compile + AST + ruff all exit 0 |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | ds-commit-gate | ds-commit-gate platinum_reader.py | PASS | exit 0 |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | ds-commit-gate | ds-commit-gate validator.py | PASS | exit 0 |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | ds-commit-gate | ds-commit-gate metrics.py | PASS | exit 0 |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | ds-commit-gate | ds-commit-gate lambda_function.py | PASS | exit 0 |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | pytest | pytest tests/exec_summary/test_llm_generator.py -v | PASS | 62/62 -- all 8 test classes |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | comp-iam | comp-iam service exec-summary-generator | SKIPPED | No graph entry expected -- TO 4 DT provisions IAM |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | comp-pii | comp-pii audit | PASS | 0 cleartext fields in new Lambda |
| 2026-04-24 | 0.4.0_DS_ClientPlatform | ADVI_49EXEC.002 | comp-cache | comp-cache collisions | PASS | 0 new cache key collisions |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.004 | comp-pipescript | comp-pipescript deployed data/orion/scripts/gold/I_C00.canonical_performance.py | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.004 | comp-iam | comp-iam service exec-summary-generator | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.004 | comp-iam | comp-iam service exec-summary-generator | PASS |
| 2026-04-24 | 0.4.0_DE_ClientPlatform | ADVI_RDVSDS.004 | comp-iam | comp-iam gaps | PASS |
| CTO-STARTUP-2026-04-27 | git log + MCP org scan + query_project (6 projects) | 1.0.0_SA_CTO | 2026-04-27 | 7 doc corrections committed a3a26d79 |
| 2026-04-27 | 0.6.0_AE_PartnerETL | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-27 | 0.4.0_DT_ClientPlatform | ADVI_49EXEC.007.dt-eventbridge-wiring-and-deploy | comp-routes | comp-routes trace exec-summary-generator | PASS |
| 2026-04-27 | 0.4.0_DT_ClientPlatform | ADVI_49EXEC.007.dt-eventbridge-wiring-and-deploy | comp-trace | comp-trace exec-summary-generator --direction both | PASS |
| 2026-04-27 | 0.4.0_DT_ClientPlatform | ADVI_49EXEC.007.dt-eventbridge-wiring-and-deploy | comp-iam | comp-iam gaps | PASS |
| 2026-04-27 | 0.6.0_AE_PartnerETL | ADVI_INFLEC.W4.13b.ae-inflec-ic00-run4-dchain | comp-pipescript | comp-pipescript deployed I_C00 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADHC_OWNPTH.sweep-fix.record-terraform-deploy | bash -n | bash -n infra/aws/lambda/ci/record-terraform-deploy.sh | PASS — syntax clean; no gold/lambda/iam work this session |
| 2026-04-27 | 1.4.0_DS_CompLearns | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-27 | 1.4.0_DS_CompLearns | (no-TO) | comp-validate | comp-validate I_09 --artifact /tmp/inflec_partner_analytics.json | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-iam | comp-iam service inf-exporter | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-iam | comp-iam service inf-otp-relay | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-routes | comp-routes trace headerMetrics | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-cache | comp-cache collisions | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-routes | comp-routes trace headerMetrics | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-iam | comp-iam service auth-validator-edge | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-iam | comp-iam gaps | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-routes | comp-routes trace getTimeseriesOverview | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-routes | comp-routes trace getFirmLeaderboard | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-routes | comp-routes trace getDashboard | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed A_00 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed A_01 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed A_03 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed C_00 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed C_07 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed D_02 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed 09 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed orion-gold-dispatch | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript deployed A_00.accounts_dimension.py | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-blast | comp-blast C_07 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-build | comp-build | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-routes | comp-routes behaviors | PASS |
| 2026-04-27 | 0.7.0_AE_CloudOps | TRSB_PATHFIX.TO-1 | comp-routes | comp-routes behaviors (pre-change baseline) | PASS — 23 behaviors, /api/general/trades/* -> APIGateway-portal confirmed |
| 2026-04-27 | 0.7.0_AE_CloudOps | TRSB_PATHFIX.TO-1 | comp-routes | comp-routes behaviors (post-route-add) | PASS — 23 behaviors unchanged |
| 2026-04-27 | 0.7.0_AE_CloudOps | ADVI_INFLEC.TO-A.ae-orion-infra-audit | comp-routes | comp-routes behaviors | PASS |
