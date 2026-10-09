# IRPT_DASHBD -- round 33 remediations

<sweep_watermark>2026-10-09T01:46Z</sweep_watermark>

Graduated at round 33's L9 (ADJUDICATION_v18.md), round label v34: W40-S1, W42-S1, S36, all OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-W40-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two earlier modules no longer run at HEAD: ~39 large_flow_e3.py and ~35 crossover_e1.py call a fee-base name that round 32's promotion to the reader removed from their namespace.",
    "evidence": [
      "investigation row IRPT_DASHBD-W40-S1",
      "org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T01Z_round33_desktop-n8rjv0a.md @76f3874a08"
    ],
    "remedy": "One repair cell: the two callers import the fee base from the reader of record under its own name, and each record module re-runs to its committed output.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v34",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v34"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W42-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Round 32's record module large_flow_e3.py no longer runs as committed: its classify calls uc.mean_daily_value, a name round 32's reader promotion removed from the round 31 module.",
    "evidence": [
      "investigation row IRPT_DASHBD-W42-S1",
      "org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T01Z_round33_desktop-n8rjv0a.md @76f3874a08"
    ],
    "remedy": "Carried by W40-S1's repair cell (same cause, same fix).",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v34",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v34"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S36",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Round 33's near-zero classes (DB-b-65: 79 of 153 'fixed') ran through a shim that rebinds uc.mean_daily_value := uc.daily_mean_value, but W38-S1 MEASURED those as different functions (mean_daily_value averages every non-zero daily value, daily_mean_value only the positive ones). So DB-b-65's E3 counts rest on a substituted fee base, not the one round 31's classifier defined.",
    "evidence": [
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~42/near_zero_e3.py:189-193 (the shim) and NEAR_ZERO_E3.json:1572 (records it as applied)",
      "investigation row IRPT_DASHBD-W38-S1 (INVESTIGATION_v1.md ~:3224-3228: 'the two means are not the same function')",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~39/large_flow_e3.py:117 and :279 still call uc.mean_daily_value (this seat's comp-find, 22 hits over the project)"
    ],
    "remedy": "In the same repair cell: re-run DB-b-65's near-zero classes with the fee base it names (no shim), and print how many of the 79 move.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v34",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v34"
    },
    "closed": false
  }
]
```
