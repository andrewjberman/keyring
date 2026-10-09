# AMGT_RESAPP -- round 80 remediations (dell1)

<sweep_watermark>2026-10-09T04:19Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T04:19:00Z. Graduated at ADJUDICATION_v98: 4 rows, all INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-S3",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "R1's store half (ASML NA 20-F re-fetch, silver row, re-analysis, draft rebuild) was held for a per-use egress word that law edit 4d77a9c3ea has since lifted; it needs no Bloomberg call.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S3",
      "packet s.3 and s.6 item 1"
    ],
    "remedy": "Cut R1's store half in round 81, then walk FWD-18 on ASML NA. Close when: the rebuilt draft is served and walked",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v81",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v81"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served /freshness sentences carry ISO days while the page's own days move to the house long form (DSGN_AMGTV1 round 56), so one page prints two date forms.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S1"
    ],
    "remedy": "The producer emits the served sentence's day in the house long form (or a structured date the page formats). Close when: one served read shows a single date form on /freshness",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v81",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v81"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W317-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The ui-walk disarm on dell1 calls ssm:DeleteParameter, which is denied by design to cloudops-dell1-agent-user (CTO~DELL1 msg 1386), so /opal/ui-walker/password stays PRESENT and the login-refused proof does not print; the account itself reads disabled, armed=no.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W317-S1",
      "packet s.6 item 4"
    ],
    "remedy": "The ui-walk skill's disarm proves dormancy without DeleteParameter (disabled account plus replaced hash, or a read-only proof). Close when: a dell1 disarm prints its proof with the parameter policy unchanged",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v81",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v81"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S6",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "dd-4 step 6 half-landed: reconcile-deployed classes a function with no recorded sha as already-in-parity and writes no artifact_sha256 (comp-lambdamap no-record stays 41), and the harvest root's CHANGELOG.json is refused by the naming limb on two existing names.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S6",
      "packet s.6 item 3"
    ],
    "remedy": "Tooling owners: reconcile-deployed writes the sha for a no-record function; the missing naming registry row lands. Close when: comp-lambdamap no-record drops for this function and the recorder commits",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v81",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v81"
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
