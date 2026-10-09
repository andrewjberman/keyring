# DSGN_AMGTV1 -- ROUND 59, ROUND-N ANALYSIS + CANDIDATE REVIEW (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~07:3xZ)

**Inputs:** `deliverables/2.0.0_SA_COO~D1/round59/ROUND59_CLOSE.md` @30d998caf7 (msg 1963). Candidate portal `3ea5d0f9` = DEV `29b18a8c`
+ 7 commits, branch `cand/dsgn-amgtv1-r59b`. The walk register is SAW-01..23 (Andrew ~05:0xZ).

## 1. Candidate review: APPROVED for DEV

Read: `git diff 29b18a8c 3ea5d0f9` covers 22 files, all under `src/pages/SecurityAnalysis/` (+720 -659).
- **No new data call:** no added `fetch`, `apiRequest` or `useQuery`, and no file under `src/api`. C-PRESENTATION-ONLY holds. The News
  tab reads only the cached /thesis bundle.
- **R2 held:** `<IdentityLine` is mounted 0 times across the five tabs. Identity is said once, in the header.
- **R3 held:** `reasonWords.ts` is unchanged, so served reasons are placed, not reworded.
- **R4/R5 held:** the collection legend is gone from the spine, 5 top days are marked, and there is one deduplicated news surface on its
  own tab.
- **Layout:** the tabs start at ~500 px, against ~2,000 before.

The box manager lands the fast-forward (law edit 4597dfacc6). If DEV moved, it is re-cut on DEV's head, the same rule as round 58.

## 2. Graded (against the register)

SAW-01..23 are dispositioned in the close, with two rows ruled there. These read MET on DEV once the candidate lands: tabs ~500 px
(SAW-20), news once (SAW-05/09), absences once (SAW-10/11/15/16), and the spine's top days (SAW-01/03). The repair list in section 3 is
what remains. FWD-1 is still Andrew's PROD walk; PROD carries rounds 53-57 and takes 58-59 at the next promote.

## 3. ENRICHMENT LIST (round 60, ONE issuance by `2.0.0_SA_COO~D1`) -- the close's repair list plus one

1. The battery29 re-anchor.
2. The footers: one as-of per card (SAW-13), the cell deferred from round 59.
3. The description line.
4. The mixed-currency line.
5. One raw-millions row.
6. The news open count.
7. **Added by this review:** the spine's per-day detail still carries collection bookkeeping, at `TimelinePanel.tsx` 520-527 and 619-632
   ("Searched: ...", "Not searched on this day", "had no search run"). Andrew called that layer irrelevant under backfill. The day detail
   keeps the day's articles and events. The search-coverage lines leave the reader's face; an empty day says "No articles on this day"
   once.

Then a PROD promote of rounds 58-60 under a pair, as for `bf780f94`, so Andrew's FWD-1 walk reads the redesign.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- FWD-1's walk of the redesigned page on PROD (hand-over, "Acts only Andrew can do").

-- 1.0.0_SA_CTO~DELL1
