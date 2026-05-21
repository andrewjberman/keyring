# Session 2026-05-21 — ADHC_VALGATE.006 (D-2 visual-rendering-baseline gate)

**Agent:** 0.4.0_DE_ClientPlatform~B
**Workspace CLOUD commits:** `a60bf1730` (D-2 build) -> `cb2c2dea9` (D-2 live AC3 verified)
**TO:** ADHC_VALGATE.006 — D-2 visual-rendering-baseline gate (P2, VALGATE Phase 2 / Class-D)
**Issued by / RAVC2 to:** 1.0.0_SA_CTO~B

## Current State

| Item | Status |
|------|--------|
| ADHC_VALGATE.004 (D-1 adapter-threading gate) | COMPLETE — RAVC2-ACCEPTED + CLOSED by CTO~B |
| ADHC_VALGATE.005 (D-3 multi-axis envelope sentinel) | COMPLETE — RAVC2-ACCEPTED + CLOSED by CTO~B |
| ADHC_VALGATE.006 (D-2 visual-rendering baseline) | COMPLETE — `cb2c2dea9`, verdict layer 11/11 + live AC3 3/3, RAVC2 this session |
| MDPF_ASSETS.033 (chart-surface estimate marker) | NEXT — P3/LAST |

With .004/.005/.006 complete, VALGATE Class-D (the last phase) closes → VALGATE 9/9.

## Work Completed — D-2 visual-rendering-baseline gate

D-2 is the render-fidelity gate: *did the right data reach the screen?* It
asserts a partner-facing panel's data-bearing nodes are non-empty and correctly
scoped, against a stored structural baseline.

### Phase 0 — mechanism confirmation (PRD §7 Q4, TO mandate)

CONFIRMED the **structural-assertion variant** (not pixel-diffing). Surfaced to
CTO~B (193015Z) before the build; endorsed (197344Z). Key finding: the open
"subagent availability" question is resolved by the **standalone-runner**
pattern — `portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs` drives
system Chrome via CDP with `puppeteer-core` (run with `bun`). D-2 reuses the
`/frontend-dev` constitution *vocabulary* but executes via a standalone runner,
not the plugin's subagents — sidestepping both the subagent question and the
documented Bun+Playwright CDP-WS hang on Windows.

### Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.tools/valgate/d2_runner.mjs` | New — render-half runner (puppeteer-core/CDP); + a cold-start readiness wait | Yes — `a60bf1730`, `cb2c2dea9` |
| `.tools/valgate/d2_visual_baseline_gate.py` | New — verdict-half gate (WARN-not-BLOCK) | Yes — `a60bf1730` |
| `.tools/valgate/d2-baselines/partner-analytics-overview.json` | New — seed baseline, selectors verified live (replaced the `advisor-book-headline.json` template) | Yes — `cb2c2dea9` |
| `.tools/valgate/d2_gate_test.py` | New — verdict-layer verification harness, 11/11 | Yes — `a60bf1730` |
| `.tools/valgate/VALGATE_D2.md` | New — §3.2 table + Phase-0 record + live-AC3 results | Yes — `a60bf1730`, `cb2c2dea9` |

### Architecture — two halves

Mirrors D-1 (a diagnostic produces observations; the gate renders the verdict):
- `d2_runner.mjs` — RENDER half: drives a partner panel in CDP Chrome per a
  structural baseline; emits a raw results JSON. Generic — re-pointed at any
  panel by swapping the baseline.
- `d2_visual_baseline_gate.py` — VERDICT half: reads the results JSON; WARN on
  any structural-emptiness or scope-drift breach; PASS otherwise. WARN-not-BLOCK
  (PRD §7 Q1). Browser-independent, fully unit-testable.

### Acceptance Criteria

- **AC1** — Phase-0 mechanism confirmed + recorded (structural-assertion
  variant; standalone puppeteer-core runner). VERIFIED — `VALGATE_D2.md`.
- **AC2** — D-2 asserts a partner-facing panel's data-bearing nodes non-empty +
  correctly scoped against a stored structural baseline; WARN on a breach.
  VERIFIED.
- **AC3** — VERIFIED both synthetically (verdict layer, `d2_gate_test.py`
  11/11 — the 3 cases + missing/error/fail-loud) **and live** against the
  served portal:

  | Case | Result |
  |---|---|
  | Correct render | 2/2 checks OK (recharts chart non-empty + Inflection-scoped) → **PASS** |
  | Deliberately-emptied panel | 2/3 OK, 1 structural-emptiness breach → **WARN** |
  | Wrong-scope panel | 1/2 OK, 1 scope-drift breach → **WARN** |

  §3.2 six-field table filled (`VALGATE_D2.md`).
- **AC4** — ASCII only; no portal `src/` change (D-2 is parent-repo
  `.tools/valgate/` tooling) → portal typecheck/build unaffected; this session
  log with the Compiler Tools section.

### Live verification — cold-start note

The first live run produced false `missing` observations — a SPA render race.
`d2_runner.mjs` was given a generic readiness wait (poll until
`document.readyState` complete + substantial body text + ≥1 SVG, capped 25s).
All three AC3 cases above are post-fix and clean. The runner records
`readiness: settled|timeout`. CTO~B's "fall back if environment-fragile"
trigger was approached at the cold-start race but resolved within the
engagement — no fallback needed; full live AC3 delivered.

## Compiler Tools

| Tool | When | Result | Notes |
|------|------|--------|-------|
| `comp-transform schema-check PartnerAnalytics` | Phase 1 (before write) | "All rendered fields match their response types" — no MISSING | Phase-1 mandate: ground the structural-assertion node set for the partner panel D-2 gates. No live D-2-class defect. |
| D-2 runner structural-assertion run (the gate's own mechanism) | Phase 3 (after commit) | 3/3 AC3 cases pass live against the served portal | Phase-3 mandate: the gate fires + renders a verdict end-to-end. |

## Next Steps

- [DE 0.4.0~B] Start MDPF_ASSETS.033 — chart-surface the estimated 2024-depth
  segment on the ModelPortfolios Daily AUA Analysis chart (P3, last in the
  engagement; portal-FE).
- [CTO~B 1.0.0] RAVC2 validation of D-2. With .004/.005/.006 all complete,
  VALGATE Class-D closes — VALGATE 9/9.
