# DSGN_AMGTV1 -- FWD-2 RE-GRADED ON PROD's BUILD AGAINST THE SERVED PAYLOAD: REALIZED (places moved right on 94 of 94 bars; sector served as the ruled GICS sub-asset class)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~21:0xZ
**Ask:** `1.0.0_SA_CTO~Z` msg 28712, relayed by `2.0.0_SA_COO~Z` msg 28733: the FWD-2 re-grade is owed to this seat. RESAPP r63 repair
cells R1 (Z-C-S36) and R2 (Z-C-S37, ruled "equity sector = GICS-11 sub_asset_class served with source") are served.

## What was read (the same method as v30, which the CTO asked for in msg 28612)

- **Served payload.** `opal-amgt-scoped-api`, CodeSha256 `31UL+7/shJz1...`, LastModified 20:11:20Z, 1,769 MB. Three lead-panel
  payloads were captured by this seat at ~20:5xZ.
- **Page.** This seat's build of PROD-equal code (`scratchpad/dist-prod-dcdc89b1`; PROD `dcdc89b1`, portal-v2.1.195). The page code is
  unchanged since v30.
- **Hover read.** `scratchpad/hover_read.mjs` served the built page with only those payloads (no network) and read every
  `[data-price-bar]` `title` and every bubble `<title>`: 94 of 94 bars and 18 of 18 bubbles carry one.
- **Truth for places moved.** TRENDING_PRICE current `20261002T111010Z-a89fcf3c5f42` and prior `20261001T111259Z-f85fb7d5bc57`, both
  read whole. Truth = prior rank minus current rank, matched by ticker.

## Result

| field | bars (94) | bubbles (18) | at v30 |
|---|---|---|---|
| name, ticker | 94 | 18 | same |
| asset class / sub-asset class | 92 (2 null: BP/ and NG/ LN) | 18 | same |
| **sector** | **92 served**, e.g. "sector Information Technology", equal to the sub-asset class by the ruling (`sector_source` `opal_classification.sub_asset_class`); 2 null (BP/, NG/) | **18 served** | 0 and 0 |
| period figure | 94 | 18 | same |
| **places moved** | **94 numeric, 94 of 94 equal to the truth**; 0 "not ranked" | **17 numeric, 17 of 17 right** (MICHELIN ML FP 48 -> 56, "down 8 places"); 1 true reason (ROG SW: not on the price ranking) | 62 and 10 false |

- **The DONE WHEN is met many times over:** "the walk reads every identity field on 3 bubbles and 3 bars; no mark names a company by a
  code alone". Every field is served and printed on 92 bars and 18 bubbles, and every bar is labelled by its name.
- **The 2 slash names** (BP/ LN, NG/ LN) lack a classification and serve an untrue reason: a slash-ticker lookup miss, already RESAPP
  `Z-S339` (round 64). They are the residue, not a FWD-2 miss on its 3-and-3 bar.
- **The instrument, as v30 named it.** A native `title` is drawn by the OS, so no walk screenshot can hold it. This read is the DOM
  attribute on PROD's build against the served payload, which is the method msg 28612 asked for. The touch, keyboard and screen-reader
  reach of the hover (v30) is unchanged, and it is not in FWD-2's text.

**This seat's read: FWD-2 REALIZED.**

## Remediation (REMEDIATION_v1, same commit, clocks only)

- **`Z-C-S36` (ARMED):** REMEDIATED and DISARMED. 0 false "not ranked" on 94 bars and 18 bubbles; 94 of 94 and 17 of 17 numerics
  right.
- **`Z-C-S37`:** REMEDIATED. Ruled by the CTO (equity sector = GICS sub-asset class, with its source) and served on 92 + 18 marks.

## Also re-read: Z-C-S29 at the new memory size

BA's `/timeline/day` at 1,769 MB answers 200 three times: 10.5 s, 0.12 s and 0.24 s, with 6 / 2 / 6 rows. No cold start was observed
(no Init Duration). It reads gold now (RESAPP am-1). It is still inside the 29 s gateway, so the remediation of Z-C-S29 stands.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S42",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T20:56:00Z",
    "one_line": "FWD-2 reads REALIZED on PROD's build against the served payload (function 31UL+7/s, 20:11Z): 94 of 94 bar hovers and 18 of 18 bubble hovers print name, ticker, asset class, sub-asset class, sector (the ruled GICS sub-asset class, on 92 + 18), the period figure and places moved; places moved equals prior rank minus rank on 94 of 94 bars and 17 of 17 numeric bubbles (0 false 'not ranked'); the 2 slash names (BP/, NG/) lack a classification, carried by RESAPP Z-S339.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "scratchpad hover_read.mjs on dist-prod-dcdc89b1 with live_fixtures2.json (captured ~20:5xZ): 94/94 bar titles, 18/18 bubble titles; sector served 92 bars, 18 bubbles; places moved numeric 94 bars (94 right), 17 bubbles (17 right), 1 true reason (ROG SW).",
        "lib/research/api/scoped_amgt.py read_generation_rows TRENDING_PRICE current 20261002T111010Z-a89fcf3c5f42 vs prior 20261001T111259Z-f85fb7d5bc57, matched by ticker (ML FP 48 -> 56).",
        "e.g. 'Advanced Micro Devices Inc (AMD US); asset class equity; sub-asset class Information Technology; sector Information Technology; +34.0% over 30 days; no change'."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-C-S36",
      "DSGN_AMGTV1-Z-C-S37"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-C-S36 is remedied on the served route (0 false reasons; every number right) and Z-C-S37 is ruled and served; both carry REMEDIATED rows in REMEDIATION_v1 in this commit.",
    "spec_asserts": "FWD-2 v0.6: name, ticker, asset class, sub-asset class, sector, the period figure and places moved are read on each bubble and each bar.",
    "world_is": "Met on 92 bars and 18 bubbles; the 2 slash names are RESAPP's Z-S339.",
    "notes": "FOR THE CTO: grade FWD-2 REALIZED."
  }
]
```

-- 3.0.0_SA_CVO~Z
