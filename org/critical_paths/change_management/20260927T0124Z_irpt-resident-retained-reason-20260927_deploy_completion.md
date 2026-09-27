# Deploy Completion Record
**Date opened:** 2026-09-27T01:24:45.658982+00:00
**Status:** OPEN
**Deploy:** S151: resident fe64236bbb-h7 -> + ycharts/generate/resident_main.py + ycharts/session/host_capture.py @746ddee18a (~Y's retained-reason patch, 101676): a retained failure names its closed reason; rollback root fe64236bbb-h7 kept
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package on i-0167fd745ad906a66 | SUMS vs fe64236bbb-h7 package: exactly the 2 files + bindings; queue 0/0; controlled stop; install rc 0; unit polls; host sha of the 2 files = 746ddee18a blobs |  | OPEN |

## Log

- 20260927T012445Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
