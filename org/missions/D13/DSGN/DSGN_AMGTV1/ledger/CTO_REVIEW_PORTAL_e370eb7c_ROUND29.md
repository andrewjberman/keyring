# DSGN_AMGTV1 round 29 -- CTO product-file review of portal e370eb7c (the Security Analysis UI/UX redesign, six cells)

**Reviewer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~00:0xZ. **Ask:** `2.0.0_SA_COO~D` msg 28812.
**Candidate:** portal e370eb7c (worktree `C:/tmp/wk-dsgn-amgtv1-82`, branch `dsgn-r29-onto-dev`). It is a fast-forward over remote DEV
39aa21c2 (ls-remote read): 28 files, +1,895 / -1,196.
**Cells:** zg-1 timeline, zg-2 header, zg-3 lead and price, zg-4 collage, zg-5 Model "what changed", zg-6 tabs and the account menu.

## What was read in full, and why those

The two changes that reach OUTSIDE Security Analysis were read line by line:
- **`src/App.tsx`** (the portal-wide shell, SAUX-35):
  - the account menu's full-page backdrop `div` is removed;
  - Escape closes the menu, as does a `pointerdown` outside the menu and its button (listeners added and removed with
    `showUserMenu`);
  - presses inside the menu are unaffected.
  - Every page gains: a click while the menu is open now reaches its target, instead of being swallowed by the invisible layer.
    Sound.
- **`src/lib/sentimentColor.ts` + `TopicCloud.tsx`** (Market Overview): `getSentimentColor` moves to one shared module, and its body
  is **byte-identical** to the pre-extraction function (stops, lerp, clamp, thresholds). Topic Cloud imports it. Market Overview's
  colours cannot change. This is FWD-21's "ONE shared sentiment-colour module".

## Checks

- **`tsc -b --noEmit` on e370eb7c:** rc=0, run by this seat.
- **0 package or lockfile changes:** no new dependency. The collage is a deterministic placement, as ruled (fold ruling 2). No
  d3/visx/apexcharts import added.
- **0 non-ASCII characters added.**
- **The issuer's battery:** battery29 with no skip ALL PASS; 12/12 round-29 checks; r27 identity 3/3; r28 fixture and render 3/3.
  Close walk 20261002T233653Z.

## One defect, routed (not blocking)

**`ChatterBubbles.tsx:75` hard-codes `NO_TONE_FILL = '#cbd5e1'`.** FWD-23's DONE WHEN reads "its colours come from
lib/chartColors.ts (0 hard-coded hex in the panel's chart files)".
- It is round 30's repair cell: the no-tone fill comes from a `lib/chartColors.ts` token.
- The legend swatch at :537 uses the same constant and follows it.
- It does not block this landing: the colour is correct and designed. Only its source breaks the clause.

## Verdict

**APPROVED.**
- It lands by the standing route: merged onto the CURRENT remote DEV head at push time, by `0.0.0_AB_MSTR~Z`, with VALGATE on the
  push.
- The PROD promote stays Andrew's word.
- FWD-23's grade on this page waits for round 30's repair of the hard-coded fill.
