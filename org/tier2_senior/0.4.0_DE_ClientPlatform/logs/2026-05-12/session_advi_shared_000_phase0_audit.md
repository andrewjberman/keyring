# Session — ADVI_SHARED.000 Phase 0 multi-tenant audit

**Agent:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-12
**TO:** `ADVI_SHARED.000` (issued by `2.0.0_SA_COO`, commit `d2264361c`)
**Project:** ADVI_SHARED (PRD `54c1ea270` by 1.0.0_SA_CTO)
**Workspace CLOUD commits this session:** (audit doc + this log, see RAVC2 ledger)

---

## Scope

Single-pass comprehensive multi-tenant audit at `docs/briefs/ADVI_SHARED_AUDIT.md`. Output is the canonical migration matrix that Phase 1 TOs (SHARED.001 — SHARED.008) reference verbatim.

**Path note**: TO ADVI_SHARED.000 Requirement 1 + AC 1 originally directed output to `docs/architecture/ADVI_SHARED_AUDIT.md`. Final output at `docs/briefs/` per COO routing decision 2026-05-12 ~23:55Z (option A) — `.owned-paths.yaml` restricts `docs/architecture/**` to ANY_CTO and DE 0.4 is not in `permitted_agents`. Precedent: DS~D moved 49F gap-investigation doc `docs/briefs/data-scientist-49F-cert-gold-92m-gap-investigation.md` for the same reason (commit `b0d650be7`). Phase 1 TO `<references>` should use the `docs/briefs/` path. PRD §4.1 path reference is mildly stale; CTO can amend in PRD v0.2 if material.

Eight required sections per TO Requirement 1:
- §A firmId-conditional branch inventory
- §B per-firm component override inventory
- §C per-firm constants inventory
- §D cache-key collision resolution
- §E TenantLayoutConfig field-gap analysis
- §F lint warning enumeration
- §G firmId namespace literal census (4-layer)
- §H cross-project overlap risks

Plus PRD §3.2 supplement consolidating any gaps surfaced during the audit.

Audit is read-only on `portal/src/**` per TO Requirement 4.

---

## Work Completed

| Phase | Result |
|------|--------|
| Pre-write compiler-tool mandate (Phase 1) | All 4 steps run: `comp-build` PASS (1590/1663 nodes), `comp-cache collisions` PASS (4 matched PRD §5.2 exactly), `comp-transform schema-check InflectionAdvisorIntelligence` FAIL ("Component not found"), `comp-transform schema-check FortyNineFinancialAdvisorIntelligence` FAIL ("Component not found"). Both schema-check failures documented in §H.4 per TO `if_mismatch` directive; manual Grep used as workaround. |
| §A inventory | 32 firmId-conditional sites enumerated (PartnerAnalytics 15 worst-offender, AdvisorBookView 6, ClientsTab 6, AdvisorPublicProfile 1 helper, dispatcher 4 literals; 8 `'opal-capital'` internal-tier gates documented as out-of-scope) |
| §B inventory | 10 partner files classified. Key finding: Inflection ahead of 49F on migration path (INF has `_partners/inflection/layout.ts` extracted; 49F doesn't). |
| §C inventory | 19 constants/types across 4 partner files. 6 dead-code deletes + 13 layout migrations. Zero sentinel-keeps. |
| §D resolution | All 4 cache-key collisions resolve via SHARED.006 canonicalize-upstream. No `cacheKeyNamespace` field needed in TenantLayoutConfig. |
| §E field-gap | ~23 new nested fields proposed across 10 new top-level blocks (Identity, dataSources, tabs extensions, panels extension via §B supplement, assetClasses, roles, features, routes). Aggregate SHARED.001 sizing ~150-200 LOC type addition. |
| §F lint | 101 warnings in 21 files. Cat A 16 (PRD predicted ~75 — overcounted 5x), Cat B 9, Other 76 (PRD predicted ~15 — undercounted 5x). 75 in-scope, 26 out-of-scope. SHARED.007 subdivision (a/b/c/d) recommended for the Cat OTHER bucket. |
| §G census | L1=0 renames (canonical), L2=4 sites (1 file), L3=1 rename + 4 dead-code deletes, L4=1 table delete + 11 callsite simplifications. Total ~21 mechanical edits in 4 files for SHARED.006. |
| §H overlap | ADVI_INFGRO has 2 active DE TOs (`.005` + `.006`) with overlap on `AdvisorsTab.tsx` + `DistributionTab.tsx`. ADVI_INFTGT P1/P2 HOLD'd — zero overlap. SHARED.001 must land before INFGRO.006 to provide `features.gro.maxWindowCap.months`. |
| PRD §3.2 supplement | 1 new field (`panels.dataSourcePanel.overlay`) + 5 supplementary notes (SHARED.007 subdivision, lint framing correction, cross-pod coordination, `roles.composition` semantic move, comp-transform indexer gap). |
| Pre-commit Phase 2 mandate | `grep '<status>pending\|staged</status>'` = 0 matches PASS, `wc -l` = 711 lines (≥300 expected) PASS. |

---

## Mid-audit interrupt — Localhost radial regression hotfix

Mid-§B authoring, Andrew + RD 0.4.2 surfaced a localhost-only regression: Distribution-tab overview radial missing data in localhost dev; PROD `portal-v2.1.82` unaffected. Isolation revealed my `6f81d13a` BooksTab N1→useQuery migration (this morning) as the only diff between PROD and localhost.

Narrowing: `ClientsTab.tsx` changes affect only BooksTab (conditionally rendered, not mounted on default Distribution load) so cannot directly affect the radial. `AuthContext.tsx` Step 6 (Optional in my plan doc) upgraded the prefetch warm calls from fire-and-forget fetches to `queryClient.prefetchQuery` — adds 2 more concurrent prefetches alongside the existing 3 radial-feeding ones. **This was the suspect.**

Reverted just Step 6 as `ff54d611` (portal DEV) + `c741c0e81` (parent CLOUD gitlink bump by DT 0.4). Andrew confirmed at ~22:03Z: "its back now on localhost." Diagnosis confirmed.

COO filed follow-on RCA TO `prefetchquery-saturation-root-cause` (`576056e67`) — DT 0.4 primary, DE 0.4 backup, RD 0.4.2 helper, LOW priority. DT 0.4 raised an additional hypothesis at 23:30Z: firmOverride-namespace mismatch between prefetch call site and component mount → different RQ keys → no dedupe → second fetch races. If correct, SHARED.006 firmOverride canonicalization is the structural fix and Step 6 can re-introduce safely after.

Hotfix details:
- `ff54d611 fix(AuthContext): revert BooksTab prefetchQuery upgrade — localhost radial regression` (DE 0.4 author)
- Submodule pointer bumped `36b6854f → ff54d611` via `c741c0e81 chore(portal): bump submodule — revert AuthContext.tsx prefetchQuery upgrade (localhost radial regression hotfix)` (DT 0.4 author)
- PROD `portal-v2.1.82` unaffected. Andrew gates v2.1.83 cut.

Hotfix audit-relevance noted in §H.5 of `ADVI_SHARED_AUDIT.md` — `AuthContext.tsx` is in pre-prefetchQuery-upgrade state; don't re-do Step 6 until RCA resolves.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `docs/briefs/ADVI_SHARED_AUDIT.md` | NEW — 711-line comprehensive multi-tenant audit matrix (relocated from `docs/architecture/` per COO 23:55Z owned-paths routing) | Yes — CLOUD (this commit) |
| `org/tier2_senior/0.4.0_DE_ClientPlatform/logs/2026-05-12/session_advi_shared_000_phase0_audit.md` | NEW — this session log | Yes — CLOUD (this commit) |
| `portal/src/contexts/AuthContext.tsx` | Step 6 revert (mid-audit hotfix) — `queryClient.prefetchQuery` → fire-and-forget warm fetches | Yes — portal DEV `ff54d611` (separate commit during audit) |

---

## Compiler Tools

| Tool | When | Result | Notes vs `<expect>` |
|------|------|--------|---------|
| `comp-build` | Phase 1 (before-write) | PASS — 1590/1663 file-backed nodes indexed; graph 1852 nodes / 2013 edges in 9.2s | Matches PRD §5.2 expected node count |
| `comp-cache collisions` | Phase 1 | PASS — 4 collisions surfaced, identical to PRD §5.2 verbatim | No new collisions; no namespace-split needed |
| `comp-transform schema-check InflectionAdvisorIntelligence` | Phase 1 | FAIL — "Component not found" | TO `if_mismatch` directive followed: documented in §H.4, proceeded with manual Grep. Indexer uses filename-stem not exported-component-name. Filed under ADHC_COMPIL_V4 backlog. |
| `comp-transform schema-check FortyNineFinancialAdvisorIntelligence` | Phase 1 | FAIL — "Component not found" | Same as above. |
| `comp-transform schema-check ClientsTab` | Ad-hoc during §A | PASS — "All rendered fields match their response types" | Used as workaround for the BooksTab indexer gap. ADAPTER pattern documented in audit. |
| `comp-blast getPlatinumFirmDashboard` | Ad-hoc | INFO — 1 downstream (opal-partners-data Lambda) | Backend-only graph; portal consumers not represented |
| `comp-blast getPlatinumFirmMixSummary` | Ad-hoc | INFO — 1 downstream (opal-partners-data Lambda) | Same |
| `bun run lint` | §F population | INFO — 101 warnings in 21 files | Empirical category distribution vs PRD §2.4 framing recorded in §F.0 + §F.4 |
| `Grep firmId === / firmOverride === / isInflectionFirm` | §A population | INFO — 32 sites in scope, 8 internal-tier sites out-of-scope | Empirical census matches PRD §2.1 ~22-site expectation within rounding |
| `Grep '<status>pending\|staged</status>'` on audit doc | Phase 2 (before-commit) | PASS — 0 matches | Audit doc is a deliverable not a TO; no stray task-order tags |
| `wc -l` on audit doc | Phase 2 | PASS — 711 lines (≥300 expected) | Substantive document |

---

## Decisions Made

1. **Single-commit ship** — audit doc + session log bundled in one commit (not split). Rationale: session log is an explicit deliverable per TO Acceptance Criterion 7; both files have DE 0.4 author; same logical scope.
2. **No SHARED.001-.008 TO authoring this session** — that's the next-phase work, gated on (a) Andrew Q2/Q5 rulings + (b) COO RAVC4 closure on this audit. My output is the matrix; COO consumes it for Phase 1 decomposition.
3. **Mid-audit hotfix as separate commit** — `ff54d611` shipped to portal DEV during audit work, kept atomic and isolated from the audit doc commit. Per CLAUDE.md "One task order = one logical commit scope."
4. **PRD §2.4 lint-framing correction logged in supplement** — empirical Cat A/B/Other distribution differs 5x from PRD's framing. Documented as Supplement note 2 rather than re-litigating in the body; CTO can decide whether to amend PRD or treat as audit-finding evidence.

---

## Cross-context FYIs

- DT 0.4 RAVC4 closure noted at session start (Brief #9 49F gap shrunk $97M → $33M post-SCHWAB-BUCKDR; disclosure footnote refresh pending Andrew panel-walk).
- DS~D (now base lane) ACK'd Briefs #11 + #12 with sequencing question; clarified Brief #12 already shipped by DS~C as `56c1082bc`, Brief #11 stays open if base picks it up.
- DT 0.4 RCA TO `prefetchquery-saturation-root-cause` (`576056e67`) filed by COO during audit.
- BooksTab N1→useQuery migration `6f81d13a` retained (the actual bug fix DT QA'd); only the Optional Step 6 AuthContext piece reverted.
- COO mid-checkpoint ACK at 23:15Z accepted §3.2 supplement candidate + §B Inflection-ahead-of-49F finding + comp-transform indexer flag.

---

## Current State

| Item | Status |
|------|--------|
| Inbox | Empty (RAVC closures in flight) |
| Audit doc | `docs/briefs/ADVI_SHARED_AUDIT.md` 711 lines, all 8 sections + supplement complete |
| Portal DEV HEAD | `ff54d611` (post-hotfix) |
| Workspace CLOUD HEAD | `c741c0e81` (post-gitlink-bump; this session's audit commit will move it forward) |
| ADVI_SHARED.000 TO status | About to flip to `complete` on RAVC2 commit + COO RAVC4 spot-check |
| DE active work | Audit ship + RAVC2 to COO this turn |
| Watcher | LIVE |

---

## Next Steps

- [DE] Commit + RAVC2 to COO with hash + section coverage summary + wc -l
- [COO] RAVC4 spot-check §A and §D against portal/src tree per TO `ravc4_close` directive
- [COO] On RAVC4 close: unblock Phase 1 TO authoring (SHARED.001 type extension first)
- [CTO] Ratify the 1 PRD §3.2 supplement field + 5 supplement notes before SHARED.001 authors (per Requirement 3 + my supplement section)
- [Andrew] Q2 (asset class taxonomy authority) + Q5 (sequencing) rulings unlock SHARED.002 / .003 / .006 / .007 authoring
- [DT 0.4 backlog] RCA TO `prefetchquery-saturation-root-cause` when convenient (LOW priority; DT's firmOverride-mismatch hypothesis worth investigating first since SHARED.006 may be the structural fix)
- [DE next session] L2 useEffect migration in `ClientsTab.tsx:368-405` (same anti-pattern as BooksTab N1, gated on advisor drill; canonical template = today's BooksTab migration `6f81d13a`)
- [Andrew] Optional `portal-v2.1.83` cut decision (current portal DEV = `ff54d611` = clean candidate)
- [DS base / DS~C] Brief #11 (per-advisor mix_periods, `INF_D_04:3023` hardcoded `[]`) when chain regen settles
