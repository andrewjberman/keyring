# VALGATE D-1 — Adapter-Threading Gate

**Project:** ADHC_VALGATE Phase 2 (Class-D render-fidelity suite) — TO `ADHC_VALGATE.004`
**Owner:** `0.4.0_DE_ClientPlatform~B`
**PRD:** `docs/architecture/ADHC_VALGATE.md` v0.1 — §4.D (D-1 spec), §3.2 (gate anatomy), §3.3, §7 Q1.

D-1 is the **structural fire + verdict** around `comp-adapter-audit`
(`ADHC_COMPIL_V4.031`). It is **not** a new diagnostic — the tool produces the
field-by-field audit; D-1 makes it fire structurally at portal pre-push and
renders a PASS / WARN / BLOCK verdict.

## §3.2 — Six-field gate anatomy

| Field | D-1 |
|---|---|
| **Trigger** | Portal pre-push hook (`.tools/portal-hooks/pre-push`), every push, per pushed ref. Fires before the existing PROD-only `tsc` typecheck. |
| **Input** | Each partner-facing static adapter function (`getPlatinum*` / `*Static*` in `portal/src/api/endpoints/*.ts`) whose body intersects a changed line range in the push. |
| **Reference** | The most-recent S3 platinum envelope for that adapter's data source — fetched by `comp-adapter-audit`. |
| **Comparison** | `comp-adapter-audit <fn>` — a field-by-field threading audit (typed raw interface vs live S3 envelope vs adapter body / return expression). D-1 reads the audit manifest and classifies the finding statuses. |
| **Verdict** | `PASS` no findings. `WARN` drift findings only. `BLOCK` an un-threaded output path on a **partner-facing** adapter (`FALLBACK-ORDER`). |
| **Action** | `BLOCK` → exit 1, push refused. `WARN` / `PASS` → exit 0, push proceeds (WARN findings printed). |

## Verdict policy

`comp-adapter-audit`'s own exit code is **not** a usable D-1 signal: every live
partner adapter carries ~65 `SCHEMA-DRIFT` WARNs (an S3 field the typed
interface does not declare = type-stale; the field is still in the envelope).
Keying BLOCK on raw audit WARNs would block every push touching a partner
adapter on day 1. D-1 parses the audit and applies its own policy:

| Audit finding status | Direction | D-1 class | Rationale |
|---|---|---|---|
| `FALLBACK-ORDER` | output-construction defect | **BLOCK** (partner-facing) | An inverted `??` fallback chain — a narrower source first masks a field only the broader source carries, dropping it from the adapter's output expression. The precise PRD D-1 defect. Anchor: INFFIN #7 inverted-fallback `32df3b85`. |
| `SCHEMA-DRIFT` / `NESTED-SCHEMA-DRIFT` | raw-side | WARN | An S3 field absent from the typed raw interface — type-stale; the field is still present in the envelope, not data-absent. |
| `TYPE-ONLY` | raw-side | WARN | A raw-interface field absent from the live S3 envelope — frequently legitimate-historical; graded `INFO` by the audit tool. |
| `NOT-THREADED` | raw-unconsumed | WARN | A raw S3 field the adapter body never references — the **inverse** of the D-1 defect; a raw field the adapter legitimately does not need is not a defect. |

- **Partner-facing** adapter + a `BLOCK`-class finding → **BLOCK** the push
  (PRD §7 Q1: D-1 partner-facing is the v1 BLOCK exception).
- **Non-partner-facing** adapter → the same finding is **WARN**, never BLOCK.
- **Partner-facing classification** (deterministic, AC2): an adapter defined in
  `portal/src/api/endpoints/advisor-intelligence.ts` is partner-facing (the
  AdvisorIntelligence partner portal). Other endpoint files → non-partner-facing.

**Documented limitation.** D-1's BLOCK precision is bounded by the tool's
signal precision. `comp-adapter-audit` audits the raw-input side and the return
expression — not the adapter's full *output type*. Of its finding categories,
only `FALLBACK-ORDER` is an output-construction defect in the PRD's
"output-without-raw-source" direction. The "missing-thread" surface (INFFIN
`d622a249`) is surfaced as a WARN but cannot be structurally distinguished from
benign drift without re-authoring the tool — which is `ADHC_COMPIL_V4` scope,
explicitly excluded from D-1.

## Files

| File | Role |
|---|---|
| `.tools/portal-hooks/d1_adapter_threading_gate.py` | The gate — diff → changed adapters → audit → verdict. |
| `.tools/portal-hooks/pre-push` | Canonical portal pre-push hook; invokes D-1. `install.sh` copies it to `portal/.git/hooks/pre-push`. |
| `.tools/portal-hooks/d1_gate_test.py` | Verification harness — verdict-logic unit tests + end-to-end synthetic-fixture tests. |
| `.tools/portal-hooks/VALGATE_D1.md` | This document. |

## Hook-surface reconciliation (spec-vs-reality)

PRD §3.3 says D-1 wires "alongside `comp-cache collisions`" at the portal
pre-push hook. Empirically `comp-cache collisions` is **not** hook-wired — the
portal pre-push hook runs only `tsc` on PROD pushes. The portal submodule has
no committed hook machinery; the pre-push surface is the parent-repo
`.tools/portal-hooks/` (deployed into `portal/.git/hooks/` by `install.sh`).
D-1 therefore lives parent-repo-side, co-located with `comp-adapter-audit`
which it wraps. (`.tools/**` is owned-paths lane `ANY`.) Reconciliation
endorsed by `1.0.0_SA_CTO~B`, 2026-05-21.

## Verification

`python .tools/portal-hooks/d1_gate_test.py` — 15/15 cases:
- Verdict logic: `FALLBACK-ORDER`+partner→BLOCK; +non-partner→WARN; 65×
  `SCHEMA-DRIFT`→WARN; `NOT-THREADED`/`TYPE-ONLY`→WARN; no findings→PASS;
  mixed `SCHEMA-DRIFT`+`FALLBACK-ORDER`→BLOCK.
- End-to-end: a synthetic adapter with a deliberately inverted `??` fallback
  chain (the INFFIN-arc `32df3b85` pattern) is BLOCKed when partner-facing,
  WARNed when non-partner-facing; a correct adapter is not blocked.
