# Deploy Completion Record
**Date opened:** 2026-09-12T06:55:09.506514+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-6: re-mint the investor_reporting bundle with ids.py as a third member (a DISTRIBUTION from the one authority), then re-run the host import check that failed this morning
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting -- re-mint via the in-flow path (python .tools/safe_deploy_core.py --mint-bundle investor_reporting), never a side script. ROLLBACK: the payload is DETERMINISTIC (sorted members, zeroed mtime, gzip mtime=0), so reverting the one-line member declaration and re-minting reproduces the current object byte-for-byte; current ETag 964b4eef4f50792d4599e7df0d419486, 34476 bytes | the BUNDLE MINTED line plus head-object ETag == local md5 and all THREE per-member shas echoed back on the object |  | OPEN |
| M1V | verify | the mdpf-daily-runner host imports the minted runner: the same read-only SSM probe that printed ModuleNotFoundError: No module named 'ids' at 06:1xZ, re-run against the re-minted bundle | IMPORT-OK with _REPO resolved and run_firm present, in the SSM stdout |  | OPEN |

## Log

- 20260912T065509Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 2 leg(s)
