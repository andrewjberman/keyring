# DSGN_AMGTV1 round 46 -- completion grade, 27 rows (3.0.0_SA_CVO~Z, 2026-10-07 ~10:5xZ)

**Ask:** `2.0.0_SA_COO~D` msg 30790 and `1.0.0_SA_CTO~Z` msg 30792. **Packet:**
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round46/COMPLETION_GRADES.round46.json` @caf62c0308.
**Graded against:** PRD v0.15 ENDPOINT, each row on its DONE WHEN. **Served:** portal DEV 8ddfe409 and PROD b06863fe
(`git -C portal ls-remote origin DEV PROD`, this seat); `git -C portal diff --stat 8ddfe409 b06863fe` is empty.

## Tally

| Verdict | Count | Rows |
|---|---|---|
| REALIZED | 20 | FWD-2, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26 |
| NOT_REALIZED | 5 | FWD-4, 7, 8, 20, 27 |
| NOT_EVALUATED | 1 | FWD-1 |
| RETIRED | 1 | FWD-3 |

Against round 41 as countersigned (19 / 5 / 2 / 1): FWD-13 and FWD-19 move to REALIZED; FWD-20 moves to NOT_REALIZED.

## What this seat read itself

- The five walk directories' result files, one verdict each: 43 PASS, 2 FAIL, 2 ERROR of 47. The packet's tally holds.
- `round46/instrument35-candidate-grades.json` whole: 65 PASS, 11 FAIL, 1 N/A of 77.
- Seven PNGs at full size: the ROG SW header and tile hover, MSFT US Peers, BA US Model (live walk, including a
  full-size crop of its foot), the 30D chatter face, the 30D price face, and the instrument's Model state.
- `21-nonusd-header.json` and round 42's `01-rog-header.json` whole; the four header-census reads' details.
- Not read by this seat: the Thesis, Exec, Posture and side-by-side PNGs; the 90D and 365D faces; CTO msg 30491
  (the re-run control's removal) and Andrew's 2026-10-05 no-permission ruling, both taken from the asks that cite them.

## The seven judgment rows

**FWD-4 -- NOT_REALIZED.** The ACCEPT is seven figures at rest in one row.
- ROG SW shows 3 of 7 (market cap CHF 287B, enterprise value CHF 313B, net debt CHF 17.71B). Price, beta, average
  volume and short interest each print the served reason. The page side passes: no tile is blank.
- **Not in the packet:** MSFT US shows 0 of 7. Every tile reads "We hold no stored company data for this name yet."
  (`tabs-MSFT-US-3-Peers.png`). Its identity line reads "sector and country are not in this security's data". So the
  gap is not confined to non-USD names.
- The two instruments disagree because they test different clauses; neither clause is the DONE WHEN. The cure is the
  producer's (AMGT_RESAPP), as the round-41 countersign ruling 2 says.

**FWD-8 -- NOT_REALIZED.** The ACCEPT says "shows readable tickers".
- MSFT US, 12 comparables: 9 print a ticker; Samsung (two listings) and SK hynix print a sentence in the Ticker
  column. The numeric codes are gone, which is the page doing its part. Three of 12 peers still have no ticker.
- The Price column is headed "currency not stated" and holds 230,500, 172,100 and 1,495,000 beside 356.62 and 589.90.
  A reader cannot compare that column.
- "TSM US" sits beside a price of 2,365. Whether that price belongs to the US listing is unread; it is worth one read
  by the producer.

**FWD-13 -- REALIZED.** The round-41 gap (the full value rode a DOM attribute only) is closed.
- The tooltip prints a "full value" row with thousands separators and its unit: "CHF 286,986,911,310", "CHF
  313,080.91131 million", "CHF 17,715 million". No raw float appears. All seven ROG tiles report tabular numerals.
- Denominator: a "full value" tooltip row is recorded on 6 tiles across 4 names (3 on ROG SW, 1 each on BA, VLO and
  AMD). The other served tiles were not hovered. One tooltip component draws all of them.
- Open and unruled: enterprise value and net debt print "... million" where market cap prints the full integer. That
  is the served unit printed as served. If one format is wanted, it is FWD-27's money-format limb.

**FWD-18 -- REALIZED against the outcome; the DONE WHEN needs an addendum.**
- The instrument's 10 FAIL cells have one cause: the clause wants one purple fill (Refresh) in each Security state
  and reads 0, with 0 refresh affordances. The packet says the control was removed on CTO msg 30491.
- The outcome and its ACCEPT ("one purple action per view") hold at zero. The list state passes every control limb.
- The DONE WHEN's "== 1 (Refresh) in Security mode" can no longer be met. The addendum and the instrument clause are
  the CTO's. Until both move, the instrument cannot PASS (see FWD-20).

**FWD-19 -- REALIZED against the outcome; the DONE WHEN needs an addendum.**
- Empty, loading and error are each captured on 6 of 6 panels (`fwd19_designedStates`, PASS); the loading and error
  panels read DESIGNED on BA US and AMD US in the live walk.
- The no-permission arm fails as designed: the packet and CTO msg 30792 both state Andrew removed that screen on
  2026-10-05. Its replacement read passes both ways: 2 of 36 sidebar links for the Opal viewer, 0 of 14 for the
  simulated non-Opal viewer.
- The PRD still names PanelNoPermission. Graded on the outcome, as the CTO asked.

**FWD-20 -- NOT_REALIZED.** The DONE WHEN is that the render check PASSES. It reads 65 PASS, 11 FAIL.
- 10 FAIL cells are the stale FWD-18 clause above.
- 1 is a page defect: the Model state carries text at 10 px (48 text nodes), under the contract floor of 11. It was
  not there at round 41 (76 / 0 / 1).
- The "can fail" half holds: 4 of 4 arms. The person's read of the six PNGs is partly done here (two of six states).

**FWD-27 -- NOT_REALIZED.** Two limbs fail on the live BA US Model tab (`tabs-BA-US-4-Model.png`, foot).
- One display name per security: the tab prints "Company short name: BOEING CO/THE" on the same page as "The Boeing
  Co". The packet says this line was not re-read. The display-name reads (4 PASS) did not reach it.
- System wording: "2 of 6 inputs have run" and "News: a source this page has no name for yet".
- What moved and holds: the Price face prints title-case names; Escape closes the account menu.

## The other rows

- **FWD-1 -- NOT_EVALUATED.** The DONE WHEN is Andrew's own signed-in walk on the live product. PROD now carries the
  walked content, so nothing but his walk remains.
- **FWD-7 -- NOT_REALIZED.** Unchanged: ASML NA serves 7 officers; AMD US and MSFT US show none. Producer-side.
- **FWD-3 -- RETIRED.**
- **FWD-2, 5, 6, 9, 10, 11, 12, 14, 15, 16, 17, 22, 23, 24, 25, 26 -- REALIZED.** Each row's cited reads carry PASS in
  this walk, and the instrument cells they cite (fwd14, fwd15, fwd16, fwd17, the band clause on 6 of 6 states) read
  PASS. FWD-5's AMD marker read is an ERROR by cause (AMD serves 0 events). FWD-25 is read by this seat on the live
  BA US Model tab: "What changed" heads the tab, 0 added and 31 changed, version times in ET.
- **FWD-21 -- REALIZED, with one reading call for the CTO.** The 30D face shows 57 of 95 names in one panel with a
  tone legend. Ten outer labels end in an ellipsis ("Taiwan Semiconductor...", "The Home De...", "Kimberly..."). The
  DONE WHEN says "no label clips". I read a deliberate ellipsis as distinct from the edge clipping SAUX-17 named; if
  the CTO reads it as a clip, this row is NOT_REALIZED.

## For the round-47 list

1. FWD-4: MSFT US has no headline figures at all; ROG SW has 3 of 7. Producer.
2. FWD-8: 3 peers with no ticker; one Price column mixing currencies; the "TSM US" price to be read. Producer.
3. FWD-20: the 10 px text on the Model tab. Page cell.
4. FWD-27: the vendor short-name line and the two system-wording lines at the foot of the Model tab. Page cell.
5. PRD addenda: FWD-18 (the purple-fill count) and FWD-19 (the no-permission state), with the instrument clause.
6. FWD-7: officers for the names that have none. Producer; the Bloomberg pull is Andrew's act.

-- 3.0.0_SA_CVO~Z

## ADDENDUM (2026-10-07 ~10:5xZ) -- two things this file got wrong

Source: `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md` @50e71b5b8d (the
countersign and its CORRECTION), CTO msg 30811.

1. **MSFT US is not a covered name.** I wrote that MSFT's empty header showed the FWD-4 gap "is not confined to
   non-USD names". I did not read the covered set before writing it. `2.0.0_SA_COO~Z` measured it (row
   AMGT_RESAPP-Z-S364): MSFT is a pool record outside the 95 covered names, and 0 of 95 covered names read that way.
   The screenshot reading stands; the inference from it does not. The same applies to my FWD-7 and FWD-8 readings on
   MSFT US: each was read on a name outside coverage. FWD-7 still rests on AMD US, and FWD-8 on the table's mixed
   Price column.
2. **The prior board I compared against was stale.** The last countersigned board was 22 / 3 / 1 / 1 (2026-10-05
   ~21:5xZ, FWD-4 already REALIZED), not 19 / 5 / 2 / 1.

**The board after the CTO's correction: 21 REALIZED, 4 NOT_REALIZED (FWD-7, 8, 20, 27), 1 NOT_EVALUATED, 1 RETIRED.**
FWD-4 is REALIZED on the CTO's 2026-10-05 covered-names rule, which is in the ledger and not yet in the PRD; my
NOT_REALIZED was a reading of the DONE WHEN as written.

-- 3.0.0_SA_CVO~Z
