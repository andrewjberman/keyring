# 1.0.0_SA_CTO — Session 15: ADVI_FIRMSEP PRD v0.1 — Multi-Firm Compartmentalization + Cottonwood Readiness

**Date:** 2026-05-07T~19:30Z (continuation)
**Frame:** Andrew architectural-assessment ask → CTO read-side audit of CloudFront + Lambda@Edge → directive to author PRD with "targeted decisions that bolster robustness but not at the risk of breaking changes" + Cottonwood-onboarding context.

---

## Andrew direct (multi-message)

1. "I want to discuss something high-level and complex... I want to make sure that we are properly splitting these based on firm-id... containment of data in those cached layers is paramount."
2. (After CTO architectural assessment): "ok write a prd for this and issue to COO. I'd like it if we can make targeted decisions here that bolster robustness but not at the risk of breaking changes."
3. (Same turn, addendum): "third partner will be coming in sooner than later, Cottonwood, so these kind of fixes should be handled the sooner the better."

---

## CTO read-side architectural audit (this session)

Read directly:
- `infra/aws/terraform/portal-auth/cloudfront.tf` (cache policy `opal_scoped_advisor_by_firm`)
- `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` (CF distribution `EVTSA9VEHNZVH`)
- `infra/aws/lambda-edge/auth-validator-edge/index.mjs` (viewer-request gate, JWT verify + X-Firm-Id inject)
- `infra/aws/lambda-edge/shared-advisor-router/index.mjs` (origin-request gate, FIRM_BUCKET_MAP, in-place origin mutation)
- `infra/aws/terraform/portal-auth/lambda-edge.tf` (Lambda@Edge resource definitions)
- `docs/architecture/INFETL_PORTAL_ROUTE_MATRIX.md` (RD's INFETL.007 audit)

### What's structurally sound ✅

1. Cache policy `opal_scoped_advisor_by_firm` (`cloudfront.tf:7-37`) includes `firm` query string + `X-Firm-Id` header in cache key. Cross-firm cache poisoning structurally prevented.
2. `X-Firm-Id` is JWT-injected by `auth-validator-edge` (`index.mjs:392`), NOT request-derived. Request can't override its own firm context.
3. Triple-gated: viewer-request validates JWT → injects → origin-request re-checks → API GW Lambda re-validates against `allowedFirmIds`.
4. `FIRM_BUCKET_MAP` identical in both Lambda@Edge files; mutation is in-place (preserves OAI auth context).
5. Opal-capital staff `?firm=` proxy with explicit 400 if missing.

### Gaps surfaced

| Gap | Severity | Phase 1 fix |
|---|---|---|
| `opal-data-inf` NOT declared as CF origin in TF | HIGH | TO-FIRMSEP.01 declare origin block (TF reflection only) |
| OAI grant cross-references invisible across `inf-pipeline` ↔ `portal-auth` | HIGH | TO-FIRMSEP.02 Terraform output/data cross-ref |
| `FIRM_BUCKET_MAP` duplicated in 2 files (TODO "extract once >2 partners") | MEDIUM (current) → HIGH (Cottonwood multiplies) | TO-FIRMSEP.03 extract to `_shared/firm-bucket-map.mjs` |
| No CI integration test on shared-advisor-router firm-routing | HIGH | TO-FIRMSEP.04 Mocha integration test in build pipeline |
| `opal-data-portal-v2-json` shared bucket cache-key composition unaudited | UNKNOWN | TO-FIRMSEP.00 Phase 0 audit + TO-FIRMSEP.06 CONDITIONAL fix |
| CW denial-event alarming absent | MEDIUM | TO-FIRMSEP.07/.08/.09 alarms |
| Stale duplicate at `infra/aws/lambda/shared-advisor-router/` | LOW (already in flight as INFETL.ROUTER-DRIFT) | TO-FIRMSEP.05 absorb scope |

---

## PRD v0.1 ship summary

**Document:** `docs/architecture/ADVI_FIRMSEP.md` (~700 lines, ~15K words)
**Project JSON:** `org/projects/ADVI_FIRMSEP.json`
**REGISTRY row:** added between INFETL and INFNNA.
**Dashboards:** CTO + COO prompt.md rows added.

**Scope:**
- §1 Andrew "targeted, non-breaking" + Cottonwood context.
- §2 Existing state — what's sound + what's brittle, with file:line references.
- §3 Multi-firm scaling pattern target state (5-row table — current N=2 vs target N=3+).
- §4 Component specs — 8 sub-sections covering each TO scope.
- §5 Compiler evidence skeleton + populated minimum-viable v0.1 evidence table sourced from CTO audit.
- §6 10 TOs phased: Phase 0 audit (1 TO), Phase 1 hardening (6 TOs), Phase 2 obs (3 TOs), Phase 3 Cottonwood onboarding (1 TO).
- §7 7 OQs (3 gate Phase 3, 4 are TO-authoring decisions for COO).
- Appendix B: 5 design alternatives explicitly rejected with rationale.
- Appendix C: 8-row risk register.
- Appendix D: cross-domain coordination with INFETL + INFNNA + bd-pipeline + inf-pipeline.

**Bandwidth model:** heavily AE 0.7 weighted (single-pod for Phase 0+1+2; +1 DS for Phase 3 ownership_map). Total ~5 effort-days Phase 0+1+2; ~1 effort-day Phase 3. Ships in parallel with INFETL Phase 1 + INFNNA RECTIFY since AE 0.7 has been the high-velocity lane.

**Out of scope per Andrew "non-breaking" constraint:**
- Per-firm CloudFront distribution.
- Replace runtime origin-mutation pattern.
- Read-path migration gold→platinum (INFETL Phase 2 scope).
- Tier policy reauthoring; Cognito migration.

**Cross-project ABSORBS:**
- `ADVI_INFETL.ROUTER-DRIFT` scope (canonical source at lambda-edge/ is current; stale duplicate at lambda/ is the cleanup target; CloudTrail audit folded in).

---

## RAVC1 issued to COO

MCP message delivered 2026-05-07T~19:36Z to `2.0.0_SA_COO` inbox. Subject: "RAVC1 — ADVI_FIRMSEP PRD v0.1 SHIPPED — multi-firm compartmentalization + Cottonwood readiness — request decomposition."

Awaiting COO RAVC2 ACK with decomposition path + sequencing.

---

## Carry-overs to next session

| Item | Owner | Status |
|------|-------|--------|
| FIRMSEP COO RAVC2 ACK + TO file authoring | COO | Awaiting ACK |
| FIRMSEP §7 OQ resolution (Cottonwood slug + OAI strategy + JWT issuer) | Andrew via CTO/COO | Pre-Phase-3 gate |
| FIRMSEP Phase 0 (TO-FIRMSEP.00) ship → informs Phase 1 .06 conditionality | AE 0.7 | Pending COO dispatch |
| INFETL.ROUTER-DRIFT absorption coordination | COO | Need closeout note in INFETL.ROUTER-DRIFT TO referencing FIRMSEP |
| INFNNA tonight cascade ETA ~21:00-22:00Z | DS~A + AE 0.7 | In flight (carry from session 14) |
| INFNNA.GOLD RAVC ACK → INFETL.011 cron-flip-ack TO authoring | DS~A → CTO | Gated on cascade success |
| INFETL.LAMBDA-DIMS / SILVER-AGGREGATOR / GOLD-EVENT-TRIGGER ship | AE 0.7 | In flight |
| INFLFE.006-data DS~A surgical fix | DS~A | Pending HIGH (carry) |
| ADVI_RPBKTPI TO-2 historical chain re-run authoring | CTO | Backlog |
| AGENT_CONTEXT_POISONING_RECOVERY.md playbook | CTO | Backlog |
| ADVI_INFETL v0.3 PRD ratchet (compiler evidence post Phase 1 ship) | CTO | Post Phase 1 ship |
| ADVI_FIRMSEP v0.2 PRD ratchet (Phase 0 unknowns resolved + compiler evidence post Phase 1 ship) | CTO | Post Phase 1 ship |

— 1.0.0_SA_CTO 2026-05-07T~19:40Z
