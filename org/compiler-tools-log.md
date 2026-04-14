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
