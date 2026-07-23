# Deploy Completion — MDPF Plain-Interpolated Label + W-3b Tooltip-Anchor Promote (portal DEV->PROD v2.1.147)

**Status:** CLOSED — completed in-session (NEVER#5). PROD 7ac7bafd, tag v2.1.147 peel-verified.
**Closed:** 2026-07-23T21:03Z
**Owner:** 0.2.0_DT_PortfolioAnalytics
**Authorization:** COO GO 204916Z (all three stated gate conditions MET), aligned with CTO bundle plan
201700Z/202837Z. Closes Andrew's twice-raised 2x-Total tooltip complaint (W-3a live in v2.1.146,
W-3b rides this head) + the Andrew-direct plain-Interpolated label.
**Window:** 2026-07-23 ~20:52Z (GO / begin) -> ~21:03Z (CI SUCCESS + tag peel-verified)

## Scope
Promote portal DEV @**17c1152b** (DE's BUNDLED head) -> PROD. Two commits vs PROD:
- `e99583f6` — plain-"Interpolated" band label (Andrew-direct 2026-07-23; removes the confidence-range
  disclaimer, superseding the earlier co-sign confirm-#2). Confidence values remain in the artifact and
  the paired accessor.
- `17c1152b` — W-3b: tooltip Total AUM ANCHORS on the TOTAL series (partner_custody_total via the paired
  aggregate read); rows carry total_aua; buckets detail; non-model balance.

## Rollback
Rollback ref = PROD **41ce41eb** (current head, tag portal-v2.1.146).

## Gate conditions met at GO (COO 204916Z)
- COMMITTED: 17c1152b on origin/DEV; tsc + provenance-guard clean.
- 4-VIEW DOM PASS: Global 0 interp-regions / 49F 0ra / INF 0ra / COT 1ra (band retained on COT, label
  now plain "Interpolated").
- W-3b MUTANT PROOF (discriminating, real served bytes, pinned 2026-07-15): pre-fix naive 558.4M
  (doubles the model term) CAUGHT; post-fix anchored 435,714,870.67 EXACT == partner_custody_total;
  identity modelSum + non_model == total to the cent. Evidence @899a0854a.

## Evidence
| Gate | Result |
|---|---|
| Delta at GO | 2 commits origin/PROD..17c1152b (e99583f6 + 17c1152b); origin/DEV == 17c1152b, main tree CLEAN at that head |
| Typecheck (pre-promote, re-baselined on 17c1152b per COO) | GREEN rc=0 |
| bun install | foreground rc=0 (420 packages) |
| Merge | --no-ff `7ac7bafd` of EXPLICIT SHA 17c1152b (not the moving origin/DEV ref); parents == 41ce41eb + 17c1152b EXACTLY; 1 file (ModelPortfolios.tsx, +26/-20) |
| Parity gate | git diff 17c1152b HEAD == EMPTY (vs the explicit target) |
| Push gates | provenance-read guard clean, VALGATE D-1 PASS, push-time tsc PASS |
| PROD commit | 7ac7bafdf0753d08a0c5122c19f72ac41931b91b (41ce41eb..7ac7bafd) |
| CI | run 30044378856 conclusion: success (gh run view --json), headSha 7ac7bafd |
| Tag | portal-v2.1.147; annotated; peeled ^{commit} == origin/PROD head EXACTLY |
| Workspace pointer | CLOUD bump f6b24a13 -> 17c1152b, gitlink VERIFIED pre-commit == exactly what PROD carries; main tree CLEAN at 17c1152b and origin/DEV unchanged at commit time (no dirty-WIP capture, unlike the 146 close) |
| Main tree | back on DEV @ 17c1152b, verified; ended at workspace root; worktree pruned (physical dir persists, Filename-too-long, inert) |

## Exercised limb (COO, folded)
The single live-PROD render of this bundled head closes the exercised limb for BOTH v2.1.146 (Global
suppress) and v2.1.147 (label + W-3b) in one shot — COO folded the 146 render into it.
