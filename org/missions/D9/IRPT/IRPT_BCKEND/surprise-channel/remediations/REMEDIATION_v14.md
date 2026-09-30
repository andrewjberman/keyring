# IRPT_BCKEND -- project sweep 4 remediations

<sweep_watermark>2026-09-29T18:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30. Graduated at sweep 4's L9 (ADJUDICATION_v18.md).

```json
[
  {
    "id": "IRPT_BCKEND-W86-S1",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The Inflection raw files are written by the gold chain, which has died daily since 2026-09-28 at step INF_API_SILVER_REPS on ModuleNotFoundError lib.silver_ids: the dependent file was deployed 09-28 07:17Z without lib/silver_ids.py. This is S216's cause. No raw file exists for 09-28 or 09-29.",
    "evidence": [
      "investigation row IRPT_BCKEND-W86-S1 (0.9.0_WK_IRPT_BCKEND~86, TO-IB-pr-241): chain_full_20260928_113305.log and HeadObject 404 on every candidate code/ prefix for silver_ids.py",
      "1.0.0_SA_CTO ruling 103088: repair first; the round-26 W86-S1 cell ships lib/silver_ids.py",
      "TO-IB-pr-241 reads complete at HEAD (first added 2026-09-29T18:48Z)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP4_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P0: deploy lib/silver_ids.py to the prefix the gold runner imports as lib.silver_ids under a DS-lane safe-deploy and its ledger, then a QA chain run that lands 09-28 and 09-29; S216 and this row disarm together on a per-account read that shows 09-29 (CTO 103088).",
    "owner": "2.0.0_SA_COO~P",
    "round": "v27",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v27"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-W86-S2",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "inf-bronze-runner stopped 4 seconds after its 2026-09-29 launch with an EMPTY stop reason; the launch monitor classified it as a normal shutdown, the retry Lambda never fired, and the 09-29 bronze run never happened. Independent of W86-S1.",
    "evidence": [
      "investigation row IRPT_BCKEND-W86-S2 (0.9.0_WK_IRPT_BCKEND~86): CloudWatch inf-ec2-launch-monitor 11:15:22Z 'reason=' then 'Suppressed normal shutdown'; describe-instances StateTransitionReason Server.InternalError",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP4_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P1: the launch-monitor classifies an empty stop reason on an instance that never reached the fetch script as a launch failure, or the retry chain gains a 'mode marker still present' check; owner placed by the issuer.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v27",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v27"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S219",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two of the live twr_daily table's 559 partitions (date=2024-07-08 and date=2025-01-09) carry schema_version 1.2 but lack bmv/emv/cf_net/cf_gross, so any since-inception read spanning them is refused by the engine's schema guard. The guard is correct; the partitions are the defect.",
    "evidence": [
      "investigation row IRPT_BCKEND-S219 (re-minted by 2.0.0_SA_COO~P from W61-S2; live parquet reads of both partitions; p19_2_ac2_live_seam.py FAIL on the control account)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP4_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P1: 0.4.0_DS_ClientPlatform re-writes the two partitions with the full column set, or the producer states they were never populated by design and bumps schema_version so the guard can key on it; then the live seam check re-runs.",
    "owner": "0.4.0_DS_ClientPlatform",
    "round": "v27",
    "remediation": {
      "state": "OPEN",
      "owner": "0.4.0_DS_ClientPlatform",
      "round": "v27"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "0.4.0_DS_ClientPlatform",
      "at": null
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S220",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The authorization guard census reads 6 failed / 2 passed at HEAD, its mutant controls included, and test_seam_paired.py reads 33 of 58 failed, so neither suite is a usable oracle. The unauthorized-reach reading is disarmed (S221, S222): the served HTTP path is guarded; the census reads an unmarked dispatcher.",
    "evidence": [
      "investigation rows IRPT_BCKEND-S220, S221, S222 (two independent import reads of export/entry.py)",
      "row W89-S2: the census pins 17 routes where the file holds 18",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP4_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P1: a ~P cell makes the census resolve through the dispatcher and moves the count pins off literals; the seam suite's causes are W90-S1's, graded when its round drains. Not claimed: a live unauthorized request, or the direct lambda:Invoke grant set on irpt-export-render.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v27",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P",
      "round": "v27"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P",
      "at": "2026-09-30T01:15:00Z"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-S223",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The published response schema comparison-catalogue.response.schema.json refs opal://irpt/contracts/v1/ComparisonCatalogue.schema.json, which is not among the 23 published top-level schemas; the drain's check graded the ref's shape, not its referent.",
    "evidence": [
      "investigation row IRPT_BCKEND-S223 (2.0.0_SA_COO~Y): census of docs/contracts/investor-reporting/v1 at 73f53c499d, 18 response schemas, 1 dangling ref",
      "TO-IB-yr-271 (the remedy the issuer cut, first added 2026-09-30T01:52Z, not terminal)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_SWEEP4_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P1: publish ComparisonCatalogue.schema.json to the v1 directory (IB-yr-271) and make the resolve-refs test run past the parse; disarm when the census reads 0 dangling of 18. Rule for every issuer: a reference is verified when it is RESOLVED, never when its prefix matches.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v27",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v27"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    },
    "closed": false
  }
]
```
