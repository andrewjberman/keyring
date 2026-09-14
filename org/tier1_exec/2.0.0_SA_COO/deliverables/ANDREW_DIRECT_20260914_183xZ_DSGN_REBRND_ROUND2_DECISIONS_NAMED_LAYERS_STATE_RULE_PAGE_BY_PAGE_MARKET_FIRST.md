# ANDREW-DIRECT 2026-09-14 ~18:3xZ -- DSGN_REBRND ROUND 2: NAMED LAYERS; TEXT FOLLOWS ITS CURRENT BACKGROUND; PAGE BY PAGE, MARKET OVERVIEW FIRST; KEEP THE SIDEBAR'S INDIGO EDGE; TOOLTIPS TO BE CLARIFIED

**Terminal:** `2.0.0_SA_COO~D`. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn.
**Answers:** the five decisions put to him at this terminal from the investigation
`DSGN_REBRND_ROUND2_TEXTURE_AND_INVERSION_INVESTIGATION_20260914.md` @1dbd5f2d1c, section 5.

## VERBATIM AND ENTIRE

> 1.) Named layers is fine. 2.) Text follows its current background is a good rule. 3.) Let's try it page by page, I
> will visual smoke and comment accordingly, starting with Market Overview page. 4.) I like faint indigo edge on the
> sidebar, I honestly think that the original sidebar coloring/setup (on DEV Branch) was fine, will see what the
> current version looks like in the interim and make a call later if we keep it as is or just revert to the DEV
> branch implementation. 5.) There are three types of tooltips that vary slightly so id have to clarify each for you.

## WHAT IT SETTLES

1. **TEXTURE IS NAMED LAYERS (option C).** One role table (page, strip, body, tile, inset, hover, selected, tooltip).
   Each role has an opaque rung in BOTH worlds, with the same separation ratio between neighbouring roles, under his
   ONE-opacity rule. The inversion is then a token swap per role.
2. **THE STATE RULE IS LAW: text follows its current background.** Ink is computed against the ground of the CURRENT
   state (rest, hover, selected/highlighted, focus, disabled), never the resting ground. So a light highlight on a dark
   component flips its text dark, and a dark highlight on a light panel flips it white.
3. **DELIVERY IS PAGE BY PAGE, STARTING WITH MARKET OVERVIEW (`/market`).** He visually smoke-tests each page and
   comments, and the next page follows his comments. That makes the round shape one page per slice, gated on his read.
4. **THE SIDEBAR'S FAINT INDIGO EDGE STAYS** (row `DSGN_REBRND-W2-S19`: the rail's 30%-alpha accent border-image,
   `portal/src/App.tsx:265`).
   - This is his word extending FWD-4's closed identity set by one member, the rail edge. The set's own terms are
     "extended only by his word".
   - The larger sidebar question is OPEN at him: keep the current treatment, or revert to the DEV-branch sidebar
     implementation, "a call later".
5. **TOOLTIPS: OPEN AT HIM.** There are three types that vary slightly, and he will clarify each. No tooltip cell is cut
   before he does.

## WHAT IT DOES NOT SETTLE

- **The sequence of the round.** Canonical order stands. Round 1's L10 slug is `3.0.0_SA_CVO`'s, and L8/L9 run in the
  feature worktree (96665). Next comes `1.0.0_SA_CTO`'s round-2 PRD addendum and its two L4-R halves, then this seat's
  ONE issuance. A round-2 order cut before round 1's slug would deadlock round 1's L10 (CLAUDE.md Rule 27, LD-0521).
  Preparation for the `/market` slice proceeds now; issuance does not.
- **The sidebar revert, and the tooltip specification.** Both are his.
- **The portal freeze, and the feature-branch confinement.** Both are unchanged.
