# Deploy Completion Record
**Date opened:** 2026-09-12T06:55:09.506514+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260912T065923Z
**Deploy:** IRPT_BCKEND IB-rt-6: re-mint the investor_reporting bundle with ids.py as a third member (a DISTRIBUTION from the one authority), then re-run the host import check that failed this morning
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting -- re-mint via the in-flow path (python .tools/safe_deploy_core.py --mint-bundle investor_reporting), never a side script. ROLLBACK: the payload is DETERMINISTIC (sorted members, zeroed mtime, gzip mtime=0), so reverting the one-line member declaration and re-minting reproduces the current object byte-for-byte; current ETag 964b4eef4f50792d4599e7df0d419486, 34476 bytes | the BUNDLE MINTED line plus head-object ETag == local md5 and all THREE per-member shas echoed back on the object | MINTED through the in-flow path (python .tools/safe_deploy_core.py --mint-bundle investor_reporting). 'BUNDLE MINTED [mdpf] investor_reporting -> s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz (md5=a35420ac32cd714856db41fbcab5a073)'. VERIFIED ON THE SERVED OBJECT, not on the producer's own report: head-object returns ETag a35420ac32cd714856db41fbcab5a073 == the local md5, ContentLength 39331 == the locally built payload, and ALL THREE per-member shas echoed back -- directory-runner-sha256 1e8eb8a5... and holdings-snapshot-sha256 4b50a166... both UNCHANGED from the previous mint, ids-sha256 fc1017b2523f2340c58969b6fe66764dc61969fcf3c9f155657e1a05e6ffc837 equal to the repo authority infra/aws/lambda/investor-reporting/_ids/ids.py byte for byte. The object's own source-repo-paths metadata now NAMES that authority, so the distribution declares where it came from. New VersionId yusulz6abd1H.aGAWnV1fZfCVXgmLqiI; the prior version is retained (bucket versioning Enabled). No file was copied into the repo: the opaque-id normalizer still has exactly ONE copy in the tree. | CLOSED 20260912T065922Z |
| M1V | verify | the mdpf-daily-runner host imports the minted runner: the same read-only SSM probe that printed ModuleNotFoundError: No module named 'ids' at 06:1xZ, re-run against the re-minted bundle | IMPORT-OK with _REPO resolved and run_firm present, in the SSM stdout | THE HOST NOW IMPORTS THE RUNNER. Same read-only SSM probe, same instance i-02448edb624a7a7cf, Status Success rc=0, writes confined to /tmp. Stdout: python3 3.9.25; boto3 1.42.97 / pandas 2.3.3 / jsonschema 3.2.0 all resolve; the unpacked tree now carries THREE files including ids.py beside the runner; and 'IMPORT-OK: directory_runner from /tmp/irpt-rt6-probe/data/assets/scripts/gold/investor_reporting/directory_runner.py' with '_REPO resolved to: /tmp/irpt-rt6-probe' and 'run_firm present : True'. THE DIFFERENCE CONTROL IS THE MORNING'S RUN OF THE SAME PROBE AGAINST THE SAME HOST: it printed 'IMPORT-FAIL: ModuleNotFoundError: No module named ids' with a two-file tree. One member declaration is the whole delta, and row IRPT_BCKEND-W2-S44 is discharged. | CLOSED 20260912T065922Z |

## Log

- 20260912T065509Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 2 leg(s)
- 20260912T065922Z LEG M1 closed: MINTED through the in-flow path (python .tools/safe_deploy_core.py --mint-bundle investor_reporting). 'BUNDLE MINTED [md
- 20260912T065922Z LEG M1V closed: THE HOST NOW IMPORTS THE RUNNER. Same read-only SSM probe, same instance i-02448edb624a7a7cf, Status Success rc=0, write
- 20260912T065923Z CLOSED -- all 2 legs proven
