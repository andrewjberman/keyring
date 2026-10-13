# MDPF_HEALGAP -- round 3 remediations (dell1)

<sweep_watermark>2026-10-13T13:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T13:50:00Z. Graduated at ADJUDICATION_v3: 13 rows. D1-W8-S1 carries its disarm clock DISARMED (remediation OPEN until a live
failed read); D1-S16 (BLOCKING) is the CTO's re-run ruling; the rest are INERT text, registry, checker or ruling items.

```json
[
  {
    "id": "MDPF_HEALGAP-D1-W8-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "HG3-t11-AC2's checker could not fail its failed-read arm (a mutant that skips the pull on rc 1/2 printed SSMGUARD-OK). Corrected at e844a20917: this seat's re-run at HEAD reads SSMGUARD-OK rc 0 on the real document and SSMGUARD-BAD rc 1 on its own -eq->-ge mutant; the live SSM document is v6 with a hash equal to the repo file. The failed-read arm is graded under stubbed tools only.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W8-S1",
      "adjudication row MDPF_HEALGAP-D1-C-S24",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_HEALGAP_R3_D1_W8_S1_DISARM_PREREAD_20261011.md @26e59cbec9"
    ],
    "remedy": "Close when: a live 22:10Z fire whose guard read fails (rc 1 or 2) runs the pull, read from that fire's log beside the guard's exit code.",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": "2026-10-13T13:50:00Z"
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-S16",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 13:25Z characteristics producer reads s3://opal-data-etfs/bbg/<T-1>/characteristics.parquet; on 2026-10-13 the 2026-10-12 partition is absent (404 at 13:33Z and 13:44Z; partitions through 2026-10-09), so three attempts failed NoSuchKey and the served characteristics.json stays at its 2026-10-12T13:26:03Z version (one trading day behind).",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-S16",
      "adjudication row MDPF_HEALGAP-D1-C-S25"
    ],
    "remedy": "The CTO rules a re-run on the partition's arrival (an off-clock run needs a never-widen half) or lets the next scheduled fire take it. Close when: the served characteristics.json is rebuilt from the bbg/2026-10-12 partition (or a later T-1) with holdings_as_of equal to as_of.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "MDPF_HEALGAP-D1-S14",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The HG-t-10 half and the healed check expected healed_at null after the repair; lambda_function.py:276-278 (cot-rebalancer-runner) writes now() for a feed that was missing and has arrived, so the live timestamp is correct and the expectation text is wrong.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-S14",
      "adjudication row MDPF_HEALGAP-D1-C-S26"
    ],
    "remedy": "Correct the half's section 5 item 3 and the healed check script to the producer's rule. Close when: the check passes on the 2026-10-13 repair's record with healed_at set, beside a control feed that never went missing (healed_at null).",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-S13",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-apply's APPLY-WHO (REFUSED: a COO does not apply) and CROSSBOX-DEPLOY (STOP) ran in WARN on this seat's round-3 applies; under ENFORCE both stop the act.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-S13",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "The CTO rules which seat applies for this project. Close when: the next apply runs under that ruling with both gates clear.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W12-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The LGIC root map (root_map.json line 264) still registers cot-satellites-registry-producer-daily, a rule HG-t-15 retired.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W12-S1",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "Retire the registry row (the CTO took it). Close when: root_map.json names no retired rule for this producer.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W11-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "satellites-characteristics-producer.tf lines 34-35 (the WHY block) name the retired cron(0 7) rule as the trigger's anchor.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W11-S1",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "Rewrite the WHY block to name the stamp-gated 13:15Z fire. Close when: the tf carries no reference to the retired rule.",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W7-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The completion stamp key blackdiamond/cottonwood/meta/<date>-complete.json is read and written live, but the key-rulings registry records meta/ as non-canonical.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W7-S2",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "The CTO rules the meta/ prefix canonical (registry row) or names its migration. Close when: the registry and the live key agree.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W7-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "hg_r3_rules.py --t9-iam passes a ListBucket statement whose Resource is widened to opal-data-assets/*, so the 'nothing wider' clause is not held on the ListBucket resource.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W7-S3",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "Tighten the checker to refuse any ListBucket Resource other than the bucket ARN. Close when: a planted widened statement reads T9IAM-BAD and the live policy reads T9IAM-OK.",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W7-S4",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The naming gate WARNed, not refused, on the stamp-prefix literal typed in satellites-registry-producer.tf:46.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W7-S4",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "Route the literal through lib/opal_naming.py address() or record its R20 departure. Close when: the naming gate reads the line clean.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W9-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The outlook transcripts pull is graded EXPOSED-MANUAL in round 3 (RECOVERS in round 2): it shares one gateway Microsoft sign-in that only a person renews.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W9-S1",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "Reconcile the PRD v0.3 addendum's person-renewed list with the census. Close when: the census and the addendum name the same set.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W9-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bd-asset-dim-pipeline-trigger is graded EXPOSED-MANUAL though its 49F login is machine-minted at 00:00Z, 04:35Z and 22:20Z.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W9-S2",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "Give the answer grammar a machine-renewed class, or re-grade the trigger. Close when: the census grades it by its measured renewal path.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W9-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 49F keepalive's dead-cookie alert tells a person to re-capture the cookie, while the session trigger's full mint re-issues it automatically.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W9-S3",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "Make the two sources agree on who renews the 49F login. Close when: the alert text and the trigger's behaviour state one renewer.",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W10-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On the EC2 path the 6d block rewrites one cottonwood gold partition (build_dim_model_portfolio.py --upload, dispatch line 554) before the slice; the slice itself writes no gold partition.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W10-S1",
      "adjudication row MDPF_HEALGAP-D1-C-S27"
    ],
    "remedy": "Name that write in the runner's writer census and in any half that re-runs the slice. Close when: the census lists it with its key.",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  }
]
```
