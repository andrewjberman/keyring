# MDPF_COTREMEDIATION -- L8/L9 adjudication of the whole channel (closure compile)

<sweep_watermark>2026-09-22T18:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01 ~08:0xZ. Trigger: 1.0.0_SA_CTO 103592 and 103613 (the laptop closure plan @2f9c18f564; the close waits only on this compile). Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed). 21 undispositioned rows (S1..S21): 10 dismissed by the four rows below, 11 graduated in REMEDIATION_v1.md, of which 4 are closed there (S4, S5, S18, S20). Both task orders of the project read complete; no JUDGMENT criterion was cut.

```json
[
  {
    "id": "MDPF_COTREMEDIATION-C-S1",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:00:00Z",
    "one_line": "S2 (the PRD's two payload leads did not reproduce on the served keys) was resolved inside the repair: both leads sit in count_as_of, not dates, and the shape is the field's lawful design.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_COTREMEDIATION-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "On the served cottonwood payload read today (version pJAETDuw..., as_of_last 2026-09-29) dates holds 0 nulls of 486 while count_as_of holds 485 nulls of 486 and count_provenance reads source_absent 485 / measured 1. The same shape on healthy data shows it is a property of the field and not of the 08-19 freeze.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api get-object opal-data-portal-v2 platinum/mdpf/cottonwood/aggregate-aua-timeseries.json (this seat, 2026-10-01 07:4xZ): the counts above",
        "org/tier2_senior/0.4.0_DS_ClientPlatform~M/deliverables/MDPF_COTREMEDIATION.TO-R1-DS_PROOF_OF_SPEC.json criterion COTR1DS-AC7: L1 and L2 relocated to count_as_of and explained at source",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_AC_GRADE_20261001.md @7bc5eb882b, AC5",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The unreproduced observation was located on another field and explained; PRD criterion AC5 grades PASS on it."
  },
  {
    "id": "MDPF_COTREMEDIATION-C-S2",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:00:00Z",
    "one_line": "S1, S9, S10 and S12 record properties with no live hazard: an exception class named for an attribution, a contract that refuses a pre-08-20 replay loudly, a pointer to the mdpf_revamp prefix, and an undeployed copy of the contract in a home nothing runs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_COTREMEDIATION-S1",
      "MDPF_COTREMEDIATION-S9",
      "MDPF_COTREMEDIATION-S10",
      "MDPF_COTREMEDIATION-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The guard reads the exact header tuple and raises (data/assets/scripts/silver/mirror_conversion.py:263-270 at HEAD), so a replay of an older file fails loud and writes nothing (S9). The class name VendorDriftError is recorded as misleading in the project row's root_cause.why_it_survived (S1). S10 is a pointer its own author did not claim as a diagnosis. S12's reachability question was settled in the row itself and no failure followed in 37 days: the repaired table holds a partition for every trading day since 2026-06-09.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/silver/mirror_conversion.py:263-270 at HEAD (this seat): assert_declared_header compares header to the declared tuple and raises VendorDriftError",
        "comp-keys partitions s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/ (this seat, 07:4xZ): 83 partition dates, latest 2026-09-29, 2 weekday gaps, both market holidays",
        "org/projects/MDPF_COTREMEDIATION.json root_cause.why_it_survived: the rename candidate HeaderContractMismatch is recorded there",
        "investigation rows MDPF_COTREMEDIATION-S1, -S9, -S10, -S12",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "None of the four is a hazard: one fails loud, one is a name, one is a pointer, one names an absence nothing reaches. The rename and the mdpf_revamp layout are carried to MDPF_CANON's decomposition in the review, not as rows."
  },
  {
    "id": "MDPF_COTREMEDIATION-C-S3",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:00:00Z",
    "one_line": "S11, S14, S15 and S21 are observations about how the fabric worked during the repair (a known finding rediscovered, a reused PID, a liveness reading that aged, a met disarm with no clock to write); none names an artifact of this project.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_COTREMEDIATION-S11",
      "MDPF_COTREMEDIATION-S14",
      "MDPF_COTREMEDIATION-S15",
      "MDPF_COTREMEDIATION-S21"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S14 was disarmed at filing by its own rule (a PID limb carries its read time). S15 self-corrected inside one dispatch cycle. S11 is a retrieval failure of the fabric, not of this pipeline. S21 records that S20's disarm condition was met on 2026-09-22; S20 now carries its clocks in REMEDIATION_v1.md, which is the carrier S21 said did not exist.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_COTREMEDIATION-S11, -S14, -S15, -S21 (their own grounding blocks)",
        "REMEDIATION_v1.md row MDPF_COTREMEDIATION-S20 (co-committed): closed with its disarm clock",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Process observations with no project artifact to remedy; S14's standing was ARMED only until its rule was stated, which the row itself did."
  },
  {
    "id": "MDPF_COTREMEDIATION-C-S4",
    "project": "MDPF_COTREMEDIATION",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-01T08:00:00Z",
    "one_line": "S8 (mirror_schemas.py has five homes and three were already divergent) is the same vendor-parity residue as S6 and is carried on S6's remediation row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_COTREMEDIATION-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "For the blackdiamond package the contract file is in parity today: the deployed zip, the lambda directory and the source all hash 8818df2f03 for mirror_schemas.py. The divergence S8 named in the eclipse, etf and orion packages was not re-read; the parity question as a whole lives on S6.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda get-function opal-assets-silver-blackdiamond (this seat, 07:5xZ): mirror_schemas.py deployed 8818df2f03 = lambda directory = source",
        "REMEDIATION_v1.md row MDPF_COTREMEDIATION-S6 (co-committed)",
        "investigation row MDPF_COTREMEDIATION-S8 (0.4.0_DS_ClientPlatform~M)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_COTREMEDIATION_CHANNEL_COMPILE_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Subsumed: one remedy (vendor parity across the silver converter packages) covers both, and it is carried on S6."
  }
]
```
