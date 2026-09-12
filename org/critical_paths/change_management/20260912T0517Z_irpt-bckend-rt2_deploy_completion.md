# Deploy Completion Record
**Date opened:** 2026-09-12T05:17:04.599309+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260912T052153Z
**Deploy:** IRPT_BCKEND IB-rt-2 (amendment 6 F3): the LAST root -- irpt-ycharts-generate, which disarms W2-S39 on the final function and puts the v0.14 envelope and the post-read business_date on it
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| Y1 | activation | irpt-ycharts-generate (root .../ycharts). ROLLBACK: restore prior S3 object version, artifact sha VGsTbaPGv70V2l2w8X85z7XK8NEB9hTkbkeDmke1Dt8=, handler entry.lambda_handler unchanged. RIDER NAMED: IB-rt-11's intake/settings.json edit is a declared build input of this function and this apply ships it -- released by amendment 6 F1, whose corrected guard runs ONE way (a zip carrying parse.py must carry both companions) and this zip carries no parse.py. W2-S42 PRE-CONDITION: the root must plan NO destroy line | artifact_sha256 == S3 content-sha256 == live CodeSha256 printed, and a post-apply plan reading No changes | APPLIED. W2-S42 PRE-CONDITION MET WITHOUT A RESTORE: the root planned 'No changes' before the upload, because research_absorbed.tf (IB-rt-9's absorption of the two research resources, added at 244d3a968d) is present at this HEAD and was simply absent from my earlier worktree -- my row mis-attributed the cause and a correcting row is filed. NO DESTROY LINE in any plan of this act; the secret ycharts/session/research-20260911 is untouched and live. Plan after the upload: s3_object_version ikMTp3_AAUhuuYE5y1nxQQMyWUEeNJRW -> ZCNjXlsZ5X4yopqr6tH83SC_GbKOZ3O3 and source_code_hash VGsTbaP... -> CJ6aBh7..., handler entry.lambda_handler UNCHANGED; 0 to add, 1 to change, 0 to destroy -- this cell's packaging and the named rider, nothing else. Apply complete: 0 added, 1 changed, 0 destroyed. CHAIN: built = S3 content-sha256 = live CodeSha256 = CJ6aBh7BWJFcT2Vv0/cJFSXHaH5cs1LvqXvJRfkXHm8=. Post-apply plan: No changes. THIS APPLY CARRIES THE RIDER (IB-rt-11's intake/settings.json) and DISARMS row W2-S39 on the last function. | CLOSED 20260912T052151Z |
| Y1V | verify | irpt-ycharts-generate extract-and-import of the DEPLOYED artifact in the flat /var/task layout, fresh isolated interpreter, repo asserted absent from sys.path, layer mounted per the LIVE function's own attachment | IMPORT-OK + negative control FIRES + three-way hash equality | VERIFIED on SERVED BYTES downloaded from the function's own Code.Location. THREE-WAY CHAIN EQUAL. Extract-and-import in the flat /var/task layout with the layer attachment READ FROM THE LIVE FUNCTION (it attaches none), in a fresh isolated interpreter with the repository ASSERTED absent from sys.path: IMPORT-OK lambda_handler=True. NEGATIVE CONTROL on the same served tree with served.py deleted: IMPORT-FAIL ModuleNotFoundError: No module named 'served'. | CLOSED 20260912T052152Z |

## Log

- 20260912T051704Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 2 leg(s)
- 20260912T052151Z LEG Y1 closed: APPLIED. W2-S42 PRE-CONDITION MET WITHOUT A RESTORE: the root planned 'No changes' before the upload, because research_a
- 20260912T052152Z LEG Y1V closed: VERIFIED on SERVED BYTES downloaded from the function's own Code.Location. THREE-WAY CHAIN EQUAL. Extract-and-import in 
- 20260912T052153Z CLOSED -- all 2 legs proven
