# Deploy Completion Record
**Date opened:** 2026-09-26T19:00:37.659084+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T193833Z
**Deploy:** IRPT hop 3: ~Y's P_HOP3_SUBMISSION_FIXES to irpt-ycharts-generate (6 rows re-pinned at a219094b1a) and the resident (f624e8a72f + the 6 patched files); CTO 101438/101441
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package on i-0167fd745ad906a66 = f624e8a72f tree + 6 patched files | SSM install rc 0; unit active; IRPT_RESIDENT_POLL lines; manifest sha; rollback root f624e8a72f retained | package fe64236bbb (scratch branch scratch/resident-hop3-20260926 = f624e8a72f + the six hop-3 files byte-copied from a219094b1a; build_resident_package.py 225 members, SHA256SUMS vs a rebuilt f624e8a72f package: exactly the 6 files + resident_bindings.json differ; local import 18/18, recipe SETTINGS_PATH -> intake/settings.json); tar sha256 05ac177e5cf01cbe.. 721276 bytes at s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-ycharts/resident/irpt-resident-fe64236bbb.tar.gz version E.Ia.MwxvaDrgwD0XbQXN1Nr7ZT.fPy2 (an earlier upload carried __pycache__ from a local import check and was superseded by this version before any install). SSM eb5f9c82: staged /opt/irpt-resident/fe64236bbb, host SUMS OK, host manifest df32f57ccca0174f.. (3652 members with pydeps), factory dry run as ec2-user OK (enrolled 1276035), receipt re-bound (prior kept as cutover_receipt.f624e8a72f.json); install-resident.sh refused while the unit was live (rc 3, by design), running unit untouched on f624e8a72f. SSM 9a5444d6: queue 0/0, controlled systemctl stop 19:15:18Z, install rc 0, unit active MainPID 151778 NRestarts 0 since 19:15:19Z on /opt/irpt-resident/fe64236bbb, IRPT_RESIDENT_POLL handled=0 x2, 0 tracebacks; host sha256 of the six = the built package's. Rollback root /opt/irpt-resident/f624e8a72f retained. | CLOSED 20260926T191836Z |
| L1 | activation | irpt-ycharts-generate artifact + apply | census vs deployed 85TXFzzv (exactly 6 members differ); import closure; safe-apply; readback CodeSha256; 0-diff replan | build input: publish worktree irpt-p-publish-20260923 fda155b428 + c982a00fca (the six files from backend a219094b1a); artifact /iFhTAvTZNnhtdhwQPJ+sPPfF67WcMYJY+NE5Fx9XXI= 538004 bytes, S3 version uM1YL.noW5pNrWzZ6osy4mPxss7aPZXC; census against the live 85TXFzzv zip: 111=111 members, exactly the six differ; package_import_check + irpt-common:5 rc 0 (60 .py, 4 named nested allowances, same as the live zip); first build ZxNASliN (CRLF templates.json) never applied; plan 0/1/0 (source_code_hash + s3_object_version); safe-apply 19:33:52Z; readback CodeSha256 /iFhTAvT.. Active/Successful handler generate_installed.lambda_handler layers [irpt-common:5]; DEPLOYED import census {modules 59, failed {}}; invoke {} -> 200 CONTRACT_VERSION before and after; replan -detailed-exitcode 0 No changes; recorder 0d4a44e385 (MSYS-mangled hash corrected) | CLOSED 20260926T193806Z |
| V1 | verify | content proof (CTO 101441) | every patched file in the served generate zip and the resident host root is byte-equal (sha256) to a219094b1a | HOP3_DEPLOYED_CONTENT_PROOF_20260926.md (IRPT_MVP_P): sha256 of the six patched files in the SERVED generate zip (downloaded from get-function after apply) and under the resident unit's running root /opt/irpt-resident/fe64236bbb (SSM 9a5444d6) each equals sha256(git show a219094b1a:<path>): custody_submission e347d1d1.., prospect_submission 2d9e71eb.., recipe a724b653.., recipe_snapshot f71c3a31.., submission 9929a829.., templates.json d10e412f.. -- 6 of 6 in both packages | CLOSED 20260926T193806Z |

## Log

- 20260926T190037Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T191836Z LEG R1 closed: package fe64236bbb (scratch branch scratch/resident-hop3-20260926 = f624e8a72f + the six hop-3 files byte-copied from a2
- 20260926T193806Z LEG L1 closed: build input: publish worktree irpt-p-publish-20260923 fda155b428 + c982a00fca (the six files from backend a219094b1a); a
- 20260926T193806Z LEG V1 closed: HOP3_DEPLOYED_CONTENT_PROOF_20260926.md (IRPT_MVP_P): sha256 of the six patched files in the SERVED generate zip (downlo
- 20260926T193833Z CLOSED -- all 3 legs proven
