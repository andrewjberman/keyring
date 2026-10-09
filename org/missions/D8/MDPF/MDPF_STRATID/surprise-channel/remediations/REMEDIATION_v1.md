# MDPF_STRATID -- round 1 remediations

<sweep_watermark>2026-10-09T03:29Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T03:29:00Z. Graduated at ADJUDICATION_v1: 3 rows, all INERT.

```json
[
  {
    "id": "MDPF_STRATID-D1-W1-S3",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two Cottonwood test files are red at the base, outside this project: test_cottonwood_pair_identity_cents.py (6 failures, KeyError 'custom' at build_cottonwood_mdpf_pair.py:502) and a live-state test in test_cottonwood_aua.py.",
    "evidence": [
      "investigation row MDPF_STRATID-D1-W1-S3 (0.9.0_WK_MDPF_STRATID~1); base not re-run (the row says INFERRED)"
    ],
    "remedy": "Route to the Cottonwood pair's owner (WSE_COTMDL) through 1.0.0_SA_CTO~DELL1. Close when: the owner rules the KeyError a defect with a cell, or a stale test with its retirement",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_STRATID-D1-W2-S1",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "To satisfy assert_keyset_identity, the Global-only key sma_additive_withheld was added as [] to every scope, so the Cottonwood, 49financial and Inflection served aggregate-aua-timeseries documents gain a key; C-GLOBAL-PAIR says per-firm views do not move under this project.",
    "evidence": [
      "investigation row MDPF_STRATID-D1-W2-S1 (0.9.0_WK_MDPF_STRATID~2)",
      "mdpf_gold_consolidator.py assert_keyset_identity; R2_RULED_EXTRAS has no entry for it"
    ],
    "remedy": "Rule whether an empty added key on the per-firm scopes is a move of those views. Either admit it in the never-widen pair's blast radius, or register sma_additive_withheld as a Global-only ruled extra and drop it from the per-firm scopes. Close when: the ruling is recorded and the 13:30Z served read matches it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_STRATID-D1-W2-S2",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Global's aum-metrics sma_additive component reports carried=False and as_of=frontier on a date whose sleeve value is Cottonwood's last measured value carried forward: the value states a claim (fresh) it does not hold (A VALUE MUST CARRY ITS CLAIM).",
    "evidence": [
      "investigation row MDPF_STRATID-D1-W2-S2 (0.9.0_WK_MDPF_STRATID~2)",
      "dim_mdpf_aum_metrics.py compose_current reads only agg['sma_additive_aua'][gi]; apply_sma_sleeve_overlay carries the last value forward"
    ],
    "remedy": "Carry a per-date source-date channel for the sleeve fold (as the Tax fold does) so as_of and carried are vintage-exact. Close when: on a carried date the component reads carried=True with the source date, on one served read",
    "owner": "2.0.0_SA_COO~S1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~S1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~S1",
      "at": null
    },
    "closed": false
  }
]
```
