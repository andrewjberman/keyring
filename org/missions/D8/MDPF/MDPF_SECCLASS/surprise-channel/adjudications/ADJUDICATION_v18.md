# MDPF_SECCLASS -- round 20 un-park: leg G read and D1-S30 (dell1)

<sweep_watermark>2026-10-12T08:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T08:55:00Z. Asked by 2.0.0_SA_COO~M1 msg 4319: TO-SC-e87b terminal; the round-20 slug held in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R20_SLUG_HELD_REMEDIATION_v11.md` lands as REMEDIATION_v11 with D1-S30 added.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T08:55:00Z",
    "one_line": "Round-20 un-park: TO-SC-e87b reads complete at HEAD (@61214770e9), and round-close-check --round 20 reads MAY-CLOSE (17 orders, 13 complete; TO-DEPLOY-e57e61 not complete and outside the verdict, held on its trigger). Leg G, read by this seat on the served S3 versions: D_04's mix_summary Unclassified is $1,846,332.73 at data_as_of 2026-10-09 both before the ship (05:45:16Z 10-11) and after it (02:01:03Z and 05:44:00Z 10-12), so leg G is NOT MET at this as_of. The cause is D1-S30 (C_06 incremental), not the SC-e-87 code, which D_03's move (-26 securities) shows reaching the gold view. D1-S26 stays OPEN: its close condition (a post-ship fire serving the 23 by NAME:: rows) is not yet met at D_04.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Round-20 un-park: TO-SC-e87b reads complete at HEAD (@61214770e9), and round-close-check --round 20 reads MAY-CLOSE (17 orders, 13 complete; TO-DEPLOY-e57e61 not complete and outside the verdict, held on its trigger). Leg G, read by this seat on the served S3 versions: D_04's mix_summary Unclassified is $1,846,332.73 at data_as_of 2026-10-09 both before the ship (05:45:16Z 10-11) and after it (02:01:03Z and 05:44:00Z 10-12), so leg G is NOT MET at this as_of. The cause is D1-S30 (C_06 incremental), not the SC-e-87 code, which D_03's move (-26 securities) shows reaching the gold view. D1-S26 stays OPEN: its close condition (a post-ship fire serving the 23 by NAME:: rows) is not yet met at D_04.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO read s3://opal-data-bd/platinum/firm/mix_summary.json versions 2026-10-12T08:5xZ: 2026-10-11T05:45:16Z (pre-ship) data_as_of 2026-10-09 mix.Unclassified market_value 1846332.7278; 2026-10-12T02:01:03Z and 2026-10-12T05:44:00Z (post-ship) the same data_as_of and the same 1846332.7278",
        "3.0.0_SA_CVO git show HEAD:org/tier2_senior/0.7.0_AE_CloudOps~SC1/task_orders/MDPF_SECCLASS.TO-SC-e87b...: <status>complete</status>",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project MDPF_SECCLASS --round 20: verdict=MAY-CLOSE",
        "investigation row MDPF_SECCLASS-D1-S30 (D_03 firm_composition versions)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Round-20 un-park: TO-SC-e87b reads complete at HEAD (@61214770e9), and round-close-check --round 20 reads MAY-CLOSE (17 orders, 13 complete; TO-DEPLOY-e57e61 not complete and outside the verdict, held on its trigger). Leg G, read by this seat on the served S3 versions: D_04's mix_summary Unclassified is $1,846,332.73 at data_as_of 2026-10-09 both before the ship (05:45:16Z 10-11) and after it (02:01:03Z and 05:44:00Z 10-12), so leg G is NOT MET at this as_of. The cause is D1-S30 (C_06 incremental), not the SC-e-87 code, which D_03's move (-26 securities) shows reaching the gold view. D1-S26 stays OPEN: its close condition (a post-ship fire serving the 23 by NAME:: rows) is not yet met at D_04."
  },
  {
    "id": "MDPF_SECCLASS-D1-C-S6",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T08:55:00Z",
    "one_line": "D1-S30 graduated INERT to REMEDIATION_v11 (owner 2.0.0_SA_COO~M1): this seat's own read of the mix_summary versions reproduces the row's figures to the cent. The first data_as_of C_06 builds after the ship is read on Tuesday 2026-10-13's fire (Monday answers Friday).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-S30"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-S30 graduated INERT to REMEDIATION_v11 (owner 2.0.0_SA_COO~M1): this seat's own read of the mix_summary versions reproduces the row's figures to the cent. The first data_as_of C_06 builds after the ship is read on Tuesday 2026-10-13's fire (Monday answers Friday).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_SECCLASS-D1-S30",
        "3.0.0_SA_CVO read s3://opal-data-bd/platinum/firm/mix_summary.json versions 2026-10-12T08:5xZ: 2026-10-11T05:45:16Z (pre-ship) data_as_of 2026-10-09 mix.Unclassified market_value 1846332.7278; 2026-10-12T02:01:03Z and 2026-10-12T05:44:00Z (post-ship) the same data_as_of and the same 1846332.7278"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v11.md."
  }
]
```
