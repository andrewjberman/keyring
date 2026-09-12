# Deploy Completion Record
**Date opened:** 2026-09-12T05:17:04.599309+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-2 (amendment 6 F3): the LAST root -- irpt-ycharts-generate, which disarms W2-S39 on the final function and puts the v0.14 envelope and the post-read business_date on it
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| Y1 | activation | irpt-ycharts-generate (root .../ycharts). ROLLBACK: restore prior S3 object version, artifact sha VGsTbaPGv70V2l2w8X85z7XK8NEB9hTkbkeDmke1Dt8=, handler entry.lambda_handler unchanged. RIDER NAMED: IB-rt-11's intake/settings.json edit is a declared build input of this function and this apply ships it -- released by amendment 6 F1, whose corrected guard runs ONE way (a zip carrying parse.py must carry both companions) and this zip carries no parse.py. W2-S42 PRE-CONDITION: the root must plan NO destroy line | artifact_sha256 == S3 content-sha256 == live CodeSha256 printed, and a post-apply plan reading No changes |  | OPEN |
| Y1V | verify | irpt-ycharts-generate extract-and-import of the DEPLOYED artifact in the flat /var/task layout, fresh isolated interpreter, repo asserted absent from sys.path, layer mounted per the LIVE function's own attachment | IMPORT-OK + negative control FIRES + three-way hash equality |  | OPEN |

## Log

- 20260912T051704Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 2 leg(s)
