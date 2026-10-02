# ETFS_RIVALS -- round 4 remediations (site-Z fabric): the L10 slug

<sweep_watermark>2026-10-01T22:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO~RV, 2026-10-01. Graduated at round 4's L9 (`adjudications/ADJUDICATION_v4.Z.md`). Three items. One stays ARMED (W4-S9, bounded by procedure only). The slug goes to 1.0.0_SA_CTO~Z for the round-4 analysis.

```json
[
  {
    "id": "ETFS_RIVALS-Z-W4-S9",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The marker-driven G1 run of rivalfunds-build-canonical-shape-lambda takes about 12 s per report date and grows with history, so any batch of more than about 45 dates (a backfill, a long outage's catch-up) exceeds the 900 s Lambda ceiling. It recovers only because written objects persist across the async retry.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W4-S9 (0.9.0_WK_ETFS_RIVALS~4): batch d5-gqgu-00 696.7 s, -01 858.1 s, -02 request 836e425a timeout at 900000 ms at 18:31:57Z",
      "investigation row ETFS_RIVALS-Z-S12: bounded by procedure ('no bulk import without windowed G1'); no code bound exists",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R4_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Bound a marker-driven G1 run in code (window it by date and continue across invocations, or chunk a bulk batch at the producer) so any batch size completes inside the ceiling. Proved by a batch above 45 dates.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v4"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~RV",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-W4-S7",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The device identity that runs WORLD acts on site Z (user/Andrew_Berman) holds AdministratorAccess, so a never-widen half's negative control ('a Put on an unrelated prefix stays DENIED') is vacuous for it: simulate-principal-policy allows Put on any bucket, a nonexistent one included. The act's real limit is the signed text and the actor's discipline, not IAM.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W4-S7 (0.9.0_WK_ETFS_RIVALS~4)",
      "DRAIN_END_READ_ROUND4.md:55: 'the negative control ran on the stage roles (S7)'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R4_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The CTO decides whether a WORLD act's device identity gets a scoped role (so a half's negative control means something), or whether halves stop writing identity-level controls and name the stage roles as the control's subject.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-W4-S14",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "d-5.AC2 reads every served G1 and G5 parquet of the replay window one at a time, so it takes 353-382 s and returns rc 124 under a worker's 120 s bound. A criterion that cannot finish inside the runner's bound reads as a failure that is not one.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-W4-S14 (0.9.0_WK_ETFS_RIVALS~4): rc=124 at 121 s twice; PASS 0 failures in 353 s under timeout 600",
      "DRAIN_END_READ_ROUND4.md:87",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R4_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The issuer's check reads the served objects in parallel or over a sampled window, or the order states the check's own time bound, so the worker's runner and the check agree.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v4"
    },
    "closed": true
  }
]
```
