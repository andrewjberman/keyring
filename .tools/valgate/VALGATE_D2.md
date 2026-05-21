# VALGATE D-2 — Visual-Rendering-vs-Baseline Gate

**Project:** ADHC_VALGATE Phase 2 (Class-D render-fidelity suite) — TO `ADHC_VALGATE.006`
**Owner:** `0.4.0_DE_ClientPlatform~B`
**PRD:** `docs/architecture/ADHC_VALGATE.md` v0.1 — §4.D (D-2 spec), §3.2, §3.3, §7 Q4.

D-2 is the render-fidelity gate: *did the right data reach the screen?* It
asserts a partner-facing panel's data-bearing nodes are non-empty and correctly
scoped, against a stored structural baseline.

## Phase-0 mechanism record (PRD §7 Q4 — TO mandate)

**Mechanism CONFIRMED: the structural-assertion variant** — not pixel/screenshot
diffing (brittle, CI-expensive; explicitly not recommended by the PRD).

Findings (surfaced to `1.0.0_SA_CTO~B`, 2026-05-21):

1. The `/frontend-dev` per-page constitution machinery exists and is live —
   `portal/.frontend-dev/testing/` holds structural-smoke constitution JSONs.
   Their action vocabulary (`assert_visible`, `assert_no_console_errors`,
   `js_eval`, `screenshot`) is the structural-assertion substrate.
2. **The "subagent availability" open question is resolved.** There is a proven
   standalone-runner pattern — `portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs`
   — that drives system Chrome via CDP with `puppeteer-core`, run with `bun`.
   D-2 reuses the constitution *vocabulary* but executes via a standalone
   runner; it does **not** invoke the `/frontend-dev` plugin's subagents.
3. The runner's own header documents why `puppeteer-core` not Playwright:
   "Bun + Playwright's WebSocket client hangs on Windows during the CDP
   upgrade ... puppeteer-core uses its own ws client which works under Bun."
   D-2 follows that proven choice.

## §3.2 — Six-field gate anatomy

| Field | D-2 |
|---|---|
| **Trigger** | Post chain-emit, against a *served* portal — run on-demand / post-deploy. D-2 needs a rendered portal; it does **not** run inside the gold chain (TO `<cross_domain_coordination>` — no gold-chain overlap). |
| **Input** | A rendered partner-facing panel's data-bearing DOM nodes. |
| **Reference** | A stored structural baseline per panel — the data-bearing-node set + the expected-scope assertions (`d2-baselines/<panel>.json`). |
| **Comparison** | Structural emptiness (an empty histogram, a `--`/`$0` hero card) and scope drift (firm-aggregate where advisor-scoped is expected). |
| **Verdict** | `PASS` every data-bearing node non-empty + every scope assertion OK. `WARN` ≥1 structural-emptiness or scope-drift breach. D-2 ships **WARN-not-BLOCK** in v1 (PRD §7 Q1). |
| **Action** | `WARN` → printed report + JSON report for a session log. D-2 never BLOCKs. Exit 0 PASS / 1 WARN / 3 internal error. |

## Architecture — two halves

D-2 mirrors D-1 (a diagnostic produces observations; the gate renders the
verdict):

| Half | File | Role |
|---|---|---|
| Render | `d2_runner.mjs` | Drives a panel in a real browser (puppeteer-core + CDP Chrome) per a baseline; emits a raw results JSON. |
| Verdict | `d2_visual_baseline_gate.py` | Reads the runner's results JSON; renders the D-2 PASS/WARN verdict. Browser-independent, deterministic. |

The split keeps the verdict logic fully unit-testable without a browser, and
lets the runner be re-pointed at any panel by swapping the baseline JSON.

## Files

| File | Role |
|---|---|
| `.tools/valgate/d2_runner.mjs` | The render-half runner — puppeteer-core / CDP. |
| `.tools/valgate/d2_visual_baseline_gate.py` | The verdict-half gate. |
| `.tools/valgate/d2-baselines/advisor-book-headline.json` | Seed/template structural baseline. |
| `.tools/valgate/d2_gate_test.py` | Verdict-layer verification harness. |
| `.tools/valgate/VALGATE_D2.md` | This document. |

## Verification

**Verdict layer — `python .tools/valgate/d2_gate_test.py`, 11/11 cases.** The
three AC3 cases against synthetic runner results: a correct render → PASS; a
deliberately-emptied panel (`--` hero card / empty bell-curve) → WARN; a
wrong-scope panel (firm-aggregate where advisor expected) → WARN. Plus
missing-node, runner-error, and unrecognized-value cases all fail loud to WARN.

**Render layer — live AC3 runner-session (procedure).** The `d2_runner.mjs`
half is exercised against a served portal:
1. Serve the portal — `cd portal && bun run dev --port 5175` (DEV branch).
2. Launch system Chrome — `chrome --remote-debugging-port=9444`.
3. Tune `d2-baselines/advisor-book-headline.json` selectors against the live
   DOM (the baseline is data — no code change).
4. `bun run .tools/valgate/d2_runner.mjs --baseline d2-baselines/advisor-book-headline.json --out d2-results.json`
   then `python .tools/valgate/d2_visual_baseline_gate.py --results d2-results.json`.
5. AC3 live: a healthy panel → PASS; deliberately empty a data-bearing node
   (or point at an advisor with no data) → WARN; a firm-scope leak → WARN.

The render-layer live verification needs a served portal + a CDP Chrome
session; it is the environment-dependent step. The verdict layer — the
deterministic core — is fully verified above.
