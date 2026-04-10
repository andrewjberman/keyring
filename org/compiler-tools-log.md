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
