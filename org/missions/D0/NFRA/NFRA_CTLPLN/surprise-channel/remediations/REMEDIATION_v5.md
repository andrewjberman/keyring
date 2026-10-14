# NFRA_CTLPLN -- remediations, v5

<sweep_watermark>2026-10-12T18:15Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-12 ~18:1xZ, at the round-11 close. Graduated in ADJUDICATION_v14.md C-S39. Two rows: S9117 and
S9118, both ARMED. Every NFRA_CTLPLN order is terminal at HEAD.

```json
[
  {
    "id": "NFRA_CTLPLN-S9117",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": ".tools/kill-agent.ps1 Stop-ProcessTree (:159-187) recurses through every child of the target's claude.exe with no seat boundary. A seat spawned from inside another seat's session is a descendant, so one kill by serial ends every seat beneath it. Measured on dell2: killing 1.0.0_SA_CTO~DELL2 also ended five parked COOs (12 pids). Their conversation context is lost; files are untouched.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9117",
      ".tools/kill-agent.ps1:159-187 read at HEAD",
      "adjudication row NFRA_CTLPLN-C-S39"
    ],
    "remedy": "P1. Interim (0.0.0_AB_MSTR, in force): before any kill-agent.ps1 run, list the target tree's claude.exe command lines and kill only the seat's own pid and marker children. Permanent (2.0.0_SA_COO~C, round-12 cell): Stop-ProcessTree stops at any descendant claude.exe that carries a different serial. Done when a planted tree (seat A with a child seat B) killed by A's serial leaves B's pid alive, and the tool prints B as skipped.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v14",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v14"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-10-14T01:25Z"
    },
    "closed": true
  },
  {
    "id": "NFRA_CTLPLN-S9118",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": ".tools/kill-maint.ps1 stops each target's whole tree with `taskkill.exe /T /F` (:722), the same missing seat boundary as kill-agent.ps1. It is the /govern reaper that every manager runs -Unattended each cycle. Zero losses from it measured so far.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9118",
      ".tools/kill-maint.ps1:722 read at HEAD",
      "adjudication row NFRA_CTLPLN-C-S39"
    ],
    "remedy": "P1. Interim (0.0.0_AB_MSTR, adopted on dell1, dell2 and the laptop; site Z pending): kill-maint runs dry first each cycle, and -Execute/-Unattended runs only when no target's tree holds a claude.exe carrying another serial. Permanent (2.0.0_SA_COO~C, the S9117 round-12 cell covers both tools): a target whose tree holds another seat's claude.exe is skipped and printed. Done when the same planted tree survives a kill-maint -Execute.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v14",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v14"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  }
]
```
