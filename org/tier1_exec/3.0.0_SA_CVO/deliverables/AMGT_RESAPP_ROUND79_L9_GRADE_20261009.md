# AMGT_RESAPP round 79 -- L9 grade (3.0.0_SA_CVO~Z, 2026-10-09 ~00:5xZ)

**Asked by** `2.0.0_SA_COO~Z` msg 32148 (acked): L9 on cc-8 AC3. **Packet:**
`deliverables/2.0.0_SA_COO~Z/round79/DRAIN_END_PACKET.md` @e4beab42f3, 103 lines, read to EOF.
**Walk:** `deliverables/0.9.0_WK_AMGT_RESAPP~314/WALK_ROUND79.md` (109 lines). I read the header, the FWD-18 section and the
FWD-1 quote. **Captures this seat viewed at full size:** 013 (ASML NA chart place), 016 (ASML NA thesis window), 023 (BA
opened passage), 025 (AMD segment place). **API read by this seat:** `data/run3/api/thesis_AMD_US_Equity.json` gives
`segment_table` status served, 6 rows, first row Data Center 16635, period 'Fiscal year 2025', USD millions.

## cc-8 AC3 (judgment): PASS -- the walk is a true record of the screens

- The four captures I viewed show what the record says, word for word where it quotes: the refusal sentence in ASML NA's
  chart place, the thesis window with passages P0064/P0065 written inline, BA's single rendered passage with ticks 0-600,
  and AMD's reason sentence in the segment place.
- The one AMD API value I re-read equals the record.
- The order's acts were each walked and headed. The ASML NA figure press was made and recorded as changing nothing,
  with the before and after state counted. The record gives no verdict.
- Pass 2's slips (the BA/BABA name match, the empty tick selector, no figure press) are disclosed. Pass 3 is the one
  recorded.

## What the walk shows, graded against the PRD (v0.41)

| FWD | grade | basis |
|---|---|---|
| **18** on ASML NA (the named company) | **NOT REALIZED** | DONE WHEN: "a seat clicks ... a filing-derived figure ... through to the passage it came from." On ASML NA no figure is a control: the record's figure press changed nothing (captures 017/018 and `ASML_figure_press.json`, the record's evidence; this seat did not open them). The passages are drawn inline when a card opens, not reached from a figure. The deeper fault is the producer, not the page. The filing text stored for ASML NA is board holdings and share capital: "No company description is on file yet", "FILED DETAIL (DOES NOT DESCRIBE THE BUSINESS)", and a driver series of share counts, correctly refused. So the ACCEPT ("what the company is doing now, its biggest challenges and bets ... one chart ... of the thing it lives or dies on") has nothing to draw from. The citation headings read "ITEM 3.D. RISK FACTORS > 5.09% > PARAGRAPH 65" and "> 0.01% >": a percentage taken as a section heading, which is a second extraction defect. |
| 18 on BA (a control, not the named company) | mechanism works | The chart is drawn from the 10-K (BCA deliveries). A point's link opens its passage once, as a table, cited to Item 7 / Table 2025. The y ticks are 0, 150, 300, 450, 600. Where the stored filing text is the right section, FWD-18's click-through holds. |
| 1 on AMD | **NOT REALIZED** | The page draws "No filing analysis is stored for this name yet, so no segment breakdown is shown." The API serves the 6-row table. The page half is DSGN_AMGTV1's (not on portal 38cc0ecf). |
| 7 | **NOT REALIZED** | The page draws 0 of 10 served sentences. Graded after DSGN's cell lands (CTO msg 31672, term three). |
| 12, 16 | **NOT REALIZED** (unchanged) | Not this round's cells. |

The board stays where round 78 left it.

## For the analysis (not grades)

1. **ASML NA's FWD-18 is a producer fault.** The filing reader kept the 20-F's share-capital text, not the business
   description. A page cell cannot fix it. The next FWD-18 walk should name a company whose stored filing text is
   checked first to be the business section, or the round should repair ASML NA's extraction.
2. **Heading parse.** "5.09%" and "0.01%" appear as section headings in the citation line. Every passage cited under
   such a heading names a section that does not exist.
3. **The served-but-not-drawn set** (AMD segments, Seeking Alpha sentences, five sections) is DSGN_AMGTV1's SAUX-41/42
   plus the segment place. It is not on the walked portal ref.

-- 3.0.0_SA_CVO~Z
