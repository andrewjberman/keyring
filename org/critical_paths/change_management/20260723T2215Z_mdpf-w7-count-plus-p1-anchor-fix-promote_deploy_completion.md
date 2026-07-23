# Deploy Completion — MDPF W-7 Count Anchor + P1 Tooltip Value-Anchor Fix (portal DEV->PROD v2.1.148)

**Status:** CLOSED — completed in-session (NEVER#5). PROD 17256834, tag v2.1.148 peel-verified.
**Closed:** 2026-07-23T22:32Z
**Owner:** 0.2.0_DT_PortfolioAnalytics
**Authorization:** COO GO 221251Z (verification complete on COO's co-signed bytes; CTO CC-informed in
parallel — fire on rebaseline-pass unless CTO or COO flags a hold in that window; no hold received).
**Window:** 2026-07-23 ~22:15Z (GO / begin) -> ~22:32Z (CI SUCCESS + tag peel-verified)

## Scope
Promote portal DEV @**343e7b2a** -> PROD. Two commits vs PROD:
- `af0867e9` — **W-7 producer count anchor** (closes Andrew's 3rd on-screen ask, the Christmas-cliff
  count swings): `readCountTotalSeries` (paired: account_count_total + count_provenance, tolerant,
  honest-None bridges exempt dates); count rides aggregate rows (global + per-firm) and both chart row
  sets; count-mode tooltip Total anchors on the producer total (client per-model count-summing was the
  exempt-date cliff class, now structurally bypassed); guard WIDENED to forbid direct reads of the two
  count arrays.
- `343e7b2a` — **P1 fix (suspect-b CONFIRMED):** v2.1.147's tooltip value-anchor was MIS-SCOPED to
  Global. W-3b's contract is `partner_custody_total` (PER-FIRM); Global's aggregate is the MODEL-ONLY
  sum, so the live Global tooltip Total dropped ~420M of non-model (showed ~1.53B beside rows composing
  ~1.95B). Anchor is now per-firm-only at both chart sites; Global falls back to the bucket sum (correct
  enterprise composition = the pre-147 behavior). The count anchor is untouched — its Global
  producer-total IS the W-7 co-signed contract.

## Provenance note (recorded honestly)
The P1 this fixes RODE IN WITH v2.1.148's predecessor — my v2.1.147 promote (`7ac7bafd`). It was gated
at the time (DE 4-view DOM PASS + W-3b reproduce-then-kill mutant on real served bytes, COO-verified);
the Global mis-scoping was not caught by that gate because W-3b's mutant exercised the PER-FIRM contract
where the anchor is correct. Recorded so the gate gap is visible, not to relitigate: a per-firm-scoped
mutant cannot falsify a Global-scoped mis-application.

## Rollback
Rollback ref = PROD **7ac7bafd** (current head, tag portal-v2.1.147).

## Gate conditions met at GO (COO 221251Z, on COO's co-signed bytes)
- VALUE/ANCHOR P1 FIX: pre-fix Total 1,676,493,815.12 ties COO's co-signed model_aua 1,676,493,815.11
  TO THE CENT — confirms a model-only anchor. Post-fix Total 1,951,161,735.56 displays 1.95B == radial
  at display precision. Decomposition verified against COO's bytes (model exact + non-model).
- COUNT (co-signed): global /global/ 55a8b379 byte-verified + cliff mutant; all 3 per-firm on their
  consumed keys (49F 501407/408v/7,026 · INF e3c8db3/423v/534 · COT 194e5bb/2v-445absent).
- 4-VIEW DOM: Global 0ra / COT 1ra (plain label) / 49F 0ra / INF 0ra.

## Residual (COO-ruled SHIP-ACCEPTABLE, documented — not a 148 defect)
Post-fix tooltip Total sits **514,428.86 under the radial** — VERIFIED to be EXACTLY the 2-day non-model
roll-forward vintage diff (tooltip nm = non_model_assets.json 07-20 274,667,920.44; radial = 07-22
275,182,349.31; diff ties to the cent). PRE-EXISTING (footnoted roll-forward), SUB-DISPLAY (both read
1.95B). 148 is a strict improvement with the residual unchanged.

## Evidence
| Gate | Result |
|---|---|
| Delta at GO | 2 commits origin/PROD..343e7b2a (af0867e9 + 343e7b2a); origin/DEV == 343e7b2a, main tree CLEAN at that head |
| Typecheck (re-baselined on 343e7b2a per standard) | GREEN rc=0 |
| bun install | foreground rc=0 (420 packages) |
| Hold check | inbox pulled immediately pre-merge per COO's window condition — no hold from CTO or COO |
| Merge | --no-ff `17256834` of EXPLICIT SHA 343e7b2a; parents == 7ac7bafd + 343e7b2a EXACTLY; 3 files (provenance-read-guard.mjs, pairedProvenanceRead.ts, ModelPortfolios.tsx) |
| Parity gate | git diff 343e7b2a HEAD == EMPTY (vs the explicit target) |
| Push gates | provenance-read guard clean **on the WIDENED rule** (now forbids direct reads of the two count arrays — all reads via accessor), VALGATE D-1 PASS, push-time tsc PASS |
| PROD commit | 17256834297b88f8407a3f9ba19bb90291e060ae (7ac7bafd..17256834) |
| CI | run 30049595858 conclusion: success (gh run view --json), headSha 17256834 |
| Tag | portal-v2.1.148; annotated; peeled ^{commit} == origin/PROD head EXACTLY |
| Workspace pointer | CLOUD bump 17c1152b -> 343e7b2a, gitlink VERIFIED pre-commit == exactly what PROD carries; main tree CLEAN at 343e7b2a, origin/DEV unchanged at commit time |
| Main tree | back on DEV @ 343e7b2a, verified; ended at workspace root; worktree pruned (physical dir persists, Filename-too-long, inert) |

## Post-promote (DE)
DE's post-promote live render closes Andrew's asks 1+2 + the P1 tooltip on the fixed bundle in one pass.
