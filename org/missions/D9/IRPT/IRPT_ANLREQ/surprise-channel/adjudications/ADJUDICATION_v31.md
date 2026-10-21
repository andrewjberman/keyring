# IRPT_ANLREQ: CVO adjudication, FWD-10 (Core) on runs 7K and 7M -- judgment MET; FWD-10 REALIZED; L10 slug withheld (round-close REFUSED)

<sweep_watermark>2026-10-21T15:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-21T15:10Z, a seat that did none of this work. Input:
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/L8_PACKET_FWD10_RUN7M_20261021.md`, blob 9cfe560b26f5 @8ff470b3ff
(msg 20261021T150233Z; verified by `git hash-object`). It adds to the 7K packet graded in ADJUDICATION_v30.

## What this seat read itself

- **The served 7M PDF** `C:/dev/andrew_samples/Opal_MultiComp_sample_FWD10_7M.pdf`: 309,963 bytes, sha256 `db369fa6f8c59709...`, which
  equals the packet; 60 pages. Pages 59 and 60 were rendered and read as images, and their text was extracted.
  - **Page 59:** the common window "2024-04-30 to 2026-10-20 (2.4 years)" with its rule; a cumulative-return chart and legend of four
    lines (Your portfolio, Opal Short-Term, Opal Long-Term, Vanguard Real Estate ETF); periodic returns 1M, 3M, YTD and 1Y for all four,
    with 3Y, 5Y and 10Y n/a in words; std dev, Sharpe, Sortino, max drawdown, alpha and beta for all four on the stated references (SPY,
    BIL).
  - **Page 60:** allocation for all four. The portfolio is 27 / 73 / 0 / 0 by accepted holdings. Short-Term is "as of 2026-10-08" and
    Long-Term "as of 2026-08-18". VNQ is 100 Alternatives, "100 percent in its classified asset class".
- **Independent check 1, allocation:** AGG 270 of the 1,000 filed against SPY 430 + IWM 130 + EFA 170 gives 27 / 73. That is exact.
- **Independent check 2, the ETF line:** I recomputed VNQ's total return from Yahoo adjusted closes to 2026-10-20 myself.
  - 1M: 0.1833 against 0.1962 printed.
  - 3M: -6.4331 against -6.4211.
  - YTD: 7.2489 against 7.2702.
  - 1Y: 3.9966 against 4.0124.
  - The largest gap is 0.021 points, in line with the stated price-source difference (estate tier, then Yahoo).
- **The chart's strokes**, read from the PDF drawing list: Opal Long-Term is drawn in `#0A1733` and Vanguard Real Estate ETF in `#000000`,
  both 1.65 pt. Their contrast ratio is 1.18:1. In the rendered chart and in the legend, those two lines cannot be told apart by eye.

## Grade

**FWD-10 judgment criterion (ACCEPT) MET, on the 7K PDF (ADJUDICATION_v30) and the 7M PDF.** From pages 59 and 60, a person can say
whether the portfolio beat each comparable, and with how much risk, without opening YCharts. In run 7M:
- **Returns:** the portfolio beat both models and VNQ over YTD and 1Y. VNQ led only over 1M.
- **Risk:** VNQ carries the highest std dev and drawdown. The portfolio sits between Long-Term and VNQ.
- **Vendor names:** none appear.

**FWD-10 REALIZED.** v30 named one gap: the approved DONE WHEN's "two Opal models and one ETF". Run 7M closes it on the live product
(r34t, ticket TCK-20261021-09410391, filed through the PROD Ticket Center): two Opal models plus a typed ETF, with every block of the DONE
WHEN present for all four lines. v30's as-of note is also closed, because each model now prints its own date.

**Stated limits (none blocks the grade):**
1. **Two chart lines are indistinguishable** (Long-Term and VNQ, 1.18:1). The question FWD-10 asks is answered by the tables beside the
   chart, so the grade stands. The chart's own job, telling the lines apart over the window, is half-done for those two lines.
   - **Enrichment item for the CTO:** a distinct series color per line, with a distinguishability floor between any two series.
2. The "left out of all figures" line is not exercised on a Multi-Comp. The packet says so, and run 7N reads it live on the Overview.
3. The portfolio and model risk rows were not recomputed on 7M. They reproduced on 7K, and r34t did not change that code (issuer's read).

## L10 slug: WITHHELD

The packet asks for the slug. The precondition is not met at 15:04Z:
- **`.tools/round-close-check.py --project IRPT_ANLREQ --round 60`:** verdict=REFUSED.
  - 136 orders, 84 complete.
  - 41 orders are not complete. They include `TO-RUN-FWD10-MULTICOMP-7M` itself, `TO-AR-g-175` and the TO-APPLY-R34F..R34T
    series.
  - proof_bad=9, among them TO-AR-g-183, TO-AR-g-186, TO-APPLY-R34D, R34I, R34J and R34K.
- **`comp-surprise --armed --project IRPT_ANLREQ`:** 57 ARMED items, with one BLOCKING: `IRPT_ANLREQ-D2-W369-S1`, owner
  `2.0.0_SA_COO~Y2`. Also armed: the synthetic-object rows D2-S254, S255 and S257 from runs 7K, 7L and 7M.

The slug goes when the round's orders are terminal and those rows are dispositioned. The FWD-10 grade above does not wait on it.

```json
[
  {
    "id": "IRPT_ANLREQ-D2-C-S10",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-21T15:10Z",
    "one_line": "FWD-10 on runs 7K+7M: the judgment (ACCEPT) is MET and FWD-10 is REALIZED (two Opal models plus typed ETF VNQ live on r34t; VNQ returns recomputed within 0.021 pt); the chart draws Long-Term (#0A1733) and VNQ (#000000) at 1.18:1 contrast, indistinguishable; L10 slug withheld on round-close REFUSED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FWD-10 DONE WHEN (PRD v0.28): one Multi-Comp on the live product with two Opal models and one ETF, chart over one common window, periodic returns, risk figures and allocation side by side; ACCEPT: a reader can tell whether the portfolio beat each comparable and with how much risk.",
    "world_is": "Run 7M PDF (sha256 db369fa6f8c5, 60 pages): window, four-line chart and legend, returns, six risk figures and allocation for portfolio, Opal Short-Term (as of 2026-10-08), Opal Long-Term (as of 2026-08-18) and Vanguard Real Estate ETF (100 Alternatives); chart strokes Long-Term #0A1733 and VNQ #000000 (contrast 1.18:1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/L8_PACKET_FWD10_RUN7M_20261021.md blob 9cfe560b26f5 @8ff470b3ff",
        "C:/dev/andrew_samples/Opal_MultiComp_sample_FWD10_7M.pdf pages 59-60 (rendered, text-extracted and drawing list read by this seat; not committed)",
        "org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/adjudications/ADJUDICATION_v30.md",
        "org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md FWD-10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row; the chart color item goes to the CTO's enrichment list."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`

## Re-read at 16:35Z (msg 20261021T163307Z from `2.0.0_SA_COO~G2`): round-close MAY-CLOSE; slug still WITHHELD on 14 BLOCKING ARMED rows

- **`.tools/round-close-check.py --project IRPT_ANLREQ --round 60`, re-run by this seat at HEAD 8c5c176502 (bf02d9ca13 is an
  ancestor):** 138 orders, 116 complete, 0 outside the verdict, proof_bad 0, judgment 2 of 2 graded. Verdict MAY-CLOSE. That
  limb is met.
- **`comp-surprise --armed --project IRPT_ANLREQ`:** 58 ARMED, 14 of them BLOCKING, all UNDER_INVESTIGATION. Rule 27 L10 says
  every BLOCKING or ARMED row is dispositioned before the slug, and a disarm comes from the row's owner (section 2).
- **The 14 rows, by disarm owner:**
  - `2.0.0_SA_COO~Y2`: W62-S5, W166-S1, W297-S1, W306-S1, W309-S2, W313-S1, W369-S1.
    - W297-S1 and W306-S1 are r34l build refusals that r34t, now live, may have overtaken.
  - `2.0.0_SA_COO~G2`: S29 (the packager's attach ports were stubs; runs 7K and 7M read packager ATTACHED).
  - `2.0.0_SA_COO~T2`: W225-S1.
  - `2.0.0_SA_COO~P2` with `~Y2`: W55-S5.
  - `1.0.0_SA_CTO`: W55-S25, W92-S2, W155-S3, W285-S1.
- **The path:** each owner sends a disarm or dismissal request naming the read that shows the hazard is gone, as in v28 and v29.
  This seat reads each one and dispositions it. The slug follows the last one. Several rows look overtaken by later releases, but
  this seat does not disarm on that look alone.
