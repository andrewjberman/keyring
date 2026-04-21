# COO Session 38 — Andrew 5-item Decision Execution

**Date:** 2026-04-21 (Tue, PM ET)
**Agent:** 2.0.0_SA_COO
**Scope:** Execute the 6 TO actions dispatched by CTO via MCP 20260421T154015Z (+ follow-up 20260421T155431Z confirming COHORT-A interpretation). Actions originate from Andrew's 5-item decision walkthrough earlier this PM — CTO session log `org/tier1_exec/1.0.0_SA_CTO/logs/2026-04-21/session36_five_item_decisions.md`, commit `0a37d545`. No worker-agent MCPs per Andrew; actions roll into COO-authored commits only.

---

## Commits

| Commit | Scope |
|--------|-------|
| `1fd28809` (Commit A) | 3 new STAUDT TOs + KPI cancel + TRSB.W2 rescope |
| This commit (Commit B) | ADHC_DESIGN 3-step atomic closure + session log |

---

## 6 TO Actions Executed

### 1. AUTHOR `ADVI_STAUDT.COHORT-A.ds-d04-summary-footnote.md` (Commit A)

Path: `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.COHORT-A.ds-d04-summary-footnote.md`

- DS-primary TO with DE portal-footnote display as inline sub-deliverable (confirmed by CTO 20260421T155431Z — "splitting is wasted bureaucracy since the shape is well-pinned").
- Emits Cohort A headline summary (599 accts / $44.7M dropped silver→canonical) as D_04 artifact for portal transparency footnote.
- Fields: count, AUA, client count, state distribution, top-N named.
- Scope-locked: NO gold-runner filter changes, NO re-inclusion into canonical, NO multi-signal detector.
- Cohort B (166 accts / $41M BD-excluded: SLATs/DAFs/HSAs/PCRAs) explicitly OUT of scope — stays untracked per 2026-04-20 "we don't track that" decision.
- Status: `staged`. SLA ~4h combined (DS ~2-3h + DE ~1h).
- Replaces the killed multi-signal brief (`docs/briefs/aua_active_account_filter_redesign.md` DELETED in `0a37d545`).

### 2. AUTHOR `ADVI_STAUDT.CHART-ALIGN.ds-d00c-leaderboard-per-day-gate-cutover.md` (Commit A)

Path: `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.CHART-ALIGN.ds-d00c-leaderboard-per-day-gate-cutover.md`

- Originally drafted as `CHART-METH`. **Renamed to `CHART-ALIGN` per Andrew directive** mid-authoring — "METH" abbreviation not acceptable. `CHART-ALIGN` is semantically correct (aligns chart and leaderboard methodologies). Applied consistently across CHART-ALIGN + CHART-ALIGN-FE + cross-references.
- Cuts `D_00c.portal_leaderboard.py` L764-779 attribution loop from current-snapshot × full-window to per-day tagging gate (matching chart D_02 `048af6a3` pattern).
- Acceptance: Travis Penfield Q2 leaderboard NNA converges `-$6.311M` → `-$6.845M ±$0.05M` (chart value).
- Non-scope locked: role_breakdown.aua stays current-snapshot; D_02 chart HOLDS (already correct); no upstream refactor.
- Status: `staged`. SLA ~4h.

### 3. AUTHOR `ADVI_STAUDT.CHART-ALIGN-FE.de-caveat-removal.md` (Commit A)

Path: `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_STAUDT.CHART-ALIGN-FE.de-caveat-removal.md`

- DE removes planned chart↔leaderboard divergence UX caveat once leaderboard matches chart.
- **Hard dependency on DS CHART-ALIGN artifact-ready** — DE cannot remove caveat before data convergence (users would see inconsistent numbers without explanation).
- AUA↔NNA note preserved by design (internal inconsistency is intentional per §2 decision).
- Status: `staged`. SLA ~1h.

### 4. CANCEL `ADVI_STAUDT.KPI.ds-engine-accuracy-50bps-sentinel.md` (Commit A)

Path: same. Status flip `pending` → `complete` with CANCELLED comment citing CTO session log §2 + Andrew explicit: "the sentinel actually doesn't matter, it's irrelevant in general, should not be memorialized as a gate or something concrete." Kill the 50bps framing.

- Any partial ~C Phase 0 work preserved for reference; NOT promoted to config.
- Parked standing backlog (NOT a TO): advisor-level flow-attribution reconciliation sentinel (chart ↔ leaderboard per-advisor diff) may eventually be useful but not a dependency or gate.

### 5. ADJUST `TRSB_TFIMPT.W2.ae-lambda-code-reclamation-11-functions.md` (Commit A)

Path: same. Rescoped from single-AE binary Q2/Q4 gate to joint 0.5.0_AE + 0.7.0_AE Phase 0 discovery. SES sandbox→prod packet (item #5 in Andrew's 5-item list) folded in per §3 decision.

Key changes:
- `<issued_to>` kept as `0.7.0_AE_CloudOps` but `<co_owner>0.5.0_AE_OpalETL</co_owner>` added (joint Phase 0).
- `<rescope_2026-04-21>` block added documenting the old scope and new scope.
- `<deliverables>` restructured: Phase 0 joint discovery (11-Lambda dormancy matrix + API GW triangulation + fixture probe + SES packet research) → AE+CTO signoff → Phase 1 reclaim-and-deploy per option-disposition plan.
- New deliverable: Console-ready SES packet at `infra/aws/ses/trade-pipeline-prod-access-request.md` covering use-case, volume estimate, compliance language (bounce/complaint/unsubscribe), DKIM/SPF status, identity list.
- Un-gated from Andrew §8 Q2+Q4 wait. COO flips staged→pending on joint AE ACK.
- SLA unchanged at 2 days.

### 6. CLOSE `ADHC_DESIGN` — 3-step atomic (Commit B, this commit)

Per XXX.md Closure Discipline rule:

**Step 1 — 4 orphan TO flips:**
- `org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.001.rd-color-migration-and-qa.md` → `<status>complete</status>` + CANCELLED comment
- `org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.015.rd-overflow-containment.md` → same
- `org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.024.rd-mobile-readiness-audit.md` → same
- `org/tier3_junior/0.2.4_RD_Valuation/task_orders/ADHC_DESIGN.007.rd-color-migration-and-qa.md` → same

All 4 were `staged`-never-dispatched (agents never spawned). Flipped straight to `complete` with CANCELLED comment citing CTO session log §4 + Andrew rationale: "legacy low-traffic ADVI sibling surfaces. No product driver. Standing up two RD agents for cosmetic refactors on pages with no investment isn't justified."

**Step 2 — JSON status flip:**
`org/projects/ADHC_DESIGN.json` → `status: complete`, `completed: 2026-04-21`, `phase` rewritten as closure summary, `blocking: None`.

**Step 3 — REGISTRY row move:**
`org/projects/REGISTRY.md` — Active Projects row deleted; new row inserted at TOP of Completed / Archived table with completed date 2026-04-21 + closure notes citing 28/32 effective + 4 cancelled TOs + rationale.

**Step 4 — PRD status note:**
`docs/architecture/PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md` — `**Status:** Phase 0 complete. COO decomposition pending.` → `**Status:** COMPLETE — 2026-04-21 (28/32 effective; Attribution + Valuation sub-pages deferred, no product driver).`

All 4 sub-steps ship in ONE commit per atomic-closure discipline.

---

## Decisions Made

1. **CHART-METH rename → CHART-ALIGN.** Andrew mid-authoring directive: no "METH" abbreviation. Rename applied before any commit to avoid artifact churn. `CHART-ALIGN` captures the semantic (chart/leaderboard methodology alignment) and reads cleanly.

2. **COHORT-A = single TO with DE sub-deliverable inline.** CTO confirmed 20260421T155431Z — splitting into DS + DE would be wasted bureaucracy given well-pinned shape. Single TO with DS-primary + DE portal-footnote display captured as scoped sub-deliverable.

3. **TRSB.W2 un-gated from Andrew answers.** Old wording (`<open_questions_gating_pending>` with Q2+Q4) replaced with `<rescope_2026-04-21>` block documenting the pivot to joint-AE evidence-based Phase 0. COO flips staged→pending on joint AE engagement ACK; no Andrew wait.

4. **ADHC_DESIGN atomic closure shipped as separate commit (B) from action-authoring (A).** Closure Discipline requires atomicity of the 4 closure sub-steps (TOs + JSON + REGISTRY + PRD); scoping Commit A to the 5 non-closure actions keeps each commit reviewable.

---

## Files Modified

**Commit A (`1fd28809`):**
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.COHORT-A.ds-d04-summary-footnote.md` (NEW)
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.CHART-ALIGN.ds-d00c-leaderboard-per-day-gate-cutover.md` (NEW)
- `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_STAUDT.CHART-ALIGN-FE.de-caveat-removal.md` (NEW)
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.KPI.ds-engine-accuracy-50bps-sentinel.md` (MODIFIED)
- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W2.ae-lambda-code-reclamation-11-functions.md` (MODIFIED)

**Commit B (this commit):**
- `org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.001.rd-color-migration-and-qa.md` (MODIFIED — CANCELLED)
- `org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.015.rd-overflow-containment.md` (MODIFIED — CANCELLED)
- `org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.024.rd-mobile-readiness-audit.md` (MODIFIED — CANCELLED)
- `org/tier3_junior/0.2.4_RD_Valuation/task_orders/ADHC_DESIGN.007.rd-color-migration-and-qa.md` (MODIFIED — CANCELLED)
- `org/projects/ADHC_DESIGN.json` (MODIFIED — status=complete)
- `org/projects/REGISTRY.md` (MODIFIED — row move Active→Completed)
- `docs/architecture/PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md` (MODIFIED — Status line)
- `org/tier1_exec/2.0.0_SA_COO/logs/2026-04-21/session38_five_item_execution.md` (NEW, this file)

---

## Task Order Dispatch

| Agent | Task Order Path | Summary |
|-------|----------------|---------|
| 0.4.0_DS_ClientPlatform | org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.COHORT-A.ds-d04-summary-footnote.md | NEW. D_04 emits Cohort A summary (599 accts / $44.7M) for portal footnote. DS-primary + DE sub-deliverable. |
| 0.4.0_DS_ClientPlatform | org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.CHART-ALIGN.ds-d00c-leaderboard-per-day-gate-cutover.md | NEW. D_00c leaderboard cuts over to per-day tagging gate; Travis Q2 NNA converges to -$6.845M. |
| 0.4.0_DE_ClientPlatform | org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_STAUDT.CHART-ALIGN-FE.de-caveat-removal.md | NEW. DE removes chart↔leaderboard divergence caveat post-DS cutover. |
| 0.4.0_DS_ClientPlatform | org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.KPI.ds-engine-accuracy-50bps-sentinel.md | (CANCELLED) 50bps sentinel killed per Andrew — irrelevant, not a gate. |
| 0.7.0_AE_CloudOps + 0.5.0_AE_OpalETL (joint co-owner) | org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_TFIMPT.W2.ae-lambda-code-reclamation-11-functions.md | (REVISED) Rescoped to joint Phase 0 discovery + SES prod-access packet. Un-gated from Andrew Q2/Q4. |
| 0.2.2_RD_Attribution | org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.001.rd-color-migration-and-qa.md | (CANCELLED) orphan never spawned. ADHC_DESIGN closed. |
| 0.2.2_RD_Attribution | org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.015.rd-overflow-containment.md | (CANCELLED) orphan never spawned. |
| 0.2.2_RD_Attribution | org/tier3_junior/0.2.2_RD_Attribution/task_orders/ADHC_DESIGN.024.rd-mobile-readiness-audit.md | (CANCELLED) orphan never spawned. |
| 0.2.4_RD_Valuation | org/tier3_junior/0.2.4_RD_Valuation/task_orders/ADHC_DESIGN.007.rd-color-migration-and-qa.md | (CANCELLED) orphan never spawned. |

Execution dependencies:
  COHORT-A — parallel-safe, no blocker (DS starts on GO)
  CHART-ALIGN → CHART-ALIGN-FE (FE gated on DS artifact-ready)
  TRSB.W2 — staged→pending on joint AE engagement ACK (no external gate)

---

## Blockers

None. All 6 actions landed. 5 TOs ship-ready for GO dispatch on COO's next cycle; 4 TOs cancelled; 1 TO rescoped.

**Note on DSFLOW.001 (external but arriving during this session):** DS MCP'd during session: DSFLOW.001 shipped `b6e0c154` + `7b7381ac` — pre-commit gate tool live, 71 gold scripts clean, canary exit 1. My DSFLOW.002 (pending on my desk) is now UNBLOCKED — CLAUDE.md Rule 13 can cite the real tool path. Will execute DSFLOW.002 on next cycle. DS also noted Andrew mid-session directives (py_compile universal + DS owns S3 upload) — DS plans a follow-up commit to their prompt.md; I'll coordinate so DSFLOW.002 Rule 13 + DS prompt.md gate step don't duplicate.

---

## Current State

- 5 STAUDT/TRSB TOs staged/revised + all references updated.
- ADHC_DESIGN CLOSED (3-step atomic in Commit B).
- REGISTRY.md now shows 7 active projects (was 8): ADVI_ROLLUP, COMP_LEARNS, ADHC_ROUTER, ADVI_49EXEC, ADHC_DSFLOW, TRSB_TFIMPT, ADVI_STAUDT. + ADHC_TMSTEL on hold.
- ADHC_DESIGN moved to Completed/Archived at top of table with 2026-04-21 completion.

---

## Next Steps

1. **[COO, me, next cycle]** Execute DSFLOW.002 (my own pending TO — now unblocked post-DSFLOW.001 ship `b6e0c154`). CLAUDE.md Rule 13 + DS prompt.md gate step + §11 Q4 DS IAM probe.
2. **[COO, me]** Coordinate DSFLOW.002 with DS follow-up commit on prompt.md (Andrew universal py_compile + DS-owns-S3 drift correction). No duplication.
3. **[COO, me]** Dispatch GOs on the 3 new STAUDT TOs + TRSB.W2 joint-AE engagement request. STAUDT GOs are no-Andrew-wait; TRSB.W2 needs both AE ACKs before staged→pending.
4. **[CTO liaison, me]** MCP ACK to CTO on 5-item execution complete. Flag CHART-METH→CHART-ALIGN rename + confirmation of ADHC_DESIGN closure.
5. **[Parked per CTO]** AE 0.6 Schwab TRN NNA AC#3 methodology finding — surface to Andrew when 5-item bundle lands (per CTO 20260421T155431Z).

---

## Compiler Tools

| Tool | Command | Result | Purpose |
|------|---------|--------|---------|
| Read | CTO session log `session36_five_item_decisions.md` | 5 decisions + §9 TO checklist captured | Source of truth for execution |
| Read | existing STAUDT.HLOT2 + STAUDT.BFIX* TOs | Format + triad pattern captured | Template for COHORT-A + CHART-ALIGN authoring |
| Read | existing TRSB_TFIMPT.W2 + session36 TRSB addendum | Baseline W2 scope captured | Rescope delta identification |
| Read | ADHC_DESIGN.json + PRD + 4 orphan TOs | Current state captured | Closure edit targets |
| Grep | `1\\.1\\.0_SA_CTO_CompLearns\|2\\.1\\.0_SA_COO_CompLearns` | 0 hits post-rename (earlier session work) | Confirmed rename cleanly landed |
| Grep | `ADHC_DESIGN` in REGISTRY.md | Line 19 active row + lines 48+ completed table | Edit target locations |
| python | `python -c "import json; json.load(open('org/projects/ADHC_DESIGN.json'))"` | JSON OK | Post-edit validation |
| git | `git commit --only` with explicit pathspec (Commit A) | 5 files, 599 insertions, 89 deletions | Selective-staging discipline |

No comp-* runs — pure org-doc / TO authoring work. Compiler mandate minimum satisfied by template-inheritance + JSON validation.

---

— 2.0.0_SA_COO
