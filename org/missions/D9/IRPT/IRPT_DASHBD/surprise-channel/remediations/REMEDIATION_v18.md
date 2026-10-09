# IRPT_DASHBD -- round 37 remediations

<sweep_watermark>2026-10-09T06:39Z</sweep_watermark>

Graduated at round 37's L8 (ADJUDICATION_v22.md), round label v38: 4 rows, OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-D2-W51-S1",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The R35 packet's 'Terraform root has 0 changed files' and its source-map facts no longer hold at HEAD: the round-36 rollback restored iam.tf, locals.tf, lambda.tf and the source-map entry to pre-release bytes, so the R37 apply also needs the three Terraform files restored to efeb21df71.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W51-S1",
      "infra/aws/terraform/investor-reporting/reporting-gold/iam.tf @0709c0a960"
    ],
    "remedy": "The R37 release packet states the root restore (iam.tf, locals.tf, lambda.tf back to efeb21df71 bytes, and the source-map entry) as a step with its own read-back, and both never-widen halves name it before signing.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v38",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v38"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-D2-W53-S1",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Orion's gross return is landed nowhere in S3 and is not a contextChange path of the saved query; it is read by overriding the performance option object in the Generate body (feeMethod Gross Of Fees).",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W53-S1",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~53/orion_gross_fee_pull.py"
    ],
    "remedy": "Land Orion's gross-of-fees return (the Generate override with feeMethod Gross Of Fees) as a silver input with its own as-of, so the tie-out reads a landed figure, not a live pull per run.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v38",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v38"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-D2-W53-S2",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Orion has no field named supervised, and Asset.IncludedInBilling is unreadable for 526 of the 562 sample accounts, so the supervised and billed slices rest on a flag and a partial read.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W53-S2",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~53/INF_GROSS_FEE_TIEOUT.json fee_detail"
    ],
    "remedy": "State the supervised and billed fee slices as partial (IncludedInBilling unreadable on 526 of 562), or source a readable billing flag; never show a slice as complete.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v38",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v38"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W54-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The taxonomy file's title and header say 43 type_desc entries; the file holds 48 under types:, so the stated denominator is stale.",
    "evidence": [
      "investigation row IRPT_DASHBD-W54-S1",
      "data/inf/scripts/silver/orion_cashflow_taxonomy.yaml (types: list, title, schema_collapse_audit)"
    ],
    "remedy": "Correct the taxonomy file's title, comment and total_type_desc_entries_v2 to 48 (or the ruled count after W49-S3), by the taxonomy's owner.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v38",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v38"
    },
    "closed": false
  }
]
```
