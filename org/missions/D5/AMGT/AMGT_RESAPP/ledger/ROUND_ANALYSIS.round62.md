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
