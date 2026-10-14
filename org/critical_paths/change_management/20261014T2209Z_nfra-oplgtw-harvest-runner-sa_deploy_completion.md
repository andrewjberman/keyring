# Deploy Completion Record
**Date opened:** 2026-10-14T22:09:57.593645+00:00
**Status:** OPEN
**Deploy:** OG-sa-1 (A2): runner stopped, SA profile copied from the main tree, runner re-registered with sa
**Authored by:** 0.7.0_AE_CloudOps~ZW
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| STOP | activation | runner ended on its own STOP file at a job boundary | cycle record stopped_by_operator + 0 cycle_runner processes + STOP file deleted | 2026-10-14T22:13:47Z CYCLE bbg 20261014T123043Z stopped stopped_by_operator failed 0, then STOP-FILE no further cycle; 0 cycle_runner\|backfill_driver processes (positive control 60); STOP deleted, Test-Path False; task Ready (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/2b_stop_and_copy.out) | CLOSED 20261014T221935Z |
| COPY | activation | runner sa profile backed up on this box then replaced by a copy of the main tree sa profile | backup path + user_id cookie count >=1 in the runner profile | backup ~/wk-harvest-runner-pin-3d88eccbc3/.runtime/opal-data-harvest/browser-profiles/sa.backup-20261014T221635Z = 264 files / 30.3 MB; robocopy /MIR exit 3, runner sa profile now 8558 files / 722.3 MB equal to the main tree's; user_id cookies 1 of 35 (names only) (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/2b_stop_and_copy.out) | CLOSED 20261014T221935Z |
| READS | verify | authenticated account read 200 through the runner profile and again through the main profile | sa1_runner_read.json + sa1_main_reread.json | runner profile 200 authorizedUser at 22:18:22Z (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/sa1_runner_read.json); main profile re-read 200 authorizedUser at 22:18:49Z (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/sa1_main_reread.json) | CLOSED 20261014T221935Z |
| REGISTER | activation | task re-registered with -Publishers bbg,wsj,barrons,sa -Windowless -RefreshOnce and Running | task read back from the scheduler | registered 2026-10-14T22:23:18Z with --publishers bbg wsj barrons sa --refresh-once, state-dir/runtime-root/stop-file/WORKDIR unchanged, read back from the scheduler; Start-ScheduledTask 22:24:45Z; state Running, 1 cycle_runner process (pid 41128), new bbg cycle UNIVERSE 242 at 22:24:46Z (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/sa1_register.out) | CLOSED 20261014T222619Z |
| WINDOW | verify | one sa cycle later an SA bronze object newer than the re-registration for BA BABA COST | sa1.AC2.sh restored branch PASS |  | OPEN |

## Log

- 20261014T220957Z OPENED by 0.7.0_AE_CloudOps~ZW with 5 leg(s)
- 20261014T221935Z LEG STOP closed: 2026-10-14T22:13:47Z CYCLE bbg 20261014T123043Z stopped stopped_by_operator failed 0, then STOP-FILE no further cycle; 0
- 20261014T221935Z LEG COPY closed: backup ~/wk-harvest-runner-pin-3d88eccbc3/.runtime/opal-data-harvest/browser-profiles/sa.backup-20261014T221635Z = 264 f
- 20261014T221935Z LEG READS closed: runner profile 200 authorizedUser at 22:18:22Z (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/sa1_r
- 20261014T222619Z LEG REGISTER closed: registered 2026-10-14T22:23:18Z with --publishers bbg wsj barrons sa --refresh-once, state-dir/runtime-root/stop-file/WO
