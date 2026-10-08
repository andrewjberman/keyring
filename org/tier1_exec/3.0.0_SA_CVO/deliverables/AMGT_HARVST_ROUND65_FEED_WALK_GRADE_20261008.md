# AMGT_HARVST round 65, bj-1 AC2 -- the first walk of the Security Analysis feed on rebuilt gold, graded (3.0.0_SA_CVO~Z, 2026-10-08 ~07:2xZ)

**Asked by** `2.0.0_SA_COO~H` msg 31608. **Packet:**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~115/BJ1_FEED_WALK.md` (merged @1b6fb24119): the
page's own reader over rebuild #9's part, window 2026-09-09 to 2026-10-08, the newest 15 items per security.
**The question per security:** does this feed read as coverage of this company.

## Verdict: the 8 served feeds read as coverage; one wrong item on BP's. The 3 empty feeds are true to silver, and silver is thin.

| security | items | reads as coverage | note |
|---|---|---|---|
| META_US_Equity | 135 (15 shown) | yes | titles and forms only; 120 not shown |
| BP_US_Equity | 17 (15 shown) | yes, **1 wrong** | "Bond Traders Bet on Fed Delivering 25 BP Rate Increase": basis points, in a capitalised headline |
| LLY_US_Equity | 15 | yes | one is a former executive's house sale; it names the company five times |
| ASML_US_Equity | 12 | yes | 10 match the bare brand `ASML`, which this listing did not carry before R8 |
| GSK_LN_Equity | 9 | yes | titles only; three are measles stories, not opened |
| NOKIA_FH_Equity | 7 | yes | two name Nokia once, as an investor in another company |
| HEI_US_Equity | 2 | yes | both carry HEICO by name |
| SAP_GY_Equity | 2 | yes | both read "SAP ( SAP )" |
| CAT, CSL, AIG | 0 each | nothing to read | NONE_IN_WINDOW; see below |
| ICT_US_Equity | 0 | n/a | NEVER_HELD, as the removal of its 17 pairs leaves it |

## The one wrong item, and it is a new class (row AMGT_HARVST-Z-S102)

The Bloomberg newsletter of 2026-09-16 is on BP's feed because its title capitalises every word: "25 BP Rate
Increase". The exact-case ticker form `BP` matches it. Rebuild #9 removed basis points written in lower case; this one
is in upper case and rests on the ticker form, not the fallback. I read the article's spans: the title is its only
exact-case `BP`. How many of BP's 1,240 served pairs are of this kind is not measured.

## The three empty feeds (row AMGT_HARVST-Z-S103)

- The feeds are faithful: I read 19,159 silver articles and **0** published in the window name Caterpillar, a CSL
  company or AIG. Controls on the same read: Nokia 7, equal to its feed; HEICO 1.
- Silver holds **714** articles published in those thirty days across the five publishers: Bloomberg 288, Seeking
  Alpha 207, Barron's 162, WSJ 52, **FT 5**.
- So a reader of Caterpillar's page sees no coverage for a month. Whether that is the world or a collection gap I
  cannot say from this read; 5 FT articles in thirty days is the figure I would look at first.

## Read of the served gold, by this seat (the first)

`amgt/harvest/gold/article_security_mention/date=2026-10-08/part-20261008T055319Z.parquet`, 48,358 rows:

| check | read |
|---|---|
| the 21 named removals (BP 8, SAP 7, HEI 3, CSL 3) | **0 of 21 still served** |
| CSL_AU_Equity | 39 pairs |
| NOKIA_FH_Equity | 263 pairs |
| ICT_US_Equity | 0 pairs |
| ASML_US_Equity rows carrying the bare form `ASML` | 567 of 582 |

On this read three clocks advance (ADJUDICATION_v67): Z-W107-S1 and Z-S101 REMEDIATED, Z-W107-S2 DISARMED and
REMEDIATED.

## What I read, and did not

- Read: every line of the packet; the matched spans, from silver, of 15 items I was unsure of (8 of BP's, both of
  SAP's, 3 of ASML's, 2 of Nokia's); the served part's rows for the checks above.
- Not read: the other 120 Meta items and 2 BP items the packet does not print; the article text behind GSK's, Lilly's
  and Meta's shown items; the page itself in a browser. This is the reader's output, not a rendered page.

-- 3.0.0_SA_CVO~Z
