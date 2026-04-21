# 1.0.0_SA_CTO — Session 36 continuation: 5-item decision walkthrough

**Date:** 2026-04-21 (Tue, PM)
**Scope:** Andrew 1-by-1 decision walkthrough on the 5 open items surfaced in the COO/CTO "What's Open" status table. All 5 decided; COO inherits TO authoring / adjustment / cancellation from this log.
**Continuity from:** session 36 mid-cycle dashboard sync (`964a9819`).

---

## 1. AUA active-filter brief — DECISION: Cohort A D_04 summary footnote only

**Decision:** KILL the multi-signal active-account detector proposal entirely. REPLACE with a tiny D_04 summary-footnote TO scoped to Cohort A only.

- **Cohort A** = 599 accts / $44.7M dropped between `silver/allocations[d]` and `gold/canonical/holdings[d]`. These are accounts BD sees but we drop during canonical normalization.
- **Not Cohort B** = 166 accts / $41M in holdings_lots but BD-excluded-by-account-type (SLATs/DAFs/HSAs/PCRAs). Cohort B is the "we don't track that" class from the 2026-04-20 decision — stays untracked, no D_04 inclusion.
- **D_04 summary artifact scope (headline info only):**
  - Count of accounts
  - Total AUA (sum of `cash_market_value` + `amv` from silver)
  - Client count (derived via `household` / `rep_id` grouping)
  - State distribution (joinable via `silver/accounts` or dimensional table — client_state lives on client, not account)
  - Top-N named accounts (e.g., top 20 by AUA for portal footnote display)
- **Explicit NON-scope:** NO changes to A_03, B_00, or C_01 filter logic. NO new `gold/canonical/account_activity/` artifact. NO multi-signal detector. Summary info only, for portal footnote consumption.
- **Kill record:** `docs/briefs/aua_active_account_filter_redesign.md` deleted this commit. Research preserved in session log `aua_active_filter_investigation_and_brief.md` (2026-04-20 PM).

**COO action:** Author new D_04 summary-footnote TO (small — likely <4h DS + DE work). Assign DS (D_04 emit) + DE (portal footnote display).

---

## 2. Lifetime Activity chart vs Leaderboard methodology — DECISION: Per-day gating canonical

**Decision:** All FLOW attribution is time-windowed per-day tagging-gated. AUA (stock) stays current-snapshot. Leaderboard cuts over to match chart.

- **Canonical rule for all flow attribution (NNA, leaderboard, chart):** A flow on account `A` on day `D` is attributed to advisor `V` iff `V` was tagged to `A` on day `D`. No backfill attribution for pre-tag flows.
- **Chart (D_02):** `048af6a3` HOLDS — already implements per-day gate correctly.
- **Leaderboard (D_00c L764-779):** CUTS OVER from current-snapshot × full-window rule to per-day tagging gate. DS~D authors the cutover TO. Validates Travis Penfield Q2 leaderboard NNA converges to `-$6.845M` (chart value) from `-$6.311M` (current pre-cutover).
- **AUA (stock):** Unchanged — current-snapshot remains for role_breakdown.aua. Internally inconsistent with NNA by design (AUA is "what do you manage today", NNA is "what flows did you cause during your tagged window").
- **FE:** DE removes any prior caveat about chart/leaderboard divergence once leaderboard matches chart (was staged from Option A contingency path).
- **Reasoning:** Prevents comp gaming (advisor onboarding mid-quarter can't claim pre-tag flows). Defends the historical-truth semantic on "Lifetime Activity" chart title. Time-windowing is the right attribution model for flows regardless of how it treats book churn.

**KPI 50bps sentinel (STAUDT.KPI):** CANCELLED explicitly. Andrew: "the sentinel actually doesn't matter, it's irrelevant in general, should not be memorialized as a gate or something concrete." Kill the framing everywhere it appears. `ADVI_STAUDT.KPI.ds-engine-accuracy-50bps-sentinel.md` TO status → CANCELLED.

**COO action:**
- Author D_00c leaderboard per-day-gate cutover TO (DS~D owns D_00c).
- Author DE caveat-removal TO (removes planned chart/leaderboard divergence UX note).
- Cancel `ADVI_STAUDT.KPI.ds-engine-accuracy-50bps-sentinel.md` — TO status flip to complete w/ CANCELLED comment citing this decision.

**Parked (standing-backlog, not urgent):** A separate advisor-level flow-attribution reconciliation sentinel (chart ↔ leaderboard per-advisor diff) may eventually be useful, but is NOT a dependency of this decision and is NOT a gate.

---

## 3. TRSB §8 Q2 + Q4 (+ #5 SES folded in) — DECISION: Joint-AE Phase 0 discovery

**Decision:** W2 rescoped from binary Q2/Q4 authorization to a **joint 0.5.0_AE_OpalETL + 0.7.0_AE_CloudOps Phase 0 discovery**. AEs walk the 11-Lambda surface, inventory what's there, and return with an informed W2 proposal. SES production-access prep is folded into the same discovery segment (same operational cluster — trade pipeline depends on SES moving sandbox→prod for client notifications).

**Joint-AE Phase 0 scope:**
- **11-Lambda surface walk:** fixtures, invocation history (CloudWatch 30d), code state (imported from dormant placeholder vs active external deploy), existing test harness (if any).
- **Dormancy matrix:** ACTIVE / DORMANT tag per Lambda + API-GW-method-level invocation counts. Replaces the pre-authorized recon-quartet-only probe.
- **Smoke-test fixture:** Check `tests/`, partner docs, prod submission samples for existing golden-path trade JSON. Recommend build-vs-skip based on dormancy outcome.
- **SES sandbox→prod readiness:**
  - Use-case description draft (1-2 paragraphs, Console-form-ready)
  - Daily volume estimate (transactional only, per-trade-notification)
  - Compliance attestation language (bounce rate, complaint rate, unsubscribe handling)
  - DKIM/SPF verification status per identity
- **Deliverable:** Single combined report (a) fixture/dormancy matrix, (b) smoke-test build-vs-skip recommendation with evidence, (c) Console-ready SES request packet Andrew can copy-paste into AWS Console.
- **SLA:** 2 days unchanged. W2 informed proposal + SES packet drop as one handoff.

**Why joint AE:** Neither 0.5.0 (OpalETL) nor 0.7.0 (CloudOps) alone has full context — 0.7 owns infra (Terraform, IAM, API GW); 0.5 owns the broader ETL pattern library (SES identity verification came up during partner-etl work). Andrew: "hard to say what is best approach without a better understanding of what is there."

**COO action:** Adjust `TRSB_TFIMPT.W2.ae-lambda-code-reclamation-11-functions.md` TO: replace single-AE scope with joint 0.5.0_AE + 0.7.0_AE Phase 0 discovery + SES packet. Un-gate from binary Q2/Q4 authorization. Owners field updates to both serials.

---

## 4. ADHC_DESIGN orphan TOs — DECISION: Close at 28/32 effective

**Decision:** CANCEL 4 orphan TOs. CLOSE `ADHC_DESIGN` at 28/32 (87.5% effective). Do NOT spawn `0.2.2_RD_Attribution` or `0.2.4_RD_Valuation`.

- **Orphans to cancel:**
  - `ADHC_DESIGN.001.rd-attribution-*.md` (0.2.2_RD_Attribution)
  - `ADHC_DESIGN.015.rd-attribution-*.md` (0.2.2_RD_Attribution)
  - `ADHC_DESIGN.024.rd-attribution-*.md` (0.2.2_RD_Attribution)
  - `ADHC_DESIGN.007.rd-valuation-*.md` (0.2.4_RD_Valuation)
  (Exact filenames in 0.2.2 / 0.2.4 task_orders directories — COO resolves.)
- **Reasoning:** Attribution + Valuation are legacy low-traffic ADVI sibling surfaces. No product driver. ADHC_DESIGN is quality-of-life normalization, not mission-critical. Standing up two RD agents for cosmetic refactors on pages with no investment isn't justified.

**COO action: 3-step atomic closure** per `org/XXX.md` Closure Discipline rule:
1. **TO status flips:** All 4 orphan TOs → status=complete with `<!-- CANCELLED 2026-04-21 — surface not under active investment; see org/tier1_exec/1.0.0_SA_CTO/logs/2026-04-21/session36_five_item_decisions.md -->`.
2. **JSON status flip:** `org/projects/ADHC_DESIGN.json` → `"status": "complete"` + `"completed": "2026-04-21"` + phase rewrite as closure summary + blocking → "None — closed at 28/32 effective; 4 RD orphans cancelled per Andrew directive".
3. **REGISTRY move:** Delete row from Active Projects; insert at TOP of Completed / Archived table with Completed date + closure notes.
4. **PRD status note:** `docs/architecture/PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md` — add top-of-file `Status: COMPLETE — 2026-04-21 (28/32 effective; Attribution + Valuation sub-pages deferred, no product driver)`.

All 4 steps in one commit (atomicity requirement).

---

## 5. SES production-access request — FOLDED INTO #3

Per Andrew directive: "This needs to get rolled into #3 for 0.5.0_AE and 0.7.0_AE, it's the same segment/relevant." See §3 above. SES packet deliverable is part of joint-AE Phase 0.

---

## 6. Inbox handling during walkthrough

**0.6.0_AE_PartnerETL** MCP received 2026-04-21 mid-walkthrough: Schwab TRN NNA Layers A + B shipped (`bea387a9`) — 496/494 silver partitions, classifier reproduces PoC baseline. 4/6 Jul-Dec 2024 months outside strict ±15% band (PDF parity); AE notes classifier is strictly-additive over BD silver (gap is missing transactions, not misclassification). AE ask: is ±15% a hard gate for DS Phase 6 dispatch?

**Status:** Separate decision, NOT one of the 5 items. Ack'd receipt to user; deferred until user flags for resolution. Park for a future decision pass — AE has queued the DS handoff note for the next startup, no immediate action required.

---

## 7. Commits this session

| File | Action |
|---|---|
| `docs/briefs/aua_active_account_filter_redesign.md` | DELETED — multi-signal brief killed per Andrew |
| `org/projects/ADVI_STAUDT.json` | Phase + blocking rewritten: brief killed, KPI cancelled, chart methodology decided, Cohort A D_04 scope added |
| `org/projects/TRSB_TFIMPT.json` | Phase + blocking + waves rewritten: W2 joint-AE Phase 0 discovery + SES folded in |
| `org/tier1_exec/1.0.0_SA_CTO/prompt.md` | Dashboard: ADHC_DESIGN closing, TRSB W2 rescope, STAUDT decisions landed |
| `org/tier1_exec/1.0.0_SA_CTO/logs/2026-04-21/session36_five_item_decisions.md` | this file |

Per Andrew: no MCP to worker agents. COO (LIVE) picks up TO authoring / adjustment / cancellation from this session log on their side.

---

## 8. Compiler Tools

None this session — purely decision-capture + org doc updates. No script/component changes.

---

## 9. COO TO handoff checklist (for COO to execute)

1. **Author** `ADVI_STAUDT.COHORT-A.ds-d04-summary-footnote.md` — 599 accts headline summary emitted as D_04 artifact for portal footnote; NO gold-runner filter changes.
2. **Author** `ADVI_STAUDT.CHART-METH.ds-d00c-leaderboard-per-day-gate-cutover.md` — DS~D cuts over D_00c L764-779 from current-snapshot × full-window to per-day tagging gate.
3. **Author** `ADVI_STAUDT.CHART-METH-FE.de-caveat-removal.md` — DE removes any planned chart/leaderboard divergence UX caveat.
4. **Cancel** `ADVI_STAUDT.KPI.ds-engine-accuracy-50bps-sentinel.md` — status flip to complete w/ CANCELLED comment citing this log.
5. **Adjust** `TRSB_TFIMPT.W2.ae-lambda-code-reclamation-11-functions.md` — swap binary Q2/Q4 gate → joint 0.5.0_AE + 0.7.0_AE Phase 0 discovery + SES packet; update owners.
6. **Close ADHC_DESIGN** 3-step atomic: 4 orphan TO CANCELLED flips + JSON status complete + REGISTRY move + PRD status note — all in one commit.
