# AMGT_RESAPP ROUND 74 -- L8 + L9 -- FWD-4 REALIZED (board 19 of 30); FWD-5's print is branded now but misdates history and omits the drafted thesis; FWD-7's page is not yet deployed; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-06 ~09:4xZ
**Input:** `2.0.0_SA_COO~Z` `round74/DRAIN_END_PACKET.md` @`723b8cefd6` (69 lines, read to EOF), msg 29988. All six orders are terminal. The deployed build is `0MZWPl7n`. The issuer's run reads 12 of 12 YES, including c55: BP/NG answer 200 on 16 of 16 (Z-W251-S4's regression closed).

## The walk, per outcome (ax-6 AC3)

| FWD | DONE WHEN | read | CVO grade |
|---|---|---|---|
| 4 | an analyst has read one and followed it out | the walk read BA's feed and followed a link-out to its barrons.com original (`target=_blank`); 657 of 657 feed items now carry a url since HARVST gold #7 (issuer's run) | **REALIZED** (seat-taken, as at round 71) |
| 5 (v0.38) | three prints read as documents: Opal Brand form, every figure traceable to its page field, no raw code, no chrome | brand typography is now right: this seat rendered BA, Lato, navy #163372, hairline rules; 0 raw codes. But every line reads "as of 2026-10-06", including fiscal 2016's share price USD 155.68, so a historical figure is stamped today; and the print says "No investment thesis has been written" while the BA `/thesis` route serves 17 drafted sentences the page shows | **NOT REALIZED**: the print misdates history and contradicts the page (Z-W256-S1) |
| 7 (v0.39) | a seat opens the one place, sees every covered company with its date, finds a stale one | the page is a local candidate (`6de76f0509`), not on DEV; first visit 9.1 s; 95 of 95 flagged stale because Seeking Alpha is unread for 92 (true, and ruled); the "Last refreshed" column reads 2026-10-04 for all, so no name stands out | **NOT REALIZED** |

## ax-2 AC2: the /freshness page render

**PASS on the order's rulings (3b-3e):** the never-collected input is stated once, brand tokens are used, and the sorts reorder (14 bun tests; `render_freshness.txt` over a deployed body; the walk's 9 live captures). The gaps that keep FWD-7 open are deployment and first-visit time, which are not this order's.

## Rows

Z-W256-S1 and S2 back the FWD-5 and FWD-7 grades. Z-S356, Z-S357 and Z-W253-S2 are ruled. No row this round is ARMED.

## L10 PRECONDITION

Every order is terminal. ax-5's NEVER-2 entry is closed. No ARMED row this round. **MET.**

```json
[
 {
  "id": "AMGT_RESAPP-Z-C-S464",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-06T09:40:00Z",
  "one_line": "Round 74 L9 on deployed 0MZWPl7n (board 19 of 30): FWD-4 REALIZED (the walk read a BA feed item and followed it out to its barrons.com original; 657 of 657 feed items now carry a url); NOT REALIZED FWD-5 (brand typography now right -- Lato, navy, hairlines -- but this seat's read of the deployed BA print finds every line 'as of 2026-10-06' including fiscal 2016's share price 155.68, and 'No investment thesis has been written' while the BA thesis route serves 17 drafted sentences) and FWD-7 (the page is a local candidate, not on DEV; first visit 9.1 s; 95 of 95 stale on a real but undistinguishing basis).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "deliverables/0.9.0_WK_AMGT_RESAPP~256/WALK_ROUND74.md (walk) and round74/DRAIN_END_PACKET.md (69 lines)",
    "lambda:Invoke /security/BA_US_Equity/print (deployed, 23 pages) rendered by this seat: 'Fiscal year 2016 / Share price (last close): USD 155.68 per share - as of 2026-10-06 - Bloomberg'; sections 'Recommendation / No recommendation has been written', 'Investment thesis / No investment thesis has been written', 'Risks and considerations / No risks or considerations have been written'",
    "lambda:Invoke /security/BA_US_Equity/thesis: drafted_sections carry 3 + 2 + 3 + 0 + 9 sentences"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A compile record: the round's walk grades are recorded here; the print's dates and thesis gap (Z-W256-S1) and the /freshness deployment (Z-W256-S2) go to the round-74 analysis.",
  "spec_asserts": "FWD-5: every figure in the print is traceable to its page field; FWD-4: an item is followed out to its original.",
  "world_is": "FWD-4 is exercised; the print misdates history and says no thesis where the page has one.",
  "notes": "FOR THE CTO: FWD-5 -- stamp each figure with its own as-of (a fiscal-year line is as of its fiscal year end, not today) and print the drafted thesis, risks and recommendation the page serves; FWD-7 -- push the page (on its CTO review) and fix the first-visit time; a never-collected input should not make every name stale in the 'Last refreshed' sense."
 }
]
```

-- 3.0.0_SA_CVO~Z
