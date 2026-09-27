# Deploy Completion Record
**Date opened:** 2026-09-27T15:49:43.409438+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T155338Z
**Deploy:** resident fe64236bbb-rs -> fe64236bbb-lt: ~Y's read-back tolerates level_as_of_type (49b85eacd2: recipe, resident_worker -- records the stored value, refuses on absence or any other drift), ~Y 101938 on CTO 101897/101929's resident terms; queue 0/0; rollback root rs kept; named in the window-15 packet
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package fe64236bbb-lt | SUMS vs rs = exactly recipe.py + resident_worker.py + bindings; live blobs == patch parent; queue 0/0; controlled stop; install rc 0; polls; host sha of the two == 49b85eacd2 blobs | package = rs + recipe.py/resident_worker.py@49b85eacd2 (enrolled 1276035); SUMS vs the rs package (225/225) = recipe.py (e90503c5 -> 339e0c0e) + resident_worker.py (f770de7c -> 388f6e7f) + bindings only; the two live rs blobs == the patch parent (49b85eacd2^); OPEN committed @db9a741c1b BEFORE the upload; tar ae854f00.. S3 version xOjZ.7lxDeZGr22kgr_DtgwdHb5gdX4p; SSM 1f3e6c68: SUMS OK, factory OK, queue 0/0, controlled stop, install rc 0, active MainPID 194244 since 15:51:47Z on /opt/irpt-resident/fe64236bbb-lt, polls 2, 0 tracebacks, NRestarts 0; host recipe 339e0c0e.., worker 388f6e7f.. = the 49b85eacd2 blobs; broker/capture/main unchanged; rollback root fe64236bbb-rs kept. Tests on 49b85eacd2: 383 passed, 30 skipped. The live proof is window 15's K5. | CLOSED 20260927T155338Z |

## Log

- 20260927T154943Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260927T155338Z LEG R1 closed: package = rs + recipe.py/resident_worker.py@49b85eacd2 (enrolled 1276035); SUMS vs the rs package (225/225) = recipe.py 
- 20260927T155338Z CLOSED -- all 1 legs proven
