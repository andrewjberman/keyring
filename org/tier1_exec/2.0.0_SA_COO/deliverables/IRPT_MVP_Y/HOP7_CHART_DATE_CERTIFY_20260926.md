# Hop 7: a real vendor PDF is refused at certification -- found offline, fixed, and proved

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~20:5xZ. This is a closer-drive item on Y's surface (`ycharts/`). The limit noted in
`HOPS_5_7_PREFLIGHT_20260926.md` said how a real Overview certifies would be "first seen live"; this measures it first.

## Finding

The deployed resident package `f624e8a72f`, plus the lane fix, runs window 3's real composition. The vendor is replayed,
but the download is the **retained real Overview PDF**, with the **pinned production census**. It ends:
- `PublicationRefused CHART_DATE_CERTIFICATION_FAILED`;
- the job is left in **CERTIFYING**, with 0 REPORT# rows;
- the vendor PDF and the extraction evidence are already retained.

The real Overview PDF is `opal-data-ycharts` `research/20260911/.../irpt-variants-20260911-overview/report.pdf`. Its
sha256 is `abab2ffe..`, equal to `pdf_validation.json`. The census sha256 is `44853788..`.

Cause:
- `publication._chart` represents a chart by its whole page, with bbox `[0, 0, W, H]`, so the value's top is 0.0.
- When the page prints exactly one "Data as of" date, the chart claims `SECTION`.
- `certify._grade_date` then requires that line to sit above the value, which is impossible at top 0.0, so the row
  grades `DATE_TAKEN_FROM_A_NEIGHBOURING_BLOCK`.

Every retained real variant hits it, on the 5-year risk/reward scatter page:

| Real PDF | Deployed certify | Fixed certify |
|---|---|---|
| overview | REFUSED (p8; scalars 61/61, charts 4/5) | PUBLISHED |
| comparison | REFUSED (p11; scalars 81/81, charts 3/4) | PUBLISHED |
| multicomp | REFUSED (p12; scalars 108/108, charts 1/2) | PUBLISHED |

Instrument: `live_walk/certify_real_pdf.py`, which runs the package's own extract and publication code and prints each
failing row.

## Fix (`P_HOP7_CHART_DATE_CERTIFY_20260926.patch`; Y branch `74b4368bef`)

For a `source_chart_representation`, a SECTION date holds when **every** "Data as of" date its page prints is the row's
date. Any other date on the page is refused `FAIL_DATE_NEIGHBOUR`, including one printed beside it on the same text row.
Scalar rows are unchanged.

The patch applies cleanly (apply-check rc=0) to CLOUD and to P's tree `irpt-p-publish-20260923` @c8a08e31d1. Both
carry certify.py sha256 `f1516e24..`, equal to the deployed file.

## Proof

- **Real run:** the resident with the fix goes from CERTIFYING (refused) to **READY**, `handled=1`, 1 REPORT# row,
  checkpoint_publication set.
- `tests/test_publication.py`: 18/18 pass in a full-layout mirror. The 3 new tests fail on the deployed certify.py.
- `run_offline_suite.py` output is byte-identical before and after.

## What ships

- `ycharts/extract/certify.py` in the **resident package**, which is hop 7's path.
- `irpt-ycharts-generate` also packages the file: `lambda-source-map.json` `staged_from` row 66, sha256 `f1516e24..`.

## Limits

- The three PDFs are the 2026-09-11 variants of a synthetic portfolio, not AAPL/VNQ.
- The live Overview may print other pages differently. This shows only that the scatter page's layout, which all three
  variants share, is refused today.

## Hops 8-9 on the real report (21:2xZ)

The served `irpt-status` `bMMJ/bQ+5`, with no overlay, answers all 4 Opal reads on the fixed resident's READY world
(`status_read_proof.py --state <real-PDF dump>`): 27/27 modules from the extract, 32 reads, 0 writes.

The published report is 35,886 bytes, with `extraction_coverage` PARTIAL:
- 57 sections: 52 dated scalar rows plus 5 charts;
- 44 of 60 disclosures emitted;
- 9 unit-conflict rows withheld, and 30 records unlocated;
- dates: 2026-08-31 (45), 2026-09-09 (7) and 2026-09-11 (5); claims: SECTION 52, REPORT 5.

What an Overview of these holdings would show in the tab is this report's shape: PARTIAL, with its gaps named.
