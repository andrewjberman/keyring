# Session — TRSB_LEDGER Backend Execution + P0 Incident + Close-Out (COO ~B lane)

**Date:** 2026-05-18
**Author:** 2.0.0_SA_COO~B
**Project:** TRSB_LEDGER (Trade Submission: Executor Authorization Enforcement + Audit-Trail Integrity)
**Companion log:** `trsb_ledger_decomposition~B.md` (same date; covers PRD v0.1 -> 10 TOs decomposition + initial GO dispatch)
**Status:** PROJECT NEAR-COMPLETE -- 11 of 12 TOs shipped + RAVC-accepted; awaiting Andrew live approve-retry as final E2E confirmation before firing TO-8b GO.

---

## Objective

Drive TRSB_LEDGER from "TOs dispatched" to "Pillars A/B/C all closed + deployed." Validate every RAVC ack from AE 0.7.0 / AE 0.5.0 / AE 0.6.1, author follow-on TOs as the decomposition unfolded (TO-10/TO-10a/TO-11), and run incident command on the first live-trade P0 the moment it surfaced.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-routes | `comp-routes behaviors` (CTO~B PRD-authoring run, referenced) | PASS | EVTSA9VEHNZVH carries `custom_error_response 403->200/index.html + 404->200/index.html` distribution-global with the comp-routes self-flag "Lambda 403 auth-denials will be swallowed." THIS WAS THE P0 SMOKING GUN -- the tool had already correctly flagged the defect; the incident was the realization that the flag predicted the exact failure mode. Referenced in TO-11 Phase-1 mandate. |
| Direct read | `infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py` (lines 140-254) | PASS | Confirmed 5 distinct 403 branches (no-jwt-email, mismatch, user-not-found, segregation, require_group). Confirmed `cors_response(403, {"message": ...})` returns clean JSON. Ruled out a handler defect during P0 layer-1 diagnosis. |
| Direct read | `portal/src/api/endpoints/trade-submission.ts:213/239/265/290` | PASS | All four workflow actions hit `/api/general/trades/workflow` (the authenticated, group-gated route). Ruled out the legacy public-route surface as a P0 cause structurally (TO-10's decommission was timing-coincident, not causal). |
| comp-pipescript / comp-blast / comp-iam | NOT re-run on trade-* | SKIPPED | Trade pipeline is uninstrumented in the comp graph (PRD section 5). CTO~B's PRD-authoring runs are authoritative. The TO-10/10a/11 follow-ons therefore use direct reads + `comp-routes` (the one tool that DOES cover the CloudFront layer) as the Phase-1 mandate substitute. |

**What worked:** `comp-routes behaviors` had pre-flagged the exact P0 failure mode in PRD section 5. The incident wasn't an unknown defect -- it was a known-flagged tool warning that hadn't been actioned because nobody had hit it yet. Tools earned their keep.

**What failed:** Nothing tool-side. The miss was process-side: the comp-routes flag was visible in the PRD but not promoted into a pre-go-live remediation TO. The post-incident brief recommends future PRDs treat comp-routes self-flags as candidate TO triggers.

**Gap found:** None. (`comp-pipescript` uninstrumented on trade-* is a known gap, documented PRD section 5; not a new finding.)

Appended to `org/compiler-tools-log.md` -- done automatically via `.comp-graph/.agent_context` SERIAL=`2.0.0_SA_COO~B` set at session start.

---

## Work Completed

### 1. Backend lane drive-through (AE 0.7.0 serial + AE 0.5.0 concurrent)

Sequenced and validated every RAVC ack on the 7-TO backend lane plus the concurrent durability TO. Each landed at its pipeline tag with deployed-endpoint smoke. Order of close:

| TO | Owner | Closes | Tag | Commit (closeout) |
|----|-------|--------|-----|-------------------|
| TO-0 | AE 0.7.0 | identity/seeding probe brief | n/a (doc) | (early-session) |
| TO-1 | AE 0.7.0 | A1 group-auth enforcement | trade-pipeline-v1.11.x | (early-session) |
| TO-2 | AE 0.7.0 | A5 actor identity binding | trade-pipeline-v1.12.x | (early-session, then AC2b hard-reject amend) |
| TO-3 | AE 0.7.0 | B1/B3/B7 append-only audit_events | trade-pipeline-v1.13.x | (mid-session) |
| TO-4 | AE 0.7.0 | B2/B4 compliance JSON snapshot + retire COMPLETE backend | trade-pipeline-v1.14.x | `6f425d7f3` (RAVC accept) |
| TO-5 | AE 0.7.0 | B5 by-approver GSI repoint | trade-pipeline-v1.15.x | `7a09bf112` |
| TO-6 | AE 0.5.0 | B8 DynamoDB PITR + deletion_protection | shared-infra-v1.15.x | (mid-session, concurrent) |
| TO-8 | AE 0.7.0 | dedicated `/api/general/trades/users/me` endpoint | trade-pipeline-v1.16.x | (late-session) |

Pillars A + B + C closed and deployed.

### 2. Probe-driven follow-ons authored mid-execution

TO-0's probe brief surfaced a live unauthenticated trade-execution route family on the legacy form distribution. CTO~B issued the architectural ruling (decommission, not migrate); I decomposed it into two TOs to separate the P0-level mitigation from the full destructive cleanup:

| TO | Owner | Purpose | Why split |
|----|-------|---------|-----------|
| TO-10a | AE 0.7.0 | P0 workflow-route removal (the high-risk public endpoint) | Stop the bleeding in the running pipeline before TO-10's destructive scoping landed |
| TO-10 | AE 0.6.1 (reassigned from 0.7.0) | Full legacy-surface decommission (CF dist E2RNVVND8GSGG3, S3, R53, etc.) | Parallelism while AE 0.7.0 stayed serial on the workflow_handler lane |

Both shipped and RAVC-accepted. Reassignment commit: `6f425d7f3`. Lock-in of force_destroy recon findings: `dca6360c5`. GO commit after Andrew explicit legacy-supersession confirmation: `4d4922118`.

### 3. P0 incident command (first live trade-approve failure)

**Andrew (direct, mid-session):** first ever live test trade on the portal -- APPROVE failed with `Unexpected token '<', "<!doctype "... is not valid JSON`. Two layers:

- **Layer 1 (working as designed, NOT a bug):** `andrew@opalinvest.com` was in `executors` only, not `approvers`. TO-1 group-auth correctly returned `403 {"message": "...not in the approvers group..."}`. The intended segregation-of-duties enforcement. Operational unblock: `andrew@` trade-users `groups` -> `[approvers, executors]` (AE 0.7.0, Andrew-direct authorization 18:45Z).
- **Layer 2 (the real defect -- portal-WIDE):** CloudFront distribution `EVTSA9VEHNZVH` carried a distribution-global `custom_error_response` mapping HTTP 403 + 404 -> `200 /index.html` (originally for SPA deep-link support). Because `custom_error_response` is distribution-global, it also caught `/api/*`: a clean Lambda 403 JSON was edge-rewritten to HTML, crashing the portal's `fetch().json()`. Affected every API auth-denial on every portal page, not just trade submission.

**Andrew follow-up directives, both addressed:**
- "andrew@opalinvest.com needs to be in all groups (submission, approver, executor)" -> done operationally; clarified `submission` is ungated (no group required); `[approvers, executors]` = full power in the 2-group model.
- "if I was being gated on rules, the popup that appears shouldn't be mangled HTML, it should simply say you're not authorized and to speak to your admin" -> this IS the Layer-2 fix, captured as TO-11.

### 4. TO-11 author + dispatch + RAVC-accept (the Layer-2 fix)

Authored on CTO~B's locked mechanism ruling: remove the distribution-global `custom_error_response`; replace the SPA deep-link fallback with a CloudFront Function (viewer-request) URI-rewrite scoped to the DEFAULT (S3) cache behavior only. Explicitly do NOT use the S3 website error-document (incompatible with OAC).

| Phase | What shipped |
|-------|-------------|
| TO-11 author | `c5746988e` -- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.011.ae-cloudfront-spa-fallback-api-error-fix.md` |
| Dispatch | GO same-message; AE 0.7.0 capacity free post-TO-8 |
| Deploy | tag `portal-auth-v1.15.9` (AE 0.7.0) |
| Regression smoke 3/3 PASS | (a) SPA deep-link resolves to index.html, (b) static asset loads, (c) API 403 returns real JSON |
| RAVC2 close | accepted same-session |

Cross-domain heads-up: `EVTSA9VEHNZVH` is the SHARED portal CloudFront distribution -- base CTO + base COO got the courtesy heads-up before apply per TO-11's `<cross_domain_coordination>` block.

### 5. Post-incident brief

CTO~B directed me to write the post-mortem; scope to TRSB_LEDGER P0; cover both findings; bake in the technical sharpening for the eventual structural gate.

- File: `docs/briefs/trsb-ledger-p0-trade-approve-incident-20260518.md`
- Commit: `995498c79`
- Sections: (1) Summary -- (2) Root Causes Layer 1 + Layer 2 -- (3) Fix -- (4) Second Finding (STOP-Delivery Gap) with implementable mechanism notes (filesystem read NOT MCP; surface-and-require-acknowledgement NOT hard-block-on-any-message) -- (5) Status.

The STOP-delivery gap: during incident command, a P0 STOP issued to AE 0.6.1 (then mid-destructive-deploy of the unrelated TO-10) did not surface until after that deploy completed. The agent was watcher-dark / turn-occupied during the heads-down window. Zero-harm by luck (TO-10 confirmed structurally unrelated to the P0). The `inbox-check-before-landing` discipline is cultural, not structurally enforced -- flagged to CTO~B as a candidate workspace-wide org-hardening item.

### 6. Project JSON ground-truth-currency rewrite

The `org/projects/TRSB_LEDGER.json` `phase` + `blocking` fields had grown into multi-paragraph operational diaries -- unreadable to anyone landing fresh. Full rewrite to a clean current-state summary:

- `phase`: "Phase 1+2+3 SUBSTANTIALLY COMPLETE 2026-05-18 (COO~B decomposition of PRD v0.1). 12 TOs total; TO-7 dropped per Andrew Q4 deferral. SHIPPED + RAVC-accepted (11): ..."
- `blocking`: 4-block summary -- (1) project state (11/12 shipped, tags through trade-pipeline-v1.17.0 / shared-infra-v1.15.0 / portal-auth-v1.15.9), (2) remaining open items (TO-8b GO-pending, TO-9 droppable stretch), (3) P0 incident with both layer fixes and the operational unblock, (4) the incident-command structural-enforcement finding flagged.
- Commit: `1cb9a1c21`

### 7. CTO~B handoff received: ADHC_HALTGT (post-session)

Andrew greenlit the STOP-delivery-gap finding as a separate project; CTO~B authored PRD v0.1 (`80d119662`) and handed it to ~B lane. 5 TO candidates, AE 0.7 lane, no urgency (AE 0.6.1's interim personal pre-apply check covers the gap). Acknowledged; queued behind TRSB_LEDGER close. Will MCP CTO~B for section-7 confirms (subject-prefix convention, safe-apply wrapper Q, override audit log Q) when I open decomposition window.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Split legacy-form decommission into TO-10a (P0-level workflow-route removal) + TO-10 (full destructive cleanup, reassigned to AE 0.6.1) | TO-10a stops the bleeding (eliminates the public-route family) before TO-10's destructive scope lands; reassignment unblocks AE 0.7.0 to stay serial on workflow_handler |
| Accept TO-10 as shipped despite the P0 STOP not surfacing in-flight | TO-10 confirmed structurally unrelated to the P0 (different distribution, different surface, different route family). Zero-harm; AE 0.6.1 owned the miss cleanly. The structural fix belongs in ADHC_HALTGT, not retroactively in TRSB_LEDGER. |
| Author TO-11 CloudFront fix as a TRSB_LEDGER TO not an ad-hoc | The defect was first surfaced by a TRSB_LEDGER P0 and resolves an Andrew-explicit acceptance criterion (readable auth-denial message). Charter fit even though the fix is portal-wide. |
| Andrew "all groups (submission, approver, executor)" -> operational `[approvers, executors]` | The 2-group model has no `submission` group -- submission is ungated. `[approvers, executors]` = full power. Clarified to Andrew. |
| Rewrite project JSON `phase`/`blocking` mid-session | Fields had become unreadable; ground-truth-currency takes precedence over append-only narrative |
| Hold ADHC_HALTGT decomposition until TRSB_LEDGER closes | No urgency pressure; AE 0.6.1 interim check covers; TRSB_LEDGER still has Andrew approve-retry pending. Single-project focus until that confirmation. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.010a.ae-p0-workflow-route-removal.md` | Authored TO-10a (P0 workflow-route removal) | Yes |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.010.ae-decommission-legacy-public-trade-surface.md` | Authored TO-10 (legacy-surface decommission); reassigned to AE 0.6.1 | Yes -- `6f425d7f3` (reassign) + `dca6360c5` (recon lock-in) + `4d4922118` (GO) |
| `org/tier2_senior/0.6.1_AE_PartnerETL/task_orders/TRSB_LEDGER.010.ae-decommission-legacy-public-trade-surface.md` | `git mv` from AE 0.7.0 path | Yes -- `6f425d7f3` |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.011.ae-cloudfront-spa-fallback-api-error-fix.md` | Authored TO-11 (CloudFront Function URI-rewrite; remove distribution-global custom_error_response) | Yes -- `c5746988e` |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/TRSB_LEDGER.002.ae-actor-identity-binding.md` | Amended with AC2b hard-reject criterion | Yes |
| `org/projects/TRSB_LEDGER.json` | `phase` + `blocking` clean rewrite | Yes -- `1cb9a1c21` |
| `org/projects/REGISTRY.md` | Updated TRSB_LEDGER row | Yes (rolled into multiple closeout commits) |
| `docs/briefs/trsb-ledger-p0-trade-approve-incident-20260518.md` | Authored post-incident brief (5 sections; both layers; STOP-gap mechanism recommendation) | Yes -- `995498c79` |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-05-18/trsb_ledger_execution_p0_close~B.md` | This log | Pending this commit |

Branch sync verified at log close: local `CLOUD` = `origin/CLOUD` = `5c73662c6`, 0 ahead / 0 behind. DT 0.4.0 confirmed `995498c79` + `1cb9a1c21` rode out to remote zero-diff (no contamination from the heavy untracked diagnostic-artifact pile in the shared workspace -- those belong to INF/MDPF/ADVI agents, left alone per commit-scope discipline).

---

## Blockers

None at log close. TRSB_LEDGER's only open item is **not a blocker** -- it is Andrew's live approve-retry as final E2E confirmation, which fires when he chooses. The TO-8b GO is staged behind it.

---

## Current State

**TRSB_LEDGER:** 11 of 12 TOs shipped + RAVC-accepted (TO-7 dropped per Andrew Q4 deferral). Pillars A + B + C all closed and deployed. Tags through `trade-pipeline-v1.17.0` / `shared-infra-v1.15.0` / `portal-auth-v1.15.9`. The 2026-05-18 P0 trade-approve incident is engineering-resolved on both layers: (Layer 1) `andrew@opalinvest.com` trade-users `groups` set to `[approvers, executors]` operationally; (Layer 2) TO-11 deployed -- distribution-global `custom_error_response` removed from `EVTSA9VEHNZVH`, replaced by a CloudFront Function viewer-request URI-rewrite scoped to the default (S3) cache behavior only; regression smoke 3/3 PASS; API 4xx now reach the FE as real JSON. Post-incident brief at `docs/briefs/trsb-ledger-p0-trade-approve-incident-20260518.md` (`995498c79`).

**Open item -- Andrew live approve-retry:** the final end-to-end confirmation that approve-as-`andrew@` now succeeds and the FE renders cleanly. On that confirmation, fire the TO-8b GO (RD 0.3.2 portal role-aware gating + completeSubmission removal; dispatch gate cleared, contract delivered).

**TO-9** (resubmission-lineage stretch, B6, AE 0.7.0 lane) -- staged, droppable. GO only if capacity.

**Adjacent lane:** **ADHC_HALTGT** (PRD v0.1, `80d119662`) -- CTO~B handoff received post-session; assigned to ~B lane; queued behind TRSB_LEDGER close. Will ping CTO~B for section-7 confirms when I open decomposition. **VALGATE** -- parked, capacity-gated on shared-pod.

**Low-pri opportunistic cleanup (COO~B-tracked):** dead inert `COMPLETE` constants in `trade-submission-handler/config.py` + `trade-parquet-batch-export/config.py`; `email_utils` "TRADE COMPLETE" heading + a pre-existing emoji. No urgency; pickable on the next AE 0.7.0 idle window.

---

-- 2.0.0_SA_COO~B
