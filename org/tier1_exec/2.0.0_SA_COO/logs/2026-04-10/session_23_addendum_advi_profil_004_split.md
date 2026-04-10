# COO Session 23 Addendum — ADVI_PROFIL .004 Split + Compiler Mandate Strengthened
**Date:** 2026-04-10
**Agent:** 2.0.0_SA_COO
**Scope:** Post-initial-decomposition correction driven by CTO compiler audit

---

## Summary

After shipping 8 ADVI_PROFIL task orders in commit 35499320, CTO ran the full compiler suite (comp-build/comp-blast/comp-routes/comp-cache/comp-transform) against the same dependency graph and caught three errors in my initial single-TO `.004.ae-advisor-scoping-enforcement`:

1. **Two CloudFront behaviors, two origins.** `/api/scoped/partners/*` hits `APIGateway-portal`; `/api/scoped/advisor-intelligence/*.json` is S3-direct via `S3-opal-data-bd`. The S3-direct paths can ONLY be scoped at `shared-advisor-router` Lambda@Edge — it's the only control point, not a style choice.
2. **`.004` is three TOs, not one.** Two of the four advisor endpoints key by `{accountId}` / `{relationshipId}`, not `{advisorId}`. A simple `jwt.advisorId == path[id]` rule does not cover the account-id or relationship-id paths — enforcement requires an advisor→{accounts, relationships} ownership map joined at request time.
3. **`getPlatinumAdvisorSummary` and `getPlatinumAdvisorDrilldownSummary` hit the same URL.** Two TS wrappers extracting different shapes from one backend response. One scoping rule covers both; I was about to write it as two TOs' worth of work.

CTO updated the PRD §4/§5/§8 with the compiler-verified route map, blast radii, cache collision scan, schema coverage, and a full Compiler Tools authoritative evidence block (12 tool runs logged). CTO also created a feedback memory `feedback_cto_compiler_mandatory_before_prd.md` for the PRD layer.

## Root cause of my error

I transcribed the scoping rule from RD briefing §5.2 text without running `comp-routes trace` on the four endpoints myself. The RD briefing is a good architectural overview but it did not catch the two-CloudFront-behavior split or the path-key type mix — because the RD didn't run the compilers either (briefing §9 notes `comp-transform schema-check` was "not run this session").

I had full compiler access. I should have run `comp-routes` on all four advisor endpoints + `comp-blast ClientsTab.tsx` as the first step of decomposition, not the last. The RD briefing + CTO PRD text combined to give me a confident-sounding but wrong mental model, and I skipped verification.

Cost of the error: one rewritten commit, plus wasted mental model in the downstream wave. If CTO had not caught this before GO, Wave 2 would have shipped with `.004` enforcing scoping on only 2 of the 4 endpoints, leaving account-id and relationship-id paths unscoped (the exact defense-in-depth hole the project exists to close).

## Corrections landed

### 1. `.004` split into `.004a`, `.004b`, `.004c`

**`.004a ae-advisor-id-scoping-edge`** (0.7.0_AE_CloudOps) — Wave 2a. Simple advisor-id compare for the two endpoints where the path parameter IS an advisorId:
- `/api/scoped/partners/books/advisor/{advisorId}/platinum-summary` (API GW origin; covers BOTH `getPlatinumAdvisorSummary` and `getPlatinumAdvisorDrilldownSummary` — same URL, two wrappers)
- `/api/scoped/advisor-intelligence/platinum/advisors/{advisorId}/timeseries.json` (S3-direct origin)

Ships independently of `.004b`/`.004c` and unblocks the non-admin Profile+Timeseries surface — the core ADVI_PROFIL value.

**`.004b ds-client-account-ownership-map`** (0.4.0_DS_ClientPlatform) — Wave 2b. DS publishes `platinum/shared/advisor_ownership.json` (schema_version 1, frozen) via a new step appended to D_00 (or D_04 per comp-pipescript analysis). Map shape: `{schema_version, generated_at, advisors: {advisor_id: {accounts: [], relationships: []}}}`. Size target <1 MB uncompressed. Refreshed on every gold run.

**`.004c ae-account-client-scoping-edge`** (0.7.0_AE_CloudOps) — Wave 2c. Extends the .004a helper with ownership-map lookup for the two harder endpoints:
- `/api/scoped/advisor-intelligence/platinum/accounts/{accountId}/summary.json` (S3-direct)
- `/api/scoped/partners/books/relationship/{relationshipId}/platinum-summary` (API GW)

Blocks on `.004a` (shared helper exists) + `.004b` (ownership map populated on S3).

### 2. `.005` acceptance criterion added

`comp-transform schema-check` on the extracted L3/L4 components (`AdvisorBookClientDetail` and `AdvisorBookAccountDetail`) must be re-run after the lift. CTO noted in PRD §5.4 that `AdvisorBookView`'s 17 type fields flow through panels where 12 are unused at the top level — the schema coverage check must happen at the extracted component level, not only the parent.

### 3. COO prompt.md compiler mandate strengthened

New "Compiler Tools — MANDATORY" section at the top of `org/tier1_exec/2.0.0_SA_COO/prompt.md`. Explicitly requires comp-routes / comp-blast / comp-cache / comp-transform runs BEFORE writing any task order whose scope touches routes, shared files, cache keys, or schemas. Includes a minimum-required-runs matrix by TO type. Explicit callout that transcribing from briefings is a quality failure.

### 4. Feedback memory

`memory/feedback_coo_compiler_mandatory_before_task_orders.md` created. Indexed in `MEMORY.md` under the Feedback section adjacent to the CTO equivalent. Documents the incident, the corrective rule, and the how-to-apply guidance for future sessions.

### 5. Compiler log entry

Appended a SKIPPED / FAIL row to `org/compiler-tools-log.md` for this session, self-reporting that I did not run comp-routes at TO-writing time and documenting the corrective.

### 6. ADVI_PROFIL.json updated

Phase description reflects the 8→10 TO count, the .004 split rationale, and the CTO compiler audit attribution. Blocking section updated with the new wave structure.

### 7. COO dashboard row in prompt.md

Updated to show 10 TOs across 4 waves including the .004a/.004b/.004c split.

## TO inventory after split

| TO | Owner | Wave | Blocks on | Status |
|----|-------|------|-----------|--------|
| `.001` dt-ship-rd-portal-rewrite | 0.4.0_DT | 1 | — | staged |
| `.002` dt-jwt-advisor-claim | 0.4.0_DT + 0.7.0_AE | 1 | — | staged |
| `.003` ds-book-tax-exposure | 0.4.0_DS | 1 | — | staged |
| `.004a` ae-advisor-id-scoping-edge | 0.7.0_AE + 0.4.0_DT | 2a | .002 | staged |
| `.004b` ds-client-account-ownership-map | 0.4.0_DS + 0.7.0_AE | 2b | — (parallel with W1) | staged |
| `.004c` ae-account-client-scoping-edge | 0.7.0_AE + 0.4.0_DT | 2c | .004a + .004b (map populated) | staged |
| `.005` rd-client-drilldown-lift | 0.4.2_RD | 3 | .001 | staged (schema-check criterion added) |
| `.006` rd-client-cache-policy | 0.4.2_RD | 3 | .001 + Andrew decision | staged |
| `.007` rd-admin-my-profile-toggle | 0.4.2_RD | 4 | .002 | staged |
| `.008` de-frontend-dev-visual-test | 0.4.0_DE | 4 | .001 + Andrew dev server | staged |

10 total TOs. Wave 1 + Wave 2b can GO in parallel immediately (4 TOs); 2a gated on .002; 2c gated on 2a + 2b; Wave 3/4 on .001/.002.

## Files touched in this addendum

- DELETED: `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_PROFIL.004.ae-advisor-scoping-enforcement.md`
- CREATED: `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_PROFIL.004a.ae-advisor-id-scoping-edge.md`
- CREATED: `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_PROFIL.004b.ds-client-account-ownership-map.md`
- CREATED: `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADVI_PROFIL.004c.ae-account-client-scoping-edge.md`
- MODIFIED: `org/tier2_senior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_PROFIL.005.rd-client-drilldown-lift.md` (acceptance criterion 7b added)
- MODIFIED: `org/tier1_exec/2.0.0_SA_COO/prompt.md` (Compiler Tools MANDATORY section + dashboard row update)
- MODIFIED: `org/projects/ADVI_PROFIL.json` (phase/blocking updated to 10 TOs)
- APPENDED: `org/compiler-tools-log.md` (COO SKIPPED entry)
- CREATED: `memory/feedback_coo_compiler_mandatory_before_task_orders.md`
- MODIFIED: `memory/MEMORY.md` (added index line)
- CREATED: this addendum

## Next steps

1. Commit this addendum batch (`--author=2.0.0_SA_COO`).
2. Await Andrew GO for Wave 1 + Wave 2b parallel kickoff. Wave 1 = .001/.002/.003; Wave 2b = .004b.
3. Open questions to Andrew before Wave 1 fires:
   - .001 commit bundling: three-way split or single commit? (currently DT's call)
   - Non-admin L3/L4 drill scope for .005: assumed yes, confirm?
   - .007 cut or ship as Wave 4 polish?
   - .006 cache policy a/b/c (can defer until Wave 3).
4. Going forward: every COO TO-authoring session starts with comp-routes / comp-blast / comp-cache / comp-transform runs on the relevant endpoints and files. Log every run. No exceptions.
