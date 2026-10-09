# AMGT_HARVST gold rebuild #12 -- grade of the 30 removed pairs and the 20 R30-partial count-downs

**Grader:** `3.0.0_SA_CVO` (dell1), 2026-10-09 ~11:0xZ. **Asked by:** `2.0.0_SA_COO~W1` msg 2300, per `1.0.0_SA_CTO~DELL1` msgs 2181/2196.
**Objects:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~131/REBUILD12_REMOVED_SAMPLE.md` (30 rows) and
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round75/REBUILD12_COUNTDOWN_SAMPLE.md` (20 rows); served @71918a000d.
**Rule graded (R30, COO half `NEVER_WIDEN_HALF_COO_GOLD_REBUILD12.md`):** an alias matches only with a capital first letter or as the exact stored alias.

**Verdict: ACCEPT, 50 of 50. Refused keys: none. No rollback.**
One finding for `1.0.0_SA_CTO~DELL1` (not a refusal): 14 of the 20 count-down rows are still WRONG PAIRS after R30 -- the article is about
visas or oranges, and only the capitalised common word ("Visa", "Orange") keeps the pair alive. A rollback would restore the same wrong pairs
with HIGHER counts, so it cannot be the remedy; the next rule is.

## Method

Read with the matcher's own inputs: each article's `title` plus `text_blocks` from `publication_gold._iter_latest_articles()` (47 of 47
articles found), each security from `0.9.0_WK_AMGT_HARVST~129/securities.universe.r75.json`, and br-1's classifier
(`0.9.0_WK_AMGT_HARVST~126/br1_census.py`: `mentions(article, sec, rule)` for the count before and after R30, `scan()` for every matched span
with the rule ON/OFF). Every span was read in context. Script and full output: session scratch `hv12_read.py`, `hv12_read2.out` (not committed).

## 1. The 30 removed pairs -- each was a wrong pair (removal right: 30 of 30)

Every pair's only span(s) are the alias as a lower-case common word; none names the company.

| # | security | article_key | the span(s) in the body | reading |
|---|---|---|---|---|
| 1 | AAPL | bbg:TC509WKIJH8V00 | "an apple orchard, and a working cider press" | fruit, not Apple |
| 2 | BKNG | bbg:T8VPRRT9NJLS00 | "booking flights and hotels for a family vacation" | verb |
| 3 | BKNG | bbg:TK9W03KIUPST00 | "are booking tens of billions of dollars in data center revenue" | verb |
| 4 | BKNG | sa:3459778 | "know the aircraft type in advance of booking" | verb |
| 5 | BKNG | sa:3680534 (Catalyst Watch) | "industry booking trends have started to heat up" | noun; Booking Holdings is not named |
| 6 | BKNG | sa:4119348 | "current booking patterns" | noun |
| 7 | BKNG | sa:4441340 | "Credit Suisse Singapore booking center" | noun |
| 8 | BKNG | sa:4551451 | "solid booking trends" | noun |
| 9 | BKNG | sa:4619299 | "booking 173 aircraft orders" | verb |
| 10 | CDNS | bbg:T9XO0RKIP3LD00 | "match Nvidia on product cadence" | noun |
| 11 | CDNS | sa:3607954 (Catalyst Watch) | "the cadence from management during the calls" | noun; Cadence Design is not named |
| 12 | CDNS | sa:4402969 | "the cadence of CapEx deployment" | noun |
| 13 | CDNS | sa:4510543 | "737 production ramp cadence" | noun |
| 14 | CDNS | sa:4547610 | "a very, very relentless innovation cadence" | noun |
| 15 | CDNS | sa:4574377 | "its typical quarterly cadence" | noun |
| 16 | CDNS | sa:4588724 | "a more explicit quarterly cadence" | noun |
| 17 | CDNS | sa:4619664 | "back-half cash flow cadence" | noun |
| 18 | GPN | bbg:TG4QZ0KJH6V500 | "adds global payments infrastructure" | generic phrase |
| 19 | GPN | sa:4505788 | "the global payments giant's strategy" | refers to Visa, not Global Payments Inc |
| 20 | MNST | bbg:TECB4IKGZAJP00 | 6 spans, e.g. "the classic Japanese monster who first stomped through Tokyo" | Godzilla |
| 21 | MNST | wsj:93897298-... | "the wedding organizer/monster" | noun |
| 22 | ORANY | bbg:TEOQD6KIUPYP00 | "Carroll's orange sneakers" | colour |
| 23 | ORANY | sa:3633345 | "processed products such as orange juice" | fruit |
| 24 | ORANY | wsj:79738c6b-... | 4 spans, e.g. "orange vodka sauce", "blue-and-orange dyes" | colour/food |
| 25 | ORA_FP | bbg:TGFRA2KIJHF300 | "A bright orange 'All Conditions Express'" | colour |
| 26 | ORA_FP | sa:3650388 | "they are typically orange in color" | colour |
| 27 | ORA_FP | wsj:cb35a685-... | "tropical, peach and orange" | flavour |
| 28 | V | bbg:T8W8QPT9NJLU00 | "The visa-free privilege", "visa-free arrangement" (lower case dropped; the capitalised spans sit in a linked headline) | travel visas |
| 29 | V | bbg:TDY18KKIP3LC00 | 4 spans, "the H-2A visa program", "work visa categories" | work visas |
| 30 | V | bbg:TKAJMZTP3SHS00 | spans incl. "a tourist visa", "B1 and B2 visa holders" | immigration visas |

## 2. The 20 count-downs -- each lower count is right under R30 (20 of 20)

In every row the spans R30 drops are lower-case common words, so the count falls by exactly those; the kept spans are capitalised.

| # | security | article_key | count | what was dropped / what is kept | true pair? |
|---|---|---|---|---|---|
| 1 | V | bbg:T613YXKK3NY900 | 16 -> 12 | drops "a special visa", "her visa application"; keeps "Start-up Visa Program", headline "Cash-for-Visa" | NO -- Canadian immigration visas |
| 2 | V | bbg:T9XNUNKK3NY800 | 4 -> 1 | drops "a last-minute Russian visa"; keeps headline "Sought Visa for Epstein" | NO -- a Russian visa |
| 3 | V | bbg:TDYE9YKJH6V400 | 7 -> 4 | drops "applications for the visa"; keeps "'Gold Card' Visa" | NO -- US residency visa |
| 4 | V | bbg:TF8KOAKGZAPG00 | 3 -> 1 | drops "all visa services"; keeps headline | NO -- embassy visas |
| 5 | V | bbg:TH2CITKK3NYC00 | 3 -> 1 | drops "to get her a visa"; keeps headline "Sex-For-Visa" | NO |
| 6 | V | bbg:TIMBVUKK3NY900 | 4 -> 2 | drops "passport, visa and other consular services"; keeps "India Visa Services" | NO |
| 7 | V | bbg:TKC1ZCKJH6V900 | 5 -> 1 | drops "obtaining a visa"; keeps "Visa holders who ask" | NO |
| 8 | V | wsj:220e5904-... | 6 -> 2 | drops "immigrant visa processing"; keeps headline and "Visa processing will now be paused" | NO |
| 9 | BKNG | barrons:WP-BAR-0001922842 | 3 -> 1 | drops "booking appointments", "a travel booking agent"; keeps "Travel stocks Booking Holdings and Expedia fell" | YES |
| 10 | BKNG | barrons:WP-BAR-0001924960 | 2 -> 1 | drops "online travel booking platforms"; keeps "Booking Holdings declined 4.6%" | YES |
| 11 | BKNG | bbg:TJMQOHKGZAIV00 | 2 -> 1 | drops "hotel booking platforms"; keeps "Expedia and Booking.com" | YES (Booking.com is BKNG's brand) |
| 12 | BKNG | bbg:TM2MNDKGZAJ300 | 5 -> 1 | drops 4 x "booking"; keeps "Expedia Group and Booking Holdings took note" | YES |
| 13 | BKNG | sa:4399165 | 2 -> 1 | drops "booking a flight"; keeps "the Booking.com app" | YES |
| 14 | BKNG | sa:4553700 | 8 -> 5 | drops "booking decisions", "booking window", "direct booking rates"; keeps title and "Booking Holdings" x4 | YES |
| 15 | ORA_FP | bbg:T8ERVUT96OSM00 | 6 -> 2 | drops "orange harvest", "orange groves"; keeps headline "Smallest Orange Crop" | NO -- Florida oranges |
| 16 | ORA_FP | bbg:TEPZPSKJH6V600 | 6 -> 4 | drops "orange juice contract"; keeps "Orange Juice Jumps", "Orange groves" | NO -- orange juice futures |
| 17 | ORA_FP | sa:4603901 | 2 -> 1 | drops "red-orange-green bands"; keeps "Total Orange" (a Nike colourway) | NO |
| 18 | ORANY | bbg:T8ERVUT96OSM00 | 6 -> 2 | as row 15 | NO |
| 19 | ORANY | bbg:TEPZPSKJH6V600 | 6 -> 4 | as row 16 | NO |
| 20 | ORANY | sa:4603901 | 2 -> 1 | as row 17 | NO |

**The finding.** R30 does exactly what was signed: every dropped span is a non-company lower-case use, so every count-down is right on its
own terms. But 14 of 20 rows (all 8 Visa, all 6 Orange) are not about the company at all, and survive only on a capitalised headline or
sentence-initial word. Visa, Orange and Booking are common nouns that title-case headlines capitalise. The next rule is for the CTO to
rule: a common-word alias (Visa, Orange, Booking, Apple, Monster, Cadence) counts only with a second anchor (a ticker form, the legal
name, "Inc"/"S.A.", or a brand form such as "Booking.com") in the same article. That would remove these pairs. Rolling back rebuild #12
would not.

## What could not be read

- Nothing among the 50 rows: 47 of 47 distinct articles were found in silver, and every row's spans were read in context.
- The sample is 30 of 285 removals and 20 of 113 count-downs (every k-th, by the issuer). The finding's 14-of-20 share is a sample share, not
  a census of the 113.

-- 3.0.0_SA_CVO
