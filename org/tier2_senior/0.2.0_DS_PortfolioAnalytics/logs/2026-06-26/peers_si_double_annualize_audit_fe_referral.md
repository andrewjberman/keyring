# /Peers Since-Inception charts wrong — audit + FE referral
**archetype:** DIAGNOSE

## Trigger
Andrew-direct: "the since-inception /peer tab charts are all using wrong data ... parser work must not have caught them or perhaps a lambda is annualizing incorrectly, more likely wrong cell though. Audit and fix, then refer the change and info to pod2 de if any frontend changes are needed."

## Finding (grounded)
ROOT CAUSE = **frontend double-annualization**, NOT a data/producer bug.

**Data layer CONFIRMED CORRECT (my DS lane — no change needed):**
- Producer `yang-generate-peer-performance/lambda_function.py` reads the workbook
  "Since Inception (4/30/2024) Statistic" cell faithfully by header-label.
- Ground truth tie: served `s3://opal-data-portal-v2/json/peers/peer_performance.json`
  (generated 2026-06-26T16:51:26Z, data_as_of 06-18) vs source
  "Models Performance vs Peers 20260618.xlsx" Peer Table sheet = **30/30 model values
  match exactly**, all 6 periods incl. SI (scratchpad `fullcmp.py`).
- The source SI column is **already annualized** (INT SI 13.87% sits sanely next to
  1Y 14.43%; cumulative over ~26mo would be ~30%+). So neither the workbook nor the
  lambda is the "wrong cell"/"annualizing incorrectly" Andrew hypothesized — the cell
  is right and the lambda just reads it.

**FE bug — `portal/src/pages/ModelPortfolios/tabs/PeersTab.tsx`:**
- Lines 14-78 (`annualizeSinceInceptionReturn` + `transformPeerData`) re-annualize SI
  via `(1+r)^(365/actualDays)-1`. Its premise comment ("Excel contains cumulative SI")
  is now FALSE → applies annualization a 2nd time. Called at lines 410-414.
- Effect (actualDays=779, exp 0.4685) — chart shows ~half true value (scratchpad `fe_repro.py`):
  UST 4.67->2.16 | ST 5.92->2.73 | INT 13.87->6.28 | LTC 18.50->8.28 | LTA 18.40->8.24.
  Hits percentile bands + benchmark arrow too (transform annualizes p5..p95 + benchmark).

**Precedent — the fix is already proven in a sibling:** `BenchmarkHeatmap.tsx:306-309`
fixed this exact bug (`const annualizeSI = (value,_p) => value` identity pass-through;
its comment even cites "UST SI ~2.3% instead of ~4.8%", matching my repro). PeersTab is
the lone component that never got the correction.

## Action
- Referred FE fix to **0.2.0_DE_PortfolioAnalytics** (msg 20260626T175925Z) with file:line +
  wrong-vs-right table + the BenchmarkHeatmap precedent. Suggested fix: mirror
  BenchmarkHeatmap — drop the PeersTab annualize/transform, render `data` directly;
  keep footnote line 525 (still true). DE was offline (NOT REGISTERED).
- CC'd **2.0.0_SA_COO** (msg 20260626T175947Z) flagging DE needs a /drive spawn to action
  the FE fix + DT deploy.
- DS half CLOSED — data layer needs no change.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| `comp-which` (x2) | routed to comp-platinum/comp-transform/pipescript backstop | natural-language routing for producer + FE-component questions |
No `comp-pipescript io` run: this was an audit + FE referral, no gold/silver/bronze
`.py` was edited (producer change = none; the only fix is frontend, DE's lane).
