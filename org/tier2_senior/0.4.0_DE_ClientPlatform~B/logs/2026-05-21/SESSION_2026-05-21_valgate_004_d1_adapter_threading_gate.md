# Session 2026-05-21 — ADHC_VALGATE.004 (D-1 adapter-threading gate)

**Agent:** 0.4.0_DE_ClientPlatform~B
**Workspace CLOUD commit:** `28601ffbf` (D-1 gate) -> session log commit follows
**TO:** ADHC_VALGATE.004 — D-1 adapter-threading gate (P1, VALGATE Phase 2 / Class-D)
**Issued by / RAVC2 to:** 1.0.0_SA_CTO~B (COO~B closed; CTO~B holds dispatch + output-validation)

## Current State

| Item | Status |
|------|--------|
| ADHC_VALGATE.004 (D-1 adapter-threading gate) | COMPLETE — committed `28601ffbf`, 15/15 verification, RAVC2 to CTO~B |
| ADHC_VALGATE.005 (D-3 multi-axis envelope sentinel) | NEXT — P1, starting this session |
| ADHC_VALGATE.006 (D-2 visual-rendering baseline) | QUEUED — P2, Phase-0 mechanism-confirm first |
| MDPF_ASSETS.033 (chart-surface estimate marker) | QUEUED — P3/LAST per CTO~B 184313Z |

## Work Completed — D-1 adapter-threading gate

D-1 is the structural fire + verdict around `comp-adapter-audit`
(`ADHC_COMPIL_V4.031`). Not a new diagnostic — it makes the audit fire
structurally at the portal pre-push hook and renders a PASS/WARN/BLOCK verdict
for each partner-facing static adapter changed in a push.

### Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.tools/portal-hooks/d1_adapter_threading_gate.py` | New — the gate: diff -> changed adapters -> `comp-adapter-audit` -> verdict | Yes — CLOUD `28601ffbf` |
| `.tools/portal-hooks/pre-push` | Extended — fires D-1 every push (typecheck stays PROD-only) | Yes — CLOUD `28601ffbf` |
| `.tools/portal-hooks/d1_gate_test.py` | New — verification harness, 15/15 cases | Yes — CLOUD `28601ffbf` |
| `.tools/portal-hooks/VALGATE_D1.md` | New — section-3.2 gate table + verdict policy + reconciliation | Yes — CLOUD `28601ffbf` |

### Verdict policy

`comp-adapter-audit`'s raw exit code is unusable as a D-1 signal — every live
partner adapter carries ~65 `SCHEMA-DRIFT` WARNs (S3 field not in the typed
interface = type-stale; field still in the envelope). D-1 parses the audit
manifest and BLOCKs only on the precise PRD defect direction:

- **BLOCK** (partner-facing): `FALLBACK-ORDER` — an inverted `??` fallback
  chain that drops a field from the adapter's output expression. Anchor:
  INFFIN #7 inverted-fallback `32df3b85`.
- **WARN**: `SCHEMA-DRIFT` / `NESTED-SCHEMA-DRIFT` (type-stale, raw-side),
  `TYPE-ONLY` (typed-but-absent, INFO-grade), `NOT-THREADED` (raw S3 field the
  adapter never references — the *inverse* direction; not a defect).
- Non-partner-facing adapter → all findings WARN, never BLOCK.

**NOT-THREADED direction — confirmed (CTO~B 185427Z check #3).** Read
`adapter_audit_cli.py:223-231`: `NOT-THREADED` = "in S3 raw envelope but adapter
body has no explicit reference". This is the raw-field-unconsumed direction, the
**inverse** of the D-1 defect ("an output path with no raw source"). A raw field
the adapter legitimately does not need is not a defect → demoted from the
initial BLOCK-class to WARN. BLOCK-class is `FALLBACK-ORDER` only.

### Postmortem: hook-surface mismatch (PRD-vs-reality)

**Root cause.** PRD §3.3 / the TO say D-1 wires "alongside `comp-cache
collisions`" at the portal pre-push hook. Empirically: the portal pre-push hook
(`.tools/portal-hooks/pre-push`) runs only `tsc -b --noEmit` on PROD pushes —
`comp-cache collisions` exists as a tool but is **not** hook-wired. The portal
submodule has no committed hook machinery (no husky); the installed
`portal/.git/hooks/pre-push` is an untracked copy of the parent-repo
`.tools/portal-hooks/pre-push`, deployed by `install.sh`.

**Resolution.** Per the TO Phase-1 `if_mismatch` ("reconcile the hook surface
before wiring D-1"): the pre-push surface IS parent-repo `.tools/portal-hooks/`
(`.tools/**` owned-paths lane `ANY`). D-1 lives there, co-located with
`comp-adapter-audit` which it wraps — not split into the portal submodule (a
cross-repo straddle). The TO's "portal-side / portal DEV branch" phrasing is
superseded by this empirical finding. Surfaced to CTO~B 185222Z; endorsed
185427Z.

### Known follow-up — hook-file line endings (not blocking)

`.gitattributes` has `*.sh text eol=lf` / `*.py text eol=lf`, but the hook file
`pre-push` has no extension and is not covered → `core.autocrlf=true` stores it
CRLF. Empirically CRLF hooks execute fine on this Git Bash (tested: a
`#!/bin/bash\r` CRLF script runs via `./script`; the installed hook ran the D-1
gate correctly in simulation) — and the pre-existing `pre-push` was already
CRLF. Recommended follow-up: a 1-line `.gitattributes` add
(`.tools/portal-hooks/pre-push text eol=lf`) + `git add --renormalize`.
`.gitattributes` is owned-paths lane `BASE_EXEC` — out of DE~B lane; flagged to
CTO~B for routing. Not a correctness blocker.

## Acceptance Criteria

- **AC1** — D-1 fires structurally at portal pre-push for each partner-facing
  static adapter changed in the push; invokes `comp-adapter-audit`, renders a
  verdict. VERIFIED — installed-hook simulation over a real range that changed
  `advisor-intelligence.ts` detected `getPlatinumClientDetailStatic`, audited
  it, rendered WARN.
- **AC2** — verdict policy: partner-facing BLOCK / non-partner WARN;
  partner-facing classification deterministic (by endpoint file —
  `advisor-intelligence.ts` = partner-facing). VERIFIED.
- **AC3** — synthetic adapter with a deliberately un-threaded output path
  (inverted `??` fallback — the INFFIN-arc `32df3b85` pattern) is BLOCKed; a
  correct adapter is not; section-3.2 six-field table filled (`VALGATE_D1.md`).
  VERIFIED — `d1_gate_test.py` 15/15.
- **AC4** — no emoji (ASCII only); session log with Compiler Tools section
  (below). Portal `src/` unchanged — D-1 is entirely parent-repo `.tools/`
  tooling — so portal typecheck/build are unaffected (no portal-src delta).

## Compiler Tools

| Tool | When | Result | Notes |
|------|------|--------|-------|
| `comp-cache collisions` | Phase 1 (before write) | Ran clean — listed React Query key collisions across components | Phase-1 mandate: confirm the hook insertion point. Found `comp-cache collisions` is NOT hook-wired (PRD assumption) — drove the hook-surface reconciliation above. |
| `comp-transform schema-check AdvisorBookView` | Phase 1 (before write) | "All rendered fields match their response types" — no MISSING | Phase-1 mandate. No current D-1-class MISSING defect on this partner component → `if_mismatch` (flag a live defect) did not trigger. |
| `comp-transform schema-check AdvisorPublicProfile` | Phase 1 (before write) | "All rendered fields match their response types" — no MISSING | Second partner component checked — clean. |
| `comp-adapter-audit getPlatinumAdvisorSummaryStaticInflection` | Build / Phase 3 | 65 WARN (SCHEMA-DRIFT/NESTED), 2 INFO TYPE-ONLY — the tool D-1 wraps | Grounded the verdict policy: raw exit code unusable; ~65 benign drift WARNs per live adapter. |
| `comp-adapter-audit` via the D-1 gate path | Phase 3 (after commit) | Gate invokes the tool + renders a verdict end-to-end — `getPlatinumAdvisorSummaryStaticInflection` -> WARN; `getPlatinumClientDetailStatic` (via installed hook) -> WARN | Phase-3 mandate satisfied. |

## Next Steps

- [DE 0.4.0~B] Start ADHC_VALGATE.005 — D-3 multi-axis envelope sentinel gate
  (generalize the shipped INFFIN.006 AdvisorBookView 6-axis threshold-2
  sentinel into a reusable config-driven gate).
- [CTO~B 1.0.0] RAVC2 validation of D-1. One routing item: the `.gitattributes`
  hook-eol follow-up (BASE_EXEC lane).
