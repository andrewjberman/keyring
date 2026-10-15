# MDPF_SECHIST-D1-S7 -- the 2026-10-15 Bloomberg pull landed late; FXFXX 2026-10-12 was requested and came back filled

Filed by 2.0.0_SA_COO~H1 (issuer; owner of the row), 2026-10-15 ~14:4xZ. Row: `org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md`
(D1-S7, @01c5f72d02). Read only; no write to any served key. The CVO writes the disposition at the compile; this is evidence, not a disposition.

## Measured at 14:4xZ

| item | value | instrument |
|---|---|---|
| manifest | `s3://opal-data-etfs/bbg/2026-10-14/run_manifest.json` EXISTS, LastModified 2026-10-15T14:33:58Z (404 on every read from 03:45Z to 13:45Z; usual landing ~11:07Z, so about 3h27m late) | head-object; control: the 10-13 key, LastModified 2026-10-14T11:07:05Z |
| as_of / class / health | `as_of` 2026-10-14, `run_class` scheduled, `generated_utc` 2026-10-15T14:33:57Z, `objects_failed` [], `history_backfill_error` null | manifest fields |
| gap re-request | `history_gap_fill`: record_as_of 2026-10-13, listed_tickers 2, requested QXO 2 ranges (8 rows) and **FXFXX 2026-10-12 to 2026-10-12, 1 row**, deferred [], error null, rows 9 | manifest field |
| the fill | `bbg/2026-10-14/history_topup.parquet` carries FXFXX on 2026-10-12 = **0.0000** (non-null) beside FXFXX 2026-10-14 = 0.0105 and SALXX 2026-10-14 = 0.0098 | parquet read |

## What it means (issuer reading, not a ruling)

- The organic blank-then-fill pair FWD-9 asked for now has both halves in the INPUT: bbg/2026-10-12 left FXFXX null on 2026-10-12 (blank served 2026-10-14 and 2026-10-15), and the next
  pull (this one) requested that day from the gap record and the vendor returned a value. The value is exactly 0.0000, a day the bond market was closed (Columbus Day); the vendor
  reported it as a reading, not a null. Whether 0.0 is the right figure for a closed day is not judged here; C-MMF says a returned value is used and a null is blank.
- The SERVED half is not yet observable: the served page is rewritten by the next scheduled gold, 2026-10-16 13:00Z, which should serve `data_as_of` 2026-10-14 and FXFXX
  windows that include 2026-10-12 (WTD and longer non-null). `R5_CHECKS/r5_fwd9_read.py filled 2026-10-12` reads exactly that. It is read after that run, together with the first served-week read.
- Row D1-S7's disarm condition ("the first scheduled manifest for as_of 2026-10-14 lands") is met. The cause of the lateness was not read.
