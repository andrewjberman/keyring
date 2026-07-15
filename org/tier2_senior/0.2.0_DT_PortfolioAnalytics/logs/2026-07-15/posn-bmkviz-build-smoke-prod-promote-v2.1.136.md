# POSN_BMKVIZ -- register, build, Andrew live-smoke x3, PROD promote v2.1.136, atomic close
**archetype:** MIXED (IMPLEMENT + DEPLOY)

## Summary
First full sovereign-delegate project cycle for this serial (activation 306834fa6, briefing
docs/briefs/SOVEREIGN_DELEGATE_AGENT_BRIEFING.md). From the Yang Liu 2026-07-10 call analysis
(basis record b36cf961b) Andrew scoped a POSN_CUSTOM expansion: (1) the Positioning Custom view
computes its blend + expanded-characteristics matrix from the models' BENCHMARK data (stable
anchors -- Yang: "the calculator should be based upon the benchmark"), (2) every Custom-view
stacked bar becomes a juxtaposed pair (opaque = benchmark basis, slightly transparent = model
actual), all 6 columns, no Mode B. Registered POSN_BMKVIZ (8c6f6cbb5), built FE-only in
PositioningSummary.tsx (+ HoldingsTab clamp), survived three Andrew live-smoke rounds, promoted
DEV->PROD portal-v2.1.136 via /prod-deploy, closed 2-step atomic (dd05e6af4) with COO CC.

## Change (portal, 4 commits on DEV -> 1 merge on PROD)
| Commit | What |
|---|---|
| c46d4308 | Custom-view dataMode 'portfolio'->'benchmark'; renderBarInner translucent companion (all 6 cols); legend key + BENCHMARK BASIS tag |
| 3835e5a3 | Smoke round 1: pair labels split (benchmark LEFT of opaque, model RIGHT of translucent, whole-pct text-xs); legend swatches green/blue diagonal slash; (Solid)/(Faded) capitalized; pair bars w-7 |
| 03719032 | Smoke round 2: Holdings Breakdown freeze-pane clamp 360px/62vh/760px -> 470px/81vh/990px (+30pct, every stop x1.3) |
| 2b066e01 | merge DEV->PROD v2.1.136 (full-DEV, passengers per sovereign call below) |

## The passenger adjudication (durable record of the sovereign call)
The origin/PROD..origin/DEV delta carried, beyond the three POSN_BMKVIZ commits: TicketCenter P0
page 11a638fb, Vident template guard c4598d82, LD-0273 surface-check CI gate + net-zero demo
pairs, and the Inflection AoR allowlist pair 73ee2705+b005545e whose own commit message reads
"HELD for coordinated-go" (the LD-0277 AoR go-live FE half; backend fold switch-OFF behind the
INF hold). Per the v2.1.130/135 passenger discipline I surfaced the full delta to Andrew
in-session with three options -- (a) POSN-only cherry-pick [recommended], (b) full merge minus
the held pair, (c) full merge as-is -- with option (c)'s preview text explicitly stating: "PROD
gets: everything on DEV, including 73ee2705 noel_soderblom allowlist (HELD)... it ships a lane's
explicitly HELD work outside its coordinated-go." **Andrew selected option (c) "Full merge
as-is" (in-session UI selection, 2026-07-15 ~14:4xZ, with the held-status in front of him).**
That selection is the sovereign authorization for the AoR FE half reaching PROD. The backend
fold remains switch-OFF; the INF hold is UNCHANGED; CTO flagged as LD-0277 gate owner (COO
routed). The FE allowlist on PROD does not release anything by itself.

## Deployment Sequence (/prod-deploy, all steps)
| Step | Action | Result |
|---|---|---|
| 0 | Gate + freeze | DT lane OK; inbox pulled (no STOP); freeze MCP'd to COO 14:36Z -> routed fleet-wide, 0.5.0~A's uncommitted shared-tree WIP (TicketCenter/Panel/SectionCard) specifically held + safe |
| 1 | DEV hygiene | main tree on DEV; local==origin/DEV (03719032); foreign WIP uncommitted (cannot ride) |
| 2 | typecheck | binding check = worktree push-time tsc (main tree carried foreign WIP); my commits tsc-clean at their own pushes |
| 3 | re-assert local PROD | update-ref -> d882b24f (v2.1.135 head) |
| 4 | worktree merge | .runtmp/portal-promote-20260715T150627Z; FOREGROUND bun install (420 pkgs, 218.8s); merge --no-ff origin/DEV (9 files, +724/-59); parity gate `git diff origin/DEV HEAD` EMPTY; push PROD d882b24f..2b066e01 (VALGATE D-1 PASS + push-time tsc PASS) |
| 5 | CI verify | run 29427465641 status=completed conclusion=success (gh run view --json, not watch); tag portal-v2.1.136 peel-verified ^{commit}==2b066e01==origin/PROD |
| 6 | pointer | CLOUD d374baf2c -> portal 03719032, pushed |
| 7 | teardown | worktree removed + pruned (clean this time, no long-path residue); main tree DEV; pwd=root |
| 8 | report | RAVC GREEN to COO 15:26Z -> freeze RELEASED fleet-wide 15:27Z; closure commit dd05e6af4 CC'd |

## Verification (exercise, not config-read)
- Blend math vs REAL served positioning_data.json (2026-07-12 partition, pulled from
  s3://opal-data-portal-v2, injected via Playwright route interception past the dev-bypass 401
  wall): even-weight benchmark blend FI 51 / EQ 49 EXACT; cost 17.21bps == (3+7.35+20.40+27.65+27.65)/5;
  beta 1.04 with UST null skipped (null-skip averaging). INT pair renders benchmark 40/60 opaque
  vs actual 31.1/68.9 translucent -- Yang's "69 vs 60" on screen.
- Holdings clamp measured live: rendered 583px at 720px viewport (81vh) vs 446px (62vh) = 1.307x.
- Portfolio + Benchmark views regression-screenshot-identical (single opaque bars; no-ghost path
  untouched). QA evidence: deliverables/posn_bmkviz_qa/ (6 screenshots).
- Andrew live-smoked every round (the render-LOOK control applied by the sovereign himself, per
  COO's 14:40Z relay note).

## Current State
- LIVE PROD: portal-v2.1.136 (2b066e01), CI SUCCESS, tag peel-verified. Positioning Custom view
  benchmark-basis with juxtaposed pairs; Holdings Breakdown +30pct; TicketCenter P0 page now
  reachable through its already-live CF behaviors; Vident guard + LD-0273 CI gate on PROD.
- Workspace CLOUD pointer d374baf2c -> portal 03719032. Main portal tree on DEV (Rule 19 held).
- POSN_BMKVIZ CLOSED COMPLETE (dd05e6af4, 2-step atomic, CC COO). Freeze released.

## Next Steps
- [standing, next portal UI work] The 14:40Z Andrew-direct relay binds forward: silver-canvas
  color law (portal/CLAUDE.md, landing from 0.5.0~A's WIP) + render-LOOK-commit control
  (/frontend-dev skill; the control is the SCREENSHOT) + portal/scripts/ui-smoke.mjs.
- [parked, discussion open] The Yang-call residual YALP_PKLAUT (Bloomberg PKL intake automation)
  + POSN Mode-B interpolation spec remain unregistered options from the b36cf961b analysis.

## Blockers
None.

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| comp-grep (x5) | PFOE decode across portal; registry/project sweeps (POSN_/YANG_/SSCN_, advisor-of-record, Alyssa/Bloomberg) | Routed the whole Yang-call estate mapping; PFOE=SSCN preset found via SecurityScanner constants |
| comp-transform schema-check PositioningSummary | data-prop contract before/after the Custom-view change | "All rendered fields match their response types" (clean) |
| comp-pulse diff (auto, safe-commit x5) | pre-commit risk reflex on every workspace commit | REFLEX CLEAN x4; 1 measured [HOLD] on the portal gitlink (read citation: CI-checkout note; pointer bump is the sanctioned op) |
| (in-band gates) | VALGATE D-1 (DEV x2 + PROD pushes), push-time tsc, surface-check via safe-commit | All PASS |

No comp-iam/comp-pipescript runs -- FE-only project, no IAM/Lambda/gold surface. Raw greps were
pipe-scoped or comp-grep; one Grep-tool VTT scan (transcript file outside repo scope).
