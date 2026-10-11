# MDPF_CANON -- round 4 remediations (dell1)

<sweep_watermark>2026-10-11T07:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1). The row graduated at ADJUDICATION_v4 (C-S50), held while TO-CN-d-1 was pending (LD-0521), landed 2026-10-11T07:10:00Z as held.
Rows still open from REMEDIATION_v3: D1-S10, W8-S4, W8-S5, W9-S7.

```json
[
  {
    "id": "MDPF_CANON-D1-S16",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": ".tools/safe-merge.sh --continue committed a merge from a stale index snapshot after HEAD moved: merge 0468b6c8ba (parents b1bd62f384, 912327aeab) reverted 7 paths of a peer's commit. They were restored byte-exact @c190e6faf8 under the audited lane override.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S16",
      "adjudication row MDPF_CANON-D1-C-S50"
    ],
    "remedy": "Route to 0.0.0_AB_MSTR (owner of .tools/safe-merge.sh): --continue re-reads HEAD and refuses when it moved since the merge opened, or rebuilds the tree from the current HEAD. Close when: a --continue after a peer commit either refuses or keeps the peer's paths, on an exercise",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v5"
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
