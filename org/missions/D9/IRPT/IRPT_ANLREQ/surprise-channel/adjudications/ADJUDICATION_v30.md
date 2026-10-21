# IRPT_ANLREQ: CVO adjudication, FWD-10 (Core) on run 7K -- judgment MET; FWD-10 NOT REALIZED (no live ETF comparable)

<sweep_watermark>2026-10-21T09:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-21T09:45Z, a seat that did none of this work. Input:
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/L8_PACKET_FWD10_RUN7K_20261021.md`, blob 9e00bb9bd186 (msg 11971; verified by
`git hash-object`).

## What this seat read itself

- **The served PDF** `C:/dev/andrew_samples/Opal_MultiComp_sample_FWD10.pdf`: 306,057 bytes, sha256 `2fc0ad5f87268a34...`, which equals the
  packet; 60 pages. Pages 59 and 60 were rendered and read as an image, and their text was extracted.
  - **Page 59:**
    - the common window, "2024-04-30 to 2026-10-19 (2.4 years)", with its rule (the latest first observation to the earliest last;
      every line rebased to 100);
    - the cumulative-return chart of the three lines (max 146.8693);
    - periodic total returns: Your portfolio 1Y 11.4675, Opal Short-Term 1.6192, Opal Long-Term 9.7409, with 3Y, 5Y and 10Y n/a and the
      words "because the common window is shorter than those periods";
    - risk: std dev, Sharpe, Sortino, max drawdown, alpha and beta for all three lines, under the stated references "Alpha and beta are
      measured against SPY ... Sharpe, Sortino and alpha use BIL".
  - **Page 60:** asset allocation side by side, with the portfolio at 24 / 76 / 0 by accepted holdings and each model by its positioning.
- **One independent check:** the portfolio's allocation, 24 / 76 / 0, is AGG's 240 of the 1,000 filed against 460 + 150 + 150 in equity
  ETFs. That is exact.
- **The issuer's figure-by-figure recomputation** (`FWD10_READ_RUN7K_20261021.md`, commit b114d42728): the models are exact, and the
  portfolio is within 0.0012 points. I accept it: it is the issuer's read, not a worker's self-grade, and its conventions were checked on
  the models first.

## Grade

**FWD-10 judgment criterion (ACCEPT) MET.** A person reading pages 59 and 60 can answer "did this portfolio beat each model I picked,
and with how much risk" without opening YCharts:
- the portfolio beat Opal Short-Term and Opal Long-Term over YTD and 1Y on the same window;
- the risk is read beside it on a stated reference, with a higher std dev and drawdown than Long-Term;
- no vendor name appears anywhere.

**FWD-10 NOT REALIZED.** The DONE WHEN Andrew approved "as written" (2026-10-20) names "one Multi-Comp ... (two Opal models and one
ETF)". The live comparison catalogue holds the five Opal models only, so no ETF comparable was exercised on the live product. The ETF path
is proved offline only (`ar_compare_checks.py`). It realizes with one live Multi-Comp that carries an ETF comparable. The other choice is
an ENDPOINT addendum, which would need Andrew's word, since he approved the ETF in the text.

**Notes for the CTO (not conditions of the judgment):**
1. **"Model positioning as of 2026-10-19" misstates the date.**
   - Page 60 prints that date, the positioning file's `data_as_of`, for both models. The file's per-model dates are 2026-10-08 (Short-Term)
     and 2026-08-18 (Long-Term), as the packet itself states in section 4.
   - A reader is told the Long-Term weights are two months fresher than they are, which is a claim the value does not carry.
   - Each model row should carry its own as-of date.
2. **The portfolio's own 3Y, 5Y and 10Y returns read n/a.**
   - Correctly so on this page's rule: the portfolio is bought at the common window start, AR-g-185's fix of run 7J's drift.
   - If Andrew wants the portfolio's own longer periods as a hypothetical held basket, that is a FWD-11 (standardized returns) item, not
     a defect of FWD-10.

```json
[
  {
    "id": "IRPT_ANLREQ-D2-C-S9",
    "project": "IRPT_ANLREQ",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-21T09:45Z",
    "one_line": "FWD-10 on run 7K: the judgment (ACCEPT) is MET on PDF pages 59-60; FWD-10 is NOT REALIZED because the approved DONE WHEN names one ETF comparable and the live catalogue has none; page 60's single 'as of 2026-10-19' misdates both models' positioning.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FWD-10 DONE WHEN (PRD v0.28, approved as written by Andrew 2026-10-20): one Multi-Comp on the live product with two Opal models and one ETF; ACCEPT: a reader can tell whether the portfolio beat each comparable and with how much risk.",
    "world_is": "Run 7K PDF (sha256 2fc0ad5f8726, 60 pages): window, chart, periodic returns, a six-figure risk table on stated references (SPY, BIL) and allocation for the portfolio and two Opal models; no ETF comparable (the catalogue holds five Opal models); page 60 prints 'Model positioning as of 2026-10-19' while the per-model dates are 2026-10-08 and 2026-08-18.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/L8_PACKET_FWD10_RUN7K_20261021.md blob 9e00bb9bd186 (msg 11971)",
        "C:/dev/andrew_samples/Opal_MultiComp_sample_FWD10.pdf pages 59-60 (rendered and text-extracted by this seat; not committed)",
        "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/FWD10_READ_RUN7K_20261021.md",
        "org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md FWD-10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row; FWD-10's ETF leg and the per-model as-of date go to the CTO's analysis."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
