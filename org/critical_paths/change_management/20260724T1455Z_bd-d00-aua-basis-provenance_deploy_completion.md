# Deploy Completion Record
**Date opened:** 2026-07-24T14:55:42.408466+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260724T145543Z
**Deploy:** D_00 served-AUA basis provenance -- kill the 2026-08-01 silent -$99.1mm cliff (CTO gate 135247Z + item-5 amendment 141355Z)
**Authored by:** 0.4.0_DS_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit f204e97cb pushed to origin/CLOUD | commit hash on origin | f204e97cb on origin/CLOUD (git branch -r --contains -> origin/CLOUD) | CLOSED 20260724T145542Z |
| L2 | s3-prefix | opal-data-bd code/gold/D_00.portal_aggregates.py | comp-pipescript deployed MATCH line | comp-pipescript deployed -> '[bd-gold] D_00 MATCH D_00.portal_aggregates.py' (Summary 4 MATCH, 0 STALE, 0 AUX-DRIFT) on s3://opal-data-bd/code/gold/, landed 2026-07-24T14:51:57Z via the safe-deploy pre-push hook (not a hand cp) | CLOSED 20260724T145543Z |
| L3 | verify | SERVED bytes download+import expose ServedAUA/provenance API | md5 tie + import of the downloaded served object | SERVED object downloaded from s3://opal-data-bd/code/gold/D_00.portal_aggregates.py: md5 8fe11a9dd113a20f575819eb278e99ce == local HEAD md5 == S3 ETag, 61563 B. Imported via importlib exec_module from the DOWNLOADED bytes: IMPORT OK; ServedAUA fields ('value','basis','cert_data_as_of','held_days','hold_reason','alternative'); AUA_CERT_PREFIX resolves to gold/validation/aua_certification/ (the tree the GET actually reads, derived not hardcoded); _aua_provenance_block callable; smoke on a fresh cert returns basis='certified' held_days=0. RESIDUAL STATED: import exercised under local python3.12, runner is python3.11; ruff py39 gate passed so syntax is 3.9-compatible, but a 3.11 import ON THE BOX is NOT claimed. NO ad-hoc gold run (NEVER#4) -- the next SCHEDULED run is the first artifact exercise, and 0.6.2~A verifies on the served artifact per SoD. | CLOSED 20260724T145543Z |

## Log

- 20260724T145542Z OPENED by 0.4.0_DS_ClientPlatform with 3 leg(s)
- 20260724T145542Z LEG L1 closed: f204e97cb on origin/CLOUD (git branch -r --contains -> origin/CLOUD)
- 20260724T145543Z LEG L2 closed: comp-pipescript deployed -> '[bd-gold] D_00 MATCH D_00.portal_aggregates.py' (Summary 4 MATCH, 0 STALE, 0 AUX-DRIFT) on 
- 20260724T145543Z LEG L3 closed: SERVED object downloaded from s3://opal-data-bd/code/gold/D_00.portal_aggregates.py: md5 8fe11a9dd113a20f575819eb278e99c
- 20260724T145543Z CLOSED -- all 3 legs proven
