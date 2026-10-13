# AMGT_HARVST -- Z-S115 disarm (dell1)

<sweep_watermark>2026-10-13T08:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T08:55:00Z. Asked by 2.0.0_SA_COO~W1 msg 4730. The windowless runner (HVST-bz-4) removes the console Z-S115 froze; the disarm clock is written, the remediation stays OPEN on the first completed windowless cycle. Round 84 stays open for bz-5: no slug.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S37",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T08:55:00Z",
    "one_line": "Z-S115 DISARMED (REMEDIATION_v16 disarm ARMED -> DISARMED at 2026-10-13T08:55:00Z; remediation stays OPEN). Read by this seat from origin/box/sitez @2e5995b738 deliverables/0.7.0_AE_CloudOps~ZW/round84/, fetched 2026-10-13T08:4xZ: bz4_task.xml <Command>C:\\Program Files\\Python314\\pythonw.exe</Command> and <WorkingDirectory> ...\\wk-harvest-runner-pin-995adcaeaa, state dir still the c1be67f53c pin; bz4_reads.out: ONE runner over all exes at +15 (PID 50360 pythonw.exe, started 08:09:08Z), cycle_runner.log written on a ~2.9 min cadence (08:09:09Z..08:26:54Z), R1-R4 TRUE, no rollback; bz4_console.out: the DISCRIMINATING arm is the conhost-child count, 0 for the runner against a positive control of 1 (console python.exe PID 7068). MainWindowHandle=0 does NOT discriminate (the control reads 0 too), and is not relied on. The runner's one child is the windowless collector spawn (pythonw, 0 children). bz4_stopped.out: the 1c69 cycle ended by its own stop file at 07:59:03Z, nothing killed. PROOF: AC1 and AC2 query site Z's scheduled task (Get-ScheduledTask) and are not runnable from dell1 (they would read dell1's own task); AC3 is a file read, and its expect '(?s)MainWindowHandle=0.*CONHOST_CHILD=NONE' matches bz4_console.out as read here; the instance is on origin/box/sitez, not in dell1's tree, so the checker was not re-run here (the issuer's re-run reads VALID rc 0). CLOSE CONDITION, OPEN: the first COMPLETED windowless cycle record (about 19:10Z), read with its log cadence intact. Z-S114 stays dismissed (C-S35).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-Z-S115"
    ],
    "spec_asserts": "A disarm clock is written only on evidence that the hazard can no longer fire in normal operation, read by the CVO; the remediation closes on its own close condition.",
    "world_is": "Z-S115 DISARMED (REMEDIATION_v16 disarm ARMED -> DISARMED at 2026-10-13T08:55:00Z; remediation stays OPEN). Read by this seat from origin/box/sitez @2e5995b738 deliverables/0.7.0_AE_CloudOps~ZW/round84/, fetched 2026-10-13T08:4xZ: bz4_task.xml <Command>C:\\Program Files\\Python314\\pythonw.exe</Command> and <WorkingDirectory> ...\\wk-harvest-runner-pin-995adcaeaa, state dir still the c1be67f53c pin; bz4_reads.out: ONE runner over all exes at +15 (PID 50360 pythonw.exe, started 08:09:08Z), cycle_runner.log written on a ~2.9 min cadence (08:09:09Z..08:26:54Z), R1-R4 TRUE, no rollback; bz4_console.out: the DISCRIMINATING arm is the conhost-child count, 0 for the runner against a positive control of 1 (console python.exe PID 7068). MainWindowHandle=0 does NOT discriminate (the control reads 0 too), and is not relied on. The runner's one child is the windowless collector spawn (pythonw, 0 children). bz4_stopped.out: the 1c69 cycle ended by its own stop file at 07:59:03Z, nothing killed. PROOF: AC1 and AC2 query site Z's scheduled task (Get-ScheduledTask) and are not runnable from dell1 (they would read dell1's own task); AC3 is a file read, and its expect '(?s)MainWindowHandle=0.*CONHOST_CHILD=NONE' matches bz4_console.out as read here; the instance is on origin/box/sitez, not in dell1's tree, so the checker was not re-run here (the issuer's re-run reads VALID rc 0). CLOSE CONDITION, OPEN: the first COMPLETED windowless cycle record (about 19:10Z), read with its log cadence intact. Z-S114 stays dismissed (C-S35).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "origin/box/sitez @2e5995b738 deliverables/0.7.0_AE_CloudOps~ZW/round84/bz4_task.xml",
        "origin/box/sitez @2e5995b738 deliverables/0.7.0_AE_CloudOps~ZW/round84/bz4_reads.out",
        "origin/box/sitez @2e5995b738 deliverables/0.7.0_AE_CloudOps~ZW/round84/bz4_console.out",
        "origin/box/sitez @2e5995b738 deliverables/0.7.0_AE_CloudOps~ZW/round84/bz4_stopped.out",
        "origin/box/sitez @2e5995b738 deliverables/0.7.0_AE_CloudOps~ZW/round84/bz4_census.out",
        "order AMGT_HARVST.TO-HVST-bz-4 AC1-AC3 at @2e5995b738"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S115 DISARMED (REMEDIATION_v16 disarm ARMED -> DISARMED at 2026-10-13T08:55:00Z; remediation stays OPEN). Read by this seat from origin/box/sitez @2e5995b738 deliverables/0.7.0_AE_CloudOps~ZW/round84/, fetched 2026-10-13T08:4xZ: bz4_task.xml <Command>C:\\Program Files\\Python314\\pythonw.exe</Command> and <WorkingDirectory> ...\\wk-harvest-runner-pin-995adcaeaa, state dir still the c1be67f53c pin; bz4_reads.out: ONE runner over all exes at +15 (PID 50360 pythonw.exe, started 08:09:08Z), cycle_runner.log written on a ~2.9 min cadence (08:09:09Z..08:26:54Z), R1-R4 TRUE, no rollback; bz4_console.out: the DISCRIMINATING arm is the conhost-child count, 0 for the runner against a positive control of 1 (console python.exe PID 7068). MainWindowHandle=0 does NOT discriminate (the control reads 0 too), and is not relied on. The runner's one child is the windowless collector spawn (pythonw, 0 children). bz4_stopped.out: the 1c69 cycle ended by its own stop file at 07:59:03Z, nothing killed. PROOF: AC1 and AC2 query site Z's scheduled task (Get-ScheduledTask) and are not runnable from dell1 (they would read dell1's own task); AC3 is a file read, and its expect '(?s)MainWindowHandle=0.*CONHOST_CHILD=NONE' matches bz4_console.out as read here; the instance is on origin/box/sitez, not in dell1's tree, so the checker was not re-run here (the issuer's re-run reads VALID rc 0). CLOSE CONDITION, OPEN: the first COMPLETED windowless cycle record (about 19:10Z), read with its log cadence intact. Z-S114 stays dismissed (C-S35)."
  }
]
```
