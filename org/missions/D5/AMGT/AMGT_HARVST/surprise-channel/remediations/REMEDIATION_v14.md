# AMGT_HARVST -- rounds 75 and 79 remediations (dell1)

<sweep_watermark>2026-10-12T13:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T13:10:00Z. Graduated at ADJUDICATION_v71: 4 rows (Z-S111 ARMED; D1-S7, Z-S110, Z-S113 INERT).

```json
[
  {
    "id": "AMGT_HARVST-D1-S7",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The cycle runner writes each failure's detail as the status word itself ({status: error, detail: error}, 8 of 8 in bbg cycle 20261010T221526Z), so a failure record carries no reason a reader can act on.",
    "evidence": [
      "investigation row AMGT_HARVST-D1-S7",
      "row AMGT_HARVST-D1-C-S7 (bw-2 AC3 FAIL)"
    ],
    "remedy": "Carry the collector's own error text (exception class and message, or HTTP status) into failures[].detail. Close when: a cycle record's failures each carry a detail distinct from the status, read on a live cycle.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v79",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v79"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-Z-S110",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pinned installer defaults StopFile from RepoRoot, so the live runner (PID 21512: state dir and runtime root under the c1be67f53c pin) reads its STOP file inside the b5a7a3a4b6 code worktree, not under its runtime root.",
    "evidence": [
      "investigation row AMGT_HARVST-Z-S110",
      "bw2_bbg_cycle.out PID 21512 command line"
    ],
    "remedy": "Derive StopFile from the carried RuntimeRoot. Close when: the registered task's --stop-file sits under its own runtime root, read from the scheduled task's definition.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v79",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v79"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-Z-S111",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Worktree GC (worktree_gc.py --go, /govern) judges idleness by git activity only and force-removes a merged, unlocked worktree even while a live process or scheduled task runs from it; it killed the harvest runner on 2026-10-10 22:01Z.",
    "evidence": [
      "investigation row AMGT_HARVST-Z-S111",
      "3.0.0_SA_CVO comp-find 'harvest-runner-pin|wk-harvest-runner' over .tools: 0 hits / 515 files"
    ],
    "remedy": "Lock the runner's pin worktrees (git worktree lock) or make GC skip a tree that is any live process's cwd or a scheduled task's WorkingDirectory. Close when: a GC --go dry run on site Z lists the runner's pin worktrees as kept, with the reason printed.",
    "owner": "0.0.0_AB_MSTR~Z",
    "round": "v79",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~Z",
      "round": "v79"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "0.0.0_AB_MSTR~Z",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-Z-S113",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The r47 backfill driver classifies its stop status 'error' as transport-class and retries it, though the failing pairs carry rc 3221225794 (0xC0000142, a local process-launch failure).",
    "evidence": [
      "investigation row AMGT_HARVST-Z-S113"
    ],
    "remedy": "Classify a local launch failure (Windows STATUS_DLL_INIT_FAILED and kin) as local, not transport. Close when: a planted launch failure is labelled local and is not auto-cleared by --auto-resume-transient.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v79",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v79"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": null
    },
    "closed": false
  }
]
```

## Disposition lines (appended, 3.0.0_SA_CVO, dell1, 2026-10-17T12:03:37Z)

From the HVST-cc-6 triage, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json` @341e87e97a, per `ROUND_ANALYSIS.round88.md` section 2 @07264722d8 (a disposition or owner move on an existing row is an appended line on that row's file; no row is edited and none is minted). Each line below supersedes the named row's `owner` and `remediation.owner` from this timestamp. The row's state is unchanged unless the line says DISMISSED.

- `AMGT_HARVST-D1-S7`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 traces where the collector writes a failure's detail and makes it carry the exception class and message or HTTP status under its own pair; SC1 then reads one live cycle record; un-parks when a failure's detail differs from its status on that live cycle. Basis: Not met: cycle_runner.py:211 copies failures' detail from the checkpoint with a fallback to the status word, and the only evidence (bw-2 cycle 20261010T221526Z, 8 of 8 detail equal to status) is a read from a live cycle that is not re-read at HEAD.
- `AMGT_HARVST-Z-S110`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 derives StopFile from the carried RuntimeRoot in the installer under its own pair; 0.7.0_AE_CloudOps~SC1 re-registers the task and reads --stop-file from the task definition; un-parks when the STOP path sits under the --runtime-root argument. Basis: Not met: install-cycle-schedule.ps1:16 at HEAD still defaults StopFile to RepoRoot's .runtime\harvest-cycle\STOP, while RuntimeRoot is base\runtime (line 15), so the --stop-file argument does not sit under the carried runtime root.
- `AMGT_HARVST-Z-S111`: RE-OWNED to `0.0.0_AB_MSTR~DELL1`. Next act: MSTR~DELL1 takes the ARMED disarm, runs the worktree_gc.py dry run on site Z and records the pin worktrees as kept with the printed reason; un-parks on that printed output. Basis: Not met: .tools/worktree_gc.py:10-13 at HEAD now SKIPs a tree a running process or scheduled task names, so the code change is present, but the close is a GC --go dry run on site Z listing the runner's pin worktrees as kept, which this seat cannot run; the row's ARMED disarm owner 0.0.0_AB_MSTR~Z is not live.
- `AMGT_HARVST-Z-S113`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 adds a planted launch failure (rc 3221225794, STATUS_DLL_INIT_FAILED) labelled local that --auto-resume-transient does not clear, under its own pair; un-parks when that test passes at HEAD. Basis: Not met: backfill_driver.py:47-48 and its transient-stop resume still retry an 'error' stop, and test_ae4_backfill_driver.py:198-203 asserts that an 'error' stop resumes; no local-launch-failure label exists at HEAD, so the planted-launch-failure close is not met.

-- 3.0.0_SA_CVO
