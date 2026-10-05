# DSGN_AMGTV1 -- round 38 enrichment list and the FWD-11 judgment (1.0.0_SA_CTO~Z, 2026-10-05 ~06:0xZ)

**Input:** `2.0.0_SA_COO~D` msg 29499; `deliverables/2.0.0_SA_COO~D/round37/ROUND37_CLOSE.md` @8f7ed51562. Round 37 is CLOSED. The
candidate `85e24287` is the approved 7f679aee merged onto DEV 3e1aa46f; its DEV push is held for Andrew's word.

## FWD-11 judgment (the person's side-by-side read)

Read from the walker's 1440 captures (`round37/walk/read-20261005T054042Z/fwd11-*.png`): Security Analysis (BA US), Philosophy and
Market.

- **The card family is not a FWD-11 defect. FWD-12 governs it.** FWD-12 ratifies the light family with at most one dark band, which
  is the /philosophy GraphicCard face. The reference pages do not share one family themselves: Market is dark navy end to end, while
  Philosophy is light cards with one dark chart card. So FWD-11's "the same pieces" is read as the shared COMPONENTS, not one colour
  family.
- **What matches:**
  - the page header (title, purple subtitle, left rule);
  - the underlined tab row, the same as Philosophy's;
  - the white hairline cards with navy ink;
  - the shared chart library and tooltip, per the issuer.
- **What does not match, so FWD-11 stays NOT_REALIZED:**
  - **Footers.** Every Market and Philosophy card ends in a footer that reads as a time and a source ("October 4th, 2026, 5:20p
    ET | Source: Bloomberg ...", "2026 | Source: Yang Liu, CFA, CAIA."). The Security Analysis cards carry none in that form; the
    news card, the timeline and the key-figure row have no footer at all.
  - **The end line.** Both reference pages end with "End of <page>. Data as of <date>." Security Analysis does not.

## ROUND 38 LIST (ONE issuance by `2.0.0_SA_COO~D`)

1. **FWD-19:** "What changed" renders the shared PanelLoading and PanelError. A 500 shows the designed error, never a skeleton.
2. **FWD-11 footers:** every card on the page ends in the shared footer, reading as a time and a source, from served fields only. A
   card with no served time or source prints no footer line (FWD-27). The page ends with the shared "End of Security Analysis. Data
   as of <served date>." line.
3. **Read owed:** FWD-11 re-read side by side on the served candidate.

**Dropped from the list: my round-37 non-blocking note** (key the money columns on a producer marker). On reflection, the present
rule fails SAFE: an unknown column reads UNSTATED and prints no average. Losing an average is benign. Averaging across currencies is
the harm FWD-8 forbids, and the present rule never does it.

## Producer gaps (routed to AMGT_RESAPP, not page cells)

- **Price currency:** no peer member serves a price currency, so the Price column reads "Not averaged: currency not stated" on every
  name. This corrects my round-37 review's line "Price reads the row's own trading currency": true for the subject, but members serve
  none.
- **Own-publication origin:** FWD-5's "the firm's own publications come first" holds only vacuously, because the day route serves no
  origin field.
- **AMD timeline:** AMD serves no timeline events. That is a served-data fact, carried as is.
