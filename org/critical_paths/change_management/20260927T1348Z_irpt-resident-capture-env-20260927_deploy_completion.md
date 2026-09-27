# Deploy Completion Record
**Date opened:** 2026-09-27T13:48:20.219028+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T135230Z
**Deploy:** resident fe64236bbb-wf -> fe64236bbb-cw: ~Y's W11 fixes (b6739556ea: session/host_capture capture_env strips PYTHON*, recipe/resident_worker read-back reads the saved portfolio after available), CTO 101897; queue 0/0 required; rollback root wf kept
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package fe64236bbb-cw | SUMS vs wf = exactly recipe.py + resident_worker.py + host_capture.py + bindings; live blobs == patch parent; queue 0/0; controlled stop; install rc 0; polls; host sha of the three == b6739556ea blobs | package fe64236bbb + certify@ad817b55ea + resident_main@746ddee18a + request_composition@f8c72944f3 + broker@e2fdd01015 + recipe.py/resident_worker.py/session/host_capture.py@b6739556ea (enrolled 1276035); SUMS vs the wf package (225/225) = recipe.py (b5cf6796 -> 5224b224) + resident_worker.py (57f785b2 -> d54bd0e5) + host_capture.py (885b6d6c -> 2905c73b) + bindings only; the three live wf blobs == the patch parent (b6739556ea^); OPEN committed @f58e5562ab BEFORE the upload; tar 32e1122a.. S3 version uSKOEt2zvJxZrSS2S.gd2JL4EgfytfM9; SSM 0a240da6: SUMS OK 225, factory OK, queue 0/0, controlled stop, install rc 0, active MainPID 189222 since 13:51:07Z on /opt/irpt-resident/fe64236bbb-cw, polls 2 in 30 s, 0 tracebacks, NRestarts 0; host recipe 5224b224.., worker d54bd0e5.., broker 3d490d6d.., capture 2905c73b.. = the committed blobs; rollback root fe64236bbb-wf kept. Tests on b6739556ea: ycharts generate + session 378 passed, 30 skipped. The live proof is window 13's K5. | CLOSED 20260927T135230Z |

## Log

- 20260927T134820Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260927T135230Z LEG R1 closed: package fe64236bbb + certify@ad817b55ea + resident_main@746ddee18a + request_composition@f8c72944f3 + broker@e2fdd01015 
- 20260927T135230Z CLOSED -- all 1 legs proven
