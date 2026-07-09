# FINDING: the BD unrealized DataMining export appears to hit a hard 500,000-row cap

**Date:** 2026-07-09 | **Author:** 0.6.0_AE_PartnerETL | **Project:** ADVI_BDAPIMIG
**Status:** OPEN -- captured, not chased (CTO directive 20260709T090845Z)
**Class:** freshness-integrity / existence-proxy family (same class as the 49F frozen-AUA incident)
**Severity:** P1 candidate -- a silently TRUNCATED export passes every existence and freshness check.

## The observation

Surfaced while grounding the 49F frozen-AUA root cause. Two real `UNREALIZED_DAILY_*.xlsx`
exports from `s3://opal-data-bd/forwardfill_v2/unrealized/`, read from the sheet XML's
`<x:dimension ref="A1:O{last_row}">` attribute (exact, authoritative, O(1)):

| export | dimension last row | data rows | round number? |
|---|---|---|---|
| `UNREALIZED_DAILY_2026-07-02.xlsx` | `A1:O488578` | 488,577 | no |
| `UNREALIZED_DAILY_2026-07-08.xlsx` | `A1:O500001` | **500,000** | **exactly** |

A perfectly round 500,000 on one date and an arbitrary 488,577 on another is the signature of a
vendor-side export cap that the 07-08 pull HIT and the 07-02 pull did not. It is not proof, but it
is the strongest single indicator available without a vendor answer.

## Why it matters (and why it is the same class as the freeze)

A truncated export is **well-formed, large, recent, and non-empty**. It therefore:
- passes `download_export`'s transport check,
- passes the new `_export_has_data_rows` content guard (it *does* have data rows),
- passes `comp-freshness` (mtime is current),
- lands a plausible multi-MB silver partition.

Nothing anywhere in the chain asserts *completeness of the row set*. This is the existence-proxy
failure one level up: we moved from "does the object exist" to "does it have any rows", but not to
"does it have ALL the rows". The 49F freeze was the 0-row instance of this; truncation is the
partial instance, and it is harder to see because every dashboard reads green.

Downstream, `bd-silver-merge` deduplicates 07-08 from 500,000 raw rows to 103,490 unique rows
("Removed 396,510 duplicate rows"). So the *silver* impact of a cap is damped by the ~4.8x raw:unique
ratio -- a truncation of the raw tail may drop few or many unique lots depending on ordering. That
damping is exactly what would let this go unnoticed indefinitely.

## What is NOT yet established (do not over-read this finding)

- Whether 500,000 is a BD server-side cap, a DataMining export limit, or a coincidence.
- Whether the truncation actually dropped unique lots, or only duplicate rows.
- Whether other tables (transactions is the other large one, 86MB / ~500k-row class) also cap.

Note also a tooling trap encountered here: `openpyxl`'s `iter_rows()` on a `read_only` worksheet is
NOT trustworthy for row counts -- it reported 500,000 for one export and could not be reconciled
against the sheet's own `<dimension>`. Use the `dimension ref` attribute, or count namespaced
`<x:row` tags. This is why `cot_bronze_ingest._export_has_data_rows` does not use openpyxl.

## Suggested next steps (owner TBD -- routed to the CTO/CVO freshness-integrity program)

1. Pull `UNREALIZED_DAILY` for several consecutive dates and read each `<dimension>`. If 500,000
   recurs exactly, it is a cap, not a coincidence.
2. Probe the vendor directly: request a window known to exceed 500,000 rows and see whether the
   export stops at exactly 500,000.
3. If confirmed: the pull must either paginate/partition the unrealized query (e.g. by account
   range or sub-window) or FAIL LOUD when `row_count == cap`, on the same principle as the empty
   guard -- a boundary-exact row count is a completeness signal, not a coincidence to be landed.
4. Check `transactions` (the other >500k-row-class table) for the same boundary.

## Grounding

- `s3://opal-data-bd/forwardfill_v2/unrealized/UNREALIZED_DAILY_2026-07-0{2,8}.xlsx`,
  `xl/worksheets/sheet.xml`, `<x:dimension ref>` read directly from the zip entry.
- `bd-silver-merge` CW log 2026/07/09, stream `[$LATEST]66ba57eee70a4adcbaee00a2c30eabb7`:
  "Removed 396,510 duplicate rows" / "OK: UNREALIZED_DAILY_2026-07-08.xlsx ->
  silver/unrealized/2026-07-08.parquet (103490 rows, 17 cols)".
- Parent incident + the master principle (bind to CONTENT, never the existence proxy):
  commit `9d44d6af5`, deploy ledger `20260709T0855Z_bd-49f-empty-stub-asof-lag-root-fix`.
