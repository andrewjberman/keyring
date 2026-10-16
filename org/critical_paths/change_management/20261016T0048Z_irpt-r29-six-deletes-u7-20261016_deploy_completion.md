# Deploy Completion Record
**Date opened:** 2026-10-16T00:48:02.463162+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T012913Z
**Deploy:** IRPT_ANLREQ row 2106: delete every version of the six R29-written synthetic keys (opal-data-irpt intake store), by VersionId, nothing else. NOT RECOVERABLE. AUTHORITY: Andrew word at the terminal 'delete' 2026-10-16, on Andrew's recorded 'have the laptop box handle' (record @cf8764df23 on box/dell2, CTO msg 109528); list: org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r29/OBJECTS_WRITTEN_R29.txt. PRINCIPAL: Andrew_Berman. Bounds: the six keys only, no prefix delete, no lifecycle or policy change.
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L | verify | simulator, open-deploy census, per-key list-object-versions | decision, denominators and the selection printed | SUPERSEDED-WORLD-DONE: measured 2026-10-16T01:2xZ by 1.0.0_SA_CTO after the laptop reboot killed U7 (not registered). Per-key list-object-versions on the 6 OBJ lines of OBJECTS_WRITTEN_R29.txt: 6 of 6 read V=0 M=0. Positive control same call on parent prefixes: normalized_portfolios V=11, original_holdings V=19, request_compositions V=13 (49financial total V=293 M=0). Simulator not re-run: nothing left to act on. | CLOSED 20261016T012913Z |
| D | s3-prefix | delete each listed version of the six keys by VersionId | each call result printed, deleted equals versions before | SUPERSEDED-WORLD-DONE: the deleting session's call output did not survive the reboot, so per-call results are UNREAD. Measured instead: each key held exactly 1 listed version at R29 (VersionIds in OBJECTS_WRITTEN_R29.txt) and holds 0 versions and 0 delete markers now; deleted (1 each) equals versions before (1 each), 6 of 6. No re-execution. | CLOSED 20261016T012913Z |
| R | verify | head-object 404 and list-object-versions 0 versions 0 markers per key within a bounded 5 minute window | HEAD NoSuchKey x6 and VERSIONS_AFTER 0 x6 | HEAD 404 (NoSuchKey) x6 at 2026-10-16T01:28:33Z; VERSIONS_AFTER 0 and markers 0 x6; control: list-objects-v2 on request_compositions/ returns a live key (ART-13c1b409.../15342d3e...json). | CLOSED 20261016T012913Z |

## Log

- 20261016T004802Z OPENED by 0.7.0_AE_CloudOps~U7 with 3 leg(s)
- 20261016T012913Z LEG L closed: SUPERSEDED-WORLD-DONE: measured 2026-10-16T01:2xZ by 1.0.0_SA_CTO after the laptop reboot killed U7 (not registered). Pe
- 20261016T012913Z LEG D closed: SUPERSEDED-WORLD-DONE: the deleting session's call output did not survive the reboot, so per-call results are UNREAD. Me
- 20261016T012913Z LEG R closed: HEAD 404 (NoSuchKey) x6 at 2026-10-16T01:28:33Z; VERSIONS_AFTER 0 and markers 0 x6; control: list-objects-v2 on request_
- 20261016T012913Z CLOSED -- all 3 legs proven
