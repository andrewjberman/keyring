# IRPT_YCDGEN round 1 -- L9 grade (3.0.0_SA_CVO, 2026-10-04 ~21:2xZ)

Asked by `2.0.0_SA_COO~Y` msg 104965 (drain-end packet `deliverables/2.0.0_SA_COO~Y/round1/DRAIN_END_PACKET.md` @70a35ee9dc). The
channel compile is ADJUDICATION_v1 + REMEDIATION_v1 (this commit): 3 rows dismissed, 2 graduated (S1 REMEDIATED and closed,
disarmed by ~Y at 19:22:34Z; W2-S3 OPEN); new row S3 (the step-7 firewall stops filed no row).

## The judgment criterion: YCD-m-1.AC2 -- FAIL

"Every number, table and chart on the source Overview PDF is listed as an element." Source:
`s3://opal-data-irpt/irpt/cottonwood/state/vendor_documents/ART-ac668d3b.../6e75336144a4....pdf` (VersionId 6Atpxe.MTB04..., 23
pages; equal to the map's `source_pdf`). Map: `deliverables/maps/overview_map.json`, 249 elements (158 number, 22 table, 13
chart, 56 text). Read by a delegate of this seat in memory only, with digits masked in any render; no figure leaves the store.

| kind | on the PDF | in the map |
|---|---|---|
| labelled numbers | 158 | 158, matched by label |
| tables | 15 (22 in the map's split of Risk Info) | all |
| charts | 17: 13 embedded images + 4 drawn as vector shapes | 13 (the images only) |
| dates and as-of stamps | 26 | all, as text |

Unlisted: p3 Stock Style Exposure (a 9-segment stacked bar), p3 Market Classification bar, p3 Region bar, p5 Stock Sector
Exposure (one bar per sector row). The map counted embedded images as charts and missed drawn shapes. Smaller gaps:
p14.e03 lists 2 of 6 printed columns (the others are words); p13.e04 dropped a wrapped header word.

## Outcomes

| FWD | verdict | reason |
|---|---|---|
| 1 | NOT REALIZED | DONE WHEN "one live run, ending in Andrew opening the report": run 3 (YCD-R1-20261004T1944Z) asked live, kept 6 answers and built a 39-page report at its builder key; the 5 live values trace to step 02 and every other element carries a not-available line, so the ACCEPT's tracing holds. The signed link was printed to Andrew at ~20:4xZ; his opening it is not on record. It realizes on his open |
| 3 | NOT REALIZED | the Overview map misses 4 charts (AC2 FAIL above); Comparison and Multi have no map |
| 2, 4, 6 | NOT REALIZED (partial evidence) | 2: kept objects exist, but every call reads `no_previous` although run 2 kept the same calls; 4: Overview layout only; 6: run 3 carries the three clocks, no record of Andrew waiting |
| 5, 7 | not exercised | -- |

The measured finding of the round (packet section 3): 2 of the map's 12 calls answer with data for a P:-portfolio; 176
of 249 elements have no answer (row W2-S3, OPEN). The report is honest about it and thin.

-- 3.0.0_SA_CVO
