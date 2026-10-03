# DSGN_AMGTV1 round 27 -- CTO product-file review of portal df019dba (AV-ze-1, served identity on hover)

**Reviewer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~15:4xZ. **Ask:** `2.0.0_SA_COO~D` msg 28555. **Candidate:** portal df019dba (worktree
`C:/tmp/wk-dsgn-amgtv1-70`, branch `dsgn-r27-onto-dev`). It is remote DEV 415f50db plus worker commit f0683e8f, a fast-forward.

## Diff read in full (3 files, +73 / -3)

- **`PriceBars.tsx`:**
  - `hoverText` joins the served name and ticker, asset class, sub-asset class, sector, the 30-day value (through the existing
    `valueText`) and `movedWords`.
  - A null `places_moved` prints the served reason through `guardedReason`, and an absent one prints "places moved not served".
  - The hover is the `title` attribute on the bar's HTML `<li>`, which renders natively.
- **`ChatterBubbles.tsx`:** the same shape, as an SVG `<title>` child of the circle, which is the correct tooltip carrier for SVG.
  The fields the chatter row does not serve today print "not served". Nothing is joined from the rankings payload (the FWD-2
  served-identity rule).
- **`types.ts`:** optional `ticker`, `classification`, `places_moved` and `places_moved_reason` on `CollectedChatterRow`. They are
  absent today and land with RESAPP round 63 cell 3.

## Checks

- **`tsc -b --noEmit` on df019dba:** rc=0, run by this seat in the worktree.
- `monthWords`, `valueText` and `guardedReason` (`reasonWords.ts:40`) all exist at df019dba.
- `RankingRowBase` already types `places_moved` / `places_moved_reason` (types.ts:166-169).
- The diff carries no non-ASCII and no device path.
- COO~D's checks: identity.cjs 3/3; round-26 battery ALL PASS; walk 20261002T144632Z (104 shots). The hover titles are blind to
  the walker and are graded by the check.

## Verdict

**APPROVED.** The landing follows the standing route: the candidate is merged onto the CURRENT remote DEV head at push time, and
VALGATE runs on the push. The PROD promote stays Andrew's to name.

**Not covered by this approval:** the bubbles' identity stays "not served" until RESAPP r63 cell 3 serves it. FWD-2 grades
REALIZED only on the served read after that.
