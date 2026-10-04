# Never-widen sign-off packet -- Y-5 / row S316, part 2: the resident (st20 -> st21) and irpt-ycharts-generate at ONE commit `3f29017cfc`, so the cents upload is BOUND at cents and a binding refusal is a named ATTENTION

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-04 ~01:4xZ.

**Authority:** Andrew ~20:3xZ "all approved" (CTO 104738); CTO 104634 (run order); row IRPT_BCKEND-S316 (owner ~Y). The Y5C half
(batch 235) served the cents upload. Its live run measured the next defect.

**The defect, measured** (Aproxy `REQ-6be454cbb317d96a6e4ba5f8`, 2026-10-04):
- The cents upload reconciled. The holdings upload POST answered 200, and NO `STEP_REFUSED` was journaled, so YCharts
  echoed cents. This MEASURES S316's cause: the float noise.
- `normalized_input.bind_normalized_upload` then compared that cents echo to the retained input's EXACT amounts and raised
  `RecipeRefused`. That was AFTER the vendor upload and BEFORE its checkpoint.
- Nothing journaled it. The message came back 900 s later, and the redelivery could only answer ATTENTION
  `AMBIGUOUS_HOLDINGS_UPLOAD` (00:56:21Z).

**Ledger:** `irpt-y5d-20261004` (U1, U2 closed; D1, D2, V1 open). **Two moves**, both or neither. No IAM, route, table, queue,
schema or contract move. No vendor call in D1 or D2.

## 1. What ships

**The code:** `3a14a49f48`, merged `3f29017cfc`; the generate row re-pinned at `99dd031309`.

| file | change |
|---|---|
| `ycharts/generate/normalized_input.py` | `bind_normalized_upload`'s `expected` is `_cents(_amount(value))`: the same rule `recipe.step_upload` sends and reconciles by. The echo is still parsed exactly and compared numerically, so a one-cent difference still refuses |
| `ycharts/generate/resident_worker.py` | `bind_upload_or_attention` wraps both bind calls (`:256-260`). A `RecipeRefused` journals `IRPT_RESIDENT_STEP_REFUSED step=upload_binding` and raises `WorkerAttention("VENDOR_UPLOAD_BINDING_REFUSED")`: terminal and named, no silent redelivery |

**Artifacts (U1, U2 closed):**
- **The generate zip:** version `w031eAfDs6mh.1ZOCaAks5bHDhKj8ajT`, 592,791 bytes, sha256 `uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ=`.
  LF build at `99dd031309`: 114 members, 0 differ from the pin, 0 CRLF. Census vs live `FgZcBjJu..`: identical 112, changed 2
  (`normalized_input.py`, `resident_worker.py`), added 0, removed 0. Cold-start smoke PASS on 3 routes.
- **The resident tar:** `irpt-resident-3f29017cfc-st21.tar.gz`, sha256 `40eaa8eefa94b699fd00430e6d0d940a7b63425af2f9a7d61f4b3c460654fcd9`,
  793,108 bytes, version `Afk.fAfNkFDqQ6_ghVaHIYiUJZtwMyFj`.
- **The install script:** sha256 `8c3a4fc1e8bbb5026604bf379b7afbb7b307a9a16221d501a32334693ac2643b`, version
  `WjDopraRJ16d6CeXA7tgNjVzjyvB98Da`. Both keys read 404 before.
- **The gate:** G1-G5 PASS. G5 vs the running st20: changed 3 (`normalized_input.py`, `resident_worker.py`, the bindings), added
  0, removed 0.

## 2. Writers of the changed comparison

The bind's expected amounts have ONE writer, `bind_normalized_upload`. It now reads `recipe._cents`, the same rule as the
CSV sent and the upload reconciliation (Y5C).

## 3. Reader census

- `bind_normalized_upload`'s result is read only by `resident_worker` (the upload checkpoint, `:258`) and by the re-bind of an
  existing checkpoint (`:260`). Its returned `total_dollars` and `rows` are unchanged in shape: `total_dollars` is the
  retained input's, and `rows` is the echo.
- The new attention code `VENDOR_UPLOAD_BINDING_REFUSED` is read by the status route as any ATTENTION. It surfaces as
  UNAVAILABLE, as `ops/owned_status.py:21-23` shows every attention.
- An input whose amounts are at cents binds exactly as before.

## 4. Blast radius

| path | after |
|---|---|
| an upload at cents (every earlier READY job) | unchanged |
| an upload with sub-cent float noise | binds at cents; the job continues to create |
| a real vendor change of a cent or more | refused, now as named ATTENTION `VENDOR_UPLOAD_BINDING_REFUSED` (was a silent redelivery, then AMBIGUOUS) |
| every other step | unchanged |

## 5. Rollback, per key

- **irpt-ycharts-generate:** re-promote S3 version `31clJjOmhSm6YK4_6kH3ZkBD9GRxSol8` (`FgZcBjJu..`, live now); CodeSha256 read back.
- **The resident:** the unit back to `/opt/irpt-resident/136ee09e9f-st20`, kept by the install script. All or none.

## 6. Proofs

Offline: `test_normalized_input` +1 (float noise binds at cents; a one-cent change refuses), `test_read_back_poll` +1 (the
named attention and its journal line). Negative control: on HEAD's two modules both FAIL. Suites: ycharts/generate 402 passed
30 skipped; intake 272 passed 1 skipped; ycharts/session 118 passed 1 skipped.

**V1:** `2.0.0_SA_COO~D`'s Aproxy from the page. The upload reconciles and binds, and the Overview reaches READY.

## 7. Apply protocol

1. Both halves at HEAD naming this file's blob.
2. **Before-read, STOP on any difference:** generate CodeSha256 `FgZcBjJu..`; root `136ee09e9f-st20`, unit active; queue 0/0,
   no non-terminal job, the provider lease not held.
3. **D1:** a fresh targeted plan (code only, 1 to change); ONE `HALT_ACK=1 safe-apply`; CodeSha256 read back `uFTONal/..`; the
   smoke on the deployed bytes.
4. **D2:** `head-object` of the script key printing `WjDopraR..`; `Y5D/install_fetch_and_run.sh` over Systems Manager (sha256
   checked against `8c3a4fc1..`). Read back: root `3f29017cfc-st21`, `normalized_input.py` (`1cbbcb47..`) and
   `resident_worker.py` (`805bc24e..`) digests, unit active, queue 0/0.
5. V1, then this ledger, `irpt-y5c-20261003` and `irpt-y5v-20261003` close on its READY.
