# Deploy Completion Record
**Date opened:** 2026-09-28T20:32:56.553266+00:00
**Status:** OPEN
**Deploy:** MX-s-10 PHASE B (TO MX-s-12): publish infra/aws/ssm/opal-bd-asset-dim-download.json @0ff972bc38 as DEFAULT of SSM doc opal-bd-asset-dim-download; retire the fees schedule leg (bd-fees-pipeline-trigger, bd-fees-trigger) + two Playwright scripts through Terraform; acceptance = the 22:10Z scheduled weekday fire (G2 disclosure). Halves: CTO RULING_MX-s-10_NEVER_WIDEN_CTO_HALF_20260928.md, CVO cvoO_NFRA_MCPINDEX_MX-s-10_NEVER_WIDEN_SECOND_HALF_20260928.md
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~8
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | G1 rollback targets read live: prior SSM DefaultVersion, served dim VersionId, id count, non-null cusip count, id-set sha256 | values printed from live aws describe-document and list-object-versions, never typed | G1 read live at 20:3xZ 2026-09-28: SSM opal-bd-asset-dim-download DefaultVersion=3 (LatestVersion=3; created 2026-09-26T21:31:57-04:00; versions 1,2,3 exist; v3 content saved to scratch, carries download-daily-asset-dim.ts x1, pull_bd_asset_dim_rest x0). Served dim s3://opal-data-bd/silver/bd_assets_dim.parquet live LATEST VersionId=kittUyy.WHGfmKRaAag.p4TqGFycZ3eA (12:22:57Z, 977308 B, etag a33f5eef4dbcdbbba1a5928ee3ca0348) == the CVO-named id, no difference; prior versions bSQWML.. 12:08:43, Pa4qx5.. 12:04:24, pdoQY5.. 06:22:06. G2 baseline read from that VersionId: 12141 asset_ids (12141 unique), 22 columns, non-null cusip 10957 (non-blank 10957), asset_id-set sha256 (sorted str ids joined by LF, no trailing LF) b38a8b0a5dd07053a2d822ef6ad6e76e44d7e9a59b6615f7d259c9c74cb9616a. Repo doc byte-equal to git show 0ff972bc38 (sha256 294a7036...ae95e). | CLOSED 20260928T203736Z |
| L2 | activation | SSM doc opal-bd-asset-dim-download published from repo file byte-equal to 0ff972bc38 and set DEFAULT | get-document DEFAULT content equals file as parsed JSON; carries rc 92 refusal and --union-bronze; AC1 PASS | 20:37-20:38Z: repo doc byte-equal to git show 0ff972bc38 (cmp; sha256 294a703617118218e386c275c4a1511bdef6dd833722031c6192ee04fd8ae95e). update-document --document-version $LATEST -> new version 4 (Hash equals the file sha256). update-document-default-version 4 -> describe-document DefaultVersion=4 LatestVersion=4 Active. Rollback = update-document-default-version 3. Readback get-document (DEFAULT) DocumentVersion=4 JSON, content equals the file as parsed JSON objects (True); carries MERGE_RC=92 refusal x1 and build_bd_assets_dim.py --union-bronze builder call x1 (--union-bronze x2). AC1: served document: rest-pull refs=4 builder refs=4 playwright refs=0 BD_PASSWORD refs=0 -- RESULT: PASS -- exit=0 | CLOSED 20260928T203948Z |
| L3 | activation | Terraform retire fees leg (bd-fees-pipeline-trigger rule+target+permission, bd-fees-trigger lambda) via safe-apply; delete two ts scripts and EC2_MANIFEST _ts_source entry | G3 plan graded (only fees-leg destroys); apply result; plan -detailed-exitcode 0; AC2 PASS |  | OPEN |
| L4 | verify | G2 at the scheduled 22:10Z fire: builder DELTA block, ids before/after/added/removed, cusip non-null before/after, per-column changed counts | AC3 PASS + run log excerpt; rollback to the G1 VersionId if ids fall or any cusip non-null->null |  | OPEN |
| L5 | git | retirement and ledger committed on the worker branch (LOCAL, not pushed) | commit hashes |  | OPEN |

## Log

- 20260928T203256Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~8 with 5 leg(s)
- 20260928T203736Z LEG L1 closed: G1 read live at 20:3xZ 2026-09-28: SSM opal-bd-asset-dim-download DefaultVersion=3 (LatestVersion=3; created 2026-09-26T
- 20260928T203948Z LEG L2 closed: 20:37-20:38Z: repo doc byte-equal to git show 0ff972bc38 (cmp; sha256 294a703617118218e386c275c4a1511bdef6dd833722031c61
