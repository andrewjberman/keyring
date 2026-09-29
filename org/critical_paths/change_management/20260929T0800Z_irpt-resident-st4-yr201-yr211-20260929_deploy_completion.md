# Deploy Completion Record
**Date opened:** 2026-09-29T08:00:28.432331+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T123158Z
**Deploy:** Resident st3 -> st4: recipe.py + resident_worker.py @14c961af32 (IB-yr-201 S194: a Comparison sends its models and refuses a PDF printing none; IB-yr-211 S193: a resolve RETRY is logged and re-offered in 60 s); ~Y 102630/102647; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | resident package st4 upload | SUMS vs st3: only recipe.py, resident_worker.py + bindings; tar sha; S3 VersionId; install script | build_resident_package.py --pin fe64236bbb with st3's 12 overrides, recipe.py + resident_worker.py re-pinned ec8f69f718 -> 14c961af32 (IB-yr-201 @f287444013 + IB-yr-211, drained by ~Y; ~Y 102647). SHA256SUMS vs st3: 225/225, differ recipe.py (4fde9ac9 -> b2fbd720), resident_worker.py (95f79dad -> 0b67be2a) and resident_bindings.json ONLY; tar 266 members = st3's; tar sha 7d10152c.. uploaded ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st4.tar.gz VersionId jK0FFkzC_Oc8m3mZMiatYrPCpuyOc9ZE, read back by version sha equal. Install script resident_host_install_st4_20260929.sh = st3's with NEW/OLD/KEY/tar/recipe/worker shas and receipt ledger changed only; bash -n OK. | CLOSED 20260929T081244Z |
| D1 | activation | resident install st3 -> st4 | halves at HEAD; ~Y gates on built st4; queue 0/0; install rc 0; polls; running root + member shas | U1 RE-PROOF for the rebuilt tar: S3 ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st4.tar.gz latest VersionId ekqvI5um7gQQ0vY4.FrprYd0vwEA5Q4U sha256 63a5e26a (226 members incl. SUMS; vs st3 only recipe.py-unchanged-bytes, resident_worker.py 5288ff5a from 0357fc7e08, bindings provenance -- ~Y ST4B gates @a6caedc4ed PASS). Halves at HEAD on the delta: CTO 102786 (SIGNOFF_RESIDENT_ST4_20260929.md last section), CRO 102791 (addendum 1 @a8938b35e7), bound to install script blob 26d1891ddc @53d0cc466b (sha256 c2283359). Queue 0/0 read 12:30Z. SSM 2bcd0fad-96b1-4f4f-a10f-37f9b621dbff Success rc 0 at 12:30:47Z: before active root fe64236bbb-st3; SHA256SUMS OK 225; factory OK (enrolled 1276035); queue 0/0; install fe64236bbb-st4 rc 0; active polls_30s=2 tracebacks_30s=0; MainPID 280258 since 12:31:13Z, NRestarts 0. RUNNING ROOT (ExecStart): /opt/irpt-resident/fe64236bbb-st4; recipe b2fbd720, resident_worker 5288ff5a, broker 3d490d6d, capture 5170522c, main 0e5c17e7. Rollback root fe64236bbb-st3 kept. CRO condition 3 (the first Analysis window reads the named stops) carried to that window. The REQ-3a1b73a8 row settle is NOT in this act (no half names it). | CLOSED 20260929T123158Z |

## Log

- 20260929T080028Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260929T081244Z LEG U1 closed: build_resident_package.py --pin fe64236bbb with st3's 12 overrides, recipe.py + resident_worker.py re-pinned ec8f69f718 
- 20260929T123158Z LEG D1 closed: U1 RE-PROOF for the rebuilt tar: S3 ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st4.tar.gz latest Version
- 20260929T123158Z CLOSED -- all 2 legs proven
