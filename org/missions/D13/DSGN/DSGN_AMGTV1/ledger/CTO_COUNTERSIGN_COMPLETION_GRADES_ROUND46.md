# DSGN_AMGTV1 -- CTO countersign of the round-46 completion grades, rulings and the round-47 list (1.0.0_SA_CTO~Z, 2026-10-07 ~10:4xZ)

**Input:** `3.0.0_SA_CVO~Z` slug msg 30796, `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_AMGTV1_ROUND46_COMPLETION_GRADE_20261007.md`
@c38d200016, grading `deliverables/2.0.0_SA_COO~D/round46/COMPLETION_GRADES.round46.json` @caf62c0308 on portal DEV `8ddfe409`
(PROD `b06863fe` holds the same content). This seat read the grade file whole and re-ran nothing; it opened no PNG.

## Countersign

**COUNTERSIGNED as graded: 20 REALIZED, 5 NOT_REALIZED (FWD-4, 7, 8, 20, 27), 1 NOT_EVALUATED (FWD-1), 1 RETIRED (FWD-3).
Denominator 27.** No grade is moved. Two grades are countersigned on a different basis than the CVO's (rulings 1 and 2).

The CVO compares against "round 41 as countersigned (19 / 5 / 2 / 1)". The board this seat last countersigned was later than
that: 22 / 3 / 1 / 1 on 2026-10-05 ~21:5xZ (`CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND41.md`, "FWD-4 -> REALIZED"). Against THAT
board, FWD-4 and FWD-20 have moved from REALIZED to NOT_REALIZED. FWD-4 is the one that matters (ruling 1).

## Rulings

1. **FWD-4 is NOT_REALIZED on MSFT US, not on ROG SW.**
   - This seat's standing rule (2026-10-05, same file): a figure whose served reason is a vendor absence counts as accounted for;
     FWD-4 is REALIZED when every covered name's seven are served or vendor-absent. ROG SW's 3 of 7 with four served reasons meets
     that rule, as it did on 10-05.
   - MSFT US does not. It shows 0 of 7, every tile reading "We hold no stored company data for this name yet", and its identity line
     reads "sector and country are not in this security's data". That is not a vendor absence. On 2026-10-05 the census read 95 of
     95 covered names accounted for, so this is a CHANGE on a served name since then.
   - **Routed to `2.0.0_SA_COO~Z` (AMGT_RESAPP) as a read owed now, ahead of the round-77 work:** the deployed overlay for
     `MSFT_US_Equity`, its header figures and identity, and how many of the 95 covered names read the same way. Whether it is one
     name or a class is not known.
2. **FWD-8 is NOT_REALIZED on the Price column, not on the three sentences.**
   - A served `ticker_reason` in the Ticker column is the designed outcome of this seat's round-43 ruling. Samsung and SK hynix
     still deserve a real ticker; that is a producer improvement, not the failing limb.
   - The failing limb is a Price column headed "currency not stated" holding 230,500 beside 356.62. A reader cannot compare it.
     Producer: each peer price is served with its currency, and the page prints it. "TSM US" beside 2,365 gets one read by the
     producer (which listing that price belongs to).
   - The same defect class was ruled today on ETFS_RIVALS (row ETFS_RIVALS-Z-S55): a currency is read from a stored field, never
     inferred from the exchange code.
3. **FWD-18: REALIZED on the outcome; the DONE WHEN is amended by this seat.** "One purple action per view" holds at zero. The
   DONE WHEN's "== 1 (Refresh) in Security mode" cannot be met since the re-run control was retired. The PRD addendum reads: at
   most one purple fill per view, and zero in Security mode. The instrument clause moves with it (round-47 item 3).
4. **FWD-19: REALIZED on the outcome; the DONE WHEN is amended by this seat.** The PRD still names `PanelNoPermission`. Andrew's
   2026-10-05 word removed that screen ("It should simply not be visible if you are not permitted"). The addendum replaces the
   no-permission arm with the read that passed: a non-Opal viewer sees no Security Analysis sidebar item.
5. **FWD-21: REALIZED, and a deliberate ellipsis is not a clip, on one condition.** A label ended with an ellipsis is a designed
   truncation; SAUX-17's clip was text cut by the panel edge. The condition: the full name is reachable from the truncated label
   (hover or focus). That read is round-47 item 4. If it fails, FWD-21 moves to NOT_REALIZED and the item becomes a page cell.
6. **FWD-20: NOT_REALIZED until the render check PASSES.** Ten of its 11 FAIL cells are the stale FWD-18 clause; one is a real page
   defect, 10 px text on the Model tab under the 11 px floor. Both are in round 47.
7. **FWD-27: NOT_REALIZED, page-side.** The Model tab's foot prints "Company short name: BOEING CO/THE" beside "The Boeing Co", and
   two system-wording lines ("2 of 6 inputs have run"; "News: a source this page has no name for yet").
8. **FWD-7: NOT_REALIZED, and its cure is in flight.** The Bloomberg officers pull is AMGT_RESAPP ba-22, signed today by both halves
   (`CTO_HALF_AMGT_RESAPP_BA22_OFFICERS_PULL_20261007.md` @4f79c10223). FWD-7 is re-graded after it lands.
9. **FWD-13's open note** (enterprise value and net debt print "... million" where market cap prints the full integer): it is the
   served unit printed as served. Not a round-47 item. It joins FWD-27's money-format limb only if a reader asks for one format.

## ROUND 47 (ONE issuance by `2.0.0_SA_COO~D`; at most three mechanical criteria per build cell)

1. **FWD-20:** the Model tab's 10 px text is raised to the contract floor. Proof: the render instrument reads 0 text nodes under
   11 px on the Model state.
2. **FWD-27:** the Model tab's foot. The vendor short-name line uses the served display name or is removed; the two system-wording
   lines become plain words. First read whether each line is page text or served text: a served line is routed to AMGT_RESAPP
   instead and named in the round's close.
3. **The instrument's FWD-18 clause:** at most one purple fill per view, zero in Security mode. Cut after the PRD addendum lands.
4. **FWD-21, one read, no build:** on the 30D face, hovering or focusing an ellipsised label shows the full name. Ten labels end in
   an ellipsis; read all ten.
5. Then the candidate comes to this seat's review, from the render. The DEV push of product files is Andrew's word through
   `0.0.0_AB_MSTR~Z`; PROD is his separate word.

## Routed to AMGT_RESAPP (`2.0.0_SA_COO~Z`)

- **Now:** the MSFT US read of ruling 1.
- **The next RESAPP enrichment list:** each peer price served with its currency; real tickers for Samsung's two listings and
  SK hynix; the "TSM US" price read.

## Owed by this seat

- The DSGN PRD addendum for FWD-18 and FWD-19's DONE WHEN (rulings 3 and 4). Both change ENDPOINT text, so the ratified-text half
  re-signs.

## Acts only Andrew can do

- **FWD-1:** his own signed-in walk on the live product. PROD carries the walked content, so nothing else remains for that row.
  Citation: the row's DONE WHEN, "one live walk, signed in with a real account ... on the live product".

-- 1.0.0_SA_CTO~Z

## CORRECTION (2026-10-07 ~10:4xZ) -- ruling 1's premise was wrong: MSFT US is not a covered name (COO~Z msg 30807, row AMGT_RESAPP-Z-S364 @bb38ea2d43)

**What I wrote:** "On 2026-10-05 the census read 95 of 95 covered names accounted for, so this is a CHANGE on a served name since
then." I assumed MSFT US was one of the 95 without reading the covered set.

**What `2.0.0_SA_COO~Z` measured** on the deployed function `MkM9Kf37`, by direct invoke: `MSFT_US_Equity` returns 200 with 7 of 7
header figures null and the blockless reason. All 95 covered names return 200 and the blockless reason reads on 0 of them (control:
AMD, 0). MSFT is not in `covered_security_keys()`: it is a pool record from the ETF holdings universe, with no research folder and
no stored company record, served as RESAPP round 72 av-1 built it. Not measured: the count among non-covered pool names, and the
gateway route.

**So there is no regression, and nothing is routed to AMGT_RESAPP for FWD-4.**

**FWD-4 moves NOT_REALIZED -> REALIZED, on this seat's 2026-10-05 rule.** That rule grades the COVERED names: REALIZED when every
covered name's seven are served or vendor-absent. ROG SW meets it (3 served, 4 with served reasons) and 0 of 95 covered names read
blockless today. One limit, stated: the per-reason census (vendor absence against "not in the latest stored pull") is the
2026-10-05 one, 0 of the second kind; it was not re-run today.
- The CVO graded the DONE WHEN as written, which says seven figures. The 10-05 rule lives only in this ledger. It goes into the PRD
  at the next amendment so the grade and the text agree; until then the CVO's reading of the text is the correct reading of the text.
- **The board: 21 REALIZED, 4 NOT_REALIZED (FWD-7, 8, 20, 27), 1 NOT_EVALUATED, 1 RETIRED. Denominator 27.**

**Two things follow for the page (round 47):**
- **Item 5, a page cell:** a name the firm does not cover says so ONCE, in plain words, where its header figures would be, in place
  of seven tiles repeating one sentence. First read how the page presents MSFT US today, and whether the served payload marks the name
  as uncovered; if it does not, that marker is a producer item and is named in the round's close.
- **Grading walks use covered names.** FWD-7's "MSFT US shows no officers" and FWD-8's MSFT peers table were read on a name outside
  coverage. The round-47 walk reads FWD-4, 7 and 8 on covered names, and walks one uncovered name only for its own designed state.
  FWD-7 and FWD-8 stay NOT_REALIZED meanwhile: AMD US is covered and shows no officers, and the Price column's mixed currencies are
  a property of the table, not of the name walked.

## ROUND 47 -- CTO review of portal candidate `ec9f9a0e` (2026-10-07 ~11:2xZ; COO~D msg 30830, close @4650e2f1ed)

**Read by this seat:** the product diff `8ddfe409..ec9f9a0e` in full (3 files, +11/-4, 0 non-ASCII added); `HeaderCards.tsx` around the
new branch at the candidate; two walk captures from `round35/walk/read-20261007T105958Z/`, looked at: `fwd24-MSFT-US-header.png` at
full size, and `tabs-BA-US-4-Model.png` at reduced size (its foot is legible in structure, not letter by letter). Not read: the
check logs, the render instrument's JSON, the other captures.

- **Placement:** `ec9f9a0e` contains `8ddfe409`, and `git ls-remote origin DEV` reads `8ddfe409`, so it is a fast-forward of DEV.
- **Item 5 (an uncovered name says so once):** `HeaderCards` returns one sentence when every slot is absent and all share one served
  reason. The MSFT US capture shows "We hold no stored company data for this name yet." once, with no tiles. Correct.
  - The slots are already filtered to those with a value or a reason, so the branch never prints an empty line.
  - The rule is keyed on the served SHAPE, not on coverage, because no coverage marker is served. So it also fires for a covered
    name whose seven figures are all absent for one shared reason. That reads correctly too (one reason, said once).
- **Item 2 (the Model tab's foot):** `SHORT_NAME` is removed from `V3_HEADER_LABELS`, which is the list the fact row iterates, so the
  line is gone and no raw key can print in its place. The two wordings are plain. The news source string is mapped on the page to
  "Articles we collect", beside the existing Bloomberg and Seeking Alpha mappings; an unmapped source reads "source not named".
- **Item 1 (10 px):** the gap mark is 11 px. One class change.
- **Item 4 (FWD-21):** 10 of 10 ellipsised labels carry the full name on hover. Focus was not read. Hover meets the condition of
  ruling 5; FWD-21 stays REALIZED.

**Verdict: APPROVED for DEV.** The page draws what is served and adds no figure.
- The DEV push of product files is Andrew's word, through `0.0.0_AB_MSTR~Z`. PROD is his separate word.
- **Item 3 is released to cut:** PRD v0.17 @8730d6c042 is ADMITTED (CVO~Z stamp @c50f85f679). `2.0.0_SA_COO~D` cuts `AV-zy-I` now;
  FWD-20 is re-graded when the instrument reads PASS.

**Seen in the MSFT capture, pre-existing and not this candidate's:** two served lines begin in lower case ("sector and country are
not in this security's data"; "no company description is held for this name yet, ..."). FWD-27, producer wording.

**For the next AMGT_RESAPP enrichment list** (named by the close, accepted here): a plain served news-source name; a served
coverage marker for a pool name outside coverage; the two lower-case served lines above.

## ROUNDS 48 and 49 -- the push sha moves to `b3440392`; FWD-20 and FWD-27 rulings (2026-10-07 ~12:4xZ)

**Rulings since the round-47 review, each first sent by message:**
- **FWD-18: REALIZED, countersigned** on `3.0.0_SA_CVO~Z`'s re-grade @4a94e19089 (msg 30857).
- **FWD-20: NOT_REALIZED.** The DONE WHEN's "FAILS a planted page on each clause" means every clause. A clause that failed on the
  real page and passed after its fix has its pair already (the size clause). The CVO's count @7ca923a956: fonts, weights, radii,
  shadows and states-present lack a pair; the other five have one.
- **FWD-27: NOT_REALIZED** on three grounds at the Model tab's foot, each holding the row (msg 30868): three money formats (page);
  "Country: UNITED STATES" (served, producer); "Filings ... has not run yet" beside 10-K citations (the input ledger, producer).
- **The board is unchanged: 21 REALIZED, 4 NOT_REALIZED (FWD-7, 8, 20, 27), 1 NOT_EVALUATED, 1 RETIRED.** My msg 30858 said 22 / 3;
  that was a miscount, corrected in msg 30860.

**Candidates reviewed after `ec9f9a0e`:**
- `97598dc3` (round 48) = `ec9f9a0e` + one commit to `scripts/ui-contract-check.mjs` (+3/-5). No product file; not read by this seat.
- `8e4dad8f` (round 49 cell 1) = `97598dc3` + `ModelTab.tsx` +4/-1. NOT approved as cut: it sent every finite number through a
  currency format. One amendment asked (msg 30881's subject): key the money format to declared money facts, correct the docstring,
  remove the unreachable lines.
- **`b3440392` = `8e4dad8f` + the amendment. APPROVED.** Read by this seat: `git diff 97598dc3 b3440392`, one file, +12/-8, 0 non-ASCII
  added. `V3_MONEY_MNEMONICS` holds the two money mnemonics; any other number returns plain grouped digits; the docstring states
  what the code does. It contains `97598dc3` and origin DEV `8ddfe409` (this seat's `ls-remote`), so it is a fast-forward of DEV.
  Not read: the checks and the 12:14Z walk, which was taken on `8e4dad8f`; the issuer states the money facts' output is unchanged
  by the amendment.

**The ONE DEV push is now `b3440392`.** It supersedes `ec9f9a0e` and `97598dc3`. Andrew's word, through `0.0.0_AB_MSTR~Z`.

**Round 49 cell 2** (the planted fail-and-clean pairs for the five clauses) is test-only and closes on its own; FWD-20 and FWD-27
go back to the CVO for re-grade after it.

## FWD-20 -> REALIZED, countersigned (2026-10-07 ~13:1xZ; COO~D msg 30927, @fc2e330e8e)

- The CVO graded FWD-20 REALIZED on the candidate @8f98b2acce and asked whether the render check, run on `8e4dad8f`, had to be run
  on the push sha. This seat required it (msg 30920).
- `round49/instrument35-b3440392/candidate.grades.json`, read by this seat: its `result` block reads PASS 76, FAIL 0, NOT_EXERCISED 0,
  N/A 1. The sha is taken from the folder name and the issuer's statement that the build was `b3440392`; the block read here does
  not carry it.
- The Model-tab walk on the same sha (`round35/walk/read-20261007T125343Z/` @6bee8e3a91; not opened by this seat): 19 reads, 17 PASS,
  1 FAIL, 1 ERROR, the same two as on `8e4dad8f`.
- **FWD-20: REALIZED. The board: 22 REALIZED, 3 NOT_REALIZED (FWD-7, 8, 27), 1 NOT_EVALUATED (FWD-1), 1 RETIRED (FWD-3). Denominator 27.**
- Still open on the instrument: it counts four designed states where PRD v0.17 says three (the grades file's own key is
  `fourStates`, with one no-permission capture). The CVO judged that stricter, not looser. Round 50's cell @1694478a45 brings it to three.
- The grade is on a candidate that is not on DEV. It is read again on DEV after Andrew's push.

## THE GRADE ON DEV `4b167888`, countersigned (2026-10-07 ~14:1xZ; CVO~Z msg 31018, @dbf5b5cff8)

Portal DEV moved `8ddfe409` -> `4b167888` at ~13:3xZ on Andrew's word at the `0.0.0_AB_MSTR~Z` terminal ("all recs approved.", its
msg 30951). Origin DEV reads `4b167888b26fe0fec9bcfc200d5678b8d3ae01f7` and CI run 37629125673 concluded success at 13:35:01Z (both
this seat's reads). The CVO graded on `2.0.0_SA_COO~D`'s DEV read @d41d3434bd; this seat did not open the grade file.

- **FWD-20: REALIZED on DEV.** Countersigned.
- **The uncovered-name read: MET** (MSFT US says its one sentence once).
- **FWD-7: NOT REALIZED, 93 of 95.** BP/ LN and NG/ LN are both covered names and serve no officer list until the slash reader
  ships (row AMGT_RESAPP-Z-S365, a round-78 cell). The CVO reads the ACCEPT as accepting a labelled Bloomberg list. So FWD-7 closes
  on that one producer cell and its redeploy, with no page work.
- **The board on DEV: 22 REALIZED, 3 NOT_REALIZED (FWD-7, 8, 27), 1 NOT_EVALUATED (FWD-1), 1 RETIRED (FWD-3). Denominator 27.**

**One finding, routed:** MSFT US reads "No articles collected for this name this month" beside a news item dated October 2nd. The
two lines draw on different inputs (the month's collected chatter over the covered names; the news feed), and MSFT is not a covered
name. To AMGT_RESAPP's round-78 list: for a name outside coverage the chatter line says the name is not in the covered set, and
never "no articles", which the item beside it contradicts.

**What is left on this project, all outside the page:** FWD-7 (the slash reader), FWD-8 (peer prices with their currency), FWD-27
(the country's case and the Filings line), each in AMGT_RESAPP's round 78; and FWD-1, Andrew's own signed-in walk. PROD is at
`b06863fe`; the promote of `4b167888` is his separate word. DSGN_AMGTV1 cuts no page round until RESAPP round 78 deploys.
