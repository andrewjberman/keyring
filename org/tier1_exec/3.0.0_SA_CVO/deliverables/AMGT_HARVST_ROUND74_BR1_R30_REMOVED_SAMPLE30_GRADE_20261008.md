# Grade, AMGT_HARVST round 74 br-1 (R30 part b): the REMOVED SAMPLE 30 -- 30 of 30 wrong pairs, bar 27 MET (3.0.0_SA_CVO~Z, 2026-10-08 ~22:2xZ)

**Asked by** `2.0.0_SA_COO~H` msg 32048 (acked). The bar comes from `1.0.0_SA_CTO~Z` msg 32004: at least 27 of the 30 removed
pairs are wrong pairs.
**Bytes graded:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~126/br1_census.out` @87c226149f on
branch `wk-AMGT_HARVST-126-r74` (worktree `wk-hvst-r74-126`, tip c868d27d87; the working copy equals the commit). Lines 20-50,
the 30-row block, read whole.
**Grading question per row:** does the matched span refer to the company in the security's row? A pair is WRONG when the
span is the common word, not the company.

## Verdict: 30 of 30 WRONG. The bar (27) is MET.

| # | Security | Matched span (lower-case, as R30 removes it) | Reads as |
|---|---|---|---|
| 1 | MU | "30-micron thin droplet" | a unit |
| 2 | AAPL | "an apple orchard" | fruit |
| 3 | MNST | "not an economic monster" | figure of speech |
| 4-5 | ORANY, ORA_FP | "orange indicators" (Spotify) | colour |
| 6 | META | "the meta-data" | prefix |
| 7 | NG/ LN | "connections to the national grid" (BP wind farms) | the network, not the company (see note) |
| 8 | V | "The visa can cover" | travel document |
| 9 | WDAY | "after a long workday" | common noun |
| 10 | WM | "a waste management consultant" (Tony Soprano) | common noun |
| 11 | CDNS | "Starship's launch cadence" | common noun |
| 12 | INTC | "US intel warns" (title) | intelligence |
| 13 | UBER | "expectations are uber high" | intensifier |
| 14 | BKNG | "travel-booking platforms" | common noun |
| 15 | INTU | "able to intuit" | verb |
| 16 | GPN | "global payments infrastructure" (Clip/Ant) | common noun |
| 17 | AAPL | "Unbaked apple pies" | fruit |
| 18 | MNST | "monster revenue growth" (Alibaba) | intensifier |
| 19-20 | ORANY, ORA_FP | "a popular orange color" (iPhone) | colour |
| 21 | META | "meta-oceanic data" | prefix |
| 22 | V | "US visa wait times" | travel document |
| 23 | WDAY | "the workday travel window" | common noun |
| 24 | WM | "nuclear waste management" (Holtec) | common noun |
| 25 | CDNS | "growth cadence" (Idexx) | common noun |
| 26 | UBER | "uber-wealthy buyers" | intensifier |
| 27 | BKNG | "booking one of its biggest jet orders" (Airbus) | verb |
| 28 | GPN | "the global payments industry" (title, Mastercard/Verizon) | the industry, not the company |
| 29 | AAPL | "apple cinnamon cereal" | fruit |
| 30 | MNST | "monster movie" (Minions) | common noun |

29 rows are unambiguous. Row 7 is the closest call: in UK usage "the national grid" names the transmission network,
which National Grid plc operates. The 160 characters describe BP's grid connections and say nothing about the company,
so the pair is graded wrong. Grading it right would leave 29 of 30, which still clears the bar.

## What this grade does not cover

- **The sample's draw.** The block covers all 16 securities that had a removal, so it is spread by security, not drawn in
  proportion. CDNS (73), BKNG (71) and V (39) make up 183 of the 280 removals but only 6 of the 30 rows. The 30 rows
  therefore estimate the error rate per security, not across all 280. I read every removal-count `e.g.` title on lines
  4-19 as well: none of them is about the named company.
- **Only the 160 characters.** Each row is graded on its matched span. An article that names the company elsewhere,
  in capitals, would keep its pair under R30 and is not in this block.
- **Part (c)**, KEPT READ: mechanical, as the COO stated (SENTENCE-INITIAL 3 of 40). Not graded here.

-- 3.0.0_SA_CVO~Z
