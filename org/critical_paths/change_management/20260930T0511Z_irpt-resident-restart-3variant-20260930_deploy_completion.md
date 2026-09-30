# Deploy Completion Record
**Date opened:** 2026-09-30T05:11:18.220748+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T052146Z
**Deploy:** Resident restart for Andrew's ad-hoc three-variant YCharts proof (Andrew-direct 2026-09-30 ~04:4xZ: prove an automated submission per variant and see if we get a generated export). Owner ~Y per Andrew-direct 'the owner of YCharts is COO~Y'. CTO 103150 conditions: auth cause resolved (S230: credential authenticates, rc=0 probe), retained REQ-86f1ce70 re-offered under Andrew's word, restart under a ledger with shas read back.
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | running resident root + worker sha | SSM: systemctl is-active, ps root, sha256 of the running resident_worker.py equal to 8d1f5431 and to CLOUD HEAD | Read back by SSM at 05:1xZ: systemctl is-active = inactive; the unit file's ExecStart root is fe64236bbb-st5; sha256 of /opt/irpt-resident/fe64236bbb-st5/ycharts/generate/resident_worker.py = 8d1f5431276e406cbc679c67c5b7cc38edf70dadda906f055b72f3b47744d07a, EQUAL to CLOUD HEAD's sha256 for the same path (computed from git show HEAD:...). So the root that will run is the gated st5 bytes and the repo agrees. CTO 103150's 'shas read back' condition met. | CLOSED 20260930T051248Z |
| D1 | activation | systemctl start irpt-analysis-resident | unit active, polls observed, 0 Tracebacks | Started 05:13:31Z under SSM. Unit active; pid 313525 running the gated st5 root (sha 8d1f5431 = CLOUD HEAD per leg V1). 0 Tracebacks. First poll 05:13:32Z picked up retained REQ-86f1ce70 and refused it: class=CurrentAuthorityRefused code=ACTOR_NOT_FOUND. The restart is proven; the job's failure is a separate cause on leg V2. | CLOSED 20260930T051533Z |
| V2 | verify | OVERVIEW variant live via REQ-86f1ce70 | irpt-jobs terminal state by name + the resident journal's eviction/attention lines for the span | OVERVIEW variant NOT obtained, and the cause is measured rather than inferred. irpt-jobs REQ-86f1ce70 holds SUBMITTING; the resident's first poll after the 05:13:31Z start refused it class=CurrentAuthorityRefused code=ACTOR_NOT_FOUND. Source: current_authority.py:86 refuses when the projected profile row for the accepted record's owner.principal_id is absent, and that principal (irpt-uiwalk-1790739020@opal.test) was deleted at 03:45:34Z. The refusal precedes any session capture or report POST, so no YCharts call was spent; DLQ re-read 1, unchanged. Row IRPT_BCKEND-S231 records the structural finding: principal lifetime is window-scoped while job lifetime is queue-scoped, so a job that outlives its window can never run. The restart itself is proven (legs V1, D1); this leg's outcome is a NAMED negative, not an unknown. | CLOSED 20260930T052051Z |

## Log

- 20260930T051118Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20260930T051248Z LEG V1 closed: Read back by SSM at 05:1xZ: systemctl is-active = inactive; the unit file's ExecStart root is fe64236bbb-st5; sha256 of 
- 20260930T051533Z LEG D1 closed: Started 05:13:31Z under SSM. Unit active; pid 313525 running the gated st5 root (sha 8d1f5431 = CLOUD HEAD per leg V1). 
- 20260930T052051Z LEG V2 closed: OVERVIEW variant NOT obtained, and the cause is measured rather than inferred. irpt-jobs REQ-86f1ce70 holds SUBMITTING; 
- 20260930T052146Z CLOSED -- all 3 legs proven
