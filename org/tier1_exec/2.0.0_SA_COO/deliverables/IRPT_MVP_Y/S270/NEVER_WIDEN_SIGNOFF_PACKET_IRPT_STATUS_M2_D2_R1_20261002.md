# Never-widen sign-off packet -- irpt-status at ONE commit `0f70e6156e` (RE-CUT): S270 M2 (the bounded per-row pool, one boto3 Table per thread, + 1024 MB) and hop 11 D2 (the SigV4 signer), then hop 11's route again (R1)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~14:3xZ; RE-CUT ~16:0xZ on CTO rulings batch 176 (the refusal of the
`b789341289` bundle: one boto3 resource Table shared by the pool's threads).
**Authority:**
- CTO rulings batch 171 (M2: the 8-worker pool, measured offline against live tables, then packeted);
- batch 174 (`memory_size` 256 -> 1024 ships with the pool; the acceptance is every history page size at or under 10 s
  server duration, cold and warm, from REPORT);
- batch 170 (D2, the s3v4 presign client on the regional endpoint, then R1 again with the full V1, under a new half).

**One packet:** M2 and D2 are both irpt-status code, and the whole-bundle rule ships them in one artifact.
**Ledger:** `irpt-status-m2-d2-r1-20261002` (U1 proven; D1, R1, V1). **Two moves:** D1 (code and memory, one function
update), then R1 (the route). No IAM, table or other function moves. No vendor call.

## 1. What ships

| move | change (plans `S270/plan_ops_m2b.txt`, `plan_api_m2b.txt`, full-root plans read ~16:0xZ) |
|---|---|
| D1 | `module.irpt_status.aws_lambda_function.this`: `memory_size` 256 -> 1024; `s3_object_version` `9S5jAZLr..` -> `wXzz3_ghlWfn7pdM12GBxlzl_WOxYQUC`; `source_code_hash` `BNe2n9cV..` -> `h7H7KgX1FsBu4XTLqqpcMOjMnwRdeL9xlGZPwzhibcg=`. The full ops plan (`plan_ops_m2b.txt`, 15:xxZ): 1 change, nothing else |
| R1 | `aws_apigatewayv2_route.irpt["GET /api/scoped/investor-reporting/analysis/requests/{requestId}/pdf"]` created on `integrations/8ogp332`. The full api plan: 1 to add |

**The bundle:**
- 47 members, every one at `0f70e6156e` (row repinned `3e32b4866a`);
- uploaded 15:59:12Z, 337,059 bytes; read back by version with the sha256 equal;
- 0 members differ from the pin.

## 2. Every member changed since live `BNe2n9cV..` (census: 42 identical, 5 changed, 0 added)

| member | commit | attributed to |
|---|---|---|
| `owned_requests.py` | `f4be46173f`, `cee32dcf47` | M2: `HISTORY_WORKERS = 8`; `_row_outcomes` runs history's per-row checks on ONE long-lived pool per process (`_history_pool`, so a warm container reuses its threads and their Tables), in row order, a denied row skipped, the first refusal in ROW order raised |
| `read_memo.py` | `f4be46173f`, `cee32dcf47` | M2 + the batch 176 fix: `ReadMemo(table_factory=...)` gives each THREAD its own Table (`threading.local`); the shared answers and the `fresh()` counter under one lock; reads run outside the lock on the thread's own Table |
| `status_installed.py` | `cee32dcf47` | the batch 176 fix: the table port is `ReadMemo(table_factory=lambda: boto3.session.Session().resource("dynamodb", config=once).Table(requests_table))` -- one Session and Table per thread; it was the only boto3 resource on the per-row path (every other port is a thread-safe client) |
| `pdf_link.py` | `5bc562f689` | D2: SigV4 on `https://s3.us-east-1.amazonaws.com`, virtual addressing |
| `served.py` | `acce364286` | **IB-pr-296** (`~P`): `render_ports_from_env` passes a retained-owner reader. Used ONLY when render ports are installed (export render). Measured at this pin (`S270/RENDER_PORTS_AT_PIN_M2B_20261002.txt`, every module from the built zip): irpt-status's installed Entry has `render_ports None`, `prospect_modes {}` and `load_prospect_owner None`, so it is unreached here. It rides because `_authz` is shared |

## 3. Proofs

**Offline:**
- **M2 against the LIVE tables** (`S270/M2_HISTORY_TIMING_20261002.json`): history at `limit=50`, 22 items. Sequential
  7.85 and 8.12 s; the pool 7.09 and 2.96 s; the same items in the same order. These are laptop times; the served
  REPORT is the acceptance.
- **M2 tests:** order kept and rows concurrent (sequential 2.4 s against the pool's under 1.2 s), a denied row skipped,
  and the first refusal in row order winning even when it finishes later. **The batch 176 test:** 40 reads on 8 threads
  give the sequential answers, every Table touched by exactly one thread, and a second pass is answered by the memo
  with no table call; the memo takes exactly one of a table and a factory. ops 229 passed.
- **Not re-measured live on the re-cut:** the laptop's network read 8-16 s per single DynamoDB/S3 call at 15:3xZ, and
  two attempts timed out in the SEQUENTIAL warm-up (`S270/m2_perthread_run.txt`). The 14:0xZ live reading stands for
  the pool; V1-a's served REPORT is the acceptance.
- **D2:** the default client signs `X-Amz-Algorithm=AWS4-HMAC-SHA256` on `opal-data-irpt.s3.us-east-1.amazonaws.com`
  with `X-Amz-Expires` 300. Negative control: a plain boto3 client signs SigV2 on the global host, the shape S3
  refused live (400 InvalidArgument).

**After D1 (V1-a, S270's acceptance):** `live_walk/s270_timing.py`. The first call after a configuration change is cold.
REPORT durations must be at or under 10 s for:
- history at the default page, cold and warm;
- history at `limit=50`;
- the single read and the status.

Any page size over 10 s means the acceptance is not met: report before R1, keep the code (no regression past M1's
timeout), and bring the next remedy.

**After R1 (V1-b, hop 11's full V1):** `live_walk/hop11_pdf_proof.py` on `REQ-c07e64ca..`, `REQ-59b42fab..`,
`REQ-abec171d..` and `REQ-a69e5751..`. Each must answer a URL on the regional bucket host that expires within 300 s and
downloads a `%PDF-` body whose sha256 and length equal the claim. A MISMATCH rolls back R1. Then
`e7b_read_proof.py --compare` must show plain reads equal; history differs only by new requests, and item 22 keeps
answering.

## 4. Apply protocol and rollback

1. Both halves at HEAD naming this file's blob.
2. **Before-read:**
   - live CodeSha256 `BNe2n9cV..`, memory 256, timeout 29;
   - the key's latest is `wXzz3_gh..` with sha `h7H7KgX1..`;
   - no `/pdf` route.
3. **D1:** a fresh targeted plan of the function showing only memory and the code move; ONE `safe-apply`; read back.
   Then V1-a.
4. **R1:** a fresh targeted plan of the route (1 to add); ONE `safe-apply`; read back. Then V1-b.

**Rollback, per key:**
- R1: a targeted destroy of the route.
- D1: re-promote `9S5jAZLr..`'s bytes as the key's latest (`copy-object` of that version), then a targeted apply with
  memory 256. irpt-status returns to `BNe2n9cV..`, which is serving now.

## 5. Not claimed

- That the pool's speedup holds at every page size: V1-a measures it.
- IB-pr-296's export behaviour: that is `~P`'s packet.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~14:3xZ, and RE-SIGNED ~16:0xZ on the re-cut, on this packet's bytes at the commit that carries it. The write set is one function update
(code and memory) and one API route. The blast radius is section 2. The rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
