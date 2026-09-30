# AMGT_HARVST -- ROUND 16 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~12:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26589, READ-acked, subject *"L10 SLUG AMGT_HARVST round 16 @713537d4d0"*,
citing `surprise-channel/adjudications/ADJUDICATION_v24.md`. The served rebuild ran under the pair `604165a591` (COO) +
`73fce69599` (this seat), and was drained and served @`8d396187d9`.

**Round 16 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

**The double count is gone.** On the AMZN crash report, the served count is 8, the text holds exactly 8 "Amazon" occurrences, and
the prototype said 8: **8 = 8 = 8.** The 8 C -> D rows each now count their one matched span once. `Z-W41-S2` graduates.

## 2. THE CVO'S DECISIONS

1. **Under-counts where a company is named by its ticker or brand -- RULED: measure the class before changing the rule.** "UPS
   freighter" reads 1 where the text says 2, and "Google" x2 is missed for Alphabet. This is round 14's alias-coverage class again.
   Adding tickers and brands blindly is unsafe: short tickers ("V", "MA", "ALL", "UPS") are common words, and brand-to-parent
   mapping ("Google" -> Alphabet) needs a source. **Round 17 cell 1 is the census:** for every security in the 191, count the
   mentions its ticker forms and its brand or short-name forms would add over today's silver. For each form, count how many
   of those hits a text read shows to be the company, on a sample printed per form. Every figure carries its denominator. The
   next analysis rules the alias rule on that census (which forms, which length floor, which brand source). No served move
   this round.
2. **`Z-W40-S1` has sat ARMED-by-spec since round 14 in no cut -- RULED: cut it now.** Name detection strips a single-story
   security's own recurring words, so its FIRST burst forms no event. No live security has that shape today, but the alias
   work above widens the name vocabulary, which is exactly the input this defect keys on. **Round 17 cell 2:** fix name
   detection so a security's first burst survives. It is exercised on the planted fixture as a mechanism test (labelled a
   fixture, never a held-out grade), with an arm showing the 8 served events unmoved. Any served move goes under a pair.

## 3. FWD GRADES
`FWD-5` / `FWD-6`: NOT REALIZED. The served half is met; the page half is the timeline panel `92a2576254`, held by Andrew's *"lets
hold on pushes and merges for now"* (~20:3xZ 09-28, to `0.0.0_AB_MSTR~Z`). The others stand as `ROUND_ANALYSIS.round15.md` left them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 17 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **Ticker and brand census** (ruling 1) | LOCAL, read-only: per-security added-mention counts for ticker and brand/short-name forms, true-hit read per form on a printed sample, denominators; the alias rule is decided at the round-17 analysis |
| 2 | **A security's first burst survives name detection** (`Z-W40-S1`) | planted-fixture mechanism test and an arm with the served events unmoved; a pair only if served gold moves |

**Fan-out:** 2 cells, independent. **NOT cells:** the event route (`Z-W39-S1`); the portal push (Andrew's hold); new held-out reads
(the Seeking Alpha 402).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)
- Read the Seeking Alpha subscription state (`Z-W37-S4`, HTTP 402) [entitlement].
- Lift *"lets hold on pushes and merges for now"* for the timeline panel push [a hold set by name].

## Compiler Tools
The CVO's S3 re-run of `ac4_one_count_per_mention.py`, and its text counts over 4 articles (v24), taken as measurements; this
seat's own e-2 rebuild (@`73fce69599`) as the reference.
