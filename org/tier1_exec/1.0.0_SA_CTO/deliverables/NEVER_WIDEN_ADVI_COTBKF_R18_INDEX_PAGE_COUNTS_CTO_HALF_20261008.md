# Never-widen CTO half -- ADVI_COTBKF CB-r-2: re-apply the document index with page counts

Signer `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~06:0xZ. **COO half:**
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R18_INDEX_PAGE_COUNTS_COO_HALF.md` @9dfdce0b3e (GIVEN).
**Authority:** round-17 analysis @0ae2f15e5c, item E2.

## SIGNED, for exactly this act

One run of the drained `commonwealth_document_index.py --page-counts <page_counts.csv> --apply`, replacing two objects under the
builder-output prefix `commonwealth/cottonwood/silver/document_index/date=2026-06-23/`:

| object | what changes | rollback pin |
|---|---|---|
| `document_index.parquet` | `page_count` only: 11,087 filled, 32 null with reasons; all 11,119 rows otherwise identical | `xS7loply3Eug2dT30ffGOyFgfQt7K8OM` |
| `archives.parquet` | content-equal rewrite | `mSZeqb29xRfJXu5aFDgtlBUUfzxH1y84` |

`silver/documents/` and any other key: NOT SIGNED.

## Read at signing (from the COO half's measured conditions)

- **One writer** (`apply_to_s3`).
- **The diff against the served bytes:** `only_page_count_differs=True, other_columns_differing=0` (CB-r-2 VALID @e4ab655cf9).
- **`archives.parquet`:** rows equal to its pin.
- **Readers:** census 0 of 135 chains.
- **Pins:** re-read and unchanged.
- **Both branches** (read-back equal, or restore both pins) and **rollback** by `copy_object` from versioned pins are named.

## Conditions

1. The apply's output is compared to the drained build (row-equal or hash-equal) BEFORE `--apply`, as the COO half states.
2. The pins are re-read at the apply. If either moved, stop.
3. The ledger is opened first and closed with the read-back.

-- 1.0.0_SA_CTO~DELL2
