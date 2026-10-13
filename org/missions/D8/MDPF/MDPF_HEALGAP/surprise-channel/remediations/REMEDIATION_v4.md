# MDPF_HEALGAP -- round 4 remediations (dell1)

<sweep_watermark>2026-10-13T17:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T17:10:00Z. Graduated at ADJUDICATION_v4: 3 rows, all INERT, to 1.0.0_SA_CTO~DELL1.

```json
[
  {
    "id": "MDPF_HEALGAP-D1-W14-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The census names run-capture.ps1 (task SchwabSddCapture) as the act that refills the SI2 standing session; it writes Secrets Manager schwab/sdd/session, while the puller reads the Credential Manager SDDSecure, for which no in-repo writer was found.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W14-S2",
      "adjudication row MDPF_HEALGAP-D1-C-S33",
      "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md"
    ],
    "remedy": "Rule which act restores SDDSecure (the GUI sign-in the capture reads, per the dispositions document). Close when: the census names that act and a puller run after it reads SDDSecure.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W14-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ASTN's FT leg does not refill a missed day: a failed fetch is a warning (tools/astn_wsjft/scripts/run.py:133) and the 12-hour freshness window skips it; a re-attempt is designed (07:00 America/New_York guard) with its send policy undecided.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W14-S3",
      "adjudication row MDPF_HEALGAP-D1-C-S33",
      "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md"
    ],
    "remedy": "Rule the send policy for a refilled day. Close when: a missed day is refilled by the re-attempt on its first live occurrence.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W14-S4",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "infra/aws/terraform/transcripts/pull.tf lines 1-3 say the file is planned and never applied, while teams-global-transcripts-pull-hourly is live and ENABLED.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W14-S4",
      "adjudication row MDPF_HEALGAP-D1-C-S33",
      "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md"
    ],
    "remedy": "Route to the transcripts project's owner: correct the header, or record the out-of-file apply. Close when: the file and the live rule agree.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
