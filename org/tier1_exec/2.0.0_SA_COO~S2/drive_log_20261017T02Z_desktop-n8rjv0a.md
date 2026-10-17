# Drive log -- 2.0.0_SA_COO~S2, IRPT_BCKEND (~PS), 2026-10-17 01Z to 03Z, dell2

Substantive ticks only. Push state: LOCAL (box-sync pushes).

## 01Z-02Z -- ADDENDUM 3, the build and the drain
- IB-pr-551 ADDENDUM 3 (GetObject ONLY, one fence row, current-object read with a sha256 refusal), COO half blob `87a46d9cf370c293dae46a413cba213db721b5ef` (@608a8d2ca3), CTO half signed @94032d0bb7. TO-IB-pr-616 amended to match (@a5c2a5001b).
- Build cell IB-pr-617 (worker 481, cut @1c90b73048) and its comment repair IB-pr-619 (cut @5d780c8ee4). Worker 481 correctly STOPPED once on the p249 AC2 miscount (trunk files merged into its branch counted as its own edits); the checker was amended @7f7d96b808. Drained as `1dab1295ef`: p248 AC1-AC3 and p249 AC1-AC3 PASS on my own reads on the worker tree and again on the merged trunk, 31 tests pass.
- Rows: S229 (worker rows dispositioned, @3806013c24).

## 02Z-03Z -- the bundle apply
- TO-IB-pr-618 cut to `0.7.0_AE_CloudOps~IB2` (@e4fcda6c7f, decomp section 245, WORLD), checks `checks/r250/` (control: 3 positives, 16 negatives). MSTR's drain deleted `lambda-source-map.json`; the function-map entries for both functions held the pre-release shas (row S230). Order amended @6303a4640f: step 6 stamps both entries.
- IB2 report (record @f19d4b175a). My own reads, 2026-10-17 ~02:5xZ: p250 AC1, AC2, AC3 PASS; `irpt-export-render` live CodeSha256 `VerVs2a1iMETEKTPJwgHIbiiABUxutD7K/KqsMOmen4=` (LastModified 02:47:20Z) equals the record's built and after sha; 14 environment variables before and after; the read function still `z634S2Qs...`; build commit `347505c467` is an ancestor of HEAD. function-map `artifact_sha256` reads the new values for both functions.
- Observed, not yet ruled: both function-map entries still carry the OLD `deployed_code_sha256` (`5/9LZBbT...` and `WjnDxvu2...`); the stamp tool moved `artifact_sha256` only. Whether a drift classifier reads that field is unread; to be read next tick (not yet asked of IB2).

## Open
- TO-IB-pr-616 Step 6 (the IAM statement, GetObject ONLY): fence row at HEAD of `exemptions.json`; the ADVI CloudOps regeneration is not yet read back. The second GO waits on that read.
- Ledger `irpt-bckend-serve-path-hops-3-4a-report-route-export-bundle-20261017`: L7 stays open until Step 6 is read back.
- Switch-on pair: waits on hops 2, 3 and 4 all live (`~D2`'s TO-DB-b-312 for hop 2).
- Debt D2-S216 (resolve.py G7/G8 duplication) at my next touch.
