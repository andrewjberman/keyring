# AMGT_RESAPP ROUND 66 -- L8 + L9 JUDGMENT -- FWD-39's word cloud reads right on BA and VLO but keeps the company's own ticker in 12 of 70 clouds (AMD #2): NOT PASS on the name-word clause; FWD-36 price 90/365 real; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-04 ~01:2xZ
**Input:** `2.0.0_SA_COO~Z`'s `round66/DRAIN_END_PACKET.md` @`4116180c1a` (3,895 B, read to EOF), msg 29100.
- **Orders:** 4 of 4 terminal (ap-1 to ap-4).
- **Deployed:** `opal-amgt-scoped-api` CodeSha256 `FcVBPafw...`, LastModified 2026-10-03T23:49:22Z, 1,769 MB.
- **Authority:** Andrew-direct ~20:3xZ cards 4 (the PX_LAST year pull) and 5 (FWD-39), and ~20:5xZ (the daily job, ADDENDUM 2).

## 1. FWD-39 -- the judgment read of the served terms

FWD-39 DONE WHEN (PRD at HEAD): "on 3 covered names, the timeline payload carries `word_cloud`: the security's top terms (at most 40)
with their counts, counted over the headlines of its own gold mention rows in the timeline's window, after a DECLARED stop-word list
(printed with its source) and the company's own name words". ACCEPT: "The PM sees the words its own coverage repeats".

**Read as a reader would** (this seat's invokes, ~01:1xZ):

| name | top terms | read |
|---|---|---|
| BA | max 40, order 28, trump 28, jet 27, air 23, defense 23, jets 21, production 21, airbus 16, faa 16, deliveries 12, farnborough 11 | **reads right**: Boeing's year (737 MAX, orders, the FAA, Farnborough). "boeing" is excluded |
| VLO | refinery 10, oil 9, diesel 6, gasoline 6, trump 6, arthur 5, port 5, venezuelan 4, e15 3, export 3 | **reads right**: Port Arthur, Venezuelan crude, E15. One publisher word, "reuters" 4 |
| AMD | chip 20, **amd 18**, tsmc 17, **top 14**, nvidia 12, earnings 11, **notable 10**, tech 10, market 9, ... **quant 6**, **among 5**, **headlines 5** | **misses the name-word clause**: the company's own name "AMD" is its #2 term. Headline boilerplate fills the rest ("Notable analyst calls ... among top picks", "Quant headlines") |

**The census over every covered name** (95 timeline payloads):
- 25 serve an empty cloud with the designed reason.
- Of the 70 non-empty clouds, **12 carry the company's own ticker word**: AMD (#2), UNH (#3), ADBE (#5), SPOT (#6), TSM (#7), NKE (#8),
  NFLX (#10), SHOP (#10), HAL (#13), INTU, COST, VLO. The exclusion covers the display-name words ("Advanced Micro Devices") but not
  the ticker or brand the coverage actually uses.
- **Boilerplate words the 158-word stop list misses:** "among" in 31 clouds, "top" 24, "quant" 15, "focus" 11, "big" 11, "notable"
  10, "higher" 7.

**Grade: FWD-39 NOT PASS on its name-word clause** (AMD is one of the three named readers, and 12 of 70 clouds carry the ticker). It
is a list-level fix:
1. add the ticker root and the served short/long name words to the exclusion;
2. extend the declared stop list with the measured headline boilerplate.

Singular and plural are not merged ("jet"/"jets", "order"/"orders"). That is cosmetic.

**One served oddity.** The empty-window block serves the route's clamped `from` (2026-01-01) after its `to` (2025-06-30), the packet
reports. An inverted range should not print as-is.

## 2. FWD-36 price 90/365 -- real windows now

`/lead-panel/rankings/trending/price?days=90` serves 94 rows and `?days=365` 95 rows, `window_end` 2026-10-02 (the last trading day),
from the stored year pull (ap-3: 95 of 95, `year_pull.json` 562,248 B, write-once). The qualified wait is cleared by Andrew's card 4.
**Owed by this seat:** the post-run read after the daily job's first scheduled run (2026-10-04 11:00Z): the 30-day exit code and row
counts, the `daily_30d.json` key, and the 90/365 branch taken.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| Z-W218-S1 | DISMISSED_WITH_REASON | a fixture stub for the new route read, inside the cell |
| Z-S344 | DISMISSED_WITH_REASON | disarmed by its owner @`6e1852e03f`: c10 keeps its 30-day clauses and c22 grades 90/365 |

The packet's three CTO-routed items (FWD-38 (d) provenance; FWD-36 tone from the served `chatter_window`; DE_US 404) are carried to
round 67 by the CTO.

## 4. L10 PRECONDITION

4 of 4 orders are terminal; both rows are dispositioned; the judgment limb is graded above. **MET.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S454",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-04T01:11:00Z",
    "one_line": "Round 66 L9: FWD-39 NOT PASS on its name-word clause -- BA and VLO clouds read as their coverage, but AMD's own name 'amd' is its #2 term, and across 95 served clouds (25 empty with reason) 12 of 70 carry the company's own ticker word (AMD, UNH, ADBE, SPOT, TSM, NKE, NFLX, SHOP, HAL, INTU, COST, VLO) while headline boilerplate the 158-word stop list misses recurs ('among' 31 clouds, 'top' 24, 'quant' 15, 'notable' 10); FWD-36 price 90/365 serve 94/95 rows ending 2026-10-02 from the stored year pull.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opal-amgt-scoped-api FcVBPafw (23:49:22Z): /security/<key>/timeline word_cloud for BA, AMD, VLO, HEI and all 95 chatter-universe keys (~01:1xZ): 25 empty; 12 of 70 non-empty contain their own ticker root; boilerplate counts as stated.",
        "/lead-panel/rankings/trending/price ?days=90 -> 94 rows, ?days=365 -> 95 rows, window_end 2026-10-02.",
        "AMGT_RESAPP PRD at HEAD, FWD-39 DONE WHEN ('after a DECLARED stop-word list ... and the company's own name words')."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W218-S1",
      "AMGT_RESAPP-Z-S344"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-39: top terms after the declared stop words and the company's own name words; the PM sees the words its own coverage repeats.",
    "world_is": "The ticker/brand word survives in 12 of 70 clouds and headline boilerplate in many.",
    "notes": "FOR THE CTO: a list-level repair -- exclude the ticker root and served short/long name words; extend the declared stop list with the measured boilerplate; do not print an inverted from/to on the empty block. Z-W218-S1 (inside the cell) and Z-S344 (disarmed @6e1852e03f) need no act."
  }
]
```

-- 3.0.0_SA_CVO~Z
