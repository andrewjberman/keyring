# AMGT_CORPUS ROUND 29 -- L8 COMPILE + L9 (CRPS-ae-1 AC4)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~09:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND29_DRAIN_END_PACKET.md` @`33bbd932c6` (3,904 B, read to EOF), msg 27716.
**L7 re-measured:** `TO-CRPS-ae-1` reads `complete` on its LAST `<status>` tag. One judgment criterion.
**Read by this seat:** `tmp/ui-walk/20261001T093108Z/shots/030-BA-Model.png` (local DEV `1f059ad1` through the walk checkout).

---

## 1. L9 -- CRPS-ae-1 AC4, "the sheet reads like the analyst's": **MET**

Against this seat's round-28 PARTIAL (ADJUDICATION_v33, three defects), read on `030-BA-Model.png`:

| v33 defect | round 29 face | closed |
|---|---|---|
| "nothing estimated in its place" over unlabelled consensus columns | subtitle "Reported figures and Bloomberg consensus estimates, from the model block"; a spanning "CONSENSUS (BLOOMBERG)" over 2026E-2028E | YES |
| data precision (P/B 540.0126, ROE 1048.6216 beside 4.69) | each row at its type: EPS 7.92 ... -0.83 / 3.91 / 8.02; P/E 14.7x ... 50.3x / 24.6x; P/B 117.6x ... 546.5x; ROE 140.8% / 684.0% / 1,048.6%; EBITDA 8,416 ... 4,343 / 8,498 / 12,322; diluted shares 644 ... 762 | YES |
| unit words disagree within the name | "Figures in USD" once above the sheet; rows read "(per share)", "(millions)", "(%)", "(multiple)"; Revenue/Sh*, EPS*, BVPS*, EBITDA* carry a mark and one footnote reads "* currency not stated by the source for marked rows" | YES |

The face now reads as an analyst's sheet: one grid, a stated currency, consensus labelled as consensus, figures at sheet precision,
and the team-case lines beneath. Two small residues remain below the sheet, outside the grid: "147 of 342 fiscal figure(s) on the
block rendered; 0 sheet row(s) not in the pack" (the issuer's own carried item: reads as a loss, and presupposes a pack), and
"Figures in USD" sitting above four rows marked "currency not stated". The footnote makes the second honest rather than wrong.
Neither changes how the sheet reads.

## 2. L8

- **`Z-W1-S28` (ARMED: BEST_DIV_YLD's unit label "DECIMAL" vs the page's percent print):** disarmed by `Z-S76` (issuer ruling), and
  the arithmetic holds on the face: BA consensus DPS 0.005 / 0.286 / 1.187 over price 196.80, x 100 = 0.0025 / 0.1453 / 0.6032,
  which equals the served 0.00254 / 0.14533 / 0.60315 and prints as 0.0% / 0.1% / 0.6%. The values are percent and only the
  producer's label is wrong. That is a label fix for the producer, not a page fix.
- **Portal:** chain c8119301 on local DEV `1f059ad1`; 15 of 16 harnesses with `posture.harness.cjs` RED on DEV too (S3-live,
  excluded from every bound as in DSGN's rounds).

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W1-S28` (ARMED) | **GRADUATED** | disarmed by `Z-S76`; verified by arithmetic on the PNG (section 2) |
| `Z-S76` (the disarm ruling) | **GRADUATED** | as above |
| `Z-S74` | **CARRIED**, INERT | still open |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 1 of 1. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W1-S28` GRADUATED. **MET**
3. **Every judgment criterion graded:** ae-1 AC4 MET. **MET**

## 5. FOR THE ROUND-29 ANALYSIS

Enrichment, not freeze-critical: the "147 of 342 ... not in the pack" footer; BEST_DIV_YLD's "DECIMAL" label at the producer;
`Z-S74`. FWD-20's remaining gap is the 49 template rows that need the V3 Model-figure pull (L4-R v0.7 condition), which waits on
Andrew's word, not on a cell.

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S35",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T09:55:00Z",
    "one_line": "L9 round 29: CRPS-ae-1 AC4 MET -- BA's Model sheet closes all three v33 defects (consensus labelled 'CONSENSUS (BLOOMBERG)' under a truthful subtitle; per-row precision 7.92 / 14.7x / 1,048.6% / 8,416; 'Figures in USD' once with a footnote for 4 marked rows); Z-W1-S28 graduates on Z-S76's ruling, verified by arithmetic (DPS 0.286 / 196.80 x 100 = 0.1453 = served 0.14533).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-CRPS-ae-1 reads 'complete' on its LAST <status> tag.",
        "tmp/ui-walk/20261001T093108Z/shots/030-BA-Model.png: subtitle 'Reported figures and Bloomberg consensus estimates, from the model block'; header 'CONSENSUS (BLOOMBERG)' over 2026E-2028E; 'Figures in USD'; EPS 7.92 ... -0.83 3.91 8.02; P/E 14.7x ... 50.3x 24.6x; ROE 140.8% 684.0% 1,048.6%; EBITDA 8,416 ... 4,343 8,498 12,322; Dividend yield 2026E-2028E 0.0% 0.1% 0.6%; footnote '* currency not stated by the source for marked rows'.",
        "Arithmetic: BA consensus DPS 0.005, 0.286, 1.187 / price 196.80 x 100 = 0.0025, 0.1453, 0.6032 vs served BEST_DIV_YLD 0.00254, 0.14533, 0.60315 (packet section 2)."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W1-S28",
      "AMGT_CORPUS-Z-S76"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @33bbd932c6 asserts ae-1 complete and the Model sheet reading like the analyst's on BA's real run.",
    "world_is": "True on the graded PNG; residues below the grid only (the 147-of-342 footer; USD stated above four currency-not-stated rows, footnoted).",
    "notes": "FOR THE ROUND-29 ANALYSIS: enrichment only -- the footer, BEST_DIV_YLD's producer label, Z-S74; FWD-20's 49 rows wait on Andrew's V3 word."
  }
]
```
