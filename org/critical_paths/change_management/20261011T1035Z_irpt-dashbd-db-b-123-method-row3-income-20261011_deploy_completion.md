# Deploy Completion Record
**Date opened:** 2026-10-11T10:35:44.501397+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T103938Z
**Deploy:** IRPT_DASHBD DB-b-123: overwrite Cottonwood method row 3 (2 keys) so income is ABSENT
**Authored by:** 0.9.0_WK_IRPT_DASHBD~98
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | capture of the 2 keys (bodies, sha256, ETag, versioning) outside the repo | sha256+size+ETag per key, bucket versioning | captured both keys outside the repo: data.parquet etag 7b70c246337d26fbba60eac594c21f0f 10421 bytes sha256 7a087b363476534681505c2d5e7ab6725a4ac451f8dadfbf66a68fda093a6596 version .MnBtIEprWTsvzhZSqkuRkJCU1n4SehQ; manifest.json etag 5951829e6839cf07e4ef3ce1afdca914 1831 bytes sha256 75846d1fc47ee320c448d399cd621c4ff6dd589d2f66de001315109a1ab0ffbc version In.WljkGD7o_t6CsgY8O7clIHMh3K1IH; bucket versioning Enabled; dry-run diff: only income_basis, income_basis_claim, income_basis_reason; other_columns_moved=0 | CLOSED 20261011T103937Z |
| L2 | activation | one overwrite of data.parquet and manifest.json under dim_return_method/method_version=3 via emit_method_row | emit_method_row return, keys_written | emit_method_row(s3, cottonwood, thresholds, upload=True, src=entry) at 2026-10-11T10:38:2xZ returned landed=true etag 9c774f3770e82ed5e7e6b2a4ebe3e7d3; head after: data.parquet 11641 bytes version hcqKO1hmuZIFPMKZrRF6gw7jS0mY4xnU, manifest.json 2037 bytes etag 6d5aabdd1e0f3cc9ff2a6c544bd327fd version 9mFo70MiWTNgg3u8xC24yvm3pmOsxQw6 | CLOSED 20261011T103937Z |
| L3 | verify | served read-back of both keys and the row | head-object both keys, served row income members, mint method_row verify | served data.parquet read back sha256 ff9afa0079273cb743f86ab1b460aeb0dbe2c7283231d416769753a3bc29ec7b: income_basis null, income_basis_claim absent, income_basis_reason non-empty, method_version 3; columns_changed the 3 income members, other_columns_moved=0; mint method-row read (verify_served lines 981-989 performed alone): method_row=match | CLOSED 20261011T103938Z |

## Log

- 20261011T103544Z OPENED by 0.9.0_WK_IRPT_DASHBD~98 with 3 leg(s)
- 20261011T103937Z LEG L1 closed: captured both keys outside the repo: data.parquet etag 7b70c246337d26fbba60eac594c21f0f 10421 bytes sha256 7a087b3634765
- 20261011T103937Z LEG L2 closed: emit_method_row(s3, cottonwood, thresholds, upload=True, src=entry) at 2026-10-11T10:38:2xZ returned landed=true etag 9c
- 20261011T103938Z LEG L3 closed: served data.parquet read back sha256 ff9afa0079273cb743f86ab1b460aeb0dbe2c7283231d416769753a3bc29ec7b: income_basis null
- 20261011T103938Z CLOSED -- all 3 legs proven
