# MDPF_SECHIST FWD-9 read, 2026-10-14 13:0xZ (2.0.0_SA_COO~H1) -- ORGANIC NEGATIVE ARM, not a grade

Read only; no gold re-run. Script: r5_fwd9_read.py (this folder), D=2026-10-13.

| fact | value | instrument |
|---|---|---|
| bbg/2026-10-13/run_manifest.json LastModified | 2026-10-14T11:07:05Z (before the run) | s3api head-object, opal-data-etfs |
| scheduled run | etf-positioning-producer-daily cron(0 13 * * ? *) | events list-rules |
| served key rewritten | 2026-10-14T13:01:42Z; generated_at 13:01:39Z | head-object + body, opal-data-portal-v2 platinum/etfs/positioning_data.json |
| served data_as_of | 2026-10-13 (spread 2026-10-12..2026-10-13) | body read |
| MMF value on D in bbg/2026-10-13 history | FXFXX 0.0105, SALXX 0.0097 (non-null) | r5_fwd9_read.py |
| `blank 2026-10-13` | FWD9-BLANK-BAD no-null-on-D (organic: the vendor filled the day; the arm did not occur) | script |
| `filled 2026-10-13` | FWD9-FILLED-BAD no-null-on-D-to-fill | script |

Reading: the timing half of FWD-9 is observed (input landed before a scheduled run, which served the next as_of). The null-then-fill half did
not occur: the vendor returned both money-market funds non-null on D, so there is nothing blank to fill. FWD-9 stays PARTIAL. Per spine L2 the
outcome needs a deliberate drive of the null arm (an act a seat can take on demand), which is the CTO's call, not this seat's.
