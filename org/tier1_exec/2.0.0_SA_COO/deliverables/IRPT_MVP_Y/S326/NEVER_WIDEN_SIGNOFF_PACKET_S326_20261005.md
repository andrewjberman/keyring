# Never-widen sign-off packet -- S326: irpt-status serves the request history newest first (read whole, bounded; the cursor contract unchanged)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-05 ~03:3xZ.

**Why:** row IRPT_BCKEND-S326 (`2.0.0_SA_COO~D`, msg 105095, BLOCKER).
- `ops/owned_requests.history` queried the firm's rows by sort key `analysis#REQ-<random hex>#1`, ascending, with `Limit`
  equal to the page size. Page 1 was therefore a random slice. The page time-sorts that slice, so it reads newest-first
  while omitting the newest. In ~D's Y-2 run, 22 list reads never showed REQ-c1b53772.
- **Measured live, read-only:** Cottonwood has 30 accepted requests, and REQ-c1b53772 is not on the old first page of 25.

**Ledger:** `irpt-s326-history-20261005` (U1 closes on this packet's artifact; D1 and V1 are open). **One move:** the
irpt-status code. No IAM, route, table, index, schema or contract changes.

## 1. What ships

**The code:** `44cc631396`, merged `80a79a7462`; the irpt-status row was repinned at `80a79a7462` (`c3de44f260`; no staged
bytes changed); artifact row `70f4ccad19`.

`ops/owned_requests.py`:
- **`_history_rows(firm)`** reads every accepted row of the firm.
  - It queries in pages of `HISTORY_SCAN_PAGE` (200).
  - Past `HISTORY_SCAN_CAP` (2000) rows it refuses `HISTORY_TOO_LARGE`; it never truncates.
  - It validates each key, as before, and each `accepted_at` (int).
  - It orders by **`accepted_at` descending, then key ascending**. Ties keep the old order, so both paired fixtures (here
    and the portal's) are unchanged.
- **`history()`** pages by position in that order.
  - The cursor is unchanged: `{tenant, owner, key}`, with key = the page's last row, owner-bound and validated as before.
  - A cursor whose row is gone refuses `INVALID_HISTORY_CURSOR`.
  - The owner and client screens run only on the page's rows, as before.

**The artifact (U1):**
- `irpt-status.zip`, version `Ji6C92YJzsOWQtvO0fJkTV2yYhqfE2bx`, 349,179 bytes, sha256
  `jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE=`.
- Built zip vs the pin's bundle: 49 members, 0 differ, 0 CRLF.
- **Census vs live `XPta1UMJ..`** (`CENSUS_S326_VS_LIVE_20261005.json`): identical 48, changed 1 (`owned_requests.py`),
  added 0, removed 0.
- **Cold-start smoke PASS** on the status, history and request-read routes (`ZIP_COLD_START_SMOKE_S326_20261005.txt`).

**Targeted plan** (`plan_s326_d1.txt`): `module.irpt_status.aws_lambda_function.this`, 0 to add, 1 to change, 0 to destroy.
Only `s3_object_version` `jVkDK9v6..` -> `Ji6C92YJ..` and `source_code_hash` `XPta1UMJ..` -> `jhGc2J4Q..` change.

## 2. Writers, readers, and the cost

- **The history order has one writer,** `history()`. Its reader is the history route (`GET .../analysis/requests`, ops
  `entry.py`). The page parses `{items, next_cursor}` unchanged.
- **The read cost changes,** and this is the one behaviour to sign for.
  - Before: one query of `limit` rows per page.
  - After: one query per 200 rows of the firm per page (Cottonwood 30 rows = 1 query), consistent reads, capped at 2000
    rows.
  - The per-row composition reads (the screens) stay page-bounded.

## 3. Blast radius

| reader | after |
|---|---|
| the page's request list | lists the firm's newest requests first, so Y-2 (REQ-c1b53772) is row 1 for Cottonwood |
| a page walking with `next_cursor` | every request exactly once, newest to oldest |
| a firm with more than 2000 accepted requests | refused `HISTORY_TOO_LARGE` (today: no firm near it) |
| status, request-read, sections and every other route | unchanged (`owned_requests.history` is the only code change) |

## 4. Proofs

- `ops/tests/test_owned_requests.py`, new tests:
  - newest-first across pages whatever the key order;
  - every scan page read, and the cap refusal;
  - a gone cursor row;
  - the bounded-page test now pins the scan page size.
- `ops` suite 248 passed, 22 skipped; `_contracts` 185 passed (the paired fixture is unchanged).
- **Offline on live rows:** the new order lists REQ-c1b53772 first, then REQ-0d97252f (Y-4), then REQ-a618aa83 (Y-5).
  **Negative control:** the old first page omits REQ-c1b53772.

## 5. Rollback, per key

Re-promote S3 version `jVkDK9v6qfVw12iBAWcSbGgO9paauYtD` (`XPta1UMJ..`, live now) with one targeted safe-apply. Read back
CodeSha256 `XPta1UMJ..`.

## 6. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read, STOP on any difference:** irpt-status CodeSha256 is `XPta1UMJ..`.
3. **D1:** a fresh targeted plan (1 to change, code only); ONE `HALT_ACK=1 safe-apply`; CodeSha256 read back `jhGc2J4Q..`.
4. **V1:** the history route read for Cottonwood (svc principal, GETs only): page 1 lists REQ-c1b53772 first, and
   `2.0.0_SA_COO~D`'s page row shows Y-2. Then the recorder runs, and the ledger and S326 close.
