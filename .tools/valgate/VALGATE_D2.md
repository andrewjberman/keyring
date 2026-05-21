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
| `.tools/valgate/d2-baselines/partner-analytics-overview.json` | Seed structural baseline (selectors verified live). |
| `.tools/valgate/d2_gate_test.py` | Verdict-layer verification harness. |
| `.tools/valgate/VALGATE_D2.md` | This document. |

## Verification

**Verdict layer — `python .tools/valgate/d2_gate_test.py`, 11/11 cases.** The
three AC3 cases against synthetic runner results: a correct render → PASS; a
deliberately-emptied panel (`--` hero card / empty bell-curve) → WARN; a
wrong-scope panel (firm-aggregate where advisor expected) → WARN. Plus
missing-node, runner-error, and unrecognized-value cases all fail loud to WARN.

**Render layer — live AC3, VERIFIED 2026-05-21.** The `d2_runner.mjs` half was
exercised against the served portal (`localhost:5175`) via an isolated headless
Chrome on CDP port 9445. All three AC3 cases passed live against the
`partner-analytics-overview` panel (the AdvisorIntelligence ASSETS OVERVIEW
panel, Inflection partner):

| Case | Baseline | Result |
|---|---|---|
| Correct render | `partner-analytics-overview.json` | 2/2 checks OK — `.recharts-surface` chart non-empty + body Inflection-scoped → **PASS** |
| Deliberately-emptied panel | + a data-bearing node with a no-match selector | 2/3 OK, 1 structural-emptiness breach → **WARN** |
| Wrong-scope panel | scope check expecting an absent partner | 1/2 OK, 1 scope-drift breach → **WARN** |

**Cold-start note.** The first run produced false `missing` observations — a
SPA render race. `d2_runner.mjs` carries a generic readiness wait (poll until
`document.readyState` complete + substantial body text + ≥1 SVG, capped 25s)
that resolved it; all three cases above are post-readiness-wait. The runner
records `readiness: settled|timeout` in its results.

**Run procedure (reproduce):**
1. Serve the portal — `cd portal && bun run dev --port 5175`.
2. Launch Chrome with CDP — `chrome --remote-debugging-port=<port> --headless=new --user-data-dir=<temp>`.
3. Fill the baseline's `login.password` in a non-committed runtime copy
   (the committed baseline carries `REPLACE_AT_RUNTIME`).
4. `NODE_PATH=portal/node_modules bun run .tools/valgate/d2_runner.mjs --baseline <baseline> --out <results.json> --cdp-port <port>`
   then `python .tools/valgate/d2_visual_baseline_gate.py --results <results.json>`.

`NODE_PATH=portal/node_modules` is required so the runner resolves
`puppeteer-core` (installed in the portal submodule, not the workspace root).
