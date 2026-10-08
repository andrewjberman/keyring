# Deploy Completion Record
**Date opened:** 2026-10-08T17:32:30.825199+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T174657Z
**Deploy:** irpt-ycharts-generate release 2: TCKT_VNEXT X-1 on-behalf upload by listed OPAL_GLOBAL filer (uploads.py, interactive_access.py, generate_installed.py); pin f7a9d0b34f; built 798Lgqw2..; rollback ZspX0qD2.. / S3 objver 4Pvl.mN3tY9bIQDDVVnGYFiNoKbrUSTh; CTO half 6d24511482
**Authored by:** 0.9.0_WK_IRPT_BCKEND~156
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-checks: pin ancestor, census=3 members, live CodeSha256 == ZspX0qD2.. | ancestor rc0 + changed_members=3 + live hash read + rollback objver | pin f7a9d0b34f ancestor of worktree HEAD rc0 (and shared tree HEAD); release-census changed_members=3 (uploads.py, interactive_access.py, generate_installed.py); live CodeSha256 ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI= LastModified 2026-10-08T10:06:18Z Active; tfstate s3_object_version 4Pvl.mN3tY9bIQDDVVnGYFiNoKbrUSTh == S3 current versionId (content-sha256 ZspX0qD2..) = ROLLBACK SOURCE; shared ycharts tf dir diff HEAD empty | CLOSED 20261008T173319Z |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-ycharts-generate -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | built sha256 == 798Lgqw2.. + new versionId | build-and-upload.sh investor-reporting irpt-ycharts-generate rc0: import-closure OK (63 .py), SHA256 798Lgqw25X1am7uCjdgYdTSOY90saT2k3n8H01eOBJ0= (== signed BUILD_ONLY), s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip write VERIFIED size=589480, new versionId pTwegws7bhMLymxAB_L8zRkJsftwhtu3, content-sha256 metadata 798Lgqw2.. (head-object). Running code unchanged by this leg. | CLOSED 20261008T173415Z |
| L3 | activation | safe-apply of ycharts saved plan -target module.irpt_ycharts_generate.aws_lambda_function.this; 0 add 1 change 0 destroy | apply output + live CodeSha256 == 798Lgqw2.. | dell2 apply from shared initialized ycharts root: saved plan (Y65-1_plan.txt, committed 9a06bf02fe) 0 add / 1 change / 0 destroy (s3_object_version 4Pvl.mN3tY9bIQDDVVnGYFiNoKbrUSTh -> pTwegws7bhMLymxAB_L8zRkJsftwhtu3, source_code_hash ZspX0qD2.. -> 798Lgqw2..); .tools/safe-apply.sh: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' comp-tagauthz gate PASSED, no TAGAUTHZ_OVERRIDE used. Live after: CodeSha256 798Lgqw25X1am7uCjdgYdTSOY90saT2k3n8H01eOBJ0= LastModified 2026-10-08T17:37:00Z Active/Successful; targeted re-plan: No changes (rc0). | CLOSED 20261008T173759Z |
| L4 | verify | after-reads 1-7 + test row and every upload key deleted and read NOT FOUND | after-reads file + NOT FOUND reads | BRANCH B (stopped, rolled back): after-reads 6 (census modules 62 failed={}) and 7 (live 798Lgqw2.., re-plan No changes) passed on release 2; test profile row put and deleted, get-item reads NOT FOUND; admit reads 1-5 NOT RUN because the operator credential cannot decrypt irpt-requests (KMS), so the admit's records could not be read or deleted - upload_keys empty, nothing written there; rolled back 17:44:54Z via s3 copy-object of version 4Pvl.. (new versionId QBeNB.XXjTccRAbSADmCh_Wv7R0brx6q, content ZspX0qD2..) + targeted safe-apply 0/1/0; live CodeSha256 ZspX0qD2.., re-plan No changes, census failed={}. Rows IRPT_BCKEND-D2-W156-S1 (BLOCKING), -S2. After-reads file Y65-1_release2_after_reads.json. | CLOSED 20261008T174656Z |

## Log

- 20261008T173230Z OPENED by 0.9.0_WK_IRPT_BCKEND~156 with 4 leg(s)
- 20261008T173319Z LEG L1 closed: pin f7a9d0b34f ancestor of worktree HEAD rc0 (and shared tree HEAD); release-census changed_members=3 (uploads.py, inter
- 20261008T173415Z LEG L2 closed: build-and-upload.sh investor-reporting irpt-ycharts-generate rc0: import-closure OK (63 .py), SHA256 798Lgqw25X1am7uCjdg
- 20261008T173759Z LEG L3 closed: dell2 apply from shared initialized ycharts root: saved plan (Y65-1_plan.txt, committed 9a06bf02fe) 0 add / 1 change / 0
- 20261008T174656Z LEG L4 closed: BRANCH B (stopped, rolled back): after-reads 6 (census modules 62 failed={}) and 7 (live 798Lgqw2.., re-plan No changes)
- 20261008T174657Z CLOSED -- all 4 legs proven
