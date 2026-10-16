# ADVI_FIRMBKTS -- round 7 remediations (dell1)

<sweep_watermark>2026-10-14T11:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T11:45:00Z. Graduated at ADJUDICATION_v8: 12 rows (5 ARMED/BLOCKING at D1-C-S51, 5 INERT at D1-C-S52, 2 ARMED late at D1-C-S55).

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W75-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "B_01's silver-noncash cap compresses market_value on 64,629 of 492,998 open lots; a position bullet over a capped lot states the cap's output as the client's value (IQLT -69.2 percent).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W75-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S51 (ADJUDICATION_v8)"
    ],
    "remedy": "No position slot (top_gainer, top_loser, concentration_risk, tax_loss_candidate, top_nna_mover) is switched on until the bullet's value is the uncapped units x price or the cap is ruled for this use (the CRO's pricing brief).",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W80-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Retiring the Door 6 key opal-data-inf/gold/meta/pipeline-complete.json would stop a live S3 notification that invokes inf-portal-publisher (ADVI_INFETL.005).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W80-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S51 (ADJUDICATION_v8)"
    ],
    "remedy": "The plan's ruling on the key names that consumer and re-points or replaces its trigger before any retirement.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v8"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W77-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The same live second watcher on the prohibited key as D1-W80-S1; the bucket's notification configuration is a singleton (DEC-7).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W77-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S51 (ADJUDICATION_v8)"
    ],
    "remedy": "Carried into the FWD-9 plan beside D1-W80-S1.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": "2026-10-16T17:16:04Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W77-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "exec-summary-trigger is live and ENABLED on the chain-complete event and no Terraform declares it.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W77-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S51 (ADJUDICATION_v8)"
    ],
    "remedy": "Declare (import) the rule, or name it in the plan as the one undeclared trigger the move must re-point.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": "2026-10-16T17:16:04Z"
    },
    "closed": true
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W77-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The served graph cannot answer the Inflection bucket's IAM-grant or Lambda-environment question.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W77-S3",
      "adjudication row ADVI_FIRMBKTS-D1-C-S51 (ADJUDICATION_v8)"
    ],
    "remedy": "The move plan's grant column is read from live IAM and Lambda, never from the graph.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S50",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A client display name reached a top_nna_mover bullet past the generator's PII guard in a dry run; nothing was served.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S50",
      "adjudication row ADVI_FIRMBKTS-D1-C-S52 (ADJUDICATION_v8)"
    ],
    "remedy": "With D1-S53: before top_nna_mover is switched on, a dry run that reaches the name guard with a name-bearing context and shows the guard drop it.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S53",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The name guard is proven only by the slot switch; with top_nna_mover OFF the guard is never reached.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S53",
      "adjudication row ADVI_FIRMBKTS-D1-C-S52 (ADJUDICATION_v8)"
    ],
    "remedy": "As D1-S50.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W79-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Cottonwood holdings have two live homes: the edge router resolves cottonwood to opal-data-cot; the IRPT holdings reader reads opal-data-cottonwood.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W79-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S52 (ADJUDICATION_v8)"
    ],
    "remedy": "The move plan names both readers and which home each moves to.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W78-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "cot-etf-ownership-daily's live SRC_BUCKET names opal-data-cot, which its code does not read.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W78-S4",
      "adjudication row ADVI_FIRMBKTS-D1-C-S52 (ADJUDICATION_v8)"
    ],
    "remedy": "FWD-5 counts live configuration: the plan clears or re-points the variable.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W80-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "router_iam.tf:26-29 cites mdpf-daily-refresh-trigger as the live guard on the Door 6 key; that rule was destroyed 2026-08-18.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W80-S2",
      "adjudication row ADVI_FIRMBKTS-D1-C-S52 (ADJUDICATION_v8)"
    ],
    "remedy": "The plan's trigger inventory corrects the citation or the guard.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W69-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "This device's commit gate reports the hashed account-id list ABSENT, so commits are not checked for client account ids (D1-S51 is one that reached a commit).",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W69-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S55 (ADJUDICATION_v8)"
    ],
    "remedy": "Provision the hashed list on dell1 so the commit gate checks account ids, and show one refusal on a planted id.",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v8"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W70-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The generator's dry-run path still puts ExecSummaryTokensIn/Out, ExecSummaryLLMCallsMade and ExecSummarySlotDropped metrics.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-W70-S1",
      "adjudication row ADVI_FIRMBKTS-D1-C-S55 (ADJUDICATION_v8)"
    ],
    "remedy": "The dry-run path writes no metric, or the metrics carry a dry-run dimension the dashboards exclude.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~B1",
      "at": null
    },
    "closed": false
  }
]
```
