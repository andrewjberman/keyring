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

**Synthetic test fixtures (forward-only convention; ADHC_COMPIL_V4.016 ship 2026-05-08 PM):**

Test-fixture runs (deliberately-failing inputs during tool-development testing) MUST include `(SYNTHETIC TEST FIXTURE) <description>` in the NOTE column. This distinguishes intentional test failures from real agent-encountered failures during retrospective analysis.

Example:
```
| 2026-04-30 | 0.4.0_DS~A | (no-TO) | comp-validate | comp-validate definitely_not_a_thing | FAIL | (SYNTHETIC TEST FIXTURE) ADHC_COMPIL.012 invalid-script-name regression test |
```

Rationale: the 2026-04-30 v3 testing day produced ~15 synthetic FAILs that inflated the comp-validate raw FAIL rate from 29% real → 36.7% raw across the full corpus. Forward-only — pre-2026-05-08 entries can be retroactively annotated by their authors when next touched, but no backfill required.

See: `docs/architecture/ADHC_COMPIL_FULL_CORPUS_RETROSPECTIVE.md` §1.4 + `org/modules/graph/comp-tools.yaml` for full methodology.

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
| 2026-04-28 | 2.0.0_SA_COO | ADVI_INFSHIP | comp-iam | comp-iam gaps | PASS |
| 2026-04-28 | 2.0.0_SA_COO | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_00c.portal_leaderboard.py | PASS |
| 2026-04-28 | 0.4.0_DS_ClientPlatform~D | INFSHIP.B3-DEP-1+B1 | comp-pipescript | comp-pipescript io | FAIL |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-iam | comp-iam service inf-jwt-trigger | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io griffe_wave1_aggregator.py | FAIL |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript deployed griffe_wave1_aggregator.py | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript io inf-gold-dispatch | FAIL |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-blast | comp-blast B_01 | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-validate | comp-validate --help | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-validate | comp-validate --list | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_05 | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_06 | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_07 | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | ADHC_BASHFIX.001 | (none) | bash -n on 43 local-runtime .sh + which/grep utility audit | PASS-AUDIT-ONLY | Orchestration + ruling + project authoring session; bash-audit metadata-not-graph; no comp-* covers shell-script utility surface (candidate for future tooling, out of scope ADHC_BASHFIX). Session log: oriapi_day2_ruling_bashfix_registration_loopq_catalog.md |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-29 | 1.0.0_SA_CTO | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-29 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/Windows/Temp/cohort_a_summary.json | FAIL |
| 2026-04-29 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact C:/Windows/Temp/cohort_a_summary.json | PASS |

## prd-evidence-check --baseline | 2026-04-29T15:15:10Z

| Status | File | Notes |
|--------|------|-------|
| WARN | ADHC_BASHFIX.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADHC_COMPIL.md | missing-s5-header |
| WARN | ADHC_COMPIL_V2.md | missing-s5-header |
| WARN | ADHC_DSFLOW.md | missing-s5-header |
| WARN | ADHC_HISTRY_schwab_bucket_design.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADHC_OWNPTH.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADHC_TMSTEL_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_49FN_V3_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_COMPLETION.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49EXEC.md | missing-s5-header |
| WARN | ADVI_49PUSH_AUTH_ARCHITECTURE.md | missing-s5-header |
| WARN | ADVI_49PUSH_P1_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P3_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P4_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P5_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ANONYM_P3_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ANONYM_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_APISCP_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_CANNNA_PLAN.md | missing-s5-header |
| WARN | ADVI_CLSPT2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_FEE_WINDOW_REVENUE.md | missing-s5-header |
| WARN | ADVI_FRONTEND_CORRECTNESS.md | missing-s5-header |
| WARN | ADVI_GLDOPS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_HEADER_SPLIT_PRIMITIVES.md | missing-s5-header |
| WARN | ADVI_INFCAPX.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_INFGRD.md | missing-s5-header |
| WARN | ADVI_INFLEC.md | missing-s5-header |
| WARN | ADVI_INFLEC_BRONZERUN.md | missing-s5-header |
| WARN | ADVI_INFLEC_BRONZERUN_V2.md | missing-s5-header |
| WARN | ADVI_INFLV2.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_INFSHIP.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_INFSHIP_PHASE2_BRIEF.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_MVP318_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_NNAFEE_FEE_EFFICIENCY_VIEWS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_OFFICE_ADDENDUM.md | missing-s5-header |
| WARN | ADVI_OFFICE_PRD.md | missing-s5-header |
| WARN | ADVI_ORIAPI.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_PROFIL_PRD.md | missing-s5-header |
| WARN | ADVI_PSCFIX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_RDVSDS.md | no-comp-tool-citation |
| WARN | ADVI_REBORN_LEADERBOARD_FEES_ROLES_FIX.md | missing-s5-header |
| WARN | ADVI_REBORN_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_REBORN_WS1_WS3_VALIDATION.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PERMISSION_GROUPS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLLUP.md | missing-s5-header |
| WARN | ADVI_ROLLUP_ADDENDUM_small_account_count.md | missing-s5-header |
| WARN | ADVI_SLEEVE_P0_DECISION.md | missing-s5-header |
| WARN | ADVI_SLEEVE_PLAN.md | missing-s5-header |
| WARN | ADVI_STAUDT.md | missing-s5-header |
| WARN | ADVI_TICKID_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_TICKID_PRICING_DIVERGENCE_ADDENDUM.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_architect_methodology_bifurcation.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_data_lineage.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_segment_analytics_variance.md | missing-s5-header,no-comp-tool-citation |
| WARN | AUA_VARIANCE_ANALYSIS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | BD_ASSET_DIM_PIPELINE.md | missing-s5-header |
| WARN | BD_CANONICAL_PRICES_CLASSIFICATION_REFACTOR.md | missing-s5-header |
| WARN | BD_NNA_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| WARN | CDRS_TFIMPT_PHASE2_HANDOFF.md | missing-s5-header |
| WARN | COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md | missing-s5-header |
| WARN | COMPILER_IAM_LAMBDA_PARSER.md | missing-s5-header |
| WARN | COMPILER_INPUT_CANONICALIZATION.md | missing-s5-header |
| WARN | COMPILER_LINT_COVERAGE_PASS.md | missing-s5-header |
| WARN | COMPILER_SILVER_SCOPE_FULL.md | missing-s5-header |
| WARN | COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md | missing-s5-header |
| WARN | COMP_LEARNS_ADVERSARIAL_QUERIES.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_ARCHITECTURE.md | missing-s5-header |
| WARN | COMP_LEARNS_AUTOMATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BACKLOG_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BENCHMARK_AUTHORING_SOP.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_COMPILER_BASELINE.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_DS_ROLE_ADDENDUM.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_HARNESS_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_HTTPX_TARGET.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_INTAKE_WAVE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_LOOP_ORCHESTRATOR.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_OPERATIONAL_MANDATE.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PARALLELIZATION_V1.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PHASE2_PROTOCOL_AMENDMENT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PILOT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PROGRAM_PURPOSE.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_QUALITATIVE_FRAMEWORK.md | missing-s5-header |
| WARN | COMP_LEARNS_RUNTIME_V1.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3_PATH_B.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_2_SELECTION.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_CLOSEOUT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_UNDOCUMENTED_SURFACES.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_WAVE3_V1.md |  |
| WARN | COMP_LEARNS_WAVE_PRD_TEMPLATE.md | no-comp-tool-citation |
| WARN | DISTRIBUTION_TAB_OTHER_DEDUPE.md | missing-s5-header |
| WARN | DRFR_PTMCH_CANON_INTERLOCK_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | DRFR_PTMCH_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | EC2_TELEMETRY_DESIGN.md | missing-s5-header,no-comp-tool-citation |
| WARN | ETFS_SECIDX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_BLAST_RADIUS_ASSESSMENT.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_COO_BRIEFING_INTEGRATION_TESTING.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_P3_OPERATIONAL_READINESS.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_ROLLBACK_PLAN.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_PERF_PRD.md | missing-s5-header |
| WARN | IDTY_RENAME_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | INCREMENTAL_RUNS_DESIGN.md | missing-s5-header |
| WARN | INFLEC_API_ENDPOINTS_CATALOG.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_BD_PARITY_MATRIX.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_BOOKSTAB_TAX_FIELD_MAP.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_DATA_INVENTORY.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_DIMS_AND_TRANSACTIONS.md | no-comp-tool-citation |
| WARN | INFLEC_DIM_PULL_REQUESTS.md | no-comp-tool-citation |
| WARN | INFLEC_ENRICH_SCOPE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_PARITY_FILL_CANDIDATES.md | no-comp-tool-citation |
| WARN | INFLEC_PORTAL_FIELD_USAGE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_TRANSACTIONS_API_PROBE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLV2_BOOKS_SCOPE_FREEZE.md | missing-s5-header,no-comp-tool-citation |
| WARN | MDLP_WYNCHT_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | MKOV_TRENDS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | NNA_VARIANCE_OPTIMIZATION_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md | missing-s5-header,no-comp-tool-citation |
| WARN | PORTFOLIO_EXPORT_TRADE_SUBMISSION_BRIDGE.md | missing-s5-header,no-comp-tool-citation |
| PASS | PRD_AUTHORING_PROTOCOL.md |  |
| WARN | ROLE_AUA_CANONICAL_CONVERGENCE_PLAN.md | missing-s5-header |
| WARN | SECURITY_SCANNER_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT_COMPACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DATA_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DESIGN_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | TRADE_ENGINE_VISUAL_POLISH.md | missing-s5-header,no-comp-tool-citation |
| WARN | TRSB_PATHFIX_PRD.md | missing-s5-header |
| WARN | TRSB_TFIMPT.md | missing-s5-header |
| WARN | gold-artifact-mapping.md | missing-s5-header,no-comp-tool-citation |

Total: 2 PASS, 131 WARN, 133 PRDs scanned.

| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.007 | comp-blast | comp-blast opal-precompute-market-metrics | PASS |
| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.007 | comp-blast | comp-blast opal-cloudfront-market-generator | PASS |
| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.007 | comp-trace | comp-trace opal-precompute-market-metrics --direction downstream | FAIL |
| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.007 | comp-trace | comp-trace opal-precompute-market-metrics --direction both | PASS |
| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.007 | comp-trace | comp-trace opal-cloudfront-market-generator --direction both | PASS |
| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.007 | comp-routes | comp-routes behaviors | PASS |
| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.007 | comp-platinum | comp-platinum reverse json/market-metrics.json.gz | PASS |
| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.007 | comp-platinum | comp-platinum reverse json/market-metrics.json | PASS |
| 2026-04-29 | 0.4.0_DS_ClientPlatform | ADVI_INFLEC.DIAGFIX.011 | comp-build | comp-build | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate --list | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate nonexistent_script --artifact /tmp/nonexistent.json | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate fee_earning_aua --artifact /tmp/missing_file_xyz.json | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate --list | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate cash_coverage_summary --artifact /tmp/empty_test_artifact.json | FAIL |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-build | comp-build | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate INF_D_00c --artifact C:/Users/AndrewBerman/AppData/Local/Temp/inflv2_vali... | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate INF_09 --artifact C:/Users/AndrewBerman/AppData/Local/Temp/inflv2_validat... | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate --help | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | (no-TO) | comp-validate | comp-validate --list | PASS |
| 2026-04-30 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.V1-SMOKE | comp-transform | comp-transform schema-check InflectionInsightsPanel | FAIL |
| 2026-04-30 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.V1-SMOKE | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-04-30 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.V1-SMOKE | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-04-30 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.V1-SMOKE | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-04-30 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.V1-SMOKE | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-30 | 0.5.0_AE_OpalETL | ADHC_CLCOMM.001.ae-build-cl-mcp-scripts | comp-blast | comp-blast org/mcp/server.py | PASS |
| 2026-04-30 | 0.5.0_AE_OpalETL | ADHC_CLCOMM.001.ae-build-cl-mcp-scripts | comp-blast | comp-blast org/mcp/broker.py | PASS |
| 2026-04-30 | 0.6.1_AE_PartnerETL | (no-TO) | comp-iam | comp-iam service inf-bronze-runner | PASS |
| 2026-04-30 | 0.6.1_AE_PartnerETL | (no-TO) | comp-blast | comp-blast inf-ec2-launch-monitor | PASS |
| 2026-04-30 | 0.6.1_AE_PartnerETL | ADVI_HISTBF.002+ADVI_JWTRES.001 | comp-iam | comp-iam gaps | PASS |
| 2026-04-30 | 0.6.1_AE_PartnerETL | ADVI_HISTBF.002+ADVI_JWTRES.001 | comp-pipescript | comp-pipescript io INF_B_00 | FAIL |
| 2026-04-30 | 0.6.1_AE_PartnerETL | ADVI_HISTBF.002+ADVI_JWTRES.001 | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_B | ADVI_HISTBF.001 | comp-validate | comp-validate INF_B_00 --artifact /tmp/holdings_2026-04-30.parquet | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_B | ADVI_HISTBF.001 | comp-validate | comp-validate INF_B_00 --artifact C:/Users/AndrewBerman/Desktop/ajb_workspace/holdings_... | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-build | comp-build | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-validate | comp-validate INF_I_D03.composition_artifacts --artifact C:/Windows/Temp/comp_brand.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io build_canonical_prices_v2 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_04 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-validate | comp-validate INF_I_D00.portal_aggregates --artifact C:/Windows/Temp/hm.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-validate | comp-validate INF_D_00c.portal_leaderboard --artifact C:/Windows/Temp/lb.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io convert_orion_to_silver | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_01c | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01b | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io build_canonical_prices_v2 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_01c | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_05 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_07 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00b | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00c | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_A_00 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_A_01 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_A_03 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_A_04 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_00 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_01 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_02 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_03 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_C_00 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_C_01 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_C_02 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_C_03 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_C_05 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_C_06 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_C_07 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_C_08 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_00c | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_02 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_05 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io convert_orion_to_silver | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_06 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_07 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_08 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_I_D00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_I_D00b | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_I_D03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io inf-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io bd_price_update | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript feeds INF_D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript consumers INF_D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io build_canonical_prices_v2 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01.holdings_lots.py | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-trace | comp-trace opal-portal-authorizer --direction upstream | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-blast | comp-blast lambda:opal-partners-data --direction both | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io bd-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io orion-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_X_99 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io --pipeline inf B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io --pipeline bd B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript deployed data/orion/manual_api/pull_inflection_transactions_rest.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript deployed data/orion/manual_api/pull_inflection_performance_rest.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript deployed data/orion/scripts/silver/convert_transactions_to_silver.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript deployed data/orion/scripts/silver/convert_performance_to_silver.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-build | comp-build | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01.bogus.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_99 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io inf-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io bd-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io orion-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io convert_orion_to_silver | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io bd_price_update | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-build | comp-build | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_00 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript --pipeline inf io B_00 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript --pipeline bd io B_00 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io --pipeline inf B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io --pipeline bd B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-build | comp-build | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_08 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript feeds B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript consumers D_00.portal_aggregates.py | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript deployed B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-build | comp-build | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_00 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io --pipeline inf B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io --pipeline bd B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-blast | comp-blast INF_D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-trace | comp-trace INF_D_04 --direction both | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-blast | comp-blast D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_99 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io inf-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io bd-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io convert_orion_to_silver | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io bd_price_update | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_X_99 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01.bogus.py | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04.employee_leaderboard.py | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_00.build_canonical_prices_v2.py | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00 --pipeline bd | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_B_99 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io inf-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00.portal_aggregates.py --pipeline bd | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io bd-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io orion-gold-dispatch | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io convert_orion_to_silver | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io bd_price_update | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io C_08 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-build | comp-build | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_00 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io --pipeline inf B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io --pipeline bd B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io INF_X_99 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io data/black_diamond/scripts/gold/B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04.client_portal_summary.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io A_00.accounts_dimension.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00 --pipeline bd | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_00.portal_aggregates.py --pipeline bd | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript feeds B_01 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript feeds B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript deployed D_04.client_portal_summary.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io B_01.bogus | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC1: INF_B_00 exists -> exit 0 + I/O MANIFEST [inf-gold] | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC1b: INF_B_99 not found -> exit 1 + Did you mean | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC2: INF_D_04 exists -> exit 0 + I/O MANIFEST [inf-gold] | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC3: inf-gold-dispatch -> DISPATCHER output [inf-gold] exit 0 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC3: bd-gold-dispatch -> DISPATCHER output [bd-gold] exit 0 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC3: orion-gold-dispatch -> DISPATCHER output [inf-gold] exit 0 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC4: convert_orion_to_silver -> I/O MANIFEST [inf-silver] exit 0 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC5: bd_price_update -> I/O MANIFEST [bd-silver] exit 0 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC6: B_00 synthetic collision -> exit 1 Ambiguous script ID (CATALOG+placeholder) | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC7: --pipeline inf B_00 -> [inf-gold] unambiguous; --pipeline bd B_00 -> [bd-gold] | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC8: B_01/D_04/C_08 unchanged -> bd-gold, no regression (exact-match-only fix) | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC9: comp-blast/comp-trace INF_D_04 -> no crash (resolver extension transparent to callers) | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC10: test_inf_id_resolver.sh 15/15 cases pass | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~C | ADHC_COMPIL.011.ds-inf-script-id-resolver | comp-pipescript | AC11: compiler-tools-log rows appended (this entry) | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-pipescript | comp-pipescript feeds D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-validate | comp-validate B_00 --artifact /tmp/test_validate_artifact.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-validate | comp-validate B_00 --artifact C:/tmp/test_validate_artifact.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-validate | comp-validate B_00 --artifact /tmp/does_not_exist_xyz.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-trace | comp-trace D_04 --direction up | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-trace | comp-trace D_04 --direction upstream | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-trace | comp-trace D_04 --direction down | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-trace | comp-trace D_04 --direction downstream | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-trace | comp-trace D_04 --direction both | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-trace | comp-trace D_04 --direction sideways | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-blast | comp-blast opal-partners-data --direction both | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-blast | comp-blast lambda:opal-partners-data --direction both | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-blast | comp-blast gold:D_04 --direction up | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-blast | comp-blast component:portal/src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx --dir... | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~D | ADHC_COMPIL.012.ds-comp-freshness-tool | comp-blast | comp-blast lambda:opal-partners-data | PASS |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.008.ae-pipescript-io-filename-canon | comp-pipescript | AC1: io B_01.holdings_lots.py == io B_01 (byte-identical) | PASS | filename-form resolver via exact filename match |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.008.ae-pipescript-io-filename-canon | comp-pipescript | AC2: io data/black_diamond/scripts/gold/B_01.holdings_lots.py == io B_01 | PASS | full path form |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.008.ae-pipescript-io-filename-canon | comp-pipescript | AC3: io B_01.bogus.py -> exit 1, "Script not found: B_01.bogus.py. Did you mean: B_01?" | PASS | bogus filename exits 1 with suggestion |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.008.ae-pipescript-io-filename-canon | comp-pipescript | AC4: 5-script fixture (B_01/D_04/A_00/D_00+--pipeline bd) x filename/fullpath forms | PASS | all 5 scripts PASS across all input forms |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.008.ae-pipescript-io-filename-canon | comp-pipescript | AC5: feeds/deployed spot-checks with filename forms | PASS | feeds+deployed both byte-identical |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.008.ae-pipescript-io-filename-canon | comp-pipescript | AC6/AC7: bare IDs still resolve correctly (regression guard) | PASS | D_04 io + feeds unchanged |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.009.ae-validate-windows-path-translator | comp-validate | AC1: /tmp/ path translates to C:/tmp/ on Windows (PowerShell direct Python call) | PASS | POSIX /tmp/ -> C:\tmp\ transparent |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.009.ae-validate-windows-path-translator | comp-validate | AC4: non-existent /tmp/ path shows dual-path error (Input path + Translated path) | PASS | error shows both paths on separate lines |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-trace | AC1: --direction upstream byte-identical to --direction up | PASS | F.3 alias normalization |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-trace | AC2: --direction downstream byte-identical to --direction down | PASS | F.3 alias normalization |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-trace | AC3: --direction both unchanged | PASS | F.3 no regression |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-trace | AC4: --direction sideways -> exit 2, invalid choice listing all 5 valid values | PASS | argparse choices updated |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-blast | AC5: lambda:opal-partners-data --direction both == bare opal-partners-data --direction both | PASS | F.4 prefix-qualified direction wiring |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-blast | AC6: gold:D_04 --direction up (returns upstream) | PASS | F.4 |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-blast | AC7: component:...AdvisorIntelligence.tsx --direction down | PASS | F.4 |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-blast | AC8: lambda:opal-partners-data (no --direction) behavior unchanged | PASS | F.4 regression guard |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.010.ae-trace-blast-direction-fixes | comp-pipescript | AC9: compiler-tools-log rows appended (this entry) | PASS | |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC1: chain bd -- 32 artifacts checked in 27.8s | PASS | <30s target met; 8-thread parallel AWS calls |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC2: chain inf -- 31 artifacts checked in 24.0s | PASS | <30s target met |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC3: artifact s3://opal-data-schwab/silver/RPS/ returns FAIL age=221h, exit 1 | PASS | live schwab_rps stale (ongoing) |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC4: --list prints BD 32 entries + INF 31 entries | PASS | grouped by pipeline, sorted by artifact_id |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC5: malformed YAML -> exit 2 with specific error (line+column) | PASS | ConfigError path distinguishable from FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC6: RPS 2026-04-17 retrospective -- mocked last_mod=2026-04-07T10:00Z, incident_date=2026-04-17T12:00Z -> FAIL age=240h | PASS | unit test in tests/comp_freshness/ |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC7: aum_snapshot 2026-04-29 retrospective -- mocked last_mod=2026-04-21T09:00Z, incident_date=2026-04-29T09:00Z -> FAIL age=192h | PASS | unit test in tests/comp_freshness/ |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC8: BD config has 32 entries (>= 30 required) | PASS | 4 vendor + 7 silver + 21 gold intermediates |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC9: INF config has 31 entries (>= 10 required) | PASS | 7 vendor + 9 silver + 15 gold intermediates |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_A | ADHC_COMPIL.012 | comp-freshness | AC10: Andrew partner-feed ACK | PASS | Andrew ACK 2026-04-30: all vendor entries severity=WARN; staleness never blocks dispatch; schwab_rps + schwab_rld downgraded from ERROR |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC11: chain bd timing <30s | PASS | 27.8s (same as AC1) |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC12: AWS_UNREACHABLE prefix distinguishes connectivity failures from stale-data FAIL | PASS | exit 2 path uses AWS_UNREACHABLE: prefix; stale data uses FAIL in output |
| 2026-04-30 | 0.4.0_DS_ClientPlatform_D | ADHC_COMPIL.012 | comp-freshness | AC13: compiler-tools-log rows appended (this entry) | PASS | |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_00c | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-trace | comp-trace schwab_rld --direction both | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-trace | comp-trace schwab_rps --direction both | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript deployed INF_B_00 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/cohort_a_summary_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/cash_coverage_summary_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/ambiguous_name_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate definitely_not_a_thing --artifact C:/tmp/cohort_a_summary_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact /tmp/does_not_exist_xyz_comp_validate_test.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate nonexistent_script_xyz --artifact C:/tmp/cohort_a_summary_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate B_00 --artifact C:/tmp/comp_validate_fixture_real.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate B_00 --strict --artifact C:/tmp/comp_validate_fixture_real.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_bad_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/cash_coverage_summary_test_fixture.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/ambiguous_name_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate definitely_not_a_thing --artifact C:/tmp/cohort_a_summary_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact /tmp/does_not_exist_xyz_comp_validate_test.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate nonexistent_script_xyz --artifact C:/tmp/cohort_a_summary_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate INF_D_04 --artifact C:/tmp/clients_tab_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate INF_D_04 --strict --artifact C:/tmp/clients_tab_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_bad_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/cash_coverage_summary_test_fixture.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact C:/tmp/ambiguous_name_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate definitely_not_a_thing --artifact C:/tmp/cohort_a_summary_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact /tmp/does_not_exist_xyz_comp_validate_test.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate nonexistent_script_xyz --artifact C:/tmp/cohort_a_summary_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate INF_09 --artifact C:/tmp/partner_analytics_test_fixture.json | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate INF_09 --strict --artifact C:/tmp/partner_analytics_test_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_bad_fixture.json | FAIL |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript deployed INF_C_07.advisor_attribution.py | PASS |

## 2026-04-30 — ADHC_COMPIL.015 (0.7.0_AE_CloudOps) — Alias resolver + exit semantics

| Date | Agent | TO | Tool | Command | Result | Note |
|------|-------|----|------|---------|--------|------|
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate D_04 --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS | AC1: resolved D_04 -> cohort_a_summary, exit 0, Resolved info line |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate D_04 --artifact C:/tmp/cash_coverage_summary_test_fixture.json | PASS | AC2: resolved D_04 -> cash_coverage_summary, exit 0 |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate D_04 --artifact C:/tmp/ambiguous_name_test_fixture.json | PASS | AC3: exit 1, candidate list in stderr |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate D_04 (no --artifact) | PASS | AC4: exit 1, multi-artifact error |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS | AC5: direct id, exit 0, no Resolved info line |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate definitely_not_a_thing --artifact C:/tmp/... | PASS | AC6: exit 1, error message in stderr |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate cohort_a_summary --artifact /tmp/does_not_exist.json | PASS | AC7: exit 1, MISSING_ARTIFACT in stderr |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate nonexistent_script_xyz --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS | AC8: exit 1, resolver catches unknown id |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate INF_09 --artifact C:/tmp/partner_analytics_test_fixture.json | PASS | AC9: exit 0, NO_CONFIG status line |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate INF_09 --strict --artifact C:/tmp/partner_analytics_test_fixture.json | PASS | AC10: exit 2, NO_CONFIG status line |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_test_fixture.json | PASS | AC11: exit 0, PASS: status line |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | comp-validate | comp-validate cohort_a_summary --artifact C:/tmp/cohort_a_summary_bad_fixture.json | PASS | AC12: exit 1, FAIL: status line |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | n/a | check COMP_VALIDATE_PROTOCOL.md has §10 | PASS | AC13: §10 + --strict documented |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | n/a | check validate_cli.py has --strict | PASS | AC14: --strict argument present |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.015 | n/a | check gold_validate_config.yaml has producer_script: fields | PASS | AC15: both BD + INF configs updated |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript deployed data/orion/scripts/silver/convert_performance_to_silver.py | PASS |

## 2026-04-30 — ADHC_COMPIL.014 (0.7.0_AE_CloudOps) — comp-shell tool

| Date | Agent | TO | Tool | Command | Result | Note |
|------|-------|----|------|---------|--------|------|
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | comp-shell scan tests/comp_shell/fixtures/01_bare_pgrep.sh | PASS | AC1 (pre-fix synthetic): ERROR pgrep:unguarded, exit 1 |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | comp-shell scan org/mcp/inbox-watch.sh | PASS | AC2 (post-BASHFIX.002): WARN pgrep:guarded, exit 0 |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | comp-shell scan .tools/ | PASS | AC3: scans all .sh under .tools/, exit 0 (0 ERROR) |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | comp-shell scan --all | PASS | AC4: workspace scan; in-scope paths clean |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | comp-shell list-forbidden | PASS | AC5: 6 utilities + fallbacks printed |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | fixture 01 (bare pgrep) | PASS | AC6a: ERROR:pgrep:unguarded emitted |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | fixture 02 (guarded pgrep) | PASS | AC6b: WARN:pgrep:guarded emitted |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | fixture 03 (comment only) | PASS | AC6c: 0 findings (comments filtered) |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | fixture 04 (string literal) | PASS | AC6d: 0 findings (single-quoted string filtered) |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | fixture 05 (heredoc) | PASS | AC6e: 0 findings (heredoc body excluded) |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | ds-commit-gate.sh | gate with bare pgrep .sh in .tools/ | PASS | AC7: hook BLOCKED exit 1 |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | ds-commit-gate.sh | gate with guarded pgrep .sh in .tools/ | PASS | AC8: hook ALLOWED exit 0 |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | ds-commit-gate.sh | gate with bare pgrep in infra/aws/ec2/ | PASS | AC9: hook skipped EC2-side, exit 0 |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | comp-shell | comp-shell scan Rule-16 in-scope paths | PASS | AC10: 0 ERROR, 4 WARN (guarded) in in-scope paths |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | n/a | escalation check | PASS | AC11: no unexpected ERRORs in in-scope paths; known (deprecated + fixture) |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | n/a | comp-tools.yaml comp-shell entry | PASS | AC12: entry added with subcommands + note |
| 2026-04-30 | 0.7.0_AE_CloudOps | ADHC_COMPIL.014 | n/a | log rows | PASS | AC13: this entry |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-blast | comp-blast gold_dispatch.sh | PASS |
[ADHC_COMPIL.013] FRESHNESS-BYPASS: 2026-04-30T21:00:00Z | gold_dispatch.sh | chain:full | test | (no reason given)
[ADHC_COMPIL.013] FRESHNESS-BYPASS: 2026-04-30T21:00:00Z | gold_dispatch.sh | chain:full | test | vendor RPS feed scheduled outage 2026-04-30

## ADHC_COMPIL.013 — comp-freshness dispatch integration (2026-04-30, 0.7.0_AE_CloudOps)

| AC | Tool | Command | Result | Note |
|----|------|---------|--------|------|
| AC1 | comp-freshness | comp-freshness chain bd (real config) | PASS (exit 0) | BD chain all PASS; vendor WARNs (schwab_uln/ult/rld/bd_assets_dim/ticker_resolution) non-blocking |
| AC2 | comp-freshness | synthetic fail_age_hours=1 fixture | PASS (exit 1) | bd_silver_canonical_prices 17.1h vs 1h threshold; gate fires, dispatcher exits 1 |
| AC3 | gold_dispatch.sh | --no-freshness-check (no reason) | PASS | Bypass logged: [ADHC_COMPIL.013] FRESHNESS-BYPASS: ... | (no reason given) |
| AC4 | gold_dispatch.sh | --no-freshness-check --bypass-reason "vendor RPS feed scheduled outage 2026-04-30" | PASS | Reason text present in log entry |
| AC5 | comp-freshness | comp-freshness chain inf (real config) | FAIL (exit 1, expected) | inf_silver_canonical_prices 199.6h stale -- remediation: silver-prep chain wired in same commit |
| AC6 | comp-freshness | config renamed (missing YAML) | PASS (exit 2) | BD and INF both exit 2 on missing config; dispatcher emits distinct tooling-failure message |
| AC7 | orion-gold-dispatch.sh | --no-freshness-check (no reason) | PASS | Mirror of AC3 for INF dispatcher; same bypass function |
| AC8 | orion-gold-dispatch.sh | --no-freshness-check --bypass-reason "<text>" | PASS | Mirror of AC4; reason text stored in log |
| AC9 | bypass log | tail org/compiler-tools-log.md after each bypass run | PASS | All bypass entries single-line; pipe-delimited; [ADHC_COMPIL.013] prefix present |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript deployed gold_dispatch.sh | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript deployed orion-gold-dispatch.sh | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript io B_01.holdings_lots.py | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-trace | comp-trace D_04 --direction downstream | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-04-30 | 0.4.0_DS_ClientPlatform~A | (no-TO) | comp-validate | comp-validate D_04 --artifact /tmp/cohort_a_summary.json | PASS |
| 2026-05-01 | 0.3.0_DT_TradingOperations | TRSB_PATHFIX.TO-2 | py_compile+AST+ruff on 4 .py files: PASS. Fixed F401 unused Role. No comp-iam (no new boto3). Migration verified via DDB scan. CW smoke test: 4 approvers + 9 executors PASS. |
| 2026-05-01 | 0.5.0_AE_OpalETL | ADHC_CLCOMM.003.ae-verification-and-close | comp-iam | comp-iam service inf-bronze-runner | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.SL-P1b | comp-blast | comp-blast gold/timeseries/holdings_lots | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.SL-P1b | comp-blast | comp-blast holdings_lots | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.SL-P1b | comp-validate | comp-validate B_01 --artifact s3://opal-data-bd/gold/timeseries/holdings_lots_shadow/20... | FAIL |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~B | ADVI_ROLLUP.SL-P1b | comp-pipescript | comp-pipescript feeds B_01 | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-pipescript | comp-pipescript deployed INF_D_00c | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-pipescript | comp-pipescript deployed orion-gold-dispatch.sh | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-blast | comp-blast holdings_lots_shadow | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-pipescript | comp-pipescript io INF_B_00.canonical_holdings | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-blast | comp-blast silver/api_dims/positions_mv | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-blast | comp-blast silver/assets_v2 | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-blast | comp-blast INF_B_00 | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-blast | comp-blast canonical_holdings | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-blast | comp-blast B_01 | PASS |
| 2026-05-01 | 0.7.0_AE_CloudOps | ADVI_INFGRD.004 | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-05-01 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFSHIP.PHASE3-FE-BUGS | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-05-01 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFSHIP.PHASE3-FE-BUGS | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-01 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFSHIP.PHASE3-FE-BUGS | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-05-01 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFSHIP.PHASE3-FE-BUGS | comp-blast | comp-blast DistributionTab | PASS |
| 2026-05-01 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFSHIP.PHASE3-FE-BUGS | comp-blast | comp-blast ClientsTab | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform_B | ADVI_49FRECN.001B | comp-pipescript | comp-pipescript io D_00.portal_aggregates.py | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io D_02.advisor_client_detail.py | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io 00_build_accounts_dimension.py | FAIL |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io A_00.accounts_dimension.py | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io 06b | FAIL |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io A_00 | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io B_01b | FAIL |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io B_01b | FAIL |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io C_06 | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-trace | comp-trace NNA_AUA_BY_ADVISOR --direction both | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript deployed E_25 | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript deployed E_25 | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.001C | comp-pipescript | comp-pipescript deployed E_25.aua_decomposition_audit | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~A | ADVI_49FRECN.002.ds-a-d04-out-of-scope-json | comp-pipescript | comp-pipescript io D_04.client_portal_summary.py | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~A | ADVI_49FRECN.002.ds-a-d04-out-of-scope-json | comp-pipescript | comp-pipescript io D_04.client_portal_summary.py | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~A | ADVI_49FRECN.002.ds-a-d04-out-of-scope-json | comp-pipescript | comp-pipescript deployed D_04.client_portal_summary.py | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~A | ADVI_49FRECN.002.ds-a-d04-out-of-scope-json | comp-build | comp-build | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~A | ADVI_49FRECN.002.ds-a-d04-out-of-scope-json | comp-pipescript | comp-pipescript deployed B_00.canonical_holdings.py | PASS |
| 2026-05-01 | 0.4.0_DS_ClientPlatform~A | ADVI_49FRECN.002.ds-a-d04-out-of-scope-json | comp-pipescript | comp-pipescript deployed A_03.positions_cube.py | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-pipescript | comp-pipescript io pull_inflection_transactions_rest.py | FAIL |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-blast | comp-blast safe-commit.sh | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-blast | comp-blast D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-iam | comp-iam service inf-jwt-trigger | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-platinum | comp-platinum reverse out_of_scope_accounts.json | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-iam | comp-iam gaps | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-platinum | comp-platinum reverse c1_recovered_accounts.json | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-pipescript | comp-pipescript postdeps D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-iam | comp-iam gaps | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-iam | comp-iam service bd-gold-runner | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-iam | comp-iam gaps | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-transform | comp-transform schema-check AccountDistributionMetrics | FAIL |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-transform | comp-transform schema-check AUMGrowthMetrics | FAIL |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-transform | comp-transform schema-check ConsolidatedOverviewPanel | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-blast | comp-blast AccountDistributionMetrics | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~B | ADVI_49FRECN.002 | comp-blast | comp-blast AUMGrowthMetrics | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check ConsolidatedOverviewPanel | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-blast | comp-blast AccountDistributionMetrics | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | DASH_STSTRP.001.de-stat-strip-density-tightening | comp-transform | comp-transform schema-check ConsolidatedOverviewPanel | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | DASH_STSTRP.001.de-stat-strip-density-tightening | comp-pipescript | comp-pipescript io INF_B_00 | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | DASH_STSTRP.001.de-stat-strip-density-tightening | typecheck | bun run typecheck (Phase 2, pre-commit) | PASS | Exit 0 — CSS-only diff, no type changes |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | DASH_STSTRP.001.de-stat-strip-density-tightening | frontend-dev | /frontend-dev Playwright 1366x912 (Phase 3, post-commit) | PASS | 4/4 scenarios — all strips single-row zero wrapping at Surface Laptop viewport |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | INFLEC-WaveD-revalidation | frontend-dev | Playwright Inflection Books S6+S7 re-validation | PARTIAL | S6 PASS (advisor list 16 rows); S7 DATA-GATE (summary.json missing in opal-data-inf) |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.S7SUMFIX | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.S7SUMFIX | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.S7SUMFIX | comp-platinum | comp-platinum reverse platinum/advisors/peter_lee/summary.json | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.S7SUMFIX | comp-pipescript | comp-pipescript deployed INF_D_04 | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service inf-gold-qa-runner | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed B_00 | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed A_03 | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service inf-gold-layer-runner | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service inf-gold-layer | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast ReturnVolatilityScatter | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io yang-model-portfolio-benchmarks | FAIL |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace getModelPortfolioBenchmarks | PASS |
| 2026-05-04 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service yang-model-portfolio-benchmarks | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript deployed gold_dispatch.sh | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.003.ds-b-track-2-fix-d04-sidecar-aqr-bfix3-option-b | comp-blast | comp-blast account_performance | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.003.ds-b-track-2-fix-d04-sidecar-aqr-bfix3-option-b | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.003.ds-b-track-2-fix-d04-sidecar-aqr-bfix3-option-b | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.003.ds-b-track-2-fix-d04-sidecar-aqr-bfix3-option-b | comp-pipescript | comp-pipescript io A_03 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.003.ds-b-track-2-fix-d04-sidecar-aqr-bfix3-option-b | comp-blast | comp-blast A_03 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | ADVI_49FRECN.003.ds-b-track-2-fix-d04-sidecar-aqr-bfix3-option-b | comp-pipescript | comp-pipescript deployed A_03 | PASS |
| 2026-05-04 | 2.0.0_SA_COO | (no-TO) | comp-transform | comp-transform schema-check ReturnVolatilityScatter | FAIL |
| 2026-05-04 | 2.0.0_SA_COO | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-04 | 2.0.0_SA_COO | (no-TO) | comp-transform | comp-transform schema-check ReturnVolatilityScatter | FAIL |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.SL-P1c | comp-pipescript | comp-pipescript io B_01 | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~C | ADVI_ROLLUP.SL-P1c | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-05-04 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed A_03.positions_cube.py | PASS |
| 2026-05-04 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript postdeps A_03.positions_cube.py | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check InflectionInsightsPanel | FAIL |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-iam | comp-iam service opal-partners-data | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check FidelityCustodianBar | FAIL |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.AUDIT-001 | comp-cache | comp-cache collisions | PASS |
| 2026-05-04 | 0.6.1_AE_PartnerETL | INFLEC_AUDIT_001_AE_ORION_VENDOR | comp-platinum | comp-platinum page AdvisorIntelligence | FAIL |
| 2026-05-04 | 0.6.1_AE_PartnerETL | INFLEC_AUDIT_001_AE_ORION_VENDOR | comp-routes | comp-routes auth-map | PASS |
| 2026-05-04 | 0.6.1_AE_PartnerETL | INFLEC_AUDIT_001_AE_ORION_VENDOR | comp-platinum | comp-platinum page Books | FAIL |
| 2026-05-04 | 0.6.1_AE_PartnerETL | INFLEC_AUDIT_001_AE_ORION_VENDOR | comp-platinum | comp-platinum | PASS |
| 2026-05-04 | 0.6.1_AE_PartnerETL | INFLEC_AUDIT_001_AE_ORION_VENDOR | comp-platinum | comp-platinum tab-audit | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~D | INFLEC_AUDIT-001_HISTBF_STATE_DUMP | comp-routes | comp-routes auth-map | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~D | INFLEC_AUDIT-001_HISTBF_STATE_DUMP | comp-platinum | comp-platinum summary | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~D | INFLEC_AUDIT-001_HISTBF_STATE_DUMP | comp-platinum | comp-platinum page PartnerAnalytics | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~D | INFLEC_AUDIT-001_HISTBF_STATE_DUMP | comp-platinum | comp-platinum page DistributionTab | PASS |
| 2026-05-04 | 0.4.0_DS_ClientPlatform~D | INFLEC_AUDIT-001_HISTBF_STATE_DUMP | comp-platinum | comp-platinum page InflectionInsightsPanel | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | INFLEC_AUDIT_001_DE_MAPPING | comp-platinum | comp-platinum page AdvisorBookView | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | INFLEC_AUDIT_001_DE_MAPPING | comp-routes | comp-routes behaviors | PASS |
| 2026-05-04 | 0.4.0_DE_ClientPlatform | INFLEC_AUDIT_001_DE_MAPPING | comp-iam | comp-iam gaps | PASS |
| 2026-05-05 | 0.4.0_DS_ClientPlatform~D | ADVI_INFLEC.AUDIT-002.aua-join-investigation | comp-pipescript | comp-pipescript io INF_D_05 | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io INF_D_06 | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io INF_D_05 | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io INF_D_07 | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io INF_I_D02b | FAIL |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io INF_I_D00c | FAIL |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-routes | comp-routes trace getPlatinumClientSummary | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io INF_I_D00c | FAIL |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io INF_I_D02b | FAIL |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript io INF_I_D02b.top_holdings | FAIL |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-platinum | comp-platinum reverse platinum/firm/activity_scan.json | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-platinum | comp-platinum reverse platinum/firm/leaderboard.json | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript deployed INF_I_D02b | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-blast | comp-blast InflectionInsightsPanel | PASS |
| 2026-05-05 | 0.7.0_AE_CloudOps | (no-TO) | comp-blast | comp-blast AdvisorBookView | PASS |
| 2026-05-05 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-routes | comp-routes trace getPlatinumPartnerAnalytics | PASS |
| 2026-05-05 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace getPlatinumClientSummary | PASS |
| 2026-05-05 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-05 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.AUDIT-004.l3-client-summary-lambda-probe | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.AUDIT-004.l3-client-summary-lambda-probe | comp-cache | comp-cache collisions | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.AUDIT-004.l3-client-summary-lambda-probe | comp-pipescript | comp-pipescript deployed orion-gold-dispatch.sh | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLEC.AUDIT-004.l3-client-summary-lambda-probe | comp-pipescript | comp-pipescript deployed orion-gold-dispatch.sh | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check BooksTab | FAIL |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-iam | comp-iam service opal-partners-data | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-routes | comp-routes behaviors | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-iam | comp-iam gaps | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-iam | comp-iam service opal-partners-data | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-iam | comp-iam service opal-partners-data | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-iam | comp-iam service opal-partners-data | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check InflectionInsightsPanel | FAIL |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-blast | comp-blast InflectionInsightsPanel | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check InflectionInsightsPanel --verbose | FAIL |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check InflectionInsightsPanel --loose | FAIL |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-iam | comp-iam service opal-partners-data | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-transform | comp-transform schema-check AdvisorBookView | PASS |
| 2026-05-05 | 0.4.0_DE_ClientPlatform | ADVI_INFLFE.003.defensive-rendering-pre-wire | comp-cache | comp-cache collisions | PASS |
| 2026-05-05 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFLFE.004.playwright-render-sweep-and-constitution | comp-pipescript | comp-pipescript io INF_I_D00b | FAIL |
| 2026-05-05 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFLFE.004.playwright-render-sweep-and-constitution | comp-pipescript | comp-pipescript io INF_I_D00b.portal_timeseries | FAIL |
| 2026-05-05 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFLFE.004.playwright-render-sweep-and-constitution | comp-pipescript | comp-pipescript io INF_I_D00b | FAIL |
| 2026-05-05 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFLFE.004.playwright-render-sweep-and-constitution | comp-pipescript | comp-pipescript deployed INF_I_D00c | PASS |
| 2026-05-05 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.AUDIT-006 | ds-commit-gate | .tools/ds-commit-gate.sh INF_I_D00c.cumulative_chart.py | PASS | py_compile+AST+ruff all exit 0 |
| 2026-05-05 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.AUDIT-006 | comp-pipescript | comp-pipescript deployed INF_I_D00c | PARTIAL | Tool targets opal-data-bd; Inflection scripts in opal-data-inf; manual S3 ls confirmed upload (20375 bytes 10:57:01Z) |
| 2026-05-05 | 0.4.0_DS_ClientPlatform~A | ADVI_INFLEC.AUDIT-006 | comp-pipescript | comp-pipescript io INF_I_D00c | SKIPPED | Phase 0 confirmed via direct script read; script already deferred geo_drill in docstring; top_states available from build_geo_view() |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast aws_cloudwatch_event_rule.inf_canonical_prices_daily | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service inf-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast aws_cloudwatch_event_rule.inf_canonical_prices_daily | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast inf-canonical-prices-daily | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service inf-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast aum_snapshot | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io INF_D_08 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace D_04 --direction both | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace INF_D_04 --direction both | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace AdvisorIntelligence --direction both | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace opal-partners-data --direction up | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace platinum/firm/leaderboard.json --direction both | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace _build_aua_view --direction down | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast build_employee_leaderboard | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast _build_aua_view | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast inf-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast _compute_window_decomposition | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-diff | comp-diff | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-diff | comp-diff --staged | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-xref | comp-xref | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace INF_D_04 --direction down | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace INF_D | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace leaderboard | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace s3:platinum/firm/leaderboard.json | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace s3:gold/artifacts/employee_leaderboard.json | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast s3:gold/canonical/holdings | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript dag | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain downstream | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript feeds D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript consumers C_07 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript overlap D_00 D_03 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript dag --pipeline inf-gold | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript dag --pipeline inf-manual-api | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain downstream --pipeline inf-gold | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io INF_C_01 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript feeds INF_D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript consumers INF_C_02 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript overlap D_04 INF_D_04 | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript overlap INF_C_01 INF_C_02 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript postdeps D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript postdeps INF_D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript stats | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain downstream --pipeline inf-gold | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline inf-gold INF_D_04 | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed nonexistent_script_xyz | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes origins | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes auth-map | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace getPlatinumLeaderboard | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace getEmployeeLeaderboard | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes endpoints | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes api-routes | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes rewrites | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes stats | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes components | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline inf-gold INF_D_04 | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline inf-silver | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline bd-silver | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-cache | comp-cache map | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service bd-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service inf-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service inf-bronze-runner | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service nonexistent-thing | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam stats | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam roles | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam role bd-gold-runner-role | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam services | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate --list | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_04 --list | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate INF_D_04 --list | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate definitely_not_a_thing | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum page AdvisorIntelligence | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum page BooksTab | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse gold/artifacts/employee_leaderboard.json | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse platinum/firm/header_metrics.json#radial_12m | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse platinum/firm/header_metrics.json --strict | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum tab-audit | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum summary | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum page PartnerAnalytics | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum page ClientsTab | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check ClientsTab --feature inflection | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform fields PartnerAnalytics | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform chains PartnerAnalytics | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform unused PartnerAnalytics | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform ternary-audit DistributionTab | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform trace ClientsTab | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-transform | comp-transform stats | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pii | comp-pii audit | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pii | comp-pii fields | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-tooltip | comp-tooltip summary | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-tooltip | comp-tooltip drift | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-tooltip | comp-tooltip canonical | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-constants | comp-constants list | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-constants | comp-constants check | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-constants | comp-constants new | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-xref | comp-xref D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-xref | comp-xref AdvisorPublicProfile | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-xref | comp-xref inf-bronze-runner | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-xref | comp-xref nonexistent_zzz | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-incrparity | comp-incrparity | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-incrparity | comp-incrparity --help | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-incrparity | comp-incrparity D_00 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pii | comp-pii sweep | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pii | comp-pii routes | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript dag --pipeline bd-silver | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript dag --pipeline inf-silver | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-cache | comp-cache key advisor | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace getEmployeeLeaderboard --direction both | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace getFirmLeaderboard --direction both | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace endpoint:getEmployeeLeaderboard --direction up | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript inject | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam role inf-gold-trigger-lambda-role | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam services | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-constants | comp-constants check --lane bd | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-constants | comp-constants check --lane inf | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace --json D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_04 | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate INF_D_04 --config data/orion/scripts/gold/gold_validate_config.yaml | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service inf-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam role bd-exporter-ec2-role | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum page InflectionInsightsPanel | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum page DistributionTab | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-build | comp-build / comp-build --check | PASS | OPS test matrix; 1250 nodes/1047 edges; SHA coverage 1085/1158 |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-trace | comp-trace D_04 / INF_D_04 / s3:gold/... / getFirmLeaderboard | PARTIAL | OPS triage #5/#6 — D_04 multiple-matches noise; INF_D_04 not in graph; platinum/* keys not in graph; Tier B refinement |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-blast | comp-blast build_employee_leaderboard / _build_aua_view / inf-gold-trigger | PARTIAL | INF helper not in graph (Tier B reality); BD blast paths PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-diff | comp-diff / --staged | PASS | Output formatting noisy ("portal" repeats) but functionally correct |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-xref | comp-xref / D_04 / AdvisorPublicProfile / inf-bronze-runner / nonexistent_zzz | PASS | Both modes operational; clean error with hints on zero-match |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-pipescript | dag/io/feeds/consumers/overlap/postdeps/deployed/inject/stats variants | PARTIAL | OPS triage #1 BLOCKING (deployed --pipeline inf-gold UnboundLocalError) + #2 BLOCKING (chain --pipeline ignored); other subcommands PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-routes | behaviors/origins/auth-map/trace/endpoints/api-routes/rewrites/stats/components | PASS | Origins count drift (6 actual vs 5 documented); not a bug |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-cache | collisions/map/key advisor | PASS | 4 shared keys reported with TYPE info |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-iam | gaps/service/role/services/roles/stats | PARTIAL | OPS triage #8 — ~100 BD Lambdas show role "(not mapped)"; INF Lambdas + EC2 roles via V4.013 fallback PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-validate | --list / D_04 / INF_D_04 / definitely_not_a_thing | PARTIAL | (SYNTHETIC TEST FIXTURE) ADHC_COMPIL_V4.OPS invalid-script-name regression test for definitely_not_a_thing |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-platinum | page (4 components) / reverse / reverse #field --strict / tab-audit / summary | PARTIAL | OPS triage #10/#11 — catalog examples AdvisorIntelligence/BooksTab fail (non-existent components); real components PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-transform | schema-check/fields/chains/unused/ternary-audit/trace/stats | PASS | --feature flag works; types parent-walk works |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-pii | audit/fields/routes/sweep | PASS | 5 PII refs across 11 components; 0 hardcoded |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-tooltip | summary/drift/canonical | PASS | 77% migration progress (34/44) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-shell | scan inbox-watch.sh / scan .tools/ / list-forbidden | PASS | 2 WARN guarded findings on inbox-watch.sh (expected) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-freshness | --list / chain bd | PASS | 32 BD entries; live AWS calls return PASS/WARN per artifact |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-constants | list/check/new/--lane bd | PARTIAL | OPS triage #4 — --lane flag not implemented (catalog drift); list/check/new PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | check-lambda-layer-deps | --function inf-gold-trigger / --pipeline / --strict | PARTIAL | OPS triage #3 — catalog says positional args + --all + --json; actual flags --function/--pipeline/--strict/--verbose only |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | comp-incrparity | comp-incrparity D_00 (quick) | PASS | Tier C BD-only confirmed |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.OPS | loop-quiescence | ADHC_COMPIL_V4 / ADVI_INFETL / ADHC (macro-prefix) | PARTIAL | OPS triage #7 — bare macro prefix returns false-positive QUIESCENT_CLEAN total=0 |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline inf-gold | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline inf-gold INF_D_04 | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain downstream --pipeline inf-gold | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain downstream | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline inf-gold INF_D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline inf-gold | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain downstream --pipeline inf-gold | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain downstream | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed D_00c | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed --pipeline bd-silver | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain full --pipeline inf-gold | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript chain incremental --pipeline inf-gold | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.019 | comp-pipescript | comp-pipescript deployed --pipeline inf-gold INF_D_04 (post-fix) | PASS | Bug 1.1 fixed (was UnboundLocalError); 2 MATCH returned cleanly |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.019 | comp-pipescript | comp-pipescript chain downstream --pipeline inf-gold (post-fix) | PASS | Bug 1.2 fixed (was silent BD return); now explicit "Unknown chain: downstream for pipeline inf-gold" + lists valid INF chains (full/incremental/label/silver_prep) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.019 | comp-pipescript | comp-pipescript chain full --pipeline inf-gold (post-fix bonus) | PASS | INF chains confirmed wired post-fix — returns 47 scripts |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.019 | comp-pipescript | comp-pipescript deployed D_00c (regression check) | PASS | BD default unchanged |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.019 | comp-pipescript | comp-pipescript chain downstream (default, regression check) | PASS | BD default unchanged; new label [bd-gold] prefix added |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript inject | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace platinum/firm/leaderboard.json --direction both | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace s3:platinum/firm/leaderboard.json --direction up | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace INF_D_04 --direction down | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace s3:platinum/firm/leaderboard.json --direction up | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace INF_D_04 --direction down --all | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast _build_aua_view | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast inf-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast bd-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace INF_D_04 --direction down --all | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast _build_aua_view | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace s3:platinum/firm/leaderboard.json --direction up | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace D_04 | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-blast | comp-blast build_employee_leaderboard | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.020 | comp-build | comp-build (post-fix) | PASS | Graph extended: 1250→1772 nodes (+42%); 1047→1344 edges (+28%); INF gold +428 function-level nodes; s3:platinum/* +98 nodes |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.020 | comp-trace | comp-trace INF_D_04 --all (post-fix) | PASS | Cat 2.1 was FAIL "No nodes matching"; now returns INF_D_04 + 30+ functions; downstream call edges traced |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.020 | comp-blast | comp-blast _build_aua_view (post-fix) | PASS | Cat 2.2 was FAIL; now BLAST RADIUS shows 4 downstream + 2-deep caller chain (build_partner_analytics → main) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.020 | comp-trace | comp-trace s3:platinum/firm/leaderboard.json (post-fix) | PASS | Cat 2.4 was FAIL; now UPSTREAM with D_04 producer + 6 read-upstream artifacts |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.020 | comp-trace | comp-trace D_04 (BD regression) | PASS | Multi-match output unchanged; same disambiguation flow |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.020 | comp-blast | comp-blast build_employee_leaderboard (BD regression+enrichment) | PASS | Returns blast radius; BD coverage enriched (7→13 GOLD nodes) due to platinum WRITES_S3 edges baked in via inject |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-constants | comp-constants check --lane bd | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-constants | comp-constants check --lane inf | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-trace | comp-trace D_04 --json | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_04 --list | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate D_04 --list --lane bd | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-validate | comp-validate definitely_not_a_thing --list | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript dag --pipeline inf-gold | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript dag | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | check-lambda-layer-deps | check-lambda-layer-deps --function inf-gold-trigger --json | PASS | Cat 3.3 ship: --json flag added for CI/programmatic |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-constants | comp-constants check --lane bd / --lane inf | PASS | Cat 3.4 ship: --lane filter added (bd shows 0 drift; inf shows 7) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-trace | comp-trace D_04 --json (multi-match disambiguation) | PASS | Cat 3.5 ship: multi-match path now emits JSON with match_count + matches[] + hint |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-validate | comp-validate D_04 --list (post-fix tightened matcher) | PASS | Cat 5.2 ship: matcher exact-or-prefix-with-underscore; D_04 matches D_04 + D_04_positions_output but NOT INF_D_04 |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-validate | comp-validate D_04 --list --lane bd | PASS | Cat 5.2 ship: --lane filter added |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-validate | comp-validate definitely_not_a_thing --list (post-fix) | PASS | Cat 5.3 ship: ERROR + 15 candidates emitted; exit 1 (was silent exit 0) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-pipescript | comp-pipescript dag --pipeline inf-gold (post-fix) | PASS | Cat 5.4 ship: now reports "S3 keys (named): 0 | detected paths: 21 (hardcoded)" instead of misleading "S3 keys: 0" |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-tools.yaml | catalog example updates | PASS | Cat 4.1/4.2/4.3/4.4 + 5.1/5.5/5.6: stale examples replaced with canonical forms (PartnerAnalytics, getFirmLeaderboard, real role names, gold:* canonical IDs, origins count 6) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-trace | comp-trace AdvisorPublicProfile (regression sample 1) | PASS | V4.017 PASS retained |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-iam | comp-iam stats (regression sample 2) | PASS | V4.017 PASS retained |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-cache | comp-cache collisions (regression sample 3) | PASS | V4.017 PASS retained |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-platinum | comp-platinum page PartnerAnalytics (regression sample 4) | PASS | V4.017 PASS retained |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.021 | comp-pipescript | comp-pipescript io D_04 (regression sample 5) | PASS | V4.017 PASS retained |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service bd-gold-trigger | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam stats | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse platinum/firm/header_metrics.json#radial_12m | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse platinum/firm/header_metrics.json#radial_12m --strict | FAIL |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse gold/artifacts/employee_leaderboard.json | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.022 | comp-iam | comp-iam service bd-gold-trigger (post-backfill) | PASS | Cat 6.1 ship: role mapped to bd-daily-trigger-lambda-role; ops [GRANTED] (was [UNKNOWN]); 95+ Lambdas backfilled |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.022 | comp-iam | comp-iam gaps (post-backfill) | PASS | 9 real permission gaps surfaced (was 0 due to missing role mappings); queued for separate remediation per TO out-of-scope |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.022 | comp-platinum | comp-platinum reverse 'platinum/firm/header_metrics.json#radial_12m' (post-fix) | PASS | Cat 6.2 ship: CONSUMED BY now empty (was 18 SPECULATIVE); #field intersection, not union |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.022 | comp-platinum | comp-platinum reverse '<key>#field' --strict | PASS | AC4 regression: --strict exits 2 with "18 speculative suppressed" message; behavior preserved |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.022 | comp-platinum | comp-platinum reverse 'gold/artifacts/employee_leaderboard.json' (no #field, regression) | PASS | AC4 regression: 1 SPECULATIVE returned as before (no-#field path unchanged) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.022 | loop-quiescence | loop-quiescence ADHC --summary (post-fix) | PASS | Cat 7.1 ship: NO_PROJECT_FILE verdict + hint to use full project code; was QUIESCENT_CLEAN total=0 false-positive |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.022 | loop-quiescence | loop-quiescence INFETL --summary (post-fix) | PASS | Cat 7.2 ship: same NO_PROJECT_FILE verdict |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.022 | loop-quiescence | loop-quiescence ADHC_COMPIL_V4 --summary (regression) | PASS | AC6 regression: full project code returns ACTIVE verdict with TOs listed (unchanged) |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam service bd-time-machine | PASS |
| 2026-05-08 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-iam | comp-iam gaps | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.023 | comp-iam | comp-iam gaps (pre-fix) | PASS | 9 gaps surfaced post-V4.022 backfill |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.023 | comp-iam | comp-iam service bd-time-machine (pre-fix) | PASS | s3:CopyObject [MISSING]; bd-time-machine-lambda-role policy lacks the action |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.023 | comp-iam | comp-iam service bd-time-machine (post-apply) | PASS | s3:CopyObject [GRANTED]; CopyVersionedRestore statement landed on bd-time-machine-lambda-role:s3-access |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.023 | comp-iam | comp-iam gaps (post-apply) | PASS | 9 → 7 gaps; 7 remaining are EC2-shipped-shell false positives (historical-prices-scheduler, inf-assets-trigger) + AWS-managed-policy false positive (opal-news-layer3-curation under AmazonS3ReadOnlyAccess attachment) |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.024 | comp-iam | comp-iam gaps | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.024 | comp-iam | comp-iam gaps | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.024 | comp-iam | comp-iam gaps | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.024 | comp-iam | comp-iam stats | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.024 | comp-iam | comp-iam gaps | PASS |
| 2026-05-08 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.024 | comp-iam | comp-iam stats | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | ADVI_INFNNA.INF_A_03_PARALLEL-EXPAND | comp-pipescript | comp-pipescript deployed INF_A_03 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | ADVI_INFNNA.INF_A_03_PARALLEL-EXPAND | comp-pipescript | comp-pipescript deployed INF_A_00.accounts_dimension | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | ADVI_INFNNA.INF_A_03_PARALLEL-EXPAND | comp-pipescript | comp-pipescript deployed INF_A_01.advisor_assignments | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | ADVI_INFNNA.INF_A_03_PARALLEL-EXPAND | comp-pipescript | comp-pipescript deployed INF_B_02.canonical_lots | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | ADVI_INFNNA.INF_A_03_PARALLEL-EXPAND | comp-pipescript | comp-pipescript deployed INF_C_01b.role_aua_backfill | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | ADVI_INFNNA.INF_A_03_PARALLEL-EXPAND | comp-pipescript | comp-pipescript deployed INF_C_03.account_performance | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | ADVI_INFNNA.INF_A_03_STALE-PURGE | comp-blast | comp-blast gold/positions_cube | PASS |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-pipescript | comp-pipescript io INF_D_00.portal_aggregates | PASS |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-pipescript | comp-pipescript io INF_D_08.nmec_nmnc_nna | PASS |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-pipescript | comp-pipescript io INF_D_04.client_portal_summary | PASS |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-pipescript | comp-pipescript io INF_D_05.activity_scan | FAIL |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-pipescript | comp-pipescript io INF_D_06.cash_drag | FAIL |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-pipescript | comp-pipescript io INF_D_07.concentration_risk | PASS |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-platinum | comp-platinum reverse advisor_intelligence_executive_summary | PASS |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-platinum | comp-platinum reverse leaderboard | PASS |
| 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-freshness ddb opal-users-v2 WARN(287h>168h) / opal-routing-config FAIL(MISSING) / synthetic 1h FAIL / all exit 1 / chain-bd-regression OK / --list DDB OK | 6/6 ACs PASS | commit 6becc77e5 |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_COMPIL_V4.015 | comp-pipescript | comp-pipescript deployed --pipeline inf-gold INF_D_04 | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-iam | comp-iam gaps | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-blast | comp-blast build_advisor_summary | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-pipescript | comp-pipescript deployed INF_D_04 | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-routes | comp-routes trace getNmecNmncNna | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-cache | comp-cache collisions | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-trace | comp-trace period_start_aua --direction both | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-pipescript | comp-pipescript io INF_D_00b | FAIL |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-pipescript | comp-pipescript io INF_D_00c | FAIL |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-pipescript | comp-pipescript io INF_D_00 | PASS |
| 2026-05-11 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFTGT.TO-4 | comp-pipescript | comp-pipescript io INF_D_00d | FAIL |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_INFRUNNERPARITY.ae-inf-gold-runner-boot-dispatcher-into-repo | comp-trace | comp-trace period_start_aua --direction both | PASS |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_INFRUNNERPARITY.ae-inf-gold-runner-boot-dispatcher-into-repo | comp-pipescript | comp-pipescript io INF_C_02 | PASS |
| 2026-05-11 | 0.7.0_AE_CloudOps | ADHC_INFRUNNERPARITY.ae-inf-gold-runner-boot-dispatcher-into-repo | comp-pipescript | comp-pipescript io INF_D_00b | FAIL |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-transform | comp-transform schema-check PartnerAnalytics | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-transform | comp-transform schema-check DistributionTab | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-cache | comp-cache collisions | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-transform | comp-transform schema-check InflectionInsightsPanel | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-routes | comp-routes trace getFirmHeaderMetrics | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-routes | comp-routes trace getTimeseriesOverview | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-transform | comp-transform schema-check AdvisorsTab --feature unassigned_bucket | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-transform | comp-transform ternary-audit AdvisorsTab | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-routes | comp-routes trace inf-gold-trigger | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-iam | comp-iam service inf-gold-trigger | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-pipescript | comp-pipescript deployed inf-gold-trigger | PASS |
| 2026-05-11 | 0.6.0_AE_PartnerETL | schwab_may_ingest_0508 | comp-iam | comp-iam service inf-gold-trigger | PASS |

## prd-evidence-check --baseline | 2026-05-11T20:23:30Z

| Status | File | Notes |
|--------|------|-------|
| WARN | 49FRECN_STANDING_BACKLOG.md | missing-s5-header,no-comp-tool-citation |
| PASS | 49F_RECONCILIATION_2026-05-01.md |  |
| WARN | ADHC_BASHFIX.md | no-comp-tool-citation |
| WARN | ADHC_CLCOMM.md | no-comp-tool-citation |
| PASS | ADHC_COMPIL.md |  |
| PASS | ADHC_COMPIL_FULL_CORPUS_RETROSPECTIVE.md |  |
| PASS | ADHC_COMPIL_V2.md |  |
| PASS | ADHC_COMPIL_V3.md |  |
| PASS | ADHC_COMPIL_V4.md |  |
| WARN | ADHC_COMPIL_V4_017_TEST_MATRIX.md | missing-s5-header |
| PASS | ADHC_DSFLOW.md |  |
| WARN | ADHC_HISTRY_schwab_bucket_design.md | no-comp-tool-citation |
| WARN | ADHC_LAMBDADOC.md | missing-s5-header |
| WARN | ADHC_OWNPTH.md | no-comp-tool-citation |
| PASS | ADHC_OWNPTH_48H_SCAN.md |  |
| WARN | ADHC_PUSHFIX.md | no-comp-tool-citation |
| WARN | ADHC_TMSTEL_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_49FN_V3_PRD.md | no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_COMPLETION.md | no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md | no-comp-tool-citation |
| PASS | ADVI_49EXEC.md |  |
| WARN | ADVI_49PUSH_AUTH_ARCHITECTURE.md | missing-s5-header |
| WARN | ADVI_49PUSH_P1_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P3_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P4_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P5_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ANONYM_P3_PRD.md | no-comp-tool-citation |
| WARN | ADVI_ANONYM_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_APISCP_PRD.md | no-comp-tool-citation |
| WARN | ADVI_CANNNA_PLAN.md | missing-s5-header |
| WARN | ADVI_CLSPT2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_FEE_WINDOW_REVENUE.md | missing-s5-header |
| PASS | ADVI_FIRMSEP.md |  |
| PASS | ADVI_FIRMSEP_PHASE0_AUDIT.md |  |
| WARN | ADVI_FRONTEND_CORRECTNESS.md | missing-s5-header |
| WARN | ADVI_GLDOPS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_HEADER_SPLIT_PRIMITIVES.md | missing-s5-header |
| WARN | ADVI_HISTBF.md | no-comp-tool-citation |
| WARN | ADVI_INFCAPX.md | no-comp-tool-citation |
| PASS | ADVI_INFETL.md |  |
| PASS | ADVI_INFGRD.md |  |
| PASS | ADVI_INFINGE.md |  |
| PASS | ADVI_INFLEC.md |  |
| WARN | ADVI_INFLEC_AUDIT.md | missing-s5-header |
| PASS | ADVI_INFLEC_BRONZERUN.md |  |
| PASS | ADVI_INFLEC_BRONZERUN_V2.md |  |
| WARN | ADVI_INFLV2.md | no-comp-tool-citation |
| PASS | ADVI_INFREL.md |  |
| WARN | ADVI_INFSHIP.md | no-comp-tool-citation |
| PASS | ADVI_INFSHIP_A2.md |  |
| WARN | ADVI_INFSHIP_PHASE2_BRIEF.md | missing-s5-header,no-comp-tool-citation |
| PASS | ADVI_INFTGT_PRD.md |  |
| WARN | ADVI_JWTRES.md | no-comp-tool-citation |
| WARN | ADVI_MVP318_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_NNAFEE_FEE_EFFICIENCY_VIEWS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_OFFICE_ADDENDUM.md | missing-s5-header |
| PASS | ADVI_OFFICE_PRD.md |  |
| WARN | ADVI_ORIAPI.md | no-comp-tool-citation |
| PASS | ADVI_PROFIL_PRD.md |  |
| WARN | ADVI_PSCFIX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_RDVSDS.md | no-comp-tool-citation |
| WARN | ADVI_REBORN_LEADERBOARD_FEES_ROLES_FIX.md | missing-s5-header |
| WARN | ADVI_REBORN_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_REBORN_WS1_WS3_VALIDATION.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PERMISSION_GROUPS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PRD.md | no-comp-tool-citation |
| WARN | ADVI_ROLLUP.md | missing-s5-header |
| WARN | ADVI_ROLLUP_ADDENDUM_small_account_count.md | missing-s5-header |
| WARN | ADVI_SLEEVE_P0_DECISION.md | missing-s5-header |
| WARN | ADVI_SLEEVE_P1B_ANALYSIS.md | missing-s5-header |
| WARN | ADVI_SLEEVE_PLAN.md | missing-s5-header |
| PASS | ADVI_STAUDT.md |  |
| WARN | ADVI_TICKID_PRD.md | no-comp-tool-citation |
| WARN | ADVI_TICKID_PRICING_DIVERGENCE_ADDENDUM.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_architect_methodology_bifurcation.md | no-comp-tool-citation |
| WARN | ADVI_data_lineage.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_segment_analytics_variance.md | no-comp-tool-citation |
| WARN | AGENT_COMMS_ARCHITECTURE.md | no-comp-tool-citation |
| WARN | AUA_VARIANCE_ANALYSIS_PRD.md | no-comp-tool-citation |
| PASS | AUTH_COTTON.md |  |
| WARN | BD_ASSET_DIM_PIPELINE.md | missing-s5-header |
| WARN | BD_CANONICAL_PRICES_CLASSIFICATION_REFACTOR.md | missing-s5-header |
| WARN | BD_NNA_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| PASS | CDRS_TFIMPT_PHASE2_HANDOFF.md |  |
| WARN | COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md | missing-s5-header |
| WARN | COMPILER_IAM_LAMBDA_PARSER.md | missing-s5-header |
| WARN | COMPILER_INPUT_CANONICALIZATION.md | missing-s5-header |
| WARN | COMPILER_LINT_COVERAGE_PASS.md | missing-s5-header |
| WARN | COMPILER_SILVER_SCOPE_FULL.md | missing-s5-header |
| WARN | COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md | missing-s5-header |
| WARN | COMP_LEARNS_ADVERSARIAL_QUERIES.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_ARCHITECTURE.md |  |
| WARN | COMP_LEARNS_AUTOMATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BACKLOG_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BENCHMARK_AUTHORING_SOP.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_COMPILER_BASELINE.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_DS_ROLE_ADDENDUM.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_HARNESS_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_HTTPX_TARGET.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_INTAKE_WAVE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_LOOP_ORCHESTRATOR.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_OPERATIONAL_MANDATE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_PARALLELIZATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_PHASE2_PROTOCOL_AMENDMENT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PILOT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PROGRAM_PURPOSE.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_QUALITATIVE_FRAMEWORK.md |  |
| WARN | COMP_LEARNS_RUNTIME_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3_PATH_B.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_2_SELECTION.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_CLOSEOUT.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_UNDOCUMENTED_SURFACES.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_WAVE3_V1.md |  |
| WARN | COMP_LEARNS_WAVE_PRD_TEMPLATE.md | no-comp-tool-citation |
| PASS | COMP_VALIDATE_PROTOCOL.md |  |
| WARN | DISTRIBUTION_TAB_OTHER_DEDUPE.md | missing-s5-header |
| WARN | DRFR_PTMCH_CANON_INTERLOCK_PRD.md | no-comp-tool-citation |
| WARN | DRFR_PTMCH_PRD.md | no-comp-tool-citation |
| WARN | EC2_TELEMETRY_DESIGN.md | missing-s5-header,no-comp-tool-citation |
| WARN | ETFS_SECIDX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_BLAST_RADIUS_ASSESSMENT.md | no-comp-tool-citation |
| WARN | GLDRST_COO_BRIEFING_INTEGRATION_TESTING.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_P3_OPERATIONAL_READINESS.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_ROLLBACK_PLAN.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_PERF_PRD.md | missing-s5-header |
| WARN | IDTY_RENAME_PRD.md | no-comp-tool-citation |
| PASS | INCREMENTAL_RUNS_DESIGN.md |  |
| PASS | INFETL_DAILY_PULLS_MATRIX.md |  |
| PASS | INFETL_MASTER_DATA_REGISTRY.md |  |
| WARN | INFETL_PORTAL_ROUTE_MATRIX.md | missing-s5-header |
| WARN | INFETL_PULL_SHAPE_VERIFY.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_API_ENDPOINTS_CATALOG.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_BD_PARITY_MATRIX.md | no-comp-tool-citation |
| WARN | INFLEC_BOOKSTAB_TAX_FIELD_MAP.md | no-comp-tool-citation |
| WARN | INFLEC_DATA_INVENTORY.md | no-comp-tool-citation |
| WARN | INFLEC_DIMS_AND_TRANSACTIONS.md | no-comp-tool-citation |
| WARN | INFLEC_DIM_PULL_REQUESTS.md | no-comp-tool-citation |
| WARN | INFLEC_ENRICH_SCOPE.md | missing-s5-header,no-comp-tool-citation |
| PASS | INFLEC_FE_BACKEND_WIRING.md |  |
| WARN | INFLEC_PARITY_FILL_CANDIDATES.md | no-comp-tool-citation |
| WARN | INFLEC_PORTAL_FIELD_USAGE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_TRANSACTIONS_API_PROBE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLV2_BOOKS_SCOPE_FREEZE.md | missing-s5-header,no-comp-tool-citation |
| PASS | MDLP_RVVALT.md |  |
| WARN | MDLP_RVVALT_RFR_SPEC.md | no-comp-tool-citation |
| WARN | MDLP_WYNCHT_PRD.md | no-comp-tool-citation |
| WARN | MKOV_TRENDS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | NNA_VARIANCE_OPTIMIZATION_PRD.md | no-comp-tool-citation |
| WARN | PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md | missing-s5-header,no-comp-tool-citation |
| PASS | PORTAL_STAT_STRIP_DENSITY.md |  |
| WARN | PORTFOLIO_EXPORT_TRADE_SUBMISSION_BRIDGE.md | no-comp-tool-citation |
| PASS | PRD_AUTHORING_PROTOCOL.md |  |
| WARN | ROLE_AUA_CANONICAL_CONVERGENCE_PLAN.md | missing-s5-header |
| WARN | SECURITY_SCANNER_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT_COMPACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DATA_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DESIGN_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | TRADE_ENGINE_VISUAL_POLISH.md | no-comp-tool-citation |
| PASS | TRSB_PATHFIX_PRD.md |  |
| PASS | TRSB_TFIMPT.md |  |
| WARN | gold-artifact-mapping.md | missing-s5-header,no-comp-tool-citation |

Total: 38 PASS, 127 WARN, 165 PRDs scanned.

## prd-evidence-check --baseline | 2026-05-11T20:28:10Z

| Status | File | Notes |
|--------|------|-------|
| WARN | 49FRECN_STANDING_BACKLOG.md | missing-s5-header,no-comp-tool-citation |
| PASS | 49F_RECONCILIATION_2026-05-01.md |  |
| WARN | ADHC_BASHFIX.md | no-comp-tool-citation |
| WARN | ADHC_CLCOMM.md | no-comp-tool-citation |
| PASS | ADHC_COMPIL.md |  |
| PASS | ADHC_COMPIL_FULL_CORPUS_RETROSPECTIVE.md |  |
| PASS | ADHC_COMPIL_V2.md |  |
| PASS | ADHC_COMPIL_V3.md |  |
| PASS | ADHC_COMPIL_V4.md |  |
| WARN | ADHC_COMPIL_V4_017_TEST_MATRIX.md | missing-s5-header |
| PASS | ADHC_DSFLOW.md |  |
| WARN | ADHC_HISTRY_schwab_bucket_design.md | no-comp-tool-citation |
| WARN | ADHC_LAMBDADOC.md | missing-s5-header |
| WARN | ADHC_OWNPTH.md | no-comp-tool-citation |
| PASS | ADHC_OWNPTH_48H_SCAN.md |  |
| WARN | ADHC_PUSHFIX.md | no-comp-tool-citation |
| WARN | ADHC_TMSTEL_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_49FN_V3_PRD.md | no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_COMPLETION.md | no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md | no-comp-tool-citation |
| PASS | ADVI_49EXEC.md |  |
| WARN | ADVI_49PUSH_AUTH_ARCHITECTURE.md | missing-s5-header |
| WARN | ADVI_49PUSH_P1_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P3_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P4_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P5_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ANONYM_P3_PRD.md | no-comp-tool-citation |
| WARN | ADVI_ANONYM_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_APISCP_PRD.md | no-comp-tool-citation |
| WARN | ADVI_CANNNA_PLAN.md | missing-s5-header |
| WARN | ADVI_CLSPT2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_FEE_WINDOW_REVENUE.md | missing-s5-header |
| PASS | ADVI_FIRMSEP.md |  |
| PASS | ADVI_FIRMSEP_PHASE0_AUDIT.md |  |
| WARN | ADVI_FRONTEND_CORRECTNESS.md | missing-s5-header |
| WARN | ADVI_GLDOPS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_HEADER_SPLIT_PRIMITIVES.md | missing-s5-header |
| WARN | ADVI_HISTBF.md | no-comp-tool-citation |
| WARN | ADVI_INFCAPX.md | no-comp-tool-citation |
| PASS | ADVI_INFETL.md |  |
| PASS | ADVI_INFGRD.md |  |
| PASS | ADVI_INFINGE.md |  |
| PASS | ADVI_INFLEC.md |  |
| WARN | ADVI_INFLEC_AUDIT.md | missing-s5-header |
| PASS | ADVI_INFLEC_BRONZERUN.md |  |
| PASS | ADVI_INFLEC_BRONZERUN_V2.md |  |
| WARN | ADVI_INFLV2.md | no-comp-tool-citation |
| PASS | ADVI_INFREL.md |  |
| WARN | ADVI_INFSHIP.md | no-comp-tool-citation |
| PASS | ADVI_INFSHIP_A2.md |  |
| WARN | ADVI_INFSHIP_PHASE2_BRIEF.md | missing-s5-header,no-comp-tool-citation |
| PASS | ADVI_INFTGT_PRD.md |  |
| WARN | ADVI_JWTRES.md | no-comp-tool-citation |
| WARN | ADVI_MVP318_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_NNAFEE_FEE_EFFICIENCY_VIEWS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_OFFICE_ADDENDUM.md | missing-s5-header |
| PASS | ADVI_OFFICE_PRD.md |  |
| WARN | ADVI_ORIAPI.md | no-comp-tool-citation |
| PASS | ADVI_PROFIL_PRD.md |  |
| WARN | ADVI_PSCFIX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_RDVSDS.md | no-comp-tool-citation |
| WARN | ADVI_REBORN_LEADERBOARD_FEES_ROLES_FIX.md | missing-s5-header |
| WARN | ADVI_REBORN_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_REBORN_WS1_WS3_VALIDATION.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PERMISSION_GROUPS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PRD.md | no-comp-tool-citation |
| WARN | ADVI_ROLLUP.md | missing-s5-header |
| WARN | ADVI_ROLLUP_ADDENDUM_small_account_count.md | missing-s5-header |
| WARN | ADVI_SLEEVE_P0_DECISION.md | missing-s5-header |
| WARN | ADVI_SLEEVE_P1B_ANALYSIS.md | missing-s5-header |
| WARN | ADVI_SLEEVE_PLAN.md | missing-s5-header |
| PASS | ADVI_STAUDT.md |  |
| WARN | ADVI_TICKID_PRD.md | no-comp-tool-citation |
| WARN | ADVI_TICKID_PRICING_DIVERGENCE_ADDENDUM.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_architect_methodology_bifurcation.md | no-comp-tool-citation |
| WARN | ADVI_data_lineage.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_segment_analytics_variance.md | no-comp-tool-citation |
| WARN | AGENT_COMMS_ARCHITECTURE.md | no-comp-tool-citation |
| WARN | AUA_VARIANCE_ANALYSIS_PRD.md | no-comp-tool-citation |
| PASS | AUTH_COTTON.md |  |
| WARN | BD_ASSET_DIM_PIPELINE.md | missing-s5-header |
| WARN | BD_CANONICAL_PRICES_CLASSIFICATION_REFACTOR.md | missing-s5-header |
| WARN | BD_NNA_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| PASS | CDRS_TFIMPT_PHASE2_HANDOFF.md |  |
| WARN | COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md | missing-s5-header |
| WARN | COMPILER_IAM_LAMBDA_PARSER.md | missing-s5-header |
| WARN | COMPILER_INPUT_CANONICALIZATION.md | missing-s5-header |
| WARN | COMPILER_LINT_COVERAGE_PASS.md | missing-s5-header |
| WARN | COMPILER_SILVER_SCOPE_FULL.md | missing-s5-header |
| WARN | COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md | missing-s5-header |
| WARN | COMP_LEARNS_ADVERSARIAL_QUERIES.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_ARCHITECTURE.md |  |
| WARN | COMP_LEARNS_AUTOMATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BACKLOG_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BENCHMARK_AUTHORING_SOP.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_COMPILER_BASELINE.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_DS_ROLE_ADDENDUM.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_HARNESS_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_HTTPX_TARGET.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_INTAKE_WAVE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_LOOP_ORCHESTRATOR.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_OPERATIONAL_MANDATE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_PARALLELIZATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_PHASE2_PROTOCOL_AMENDMENT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PILOT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PROGRAM_PURPOSE.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_QUALITATIVE_FRAMEWORK.md |  |
| WARN | COMP_LEARNS_RUNTIME_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3_PATH_B.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_2_SELECTION.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_CLOSEOUT.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_UNDOCUMENTED_SURFACES.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_WAVE3_V1.md |  |
| WARN | COMP_LEARNS_WAVE_PRD_TEMPLATE.md | no-comp-tool-citation |
| PASS | COMP_VALIDATE_PROTOCOL.md |  |
| WARN | DISTRIBUTION_TAB_OTHER_DEDUPE.md | missing-s5-header |
| WARN | DRFR_PTMCH_CANON_INTERLOCK_PRD.md | no-comp-tool-citation |
| WARN | DRFR_PTMCH_PRD.md | no-comp-tool-citation |
| WARN | EC2_TELEMETRY_DESIGN.md | missing-s5-header,no-comp-tool-citation |
| WARN | ETFS_SECIDX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_BLAST_RADIUS_ASSESSMENT.md | no-comp-tool-citation |
| WARN | GLDRST_COO_BRIEFING_INTEGRATION_TESTING.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_P3_OPERATIONAL_READINESS.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_ROLLBACK_PLAN.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_PERF_PRD.md | missing-s5-header |
| WARN | IDTY_RENAME_PRD.md | no-comp-tool-citation |
| PASS | INCREMENTAL_RUNS_DESIGN.md |  |
| PASS | INFETL_DAILY_PULLS_MATRIX.md |  |
| PASS | INFETL_MASTER_DATA_REGISTRY.md |  |
| WARN | INFETL_PORTAL_ROUTE_MATRIX.md | missing-s5-header |
| WARN | INFETL_PULL_SHAPE_VERIFY.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_API_ENDPOINTS_CATALOG.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_BD_PARITY_MATRIX.md | no-comp-tool-citation |
| WARN | INFLEC_BOOKSTAB_TAX_FIELD_MAP.md | no-comp-tool-citation |
| WARN | INFLEC_DATA_INVENTORY.md | no-comp-tool-citation |
| WARN | INFLEC_DIMS_AND_TRANSACTIONS.md | no-comp-tool-citation |
| WARN | INFLEC_DIM_PULL_REQUESTS.md | no-comp-tool-citation |
| WARN | INFLEC_ENRICH_SCOPE.md | missing-s5-header,no-comp-tool-citation |
| PASS | INFLEC_FE_BACKEND_WIRING.md |  |
| WARN | INFLEC_PARITY_FILL_CANDIDATES.md | no-comp-tool-citation |
| WARN | INFLEC_PORTAL_FIELD_USAGE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_TRANSACTIONS_API_PROBE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLV2_BOOKS_SCOPE_FREEZE.md | missing-s5-header,no-comp-tool-citation |
| PASS | MDLP_RVVALT.md |  |
| WARN | MDLP_RVVALT_RFR_SPEC.md | no-comp-tool-citation |
| WARN | MDLP_WYNCHT_PRD.md | no-comp-tool-citation |
| WARN | MKOV_TRENDS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | NNA_VARIANCE_OPTIMIZATION_PRD.md | no-comp-tool-citation |
| WARN | PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md | missing-s5-header,no-comp-tool-citation |
| PASS | PORTAL_STAT_STRIP_DENSITY.md |  |
| WARN | PORTFOLIO_EXPORT_TRADE_SUBMISSION_BRIDGE.md | no-comp-tool-citation |
| PASS | PRD_AUTHORING_PROTOCOL.md |  |
| WARN | ROLE_AUA_CANONICAL_CONVERGENCE_PLAN.md | missing-s5-header |
| WARN | SECURITY_SCANNER_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT_COMPACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DATA_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DESIGN_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | TRADE_ENGINE_VISUAL_POLISH.md | no-comp-tool-citation |
| PASS | TRSB_PATHFIX_PRD.md |  |
| PASS | TRSB_TFIMPT.md |  |
| WARN | gold-artifact-mapping.md | missing-s5-header,no-comp-tool-citation |

Total: 38 PASS, 127 WARN, 165 PRDs scanned.

## prd-evidence-check --baseline | 2026-05-11T20:17:26Z

| Status | File | Notes |
|--------|------|-------|
| PASS | 49F_RECONCILIATION_2026-05-01.md |  |
| WARN | 49FRECN_STANDING_BACKLOG.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADHC_BASHFIX.md | no-comp-tool-citation |
| WARN | ADHC_CLCOMM.md | no-comp-tool-citation |
| PASS | ADHC_COMPIL.md |  |
| PASS | ADHC_COMPIL_FULL_CORPUS_RETROSPECTIVE.md |  |
| PASS | ADHC_COMPIL_V2.md |  |
| PASS | ADHC_COMPIL_V3.md |  |
| PASS | ADHC_COMPIL_V4.md |  |
| WARN | ADHC_COMPIL_V4_017_TEST_MATRIX.md | missing-s5-header |
| PASS | ADHC_DSFLOW.md |  |
| WARN | ADHC_HISTRY_schwab_bucket_design.md | no-comp-tool-citation |
| WARN | ADHC_LAMBDADOC.md | missing-s5-header |
| WARN | ADHC_OWNPTH.md | no-comp-tool-citation |
| PASS | ADHC_OWNPTH_48H_SCAN.md |  |
| WARN | ADHC_PUSHFIX.md | no-comp-tool-citation |
| WARN | ADHC_TMSTEL_PRD.md | missing-s5-header,no-comp-tool-citation |
| PASS | ADVI_49EXEC.md |  |
| WARN | ADVI_49PUSH_AUTH_ARCHITECTURE.md | missing-s5-header |
| WARN | ADVI_49PUSH_P1_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P3_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P4_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P5_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ANONYM_P3_PRD.md | no-comp-tool-citation |
| WARN | ADVI_ANONYM_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_APISCP_PRD.md | no-comp-tool-citation |
| WARN | ADVI_architect_methodology_bifurcation.md | no-comp-tool-citation |
| WARN | ADVI_CANNNA_PLAN.md | missing-s5-header |
| WARN | ADVI_CLSPT2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_data_lineage.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_FEE_WINDOW_REVENUE.md | missing-s5-header |
| PASS | ADVI_FIRMSEP.md |  |
| PASS | ADVI_FIRMSEP_PHASE0_AUDIT.md |  |
| WARN | ADVI_FRONTEND_CORRECTNESS.md | missing-s5-header |
| WARN | ADVI_GLDOPS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_HEADER_SPLIT_PRIMITIVES.md | missing-s5-header |
| WARN | ADVI_HISTBF.md | no-comp-tool-citation |
| WARN | ADVI_INFCAPX.md | no-comp-tool-citation |
| PASS | ADVI_INFETL.md |  |
| PASS | ADVI_INFGRD.md |  |
| PASS | ADVI_INFINGE.md |  |
| PASS | ADVI_INFLEC.md |  |
| WARN | ADVI_INFLEC_AUDIT.md | missing-s5-header |
| PASS | ADVI_INFLEC_BRONZERUN.md |  |
| PASS | ADVI_INFLEC_BRONZERUN_V2.md |  |
| WARN | ADVI_INFLV2.md | no-comp-tool-citation |
| PASS | ADVI_INFREL.md |  |
| WARN | ADVI_INFSHIP.md | no-comp-tool-citation |
| PASS | ADVI_INFSHIP_A2.md |  |
| WARN | ADVI_INFSHIP_PHASE2_BRIEF.md | missing-s5-header,no-comp-tool-citation |
| PASS | ADVI_INFTGT_PRD.md |  |
| WARN | ADVI_JWTRES.md | no-comp-tool-citation |
| WARN | ADVI_MVP318_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_NNAFEE_FEE_EFFICIENCY_VIEWS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_OFFICE_ADDENDUM.md | missing-s5-header |
| PASS | ADVI_OFFICE_PRD.md |  |
| WARN | ADVI_ORIAPI.md | no-comp-tool-citation |
| PASS | ADVI_PROFIL_PRD.md |  |
| WARN | ADVI_PSCFIX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_RDVSDS.md | no-comp-tool-citation |
| WARN | ADVI_REBORN_LEADERBOARD_FEES_ROLES_FIX.md | missing-s5-header |
| WARN | ADVI_REBORN_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_REBORN_WS1_WS3_VALIDATION.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PERMISSION_GROUPS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PRD.md | no-comp-tool-citation |
| WARN | ADVI_ROLLUP.md | missing-s5-header |
| WARN | ADVI_ROLLUP_ADDENDUM_small_account_count.md | missing-s5-header |
| WARN | ADVI_segment_analytics_variance.md | no-comp-tool-citation |
| WARN | ADVI_SLEEVE_P0_DECISION.md | missing-s5-header |
| WARN | ADVI_SLEEVE_P1B_ANALYSIS.md | missing-s5-header |
| WARN | ADVI_SLEEVE_PLAN.md | missing-s5-header |
| PASS | ADVI_STAUDT.md |  |
| WARN | ADVI_TICKID_PRD.md | no-comp-tool-citation |
| WARN | ADVI_TICKID_PRICING_DIVERGENCE_ADDENDUM.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_49FN_V3_PRD.md | no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_COMPLETION.md | no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md | no-comp-tool-citation |
| WARN | AGENT_COMMS_ARCHITECTURE.md | no-comp-tool-citation |
| WARN | AUA_VARIANCE_ANALYSIS_PRD.md | no-comp-tool-citation |
| PASS | AUTH_COTTON.md |  |
| WARN | BD_ASSET_DIM_PIPELINE.md | missing-s5-header |
| WARN | BD_CANONICAL_PRICES_CLASSIFICATION_REFACTOR.md | missing-s5-header |
| WARN | BD_NNA_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| PASS | CDRS_TFIMPT_PHASE2_HANDOFF.md |  |
| WARN | COMP_LEARNS_ADVERSARIAL_QUERIES.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_ARCHITECTURE.md |  |
| WARN | COMP_LEARNS_AUTOMATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BACKLOG_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BENCHMARK_AUTHORING_SOP.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_COMPILER_BASELINE.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_DS_ROLE_ADDENDUM.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_HARNESS_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_HTTPX_TARGET.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_INTAKE_WAVE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_LOOP_ORCHESTRATOR.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_OPERATIONAL_MANDATE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_PARALLELIZATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_PHASE2_PROTOCOL_AMENDMENT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PILOT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PROGRAM_PURPOSE.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_QUALITATIVE_FRAMEWORK.md |  |
| WARN | COMP_LEARNS_RUNTIME_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3_PATH_B.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_2_SELECTION.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_CLOSEOUT.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_UNDOCUMENTED_SURFACES.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_WAVE_PRD_TEMPLATE.md | no-comp-tool-citation |
| PASS | COMP_LEARNS_WAVE3_V1.md |  |
| PASS | COMP_VALIDATE_PROTOCOL.md |  |
| WARN | COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md | missing-s5-header |
| WARN | COMPILER_IAM_LAMBDA_PARSER.md | missing-s5-header |
| WARN | COMPILER_INPUT_CANONICALIZATION.md | missing-s5-header |
| WARN | COMPILER_LINT_COVERAGE_PASS.md | missing-s5-header |
| WARN | COMPILER_SILVER_SCOPE_FULL.md | missing-s5-header |
| WARN | COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md | missing-s5-header |
| WARN | DISTRIBUTION_TAB_OTHER_DEDUPE.md | missing-s5-header |
| WARN | DRFR_PTMCH_CANON_INTERLOCK_PRD.md | no-comp-tool-citation |
| WARN | DRFR_PTMCH_PRD.md | no-comp-tool-citation |
| WARN | EC2_TELEMETRY_DESIGN.md | missing-s5-header,no-comp-tool-citation |
| WARN | ETFS_SECIDX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_BLAST_RADIUS_ASSESSMENT.md | no-comp-tool-citation |
| WARN | GLDRST_COO_BRIEFING_INTEGRATION_TESTING.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_P3_OPERATIONAL_READINESS.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_ROLLBACK_PLAN.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_PERF_PRD.md | missing-s5-header |
| WARN | gold-artifact-mapping.md | missing-s5-header,no-comp-tool-citation |
| WARN | IDTY_RENAME_PRD.md | no-comp-tool-citation |
| PASS | INCREMENTAL_RUNS_DESIGN.md |  |
| PASS | INFETL_DAILY_PULLS_MATRIX.md |  |
| PASS | INFETL_MASTER_DATA_REGISTRY.md |  |
| WARN | INFETL_PORTAL_ROUTE_MATRIX.md | missing-s5-header |
| WARN | INFETL_PULL_SHAPE_VERIFY.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_API_ENDPOINTS_CATALOG.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_BD_PARITY_MATRIX.md | no-comp-tool-citation |
| WARN | INFLEC_BOOKSTAB_TAX_FIELD_MAP.md | no-comp-tool-citation |
| WARN | INFLEC_DATA_INVENTORY.md | no-comp-tool-citation |
| WARN | INFLEC_DIM_PULL_REQUESTS.md | no-comp-tool-citation |
| WARN | INFLEC_DIMS_AND_TRANSACTIONS.md | no-comp-tool-citation |
| WARN | INFLEC_ENRICH_SCOPE.md | missing-s5-header,no-comp-tool-citation |
| PASS | INFLEC_FE_BACKEND_WIRING.md |  |
| WARN | INFLEC_PARITY_FILL_CANDIDATES.md | no-comp-tool-citation |
| WARN | INFLEC_PORTAL_FIELD_USAGE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_TRANSACTIONS_API_PROBE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLV2_BOOKS_SCOPE_FREEZE.md | missing-s5-header,no-comp-tool-citation |
| PASS | MDLP_RVVALT.md |  |
| WARN | MDLP_RVVALT_RFR_SPEC.md | no-comp-tool-citation |
| WARN | MDLP_WYNCHT_PRD.md | no-comp-tool-citation |
| WARN | MKOV_TRENDS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | NNA_VARIANCE_OPTIMIZATION_PRD.md | no-comp-tool-citation |
| WARN | PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md | missing-s5-header,no-comp-tool-citation |
| PASS | PORTAL_STAT_STRIP_DENSITY.md |  |
| WARN | PORTFOLIO_EXPORT_TRADE_SUBMISSION_BRIDGE.md | no-comp-tool-citation |
| PASS | PRD_AUTHORING_PROTOCOL.md |  |
| WARN | ROLE_AUA_CANONICAL_CONVERGENCE_PLAN.md | missing-s5-header |
| WARN | SECURITY_SCANNER_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT_COMPACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DATA_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DESIGN_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | TRADE_ENGINE_VISUAL_POLISH.md | no-comp-tool-citation |
| PASS | TRSB_PATHFIX_PRD.md |  |
| PASS | TRSB_TFIMPT.md |  |

Total: 38 PASS, 127 WARN, 165 PRDs scanned.

## prd-evidence-check --baseline | 2026-05-11T20:20:28Z

| Status | File | Notes |
|--------|------|-------|
| PASS | 49F_RECONCILIATION_2026-05-01.md |  |
| WARN | 49FRECN_STANDING_BACKLOG.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADHC_BASHFIX.md | no-comp-tool-citation |
| WARN | ADHC_CLCOMM.md | no-comp-tool-citation |
| PASS | ADHC_COMPIL.md |  |
| PASS | ADHC_COMPIL_FULL_CORPUS_RETROSPECTIVE.md |  |
| PASS | ADHC_COMPIL_V2.md |  |
| PASS | ADHC_COMPIL_V3.md |  |
| PASS | ADHC_COMPIL_V4.md |  |
| WARN | ADHC_COMPIL_V4_017_TEST_MATRIX.md | missing-s5-header |
| PASS | ADHC_DSFLOW.md |  |
| WARN | ADHC_HISTRY_schwab_bucket_design.md | no-comp-tool-citation |
| WARN | ADHC_LAMBDADOC.md | missing-s5-header |
| WARN | ADHC_OWNPTH.md | no-comp-tool-citation |
| PASS | ADHC_OWNPTH_48H_SCAN.md |  |
| WARN | ADHC_PUSHFIX.md | no-comp-tool-citation |
| WARN | ADHC_TMSTEL_PRD.md | missing-s5-header,no-comp-tool-citation |
| PASS | ADVI_49EXEC.md |  |
| WARN | ADVI_49PUSH_AUTH_ARCHITECTURE.md | missing-s5-header |
| WARN | ADVI_49PUSH_P1_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P3_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P4_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_49PUSH_P5_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ANONYM_P3_PRD.md | no-comp-tool-citation |
| WARN | ADVI_ANONYM_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_APISCP_PRD.md | no-comp-tool-citation |
| WARN | ADVI_architect_methodology_bifurcation.md | no-comp-tool-citation |
| WARN | ADVI_CANNNA_PLAN.md | missing-s5-header |
| WARN | ADVI_CLSPT2_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_data_lineage.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_FEE_WINDOW_REVENUE.md | missing-s5-header |
| PASS | ADVI_FIRMSEP.md |  |
| PASS | ADVI_FIRMSEP_PHASE0_AUDIT.md |  |
| WARN | ADVI_FRONTEND_CORRECTNESS.md | missing-s5-header |
| WARN | ADVI_GLDOPS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_HEADER_SPLIT_PRIMITIVES.md | missing-s5-header |
| WARN | ADVI_HISTBF.md | no-comp-tool-citation |
| WARN | ADVI_INFCAPX.md | no-comp-tool-citation |
| PASS | ADVI_INFETL.md |  |
| PASS | ADVI_INFGRD.md |  |
| PASS | ADVI_INFINGE.md |  |
| PASS | ADVI_INFLEC.md |  |
| WARN | ADVI_INFLEC_AUDIT.md | missing-s5-header |
| PASS | ADVI_INFLEC_BRONZERUN.md |  |
| PASS | ADVI_INFLEC_BRONZERUN_V2.md |  |
| WARN | ADVI_INFLV2.md | no-comp-tool-citation |
| PASS | ADVI_INFREL.md |  |
| WARN | ADVI_INFSHIP.md | no-comp-tool-citation |
| PASS | ADVI_INFSHIP_A2.md |  |
| WARN | ADVI_INFSHIP_PHASE2_BRIEF.md | missing-s5-header,no-comp-tool-citation |
| PASS | ADVI_INFTGT_PRD.md |  |
| WARN | ADVI_JWTRES.md | no-comp-tool-citation |
| WARN | ADVI_MVP318_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_NNAFEE_FEE_EFFICIENCY_VIEWS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_OFFICE_ADDENDUM.md | missing-s5-header |
| PASS | ADVI_OFFICE_PRD.md |  |
| WARN | ADVI_ORIAPI.md | no-comp-tool-citation |
| PASS | ADVI_PROFIL_PRD.md |  |
| WARN | ADVI_PSCFIX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_RDVSDS.md | no-comp-tool-citation |
| WARN | ADVI_REBORN_LEADERBOARD_FEES_ROLES_FIX.md | missing-s5-header |
| WARN | ADVI_REBORN_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_REBORN_WS1_WS3_VALIDATION.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PERMISSION_GROUPS.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVI_ROLGAT_PRD.md | no-comp-tool-citation |
| WARN | ADVI_ROLLUP.md | missing-s5-header |
| WARN | ADVI_ROLLUP_ADDENDUM_small_account_count.md | missing-s5-header |
| WARN | ADVI_segment_analytics_variance.md | no-comp-tool-citation |
| WARN | ADVI_SLEEVE_P0_DECISION.md | missing-s5-header |
| WARN | ADVI_SLEEVE_P1B_ANALYSIS.md | missing-s5-header |
| WARN | ADVI_SLEEVE_PLAN.md | missing-s5-header |
| PASS | ADVI_STAUDT.md |  |
| WARN | ADVI_TICKID_PRD.md | no-comp-tool-citation |
| WARN | ADVI_TICKID_PRICING_DIVERGENCE_ADDENDUM.md | missing-s5-header,no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_49FN_V3_PRD.md | no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_COMPLETION.md | no-comp-tool-citation |
| WARN | ADVISOR_INTELLIGENCE_YANG_FEEDBACK_V2.md | no-comp-tool-citation |
| WARN | AGENT_COMMS_ARCHITECTURE.md | no-comp-tool-citation |
| WARN | AUA_VARIANCE_ANALYSIS_PRD.md | no-comp-tool-citation |
| PASS | AUTH_COTTON.md |  |
| WARN | BD_ASSET_DIM_PIPELINE.md | missing-s5-header |
| WARN | BD_CANONICAL_PRICES_CLASSIFICATION_REFACTOR.md | missing-s5-header |
| WARN | BD_NNA_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| PASS | CDRS_TFIMPT_PHASE2_HANDOFF.md |  |
| WARN | COMP_LEARNS_ADVERSARIAL_QUERIES.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_ARCHITECTURE.md |  |
| WARN | COMP_LEARNS_AUTOMATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BACKLOG_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_BENCHMARK_AUTHORING_SOP.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_COMPILER_BASELINE.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_DS_ROLE_ADDENDUM.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_HARNESS_FRAMEWORK.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_HTTPX_TARGET.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_INTAKE_WAVE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_LOOP_ORCHESTRATOR.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_OPERATIONAL_MANDATE.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_PARALLELIZATION_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_PHASE2_PROTOCOL_AMENDMENT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PILOT.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_PROGRAM_PURPOSE.md | missing-s5-header,no-comp-tool-citation |
| PASS | COMP_LEARNS_QUALITATIVE_FRAMEWORK.md |  |
| WARN | COMP_LEARNS_RUNTIME_V1.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_STAGE3_PATH_B.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_2_SELECTION.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_TARGET_CLOSEOUT.md | no-comp-tool-citation |
| WARN | COMP_LEARNS_UNDOCUMENTED_SURFACES.md | missing-s5-header,no-comp-tool-citation |
| WARN | COMP_LEARNS_WAVE_PRD_TEMPLATE.md | no-comp-tool-citation |
| PASS | COMP_LEARNS_WAVE3_V1.md |  |
| PASS | COMP_VALIDATE_PROTOCOL.md |  |
| WARN | COMPILER_BLAST_SCRIPT_ARTIFACT_EDGES.md | missing-s5-header |
| WARN | COMPILER_IAM_LAMBDA_PARSER.md | missing-s5-header |
| WARN | COMPILER_INPUT_CANONICALIZATION.md | missing-s5-header |
| WARN | COMPILER_LINT_COVERAGE_PASS.md | missing-s5-header |
| WARN | COMPILER_SILVER_SCOPE_FULL.md | missing-s5-header |
| WARN | COMPILER_VALIDATE_COVERAGE_AND_PASSTHROUGH.md | missing-s5-header |
| WARN | DISTRIBUTION_TAB_OTHER_DEDUPE.md | missing-s5-header |
| WARN | DRFR_PTMCH_CANON_INTERLOCK_PRD.md | no-comp-tool-citation |
| WARN | DRFR_PTMCH_PRD.md | no-comp-tool-citation |
| WARN | EC2_TELEMETRY_DESIGN.md | missing-s5-header,no-comp-tool-citation |
| WARN | ETFS_SECIDX_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_BLAST_RADIUS_ASSESSMENT.md | no-comp-tool-citation |
| WARN | GLDRST_COO_BRIEFING_INTEGRATION_TESTING.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_P3_OPERATIONAL_READINESS.md | missing-s5-header,no-comp-tool-citation |
| WARN | GLDRST_ROLLBACK_PLAN.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md | missing-s5-header,no-comp-tool-citation |
| WARN | GOLD_PERF_PRD.md | missing-s5-header |
| WARN | gold-artifact-mapping.md | missing-s5-header,no-comp-tool-citation |
| WARN | IDTY_RENAME_PRD.md | no-comp-tool-citation |
| PASS | INCREMENTAL_RUNS_DESIGN.md |  |
| PASS | INFETL_DAILY_PULLS_MATRIX.md |  |
| PASS | INFETL_MASTER_DATA_REGISTRY.md |  |
| WARN | INFETL_PORTAL_ROUTE_MATRIX.md | missing-s5-header |
| WARN | INFETL_PULL_SHAPE_VERIFY.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_API_ENDPOINTS_CATALOG.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_BD_PARITY_MATRIX.md | no-comp-tool-citation |
| WARN | INFLEC_BOOKSTAB_TAX_FIELD_MAP.md | no-comp-tool-citation |
| WARN | INFLEC_DATA_INVENTORY.md | no-comp-tool-citation |
| WARN | INFLEC_DIM_PULL_REQUESTS.md | no-comp-tool-citation |
| WARN | INFLEC_DIMS_AND_TRANSACTIONS.md | no-comp-tool-citation |
| WARN | INFLEC_ENRICH_SCOPE.md | missing-s5-header,no-comp-tool-citation |
| PASS | INFLEC_FE_BACKEND_WIRING.md |  |
| WARN | INFLEC_PARITY_FILL_CANDIDATES.md | no-comp-tool-citation |
| WARN | INFLEC_PORTAL_FIELD_USAGE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLEC_TRANSACTIONS_API_PROBE.md | missing-s5-header,no-comp-tool-citation |
| WARN | INFLV2_BOOKS_SCOPE_FREEZE.md | missing-s5-header,no-comp-tool-citation |
| PASS | MDLP_RVVALT.md |  |
| WARN | MDLP_RVVALT_RFR_SPEC.md | no-comp-tool-citation |
| WARN | MDLP_WYNCHT_PRD.md | no-comp-tool-citation |
| WARN | MKOV_TRENDS_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | NNA_VARIANCE_OPTIMIZATION_PRD.md | no-comp-tool-citation |
| WARN | PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md | missing-s5-header,no-comp-tool-citation |
| PASS | PORTAL_STAT_STRIP_DENSITY.md |  |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| WARN | PORTFOLIO_EXPORT_TRADE_SUBMISSION_BRIDGE.md | no-comp-tool-citation |
| PASS | PRD_AUTHORING_PROTOCOL.md |  |
| WARN | ROLE_AUA_CANONICAL_CONVERGENCE_PLAN.md | missing-s5-header |
| WARN | SECURITY_SCANNER_PRD.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SECURITY_SCANNER_XLSM_AUDIT_COMPACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DATA_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | SSCN_DESIGN_CONTRACT.md | missing-s5-header,no-comp-tool-citation |
| WARN | TRADE_ENGINE_VISUAL_POLISH.md | no-comp-tool-citation |
| PASS | TRSB_PATHFIX_PRD.md |  |
| PASS | TRSB_TFIMPT.md |  |

Total: 38 PASS, 127 WARN, 165 PRDs scanned.
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io INF_D_00 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io INF_D_08 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript postdeps INF_D_04 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-trace | comp-trace nna_geo --direction both | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-platinum | comp-platinum reverse dashboard | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFTGT.TO-8 | comp-pipescript | comp-pipescript io INF_D_05 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | (no-TO) | comp-pipescript | comp-pipescript io INF_D_06 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1 | comp-pipescript | comp-pipescript io INF_C_00 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1 | comp-pipescript | comp-pipescript io INF_C_02 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1 | comp-pipescript | comp-pipescript io INF_C_03 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1 | comp-pipescript | comp-pipescript io INF_D_00c | FAIL |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1 | comp-pipescript | comp-pipescript io INF_D_00c.portal_leaderboard | FAIL |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1 | comp-platinum | comp-platinum reverse leaderboard | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1 | comp-blast | comp-blast gold/positions_cube | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~A | ADVI_INFTGT.TO-7 | comp-pipescript | comp-pipescript io INF_D_07 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~A | ADVI_INFTGT.TO-7 | comp-trace | comp-trace holdings --direction both | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.STAGE_NEG1 | comp-pipescript | comp-pipescript io INF_C_00 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1_5_DEEP_PROBE | comp-blast | comp-blast canonical_performance | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1_5_DEEP_PROBE | comp-pipescript | comp-pipescript deployed INF_C_00 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~D | ADVI_INFGRO.PHASE1_5_DEEP_PROBE | comp-pipescript | comp-pipescript deployed INF_D_07 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-blast | comp-blast holdings_lots | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-blast | comp-blast gold/timeseries/holdings_lots | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-pipescript | comp-pipescript io INF_D_08 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-trace | comp-trace nna_geo --direction both | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-pipescript | comp-pipescript io INF_D_00d | FAIL |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-trace | comp-trace INF_D_00d.cumulative_chart:build_nna_geo_view --direction both | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-pipescript | comp-pipescript io INF_D_00 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-platinum | comp-platinum reverse cumulative_chart | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-blast | comp-blast canonical_nna | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-blast | comp-blast INF_C_01 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-blast | comp-blast INF_C_01.canonical_nna | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-validate | comp-validate INF_D_00 --artifact /tmp/header_metrics_validate.json | FAIL |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-validate | comp-validate --help | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-validate | comp-validate --list --lane inf | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-validate | comp-validate INF_D_00c --artifact /tmp/leaderboard_validate.json --lane inf | FAIL |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-validate | comp-validate INF_09 --artifact /tmp/pa_validate.json --lane inf | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-blast | comp-blast INF_D_00d.cumulative_chart:build_geo_view | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-pipescript | comp-pipescript io INF_D_04 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-pipescript | comp-pipescript postdeps INF_D_04 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-pipescript | comp-pipescript io INF_D_00 | PASS |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-pipescript | comp-pipescript io INF_D_00b | FAIL |
| 2026-05-11 | 0.4.0_DS_ClientPlatform~C | ADVI_INFGRO.TO-000 | comp-pipescript | comp-pipescript io INF_D_00c | FAIL |
| 2026-05-11 | 0.6.1_AE_PartnerETL | ADVI_INFGRO.AE-TF-APPLY-BILLPERF | comp-blast | comp-blast INF_C_02 | PASS |
| 2026-05-11 | 0.6.1_AE_PartnerETL | ADVI_INFGRO.AE-TF-APPLY-BILLPERF | comp-blast | comp-blast INF_D_00c | PASS |
| 2026-05-11 | 0.6.1_AE_PartnerETL | ADVI_INFGRO.AE-TF-APPLY-BILLPERF | comp-pipescript | comp-pipescript overlap INF_C_02 INF_C_01 | PASS |
| 2026-05-11 | 0.6.1_AE_PartnerETL | ADVI_INFGRO.AE-TF-APPLY-BILLPERF | comp-transform | comp-transform schema-check AdvisorsTab --feature gro_decomposition | PASS |
| 2026-05-11 | 0.6.1_AE_PartnerETL | ADVI_INFGRO.AE-TF-APPLY-BILLPERF | comp-pipescript | comp-pipescript io INF_C_02 | PASS |
| 2026-05-12 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-routes | comp-routes trace getPartnerAnalytics | PASS |
| 2026-05-12 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-pipescript | comp-pipescript io partner_analytics | FAIL |
| 2026-05-12 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_04 | PASS |
| 2026-05-12 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_04.client_portal_summary | PASS |
| 2026-05-12 | 1.0.0_SA_CTO | (no-TO) | comp-iam | comp-iam service inf-portal-publisher | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform~D | BRIEF9_DE_49F_FEE_ACCOUNT_COUNTS_AND_92M_GAP | comp-pipescript | comp-pipescript io D_00 | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform~D | BRIEF9_DE_49F_FEE_ACCOUNT_COUNTS_AND_92M_GAP | comp-pipescript | comp-pipescript io D_04 | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform~D | BRIEF9_DE_49F_FEE_ACCOUNT_COUNTS_AND_92M_GAP | comp-pipescript | comp-pipescript deployed D_00 | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform~D | BRIEF9_DE_49F_FEE_ACCOUNT_COUNTS_AND_92M_GAP | comp-pipescript | comp-pipescript deployed D_04 | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_04 | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io C_03 | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript deployed INF_C_07.advisor_attribution.py | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed convert_schwab_rps_to_parquet convert_schwab_acc_to_parquet co... | FAIL |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed convert_schwab_rps_to_parquet | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed convert_schwab_acc_to_parquet | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed convert_schwab_trn_to_parquet | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed convert_schwab_uln_to_silver | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed convert_schwab_trn_to_nna_silver | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed build_schwab_bd_account_xref | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed convert_schwab_rps_to_silver | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed A_03 | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed B_01 | PASS |
| 2026-05-12 | 0.6.0_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed schwab_flows | PASS |
| 2026-05-12 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-transform | comp-transform schema-check BooksTab | FAIL |
| 2026-05-12 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-blast | comp-blast getPlatinumFirmDashboard | PASS |
| 2026-05-12 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-blast | comp-blast getPlatinumFirmMixSummary | PASS |
| 2026-05-12 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-12 | 0.4.2_RD_AdvisorIntelligence | (no-TO) | comp-transform | comp-transform fields BooksTab | FAIL |
| 2026-05-12 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-12 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-blast | comp-blast useTenantLayout | PASS |
| 2026-05-12 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-blast | comp-blast AdvisorIntelligence | PASS |
| 2026-05-12 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-05-12 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-transform | comp-transform schema-check AdvisorIntelligence | FAIL |
| 2026-05-12 | 0.1.0_DS_MarketIntelligence | (no-TO) | comp-transform | comp-transform schema-check ClientsTab | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-build | comp-build | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-05-12 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check InflectionAdvisorIntelligence | FAIL |
| 2026-05-12 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-transform | comp-transform schema-check FortyNineFinancialAdvisorIntelligence | FAIL |
| 2026-05-12 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_04.client_portal_summary.py | PASS |
| 2026-05-12 | 0.6.1_AE_PartnerETL | ADVI_INFLEC.GROUPD.chain22 | comp-pipescript | comp-pipescript deployed INF_D_00c | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | ADHC_INFCAT_ORPHAN-bugA-walkback | comp-pipescript | comp-pipescript io INF_C_07 | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | ADHC_INFCAT_ORPHAN-bugA-walkback | comp-pipescript | comp-pipescript consumers INF_C_07 | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | ADHC_INFCAT_ORPHAN-bugA-walkback | comp-iam | comp-iam service inf-unified-account-dim-daily | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | ADHC_INFCAT_ORPHAN-bugA-walkback | comp-pipescript | comp-pipescript deployed INF_C_07 | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | ADHC_INFCAT_ORPHAN-bugA-walkback | comp-pipescript | comp-pipescript deployed --help | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | ADHC_INFCAT_ORPHAN-bugA-walkback | comp-pipescript | comp-pipescript --help | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | ADHC_INFCAT_ORPHAN-bugA-walkback | comp-pipescript | comp-pipescript deployed INF_C_07 --pipeline inf-gold | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~B | ADVI_INFTGT.TO-1b | comp-pipescript | comp-pipescript io INF_D_00c | FAIL |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~B | ADVI_INFTGT.TO-1b | comp-pipescript | comp-pipescript io INF_D_00c.portal_leaderboard | FAIL |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | brief-ticker-masking-investigation | comp-pipescript | comp-pipescript deployed --pipeline inf-gold | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | brief-ticker-masking-investigation | comp-pipescript | comp-pipescript deployed INF_D_02b --pipeline inf-gold | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | brief-ticker-masking-investigation | comp-pipescript | comp-pipescript deployed INF_D_05 --pipeline inf-gold | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | brief-ticker-masking-investigation | comp-pipescript | comp-pipescript deployed INF_D_07a --pipeline inf-gold | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | brief-ticker-masking-investigation | comp-pipescript | comp-pipescript deployed D_03 --pipeline bd-gold | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | brief-ticker-masking-investigation | comp-pipescript | comp-pipescript deployed --pipeline bd-gold | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | brief-ticker-masking-investigation | comp-pipescript | comp-pipescript deployed INF_D_04 | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~B | ADVI_DWSPLT.TO-1 | comp-pipescript | comp-pipescript io convert_transactions_to_silver | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform | (no-TO) | comp-platinum | comp-platinum reverse platinum/clients/100/detail.json | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform | SMARTX_NONMDL.TO-1 | comp-iam | comp-iam service smartx-ingestion-lambda | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform | SMARTX_NONMDL.TO-1 | comp-iam | comp-iam gaps | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform | SMARTX_NONMDL.TO-1 | comp-iam | comp-iam service smartx-ingestion-lambda | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform | SMARTX_NONMDL.TO-1 | comp-iam | comp-iam gaps | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-pipescript | comp-pipescript io INF_D_02 | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-transform | comp-transform ternary-audit DistributionTab | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-pipescript | comp-pipescript deployed INF_D_02 | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-pipescript | comp-pipescript deployed INF_D_02c | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-pipescript | comp-pipescript --help | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-pipescript | comp-pipescript deployed --help | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-pipescript | comp-pipescript deployed --pipeline inf-gold INF_D_02 | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-pipescript | comp-pipescript deployed --pipeline inf-gold INF_D_02c | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.001 | comp-routes | comp-routes trace getFirmLeaderboard | PASS |
| 2026-05-13 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.002 | comp-pipescript | comp-pipescript deployed INF_D_02 --pipeline inf-gold | PASS |
| 2026-05-13 | 1.0.0_SA_CTO | (no-TO) | comp-transform | comp-transform schema-check ContinuousNnaDivergingView | FAIL |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript deployed data/orion/scripts/gold/INF_D_02.advisor_client_detail.py | PASS |
| 2026-05-13 | 0.4.0_DS_ClientPlatform~C | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_04.client_portal_summary | PASS |
| 2026-05-13 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-routes | comp-routes trace getFirmLeaderboard | PASS |
| 2026-05-14 | 0.4.0_DS_ClientPlatform~B | (no-TO) | comp-pipescript | comp-pipescript io INF_D_00c | FAIL |
| 2026-05-14 | 0.4.0_DS_ClientPlatform~A | P0_INF_D_00c_dtype_hotfix | comp-pipescript | comp-pipescript io INF_D_00c.portal_leaderboard | FAIL |
| 2026-05-14 | 0.4.0_DS_ClientPlatform~A | P0_INF_D_00c_dtype_hotfix | comp-pipescript | comp-pipescript io INF_D_00c.portal_leaderboard.py | FAIL |
| 2026-05-14 | 0.4.0_DS_ClientPlatform~A | P0_INF_D_00c_dtype_hotfix | comp-pipescript | comp-pipescript io INF_D_00c | FAIL |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_INFGRO.005 | comp-transform | comp-transform schema-check AdvisorsTab --feature gro_decomposition | PASS |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_INFGRO.005 | comp-transform | comp-transform ternary-audit AdvisorsTab | PASS |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_INFGRO.005 | comp-routes | comp-routes trace getFirmLeaderboard | PASS |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_INFGRO.005 | comp-cache | comp-cache collisions | PASS |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_INFGRO.005 | comp-pipescript | comp-pipescript deployed INF_D_00c.portal_leaderboard | PASS |
| 2026-05-14 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_00c | PASS |
| 2026-05-14 | 0.7.0_AE_CloudOps | (no-TO) | comp-pipescript | comp-pipescript deployed INF_D_00c.portal_leaderboard | PASS |
| 2026-05-14 | 0.7.0_AE_CloudOps | (no-TO) | comp-transform | comp-transform schema-check AdvisorsTab | PASS |
| 2026-05-14 | 0.7.0_AE_CloudOps | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-05-14 | 0.7.0_AE_CloudOps | YANG_ALLOC_CLEANUP | comp-pipescript | comp-pipescript io yang-generate-allocation-summary | FAIL |
| 2026-05-14 | 0.7.0_AE_CloudOps | YANG_ALLOC_CLEANUP | comp-iam | comp-iam service yang-generate-allocation-summary | PASS |
| 2026-05-14 | 0.7.0_AE_CloudOps | YANG_ALLOC_CLEANUP | comp-iam | comp-iam service yang-generate-allocation-summary | PASS |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_SHARED.001 | comp-transform | comp-transform schema-check TenantLayoutConfig | FAIL |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_SHARED.001 | comp-blast | comp-blast TenantLayoutConfig | PASS |
| 2026-05-14 | 0.4.0_DS_ClientPlatform~D | ADVI_INFINC.001 | comp-pipescript | comp-pipescript io INF_B_00 | PASS |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_SHARED.006 | comp-cache | comp-cache collisions | PASS |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | ADVI_SHARED.006 | comp-routes | comp-routes trace advisor-intelligence | PASS |
| 2026-05-14 | 0.4.0_DT_ClientPlatform | (no-TO) | comp-cache | comp-cache collisions | PASS |
| 2026-05-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_SHARED.007 | comp-routes | comp-routes trace advisor-intelligence | PASS |
| 2026-05-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_SHARED.007 | comp-routes | comp-routes behaviors | PASS |
| 2026-05-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_SHARED.007 | comp-routes | comp-routes trace getClientsTab | PASS |
| 2026-05-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_SHARED.007 | comp-routes | comp-routes trace /api/scoped/advisor-intelligence | PASS |
| 2026-05-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_SHARED.007 | comp-pipescript | comp-pipescript io shared-auth-validator-edge | FAIL |

| 0.1.0_DE_MarketIntelligence | 2026-05-14 | comp-tooltip drift | N/A (no tooltip work) | P1 circular import fix session |
| 2026-05-14 | 0.1.0_DE_MarketIntelligence | (no-TO) | comp-routes | comp-routes trace getPlatinumPartnerAnalytics | PASS |
| 2026-05-14 | 0.1.0_DE_MarketIntelligence | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-05-14 | 0.1.0_DE_MarketIntelligence | (no-TO) | comp-routes | comp-routes behaviors | PASS |
| 2026-05-14 | 0.4.0_DE_ClientPlatform | P1_5surface_phase_1_4_fee_cascade_wiring | comp-routes | comp-routes trace getHeaderMetrics | PASS |
| 2026-05-14 | 0.4.0_DS_ClientPlatform~C | P0_156k_bronze_vs_gold_5_14_variance | comp-pipescript | comp-pipescript io INF_D_04.client_portal_summary | PASS |
| 2026-05-14 | 0.4.0_DS_ClientPlatform~C | P0_156k_bronze_vs_gold_5_14_variance | comp-blast | comp-blast INF_D_04.client_portal_summary | PASS |
| 2026-05-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.NNN.rd-nna-l0-firm-wide-display-bug | comp-validate | comp-validate --help | PASS |
| 2026-05-14 | 0.4.2_RD_AdvisorIntelligence | ADVI_INFFIN.NNN.rd-nna-l0-firm-wide-display-bug | comp-pipescript | comp-pipescript deployed data/orion/scripts/gold/INF_D_02.advisor_client_detail.py | PASS |
| 2026-05-14 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed inf-gold-trigger | PASS |
| 2026-05-14 | 0.6.1_AE_PartnerETL | (no-TO) | comp-iam | comp-iam service inf-gold-trigger | PASS |
| 2026-05-14 | 0.6.1_AE_PartnerETL | (no-TO) | comp-blast | comp-blast inf-gold-trigger | PASS |
| 2026-05-14 | 0.6.1_AE_PartnerETL | (no-TO) | comp-validate | comp-validate gold-nan | PASS |
| 2026-05-14 | 0.6.1_AE_PartnerETL | (no-TO) | comp-validate | comp-validate gold-nan --strict | FAIL |
| 2026-05-14 | 0.6.1_AE_PartnerETL | (no-TO) | comp-pipescript | comp-pipescript deployed data/orion/scripts/bronze/pull_eclipse_portfolios.py | PASS |
