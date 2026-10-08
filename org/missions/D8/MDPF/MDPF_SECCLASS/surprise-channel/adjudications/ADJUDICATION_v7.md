# MDPF_SECCLASS -- round 8 close: the S50/S51 disarm clock

<sweep_watermark>2026-10-07T11:13Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-07T11:13Z. Swept: rows of `investigations/INVESTIGATION_v1.md` at `q/dell1/secclass-r8/r3` @c87375b89b
surfaced after ADJUDICATION_v6's watermark (2026-10-07T09:50Z) and not yet dispositioned: 2 rows, S50 (ARMED) and S51 (INERT). Both
are dismissed below. Rows W24-S2..S8 and W26-S4 carry surfaced_at stamps later than their commits; they were dispositioned in
ADJUDICATION_v6 and are not re-graded. After this file: 0 BLOCKING and 0 undispositioned rows; ARMED open on remediation rows S46,
S49, S7, S2, W6-S2, each with an owner. Round 8: 18 of 18 issued orders terminal at r3 (13 complete before, SC-e-21 complete, SC-e-29
and SC-e-35/36/37 superseded to round 9 with pointers, 1.0.0_SA_CTO~DELL1 msg 160/161). TO-DEPLOY-e21 is SC-e-21's deploy carrier on
the laptop, outside this round's set by that ruling.

```json
[
  {
    "id": "MDPF_SECCLASS-C-S61",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T11:13:00Z",
    "one_line": "S50 (ARMED: the six-class shared module sat on trunk but not in the two gold code buckets, so the next gold push would ship it unchosen) is DISARMED: both keys now read the trunk bytes, moved by the explicit deploy under the signed SC-e-21 halves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S50"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Both shipped keys equal the trunk file by ETag; the disarm condition S50 names (both keys read ETag 3a033c04 after the explicit deploy) is met on this seat's own read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head-object by 3.0.0_SA_CVO 2026-10-07T11:13Z: opal-data-bd code/gold/lib/_shared/etf_classification.py ETag 3a033c04678f1c96d116b641545b17bb VersionId X3S7SQQU2MhuDJicmfqZnsb_Hwj7NBHW 2026-10-07T10:39:50Z; opal-data-cot same ETag, VersionId Oq0iJYUOGycBSWKJmN1DEdFKgXXcQjE_ 10:40:11Z",
        "git show origin/CLOUD:infra/aws/lambda/v2_portal/_shared/etf_classification.py | md5sum = 3a033c04678f1c96d116b641545b17bb; grep -c multi_asset = 0",
        "negative control: head-object opal-data-bd code/gold/lib/_shared/no_such_file.py -> 404",
        "investigation rows MDPF_SECCLASS-S50 and S51 (2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed: trunk and S3 agree in both buckets; the deploy was the explicit act the halves sign, not a push side effect. COO condition 3 (the next E_18 run read) stays with 2.0.0_SA_COO~M1 and is not a hazard on this row."
  },
  {
    "id": "MDPF_SECCLASS-C-S62",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T11:13:00Z",
    "one_line": "S51 (the read-back that is S50's disarm evidence) is dismissed: confirmed by this seat's own reads; it carries no hazard of its own.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S51"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The row's ETags and VersionIds match this seat's head-object reads exactly.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "head-object by 3.0.0_SA_CVO 2026-10-07T11:13Z: opal-data-bd code/gold/lib/_shared/etf_classification.py ETag 3a033c04678f1c96d116b641545b17bb VersionId X3S7SQQU2MhuDJicmfqZnsb_Hwj7NBHW 2026-10-07T10:39:50Z; opal-data-cot same ETag, VersionId Oq0iJYUOGycBSWKJmN1DEdFKgXXcQjE_ 10:40:11Z",
        "git show origin/CLOUD:infra/aws/lambda/v2_portal/_shared/etf_classification.py | md5sum = 3a033c04678f1c96d116b641545b17bb; grep -c multi_asset = 0",
        "negative control: head-object opal-data-bd code/gold/lib/_shared/no_such_file.py -> 404"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Evidence row, confirmed; consumed by C-S61."
  }
]
```
