# Session 22 — Dashboard reconcile + ADVI_SHARED PRD authoring

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-05-12 ~21:25Z..~22:15Z (~50min wall)
**Frame:** Andrew direct "RECONCILE ANY DASHBOARDS/REGISTRIES" (via COO 21:25Z relay) → CTO dashboard mirror pass → DT 0.4 directive for new ADVI_SHARED PRD → PRD authored + shipped.

---

## Session arc

Two distinct workstreams in one session:

1. **CTO dashboard mirror pass** — reconcile `org/tier1_exec/1.0.0_SA_CTO/prompt.md` Project Status Dashboard against COO's authoritative REGISTRY.md refresh (`982f73c03` / `d9bcc45a3`). Result: `b6f6b0c9a`.
2. **ADVI_SHARED PRD v0.1 authoring** — Andrew direct 2026-05-12 evening via DT 0.4 brief `cd0847d1d` post `portal-v2.1.82` PROD deploy. Result: `54c1ea270` (684-line PRD + project JSON + REGISTRY row).

---

## Workstream 1 — Dashboard mirror pass

### Trigger
Inbox message from 2.0.0_SA_COO 21:25Z relaying Andrew "RECONCILE ANY DASHBOARDS/REGISTRIES YOU AND COO KEEP WITH CURRENT STATE." COO had already done the COO-side reconciliation (REGISTRY refresh + 29-TO pre-May sweep close + ADVI_INFSHIP closure); requested CTO mirror pass on prompt.md dashboard.

### What I corrected
CTO `prompt.md` dashboard header was last updated 2026-05-06 PM (session 11) — ~6 days stale. Mirror pass:

| Change | Detail |
|---|---|
| Header narrative paragraph | Refreshed for 2026-05-12 PM state (chain marathon $203M aligned, INFPUBLISHERDEDUP, 4-panel-gap closure, SCHWAB-BUCKDR, INFLFE/INFSHIP/INFNNA all closed) |
| ADVI_ROLLUP row | Post-may-sweep state (COO d9bcc45a3); candidate for closure |
| ADVI_INFLEC row | Partner-demo surface STRUCTURALLY COMPLETE 2026-05-12 |
| ADVI_INFREL row | TO-001 FINAL CLOSE 2026-05-11 (AE 0.6.1 RAVC6 + v1.7.46) |
| ADVI_FIRMSEP row | Phase 2 obs COMPLETE 2026-05-11 (AE 0.7 `63358ee24`) |
| ADVI_INFETL row | gold_prof v2.0 + INFPUBLISHERDEDUP today |
| ADHC_COMPIL_V4 row | Added (was missing from CTO dashboard) |
| ADVI_INFGRO row | Stage 1 staged+dispatch_held (Andrew 3-decision pending) |
| ADVI_INFTGT row | P0 closed 2026-05-11; P1/P2 absorbed by inline ships |
| Removed: ADVI_INFLFE | → Recently Completed (TO-006-data absorbed by chain marathon) |
| Removed: ADVI_INFSHIP | → Recently Completed (Andrew directive close pre-May) |
| Removed: ADVI_INFNNA | → Recently Completed (Phase 1 complete 2026-05-11) |
| Pipeline Tags table | BD v2.24.6 → **v2.24.7**, Portal Auth v1.15.5 → **v1.15.7**, Inf Pipeline v1.7.43 → **v1.7.51** (+8 jump), Portal v2.1.75 → **v2.1.82** |

### Commit + push
- `b6f6b0c9a` author `1.0.0_SA_CTO` — `org/tier1_exec/1.0.0_SA_CTO/prompt.md` only (1 file, +18 / -15)
- `.tools/safe-commit.sh --only` PASS; pushed to CLOUD without issues
- RAVC-close ACK to COO via MCP; COO confirmed bidirectional close (subsequent message reported "additional resolution" — explicit Portal v2.1.82 tag matched COO's DEV-pointer record)

---

## Workstream 2 — ADVI_SHARED PRD authoring

### Trigger
Inbox message from 0.4.0_DT_ClientPlatform: Andrew direct directive (verbatim quote in DT brief `cd0847d1d`): "ADVI_SHARED... will be all about how to manage the shared vs fine-tuned/bespoke components and elements of ADVI between the various advisors... as we add new advisors, we want to be able to easily generate fine-tuned ADVI pages."

DT brief identified the empirical trigger: 102 architectural lint warnings remaining after `portal-v2.1.82` PROD deploy (`bf26d1b8` cleared 12 TS errors + 7 lint errors first). Warnings cluster:
- Category A `react-refresh/only-export-components` ~75
- Category B `react-hooks/static-components` ~12
- Other react-hooks deps ~15

### RAVC1 ack workflow
- Inbox-watch fired at 21:32Z; check_inbox surfaced DT message
- RAVC1 ack sent immediately to DT 0.4 (`20260512T213258Z_..._RAVC1_ack__ADVI_SHARED_PRD_request_recei.md`) — sequencing plan + initial framing thoughts
- COO RAVC-close on dashboard-reconcile arrived in parallel; informational only; standing by for ADVI_SHARED RAVC2

### PRD authoring sequence
1. **Pre-authoring repo check** (PRD_AUTHORING_PROTOCOL.md §6): `docs/architecture/ADVI_SHARED.md` confirmed NEW; `org/projects/ADVI_SHARED.json` confirmed NEW; macro `ADVI` already in MACRO_CODES.md
2. **Compiler-evidence sweep** (PRD_AUTHORING_PROTOCOL.md §5):
   - `comp-build` — cache rebuild; 1590/1663 source SHAs indexed; 1360 CALLS / 99 FETCHES / 268 READS_S3 / 232 WRITES_S3 / 54 TRIGGERS edges
   - `comp-blast AdvisorIntelligence` — 3 endpoints / 1 Lambda (opal-partners-data); confirmed shared Lambda serves both 49F + INF
   - `comp-blast useTenantLayout` — NO MATCH (hooks aren't graph nodes today); logged as ADHC_COMPIL_V4 backlog candidate
   - `comp-cache collisions` — **4 cache-key collisions surfaced empirically** (`['advisor-book-view', advisorId, firmOverride]`, `['advisor-intelligence', 'timeseries-overview', firmOverride]`, `['firm-leaderboard', firmOverride]`, `['partner-analytics', granularity, firmOverride]`) — firmId namespace ambiguity causes hash divergence between `'inf'` vs `'inflection'` callers
   - `comp-transform schema-check AdvisorIntelligence` — "Component not found" (dispatcher node, not leaf); deferred per-component schema-check to TO-level Phase 1 mandates
3. **Empirical code-state survey:**
   - `useTenantLayout` LAYOUTS map has 1 entry (`inflection` only)
   - 4 call-sites adopt `useTenantLayout`; **3 files still inline `isInflectionFirm` pattern** (22 call-sites total): PartnerAnalytics.tsx (15 — worst offender), AdvisorBookView.tsx (5), ClientsTab.tsx (5)
   - `_partners/49financial/` has 3 files (constants/index/roles); `_partners/inflection/` has 5 + overrides/ (`FidelityCustodianBar` only)
   - **firmId namespace is 4-layer:** firmAccess.ts L1 ('49financial'/'inflection'/'cottonwood') vs PARTNER_VIEWS L2 ('bd'/'inflection') vs _partners/* L3 ('bd'/'inf') vs LAMBDA_FIRM_ID L4 maps L3→L1
4. **PRD draft** — 684 lines, 13 sections + 2 appendices:
   - §1 background + Andrew quote
   - §2 current-state audit (4 sub-sections including the 4-layer firmId mess)
   - §3 target architecture (canonical firmId, extended TenantLayoutConfig, §3.3 co-location convention, §3.4 two-tier component-extraction rule, §3.5 scaffolding tool spec, §3.6 lint regression gate)
   - §4 phased migration plan with sequencing diagram (Phase 0 audit / Phase 1 extend+refactor+canonicalize 7-8 TOs / Phase 2 scaffold 2-3 TOs / Phase 3 regression gate 2 TOs)
   - §5 Compiler Evidence table + findings narrative
   - §6 TO mandate template + cross-domain coordination notes for SHARED.006
   - §7 7 open questions for Andrew/COO triage
   - §8 8 project-level acceptance criteria
   - §9 6 risks + mitigations
   - §10 cross-references
   - §11 versioning
   - §12 Appendix A — 102-warning per-file inventory
   - §13 Appendix B — Firm naming taxonomy current→canonical

### Commit + push
- `54c1ea270` author `1.0.0_SA_CTO` — 3 files (`docs/architecture/ADVI_SHARED.md` + `org/projects/ADVI_SHARED.json` + `org/projects/REGISTRY.md`)
- `git add` required first (new files; safe-commit.sh --only needs git to track them); then `.tools/safe-commit.sh --only` PASS
- Pushed to CLOUD: `b6f6b0c9a..54c1ea270`
- RAVC2 to COO: `20260512T214331Z_..._RAVC2__ADVI_SHARED_PRD_v0.1_SHIPPED_54c1.md`
- RAVC2 close to DT 0.4: `20260512T214347Z_..._RAVC2_close__ADVI_SHARED_PRD_v0.1_SHIPPE.md`

### Key architectural decisions captured in PRD

| Decision | Rationale |
|---|---|
| Canonical firmId = `firmAccess.ts` L1 namespace ('49financial', 'inflection', 'cottonwood', 'opal-capital') | Closest to JWT source; downstream consumers converge. Eliminates all 4 ambiguity bugs in §2.2 |
| File-org Category A = co-location with split modules (page-as-directory) | Locality of reasoning wins on read path; per-domain shared module risks dumping ground |
| Component-extraction Category B = two-tier rule (sibling-file ≥30 lines; function-returning-JSX <30 lines) | Single-tier rule either over-extracts trivial helpers (bad readability) or fails to extract substantive inner components |
| Lint regression gate = custom ESLint rule (CI grep fallback) | IDE feedback on save; auto-fix hints; can downgrade-to-WARN during migration |
| 49Financial canonical literal stays `'49financial'` (not renamed) | Already in JWT/DDB; rename forces multi-system downtime. Component name `FortyNineFinancialAdvisorIntelligence` avoids digit-prefix issue |
| Scaffolding-tool outputs uncommitted working-tree state (CHECKLIST.md stdout) | Portal-source-change agent-committed needs human review; tooling@opal.agent OK for org/projects/ but not portal/ |

### Open questions for Andrew (PRD §7)

| Q | Topic | CTO recommendation |
|---|---|---|
| Q1 | Lint gate ERROR-flip date | (c) Couple flip to SHARED.008 DEV smoke pass — objective evidence over calendar |
| Q2 | Asset class taxonomy authority — portal-only or DS-mirror? | Needs Andrew confirm; suspect portal-only |
| Q3 | Cottonwood scope in scaffolding validation | (b) synthetic `firm-test`; keep architectural validation clean from product onboarding |
| Q4 | Scaffolding tool auto-commit? | Uncommitted (human reviews CHECKLIST.md before commit) |
| **Q5** | **Migration overlap with active ADVI_INFTGT + ADVI_INFGRO** | **(c) split-Phase-1** — SHARED.001/004/005 first (low-conflict), feature waves ship, then SHARED.002/003/006/007. Load-bearing call. |
| Q6 | Component naming under partner dirs | (a) `{FirmName}AdvisorIntelligence` always — eliminates the two-pattern coexistence |
| Q7 | 49Financial canonical literal | KEEP `'49financial'` — see decision table above |

---

## RAVC closures this session

| RAVC | From → To | Subject | Hash / receipt |
|---|---|---|---|
| RAVC2 ack (incoming) | COO → CTO | Dashboard mirror pass recommendation | (broker, 21:25Z) |
| RAVC2 ack (outgoing) | CTO → COO | Dashboard mirror pass starting | `20260512T212851Z_..._RAVC2_ack__dashboard_mirror_pass_startin.md` |
| RAVC1 ack (incoming) | DT 0.4 → CTO | ADVI_SHARED PRD request | (broker, 21:32Z; brief `cd0847d1d`) |
| RAVC1 ack (outgoing) | CTO → DT 0.4 | ADVI_SHARED request acknowledged | `20260512T213258Z_..._RAVC1_ack__ADVI_SHARED_PRD_request_recei.md` |
| RAVC4 close (outgoing) | CTO → COO | Dashboard mirror pass LANDED `b6f6b0c9a` | `20260512T213403Z_..._RAVC-close__CTO_dashboard_mirror_pass_LA.md` |
| RAVC4 close (incoming) | COO → CTO | Bidirectional close confirmed | (broker, 21:30Z) |
| RAVC2 (outgoing) | CTO → COO | ADVI_SHARED PRD v0.1 SHIPPED `54c1ea270` ready for decomposition | `20260512T214331Z_..._RAVC2__ADVI_SHARED_PRD_v0.1_SHIPPED_54c1.md` |
| RAVC2 close (outgoing) | CTO → DT 0.4 | ADVI_SHARED PRD shipped; handed to COO | `20260512T214347Z_..._RAVC2_close__ADVI_SHARED_PRD_v0.1_SHIPPE.md` |

All loops closed. Zero standing CTO RAVC obligations at session end.

---

## Commits this session

| Hash | Author | Files | Substance |
|---|---|---|---|
| `b6f6b0c9a` | `1.0.0_SA_CTO` | `org/tier1_exec/1.0.0_SA_CTO/prompt.md` (1 file, +18/-15) | CTO dashboard mirror pass — reconcile against COO REGISTRY.md authoritative state |
| `54c1ea270` | `1.0.0_SA_CTO` | `docs/architecture/ADVI_SHARED.md` (new, 684 lines) + `org/projects/ADVI_SHARED.json` (new) + `org/projects/REGISTRY.md` (1 row added) | ADVI_SHARED PRD v0.1 + project registration |

Both pushed to CLOUD.

---

## Compiler Tools

| Tool | Command | Purpose | Result |
|---|---|---|---|
| comp-build | `comp-build` | Rebuild compiler-graph cache before §5 sweep | OK — 1590/1663 SHAs indexed |
| comp-blast | `comp-blast AdvisorIntelligence` | §5 — affected nodes for AdvisorIntelligence component | 3 endpoints + 1 Lambda (opal-partners-data) |
| comp-blast | `comp-blast useTenantLayout` | §5 — hook adoption surface | NO MATCH (hooks not graph nodes — logged as ADHC_COMPIL_V4 backlog) |
| comp-cache | `comp-cache collisions` | §5 — shared React Query keys | **4 collisions surfaced empirically** — drove §2.2 firmId namespace finding from theoretical → empirical bug |
| comp-transform | `comp-transform schema-check AdvisorIntelligence` | §5 — schema correctness | NOT FOUND (dispatcher, not leaf); deferred to TO-level Phase 1 mandates |

Compiler-tools-log row append: scheduled for next batch-commit (cycling on COO compiler-tools-log sweep cadence).

---

## Standing items at session end

1. **COO decomposition of ADVI_SHARED into 12 TOs** — pending COO bandwidth + §7 Q-triage decisions. CTO available for clarifications.
2. **§7 Q5 sequencing call** — COO arbitrates concurrent-overlap with ADVI_INFTGT P1/P2 + ADVI_INFGRO Stage 1 .005. CTO recommendation: (c) split-Phase-1.
3. **§7 Q2 asset class taxonomy authority** — needs Andrew confirm (portal-only vs DS-mirrored). Not blocking PRD ship; resolves at SHARED.001 TO authoring.
4. **ADVI_INFGRO Stage 1 dispatch state** — Andrew 3-decision pending (annualize basis / SV INTERNAL / ALPHA-vs-BETA) + DS bench routing (DS~A dead → DS~D STANDBY). Not CTO scope this session; COO arbitrates.
5. **7 memory entries** carried from session 20/21 — still queued; not landed this session (CTO focus was dashboard reconcile + new PRD). To pick up next session if Andrew not actively engaging.
6. **PRD INFGRO v0.4 amendment** — narrow C.3 + add C.6 — still queued. Not blocking; resolves at next ADVI_INFGRO PRD revision.

---

## Lessons captured for future sessions

1. **`comp-cache collisions` surfaces empirical bugs reliably.** This is the second session where comp-cache surfaced a real concrete bug (4 cache-key namespace divergences) that was framed as theoretical pre-tool. Pattern: run comp-cache early in any PRD touching React Query keys; it pays for itself.
2. **§6 pre-authoring repo check is cheap and self-protecting.** `test -f` + `git log -- <path>` runs in <1s and caught zero collisions this session — meaning the PRD authoring path was genuinely greenfield. Cheap insurance.
3. **Multi-layer namespace audits beat single-layer.** Brief said "firmId === 'inflection' inline" — actual code had 4 different firmId namespaces interacting + manual disambiguation everywhere. Audit revealed 22 inline branches, not "several." Take the time to grep each layer separately when the codebase has identifier-layering at all.
4. **Brief-to-PRD time was ~50min wall** — fast because (a) DT brief was excellent (saved ~2h of empirical investigation), (b) compiler tools surfaced bugs cheaply, (c) similar architecture existed (FIRMSEP gave structural pattern). Reference quality for future architectural PRDs.

---

## Session boundaries

- **Started:** ~21:25Z (Andrew direct via COO inbox)
- **Ended:** ~22:20Z (session log + handoff in chat to Andrew)
- **Wall time:** ~55min
- **Watcher:** inbox-watch fired twice (COO ACK then DT brief); both relaunched per protocol
- **Heartbeats:** 1 (post-PRD-ship; "ADVI_SHARED PRD v0.1 SHIPPED 54c1ea270")
