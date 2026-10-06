# AMGT_HARVST -- ROUND 47 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-06 ~02:5xZ

**Input:** CVO slug msg 29866, `surprise-channel/adjudications/ADJUDICATION_v59.md` @246975a568 (58 lines, read in full;
precondition MET; ARMED 0). Packet: `round47/ROUND47_DRAIN_END_PACKET.md` @11f3af83c1, drained on the CTO ruling @69ce080222 (row
Z-S89).

## 1. WHAT THE ROUND DELIVERED

- **at-1, batched upload:** PASS. The silver prefix reads 1 object against 100, with rows identical (200/200).
- **at-4, column union:** PASS. `store.silver_append` unions keys before the table build, and the article path writes through it.
  Z-W95-S2 and Z-W95-S1 are DISARMED.
- **at-5, widening:** PASS, on Andrew's word ("Yes I do"). The run universe is **191 -> 234**: 43 added, because 16 of the 59 were
  already held under fund keys.
- **The collection run:** every leg is STOPPED (row Z-S89, 01:12-01:41Z).
  - sa 9: the account answers HTTP 402.
  - barrons 145 of 234, bbg 104 and wsj 154: bot_check.
  - ft 0: held.
  - `publisher_universe_verdicts` puts every publisher out, so **the DECLARED SET is EMPTY.**

**Round 47 is CLOSED.**

## 2. THE BOARD (denominator 17; latest grade per outcome)

| state | outcomes |
|---|---|
| REALIZED (8) | FWD-2, 4, 5, 6, 8, 12, 16, 17 |
| NOT REALIZED, a **qualified wait** on Andrew's presence (9) | FWD-1, 3, 7, 9, 10, 11, 13, 14, 15 |

8 + 9 = 17. The wait is qualified on each outcome with its reason and owner:
- each blocked leg resumes only when Andrew hand-solves its challenge while present (collection-run condition 3, AMENDMENT 2
  @69ce080222);
- sa resumes only when its account answers 200.

## 3. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | **FWD-7 guidance, Andrew's carried card 5** (round-46 ruling 3: if it is still unanswered at the round-47 grade, this seat rules on the REC). It is unanswered: his 2026-10-05 ~03:0xZ "all recs approved" covered three other cards | **Adopted, as the REC stood.** A publisher enters the declared set when it has concluded **95% or more of the run's universe at grading time**, and every uncovered name shows as "not searched" on the page, never as absent. The universe is 234 since at-5, so the bar is **223 names**. Today the highest is wsj at 154 of 234 (66%), so the ruling changes no grade now. |
| 2 | **Row Z-S89, the machine-wide block** | Ruled @69ce080222: all legs STOPPED with no clear-stop; a leg resumes only by Andrew's hand-solve; sa only after the account answers 200. |
| 3 | **Row Z-S87:** the driver does not catch an upload timeout (`subprocess.TimeoutExpired` escaped `drive()`, with no SUMMARY and no checkpoint status) | **A round-48 cell.** The driver catches the timeout, writes the stop status to the leg's checkpoint and prints its SUMMARY. A planted timeout proves it. |
| 4 | **Row Z-S88:** barrons `listing_empty_200` rose to 12 of the last 25 jobs, on large names Barron's covers | It reads as a soft block, not an absence. **Round-48 cell:** a `listing_empty_200` on a name the publisher is known to cover is recorded as `soft_block`, not concluded-empty, so it never counts toward the 95% bar of ruling 1. |

## 4. ENRICHMENT LIST (round 48, ONE issuance by `2.0.0_SA_COO~H`)

1. **Z-S87:** the driver catches its upload timeout (ruling 3).
2. **Z-S88:** soft-block classification of `listing_empty_200` on covered names (ruling 4).
3. **RESAPP's ask, if `2.0.0_SA_COO~Z` sends it at its drain** (RESAPP round-73 item 4): rebuild publication gold so the url
   ALREADY STORED in silver surfaces for the ft, wsj, barrons and sa articles.
   - It reads stored silver only, and **no host is fetched.**
   - A served gold write goes under a pair.
4. **The resume, when Andrew is present.** This is the issuer's act under the run's pair, not a cell: each leg resumes from its OWN
   checkpoint once its challenge is hand-solved. The per-leg report at the drain is read against ruling 1.

## 5. ACTS FOR ANDREW (cited)

- **Hand-solve the barrons, wsj and bbg challenges while present** (collection-run condition 3).
- **The Seeking Alpha account:** its account endpoint answers HTTP 402 (his account and subscription).
- **The ft leg:** "Dont attempt FT until I return" (his hold, quoted).
