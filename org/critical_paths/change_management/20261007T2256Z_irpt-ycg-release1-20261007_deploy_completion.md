# Deploy Completion Record
**Date opened:** 2026-10-07T22:56:15.802381+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T120556Z
**Deploy:** irpt-ycharts-generate release 1: IB-pr-357 (served.py 7cc704) + ~P x3 + ~G2 x2 inert + E-Y4 x14; pin 1b5afe6a49; built ZspX0qD2..; rollback uFTONal.. / S3 objver w031eAfDs6mh..; CTO half d2d2859a2a
**Authored by:** 2.0.0_SA_COO~Y2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-release baseline: live CodeSha256 == S3 objver w031eAfDs6mh content-sha256 == tfstate source_code_hash (uFTONal..); before-key-set of the LIVE zip (after-read 4 before); CloudWatch Errors/Invocations hour-before | three-plane equality + key set + metric numbers | three-plane baseline equal ~23:05Z: live CodeSha256 uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ= (LastModified 2026-10-04T01:57:24Z) == S3 objver w031eAfDs6mh.1ZOCaAks5bHDhKj8ajT content-sha256 uFTONal.. == tfstate source_code_hash uFTONal.. + s3_object_version w031eAfDs6mh..; ROLLBACK SOURCE = that objver. After-read 4 BEFORE (offline, live zip re-hashed uFTONal..): success status keys include internal_correlation_id; refusal keys do not (L1_envelope_keys_before.txt). CloudWatch hour-before 22:05-23:05Z: Errors no datapoint, Invocations no datapoint (0 traffic). | CLOSED 20261007T232118Z |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-ycharts-generate -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | built sha256 == ZspX0qD2.. + new versionId | build-and-upload.sh investor-reporting irpt-ycharts-generate rc=0: import-closure OK (63 .py), SHA256 ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI= (== the signed BUILD_ONLY), s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip new versionId 4Pvl.mN3tY9bIQDDVVnGYFiNoKbrUSTh, content-sha256 metadata ZspX0qD2.. (head-object). Running code unchanged by this leg. | CLOSED 20261007T233356Z |
| L3 | activation | safe-apply of infra/aws/terraform/investor-reporting/ycharts saved plan -target module.irpt_ycharts_generate.aws_lambda_function.this; 0 add 0 destroy | apply output + 0-diff re-plan | dell2 apply (Andrew 106648; grant read back 09:38Z): pre-check live uFTONal.., S3 current 4Pvl.mN3tY9.. content ZspX0qD2..; fresh targeted plan 0 add / 1 change / 0 destroy (s3_object_version w031.. -> 4Pvl.., source_code_hash uFTONal.. -> ZspX0qD2..); .tools/safe-apply.sh: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Live after: CodeSha256 ZspX0qD2bCkFVoi3X8W0cBiPlHY37utqPysuLXMeduI= LastModified 2026-10-08T10:06:18Z Active/Successful. Seat-gate printed WARN-mode STOP on ~G2's open ledger irpt-ycdgen-r6-branch-b2 naming the root (WARN is not a block, msg 1226; this apply touched only the Lambda, not the resident). | CLOSED 20261008T101627Z |
| L4 | verify | after-reads 1-7 of NEVER_WIDEN_PAIR_RELEASE1 + CTO msg 1133 (a) no-token POST refusal envelope lacks internal_correlation_id, (b) CloudWatch hour-after vs hour-before | after-reads file | RELEASE1_AFTER_READS.md (deliverables/2.0.0_SA_COO~Y2/release1_ycg/): 1 deployed zip 0 fixtures/har (100 members, zip re-hashed ZspX0qD2..); 2 laptop fitz relay 431 passed/30 skipped/offline_rc=0 at 1b5afe6a49; 3 zip trace 0 readers, planted control 1 caught; 4 offline AFTER status keys lack internal_correlation_id (BEFORE had it); live no-token POST 401 at the authorizer with no internal id (gateway-level only, stated); 6 import census 62 modules failed={}; 7 deployed == built == S3 4Pvl..; CTO (b) CloudWatch after-hour Errors 0 / Invocations 1 / Throttles 0 vs before no datapoints -> no rollback. After-read 5 = Andrew's F1 retry, read back by ~G2 (CTO msgs 1133/1149); it opens now. Source map recorded at ZspX0qD2.. / 1b5afe6a49 / 10:06:18Z. | CLOSED 20261008T115843Z |

## Log

- 20261007T225615Z OPENED by 2.0.0_SA_COO~Y2 with 4 leg(s)
- 20261007T232118Z LEG L1 closed: three-plane baseline equal ~23:05Z: live CodeSha256 uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ= (LastModified 2026-10-0
- 20261007T233356Z LEG L2 closed: build-and-upload.sh investor-reporting irpt-ycharts-generate rc=0: import-closure OK (63 .py), SHA256 ZspX0qD2bCkFVoi3X8
- 20261008T101627Z LEG L3 closed: dell2 apply (Andrew 106648; grant read back 09:38Z): pre-check live uFTONal.., S3 current 4Pvl.mN3tY9.. content ZspX0qD2
- 20261008T115843Z LEG L4 closed: RELEASE1_AFTER_READS.md (deliverables/2.0.0_SA_COO~Y2/release1_ycg/): 1 deployed zip 0 fixtures/har (100 members, zip re
- 20261008T120556Z CLOSED -- all 4 legs proven
