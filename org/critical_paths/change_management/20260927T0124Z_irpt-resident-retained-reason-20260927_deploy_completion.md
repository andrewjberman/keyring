# Deploy Completion Record
**Date opened:** 2026-09-27T01:24:45.658982+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T013100Z
**Deploy:** S151: resident fe64236bbb-h7 -> + ycharts/generate/resident_main.py + ycharts/session/host_capture.py @746ddee18a (~Y's retained-reason patch, 101676): a retained failure names its closed reason; rollback root fe64236bbb-h7 kept
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package on i-0167fd745ad906a66 | SUMS vs fe64236bbb-h7 package: exactly the 2 files + bindings; queue 0/0; controlled stop; install rc 0; unit polls; host sha of the 2 files = 746ddee18a blobs | package fe64236bbb + certify.py @ad817b55ea + resident_main.py/host_capture.py @746ddee18a (build_resident_package --override); SUMS vs the h7 package: exactly the 2 files + bindings; both live blobs == the patch parent (cfe19f8abf, d7048c1e7c); tar 06deb327.. S3 version 0E3xSm1J6Aelk93_Eo2ZdyO1jKOa0G2Q; SSM 379dfb1e: SUMS OK 225, factory OK, queue 0/0 (window 6's message reached the DLQ ~01:27Z), controlled stop 01:29:54Z, install rc 0, unit active MainPID 164491 since 01:29:55Z on /opt/irpt-resident/fe64236bbb-rr, polls 2, 0 tracebacks; running root resident_main 8136387d.. host_capture 885b6d6c.. = 746ddee18a blobs; rollback root fe64236bbb-h7 kept | CLOSED 20260927T013100Z |

## Log

- 20260927T012445Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260927T013100Z LEG R1 closed: package fe64236bbb + certify.py @ad817b55ea + resident_main.py/host_capture.py @746ddee18a (build_resident_package --ove
- 20260927T013100Z CLOSED -- all 1 legs proven
