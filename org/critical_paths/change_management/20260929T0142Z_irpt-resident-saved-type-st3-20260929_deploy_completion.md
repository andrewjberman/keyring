# Deploy Completion Record
**Date opened:** 2026-09-29T01:42:08.640310+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T025120Z
**Deploy:** Resident st2 -> st3: recipe.py + resident_worker.py @ec8f69f718 (TO-IB-yr-1, a saved portfolio type other than fixed refuses a tolerated setting before generation); ~Y 102524; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | resident package st3 upload | SUMS vs st2: only recipe.py, resident_worker.py + bindings; tar sha; S3 VersionId; install script sha checks | build_resident_package.py --pin fe64236bbb with st2's 12 overrides, recipe.py + resident_worker.py re-pinned 12a67ed5ee -> ec8f69f718 (git diff 12a67ed5ee..ec8f69f718 on the two = 7+/1-, the TO-IB-yr-1 change only); SHA256SUMS vs st2 (read from the S3 st2 tar, provenance read from its bindings): 225/225, differ recipe.py (982d8171 -> 4fde9ac9), resident_worker.py (9b2dbd18 -> 95f79dad) and resident_bindings.json ONLY; manifest 952a183d; tar 266 members = st2's 266; tar sha 26769a37.. uploaded ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st3.tar.gz VersionId vDS2rcSqdOEi90kjFAV5oadXrF7hlHSP, read back by version sha == 26769a37; install script resident_host_install_st3_20260929.sh (st2's with NEW/OLD/KEY/tar/recipe/worker shas and receipt ledger changed only; bash -n OK; sha 87c70e76). | CLOSED 20260929T014626Z |
| D1 | activation | resident install st2 -> st3 | halves at HEAD; ~Y gates on built st3; queue 0/0; install rc 0; polls; running root + member shas read back | Both halves at HEAD naming blob 17661cbe: CTO @2b3fc1c1a3 (102535), CRO @a80bf5ac96 (102551); ~Y four gates on built st3 recorded before the run (@0f331f6c22; ~Y 102543 @415701c935). SSM add63ec1-75b8-4fd0-b841-e60e258e39d9 (script resident_host_install_st3_20260929.sh sha 87c70e76, committed 03cccc5a37) Success rc 0. LIVE BEFORE-READ (script line 1): active=active root=/opt/irpt-resident/fe64236bbb-st2; queue visible/in-flight 0/0. tar sha 26769a37 OK, SHA256SUMS OK 225, all 10 member shas checked, factory OK on resident_main.py's own sys.path (enrolled 1276035), controlled stop, install fe64236bbb-st3 rc 0, active=active polls_30s=2 tracebacks_30s=0, MainPID 261514 since 02:49:20Z, NRestarts 0. RUNNING ROOT READ BACK (systemctl ExecStart): /opt/irpt-resident/fe64236bbb-st3; recipe.py 4fde9ac9, resident_worker.py 95f79dad (== ec8f69f718), broker 3d490d6d, capture 5170522c, main 0e5c17e7 unchanged. Rollback root fe64236bbb-st2 kept; receipt copied to cutover_receipt.fe64236bbb-st2.json. Live behaviour proof (a saved non-fixed type with a tolerated row -> ATTENTION TOLERANCE_REQUIRES_STATIC) rides window 21's Analysis bodies. | CLOSED 20260929T025054Z |

## Log

- 20260929T014208Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260929T014626Z LEG U1 closed: build_resident_package.py --pin fe64236bbb with st2's 12 overrides, recipe.py + resident_worker.py re-pinned 12a67ed5ee 
- 20260929T025054Z LEG D1 closed: Both halves at HEAD naming blob 17661cbe: CTO @2b3fc1c1a3 (102535), CRO @a80bf5ac96 (102551); ~Y four gates on built st3
- 20260929T025120Z CLOSED -- all 2 legs proven
