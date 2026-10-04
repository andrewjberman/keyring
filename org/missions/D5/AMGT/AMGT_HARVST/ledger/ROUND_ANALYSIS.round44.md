# AMGT_HARVST -- ROUND 44 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-04 ~20:1xZ

**Input:** CVO slug msg 29208, `surprise-channel/adjudications/ADJUDICATION_v56.md` @876c7d30e1 (precondition MET; ARMED 0).
The packet is `deliverables/2.0.0_SA_COO_H/round44/ROUND44_DRAIN_END_PACKET.md` @76d0723778, and the reads are @02217a491f. They ran
17:58Z-18:41Z, before the site-Z crash, and were committed on relaunch.

## 1. WHAT THE ROUND DELIVERED

Four READ cells, with no writes, no collection and no vendor call:
- aq-1 FWD-2: FAIL. Four of five publishers lose named fields, and 3 of 50 sampled wsj originals have no silver row.
- aq-2 FWD-5: PASS on judgment, 15 days on 5 names with 0 order violations.
- aq-3 FWD-7: FAIL. The applied `CHATTER_AXIS_SOURCE` is `legacy`, and the gold dry run HOLDS on an empty declared set.
- aq-4 FWD-12: (a), (b) and (d) PASS. (c) FAILS: `config.json` `sa: 25` overrides the code default of 200 on the worker path.

**Round 44 is CLOSED.**

## 2. GRADES AND THE BOARD

**FWD-5: REALIZED.** The CVO graded it PASS on judgment and offered it for the board. "Strongest" = tier first, then mention count,
which is FWD-7's own meaning of strength. The PROD page renders the served order (`TimelinePanel.tsx` @dbd29c63).

**The board** (latest grade per outcome; rounds 29-44 and ADJUDICATION_v56; denominator 17):

| state | outcomes |
|---|---|
| REALIZED (6) | FWD-4, FWD-5, FWD-6, FWD-8, FWD-16, FWD-17 |
| Open, finishing needs NO new collection (2) | FWD-2, FWD-12 |
| Open, finishing NEEDS new collection (9) | FWD-1, FWD-3, FWD-7 (moved here by ruling 2), FWD-9, FWD-10, FWD-11, FWD-13, FWD-14, FWD-15 |

6 + 2 + 9 = 17.

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **FWD-2** (fields lost in silver; 3 wsj originals with no silver row) | **Cut the repair in round 45** as offered: type the lost fields, barrons first, find why the 3 wsj originals have no row, and rebuild silver from the stored originals. It is a served write, so it goes under a pair. | Every input is already stored. Nothing waits on collection. |
| 2 | **FWD-7** (the packet offers "re-rule `C-HV-RANK-DECLARED-SET` for a backfilled store" as the alternative to collection) | **Not re-ruled. FWD-7 moves to the collection partition.** The flip to `gold` stays HELD until a universe-scope collection lands in the window, which waits on Andrew's word on collection. | The contract exists so that an unsearched name is never read as a quiet one (grounds @ddcc71fd2d, research @784068f4c0). With no collection in the window, every name's window is unsearched. A rank served from a backfilled store would be exactly the vacuous rank the contract forbids. The legacy rank serving empty today (NO_SIGNAL_IN_WINDOW 191 of 191) is the honest output of the same fact. |
| 3 | **FWD-12 (c)** | **Cut the LOCAL repair in round 45.** The worker path's effective sa listing cap must be past 25: either the code default of 200 governs, or the config value is set past 25. One plant fails with the fix removed. (a), (b) and (d) are re-read unchanged, and FWD-12 is then graded whole. | (c)'s DONE WHEN is "the listing page cap is raised past 25". That is a code and config fact, so proving depth on a new backfill is not part of it. A backfill is collection and stays held. FWD-12 is the precondition for any future backfill, so closing it now removes a gate before Andrew's word arrives. |
| 4 | **Row `AMGT_HARVST-Z-S82`** (19,967 of 31,042 served gold mention rows are pre-2026) | **KEEP the rows in gold**, with no store write and nothing trimmed. **CLIP the served events and timeline at `STORE_START` (2026-01-01)**, the same bound the windows already use. Cut in round 45 under a pair. Relayed to `2.0.0_SA_COO~H` in the tick-1 message of this seat's self-drive. | FWD-9 declares the history since 2026-01-01. The deeper rows came from where the sa listing happened to reach, so they are uneven by name: some names show 2013 days and others show none. A reader would infer quiet years that were simply never searched. Keeping them in gold makes the clip reversible and loses nothing. FWD-12 (d) holds: these are real articles, not wrong ones. |
| 5 | **MSFT's busiest days carry no tier-A article** (CVO observation) | **No cell.** | It is the legacy rank's population, and FWD-7's gold rank addresses it. FWD-7 is held by ruling 2. |
| 6 | **The 9 collection outcomes** | **Not cut.** | Andrew, 2026-10-03 ~17:3xZ: "We will discuss internally on how to proceed with further data collection after review." |

## 4. ENRICHMENT LIST (round 45, ONE issuance by `2.0.0_SA_COO~H`)

1. **FWD-2** (SERVED, pair): type every lost field for barrons, bbg, ft and wsj in `lib/opal_data_harvest/silver_from_bronze.py` and the
   publisher field maps. Find why the 3 sampled wsj originals have no silver row. Rebuild silver from the stored originals. Graded by
   re-running aq-1's field census: 0 fields lost across the five publishers, and every sampled original has its row.
2. **FWD-12 (c)** (LOCAL): the worker path's effective sa listing cap is past 25, with one plant that fails when the fix is removed.
   aq-4 (a), (b) and (d) are re-read unchanged.
3. **Z-S82** (SERVED, pair): the served events and timeline clip at `STORE_START`, and gold is untouched. Print the number of clipped
   rows and the names they fall on. The windows read unchanged.
4. **No collection, no vendor call, no backfill.**

## 5. ACTS FOR ANDREW (cited)

- **His word on further data collection.** It is the one act that makes the 9 collection outcomes cuttable, FWD-7 among them. The
  hold, quoted: "We will discuss internally on how to proceed with further data collection after review" (2026-10-03 ~17:3xZ). After
  round 45, HARVST's end state is HELD on that word.
