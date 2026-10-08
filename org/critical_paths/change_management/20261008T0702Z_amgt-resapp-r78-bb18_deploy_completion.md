# Deploy Completion Record
**Date opened:** 2026-10-08T07:02:23.648579+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 78 AMGT-bb-18: the code redeploy of opal-amgt-scoped-api at the pin fbb643923e (the adapter's six hookups + the dossier reader to method 7); base CodeSha256 MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg=, artifact VersionId VHwcuot4i70V2evVL44EBgQc0BcAtScd; rollback = the kept zip C:/tmp/ba20-r77-14a36147bd.zip through the module, one code-only safe-apply, never an S3 delete
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the artifact is built from a DETACHED worktree at EXACTLY fbb643923e9ab3db14aa8d8062fa9015a6722690, --build-only to a kept path, PIP_NO_INDEX=1 + PIP_FIND_LINKS=C:/tmp/bb18-wheels + AMGT_DEPLOYED_ZIP=C:/tmp/ba20-r77-14a36147bd.zip | the kept zip's path and its sha256 in base64, the pin hash, and the PIP_LOG showing 0 index requests |  | OPEN |
| L2 | verify | the two pre-upload gates: r78_bb23.py --compare-zip reads EQUAL YES 147 of 147, and the CONTENT-DIFF reads CHANGED 22 / ADDED 8 / REMOVED 0 with the three dist-info RECORD files shown sorted-line-equal (43, 19, 5) | the printed compare-zip line, the content-diff counts, and the 3 of 3 sorted-line equality with line counts |  | OPEN |
| L3 | s3-prefix | upload_verified.sh puts THAT kept zip on s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip | the new VersionId and the content-sha256 metadata equal to the kept zip's sha256 |  | OPEN |
| L4 | activation | ONE safe-apply on infra/aws/terraform/harvest/, plan graded UNTARGETED and showing exactly ONE in-place update of the function's code; memory stays 1769 | the plan's one-resource line, then a 0-diff re-plan, and a live CodeSha256 that differs from MkM9Kf37 and equals the kept zip's |  | OPEN |
| L5 | verify | ONE direct invoke of the snapshot's scheduled event {amgt_scheduled_action: refresh_freshness_snapshot} written by the new code | the stamp, and a NEW VersionId at the same snapshot key with 302 rows (rollback = copy-object of GyD7kjRk9hcHp4npg3vtTFiEOpz8QHGL, never a delete) |  | OPEN |
| L6 | verify | AC1 (R78 DEPLOYED YES 3 of 3), AC2 (r76 c62/c63 and r75 c59 on the deployed function) and AC3 (r77 served shape, no regression) | each criterion's own output lines and exit code |  | OPEN |

## Log

- 20261008T070223Z OPENED by 0.7.0_AE_CloudOps~A with 6 leg(s)
