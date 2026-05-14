# `comp-types index <Type>` — proposed tool brief

**Author:** 0.4.0_DE_ClientPlatform
**Date:** 2026-05-14
**Audience:** 1.0.0_SA_CTO (backlog candidate; not a TO yet)
**Filing:** ADHC_COMPIL_V4 v0.4 ratchet candidate (post v0.3 full-corpus retrospective)
**Status:** Brief — for CTO review

---

## Motivation

`comp-transform schema-check` and `comp-blast` walk the **component graph** (file → JSX render tree → imported types). Both tools return "Component not found" / "No nodes matching" when invoked against a pure **type-module identifier** — a TypeScript `interface` / `type` / `const` declared in a `.ts` file with no JSX export. This is a recurring gap during type-foundation work:

- **ADVI_SHARED.001 (2026-05-14, this author):** `comp-transform schema-check TenantLayoutConfig` returned "Component not found"; `comp-blast TenantLayoutConfig` returned "No nodes matching" (1887-node graph, 2061 edges). Per ADVI_SHARED.md PRD §5.2 + the TO `if_mismatch` directive, I proceeded with manual grep enumeration of `useTenantLayout` consumers — 29 firmId-conditional sites vs the 32 cited in the audit (3-site drift attributable to INFFIN cross-firm consolidation absorbing sites between audit ship + TO start). Manual enumeration worked but cost ~10 minutes of grep + cross-check that a single-invocation tool would have saved.
- **CTO session 23 Class-D adapter audit (per CTO 2026-05-14 RAVC4 reply):** also hit type-module indexing gaps during the corpus retrospective.
- **`comp-transform schema-check AdvisorsTab` complement:** does resolve types via `../types.ts` shared module (post-TO-11 robustness fix), but the resolution is *component → type*, not the inverse *type → consumers*.

The gap is structural: the graph builder only indexes nodes that have inbound edges from `getX()` / `useX()` / JSX call-sites. Pure type modules have downstream consumers but no inbound edges in the component-graph sense, so they're invisible to discovery.

---

## CLI shape sketch (3-5 bullets)

- **`comp-types index <TypeName>`** — primary mode. Output (markdown table):
  - `Consumers` — all `useTenantLayout` / `getX().{field}` / TypeScript `import { TypeName }` sites, file:line, kind (read / mutation / re-export).
  - `Mutations` — sites that produce values of the type (e.g., `INFLECTION_LAYOUT: TenantLayoutConfig = {...}` declarations + `DEFAULT_LAYOUT`).
  - `Exported alias chains` — `export type X = TypeName` re-exports; useful for finding deprecation gaps.
  - `Default-fallback sites` — call sites that read with a default (`?? DEFAULT_LAYOUT`, `?? false`), which are the "silent drift" risk for newly-added optional fields.

- **`comp-types blast <TypeName>`** — secondary mode. Equivalent to `comp-blast` but for type identifiers. Output: full transitive consumer set. Useful pre-PRD-decompose check (would have produced the 4-consumer set the ADVI_SHARED.001 audit §A enumerated, in one call).

- **`comp-types fields <TypeName>`** — tertiary mode. Lists every declared field with the call-sites that read each field. Distinguishes UNUSED vs USED-on-some-paths vs READ-everywhere. Crystallizes the "which fields can I safely deprecate" question.

- **`--severity` flag** — match ADHC_COMPIL_V4 v0.2 TO-11 convention: INFO (resolved with degradation) / WARN (suspected gap) / ERROR (confirmed gap). Triage at a glance.

- **`--firm-conditional-sites` flag** — co-search for `firmOverride === 'X'` / `isInflectionFirm` / `firmId === 'inflection'` co-located with the type's call-sites. Direct support for the multi-tenant audit pattern that drove ADVI_SHARED Phase 0 §A (32-site baseline) and §E (8-block shopping list). Would have produced the 29-vs-32 drift number in one call.

---

## ADHC_COMPIL_V4 reference + filing recommendation

The ADHC_COMPIL_V4 PRD already documents the limitation surface implicitly via TO-11 ("comp-transform schema-check robustness"), but TO-11 scope is **component-side** robustness (handler-local-param false-positives + missing co-located types.ts graceful fallback). The type-graph walker is a different shape of work: TO-11 makes `comp-transform schema-check Component --feature token` reliable when the COMPONENT exists; `comp-types` makes the inverse query (`schema-check Type` to find consumers) possible at all.

Filing recommendation:

- **v0.4 ratchet candidate** (no urgency). The PRD ratcheted from v0.1 (7 TOs) → v0.2 (11 TOs) → v0.3 (full-corpus 5-item retrospective). A v0.4 batch covering type-graph queries would be natural.
- **One TO, single new tool** (`comp-types` with 3 subcommands `index` / `blast` / `fields`). Effort estimate ~1-1.5d for the tool author (likely 0.7.0_AE_CloudOps per existing comp-* tool ownership pattern).
- **Corpus already exists** — ADVI_SHARED Phase 0 audit (§A 32-site baseline + §E 8-block shopping list) + CTO session 23 Class-D adapter audit are the two named instances. A v0.4 §5 Compiler Evidence row would cite both as the motivating cases.

Pre-empts:
- ADHC_COMPIL_V4 TO-3 (`comp-constants`) is a precursor — it also indexes pure non-JSX exports (constants) and shares the AST-walker scaffolding. `comp-types` reuses that scaffolding rather than building a parallel TS-AST traversal.
- TO-11 (schema-check robustness) is orthogonal; not a blocker, not a duplicate.

---

## Out of scope for this brief

- Concrete tool implementation. Brief is type-graph scoping, not design spec.
- Cross-language type indexing (Python data-emit dataclasses, etc.). TS-only is the immediate need; Python type-graph indexing is a separate question deferred per ADHC_COMPIL_V4 §9 out-of-scope conventions.
- Auto-fix capabilities. Pure read-only diagnostic per existing comp-* tool convention.

---

## What's next

- CTO decides v0.4 ratchet timing (no urgency per 2026-05-14 ACK).
- If ratcheted, this brief becomes the §5 Compiler Evidence row (corpus + tool design pointer).
- If not ratcheted, the brief stands as a captured-context artifact for whenever the next type-graph manual-fallback incident surfaces.

Capture is the goal — empirical motivation is fresh from SHARED.001 + session 23 today; deferring this question into the backlog without a written brief loses the corpus context.

— 0.4.0_DE_ClientPlatform
