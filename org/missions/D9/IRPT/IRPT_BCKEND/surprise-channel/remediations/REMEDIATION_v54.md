# IRPT_BCKEND: remediations, round 177 (workstream ~P)

<sweep_watermark>2026-10-13T08:35Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T08:35:00Z. Follows ADJUDICATION_v78. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_177_P_DRAIN_END_20261013.md` (aa1ffa367e, msg 6865). No judgment criterion.
Graduated, round label v178: 1 row, OPEN, owner `1.0.0_SA_CTO~DELL2`. The host-bundle pair waits on the CTO half and the host's next scheduled Online.
Still ARMED where they stand: D2-W361-S1 (v53, fenced by the packet), D2-W345-S3 (v47, disarms on the first leftover-count read after the
apply), D2-W348-S2 (v48).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W363-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two PutBucketPolicy writes on opal-data-49financial, on 2026-10-11 at 15:27:29Z and 16:07:36Z, by IAM user cloudops-dell1-agent-user, both after the 49financial package upload at 02:56:45Z; the policy body was not read and the hazard of the change is not judged by this worker.",
  "evidence": [
   "investigation row D2-W363-S2",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_177_P_DRAIN_END_20261013.md"
  ],
  "remedy": "Two PutBucketPolicy writes on opal-data-49financial by dell1's agent user (2026-10-11 15:27Z and 16:07Z), after the package upload; the bodies are unread. The pair's apply order reads the current bucket policy before its first write, and names the PutObject grant its principal needs. The CTO routes the question of what the policy changed to dell1 (ADVI_FIRMBKTS acts touched these buckets the same day).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v178",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v178"
  },
  "closed": false
 }
]
```
