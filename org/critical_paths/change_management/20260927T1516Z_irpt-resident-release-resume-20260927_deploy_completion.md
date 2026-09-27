# Deploy Completion Record
**Date opened:** 2026-09-27T15:16:56.546708+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T152015Z
**Deploy:** resident fe64236bbb-dx -> fe64236bbb-rs: ~Y's read-back release-and-resume (38ee23deaa: recipe, resident_worker -- 2 status GETs per receive, calculating/WAF read raises ReadBackPending, no read re-capture), CTO 101929; queue 0/0; rollback root dx kept
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package fe64236bbb-rs | SUMS vs dx = exactly recipe.py + resident_worker.py + bindings; live blobs == patch parent; queue 0/0; controlled stop; install rc 0; polls; host sha of the two == 38ee23deaa blobs | package fe64236bbb + certify@ad817b55ea + request_composition@f8c72944f3 + broker@e2fdd01015 + resident_main/host_capture@ec5804f6e0 + recipe.py/resident_worker.py@38ee23deaa (enrolled 1276035); SUMS vs the dx package (225/225) = recipe.py (5224b224 -> e90503c5) + resident_worker.py (3c41980c -> f770de7c) + bindings only; the two live dx blobs == the patch parent (38ee23deaa^); OPEN committed @354adb646c BEFORE the upload; tar 0b628d36.. S3 version uG_ZGptMLQzXiTO8bwGKtlMRHK2Yw25W; SSM 266ac6cf: SUMS OK, factory OK, queue 0/0, controlled stop, install rc 0, active MainPID 192953 since 15:18:44Z on /opt/irpt-resident/fe64236bbb-rs, polls 2 in 30 s, 0 tracebacks, NRestarts 0; host recipe e90503c5.., worker f770de7c.. = the 38ee23deaa blobs; broker/capture/main unchanged; rollback root fe64236bbb-dx kept. Tests on 38ee23deaa: 381 passed, 30 skipped. The live proof is window 15's K5. | CLOSED 20260927T152014Z |

## Log

- 20260927T151656Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260927T152014Z LEG R1 closed: package fe64236bbb + certify@ad817b55ea + request_composition@f8c72944f3 + broker@e2fdd01015 + resident_main/host_captur
- 20260927T152015Z CLOSED -- all 1 legs proven
