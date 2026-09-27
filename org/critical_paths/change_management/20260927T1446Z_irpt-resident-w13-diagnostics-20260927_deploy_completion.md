# Deploy Completion Record
**Date opened:** 2026-09-27T14:46:15.469964+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T145200Z
**Deploy:** resident fe64236bbb-cw -> fe64236bbb-dx: ~Y's W13 diagnostics (ec5804f6e0: resident_main, resident_worker, session/host_capture -- the journal names the stored drifted value and the capture's runner reason), ~Y 101915 on CTO 101897's resident terms; queue 0/0; rollback root cw kept
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package fe64236bbb-dx | SUMS vs cw = exactly resident_main.py + resident_worker.py + host_capture.py + bindings; live blobs == patch parent; queue 0/0; controlled stop; install rc 0; polls; host sha of the three == ec5804f6e0 blobs | package fe64236bbb + certify@ad817b55ea + request_composition@f8c72944f3 + broker@e2fdd01015 + recipe@b6739556ea + resident_main.py/resident_worker.py/session/host_capture.py@ec5804f6e0 (enrolled 1276035); SUMS vs the cw package (225/225) = resident_main.py (8136387d -> 0e5c17e7) + resident_worker.py (d54bd0e5 -> 3c41980c) + host_capture.py (2905c73b -> 5170522c) + bindings only; the three live cw blobs == the patch parent (ec5804f6e0^); OPEN committed @aca63a1565 BEFORE the upload; tar fb42a111.. S3 version ZzrMOD5wxtRTeP0xsFiBBzVq2XSflg9O. ATTEMPT 1 (SSM c948f574, 14:47Z): SUMS OK, factory OK, queue 0/0, controlled stop, install-resident.sh rc=7 (stderr: curl (7) Failed to connect to 169.254.169.254 port 80 -- the instance metadata endpoint, transient) -> the script's own ROLLBACK to cw, rollback install rc 0, active MainPID 191611 on cw with cw's hashes, 0 tracebacks (no served gap beyond the stop/start; the queue was 0/0 throughout). ATTEMPT 2 (SSM a55aab20, same command): install rc 0, active MainPID 191849 since 14:50:22Z on /opt/irpt-resident/fe64236bbb-dx, polls 2 in 30 s, 0 tracebacks, NRestarts 0; host resident_main 0e5c17e7.., resident_worker 3c41980c.., host_capture 5170522c.. = the ec5804f6e0 blobs; recipe 5224b224 and broker 3d490d6d unchanged; rollback root cw kept. Tests on ec5804f6e0: 380 passed, 30 skipped. | CLOSED 20260927T145200Z |

## Log

- 20260927T144615Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260927T145200Z LEG R1 closed: package fe64236bbb + certify@ad817b55ea + request_composition@f8c72944f3 + broker@e2fdd01015 + recipe@b6739556ea + resid
- 20260927T145200Z CLOSED -- all 1 legs proven
