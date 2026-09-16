# L4-R REVIEW -- POSN_ASTTAX PRD v0.9 @8eabf98d81, BRIEF HALF -- SIGN

**Reviewer:** 4.0.0_SA_CRO~Z (brief half; `TREE_PRD_SIGNOFF`)
**Delivered by:** `1.0.0_SA_CTO~Z` msg 22969 (the CTO's one L10 send for round 5), 2026-09-15T03:03:37Z
**Reviewed:** 2026-09-15 ~03:1xZ (fifteenth review of this PRD by this seat)

## CONTROLS RUN BEFORE THE STAMP

| control | read | result |
|---|---|---|
| last-touch of the PRD == the review pin | `git log -1 -- prd/POSN_ASTTAX_PRD.md` -> `8eabf98d81` (1.0.0_SA_CTO~Z, 2026-09-14T23:02:51-04:00) | MATCH |
| bump scope measured | `git diff --stat 709d7b4221 8eabf98d81 -- <prd>` -> 1 file, +87 / -2 | header version + `endpoint_outcomes` += FWD-7; ONE new s.0 ADDENDUM v0.9 block; FWD-7 appended inside ENDPOINT; nothing else moved |
| which half changed | ENDPOINT gained FWD-7 (CVO half); the addendum is brief half | both halves re-open, as the send says; `prd-signoff.py status` before the stamp: both STALE |

## CONTENT CHECK -- each entry against the word it carries, CONTENT not pointer

| entry | carries | source word | verdict |
|---|---|---|---|
| verbatim block | ~00:4xZ (legend shows only present classes) @85621749e2; ~02:1xZ (no row for an absent class; Satellites Holdings Breakdown empty) @65410eedaf; ~02:3xZ (fix tonight, ad hoc) @0553548fe2 | relays 22954 / 22960 held by this seat; all three pinned | byte-faithful; every citation carries a vintage this time |
| FWD-7 (addendum copy) | each holding's characteristics and performance in the Satellites Holdings Breakdown; EXERCISED; blank only where nothing prices the holding | ~02:1xZ word | content present; the ENDPOINT copy is the CVO's to sign |
| C-HOLDING-MEASURES | `tickers` block per artifact: fee / aum / active / yield / duration / credit / beta / returns / source; precedence Yang row -> Bloomberg partition -> NULL; adapter attaches, no arithmetic; measured basis 25 tickers, 23 Yang, GLD bbg-only, CASH none; `aum <- FUND_TOTAL_ASSETS` and `fee <- FUND_EXPENSE_RATIO` unit-equal on 5 of 5 overlapping tickers; active/credit NULL for a bbg-sourced ticker; GLD returns NULL disclosed as a vendor-pull gap | Z-S132 (spec gap) + brief R4 as refined by card 6 | content present with denominators; matches |
| C-PRESENT-CLASSES | one presence set per render drives legend, Asset Class rows, section count; `ASSET_CLASSES` order/colours; colours keyed by class so hiding shifts nothing; FWD-6 grading rule stated, ratified text untouched | ~00:4xZ + ~02:1xZ words; Z-S118 / Z-S131 | content present; matches |
| C-SUMMARY-COPY | third percent label rounds (`:1011`); Satellites footer names `holdings.json` `as_of` + Black Diamond; subtitle/unresolved notice stop describing the removed blend | Z-S115 / Z-S117 / Z-S119 | content present |
| C-B4-SCHEDULE | `cron(30 12 * * ? *)` UTC, after the 07:00 America/New_York pull in both DST states; never success-of-upstream; driven run with explicit `bbg_as_of` under its own halves; scheduled fire = organic leg | Z-S120 / Z-S130; CLAUDE.md scheduled-not-triggered rule; Andrew-direct 2026-09-10 no-wait | content present; matches |
| cells B6 / F4 / F5 | guidance, not a dispatch; disjoint files; B6 precedes F4's bar | -- | consistent with the eight-cell shape and the freeze |

## TWO NOTES, NON-BLOCKING, RETURNED BY PINNED LINE

1. `POSN_ASTTAX_PRD.md` @8eabf98d81, ENDPOINT block, the line under FWD-7 *"(appended v0.9 at L10 on Andrew-direct
   ~02:1xZ / ~02:3xZ, records @65410eedaf / @0553548fe2)"* is a PROVENANCE line inside ENDPOINT -- the same shape
   `3.0.0_SA_CVO~Z` refused at v0.7 (f5ec8353e0) and the CTO then deleted (99cc431075). Not this seat's half; flagged
   because Andrew wants tonight and a second refusal cycle costs an hour. The addendum already carries the provenance.
2. C-HOLDING-MEASURES discloses GLD's performance cells as NULL because the ETF pull "carries no return field". The same
   pull's `history_topup` gained GLD and VXX daily rows on 2026-09-11 (CTO 22899: +2 rows), so return WINDOWS are
   computable from history for a bbg-sourced ticker if Andrew wants them -- a B6 design option to put to him, not a spec
   defect and not a reason to withhold.

## VERDICT

**SIGN.** Stamp: `python .tools/prd-signoff.py sign POSN_ASTTAX --half brief --review <this file>@<its pin>`.
