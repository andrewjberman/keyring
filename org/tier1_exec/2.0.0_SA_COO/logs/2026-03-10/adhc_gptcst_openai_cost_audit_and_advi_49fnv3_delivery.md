# COO Session Log — ADHC_GPTCST Cost Audit + ADVI_49FNV3 Delivery Review
**Agent:** 2.0.0_SA_COO
**Date:** 2026-03-10
**Start Time:** 09:00
**End Time:** 19:30

---

## Objective

Two parallel workstreams this session:
1. Complete ADVI_49FNV3 Phase 1a delivery audit and drive outstanding task orders to completion
2. Launch ADHC_GPTCST (GPT Cost Audit and Optimization) — a new cross-cutting project
   Andrew registered after OpenAI costs became a concern

---

## Work Completed

### 1. ADVI_49FNV3 — Delivery Audit and F2 Redesign

#### 1a. Downstream check on 2026-03-09 work

All four first-order agents had active logs from 2026-03-09:

| Agent | Status | Key Deliverable |
|-------|--------|----------------|
| 0.4.0_DE | COMPLETE | F3-fix (TDZ crash) + F3b (continuous NNA drill parity) — portal DEV 9c1881a + 3367cd8 |
| 0.4.0_DS | COMPLETE | F5-fix (ytd key added to both leaderboard publishers) — CLOUD edf8ac06 |
| 0.4.2_RD | COMPLETE | F2/F4/F6/F7/N1-N2 — portal DEV 594c3f6 |
| 0.4.0_DT | COMPLETE | NNAVAR scripts 05/05b deployed to S3 (no rebuild triggered) |

All 14 ADVI_49FNV3 Phase 1a task orders confirmed complete. Pending: DT push of
portal DEV commits + bd-pipeline Lambda deploy (F5 ytd keys).

#### 1b. ADVI_49FNV3-003 — F2 Projection Visualization Thread

CTO issued analysis doc and task order requesting a Pattern 0 alignment thread on
F2 projection flaws and GRO chart redesign. Andrew reviewed the RD's implementation
and identified 4 flaws: AUA projection 0/0 regression, GRO chart unintelligible,
tooltip "(add)" format, and GRO tooltip _proj leakage.

Ran thread ADVI_49FNV3-003 (CTO + DE + RD, 8 turns, gpt-5.2):
- Converged on full contract: full-history prior lookup for AUA, GRO hybrid chart
  (stacked bars + total line), datum-driven tooltip, 3 GRO hero tiles
- Issued RD task order ADVI_49FNV3.003.f2-projection-gro-redesign.md

RD completed the task order (portal DEV 469767e). Andrew reviewed and identified that
projections still only appear in Annual view, not Monthly/Quarterly.

#### 1c. F2 Projection Root Cause + Redesign Decision

COO investigation: discovered the ghost bar model silently produces 0 when projected
value is below actual (max(0,...) guard). For Monthly/Quarterly, AUA may decline
period-over-period; Annual is almost always positive YoY. This is why Annual shows
ghost but Monthly/Quarterly do not.

Andrew's decision: replace ghost bars entirely with a **dashed horizontal line** at
the projected value — green if above actual, red if below. Works in both directions.

Issued RD task order ADVI_49FNV3.003b.f2-projection-line-redesign.md.

RD completed (status: complete per task order).

#### 1d. Stale S3 artifact deleted

Discovered `s3://opal-data-portal-v2/api/public/advisor-intelligence/timeseries_chart.json`
was a January 16 relic not served by any live routing path. Deleted.
Three additional stale files remain at that prefix (same Jan 16 batch) — awaiting
Andrew authorization to purge the full `api/public/advisor-intelligence/` prefix.

#### 1e. BD pipeline staleness investigation

`opal-data-bd/gold/timeseries_chart.json` last data date was 2026-03-02 despite
daily pipeline schedule. Issued task order ADVI_49FNV3.004 to 0.6.0_AE_PartnerETL
to investigate root cause. Task order marked complete by AE (same session).

---

### 2. ADHC_GPTCST — GPT Cost Audit and Optimization

#### 2a. Project registration

Andrew registered new macro code ADHC (Ad-hoc / Cross-Cutting) and project
ADHC_GPTCST (GPT Cost Audit and Optimization). Three-phase scope: Audit → Optimize
→ Integrate into morning infrastructure report.

#### 2b. Thread ADHC_GPTCST-001 — Caller Inventory

Ran Pattern 2 investigation thread between 0.5.0_AE_OpalETL and 0.7.0_AE_CloudOps
(6 turns, gpt-5.2, tools enabled). Key findings:

**Complete caller inventory:**

| Caller | Model | Trigger | Optimization |
|--------|-------|---------|-------------|
| news-trending-analysis | gpt-4o + embeddings + gpt-4o-mini | Daily 9:30 AM ET | Downgrade keyword validation gpt-4o → gpt-4o-mini |
| opal-news-layer3-curation | gpt-4o / gpt-4o-mini | Chained from above | Reduce MAX_TOKENS |
| semantic-news-layer3-curation | gpt-4o | 2x daily | Add idempotency guard |
| keyword-intelligence-generator | gpt-4o-mini + web search | Chained from above | Double-trigger risk |
| opal-trending-image-generator | gpt-4o-mini | After Layer 3 | Replace with deterministic |
| market-update-generator | gpt-4-turbo-preview (deprecated) | API-driven | Migrate + cache |
| opal-infrastructure-monitor | gpt-4o-mini | Weekday 9 AM ET | Add OPENAI_USAGE line |
| SmartX EC2 supervisor | gpt-4o up to 15 iterations | EC2 cron | Downgrade + fix secret name |

**Critical finding:** `infrastructure_monitor` already has `openai_cost_tracker.py`
but it is not imported, function names are mismatched vs lambda-source-map.json, and
it uses an unreliable `"api.openai.com"` log heuristic rather than token-accurate parsing.

Issued two task orders:
- ADHC_GPTCST.001 to 0.5.0_AE_OpalETL — Lambda optimizations + OPENAI_USAGE log lines
- ADHC_GPTCST.001 to 0.7.0_AE_CloudOps — Phase 3 morning report integration + SmartX fixes

Both completed same session. Status:
- 0.5.0_AE_OpalETL: news-v2.5.0 deployed (4 Lambdas with OPENAI_USAGE lines, model
  downgrades, idempotency guard). market-update-generator + opal-trending-image-generator
  blocked (pre-Terraform) — escalated to Andrew.
- 0.7.0_AE_CloudOps: code complete (commit 1f6bc00e) but opal-infrastructure-monitor
  has no Terraform resource — cannot deploy. SmartX EC2 host unknown (ec2_host: null).

#### 2c. Actual spend analysis from billing CSVs

Andrew provided cost_2026-02-08_2026-03-10.csv and completions_usage_2026-02-08_2026-03-10.csv.

**$59.61 total over 31 days.**

| Model | Requests | Tokens | Cost |
|-------|----------|--------|------|
| gpt-5.2-2025-12-11 | 86 | 9.2M in / 113K out | ~$13-15 (thread orchestrator) |
| gpt-4o-2024-08-06 | 178 | 2.4M | ~$7 (Lambda callers) |
| gpt-5-nano-2025-08-07 | 21 | 303K | ~$3 |
| gpt-4o-mini-2024-07-18 | 5,096 | 5.6M | ~$1.80 |

Key finding: the largest single cost driver is **keyword-intelligence-generator running
2x daily on schedule**, doing 2 web searches per keyword × 20 keywords = 40 web searches
per run, 80/day. Key `key_nK9bCScunQ73ryVF` shows 3,553 requests over 29 days at
~122/day — consistent daily automation. This started Feb 23 (574 reqs that day —
likely initial activation).

Thread orchestrator spend (~$15) is from 6 days of thread activity (Mar 3–10).
The bulk of the $59 is from automated Lambda web search activity, not threads.

#### 2d. Keyword intelligence architecture investigation

Andrew observed: modal loads take 10-15 seconds on first click despite pre-computation
running 2x daily. Subsequent clicks in same session come faster.

COO investigation revealed a **cache miss problem**:
1. Pre-computation writes DynamoDB with SK = today's date (UTC)
2. Live path in portal_data_proxy does cache lookup SK = today's date
3. Pre-computation runs at ~9:50 AM EDT — 20 minutes AFTER market open (9:30 AM ET)
4. Portal users at 9:30 AM see cache MISS → full 7-day DynamoDB scan + GPT call
5. **Critical bug: live path never writes back to DynamoDB** — every cache miss recomputes
   from scratch, even if the same keyword was computed 30 seconds earlier

"Second click feels faster" = Lambda container warmup, not cache hit.

Additionally: live path has NO web search enrichment (only pre-computation does).
Result: users are effectively always computing live, paying for pre-computation that
goes unused.

Andrew's conclusion: no need to eliminate pre-computation — keep top 10 as a dataset
that may be useful downstream — but fix the system so the cache actually works.

#### 2e. ADHC_GPTCST-002 — Cache Fix

Issued task order ADHC_GPTCST.002 to 0.5.0_AE_OpalETL. Three changes:
1. Write-back to DynamoDB after live computation in portal_data_proxy
2. MAX_KEYWORDS 20 → 10 (halve web search cost, keep dataset)
3. EventBridge fallback schedule updated to 8AM/8PM UTC (before US market open)

Completed same session. Delivered as news-v2.6.0 + market-overview-v1.6.0.
Bonus: portal_data_proxy migrated from legacy deploy.sh to S3-backed Terraform
(was the last Lambda using lifecycle.ignore_changes + placeholder.zip).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| F2 ghost bars → dashed line | Ghost bars can't show downward projections (max(0,...) guard). Dashed line works bidirectionally. Green/red by direction. Andrew's choice. |
| Keep keyword intelligence pre-computation | Andrew wants the dataset for potential downstream use. Reduce to 10, fix the cache, keep the pipeline. |
| Thread model not the primary cost driver | gpt-5.2 threads cost ~$15 over 31 days. Main driver is automated web search. No model changes needed for threads. |
| Delete api/public/advisor-intelligence/timeseries_chart.json | Stale Jan 16 relic, no routing path reads from it. COO-executed directly. |

---

## Files Modified (COO-authored)

| File | Action | Committed |
|------|--------|-----------|
| `org/threads/staging/run-ADVI_49FNV3-003-f2-projection-gro-redesign.sh` | Created + ran | Local |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_49FNV3.003.f2-projection-gro-redesign.md` | Issued | Local |
| `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_49FNV3.003b.f2-projection-line-redesign.md` | Issued | Local |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_49FNV3.004.gold-pipeline-staleness-investigation.md` | Issued | Local |
| `org/tier1_exec/2.0.0_SA_COO/task_orders/ADVI_49FNV3.003.f2-visualization-thread.md` | Marked complete | Local |
| `org/threads/staging/run-ADHC_GPTCST-001-openai-cost-audit-inventory.sh` | Created + ran | Local |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/ADHC_GPTCST.001.openai-caller-optimization.md` | Issued | Local |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADHC_GPTCST.001.openai-cost-tracking-phase3.md` | Issued | Local |
| `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/ADHC_GPTCST.002.keyword-intelligence-cache-fix.md` | Issued | Local |

---

## Blockers / Open Items

| Item | Owner | Priority |
|------|-------|----------|
| `opal-infrastructure-monitor` has no Terraform resource — Phase 3 cost tracking cannot deploy | [0.7.0_AE_CloudOps] create TF module | Medium |
| SmartX EC2 supervisor fix cannot deploy — ec2_host null in EC2_MANIFEST.json | [0.7.0_AE_CloudOps] start instance + sync-ec2-manifest | Medium |
| `market-update-generator` + `opal-trending-image-generator` pre-Terraform | [Andrew] decide Terraform home | Low |
| 3 remaining stale files at `api/public/advisor-intelligence/` (Jan 16 batch) | [Andrew] authorize purge | Low |

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

ADVI_49FNV3 Phase 1a: all 14 task orders complete. F2 projection redesign complete
(dashed line, green/red). F3/F3b NNA drill fixes live. F5 ytd keys deployed. GRO
hybrid chart, tooltips, hero metrics live. Pending: DT push of accumulated portal DEV
commits and bd-pipeline Lambda deploy.

ADHC_GPTCST Phase 1+2 substantially complete: full caller inventory produced, Lambda
optimizations deployed (news-v2.5.0), keyword intelligence cache fixed (news-v2.6.0 +
market-overview-v1.6.0), web search cost halved. Two deployment blockers remain for
Phase 3 (infrastructure-monitor Terraform, SmartX EC2 host).

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push portal DEV** — accumulated commits:
   portal DEV `594c3f6` (F2/F4/N1-N2), `9c1881a` (F3-fix), `3367cd8` (F3b),
   plus RD's 003b dashed-line commit. DE must review 003b before DT pushes.

2. **[0.4.0_DT_ClientPlatform] Deploy bd-pipeline** — F5 ytd Lambda changes
   per `docs/briefs/devops-brief-49fnv3-f5-qtd-publisher-fix.md`. Then
   `[0.4.0_DE_ClientPlatform]` wires `periodToChartWindow` for qtd/ytd.

3. **[0.4.0_DT_ClientPlatform] Trigger gold rebuild** — NNAVAR JNL/sweep fix
   (scripts 05/05b, already on S3) + AUAVAR BKF fix (script 02). One rebuild
   covers both. Authorized per NNAVAR decision log 2026-03-09.

4. **[0.7.0_AE_CloudOps] Create Terraform module for opal-infrastructure-monitor**
   — prerequisite for Phase 3 morning report cost section going live.

5. **[0.6.0_AE_PartnerETL] BD pipeline staleness** — investigate and fix
   daily pipeline not running past 2026-03-02 (ADVI_49FNV3.004).

**Do NOT:**
- Push portal DEV before DE reviews the 003b dashed-line commit
- Trigger gold rebuild before ADVI_49FNV3 portal work reaches PROD
- Use `aws lambda update-function-code` for infrastructure-monitor or any other Lambda
