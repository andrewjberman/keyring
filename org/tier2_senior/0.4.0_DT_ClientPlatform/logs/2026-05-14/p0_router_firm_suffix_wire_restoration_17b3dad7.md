# DT Session — P0 Phase 2: ROUTER_FIRM_SUFFIX wire-restoration (17b3dad7) + SHARED.005/.007a co-bundle

**Author:** 0.4.0_DT_ClientPlatform
**Date:** 2026-05-14
**Driver:** Andrew empirical 500s post-Phase-1 → CTO/COO routing → DE second-commit + bundle push
**Duration:** ~14:41Z – 14:57Z (~16min wall, incl. ~10min CTO/COO routing-thrash + DE 29-callsite scope expansion)

---

## Current State

**P0 fully CLOSED. Two forward-fix commits LIVE on portal DEV; SHARED.005 + SHARED.007a co-bundled clean.**

- Portal DEV: `17b3dad7` (`8b71292f..17b3dad7` pushed this turn)
- Parent CLOUD: `94e523a4f` (`64e583272..94e523a4f` pushed; DE's submodule pointer bump)
- Both refs zero-diff vs origin
- Submodule pointer `portal` = `17b3dad7` (matches portal DEV HEAD)
- CW 5xx/4xx baseline 0% pre-Andrew-smoke; awaiting post-smoke re-pull for the empirical 5xx→0% transition signal CTO requested

---

## Incident Continuation Timeline (Phase 2)

Phase 1 (AuthContext.tsx:35 hotfix) was the previous session log: `p0_authcontext_audit_gap_fix_forward_8b71292f.md`. Phase 2 picks up immediately after that push landed.

| Time (Z) | Event |
|---|---|
| ~14:39 | Phase 1 push `d9882117..8b71292f` LIVE on portal DEV |
| ~14:41 | **Andrew empirical post-Phase-1 dev-smoke:** `?firm=49financial` endpoints returning **500** (not 401 anymore). Evidence: `platinum/firm/leaderboard.json?firm=49financial → 500` + `platinum/firm/cohort_a_summary.json?firm=49financial → 500`. AuthContext fix unblocked `getClientsTab` (`?firmId=` path) but 8+ `?firm=` callsites still broken. |
| ~14:42 | CTO PAUSE message arrived (~3min late vs Phase 1 push) — would have wanted both commits bundled to avoid partial recovery. Timing collision surfaced to CTO + COO. |
| ~14:43 | COO URGENT MCP: prepare full SHARED.006 revert (Commits A+B+C+D + AuthContext follow-on). HOLD execute until DE empirical confirm. Destructive-op authorization implied but not granted. |
| ~14:43 | DT prepped 5-commit revert dry-run (A+B+C+D + `8b71292f`). Surfaced CTO/COO conflict to CTO for ratify — forward-fix (Option A) vs full-revert (Path B). |
| ~14:44 | COO RETRACTED revert ask (concur with my FYI Option 1+3). Forward-fix path ratified. Revert dry-run archived. |
| ~14:45 | CTO P0 RE-CONFIRMED: empirical 500s vindicate my FIRST diagnostic (8 `?firm=` callsites broken). Retrospective walk-back was wrong. Option A standard non-destructive push when DE ships ROUTER_FIRM_SUFFIX. |
| ~14:46 | RD 0.4.2 ships `b2808fa3` SHARED.007a dead-code sweep (-566 LOC; pure deletion; lint 86→85). Bundled into next-push queue. |
| ~14:54 | DE ships `17b3dad7` (P0 ROUTER_FIRM_SUFFIX inverse map). Scope: 29 callsites (3.5x my original 8-callsite enumeration; broader portal-wide grep caught all `?firm=${firmOverride}` instances via single `bucketSuffix()` helper). |
| ~14:55 | DT typecheck (with cache reset) PASS on HEAD `17b3dad7`. |
| ~14:56 | DT push: `git push origin DEV` `8b71292f..17b3dad7`. Bundle = `b2808fa3` + `17b3dad7`. Parent CLOUD push: `64e583272..94e523a4f` (DE's submodule pointer bump + intervening commits). |
| ~14:56 | CW 5xx + 4xx baseline pull — 0% in last 15min window. |
| ~14:57 | RAVC2 CLOSE to CTO + COO + DE + RD with push hashes + retrospective lessons banked. |

---

## Wire-Protocol Divergence Root Cause (full)

The full incident was a two-tier wire-protocol divergence between portal-frontend canonical literals and data-layer-Lambda expectations. Pre-SHARED.006, the portal kept BOTH forms simultaneously: a portal-internal `firmOverride` in short-form (`'bd'`/`'inf'`) plus per-callsite translation at the api-endpoint layer via `LAMBDA_FIRM_ID` map. Two distinct wire payloads coexisted at adjacent callsites:

| Wire path | Pre-SHARED.006 form | Consumer | Why |
|---|---|---|---|
| `?firmId=` | `inflection`, `49financial` (canonical-long-form, mapped) | opal-partners-data Lambda (DDB partition key lookup) | DDB partition keys are full-form for portal-staffed admins |
| `?firm=` | `inf`, `bd` (short-form, direct) | shared-advisor-router Lambda@Edge → `opal-data-${firmParam}` S3 bucket suffix | bucket suffixes are short |

SHARED.006 Commits A+B canonicalized the portal-internal namespace to long-form (`'inflection'`/`'49financial'`). Commit C deleted the `LAMBDA_FIRM_ID` map (now identity for `?firmId=` callsites). Commit D folded helper functions + Cottonwood readiness gate.

**The architecture-level correctness:** portal-internal namespace was unified onto a single canonical form ✓. **The wire-correctness gap:** the 29 `?firm=` callsites that previously sent short-form to the S3 router now send long-form, but the router (and downstream data layer) still expect short-form bucket suffixes. The 8 `?firm=` callsites I enumerated in the initial diagnostic were a SUBSET of the actual 29 (my regex `firmOverride.*=.*'(inf|bd)'`-grade was too narrow; missed template-literal interpolations + URLSearchParams object values + nested assignments).

Additionally, `AuthContext.tsx:35` had a hardcoded `firmOverride='bd'` outside the audit §G scope (lived in `src/contexts/`, not `src/pages/AdvisorIntelligence/`); pre-Commit-C the `LAMBDA_FIRM_ID` map translated `'bd' → '49financial'` on every Lambda request, masking the unmapped-consumer bug. Post-Commit-C the api passed `'bd'` raw to Lambda → 401 on `getClientsTab`. Phase 1 (`8b71292f`) fixed this; Phase 2 (`17b3dad7`) fixed the 29 `?firm=` callsites.

**The forward-fix architectural pattern:**
- Portal-internal: canonical form (SHARED.006 win preserved)
- Wire boundary (S3 router path): `bucketSuffix()` helper translates canonical → short-form at the 29 callsites
- Wire boundary (Lambda DDB path `?firmId=`): canonical passthrough (no translation; matches DDB partition key form)
- Data layer: unchanged (already accepts short-form for `?firm=`)

This is the two-tier translation pattern CTO formalized as the correct architectural shape: bidirectional translators where wire-boundary consumers diverge from internal canonical, with per-callsite explicit translation maps.

---

## Diagnostic Retrospective — What I Got Right, Wrong, and Banked

### Got right (first pass)

1. **`?firm=` vs `?firmId=` two-pattern hypothesis** — DT diagnostic at 14:36Z correctly identified the wire-protocol divergence mechanism: pre-SHARED.006 had TWO distinct query patterns with DIFFERENT expected wire forms, and the 8 `?firm=` S3-router callsites would 500/404 under canonical-form input.
2. **L75 comment as smoking-gun documentation** — found and surfaced the original code's own documentation of the dual-pattern requirement.
3. **`comp-routes behaviors` for CF custom_error_response** — surfaced the `HTTP 403 → 200 /index.html` masking mechanism explaining the JSON.parse symptom.
4. **`aws s3 ls` for ground-truth bucket names** — verified `opal-data-bd` + `opal-data-inf` exist; `opal-data-49financial` + `opal-data-inflection` don't.
5. **Two rollback paths prepped (Path 1 surgical, Path 2 full revert) at 14:34Z** — armed for fast execution when DE verdict landed.

### Got wrong (retrospective walk-back)

1. **Retrospective claim "the 8 `?firm=` callsites were actually FINE because their input firmOverride came from canonicalized-by-A+B sources"** at 14:40Z. This was a re-read of the canonicalization logic without new empirical evidence. The reasoning was: "PARTNER_VIEWS + claims.firmId + Select Partner dropdown all canonical post-A+B → `?firm=${firmOverride}` sends canonical to router → can the router handle canonical?" — and I leaned toward "yes" based on `FIRM_CONFIG[firmId]?.bucket` lookup at router L199. But the partner-firm path uses FIRM_CONFIG (canonical-keyed) while the opal-capital-staff path uses `opal-data-${firmParam}` (suffix-construction). My re-read collapsed those two paths.

2. **DE's broader 29-callsite scope vs my narrow 8** — my initial enumeration was a VALUE-literal regex search (`firmOverride.*=.*'(inf|bd)'`) which finds assignments and comparisons but misses template-literal interpolations + URLSearchParams object values + nested helper-function calls. DE's broader `git grep "?firm=\${firmOverride}"` portal-wide caught all 29 instances via single uniform pattern. Two different audit grep shapes catch different surface classes (banking via DE's `feedback_audit_grep_scope_completeness.md` memory entry).

### Banked but didn't matter (this incident)

The 8-callsite list I initially flagged was a CORRECT-MECHANISM-WRONG-SCOPE diagnostic. The mechanism (wire-form mismatch at `?firm=` callsites) was right; the scope (8 vs 29) was narrow. Banking under "mechanism-correct, scope-wrong" — useful for ruling-in/ruling-out but not sufficient on its own. Future canonicalization audits should run BOTH grep shapes (value-literal + pattern-template).

### MCP-ordering hazard (own observation)

CTO message sequence (1) standby (2) push immediately (3) PAUSE arrived in that order, but #2→#3 collapsed under "Andrew is waiting" urgency. DT executed #2 before #3 arrived (~3min collision window). CTO owned the routing failure on their side too in their RAVC4 message: "Push pauses should be issued BEFORE the FIX-FORWARD ratify if downstream second-commit dependency exists, not after." My corresponding lesson: under critical-path P0 time pressure, prefer "hold for double-confirm" on time-pressure pushes when a downstream-second-commit dependency exists upstream of the current commit — even when prior signal said "push immediately."

---

## Quality Gate Decisions

**Cache-reset typecheck discipline** (from RD 0.4.2's `74a29229` retrospective): `rm -rf node_modules/.vite node_modules/.tmp tsconfig.tsbuildinfo` before `bun run typecheck`. Applied this turn; 0 errors on HEAD `17b3dad7` cleanly.

**P0 time-pressure flex on separate build + lint gates** (COO RAVC2 ratified): skipping `bun run build` and `bun run lint` separate runs was acceptable here — tsc clean + DE local-verify covered the failure surface. Lint stays at ~85 (SHARED.007a closed 1 warning; SHARED.007b/c/d remaining for next session). **Banking the discipline:** "P0 push under demo-time-pressure can flex separate-build/lint gates if tsc passes AND authoring engineer verified locally; restore full-gates for non-P0 pushes."

**No tag cut + no PROD push** — DEV ship only. PROD remains at `portal-v2.1.86` (`38dfc4979`). Andrew-gated for promotion.

**Force-with-lease envelope unused** — destructive op authorization went unrequested (Path B revert never executed). Standard non-destructive `git push origin DEV` throughout both P0 phases.

---

## Bundle Inventory — Phase 2 Co-Bundle

| # | SHA | Author | Subject |
|---|-----|--------|---------|
| 1 | `b2808fa3` | RD 0.4.2 | SHARED.007a Cat A dead-code sweep — `_partners/{49f,inf}/constants.ts` dead-code + `_shared/AdvisorPublicProfile.tsx` 482-LOC dead `TimeSeriesPanel` + 11 unused imports + 11 dead helpers + 2 dead useMemos (3 files / +39/-605 LOC; lint 86→85) |
| 2 | `17b3dad7` | DE 0.4 | P0 ROUTER_FIRM_SUFFIX inverse map — `?firm=` S3-bucket-suffix wire-protocol fix (29 callsites via single `bucketSuffix()` helper) |

Parent CLOUD intervening commits since my last bump (cleaning up the timeline):
- `9766b6956` (DE) submodule bump to `8b71292f`
- `cabf3d01d` (AE 0.6.1) docs(inf-pipeline) brief §4.3+§4.6 expansions
- `b970c3ebb` (DT) log: P0 AuthContext fix-forward retrospective (Phase 1 log)
- `a4a4fd0b2` (??) intervening
- `0090b3be1` (COO) closure SHARED.004+.006 status flip
- `64e583272` (??) intervening
- `94e523a4f` (DE) submodule bump to `17b3dad7`

---

## Compiler Tools

| Tool | Result | What it caught / drove |
|------|--------|------------------------|
| `bun run typecheck` (cache-reset) on HEAD `17b3dad7` | 0 errors | Pre-push canonical gate. Cache-reset discipline (rm -rf node_modules/.vite + .tmp + tsconfig.tsbuildinfo) preserves diagnostic fidelity per RD's `74a29229` post-mortem lesson. |
| `comp-routes behaviors` | Confirmed CF custom_error_response `HTTP 403/404 → 200 /index.html` masking mechanism | Explained JSON.parse symptom; surfaced to CTO + DE during diagnostic phase. |
| `comp-routes trace getClientsTab` | Resolved URL `/api/scoped/advisor-intelligence/clients-tab?firmId={param}` + API Gateway routing + auth-validator-edge viewer-request | Confirmed `?firmId=` (Lambda DDB) vs `?firm=` (S3 router) two-pattern routing. |
| `aws s3 ls | grep opal-data-` | Listed `opal-data-bd`, `opal-data-inf` (real); `opal-data-49financial`, `opal-data-inflection` (don't exist) | Ground-truth confirmation that canonical-form `firmParam` would 404 in opal-capital-staff bucket-construction path. |
| `aws cloudwatch get-metric-statistics` (4xx + 5xx rates on EVTSA9VEHNZVH last 15min, 1-min period) | Baseline 0% across all sample points | Pre-push CW baseline; awaiting post-Andrew-smoke re-pull for empirical 5xx→0% transition signal CTO requested. |
| `git log -L 125,135:portal/src/.../FeeEfficiencyPanel.tsx` (previous P0 phase) | Pinpointed SHARED.004 broken-import commit `2057099c` | Single-commit blame for typecheck regression; led to RD 0.4.2's `74a29229` 1-line fix. |
| `grep -rn "firm" infra/aws/lambda-edge/shared-advisor-router/index.mjs` | Confirmed bucket-construction L186-198 (opal-capital-staff path) vs FIRM_CONFIG lookup L199-200 (partner-firm path) | Distinguished the two router paths handling Andrew's internal-staff vs partner-user flows. |

Compiler-tools-log entries auto-appended via `.comp-graph/.agent_context` for any comp-* tool invocations.

---

## Verification

**Portal DEV remote state at session end:**
- `git ls-remote origin DEV` -> `17b3dad73dfe64adb39c3ca25ac751cb9d2f2769`
- Local `DEV` rev-parse identical
- Zero-diff

**Parent CLOUD remote state at session end:**
- `git ls-remote origin CLOUD` -> `94e523a4f29e6bb94c5351183e09db1faf1f85b3`
- Local HEAD rev-parse identical
- Submodule pointer `portal` = `17b3dad7`
- Zero-diff

**CW 5xx + 4xx baseline at push completion:** 0% across all 1-min sample points in the last 15min window. Pre-Andrew-smoke baseline. Post-smoke re-pull pending.

**Andrew dev-smoke unblocked** — both wire paths fixed:
- `?firmId=` (Lambda DDB partition-key): AuthContext.tsx:35 `'bd' → '49financial'` ensures canonical-form passthrough at the unmapped-consumer surface
- `?firm=` (S3 bucket-suffix via shared-advisor-router): `bucketSuffix()` helper translates canonical → short-form at 29 callsites in api/endpoints/advisor-intelligence.ts

---

## Banking — 4 Structural Lessons (COO + CTO ratified)

1. **RAVC1 reviewer protocol delta** — Lambda-boundary-touching refactors require broader-than-commit-scope grep at L4 cross-domain review. Two grep shapes mandatory: (a) VALUE-literal grep (`firmOverride.*=.*'(inf|bd)'`-grade) for direct comparisons + (b) PATTERN/template grep (`firm=${firmOverride}`-grade) for interpolations. Plus `aws s3 ls + aws dynamodb scan` for data-layer canonical-form verify. (Joins DE's §3.X.1 audit-grep-scope-completeness memory entry.)

2. **Retrospective walk-back discipline** — when offering a "retrospective walk-back" of a prior diagnostic, support with new empirical evidence (not re-read of same code). Re-reads can produce false-confidence flips; only empirical signals (network tab, CW metrics, S3/DDB inspection) resolve diagnostic divergence. (CTO meta-rule from this incident.)

3. **MCP-ordering hazard during P0** — under critical-path P0 time pressure, the natural "re-read diagnostic before next push" loop can get collapsed by urgency signals. Push pauses should be issued BEFORE the FIX-FORWARD ratify if downstream second-commit dependency exists, not after. From DT execution lane: prefer "hold for double-confirm" on time-pressure pushes when downstream second-commit dependency exists upstream of the current commit. Plus COO's reciprocal: "verify CTO+COO converged BEFORE destructive-op-class action asks." (Both sides of the routing-thrash own a discipline lesson.)

4. **Two-tier translation pattern** — canonical-internal + wire-boundary-translator IS the correct architectural shape for multi-tenant canonicalization PRDs touching boundary surfaces with divergent expectations. Future PRDs touching firmId (or any equivalent multi-tenant identifier) enumerate per-boundary expectation and ship the appropriate translator alongside the canonicalization. Translators are scoped to specific consumer paths (S3-router suffix vs Lambda DDB partition vs JWT claim vs etc.). (CTO architectural ruling banked for §3.X.3 canonicalization PRD template.)

5. **(Quality-gate flex banked by COO RAVC2 acceptance):** P0 push under demo-time-pressure can flex separate-build/lint gates if tsc passes AND authoring engineer verified locally; restore full-gates for non-P0 pushes.

---

## Deployment Tags

| Pipeline | Tag | Commit | Notes |
|---|---|---|---|
| portal (PROD baseline) | `portal-v2.1.86` | `38dfc4979` | unchanged this session |
| (next PROD candidate) | `portal-v2.1.87` candidate | `17b3dad7` | NOT cut — Andrew-gated; +20 commits over v2.1.86 (16 morning bundle + SHARED.005 + 2 P0 forward-fix commits + SHARED.007a + intermediate) |
| (parent CLOUD) | no tag | `94e523a4f` | DT does not tag interim-state-only commits |

---

## Next Steps

- [Andrew] Resume dev-smoke against `17b3dad7`. Validate getClientsTab + 8 `?firm=` endpoints (header_metrics, cumulative_chart, timeseries_overview, partner_analytics, platinum_cumulative_chart, inflec_timeseries_chart, firm_mix_views, books_composition + 21 other ROUTER_FIRM_SUFFIX-translated callsites) all return 200s. Then INFFIN v0.1 close validation.
- [DT 0.4] Post-Andrew-smoke CW 5xx + 4xx re-pull for empirical 5xx→0% transition signal. Surface to CTO + COO as RAVC corroboration of the wire-restoration fix.
- [Andrew/CTO] PROD-promote signal on `portal-v2.1.87` cut when dev-smoke fully clears + chain #131842 recovery wrap (gold-d ETA per AE 0.6.1).
- [CTO] Post-mortem write-up: 4 structural lessons banked + §3.X canonicalization PRD template draft.
- [COO] Add §3.X canonicalization PRD template to `org/standards/` when CTO draft lands.
- [RD 0.4.2] SHARED.007b/c/d follow-on lint sweep + .008 close gate (next session per COO).
- [DE 0.4] SHARED.008 DT+RD Phase 1 close gate co-author per ADVI_SHARED §6.2.
- [DT 0.4] Standing by for SHARED Phase 2/3 dispatch + FIRMSEP.10 Cottonwood frontend wiring (post-CTO architectural call on own-pipeline vs shared-multi-tenant).
