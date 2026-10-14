# MDPF_SECHIST -- round 5 remediations (dell1)

<sweep_watermark>2026-10-13T18:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T18:50:00Z. Graduated at ADJUDICATION_v6: 3 rows (Z-S2 disarmed with work owed; D1-S1 and D1-S6 INERT).

```json
[
  {
    "id": "MDPF_SECHIST-Z-S2",
    "project": "MDPF_SECHIST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The SH-t-8 take of etf_daily_pull.py (blob 75342a6958) reached site Z's shared tree through box-sync 574fe5ce6b before its NEVER-2 ledger existed: box-sync is not gated on a producer/ledger pair. This instance is closed (ledger CLOSED, scheduled runs accepted).",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECHIST_R5_D1_S2_Z_S2_DISARM_PREREAD_20261011.md @ba3522e2f5",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/DISARM_EVIDENCE_D1_S2_Z_S2_20261011.md @2de5d9fbef",
      "3.0.0_SA_CVO read s3://opal-data-etfs/bbg/2026-10-12/run_manifest.json: LastModified 2026-10-13T14:39:56Z, run_class scheduled, history_gap_fill and history_backfill_exhausted PRESENT; bbg/2026-10-13/run_manifest.json NoSuchKey (that pull is due 10-14)",
      "adjudication row MDPF_SECHIST-D1-C-S3"
    ],
    "remedy": "Gate box-sync's integration of a scheduled producer's code on an open or closed ledger entry for that producer (the integration-path question the row assigns). Close when: a box-sync carrying a producer change with no ledger entry is refused, beside a control that carries a ledgered change.",
    "owner": "0.0.0_AB_MSTR~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~Z",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~H1",
      "at": "2026-10-13T18:50:00Z"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECHIST-D1-S1",
    "project": "MDPF_SECHIST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "SH-t-19's depth bound marks a ticker exhausted for good when its backfill returns zero rows; a per-security vendor error returned as an empty response also reads as zero, so a transient error can exhaust a ticker permanently.",
    "evidence": [
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/L8_PACKET_MDPF_SECHIST_ROUND5_20261013.md @cfe2c63636 (blob 94f159fdd3, verified)",
      "adjudication row MDPF_SECHIST-D1-C-S4"
    ],
    "remedy": "The staged expiry cell (r6_staged/SH_EXHAUSTED_EXPIRY_CELL_STAGED.md): an exhausted entry expires and is retried. Close when: an exhausted ticker past its expiry is re-requested, beside a control inside the window that is skipped.",
    "owner": "2.0.0_SA_COO~H1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~H1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~H1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECHIST-D1-S6",
    "project": "MDPF_SECHIST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The live cot-satellites-characteristics-producer package vendors etf_positioning_gold.py at 09408b19e5, four SECHIST commits behind HEAD, so the MMF rule (FWD-9) does not reach its served values; the effect is unmeasured.",
    "evidence": [
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/L8_PACKET_MDPF_SECHIST_ROUND5_20261013.md @cfe2c63636 (blob 94f159fdd3, verified)",
      "adjudication row MDPF_SECHIST-D1-C-S8"
    ],
    "remedy": "Decide and, if decided, redeploy the characteristics producer under its own never-widen pair. Close when: its live package carries the HEAD rule by content, or a recorded ruling keeps it pinned with the served effect measured.",
    "owner": "2.0.0_SA_COO~H1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~H1",
      "round": "v5"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~H1",
      "at": null
    },
    "closed": false
  }
]
```
