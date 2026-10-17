# AMGT_HARVST -- round 85 remediations (dell1)

<sweep_watermark>2026-10-14T14:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T14:00:00Z. Graduated at ADJUDICATION_v80 D1-C-S51: 2 rows.

```json
[
  {
    "id": "AMGT_HARVST-Z-S121",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The one refresh per publisher per cycle reports done and the next job is refused 'expired' again; the cause is unread.",
    "evidence": [
      "investigation row AMGT_HARVST-Z-S121",
      "adjudication row AMGT_HARVST-D1-C-S51 (ADJUDICATION_v80)"
    ],
    "remedy": "The CTO's round-85 analysis: park as ordered, or a round 86 that reads the session, credential and producer behind the refusal.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v85",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v85"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-Z-S120",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The runner's graceful-stop file sits in a directory nothing creates, so the documented stop step fails.",
    "evidence": [
      "investigation row AMGT_HARVST-Z-S120",
      "adjudication row AMGT_HARVST-D1-C-S51 (ADJUDICATION_v80)"
    ],
    "remedy": "The installer creates the STOP file's parent at registration, or the stop step creates the directory; carried in the park record.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v85",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v85"
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

- `AMGT_HARVST-Z-S121`: RE-OWNED to `1.0.0_SA_CTO~DELL1`. Next act: 1.0.0_SA_CTO~DELL1 rules park as ordered or orders a round 86 that reads the session, credential and producer behind the refusal; un-parks on that ruling on record. Basis: Not met and already owned by a live seat: the graduation at ADJUDICATION_v80 row D1-C-S51 gives the decision to 1.0.0_SA_CTO~DELL1's round-85 analysis, and the refresh-not-curing cause (session, credential, producer) is unread at HEAD.
- `AMGT_HARVST-Z-S120`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 makes the registration create the STOP file's parent, or the stop step create it, under its own pair; un-parks when the STOP path's parent exists after registration on site Z and the stop command writes the file. Basis: Not met: install-cycle-schedule.ps1 never creates the STOP file's parent (its only file creation is the scheduled-task registration), and cycle_runner.py:68 creates only the log path's parent, so the documented stop step still fails on a missing directory.

-- 3.0.0_SA_CVO
