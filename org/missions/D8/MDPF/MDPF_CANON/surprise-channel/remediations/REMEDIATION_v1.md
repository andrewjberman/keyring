# MDPF_CANON -- round 1 remediations (dell1)

<sweep_watermark>2026-10-09T21:41Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T21:41:00Z. Graduated at ADJUDICATION_v1: 5 rows, all INERT.

```json
[
  {
    "id": "MDPF_CANON-D1-S1",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Three test_global_fold_flag2.py cases fail at box/dell1 before any MDPF_CANON change (carried vs measured label; 128.0 vs 120.0): a pre-existing red in the global fold's tests.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S1"
    ],
    "remedy": "Route to the global fold's owner and fix or rule the three cases. Close when: the three cases pass or carry a ruling",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W1-S1",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Terraform opal_name module's scope_bucket['global'] is opal-data-portal-v2 while address(mdpf, global, gold, ...) puts the composite gold in opal-data-mdpf; the build used local.mdpf_bucket. The builder map is tier-blind.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W1-S1"
    ],
    "remedy": "Make the Terraform map tier-aware or rule the composite home. Close when: the map and address() agree for composite gold",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-S2",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "iam:SimulatePrincipalPolicy is denied to the dell1 CloudOps principal (and to this seat's user) for every policy source but its own, so an IAM criterion naming it cannot be run as written.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S2",
      "3.0.0_SA_CVO: SimulatePrincipalPolicy AccessDenied for cloudops-dell1-agent-user earlier this session"
    ],
    "remedy": "Grant the read or rule the committed evaluator as the instrument (standing row MDPF_HEALGAP-D1-S11). Close when: a grant or a ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-C-S9",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The parquet emitter stores a JSON boolean as text (value_text) and drops the _provenance leaves.",
    "evidence": [
      "adjudication row MDPF_CANON-D1-C-S9"
    ],
    "remedy": "Type booleans in the partition (or rule text), and decide whether _provenance travels. Close when: the bool reads back as a bool, or the ruling is recorded",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-C-S2",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CN-a-2 AC3 is NOT MET: the daily path has not written a partition live, the second-run 'unchanged' arm is proven only in a fake-S3 test, and legacy JSON byte-identity is not measured.",
    "evidence": [
      "adjudication row MDPF_CANON-D1-C-S2"
    ],
    "remedy": "Read the 2026-10-10 13:30Z scheduled fire: the day's data.parquet written at address() per built scope and artifact; one re-invoke of the same day reads 'unchanged'; the legacy JSON sha equals the prior build's for that day. Close when: those three reads are recorded",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  }
]
```
