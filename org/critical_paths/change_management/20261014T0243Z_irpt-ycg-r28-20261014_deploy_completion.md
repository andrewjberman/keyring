# Deploy Completion Record
**Date opened:** 2026-10-14T02:43:27.106382+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R28c leg L3: irpt-ycharts-generate (the upload door): template_reader.py r19.3, portfolio.py, uploads.py, security_resolution.py moved and trading_calendar.py ADDED at the package root, to CodeSha256 reAjAQOV..; pair COO blob e9bb20d7fe + CTO half @d3adae2fc8; starts only after the ~IB2 ledger read CLOSED and L4 closed
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | COO half hash; ~IB2 ledger CLOSED at HEAD (per tree); L4 closed by the COO message; census (no open entry naming irpt-ycharts-generate); R0b live CodeSha256 xP47NQDn.., key latest VXbWnMBm.., object hash; G3 and G4 before | reads printed |  | OPEN |
| L2 | s3-prefix | detached worktree at 0c0ae5a8f5 (core.longpaths), guard printed, ycharts_release_input.diff d80f656489 applied uncommitted with --unidiff-zero, BUILD_ONLY digest equals reAjAQOVVfD4Wui2u0UfZRt7cr9o6ioFKIwXa+8EVgc=, then upload, read back equals the staged zip ade023010395 | digest, VersionId, readback |  | OPEN |
| L3 | verify | scoped plan -target=module.irpt_ycharts_generate.aws_lambda_function.this from infra/aws/terraform/investor-reporting/ycharts: 0 add 1 change 0 destroy, last_modified s3_object_version source_code_hash only | plan summary and attributes |  | OPEN |
| L4 | activation | safe-apply on the saved plan | Apply complete 0/1/0 |  | OPEN |
| L5 | verify | G1 CodeSha256 reAjAQOV..; G2 105 members, four differ, calendar added; G3 refusal envelope equals before; G4 environment and role unchanged | G1-G4 |  | OPEN |
| L6 | git | four pin moves with sha256, trading_calendar.py row and its files[] entry, plus artifact_* and last_deployed_* applied to the trunk map in own worktree; commit | commit hash |  | OPEN |

## Log

- 20261014T024327Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
