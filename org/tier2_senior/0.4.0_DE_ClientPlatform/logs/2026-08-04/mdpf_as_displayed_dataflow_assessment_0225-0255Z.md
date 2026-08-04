# MDPF as-displayed dataflow assessment (Andrew-direct via CVO) — 0225-0255Z

**archetype:** TRACE

## What happened

Fresh seat instantiation (Andrew-direct for this task). Startup: /watcher armed (Monitor task
bchr4z7l3, TaskOutput-confirmed running; no orphan found, prefix /cygdrive/c), LD-0290 serial file
written, registered PID 17772, A.2 audit-invoker (2 pre-existing baseline-missing findings, not
mine, non-blocking), A.3 PATH 94/94 + comp-which exercised live, B.1 to-check (7 TOs held, all
staged/pre-existing — none GOed), hooks D/E done, zero crons.

GO received 022922Z (CVO, Andrew-direct relayed): assess the AS-DISPLAYED portal MDPF dataflow —
rendered view -> fetch URL -> resolved S3 object (full bucket+key) -> writer, deployed-plane
grounded. ACKed same minute. COO queue-note (row-6 render-half after) ACKed non-preempting.

**Delivered:** `deliverables/MDPF_AS_DISPLAYED_DATAFLOW_ASSESSMENT_20260804.md` @b48634789a
(committed, unpushed per lanes-commit/integrators-push). Report MCPed to CVO cc COO 025153Z/025201Z.

**Verdict:** Andrew's acceptance example PASSES — json/mdpf/* displayed nowhere. Live CF
distribution EVTSA9VEHNZVH binds public-data-router:6 on /api/general/*; the deployed v6 artifact
(downloaded from the live qualifier) rewrites /api/general/mdpf/ -> /platinum/mdpf/ ahead of the
general /json/ branch; the router's own CW logs show all real mdpf traffic 08-01+08-03 -> platinum;
PROD-wide grep shows json/mdpf in comments only. Key finding F1: the page's BASE metrics
(cards + quarterly totals + page-gate) render from json/portfolios/aum-metrics.json — json CHANNEL,
FROZEN 2026-07-23 (writer flag-disabled) — adjudication surfaced to CVO (channel-reading vs
json/mdpf-reading of Andrew's verbatim). F2 platinum aum-metrics cottonwood-only; F3 T2.A
corroborated at display layer; F4 four deployed comment blocks falsified; F5 json/mdpf
written-daily-read-never; F6 underscore twins displayed never.

Self-caught method note: my first provenance pull collided two artifacts on the shared basename
`aum-metrics.json` in the scratchpad (the exact 4-way-collision trap the briefing named) — caught
on the byte count, re-pulled with distinct names before any conclusion rested on it.

## Compiler Tools

| Tool | Result |
|---|---|
| comp-cluster ModelPortfolios (+ --json, --help) | Page map: 1 cluster, 25 sources, 118/119 coverage. Worked. Gap noted: sources mix live calls with DEAD endpoint declarations (imported-module edges) — 5 of its URL sources have zero deployed callers; a live-call flag would sharpen it |
| comp-routes behaviors/rewrites/trace/edge-versions | Worked; DESIRED table had the mdpf->platinum rule; honest self-labeling drove the APPLIED grounding. MSYS note: trace arg needs quoting (leading-slash mangle, tool self-detected) |
| comp-kuzu (schema + writer queries) | READS_URL edges resolved; NO WRITES edge exists for json/portfolios/aum-metrics.json — writer graph gap, writer INFERRED via census @ae2d684f3b instead |
| comp-blast | Not fired: the CVO census (01:1xZ same night) had just exercised it on this estate; the display-side question needed caller/router/log grounding, which blast does not carry |
| raw aws (inline # rail-checked each call) | Live get-distribution-config, lambda get-function v6 artifact, s3 ls/get-object provenance, CW filter-log-events rewrite lines — the APPLIED+EXERCISED legs |

## Open / handed off

- CVO validation of the report (RAVC close pending).
- F1 adjudication (json channel vs json/mdpf reading) — CVO/Andrew.
- Row-6 render-half TO — COO authoring; I said ready-for-next.
- 7 pre-existing staged TOs unchanged (MDPF_3FIRMS x4, MDPF_REVAMP.S5-ROLLOVER, NFRA_TSGRAPH P3-2/P3-3) — no GO held.
