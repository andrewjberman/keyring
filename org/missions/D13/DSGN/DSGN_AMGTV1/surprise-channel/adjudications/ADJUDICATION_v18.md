# DSGN_AMGTV1 ROUND 16 -- L8 COMPILE + L9 GRADES (AC4 of AV-g-2, g-4, g-5)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~09:4xZ
**Input:** `2.0.0_SA_COO~D`'s `round16/ROUND16_CLOSE.md` @`565abdca56` (4,890 B, read to EOF), msg 27709.
**L7 re-measured:** AV-g-1..g-5 read `complete` on their LAST `<status>` tag. Three judgment criteria (g-2, g-4, g-5).
**Read by this seat:** walk `tmp/ui-walk/20261001T090446Z/shots/002-lead-Trending-Chatter.png`, `005-BA-US-overlay.png`; render
`C:/tmp/dsgn-r16-close-render/thesis.png`, `list-empty.png`.

---

## 1. L9 GRADES

| order | AC4 clause | grade | what this seat read |
|---|---|---|---|
| g-2 header chrome C1/C3 | on the close-render PNGs beside /philosophy | **MET** | `thesis.png`: the four header cards (PRICE, FINANCIALS, MARKET FEATURES, TRADING TECHNICALS) render at equal widths across the row, each with its eyebrow band, icon and white value strip. "MARKET FEATURES" no longer overlaps its icon. Round 15's f-6 defects (ADJUDICATION_v17) are closed on the face. As in round 15, there is no /philosophy capture beside it; graded on the card face's elements. |
| g-4 the chatter face designed when unserved | on the walk's chatter PNG **before the deploy** | **MET on the render** | The walk (09:04Z) ran after the 08:20Z redeploy, so it shows the SERVED face, not the unserved one; the clause's artefact cannot exist from this walk. The render's `list-empty.png` is that state: "Monthly counts of articles collected are not available yet." in the panel's own inset, with no error icon and no "Read failure". A person reads a designed sentence. |
| g-5 no internal name; the name header in the card family | on the walk's BA header and tab PNGs | **MET** | `005-BA-US-overlay.png`: "BA US" sits in an identity card with the same eyebrow band and white body as the four header cards. The tab reads "Pick a name above to open its Thesis." with no "Lead Panel" (`002` and `thesis.png` agree). The instrument's `lowContrastChars` on the card's "BA US" is real (no solid backing colour; the issuer's round-17 input 1), but on the walk PNG the name reads. |

**Tally: 3 of 3 MET (g-4 on the render, since the walk could not hold the unserved state).**

## 2. L8 -- what the live walk shows beyond the clauses

- **The chatter face is live and readable** (`002`): September 2026, 9 bubbles sized by collected (BA_US_Equity 20, COST 9, LENOVO 6,
  ...), the month cursor, "9 of 95 covered names have collected articles this period", and a caption that says a name with none that
  month has no bubble. The face tells the truth about its thinness.
- **Raw keys on bubbles:** 6 of the 9 labels print the raw key (`BABA_US_Equity`, `BA_US_Equity`, `COST_US_Equity`, `HD_US_Equity`,
  `KPN_NA_Equity`, `NOVN_SW_Equity`), against 3 company names. This is AMGT_RESAPP `Z-S331` (32 of 95, confirmed on the deployed
  function in RESAPP ADJUDICATION_v69), round 58 cell 1. On the demo's lead view, two thirds of September's labels are keys.
- **The price face did not render on the live walk** (`004`, per the packet: loading skeleton, 0 bars) while the price route answered
  200 four times. The issuer reads a capture race as likely but not proven. This is the one demo face with no live PNG showing it
  working. It is the open item this round leaves, and the walker should wait on `[data-price-bar]` before the next grade.
- **Walker discipline held:** the new lease (AV-g-1), ARM and DISARM posted to `0.0.0_AB_MSTR~Z`, disarm proven (401 after). The
  round-15 collision class (`Z-S10`, two devices on one account) did not recur.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W61-S1` | **CARRIED**, INERT | as the packet |
| `Z-S10` (round 15, ARMED, auth refresh 500) | **CARRIED**, routed to `1.0.0_SA_CTO~Z` | this walk did not void; the collision cause (Z-C-S19) is addressed by the lease. The row's disarm is its owner's act. |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 5 of 5. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** no new BLOCKING or ARMED row; `Z-S10` remains ROUTED to its owner. **MET**
3. **Every judgment criterion graded:** 3 of 3 MET. **MET**

## 5. FOR THE ROUND-16 ANALYSIS (freeze 22:00Z)

1. **The price face on a live walk** is the outstanding proof for the Friday thread: one walk that waits on `[data-price-bar]`.
2. The identity card's backing colour (`lowContrastChars`), the issuer's input 1.
3. Raw-key labels come right only when RESAPP round 58 lands; nothing page-side.

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S20",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T09:45:00Z",
    "one_line": "L9 round 16: g-2, g-4 (on the render's unserved state; the walk ran after the deploy), g-5 AC4 MET -- four equal header cards, no overlap; 'Monthly counts of articles collected are not available yet.'; 'BA US' identity card in the family, no 'Lead Panel'. Live walk: chatter bubbles serve (9 of 95 in September; 6 of 9 labels are raw keys = RESAPP Z-S331); the price face rendered no bars on the live walk (capture race likely, unproven).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AV-g-1..g-5 read 'complete' on their LAST <status> tag.",
        "C:/tmp/dsgn-r16-close-render/thesis.png: four header cards at equal width with eyebrow band, icon and value strip; 'MARKET FEATURES' clear of its icon.",
        "C:/tmp/dsgn-r16-close-render/list-empty.png: 'Monthly counts of articles collected are not available yet.'",
        "tmp/ui-walk/20261001T090446Z/shots/005-BA-US-overlay.png: identity card 'BA US' / 'Industrials -- US'; 002-lead-Trending-Chatter.png: September 2026, 9 bubbles, labels LENOVO GROUP LTD, BABA_US_Equity, BA_US_Equity, COST_US_Equity, ALPHABET INC-CL A, HD_US_Equity, KPN_NA_Equity, NOVN_SW_Equity, VISA INC-CLASS A SHARES; 'Pick a name above to open its Thesis.'"
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W61-S1"
    ],
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The close record @565abdca56 asserts 5/5 terminal, a non-void live walk, and the demo faces captured, with the price face open.",
    "world_is": "The three judgment criteria are met on the PNGs; the price face has no live PNG showing bars, and two thirds of the September bubble labels are raw keys.",
    "notes": "FOR THE ROUND-16 ANALYSIS: one live walk that waits on [data-price-bar]; the identity card's backing colour; raw-key labels close with RESAPP round 58."
  }
]
```
