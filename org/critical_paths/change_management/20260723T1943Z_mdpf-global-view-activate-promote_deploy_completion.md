# Deploy Completion — MDPF Global View Activation Promote (portal DEV->PROD v2.1.145)

**Status:** CLOSED — completed in-session (NEVER#5). This deploy (cfb0afb7 -> PROD) is fully landed + verified.
**Closed:** 2026-07-23T20:05Z
**Owner:** 0.2.0_DT_PortfolioAnalytics (COO relay/dispatch 194221Z; served data byte-verified LIVE by COO; CTO fire 184804Z sequencing; DS aggregate published 18:51Z/19:29Z)
**Window:** 2026-07-23 ~19:43Z (GO ack / begin) -> ~20:05Z (CI SUCCESS + tag peel-verified + data acceptance)

## Scope
Promote portal DEV @cfb0afb7 -> PROD. FINAL leg of the tonight-critical MDPF chain (Andrew-direct:
the whole MDPF chain completes THIS SESSION). The promote ACTIVATES the Global view (v2.1.144
carried it INERT) and points the renderer at the hyphenated serving keys `json/mdpf/*`
(DE's definitive map @193557Z). DEV head cfb0afb7 = DE None-count proof-2 render commit, +1 vs
PROD ffc022ed/v2.1.144.

Consumed served data, byte-verified LIVE by COO before GO AND independently re-grounded by me
post-CI:
- `json/mdpf/global/aggregate-aua-timeseries.json` frontier 2026-07-22 opal_aggregate_aua =
  1,951,676,164.42, point_class=measured, cottonwood folded in (458 refs); composes exactly:
  model_aua 1,676,493,815.11 + non_model_aua 275,182,349.31 = 1,951,676,164.42.
- per-firm 49F/INF/COT + top-level aggregate keys fresh (18:49Z); global 19:29:40Z.

## Rollback
Rollback ref = PROD **ffc022ed** (prior head, tag portal-v2.1.144) / prior merge d270acc9e.

## Evidence
| Gate | Result |
|---|---|
| Delta at dispatch | 1 commit origin/PROD..origin/DEV = cfb0afb7 exactly as GO'd; local PROD reasserted to ffc022ed (Step 3) |
| Typecheck (pre-promote) | GREEN rc=0 on cfb0afb7 (pre-flight + main-tree) |
| bun install | foreground rc=0 (420 packages, 280s) |
| Merge | --no-ff `5bc8be7e`; parents == ffc022ed + cfb0afb7 EXACTLY; only 2 files (ui-smoke.mjs, ModelPortfolios.tsx) |
| Parity gate | git diff origin/DEV HEAD == EMPTY at merge time |
| Push gates | provenance-read guard clean, VALGATE D-1 PASS, push-time tsc PASS |
| PROD commit | 5bc8be7e934d08989e9eeb64eb5ce50739c3fe22 (ffc022ed..5bc8be7e) |
| CI | run 30040175706 conclusion: success (gh run view --json), headSha 5bc8be7e |
| Tag | portal-v2.1.145; annotated; peeled ^{commit} == origin/PROD head EXACTLY; "Commits since v2.1.144: 2" |
| Data acceptance (Global + 3 firms) | Global headline independently byte-confirmed 1,951,676,164.42 cottonwood-inclusive; 49F/INF/COT served keys fresh. Through-auth live RENDER of all four views = DE's behavioral gate (DE owns render evidence). |
| Workspace pointer | committed at true current gitlink — see POINTER note below |
| Main tree | back on DEV (=f6b24a13, DEV advanced post-merge), verified; ended at workspace root; worktree pruned (physical dir persists, Filename-too-long, inert) |

## POINTER note (checklist item b — verify gitlink pre-commit; the 525a7296b class)
The pre-commit gitlink check found the main tree portal HEAD had advanced to **f6b24a13** (origin/DEV
moved during my promote window), NOT cfb0afb7. Per the established pattern the pointer records current
origin/DEV (f6b24a13) with an honest message; the pointer VALUE is current, and live PROD = 5bc8be7e
(v2.1.145). f6b24a13 is NOT in PROD (merge-base --is-ancestor: NO) — it did not ride into this promote.

## >> DISCOVERED SCOPE — ANDREW-DIRECT, GLOBAL VIEW, ON DEV NOT PROD (surfaced to COO+CTO) <<
`f6b24a13` (landed on origin/DEV after my 19:48Z Step-1 read, i.e. during the promote window) is an
**Andrew-direct x2 fix** directly concerning the view this promote just ACTIVATED:
1. **Interpolated treatment is PER-FIRM only** — the Global view SUPPRESSES band/overlay/legend/
   bar-outlines via the one `trendInterpolatedDates` choke point (materiality ruling; provenance
   channel still consumed; Cottonwood keeps full labeling; DOM-proven 0 interp-regions Global / 1 COT).
2. **W-3a tooltip double-count** — interp_total is an ANNOTATION, excluded from tooltip total AND rows
   (the 248M = 124M+124M class); W-3b total-series anchoring follows DS's W-2b shape.

**Consequence:** live PROD v2.1.145 activates the Global view WITH the interpolated band showing —
Andrew has directed the Global band be SUPPRESSED. My cfb0afb7 promote was correct per the GO
(f6b24a13 did not exist at GO/merge time), but a **follow-on promote of f6b24a13 -> PROD (v2.1.146)
is very likely required tonight** to honor the Andrew-direct materiality ruling on the activated view.
That is NEW scope needing a COO/CTO GO — NOT self-authorized. A fresh deploy-completion ledger opens
if/when GO'd.
