# L4-R REVIEW -- ETFS_RIVALS PRD v0.18 corrected @1fe8dd0132, ratified-text half -- SIGN

**Reviewer:** `3.0.0_SA_CVO~Z`. **Delivery:** `1.0.0_SA_CTO~Z` msg 30622. **Prior signed:** v0.18 @e0e0c3cf78 (review
@fe586ea2e2, sign-off @fbabb6319c). **Reviewed bytes:** `git show 1fe8dd0132:org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`,
ratified-text half_hash **06d168913eee8e44e876294c9c65cb7b4348f07e6c980e8b74388369920adcd1** (`prd_signoff_lib.half_hashes`).

## The change since @e0e0c3cf78 (two commits, `96c1938b74` and `1fe8dd0132`)

| change | read |
|---|---|
| `FWD-22` gains a HOVER line: pointing at any part of the curve reads the day's price and date; "FWD-22 is NOT REALIZED without it" | **This applies the earlier review's condition exactly.** His words, "just like in market overview", are now in the fence |
| `FWD-22` RESERVED narrows to one point: whether the page may carry ONE script | the right question |
| `FWD-23` gains UNIT: one unit for all three periods; calendar or NYSE trading days is RESERVED to Andrew; no 90d or 365d cell is cut until he answers | correct. His 2026-10-04 word set 30 days as "the last 30 trading days", so the unit is a real fork (365 trading days is about 17 months) |
| `FWD-23` gains AMENDS: `FWD-14` and `FWD-19` where they name the displayed periods | correct. Both fences name "30 trading days" and "quarter and year to date" (`:258`, `:276`), and an unamended fence would contradict `FWD-23` |
| F.3 card 1 reworded; F.4 corrected | they agree with the fence |
| F.5: Andrew's answers, and the ruling that the curves live in a per-fund chart object behind one gateway route | see below |

## F.5 against Andrew's words

The record is `cooRV_ANDREW_DIRECT_20261007_051xZ_RIVALFUNDS_BBG_BACKFILL_YES_PAGE_ONLY_HIDE_MTD.md` (33 lines, read whole).

- **"Yes for the rivalfunds funds only. Probably an ad hoc backfill for the selected funds that uses the existing BBG route":**
  F.5 holds the vendor word at that reach. It covers Bloomberg daily closes, those funds' securities, and about 365 days. It is ad
  hoc and not a schedule, and no Positioning file changes.
- **"rivalfunds page only":** F.2's scope is confirmed.
- **"Yeah can hide MTD too":** F.2's MTD ruling is confirmed. This closes item 1 of the earlier review's recorded points.

The curves-in-their-own-object ruling is the CTO's, on a measured size finding (417 B per fund section against about 1,500 B per
curve). The address is stated as `address()` output, and the route is released by NFRA_OPLGTW. No new address is typed in the PRD.

## Recorded, not blocking

1. **The backfill depth and the unit are coupled.** The authorized depth is "about 365 days" of closes. If Andrew answers
   "trading days" for the unit, a 365-trading-day window needs about 17 months of closes, which is deeper than the word given. The
   unit card should say so, so that one answer settles both.
2. **Card 1 answered NO leaves `FWD-22` unrealizable as written.** The no-script branch (a link to a chart page) has no any-day
   hover, and the HOVER line makes that hover part of the outcome. A NO therefore needs an ENDPOINT amendment, not only a build
   choice. F.5 item 3 should say so.
3. **`C-SECURITY-UNIVERSE`** still does not say which of the two daily fires writes the date's object (carried from the earlier
   review).

## Verdict

**SIGN**, ratified-text half, at half_hash 06d168913eee8e44e876294c9c65cb7b4348f07e6c980e8b74388369920adcd1.

-- 3.0.0_SA_CVO~Z
