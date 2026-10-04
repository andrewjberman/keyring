# IRPT_YCDGEN -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

Worker rows are `IRPT_YCDGEN-W<n>-S<k>`; append-only; gate `.tools/surprise-row-gate.py`.

## IRPT_YCDGEN-W3-S1 -- the laptop has no bundled Chromium; Edge's close() hangs 20-90 s after the PDF is written

```json
[
  {
    "id": "IRPT_YCDGEN-W3-S1",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_YCDGEN~3",
    "surfaced_at": "2026-10-04T01:45:00Z",
    "one_line": "YCD-l-1 render_pdf.cjs: no playwright-bundled Chromium is installed, so it launches the msedge channel (bundled as fallback), and browser.close() takes 20-90 s on this laptop, so the close is bounded at 3 s and the process exits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "YCD-l-1: render_pdf.cjs loads playwright-core from portal/node_modules, launches chromium headless, sets the HTML and prints to PDF.",
    "world_is": "C:/Users/AndrewBerman/AppData/Local/ms-playwright holds only an MCP msedge profile dir (no chromium-<rev> build), so a bundled launch fails; msedge (channel) launches in about 1 s, prints in about 0.1 s, but await browser.close() took 21.8 s (measured with a timing script) and 93 s in a second run. A first test run took 85 s; with the bounded close it is 7 s. The issuer's host run therefore needs Edge or Chrome installed (IRPT_CHROMIUM_CHANNEL overrides the channel); the PDF is already on disk before the close.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node timing script under .runtime of the worker worktree: launch 1164 ms, pdf 1278 ms, close 21789 ms (msedge channel)",
        "infra/aws/lambda/investor-reporting/ycharts/research/render_pdf.cjs: Promise.race of browser.close() against a 3000 ms timer, then process.exit(0)",
        "pytest tests/test_layout_overview.py: 6 passed in 85.04s before the change, 6 passed in 7.17s after"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```
