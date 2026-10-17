# Deploy Completion Record
**Date opened:** 2026-10-17T16:27:00.874501+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T165756Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R36S: irpt-status release r36S (acceptance.py gains get_commentary_ref) at pin ae2ab2072b: build and upload (U), scoped Terraform apply of the function code (C), after-reads G1-G6 (V); COO half blob b659221aa1, CTO half c9789c47f5
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | the irpt-status package built at the pin and uploaded as the new latest version of investor-reporting/irpt-status.zip | digest equal to the expected CodeSha256, object read back sha256 dbbe1d97 | irpt-status package built at the pin ae2ab2072b (BUILD_ONLY digest 274dl2bC.. equal first), uploaded 2026-10-17T16:37:49Z as version 5Uqt.3DqL8QHzaOKv0clIZ14XADNH7ZD, object read back sha256 dbbe1d97.. equal; previous latest vP3Bt0tM.. kept | CLOSED 20261017T165755Z |
| C | activation | scoped plan 0/1/0 at module.irpt_status.aws_lambda_function.this then safe-apply | plan counts and the live CodeSha256 274dl2bC | scoped plan 0 add 1 change 0 destroy (last_modified, s3_object_version, source_code_hash only); one safe-apply 2026-10-17T16:41:14Z: Apply complete 0 added 1 changed 0 destroyed; live CodeSha256 274dl2bC.. | CLOSED 20261017T165755Z |
| V | verify | after-reads G1 to G6, the record A_AFTER_R36S.txt and the function-map record | the G1-G6 lines | G1 CodeSha256 equal; G2 acceptance.py only, 49 of 49; G3 refusal 401 sha equal; G4 READY read byte-identical; G5 NOT MADE (issuer AMENDMENT 1: the commentary PDF artifact is not retained for any request); G6 changed_members 0; viewer row removed, ABSENT GSI and CONSISTENT; record A_AFTER_R36S.txt; map record in the following commit | CLOSED 20261017T165755Z |

## Log

- 20261017T162700Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
- 20261017T165755Z LEG U closed: irpt-status package built at the pin ae2ab2072b (BUILD_ONLY digest 274dl2bC.. equal first), uploaded 2026-10-17T16:37:49
- 20261017T165755Z LEG C closed: scoped plan 0 add 1 change 0 destroy (last_modified, s3_object_version, source_code_hash only); one safe-apply 2026-10-1
- 20261017T165755Z LEG V closed: G1 CodeSha256 equal; G2 acceptance.py only, 49 of 49; G3 refusal 401 sha equal; G4 READY read byte-identical; G5 NOT MAD
- 20261017T165756Z CLOSED -- all 3 legs proven
