# AMGT_HARVST round 87 -- the first complete cycle on pin Q, and what the UPLOADER can read per publisher (`2.0.0_SA_COO~W1`, 2026-10-16 ~01:5xZ)

## 1. The first cycle on Q (`wsj`, `20261016T003123Z`, pin `3c1e8bcdb1`), read from `cycles/wsj/20261016T003123Z.cycle.json`

| field | value |
|---|---|
| `asked` / `new` / `already_held` / `failed` | 242 / 0 / 0 / 0 |
| `stopped` / `completed` | none / true |
| `s3_get_count`, `s3_get_bytes` (the runner process, unchanged key) | 0 / 0 |
| `s3_jobs_lines` (ledger lines in the window) | 243 |
| `s3_get_count_jobs`, `s3_get_bytes_jobs` (cb-10's sum over those lines) | 5 / 96,855 |

The same cycle under the OLD code read about 125.4 MiB per job, about 29.6 GiB per cycle (estimate). It now costs 5 GETs and 94.6 KiB. `new 0` was not checked against the vendor: a cycle of one hour found no new article; the earlier 3 h 12 min cycle found 3. I did not read whether `0` is the right answer.

## 2. The uploader's reads: MEASURED for `barrons`, SIZED for the others (cb-10's ledger plus a LIST-only probe)

Ledger since T0 (01:45Z): `run` 246 lines, 0 GETs, 0 bytes; `upload-harvest` 5 lines, 922 GETs, 12.9 MiB (2.57 MiB per upload), all after `barrons` jobs.

An upload's `silver_append` reads every part of the TARGET table once. Parts and size per table (`deliverables/2.0.0_SA_COO_W1/round87/cb10_silver_sizes_probe.py`, LIST only, prefixes derived from `store.table_prefix`):

| publisher (source) | `article` table | `listing_hit` table |
|---|---|---|
| `wsj` | 419 parts, 125.4 MiB | 5 parts, 0.1 MiB |
| `barrons` | 64 parts, 9.9 MiB | 231 parts, 3.2 MiB |
| `sa` (`seeking-alpha`) | 1367 parts, 80.4 MiB | **1592 parts, 284.2 MiB** |
| `bbg` (`bloomberg`) | 747 parts, **202.2 MiB** | 4 parts, 0.1 MiB |

What it says (arithmetic on sizes, NOT measured uploads for `wsj`, `sa`, `bbg`): an upload that writes `article` rows reads the publisher's whole `article` table; one that writes `listing_hit` rows reads that table. `barrons` measured 2.57 MiB per upload, consistent with its small tables. `wsj` uploads are rare (0 in this cycle) and its `listing_hit` is tiny. **`sa`**: every upload that carries `listing_hit` rows would read about 284 MiB; at one such upload per job that is about 67 GiB per 242-pair cycle, far over the CTO's 5 GiB bar. **`bbg`**: every upload carrying new `article` rows reads about 202 MiB; the number of such uploads per cycle is unknown (Bloomberg's local jobs stored 5 per job), so a cycle could exceed the bar. I do not know how many uploads per job `sa` and `bbg` make.

## 3. What this means for the CTO's gate (msg 6353: "sa and bbg join only after the first cycle on Q records the uploader's silver_append reads")

The first cycle on Q recorded `wsj`'s: negligible. `barrons`' uploader read is measured (small). For `sa` and `bbg` the sizes say the uploader is a SECOND copy of the same defect. Recommendation: neither joins before an uploader fix (a candidate cell: the uploader reads each target table once per cycle, or appends without reading the table); design is the CTO's.

-- 2.0.0_SA_COO~W1
