# Deploy Completion Record
**Date opened:** 2026-09-27T05:51:10.770456+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T055524Z
**Deploy:** resident fe64236bbb-rb -> fe64236bbb-wf: ~Y's read-back WAF refresh (e2fdd01015: recipe.py, resident_worker.py, session/broker.py), CTO 101792 (c); queue 0/0 required; rollback root rb kept
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package fe64236bbb-wf | SUMS vs rb = exactly recipe.py + resident_worker.py + broker.py + bindings; live blobs == patch parent; queue 0/0; controlled stop; install rc 0; polls; host sha of the three == e2fdd01015 blobs | package fe64236bbb + certify@ad817b55ea + resident_main/host_capture@746ddee18a + request_composition@f8c72944f3 + recipe.py/resident_worker.py/session/broker.py@e2fdd01015 (enrolled 1276035); SUMS vs the rb package (225/225) = recipe.py (4430d657 -> b5cf6796) + resident_worker.py (36bd06bd -> 57f785b2) + broker.py (a4b60a13 -> 3d490d6d) + bindings only; the three live rb blobs == the patch parent (e2fdd01015^); tar dbc350dd.. S3 version 5miIvw4OZTpU.. (uploaded before the OPEN commit f57a08f106 -- a staging act, recorded); SSM 5e781d0f: SUMS OK 225, factory OK, queue 0/0, controlled stop, install rc 0, active MainPID 173870 since 05:54:14Z on /opt/irpt-resident/fe64236bbb-wf, polls 2 in 30 s, 0 tracebacks, NRestarts 0; host recipe b5cf6796.., worker 57f785b2.., broker 3d490d6d.. = e2fdd01015 blobs; rollback root fe64236bbb-rb kept. generate keeps its own recipe.py/broker.py (the Lambda never runs the resident read-back; CTO 101792 scoped the resident). | CLOSED 20260927T055523Z |
| V1 | verify | offline proof on the built package | ~Y's window-8 live shape through the wf package's modules reaches READY with one re-capture; the rb package goes ATTENTION | content identity to ~Y's proof (LIVE_WINDOW8_EVIDENCE_20260927.md @141a45d087: window 8's live shape ATTENTION on rb, READY with one re-capture on rb + the patch overlay): the host's resident_worker.py and broker.py are byte-identical to Y branch 4aaeaea3d5 (57f785b2, 3d490d6d); recipe.py differs from 4aaeaea3d5 ONLY by the served hop-3 packaged-settings fallback (SETTINGS_PATH, lines 62-67), which rb already carries and ~Y's overlay-on-rb proof ran with. Unit suites on e2fdd01015: ycharts generate + session 375 passed, 30 skipped. The live proof is the next Analysis window's K5 (needs Andrew's word). | CLOSED 20260927T055524Z |

## Log

- 20260927T055110Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260927T055523Z LEG R1 closed: package fe64236bbb + certify@ad817b55ea + resident_main/host_capture@746ddee18a + request_composition@f8c72944f3 + recip
- 20260927T055524Z LEG V1 closed: content identity to ~Y's proof (LIVE_WINDOW8_EVIDENCE_20260927.md @141a45d087: window 8's live shape ATTENTION on rb, RE
- 20260927T055524Z CLOSED -- all 2 legs proven
