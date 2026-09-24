# Never-widen half, 2.0.0_SA_COO~M -- the N1 push's two served objects (LD-0613 Progress 11)

**Author:** 2.0.0_SA_COO~M, 2026-09-24 ~18:1xZ. **Asked by:** 1.0.0_SA_CTO msg 100797.
**Status:** Andrew's "Push it" (~17:5xZ, `d4202fe6a3`) replaced this half as the push gate. It remains the measured
blast-radius record for the push, and it names one precondition for the pusher (section 3).

## 1. Key `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`

- **Served now (head-object):** version `Ku6.brgEK.LYO6RIqzXSNdyAM9j_NsCX`, LastModified 2026-09-23T20:46:14Z. All 10
  member stamps equal the `751e48b969` (origin/CLOUD) blob sha256.
- **Writers of the key: 1.** `.tools/safe_deploy_core.py` `mint_bundle`, reached by the pre-push gate or `--mint-bundle`.
  No other file names the key; `schedule.tf:194` is a reader.
- **Moves (committed bytes, blob sha256 at `d4202fe6a3`):** 2 of 10 members.
  - `holdings_snapshot.py`: `5f310f5c...` -> `880b52e75915e995...`.
  - `HoldingsSnapshot.schema.json` (2.0.0_SA_COO~P's file): `682f3eb2...` -> `6fea93226899ec0e...`.
  - The other 8 members are byte-equal to their served stamps.
- **The consumer's own rule, both branches.** `irpt-directory-refresh` is live ENABLED (cron 09:00 ET MON-FRI). It
  dispatches by SSM, extracts the tar and runs ONLY `directory_runner.py` (`directory/refresh.py:569-588`).
  `directory_runner.py` imports neither moved file; its closure is the 8 unchanged members.
  - **Build completes:** same output as today.
  - **Build refuses:** same refusal code, unchanged.
  - **Log-only change:** the dispatch's `bundle sha256` echo and member listing.
- **`holdings_snapshot.py` from the bundle, both branches:**
  - **Scheduled:** its only trigger, `irpt-holdings-snapshot`, reads DISABLED live, and its target is an inert SQS
    message. It does not fire.
  - **Run by hand from the bundle:** it raises `ModuleNotFoundError: publication` at import, before any read or write.
    Measured on the HEAD 10-member closure, with `directory_runner` IMPORT-OK as the positive control. The served bytes
    import `publication` too (origin `:99`).
- **Rollback:** the bucket is versioned (Enabled, read). Copy the prior version back:
  `aws s3api copy-object --bucket opal-data-mdpf --key <key> --copy-source "opal-data-mdpf/<key>?versionId=Ku6.brgEK.LYO6RIqzXSNdyAM9j_NsCX" --metadata-directive COPY`.
  Then read back `holdings-snapshot-sha256 = 5f310f5c26f66fbe...`.

## 2. Key `s3://opal-data-mdpf/code/scripts/gold/taxsma_membership.py`

- **Served now:** version `GMs.xhrRBXWFpnU56ab8HEUINLxV7ab5`, ETag `6375ddd4...`, equal to the origin blob md5.
- **Writers of the key: 1.** `safe_deploy_core` `deploy_file` (gold layer), which reads INDEX bytes.
- **Moves:** one commit, `d3a8c3e7e3`. It implements `S3DispositionStore`, which before raised `NotImplementedError`,
  and adds `asdict` to the imports. The new md5 is `0c6da86f...`.
- **The consumer's own rule, both branches.** The served caller is `mdpf_gold_consolidator.py` (served ETag `5dbc7a53...`,
  equal to origin; unchanged in N1). Its only call, `run_taxsma_prelude(now=, gateway_call=)` at `:1932`, passes no
  store, so `:1287-1288` constructs `LocalDispositionStore()` (in memory).
  - **S03 passes:** classify, count and emit go into the in-memory store. No changed line runs.
  - **S03 refuses:** it returns `_failed(...)`, unchanged.
  - The only constructor of `S3DispositionStore` is `investor_reporting/tax_membership_once.py:171`. It is not served
    (non-member) and runs from the repo by hand.
- **Rollback:** copy-object from `versionId=GMs.xhrRBXWFpnU56ab8HEUINLxV7ab5`, then read back ETag `6375ddd4ee9b87e5687c079d3426c82b`.

## 3. Precondition for the pusher: the bundle mint reads WORKING-TREE bytes

`build_bundle_payload` (`safe_deploy_core.py:891-893`) reads `WORKSPACE/<repo_path>`. `deploy_file` reads the index
(`_index_blob`, `:686`).

At ~18:0xZ the shared tree held 3 JSON members as CRLF over LF blobs: `data/firm_registry.json`,
`HoldingsSnapshot.schema.json` and `DirectoryEntry.schema.json` (`core.autocrlf=true`; no eol attribute on them).
- **Effect:** a push from that tree would have minted 4 changed members, not 2.
- **Two of the four were read by the live directory runner:** `firm_registry.json` and `DirectoryEntry.schema.json`.
- **Stamps:** they would no longer equal any git blob.

2.0.0_SA_COO~M rewrote the 3 files to their blob bytes; `git diff` rc=0 and status is clean. They return to CRLF the
next time git checks them out. **Before the push, check `git ls-files --eol` on the 10 members: every one must read
`w/lf`.**
