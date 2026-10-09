# IRPT_DASHBD -- round 36 remediations

<sweep_watermark>2026-10-09T05:15Z</sweep_watermark>

Graduated at round 36's L8 (ADJUDICATION_v21.md), round label v37: 7 rows, OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-D2-W47-S5",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The amended sizing read (dry_run + backfill, population, 2026-10-07) logged LOTS_SKIPPED on a realized-lot key repeat in batch 2 of 8, so lots_rows is 0 and precondition 3 is not met; the first fire was NOT run.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W47-S5",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~47/R35_APPLY_RECORD.json dry_run and dry_run_first"
    ],
    "remedy": "The re-cut makes the realized-lot key unique within a day (or states the composite key) and proves lots_rows > 0 on the population sizing read before any apply.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v37",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v37"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-D2-W47-S4",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Pins 0-4 leave four CHANGED bundle members (opal_naming.py, systems.json, exemptions.json, reporting_policies.json) packaged at their older source-map pins, not the HEAD bytes the packet's file list prints.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W47-S4",
      "infra/aws/lambda/ci/lambda-source-map.json @d5c11dc683 staged_from"
    ],
    "remedy": "The re-cut packages the four bundle members at HEAD bytes, or states each older pin and why, in the release's file list.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v37",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v37"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W48-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "No Commonwealth-reported window overlaps the Black Diamond source's value coverage for the same account, so Cottonwood's tie-out is 0 of 61 account-windows, every miss structural and none an arithmetic disagreement.",
    "evidence": [
      "investigation row IRPT_DASHBD-W48-S1",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/COT_RETURNS_TIEOUT.json"
    ],
    "remedy": "Name Cottonwood's tie-out source for the BD-covered period (an independent overlap) or state that FWD-11's Cottonwood tie-out is unmeasurable there, by ruling.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v37",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v37"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W48-S2",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two inputs the Cottonwood adapter needs are absent from its source: a cash balance held outside the holdings table, and the net-or-gross basis of the reported figure.",
    "evidence": [
      "investigation row IRPT_DASHBD-W48-S2",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/adapter_source.json"
    ],
    "remedy": "Source the cash balance held outside the holdings table and the reported figure's net-or-gross basis, or state each as absent in a sentence on the page.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v37",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v37"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-W49-S1",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The registry has no custody master or bindings for the Orion source, so the adapter's declaration carries no registry_key and the run takes it on the command line; the firm's own bucket holds only irpt/ while its Orion data sits in the routed legacy alias.",
    "evidence": [
      "investigation row IRPT_DASHBD-W49-S1",
      "infra/logic/registry/scopes.json (firm entry: bucket_provisioned true, bindings null, aliases with routed bucket)"
    ],
    "remedy": "Add the Orion custody master and bindings to the registry (rule 30: a builder refusal is a missing row), so the adapter declaration carries a registry_key; route the legacy alias through it.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v37",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v37"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W49-S2",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The reported source is NET of fees and the contract's total_return_daily is GROSS: the contract-literal tie-out is 24 of 562 account-windows within 0.35 pp, and the same inputs with the fee left inside the return are 421 of 562.",
    "evidence": [
      "investigation row IRPT_DASHBD-W49-S2",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~49/INF_RETURNS_TIEOUT.json (within, net_basis, class_counts)"
    ],
    "remedy": "Tie Inflection out like with like: compound the fee back into the gross return before comparing with the net source, and report both counts.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v37",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v37"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-W49-S3",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two flow classes depart from the firm's ratified cashflow taxonomy and were chosen by measurement: Internal Account Journal In/Out and Federal/State Tax Withheld enter F_t as boundary-crossing flows.",
    "evidence": [
      "investigation row IRPT_DASHBD-W49-S3",
      "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~49/INF_RETURNS_TIEOUT.json (flow_set_probe)"
    ],
    "remedy": "Rule the two flow classes (Internal Account Journal In/Out; Federal/State Tax Withheld) against Inflection's ratified cashflow taxonomy, or amend the taxonomy by its owner.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v37",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v37"
    },
    "closed": false
  }
]
```
