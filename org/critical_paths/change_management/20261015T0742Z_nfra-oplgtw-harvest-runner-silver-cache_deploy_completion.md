# Deploy Completion Record
**Date opened:** 2026-10-15T07:42:21.830827+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261015T192201Z
**Deploy:** OG-eg-2: harvest runner pin moved in place 3d88eccbc3 -> 7662e9c016 (silver cache), runner stopped at a job boundary and restarted
**Authored by:** 0.7.0_AE_CloudOps~ZW
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| STOP | activation | runner ended on its own STOP file at a job boundary (never killed) | cycle record stopped_by_operator + 0 cycle_runner processes + task not Running | 2026-10-15T07:44:30Z CYCLE bbg 20261014T222446Z stopped stopped_by_operator failed 0, then STOP-FILE no further cycle; waiter saw task Ready + 0 cycle_runner processes at 07:44:37Z, never killed (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/EG2_BEFORE.json, EG2_PROOF.json) | CLOSED 20261015T074816Z |
| PIN | activation | pin worktree checked out at 7662e9c016, still LOCKED, STOP file deleted | rev-parse HEAD 7662e9c016 + silver_cache count 1 + git worktree list locked | pin rev-parse HEAD 7662e9c01684e914ce36d0167b8c29b84e1b2870; show HEAD:store.py grep -c 'def silver_cache' = 1; tracked status EMPTY before and after; STOP deleted Test-Path False; git worktree list --porcelain still 'locked AMGT_HARVST live cycle runner pin (HVST-bz-10)' | CLOSED 20261015T074816Z |
| START | activation | task Start-ScheduledTask, State Running, registration unchanged | task read back Running + EG2_PROOF.json written | Start-ScheduledTask 2026-10-15T07:47:40Z, State Running, 1 cycle_runner process (pid 37428); arguments and WorkingDirectory byte-equal to EG2_BEFORE.json; EG2_PROOF.json written (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/EG2_PROOF.json) | CLOSED 20261015T074816Z |
| FIRSTREC | verify | first cycle record after the start carries s3_get_count and s3_get_bytes (<=10 GB) | eg2.AC2.sh PASS | CLOSED SUPERSEDED BY NFRA_OPLGTW.TO-OG-eg-3 -- the proof this leg asks for can never be produced on this box. The leg wants the first cycle record after OG-eg-2's restart to carry s3_get_count and s3_get_bytes (eg2.AC2.sh PASS). The runner that restart produced (PID 37428, started 2026-10-15T07:47:40Z) has now been RETIRED under OG-eg-3: STOP file 18:13:30Z, ended stopped_by_operator at a job boundary, task Disabled 19:04:24Z, and the site Z runner will not start again -- Andrew moved all harvest operations to dell1 (PRD v3.11, CTO msg 34500, dell1's CTO accepted). So there is no future site Z cycle record to carry those fields. RECORDED AS NOT-EXERCISED rather than as a pass: this seat did not run eg2.AC2.sh and does not claim it passes. The E1/E2 GET-bytes proof is owed on dell1, which runs the same code at pin 39ae28559b. ONE CORRECTION TO THE RETIRE ORDER'S PREMISE, which bears on this leg: OG-eg-3 says site Z stored new 0 for every publisher since the 14:02Z Python outage. The runner's own log shows otherwise for sa -- 'JOB sa security-d13cdd57ffa64286 status=new_articles stored=2' at 18:25:18Z and 'CYCLE sa ... asked 242 new 3' at 18:33:06Z -- because the live process predated the outage and kept the standard library it had loaded. So the baseline for sa on this box is new 3 over a cycle that reached 7 of 242 pairs, not zero. Row NFRA_OPLGTW-Z-S151. NOTE ON WHERE THIS WORDING LIVES: deploy_ledger.py's close line is fixed text it writes itself, so the SUPERSEDED declaration the order asks for is made here, in the last leg's proof, inside the same entry. | CLOSED 20261015T192201Z |

## Log

- 20261015T074221Z OPENED by 0.7.0_AE_CloudOps~ZW with 4 leg(s)
- 20261015T074816Z LEG STOP closed: 2026-10-15T07:44:30Z CYCLE bbg 20261014T222446Z stopped stopped_by_operator failed 0, then STOP-FILE no further cycle; w
- 20261015T074816Z LEG PIN closed: pin rev-parse HEAD 7662e9c01684e914ce36d0167b8c29b84e1b2870; show HEAD:store.py grep -c 'def silver_cache' = 1; tracked 
- 20261015T074816Z LEG START closed: Start-ScheduledTask 2026-10-15T07:47:40Z, State Running, 1 cycle_runner process (pid 37428); arguments and WorkingDirect
- 20261015T192201Z LEG FIRSTREC closed: CLOSED SUPERSEDED BY NFRA_OPLGTW.TO-OG-eg-3 -- the proof this leg asks for can never be produced on this box. The leg wa
- 20261015T192201Z CLOSED -- all 4 legs proven
