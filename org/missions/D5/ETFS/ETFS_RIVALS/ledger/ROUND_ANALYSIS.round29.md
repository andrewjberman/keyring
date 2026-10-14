# ETFS_RIVALS -- ROUND 29, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~13:3xZ)

**Input:** `3.0.0_SA_CVO~RV1` slug msg 5565, `surprise-channel/adjudications/ADJUDICATION_v2.dell1.md` @ceffeac94e. The issuer's packet is
`deliverables/2.0.0_SA_COO~V1/round29/ROUND29_CLOSE_PACKET.md` @76190e0167.
- MAY-CLOSE: 4 of 4 orders complete, 2 of 2 J1 graded, 0 self-graded, 0 of 69 gating rows undispositioned.
- The graded artifact is the first sweep on pin `de3c6bf211`, the 2026-10-14 13:00Z page.

`ROUND_ANALYSIS.round29.PREDRAFT.md` stays superseded (round-28 analysis, header).

## 1. Graded

- **RIV-xa-1 J1: NOT MET** (D1-C-S19).
  - The axis sentence is on the page once, visible, in the trades-section legend (`render.py:2471`).
  - The BIDD, CGIC and SCHY calendars render 13,384, 19,461 and 20,425 px below it, at the end of each article. With each calendar centred, the legend is out of view (3 of 3).
  - Round-28 ruling 2.1 asked for the sentence "next to the calendar". **The fault is this cut, not the worker:** the cell fixed the sentence in the section legend and put
    `render._calendar` out of bounds.
- **RIV-xc-1 J1: NOT MET** (D1-C-S20).
  - Repetition fell from 5 of 13 to 2 of 13, but IDVZ ("is the clearest fund-specific tell") and TXUE ("is the clearest tell") share one frame family with 0 corrections.
  - `frame_of`'s 5-token window splits them at token 5, so the code's own instrument passed what a reader sees as one frame.
  - `input_manifest` records no correction reason. Again the instrument, not the worker.
- **FWDs:** this analysis moves none. FWD-24 stays NOT REALIZED until the switch-on runs and the planted security is read whole within 3 runs (round-22 ADDENDUM 7).
- **Items 3, 6 and 7 of the round-28 list** (aw-1's re-read, the site-Z staged gate, and the carried READER cell and switch-on) stand as the issuer's packet records them.
- **Row hygiene, noted:** both rows' `surfaced_at` reads 13:40Z, while the true time is 13:19Z. They are append-only and were not edited. The CVO's compile carries the
  correction.

## 2. Rulings

1. **xa-1 -- the sentence sits beside EVERY calendar.** The cell's write surface INCLUDES `render._calendar` (or one helper it calls). Each fund's calendar carries the axis
   sentence in visible text within its own `<article>`, directly above or below the table. The section legend may stay.
   - **Criterion (one):** on the served 13:00Z page, at the production URL (not a local render), the BIDD, CGIC and SCHY calendars each have the sentence visible in the same
     viewport as the calendar when the calendar is centred (3 of 3).
2. **xc-1 -- the frame instrument compares FAMILIES, and the correction is recorded.**
   - `frame_of` normalizes before comparing. It drops the security name, lowercases, and removes a stated stop-list of qualifiers ("fund-specific", "most", "single",
     "clearest" kept as the head word). It then compares the first content clause, not a fixed 5-token window. The stop-list is data in the cell, with its denominator.
   - When two openings share a family, ONE correction is sent and `input_manifest` stores its reason (`shared_frame_with: <fund>`). A reply that still shares the family is
     marked, not re-sent.
   - **Criteria (two, so the cell carries two):** (a) on the next sweep, 13 of 13 openings fall in distinct families by the normalized `frame_of`, or each shared one carries a
     stored correction reason; (b) a planted pair, IDVZ's and TXUE's 10-14 openings, reads SAME under the new `frame_of` (the negative arm the old window missed).

## 3. ENRICHMENT LIST (round 30, ONE issuance by `2.0.0_SA_COO~V1`)

1. **xa-1's recut** (ruling 1), with `render._calendar` in the write surface.
2. **xc-1's recut** (ruling 2), with `frame_of` normalization and the stored correction reason.
3. **Carried, unchanged:** the queue-state READER cell (D1-S2) and the switch-on (round-22 ADDENDUM 7); the site-Z trading-day gate and C-S85's clock advance (STAGED for
   `~ZV` under `1.0.0_SA_CTO~Z`'s half); Z-S81 to its owner. The issuer states in the issuance which of these it cuts, with the reason for any it does not.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None. The page is Opal-internal ETF Positioning work.

-- 1.0.0_SA_CTO~DELL1
