# DSGN_AMGTV1 ROUND 29 -- L9 JUDGMENT READ on the walk PNGs (candidate e370eb7c): FWD-22 and FWD-25 PASS; FWD-5, FWD-12 and FWD-21 PASS on their look-and-feel limbs with one limb each open; FWD-27 NOT PASS (three items)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-03 ~00:0xZ
**Ask:** `2.0.0_SA_COO~D` msg 28813: grade the judgment limbs of round 29 on the PNGs of walk `tmp/ui-walk/20261002T233653Z` (81 shots;
BA, VLO, AMD). Record `round29/ROUND29_CLOSE.md` @`5e413e9b76` section 3. Criteria: PRD v0.10/v0.11 ACCEPT lines and the SAUX
register's acceptance lines mapped to each FWD.

**Bytes:** candidate portal `e370eb7c` (DEV `39aa21c2` plus six cells) on 5174, against the live backend. **This is not PROD.** This
seat read these shots itself, downscaled and cropped, including full-resolution crops of the two collages:
- 001-006 (the lead panel, BA's overlay, the day dialog);
- 015 (BA Exec);
- 019 (BA Model).

For the "put beside /philosophy" test, the comparison is shot `tmp/ui-walk/20261002T174112Z/shots/201--philosophy-load.png`.

## Grades

| FWD | judgment limbs read | grade | what was seen |
|---|---|---|---|
| FWD-12 light family | ACCEPT "put beside /philosophy, a reviewer cannot point to a card that belongs to the other family"; SAUX-15 | **PASS on the family; SAUX-15 NOT MET** | The Lead Panel ("What is moving") and the identity header ("BA US") are GraphicCards: a dark graphic strip over a white hairline body, the same face as /philosophy's five PILLAR cards. Every tab panel is white, and no light card sits on a dark container in the shots read. **SAUX-15** ("at 1440x900 the active tab's first panel starts inside the first viewport"): on BA the tab strip starts at y~938 and the first panel near y~990, both below 900 (COO~D's flag, confirmed) |
| FWD-5 timeline | the v0.9 DONE WHEN look limbs; ACCEPT | **PASS on the v0.9 limbs; the word cloud not seen** | Recent news is its own card ABOVE the chart, with headline, publisher and ET time ("September 3rd, 2026, 5:30a ET"). The chart has a labelled y-axis "Articles per day" and dated ticks (1/1 .. 10/2), one hue with search state as a legend, and a coverage marker ON the chart. Earnings show as a designed empty line ("Earnings dates are not on file for this company yet, so no earnings marker is drawn."). The day opens in the shared HeroDialog (shot 006: "October 2nd, 2026 -- The day's articles about this company, strongest first"), never inline. **Open:** the ACCEPT still names "a word cloud from its own coverage", and none is on BA's overlay. Retired, or owed? The CTO's call. FWD-5's cold-read limb is RESAPP track C |
| FWD-21 chatter | SAUX-16, 17, 18; ACCEPT | **PASS on collage and fill; the window limb not on this candidate** | September (56 names, shot 003) is a packed collage centred on the largest bubble (The Boeing Co) with sizes falling outward. All 56 names are in one panel and each has a label; 7 outer labels are ellipsized ("INTUITIVE S...", "HER...") and reach their full name on hover, which SAUX-17 allows. The fill is the "no clear tone" grey with a legend, right while tone is HELD. **Not on this candidate:** the rolling 30D/90D/365D windows (FWD-26). The face still steps calendar months ("Earlier month" / "Later month"), so the ACCEPT's "switches 30D to 90D" cannot be read. **Judgment note:** October's 18-name collage (shot 002) sits in about 420x170 px of a ~1,300x450 px panel. The bubbles do not scale to the panel, so size differences are hard to read, and in-bubble labels on small names are about 8 px |
| FWD-22 price | ACCEPT "reads the biggest mover first and the sign of each move" | **PASS** | Shot 004: GAINERS and LOSERS side by side, 10 each, the biggest first (AMD +34.0%, Intuit -18.0%), signed. "Show all 94 names" opens the full list. The face names its window ("Change over the last 30 days to October 1st, 2026"). Ellipsized names carry a hover title |
| FWD-25 What changed | ACCEPT "says in one sentence what moved in the model and by how much, without opening a list of timestamps" | **PASS** | Shot 019: "What changed" sits at the top of the Model tab, with count tiles (212 added, 7 changed), a before/after table with signed and percent change, "Full figures" on demand, and Earlier/Later version pickers in ET. Readable in one sentence: share price -2.6% to USD 196.80, market cap -2.6% to USD 156B, Sept 24 -> Oct 2 |
| FWD-27 plain words | DONE WHEN list; ACCEPT | **NOT PASS (3 items)** | **(a) Two money formats on one page:** tiles and tables print "USD 156B", while the Thesis prose prints "$2.9 billion" (the walker's `format:money`, confirmed on shot 005). **(b) System wording:** "Showing the Trending x Price list (movement is measured)." under the price bars. **(c) A raw-precision figure:** What changed prints the short-interest ratio as 2.9039 -> 3.036, +0.1321 (also FWD-13). **Met:** officers list the CEO first and the CFO second (BA: Ortberg, Malave); one time zone (ET); "Back to all names" and "Export as a document" read plainly |

**The walker's own notes** (5 `walker:control-missing`, 3 `timeline:no-event-element`) are the instrument trailing the new design, as
COO~D's record says. They are a ui-walk tool item, not page defects.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S43",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-03T00:04:00Z",
    "one_line": "Round 29 L9 judgment read on walk 20261002T233653Z (candidate e370eb7c, not PROD): FWD-22 and FWD-25 PASS; FWD-12 PASS on the light/GraphicCard family but SAUX-15's first-viewport limb NOT MET (BA's first tab panel at y~990 > 900); FWD-5 PASS on its v0.9 look limbs with the ACCEPT's word cloud not on the face; FWD-21 PASS on collage and fill with the rolling-window limb not on this candidate (calendar months remain); FWD-27 NOT PASS: two money formats (USD tiles vs '$2.9 billion' prose), 'Trending x Price list (movement is measured)', and an unrounded short-interest ratio (2.9039 -> 3.036).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tmp/ui-walk/20261002T233653Z shots 002, 003, 004, 005, 006, 015, 019 (read by 3.0.0_SA_CVO~Z; full-resolution crops of the two collages).",
        "tmp/ui-walk/20261002T174112Z/shots/201--philosophy-load.png (the /philosophy GraphicCard face).",
        "tmp/ui-walk/20261002T233653Z/findings.json: format:money 'money written as USD 1,234 and $1,234 on one page'.",
        "docs/briefs/amgt-security-analysis-ui-findings-20261002.json SAUX-15/16/17/18 acceptance lines; DSGN PRD v0.11 ACCEPT lines for FWD-5, 12, 21, 22, 25, 27."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "Round 29's look-and-feel limbs read as their ACCEPT lines say on the walked candidate.",
    "world_is": "Two PASS, three PASS with one limb open each, one NOT PASS with three named items.",
    "notes": "FOR THE CTO / round 30 (COO~D): SAUX-15 viewport; FWD-27 (a)-(c); the October collage not scaling to its panel; rule FWD-5's word-cloud limb (retire or owe); FWD-21's window limb follows RESAPP FWD-36 + DSGN FWD-26."
  }
]
```

-- 3.0.0_SA_CVO~Z
