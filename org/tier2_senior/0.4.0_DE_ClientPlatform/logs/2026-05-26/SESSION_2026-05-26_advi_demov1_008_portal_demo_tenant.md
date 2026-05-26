# SESSION: ADVI_DEMOV1.008 -- Portal demo-tenant connection (Phase 6 Frontend Connection)

**archetype:** IMPLEMENT

**Date:** 2026-05-26
**Agent:** 0.4.0_DE_ClientPlatform
**Project:** ADVI_DEMOV1 (Phase 6 Frontend Connection)
**TO:** ADVI_DEMOV1.008.de-portal-demo-tenant-connection
**Issued by:** 2.0.0_SA_COO (commit `6e17b7b4d`; GO ~15:29Z)
**Andrew sovereign direct context:** 2026-05-26 ~15:45Z verbatim: "if all the data is prepared in opal-data-demo, then it is time to connect it to frontend ... select 'Demo' and see all the data populate in canonical format just how it is already done for 49 Financial and Inflection Wealth Management."

## Spawn-with-direction context

DE 0.4_DE_ClientPlatform revived from LD-0014 retirement per Andrew sovereign-direct /allocation #7 implicit AC9-lift (ws COO commit `f7f12d4bb`). MSTR /mstr-spawn ~15:23Z; SPAWN-WITH-DIRECTION canonical pattern (LD-0021) with TO-008 routing inline in spawn-msg. Parallel to AE 0.7 sovereign-spawn ~15:11Z pattern from /allocation #6.

## What shipped

Single coordinated commit on portal submodule DEV branch: `03a85441` (9 files, +499/-2).

**6 portal items wired** (4 PRD-enumerated + 2 PRD-completeness additives ratified by COO under decomposition authority pre-commit per [[feedback_self_correction_upstream_of_verify_channel]] upstream-of-verify-channel doctrine):

| # | File | Change |
|---|---|---|
| 1 | `src/api/endpoints/advisor-intelligence.ts` | `ROUTER_FIRM_SUFFIX` add `'demo': 'demo'` (identity-to-identity per opal-data-demo bucket naming) |
| 2 | `src/lib/firmAccess.ts` | `FIRM_ALLOWED_PATHS['demo']` = full 8-path set + `FIRM_EMAIL_DOMAINS['demo'] = 'demo.test'` |
| 3 | `src/pages/AdvisorIntelligence/_partners/demo/` | NEW 4-file directory mirroring `_partners/49financial/`: constants.ts (~16 LOC; BD_SOURCE_ATTRIBUTION reused), roles.ts (~22 LOC; DEMO_ROLES mirroring 49F 5-role taxonomy), layout.ts (~110 LOC; DEMO_LAYOUT mirroring FORTY_NINE_FINANCIAL_LAYOUT BD-pipeline-native), index.tsx (~290 LOC; DemoAdvisorIntelligence mirroring 49F structurally) |
| 4 | `src/pages/AdvisorIntelligence/index.tsx` | `ALL_PARTNER_FIRMS` += `{ id: 'demo', name: 'Demo' }`; `PARTNER_VIEWS['demo'] = DemoAdvisorIntelligence` |
| 5 | `src/pages/AdvisorIntelligence/_shared/hooks/useTenantLayout.ts` | `LAYOUTS` registry add `'demo': DEMO_LAYOUT` (avoids 9 _shared/ components silent-fallthrough to DEFAULT_LAYOUT placeholder-sentinels; COO additive 5) |
| 6 | `src/pages/AdvisorIntelligence/_shared/types/TenantLayoutConfig.ts` | `CanonicalFirmId` union extension include `'demo'` (AC5 bun-tsc load-bearing; COO additive 6) |

## PRD-completeness finding (banked)

Source walk during pre-implementation surfaced 2 structurally-required edits not in PRD v0.4 Sec. 6.1's explicit 4-item enumeration:

(5) `useTenantLayout.ts` LAYOUTS registry: without `'demo'` entry, 9 `_shared/` components reading via `useTenantLayout(firmId='demo')` silently fall through to `DEFAULT_LAYOUT`. DEFAULT_LAYOUT carries PLACEHOLDER SENTINELS per SHARED.001 Sec. E.10 (`displayName: ''`, `sourceAttribution: ''`, `roles.keys: []`) -- the fallthrough renders demo with empty UI strings.

(6) `CanonicalFirmId` union extension: bun tsc errors at `demo/layout.ts`'s `firmId: 'demo'` declaration without the union extension. AC5 load-bearing.

Surfaced to ws COO 15:29Z MCP; COO direct-ratified under decomposition authority 15:40Z per Option A. CC ws CTO informational (PRD v0.4.1 micro-amendment scribe at /ws-charter convenience; non-gating). [[feedback_corroborate_with_concern_verdict_shape]] pattern operating at pre-impl design-gate.

## Acceptance criteria evidence

| AC | Status | Evidence |
|---|---|---|
| AC1: single coordinated commit | PASS | `03a85441` on portal DEV; 9 files; safe-commit.sh wrapper (Rule 14a) |
| AC2: comp-transform schema-check --feature demo | DEFERRED -- TOOL GAP | comp-graph keys per-file index.tsx as "index" component -> multi-collision blocks lookup; structurally satisfied (DemoView consumes identical fields to FortyNineFinancialView) |
| AC3: comp-transform ternary-audit | DEFERRED -- TOOL GAP | Same multi-"index" gap; structurally satisfied (PARTNER_VIEWS map dispatch; zero `cohort === 'demo'` ternary chains) |
| AC4: comp-cache collisions | PASS | 4 baseline by-design collisions unchanged; demo's index.tsx adds 4th by-design caller to firm-leaderboard key (additive; same response shape) |
| AC5: bun tsc clean | PASS | exit 0 |
| AC6: bun build clean | PASS | exit 0; built in 11.72s |
| AC7: dev-server smoke renders 'Demo' option | STRUCTURAL PASS | dist/assets/*.js bundle contains "Demo" + "49 Financial" + "Inflection Wealth Management" partner labels (grep verified); TO-VAL-FE full visual smoke deferred to Andrew UAT |
| AC8: RAVC2-Request | IN FLIGHT | this session log + MCP RAVC2 to ws COO |

## Compiler Tools

| Tool | Run | Result | Notes |
|---|---|---|---|
| `comp-build` | post-write graph rebuild | 1684/1749 file-backed nodes; 1468 CALLS / 105 FETCHES edges | demo subdir not yet indexed (worktree not main tree) |
| `comp-cache collisions` | post-write | clean; 4 baseline by-design collisions unchanged | no new colliding-key class introduced |
| `comp-transform schema-check AdvisorIntelligence --feature demo` | post-write probe | "Component not found" | comp-graph indexes 3 separate index.tsx files as "index" component -- naming-collision gap; flagged for /spot-check / CVO comp-tools-expansion follow-up |
| `comp-transform schema-check FortyNineFinancialView --feature demo` | post-write probe (alias variant) | "Component not found" | same gap |
| `comp-transform schema-check DemoAdvisorIntelligence --feature demo` | post-write probe (new variant) | "Component not found" | demo subdir not in main tree (worktree-only) |
| `comp-transform ternary-audit AdvisorIntelligence` | post-write probe | "Component not found" | same gap |

Tool-resolution gap is observable structural limitation, not a TO-008 regression. comp-transform's component-name keying needs refinement to disambiguate per-directory index.tsx files (e.g., `<dir>:index` or alias-aware). Surfacing to ws CVO via RAVC2 for follow-up alongside CVO's comp-* expansion brief (ws COO endorsed `92b198aac`).

## Risks (PRD Sec. 6.1) -- mitigation status

| Risk | Mitigation | Status |
|---|---|---|
| R1: DemoView divergence from 49F canonical | structural mirror | OK (TS shape identical; same _shared infra consumption) |
| R2: Hidden firmId hard-branch trip | grep audit | OK (zero `firmId === '49financial'` / `'inflection'` branches in portal/src; only `firmId === 'opal-capital'` internal-gates which don't need demo-extension) |
| R3: Advisor-empty surface for demo | Andrew UAT (TO-VAL-FE) | DEFERRED to TO-VAL-FE Smoke-C |
| R4: PROD-strand on cherry-pick | DT-pod ephemeral worktree | DEFERRED to TO-009 (DT-pod authority) |
| R5: React Query key collision | comp-cache collisions | OK (clean; only additive same-shape collisions) |

## Cross-domain coordination

Per PRD Sec. 6.1: shared-advisor-router L@E + CloudFront behaviors already firm-agnostic for `?firm=demo` per ADVI_DEMOV1 Sec. 3 + Phase 6 PRD acceptance -- no AE 0.7 LEDGEH/CDNCOHT critical-path touch. Confirmed by zero infra-change scope of TO-008 (AC9-INDEPENDENT per TO file).

## Downstream

- TO-009 (DT-pod portal DEV->PROD push): COO authors + dispatches when this RAVC2-Accepted
- TO-VAL-FE (Andrew UAT visual-smoke): closes original ADVI_DEMOV1 AC4 + Phase 6 + project as a whole

## Throughput note

Spawn 15:23Z -> commit 03a85441 ~16:00Z = ~37min DE wall (well under PRD's ~3-5h estimate). Single-session compression via: clean spawn-with-direction context + 49F template fidelity + parallel pre-work + same-session COO completeness-ratify cycle (15:29Z finding -> 15:40Z ratify -> commit ~16:00Z).

## Post-ship closure

**ws COO RAVC2-ACCEPT** delivered 15:48Z (`20260526T154838Z` MCP) — crossed-in-transit with my RAVC2-Request (~10min apart). All 8 ACs evidence-banked; AC2/AC3 comp-graph multi-"index" component-name tool-gap folded into ADHC_COMPIL_V5 follow-on as Fix-4 candidate (distinct from existing 3 fixes per CVO comp-* expansion brief `92b198aac`). Joined today's fast-lane bank as 5th spawn-to-ship record (sibling to AE 0.6.1 CDNCOHT-INTERIM ~10/5min two-chain + AE 0.7 CDNCOHT TO-001 ~19min + DS 0.1.0 YALP_MKTOVR cascade 72min end-to-end). Banked as canonical DE-pod-4 revival fast-lane reference pattern.

**COO 4-ask disposition:**
1. RAVC2-ACCEPT TO-008 — DONE
2. Author + dispatch TO-009 — pending next /drive cycle (~15:47Z); DT pod choice via /allocation #8 (likely DT 0.4 P3 SPAWN-NEEDED per Andrew implicit-lift Phase 6 parallel to DE 0.4 spawn pattern)
3. Tool-gap surface — banked in RAVC2-ACCEPT body; folded into ADHC_COMPIL_V5
4. ADVI_DEMOV1 JSON phase advance — COO in-flight (status stays `active` for TO-009 + TO-VAL-FE remainder of Phase 6)

**CronCreate /work 20m cycles post-RAVC2-ACCEPT:**

| Cycle | Time | Outcome | Notes |
|---|---|---|---|
| 1 | ~16:05Z | NO-WORK | Inbox: 1 message (COO RAVC2-ACCEPT — closure ACK; no return work required). Watcher repair: PRIOR-SESSION-ORPHAN AUTO-RESPAWN-INTERRUPT-LOST (PID 135857) killed + relaunched tracked (bzriq2d4y). TO queue: 0 actionable (TO-008 complete; TO-009 DT scope; TO-VAL-FE Andrew scope). |
| 2 | ~16:25Z | NO-WORK | Inbox empty. Watcher PROCESS-OK tracked (byrv8iziz). TO queue unchanged. KEEP-ACTIVE per /allocation #7 disposition for any Phase 6 follow-on. |

**ws CTO CC informational** delivered 15:47Z proposing PRD v0.4.1 micro-amendment (Phase 6 §6.1 item enumeration + AC list update to match shipped 6-item reality + cottonwood sister-class precedent note). Non-gating; at CTO's /ws-charter cycle convenience. No response required from me.

**Standing posture:** KEEP-ACTIVE; CronCreate /work 20m primary loop; tracked watcher live; heartbeat current. Available for any Phase 6 follow-on surface (TO-VAL-FE-driven DE fix if Andrew UAT exposes issue; /allocation #8 re-evaluation if COO disposition changes; cross-pod DE dispatches per POD_DE_ANY lane discipline).

## Memory candidates (banked for future write)

Observed patterns worth distilling for the memory system once Phase 6 fully closes:

- **Pre-implementation source-walk PRD-completeness finding pattern** — DE walked source pre-coding and surfaced 2 structurally-required edits (useTenantLayout LAYOUTS + CanonicalFirmId union) not in PRD's explicit enumeration; ratified by COO direct-Option-A pre-commit; shipped in same coordinated commit. Empirical anchor for [[feedback_self_correction_upstream_of_verify_channel]] extended downward to DE-level. Useful for: future partner-onboarding work, multi-tenant module wiring.
- **Type-system-load-bearing additive shape** — item 6 (CanonicalFirmId union extension) was strictly required for AC5 `bun tsc` clean, distinct from item 5's runtime-correctness rationale. Distinguishing "compile-load-bearing" vs "runtime-load-bearing" additives sharpens the COO scope-ratify call from "ratify or counter" to "ratify (must-have) + ratify (should-have)".
- **comp-graph multi-"index"-component naming collision** — observable structural limitation in comp-transform schema-check / ternary-audit lookup for the AdvisorIntelligence component family; surfaced as Fix-4 candidate for ADHC_COMPIL_V5. Reusable across any portal codebase area with per-directory `index.tsx` barrel exports (i.e., most React feature folders).
- **Crossed-in-transit ACK pattern** — COO RAVC2-ACCEPT + DE RAVC2-Request shipped within ~10min of each other (no causal dependency; both racing toward closure). Sister pattern to [[feedback_standby_prep_compress_to_delivery_when_context_sufficient]] for compression on the closure-side rather than the dispatch-side.

## Phase 6 follow-on: portal-DEV-rule brief arc (Andrew-direct → CLAUDE.md Rule 19)

Separate sub-session arc triggered by Andrew direct 2026-05-26 ~16:35Z immediately after the TO-008 strand discussion: *"DT will do it, I want you to write a brief on the subject because we need to make it a rule that you always switch localhost back to DEV because this is an obnoxious footgun that keeps happening."*

Trigger: discovery during TO-008 that the main `portal/` worktree was stranded on PROD (commit `0be05530`), forcing DE 0.4 to detour into the `.runtmp/portal-dev-verify` ephemeral worktree to access DEV. Andrew then hit `localhost` expecting demo + couldn't see it — diagnostic question "is PROD on localhost again?" confirmed footgun recurrence.

### Brief authoring + dispatch

**Brief artifact:** `docs/briefs/portal-main-tree-stays-on-dev-rule-20260526.md` committed `14235c0d2` (CLOUD; `--force` safe-commit bypass with audit entry per persistent multi-agent index contention from DS 0.1 staging files in shared `docs/briefs/` directory — canonical wrapper-doc scenario).

**Brief structure:**
- §1 Problem statement (silent footgun: `bun run dev` doesn't warn that branch is PROD)
- §2 Incident inventory (3 strands in 5 days: 2026-05-22 pod 3 + SSCN + 2026-05-26 TO-008)
- §3 Root cause (cherry-pick-onto-PROD mechanism does `git checkout PROD` in main tree with no `git checkout DEV` after)
- §4 Proposed rule (main tree always sits on DEV; any branch-state change restores DEV in same operation; 3 corollaries)
- §5 Structural enforcement candidates (A post-checkout hook warning + B `.tools/portal-promote.sh` wrapper + git()-shadow ban + C predev check; ranked by reliability)
- §6 Routing recommendation (CLAUDE.md rule + structural-enforcement PRD)
- §7 Asks of ws CTO (ratify + PRD authoring + COO routing)
- §8 Asks of ws COO (DT decomposition + /spot-check HEAD check + `.runtmp` cleanup)
- §9 Open questions (cultural-vs-structural sufficiency, replace-vs-coexist, carve-outs)

**Dispatch:**
- ws CTO `1.0.0_SA_CTO` — `[BRIEF-ASK-RATIFY]` MCP 16:50Z (primary ratifier)
- ws COO `2.0.0_SA_COO` — `[CC]` MCP 16:50Z (decomposition awareness; ACK received 17:09Z confirming 3-in-5-days = "cultural alone insufficient" signal + R&D candidate framing; ACK noted that brief §8 Ask 2 `/spot-check` HEAD check is CVO scope not COO scope — banked routing correction)

### CTO ratify outcome (cycle #32, commit `c08f4287f` ~17:30Z)

**Brief RATIFIED.** Both my leans confirmed:

- **Q1 (cultural vs structural sufficiency):** STRUCTURAL warranted. CTO cited ADHC_HALTGT precedent (similar multi-incident → structural transition). Cultural rule binds NOW via Rule 19; structural enforcement (A+B+C combo) implements via PRD next session.
- **Q2 (`.tools/portal-promote.sh` REPLACE vs coexist):** REPLACE + shadow-ban. CTO cited ADHC_OWNPTH.010 `git()` shell-shadow for destructive HEAD moves as binding precedent. Partial adoption keeps footgun alive.
- **Q3 (carve-outs):** Deferred to Andrew enumeration via the MCP CC already routed.

**Shipped this CTO tick (commit `c08f4287f`):**
- **CLAUDE.md Rule 19** — portal main worktree always stays on DEV; restore-on-discovery rule; ban on `.runtmp/portal-*` workaround as workaround pattern. Co-located with Rules 17-18 in Critical Deployment Rules block (binding rule, not portal-section informational).

**Deferred to next CTO session:**
- Structural enforcement PRD (A+B+C combo, ~2-4h DT wall) per CTO capacity flag (queued alongside Wave-2 YALP_* PRDs + ADHC_COMPIL_V5 TO-003 + LD-scribe).
- Memory update bundling — CTO will extend [[feedback_portal_prod_promotion_strands_main_tree]] with the implemented enforcement reference once structural PRD ships. If another strand surfaces in interim, DE 0.4 can extend the memory directly per brief §6 (3).
- `.runtmp/portal-dev-verify` cleanup — COO operational doctrine call via her /drive sweep + DT-pod coordination.

### Brief arc timeline

| Time | Event |
|---|---|
| ~16:30Z | TO-008 strand discovered; Andrew hits localhost, sees PROD, asks "is PROD on localhost again?" |
| ~16:35Z | Andrew direct: "write a brief on the subject ... make it a rule" |
| ~16:45Z | Brief authored at `docs/briefs/portal-main-tree-stays-on-dev-rule-20260526.md` |
| ~16:50Z | Brief committed `14235c0d2` (--force bypass; DS 0.1 multi-agent contention; audit logged); MCP dispatch to ws CTO + CC ws COO |
| ~17:09Z | ws COO ACK CC received (well-scoped; 3-in-5-days signals structural-warranted; routing-deferred on CTO capacity) |
| ~17:30Z | ws CTO RATIFY (cycle #32); CLAUDE.md Rule 19 shipped `c08f4287f`; structural PRD deferred next session |

End-to-end wall: Andrew-direct ask → CLAUDE.md rule binding = ~55min. Sub-arc included: brief authoring (~10min) + dispatch (~5min) + COO ACK (~20min) + CTO ratify (~20min).

### Standing posture

- Cultural Rule 19 binds NOW (CLAUDE.md committed).
- Structural enforcement (A+B+C) PRD pending next CTO session.
- If DT pods do another bare `git checkout PROD` in the main tree during interim window → Rule 19 violation surfaced via /spot-check or /verify-channel → REPAIR-AMENDMENT or DRIVE_ESCALATION routing per CTO close-out note.
- DE 0.4 KEEP-ACTIVE per /allocation #7 disposition for any Phase 6 follow-on (TO-008 ship + brief arc both shipped; standby for TO-VAL-FE issue surface or interim-strand discovery).
