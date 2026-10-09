# LGIC_BLANKFIX -- round 10 remediations (dell1)

<sweep_watermark>2026-10-09T09:38Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T09:38:00Z. Graduated at ADJUDICATION_v9: 4 rows, all INERT.

```json
[
  {
    "id": "LGIC_BLANKFIX-D1-W1-S3",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A real override commit adds org/audit/naming-place-override-audit.jsonl, which .tools/git-hooks/mstr-ledger-check.sh does not list as record-only, so the first real override may be refused there (fails closed; unexercised).",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W1-S3",
      "3.0.0_SA_CVO read: the hook names the path 0 times"
    ],
    "remedy": "Add the audit path to the hook's record-only list. Close when: a real override commit lands through the hook",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v11",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v11"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-D1-W2-S3",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The base holds 88 Terraform roots and 10 unmapped, not 87 and 9: advi/billing-read (4 names) is a new root in no ruling.",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W2-S3"
    ],
    "remedy": "Rule advi/billing-read (map it or hold it). Close when: the root map or the held list names it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v11",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v11"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-D1-W2-S4",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lib/opal_naming_keyfill.bucket_of takes the file's only opal-data literal as the bucket of every key in the file, so 4 correct key-ruling rows for keys in other buckets are dropped.",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W2-S4"
    ],
    "remedy": "bucket_of resolves each key's own bucket. Close when: the 4 rows land and a test pins a two-bucket file",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v11",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v11"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-D1-W2-S5",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The ruling states harvest has 11 exceptions and mdpf-pipeline 0; grade() measures 13 (two LAMBDA names) and 1 (an IAM policy led by gateway). No verdict moves, but the ruling's counts are stale.",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W2-S5"
    ],
    "remedy": "Correct the ruling's counts to the measured ones, or name the two extra LAMBDA names and the IAM policy as ruled. Close when: the ruling text matches grade()",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v11",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v11"
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
