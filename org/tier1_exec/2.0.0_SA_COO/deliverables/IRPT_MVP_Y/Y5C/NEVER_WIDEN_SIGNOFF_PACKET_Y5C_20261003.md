# Never-widen sign-off packet -- Y-5 / row S316: the resident (st19 -> st20) and irpt-ycharts-generate at ONE commit `136ee09e9f`, so the holdings upload sends and reconciles dollars at cents and a refused echo names its counts

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-03 ~23:5xZ.

**Authority:** Andrew ~20:3xZ "all approved" (CTO 104738): Y-5 then Y-4 run. CTO 104634: the run order. Row
IRPT_BCKEND-S316 (BLOCKING, owner ~Y) @88e1593ea1: Y-5 V1's Aproxy job `REQ-51d9daac..` went ATTENTION
VENDOR_UPLOAD_REFUSED at 22:28:59Z. The page half passed: the proxy box appeared, SGOV was named, and the upload went NORMALIZED.

**Ledger:** `irpt-y5c-20261003` (U1, U2 closed; D1, D2, V1 open). **Two moves** in one window, both or neither. No IAM, route,
table, queue, schema or contract move. No vendor call in D1 or D2.

## 1. What ships

**The code:** `fbae4f4190`, merged `136ee09e9f`; the generate row re-pinned at `e4cf38c400` (84 entries; bytes change in 2).

| file | change |
|---|---|
| `ycharts/generate/recipe.py` | `_cents`: the advisor's amount at cents, half up; one that rounds to zero is refused like any non-positive amount. `holdings_csv` sends it; `step_upload`'s `expected` is it. The echo is still parsed exactly (Decimal) and compared numerically, so a one-cent vendor change still refuses. `step_upload` also returns `echo_counts` (sent, echoed, missing, extra, amount_diff, sub_cent, missing_punct, errors, rounded, unique, record_id_int) and `vendor_status`: counts and closed tokens only |
| `ycharts/generate/resident_worker.py` | `refusal_line`, for the upload step only, appends `upload=<counts> vendor_status=<token> weight=<token>`. Every other step's line is byte-identical (the existing exact-line tests pass unchanged) |

**Why both:** the resident runs the job (`recipe.step_upload`, `refusal_line`); the Lambda bundle packages the same two modules.
One commit, all or none.

**ONE behavioural change: cents.** The rest is instrument. The cause is INFERRED, not measured: the easy file's amounts, counted
in memory, carry 12-15 decimals in 10 of 99 rows (binary float noise). If the next run passes, the difference names it as the
cause. If it refuses, the counts name the cause.

**Artifacts (U1, U2 closed):**
- **The generate zip:** version `31clJjOmhSm6YK4_6kH3ZkBD9GRxSol8`, 592,374 bytes, sha256
  `FgZcBjJuwuBD0P97xHCgnj37gjdyHzl+8zky26MD2Nk=`. LF build at `e4cf38c400`: 114 members, 0 differ from the pin, 0 CRLF. Census
  vs live `jKsI7pZW..`: identical 112, changed 2 (`recipe.py`, `resident_worker.py`), added 0, removed 0. Cold-start smoke PASS
  on its three routes.
- **The resident tar:** `irpt-resident-136ee09e9f-st20.tar.gz`, sha256 `1e3756f4a1735c6b9f5d655823aa4bade9cd651a0c8513d12facaeab62df5f24`,
  792,704 bytes, version `cCO3C_41ttJOTNVTVYWIaBEjmdY88zUX`.
- **The install script:** sha256 `b06a67203d7de3074e4bd171d76e2bdae3dba263621ca20dff9a2a571ce602ea`, version
  `sAGXWaCzCUxzSz9QGF8kl61aF2jwXCcE`. Both keys read 404 before.
- **The gate:** G1-G5 PASS. G5 vs the running st19: changed 3 (`recipe.py`, `resident_worker.py`, the generated bindings), added
  0, removed 0. The capture library and wrapper equal st19's.

## 2. Writers of the changed value

The dollars sent to YCharts have ONE writer, `recipe.holdings_csv`, and the reconciliation's expected value has one,
`step_upload`; both now read `_cents`. The create step's items (`items_body`) come from the ECHOED weighting, as before.

## 3. Reader census

- `step_upload`'s result is read by `resident_worker` (its `ok`; `refusal_line` on refusal) and `job.py:371` (appended to
  the job record's steps). The new keys `echo_counts` and `vendor_status` are counts and tokens; `refusal_line` is their only
  reader. The checkpointed rows still come only from a reconciled echo.
- An upload whose amounts all have at most two decimals sends a byte-identical CSV (unchanged path). Only amounts with more
  decimals are rounded, and only an amount under half a cent is newly refused, before any request.
- No contract, page or other Lambda reads these values.

## 4. Blast radius

| path | after |
|---|---|
| an upload with amounts at cents (every earlier READY job) | unchanged CSV, unchanged reconciliation |
| an upload with sub-cent float noise | sent at cents; reconciles if the vendor echoes cents |
| an amount under half a cent | refused before any vendor request (was sent) |
| a refused upload | the same refusal, plus the counts line in the journal |
| every other step and its journal line | unchanged |

## 5. Rollback, per key

- **irpt-ycharts-generate:** re-promote S3 version `YImF8vih8CBtZqEM7XksUccMJ63UayVz` (`jKsI7pZW..`, live now) with ONE targeted
  plan and safe-apply; CodeSha256 read back.
- **The resident:** the unit back to `/opt/irpt-resident/a163441fb0-st19`, which the install script keeps; unit active and queue
  0/0 read back. All or none.

## 6. Proofs

Offline: `test_recipe_decimal` +3 (float noise sent and reconciled at cents; missing and sub-cent counts; rounds-to-zero refused
before transport) and `test_read_back_poll` +1 (the upload line's counts with no identifier; other steps unchanged). Negative
control: on HEAD's `recipe.py` and `resident_worker.py` the 4 new tests FAIL. Suites: ycharts/generate 400 passed 30 skipped;
intake 272 passed 1 skipped; ycharts/session 118 passed 1 skipped.

**V1 (YCharts, under the solo gate):** `2.0.0_SA_COO~D`'s Aproxy from the page, Cottonwood chosen. The upload reconciles and the
Overview reaches READY, or the refusal line names its counts.

## 7. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read, STOP on any difference:** generate CodeSha256 `jKsI7pZW..`; root `a163441fb0-st19`, unit active; queue 0/0,
   no non-terminal job, the provider lease not held.
3. **D1:** a fresh targeted plan (code only, 1 to change); ONE `HALT_ACK=1 safe-apply`; CodeSha256 read back `FgZcBjJu..`; the
   cold-start smoke on the deployed bytes.
4. **D2:** `head-object` of the script key printing `sAGXWaCz..`; `Y5C/install_fetch_and_run.sh` over Systems Manager (sha256
   checked against `b06a6720..`). Read back: root `136ee09e9f-st20`, the `recipe.py` (`0d57427f..`) and `resident_worker.py`
   (`a1b6adc3..`) digests, unit active, queue 0/0.
5. V1, then the ledger closes (and `irpt-y5v-20261003` V1 with it).
