# Deploy Completion Record
**Date opened:** 2026-09-27T03:39:47.771421+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T034303Z
**Deploy:** Window-7 read-back fix: resident fe64236bbb-xv -> fe64236bbb-rb (+ ycharts/generate/recipe.py + resident_worker.py @07f1982ab9, ~Y P_READ_BACK_POLL; CTO 101763); rollback root xv
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package fe64236bbb-rb | SUMS vs xv package: exactly recipe.py + resident_worker.py + bindings; queue 0/0; controlled stop; install rc 0; polls; host sha of both = 07f1982ab9 blobs | package fe64236bbb + certify@ad817b55ea + resident_main/host_capture@746ddee18a + request_composition@f8c72944f3 + recipe.py/resident_worker.py@07f1982ab9; SUMS vs the xv package = recipe.py (a724b653 -> 4430d657) + resident_worker.py (2dcd8c05 -> 36bd06bd) + bindings only; both live blobs == the patch parent (f18ab75765, 09bd768850); tar 4c29466d.. S3 version 67AKp7l7ZZPCwPVq6lRZWogcXiSf6W7C; SSM 565fb9f3: SUMS OK, factory OK, queue 0/0, controlled stop, install rc 0, active MainPID 169439 since 03:41:53Z on /opt/irpt-resident/fe64236bbb-rb, polls 2, 0 tracebacks; host recipe 4430d657.., worker 36bd06bd.. = 07f1982ab9 blobs; rollback root fe64236bbb-xv kept. generate keeps its recipe.py (never calls step_read_back; CTO 101763 scoped the resident) | CLOSED 20260927T034303Z |

## Log

- 20260927T033947Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260927T034303Z LEG R1 closed: package fe64236bbb + certify@ad817b55ea + resident_main/host_capture@746ddee18a + request_composition@f8c72944f3 + recip
- 20260927T034303Z CLOSED -- all 1 legs proven
