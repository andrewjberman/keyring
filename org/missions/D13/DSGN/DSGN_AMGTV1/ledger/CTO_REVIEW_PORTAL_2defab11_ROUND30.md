# DSGN_AMGTV1 round 30 -- CTO product-file review of portal 2defab11, `1.0.0_SA_CTO~Z`, 2026-10-03 ~01:5xZ

**Ask:** `2.0.0_SA_COO~D` msg 28865. Worktree `C:/tmp/wk-dsgn-amgtv1-82`, branch `dsgn-r30-onto-dev`, portal HEAD `2defab11b6` (clean
tree). It is the approved round-29 candidate e370eb7c (review @a43b54dfee) plus zh-1 `df863c97` and zh-2 `621f553e`, merged with DEV
`c9d303db`.

## What I read (the round-30 product diff, e370eb7c..7ade6779: 9 files, +55/-32, every hunk)

| file | change | verdict |
|---|---|---|
| `useLeadPanelApi.ts`, `LeadPanel.tsx` | The ranking read is `enabled` on the Price face only. The Chatter face issues no ranking read. The starred join is read off the served collected rows (`security_key` + `ticker`, RESAPP am-3). `ResolutionNote` is no longer rendered, which removes the "(movement is measured)" system words. `chatterData` is declared (:434) before its use. | OK: one served universe per face (Z-W208-S1). |
| `chartColors.ts`, `ChatterBubbles.tsx` | The hard-coded `#cbd5e1` moves into the palette as `CHATTER_NO_TONE_FILL`. It is an additive export, and both uses read it. | OK: FWD-23's token. |
| `SecurityOverlay.tsx` | The Refresh primary uses the canonical `buttonClass('primary', ...)` ink, not a hand-written white. The identity header is tighter (gap 2, p-3, band h-10). | OK. |
| `HeaderBrief.tsx` | At most 2 feed items are open at rest. An item with no url renders as a plain title, not a link (the ruling on the feed's `url: null`). | OK. |
| `TimelinePanel.tsx` | Chart height 240 -> 200 (first viewport). | OK. |
| `WhatChangedPanel.tsx` | An unformatted figure now prints at its Model-sheet row's display precision (`formatSheetValue`). The full served values stay in "Full figures". | OK: page formatting only (FWD-27 v0.13). Served prose is untouched (C-PRESENTATION-ONLY). |
| `renderCheck.tsx` | The persistent-panel probe reads `data-header-action="back"`. | OK (check code). |

## Measured by this seat

- `tsc --noEmit -p tsconfig.app.json` on 2defab11: rc=0, 0 lines, 17 s.
- Ancestry: e370eb7c and c9d303db are both ancestors of 2defab11.
- **Origin DEV has moved to `8526dacb`** (one commit, DSGN_REBRND round 3 E2 under COO~D's FAST lease, `src/pages/Positioning/*` only,
  0 SecurityAnalysis files). `git merge-tree --write-tree 8526dacb 2defab11` gives rc=0, a clean merge. The candidate is therefore NOT
  a fast-forward of current DEV. The landing merges DEV first; a rebase is never used on the shared branch.

## Not met, and placed

- **SAUX-15's first viewport:** the tab underline moved 963 -> 917 px, but the served feed grew from 1 item to 69. Showing 1 item at
  rest is a round-31 item (COO~D's close, `round30/ROUND30_CLOSE.md`).

## Verdict

**APPROVED** for portal DEV as one landing that carries rounds 29 and 30 (e370eb7c + zh-1 + zh-2), merged onto the DEV tip of the day.
The DEV push is `0.0.0_AB_MSTR~Z`'s on Andrew's word (CLAUDE.md, Portal: a product-file candidate is pushed by MSTR on Andrew's word).
Round 29 already waits on that word, and this approval adds round 30 to the same push. PROD stays gated.

## ADDENDUM 1 (`1.0.0_SA_CTO~Z`, 2026-10-03 ~16:4xZ) -- origin DEV moved to `525c9404`; the landing terms admit it

Asked by `0.0.0_AB_MSTR~Z` (msg 28885). This seat read the DEV side (`c9d303db..525c9404`, 35 commits after `8526dacb`, all laptop
COO~D FAST) on the two overlapping paths, every hunk:
- **`__rendercheck__/renderCheck.tsx`:** one comment and one offender-fixture string change from "silver canvas" to "light canvas".
  The text is all that changes, and no predicate moves. Round 30's change to the same file is the `persistentPanelPresent` probe, on
  a different line.
- **`src/lib/chartColors.ts`:** DEV adds `pink400`, a contrast note, `CLASS_INK_ON_DARK` and `getAssetClassInkOnDark`. Round 30 adds
  `CHATTER_NO_TONE_FILL`. Both sides are purely additive.
- `git merge-tree --write-tree 525c9404 2defab11`: rc=0, clean.

**Verdict unchanged: APPROVED.** The landing merges current DEV first (no rebase), MSTR~Z runs battery29 on the merge, and the push
is on Andrew's word. A battery failure on the merge is a STOP, and the merge goes back to COO~D.
