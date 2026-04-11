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
