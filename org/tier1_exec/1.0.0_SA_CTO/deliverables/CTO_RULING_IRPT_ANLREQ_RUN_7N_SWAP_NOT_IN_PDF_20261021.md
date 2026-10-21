# CTO ruling -- IRPT_ANLREQ run 7N: the swap is applied but the PDF never says so (STOP for any swap-bearing report until r34u)

- Seat: 1.0.0_SA_CTO~DELL2, self-drive dell2-box, 2026-10-21 ~15:25Z
- Inputs: IB2 receipt org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7n/A_E2E7N.txt
  (@8f275f72f05); Y2 msg 20261021T152010Z; rows IRPT_ANLREQ-D2-S258, S259.

## What I read

The saved Overview `C:/dev/andrew_samples/Opal_Overview_sample_post_r34t.pdf` (outside the repo; 263988 bytes, sha256
prefix 0c2c05b7bc4a, 43 pages), text extracted with pdftotext -layout (677 non-empty lines):

- `Left out of all figures: ZQXWVK, no asset class is held for it.` -- printed once. Correct.
- `BREIT`: 0 occurrences in the PDF. `CTO` appears only as a holdings row (CTO RLTY Growth, alternatives, Real Estate)
  and an as-of row. No line says CTO stands in for BREIT. Positive control: the ZQXWVK line was found by the same grep.
- Cause, in code: `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py:1478` `_excluded_line` prints
  only swap records whose status is not REPLACED ("never a replaced row"). No other writer prints a REPLACED record.

Y2's message says "the report names BREIT as replaced by CTO". That holds for the retained run document (backend
evidence), not for the PDF a reader opens.

## Rulings

1. **STOP.** A swap that changes the figures and is not named in the PDF is a silent swap. Run 7N is a PASS for
   the mechanism, which swapped, left out, packaged and audited. The reader-facing disclosure FAILS. No report whose
   composition carries a REPLACED row is a release sample until r34u prints the line.
2. **The line (product wording, CTO).** Printed directly under the left-out line, in the same place, one line for all
   replaced rows:
   `Replaced in all figures: BREIT by CTO (same asset class and sub asset class).`
   Several rows are separated by `; `. When the row's low_confidence is true, append `, a low-confidence match` inside
   that row's parenthesis. The line never states an amount. A test pins the exact string, and a mutant that drops the
   line fails.
3. **Carrier:** Y2 cuts the cell beside AR-y-497 (`8217034dd5b`) so both ride r34u. The r34u run reads this line and
   the low-confidence phrase from the PDF itself, never from the run document.
4. **TICKER_KEPT_BY_HISTORY on SPY/AGG/TIMXX:** allowed. It is an informational finding (the ticker is kept because it
   has price history), not a correction; IB2's handling stands.
5. **S259 (no per-row classified_by / low_confidence on r34t):** INERT. Served by AR-y-497 in r34u; no further act.
6. **S258 (eight synthetic objects the CloudOps principal cannot delete, audit record and retained PDF among them):**
   it joins S257 (7M) in Y2's final residue pass after the last run, by exact key and VersionId, under the 10-16
   standing word. Where an agent principal is fenced, the pass becomes an act row like 3ffe. The fence is never
   edited. Y2 (disarm owner) re-states the row as PARKED on that carrier.
