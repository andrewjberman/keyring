# AMGT_RESAPP -- ROUND 62 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~11:4xZ

**Input:** CVO~Z slug msg 28433, `surprise-channel/adjudications/ADJUDICATION_v74.md` @5542cd4564 (precondition MET). The round is
al-1: act (A), memory, and act (B), the read deadline. Both were cut under round-61 rulings 5 and 5a. COO~Z's measured times are in
msg 28427. **Round 62 is CLOSED.**

## 1. WHAT THE ROUND DELIVERED

- **Track A:** `opal-amgt-scoped-api` runs at 10240 MB. 3538 MB missed (21.7, 20.4 and 22.9 s cold); 10240 passed (16.9, 16.6 and
  19.1 s cold). Peak memory use is about 460 MB at every tier, so the time is CPU-bound, not memory-bound.
- **Track B:** live at 11:27Z (`bZBmEtRr...`, read by this seat) and graded at 11:32Z, inside the 12:30Z freeze. A day read that
  passes 18 s now serves its mentions with `headline: null` and a plain `headline_reason`, as a 200.
- **CVO~Z's read of the guarded build:** 12 of 12 BA day calls answered 200, with 0 errors. **Z-C-S29's timeout is disarmed.**
  However, 7 of 11 cold calls hit the deadline (Sept 8: 6 of 7), and PROD's page renders that case as "[no headline]". A warm call
  serves headlines in 0.6 s.

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **A one-off warm-up read before Andrew's demo read, by `2.0.0_SA_COO~Z`.** Starting about 12:50Z, fire 2 sequential read-only invokes of BA `/timeline/day/2026-09-08`: the first may hit the deadline, and its worker fills the process cache; the second must carry headlines. Repeat the pair once on MSTR~Z's word that Andrew is starting, if more than 10 min have passed. It is an invoke, not a deploy, so it is inside the freeze. **It is not a scheduled warmer:** no cron, rule or loop is built, under the moratorium on standing monitors. | a cold demo click shows "[no headline]"; a warm one shows the headlines |
| 2 | **Track C, post-demo, round 63:** the day route stops reading whole-publisher silver, using either a headline on the gold mention row or a per-day article index. The criterion is a cold BA day read under 5 s. After that, memory goes back down from 10240, re-measured. | 10240 MB is CPU spent on reading 160 MB to print a few headlines |
| 3 | **DSGN, post-demo:** the day view prints `headline_reason` in place of `[no headline]` (carried from the al-1 (B) CTO half). | the face should state the reason |
| 4 | **Round 63's list, after the demo:** track C; the reason class served beside the peers reason text (carried from the DSGN round-26 review); and round-60 ruling 3's carried items. | carried |

**The freeze holds:** nothing deploys to `opal-amgt-scoped-api` until Andrew's demo read is over.

## ADDENDUM ~14:0xZ -- track C RULED: option A (headline into gold), on CRO~Z design-fork research

**Input:** COO~Z msg 28498, findings `deliverables/2.0.0_SA_COO~Z/round63-prep/TRACKC_FINDINGS.md` @36414ad802. The BA day route
reads 1,884 silver objects (140 MB) to use 5 rows. CRO~Z research
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESEARCH_TIMELINE_HEADLINE_GOLD_VS_SILVER_20261002.md` @adb64006ed supports A:
- the same producer's `chatter_event.lead_headline` held its schema across 4+ rebuilds;
- the only request-time silver read in serving code is this route, and it aged in hours.

**Ruling (driver, after research): A.** `title` and `published_precision` join `GOLD_MENTION_SCHEMA`, and the day route reads
them from gold. It reads no silver at request time.

| step | owner | act | conditions |
|---|---|---|---|
| 1 | `2.0.0_SA_COO~H` (AMGT_HARVST: `publication_gold.py`) | add `title` (VERBATIM, rule 17b) and `published_precision` to the gold mention rows; rebuild gold under a never-widen pair. This moves served gold, and the CTO half is owed here | the producer change and the gold rebuild land BEFORE step 2. Optional, in the same cell: `build_event` drops its second whole-silver title scan (research s.5) |
| 2 | `2.0.0_SA_COO~Z` (AMGT_RESAPP round 63) | the day route serves `headline` from the gold row; the silver read and the 18 s deadline path are removed; memory is re-measured down from 10240 | a cold BA day read under 5 s at the re-measured memory; the two control-day bodies byte-equal except `headline_reason` (absent); the never-widen pair |
| 3 | `2.0.0_SA_COO~D` (DSGN, post-demo) | the day view prints `headline_reason` instead of `[no headline]` while any stale gold row lacks a title | carried from the al-1 (B) CTO half |

## ADDENDUM ~14:3xZ -- the freeze lifts; round 63's list is final (DSGN round-26 grades)

**The freeze lifts.** Andrew's demo read is over: his "yes to all" (@383e989b95) gated the PROD promote on "once the demo is over",
and the promote landed (portal PROD f76b02acb6, ~13:5xZ). Deploys to `opal-amgt-scoped-api` resume under their pairs.

**Round 63 (`2.0.0_SA_COO~Z`, ONE issuance):**

| # | cell | from | class |
|---|---|---|---|
| 1 | Track C step 2: the day route reads `headline` from gold; the silver read and the 18 s path go; memory is re-measured down from 10240. AFTER HARVST lands step 1 (aj-7) and rebuild #5 (aj-8 unblocks it) | track C ruling (above) | served, with the pair |
| 2 | **FWD-7, officer fallback** (DSGN grades: NOT_REALIZED on CVO~Z v26 @07446385f1). A filing with no officer section (ASML_NA's 20-F) falls back to the Bloomberg officer list with its source named, as 6861_JP and CSL_AU already do. 6501_JP and 2317_TT gain a management object, or the reason none is served | DSGN COMPLETION_GRADES.round26 @0c4c6d6368 | served, with the pair |
| 3 | **FWD-2, chatter-row identity:** the collected-chatter rows serve `ticker`, `classification` and `places_moved` beside `display_name`. DSGN r27 (AV-ze-1) reads them the day they are served | COO~D msg 28526 | served, with the pair |
| 4 | The reason CLASS served beside each peers absent-column reason, so the page maps by class, not by exact text | DSGN round-26 review | served, with the pair |
| 5 | Round-60 ruling 3's carried items: Z-S332; the dead chatter legacy inputs; the page universes; the duplicate dossier reads | round 60 | as cut |

**Round 63, cell 3 widened (~15:0xZ, DSGN FWD-24 on `3.0.0_SA_CVO~Z` v28 @17da4156e3):**
- The overlay route's `breakout_price` row also serves `places_moved` from the same rankings row the route already reads.
- Today the header prints "#7 | +5.79%" for VLO with no places moved, while the rankings serve 13.
- Plant: VLO's breakout_price row carries places_moved = the rankings value. A security with no rankings row carries the reason
  instead.
- If round 63 is already issued, this is an issuer amendment; otherwise it is part of cell 3.
