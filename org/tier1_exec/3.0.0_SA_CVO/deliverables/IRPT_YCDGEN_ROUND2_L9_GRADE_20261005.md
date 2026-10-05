# IRPT_YCDGEN round 2 -- L9 grade (3.0.0_SA_CVO, 2026-10-05 ~00:2xZ)

Input: drain-end packet `deliverables/2.0.0_SA_COO~Y/round2/DRAIN_END_PACKET.md` @fda2a4e8c7. The channel compile is
ADJUDICATION_v2 + REMEDIATION_v2 (drafts beside this file): 1 row dismissed (S2), 3 graduated OPEN (S3, W3-S2, W3-S3),
round label v3, 0 ARMED. Reads at CLOUD HEAD a2a65ff7cc; read-only AWS as user/Andrew_Berman; no YCharts call. No figure
value, client name or account number appears below.

## YCD-m-2.AC4 (the m-1.AC2 re-grade) -- PASS

"Every number, table and chart on the source Overview PDF is listed as an element." Source: the retained Overview,
VersionId 6Atpxe.MTB04QljV8tH9nItsdSxFZkop, 582,765 bytes, 23 pages, read in memory only (census_r2.py,
raw_drawings.py, grey_big.py, number_match.py). Map: `deliverables/maps/overview_map.json` at HEAD, 253 elements
(158 number, 22 table, 17 chart, 56 text), 12 calls; against round 1: +4 elements, 0 removed, 0 renumbered, only
p13.e04 and p14.e03 changed (their notes).

| kind | on the PDF | in the map |
|---|---|---|
| labelled numbers | 158 (p2 14, p3 19, p4 62, p5 28, p6 16, p8 19) | 158, matched by label |
| tables | 14 physical: p2 x2, p6, p7 x2, p9 x2, p10, p11, p12, p13 x2, p14 x2 (round 1's record said 15 over the same list) | 22, all: the map splits Risk Info into 7 rows, Risk/Reward into 2, and p12 into its portfolio row and its holding rows |
| charts | 17: 13 embedded images (p2 x4, p3, p5, p6 x2, p7 x2, p8, p9 x2) + 4 vector-drawn | 17 |
| vector-drawn charts | p3 9-segment stacked bar under Stock Style Exposure; p3 single bar over the Market Classification legend; p3 single bar over the Region legend; p5 one bar per sector row (14 rows) | p3.e24 Stock Style Exposure chart, p3.e25 Market Classification chart, p3.e26 Region chart, p5.e34 Stock Sector Exposure chart: page 3/3/3/5, kind chart, label the printed title, source the same call and calc ids as the sibling number elements, claim inferred |

- p14.e03 now lists six columns (Name, Inception Date, Type, Rebalance Frequency, Start, As Of), as printed.
- p13.e04 has its wrapped header word "Prosp" back, as printed.
- Nothing else unlisted: every other non-white vector drawing in the body is a legend dot, a hairline table rule, a
  full-width grey section band, a grey row stripe (p7 Risk Info), a text bullet (p14) or a link underline (p22); no
  grey or stroked chart exists. p4 (Expanded Region Exposure) carries 3 legend dots and no chart. Pages 15-23 carry
  boilerplate prose only (covered by text elements, as in round 1).

## YCD-c-2.AC3 (C-FIRM) -- PASS

"No figure value from a client file or vendor answer is in either file." PRD C-FIRM: git holds no client figure; the map
family carries element ids, verdicts and reasons. Files: `overview_coverage.json` and `coverage_probe_map.json` at HEAD.

- 705 numeric tokens checked (0 decimals), intersected in memory with the PDF's 332 distinct numeric tokens and with the
  kept answers the files point to (run YCD-R1-20261004T1944Z, 6 objects) plus, as a wider net, the round-2 close runs
  that executed the probe map (YCD-R2-20261004T2315Z-A/-B, 4 objects). Controls: a planted PDF token and a planted
  kept-answer value both match; a nonsense token does not.
- 619 tokens match; every one is structural: 282 element-id digits, 142 formula constants ("1" in "sums to 1" and
  "1 / sum"), 121 window or bucket digits inside calc/metric/column ids, 28 step numbers, 28 JSONPath indices, 9 run
  numbers ("run 3"), 3 HTTP statuses, 2 schema versions, 2 run/round labels, 1 page count, 1 artifact-hash fragment.
- Figure values found: 0. Paths with matches: `$/elements[*]/id`, `.../reason`, `.../via/{columns,element_columns,
  statistic_columns,metric_ids_evidenced,field,benchmark_field,inception_field,weighting,aggregation}`, `$/run`,
  `$/basis`, `$/schema`; probe map `$/calls[*]/params/{metrics,xAxisMetric}`, `$/schema`, `$/source_pdf/{pages,
  artifact_prefix}`.

## Outcomes (evidence for the slug)

| FWD | evidence at this read |
|---|---|
| 1 | Still Andrew's act: the fresh signed link to the run-3 report was printed to him at ~22:1xZ (packet section 2); his opening it is not on record. NOT REALIZED until he opens it |
| 2 | Run A (`--bootstrap-index`) reads no_previous for both calls; run B reads false for both against run A (run.json of each, read). The true arm (a changed answer) is pinned only by r-2's tests, not by a live run |
| 3 | Both OTHER_ENDPOINT probe routes answer 200 for a model portfolio in both runs (scatter POST with the documented metric ids, 200 with data.series; general_data xAxis=metrics, 200 DATA); round 1's scatter ids answered 400. The Overview map is now complete (m-2.AC4 PASS); the 4 new chart elements are not yet in the coverage table |

Defect carried with no row: the keeper labels the scatter answer IDENTIFIERS although it carries `data.series`
(C-KEEP's shape rule does not know that key; packet section 3).

-- 3.0.0_SA_CVO (reads by a read-only delegate of this seat)
