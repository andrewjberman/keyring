# MDPF_SECCLASS -- round 21 remediations (dell1)

<sweep_watermark>2026-10-12T10:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T10:20:00Z. Graduated at ADJUDICATION_v19: 4 rows (D1-W83-S5 ARMED; D1-W80-S3, D1-W80-S4, D1-W83-S4 INERT).

```json
[
  {
    "id": "MDPF_SECCLASS-D1-W83-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "C_06's incremental fires never re-derive a retained date while B_00 keeps moving that date's canonical bytes (2026-10-06/07/08 content moved 2026-10-11T04:16:35Z and 2026-10-12T00:33:48Z); the watermark is 2026-10-09 and no later partition exists, so the next default fire re-serves none of them and the served totals for those dates stay on superseded content.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W83-S5",
      "adjudication row MDPF_SECCLASS-D1-C-S9",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/W78_PARTITION_REWRITE_WRITER_20261012.json"
    ],
    "remedy": "The CTO rules: a one-off correction of the retained dates by rebuild from their canonical partitions, or acceptance of the drift on the record. Close when: either the rebuilt dates' served totals equal a rebuild from the current canonical bytes (beside an untouched control date), or the acceptance is recorded with the dates and dollars it leaves.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v21",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v21"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": "2026-10-14T11:42:16Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-D1-W80-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C_06's incremental summary write builds advisor_daily_new only from the fire's new partitions, so an advisor with no new date in a fire is absent from that fire's mix_daily_summary.json payload. Pre-existing; not measured live.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W80-S3",
      "adjudication row MDPF_SECCLASS-D1-C-S10"
    ],
    "remedy": "Measure first: compare the advisor set of two consecutive served mix_daily_summary.json versions against the advisors with any date. Close when: the read shows no advisor dropped (not a defect), or a fix keeps every advisor and a served version proves it.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v21"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W80-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "SC-e-91's retained revisit sees only each date's stored top-10 holdings per relationship: of the 2026-10-09 mix-level Unclassified $1,846,399.46, $1,326,892.62 (71.86%) is listed and $653,857.12 resolves now; $519,506.84 (28.14%) moves only by a rebuild of the date.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W80-S4",
      "adjudication row MDPF_SECCLASS-D1-C-S7",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_RETAINED_UNCLASSIFIED_20261012.md (Reach)"
    ],
    "remedy": "The CTO rules whether a rebuild cell for 2026-10-06..09 is warranted (with D1-W83-S5). Close when: a rebuild moves the unlisted share and a served read shows it, or the limit is accepted on the record.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v21"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-W83-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "comp-pipescript io lists B_02 as an implicit writer of CANONICAL_HOLDINGS_PREFIX, while the code shows B_02 reads that prefix and writes only canonical_lots keys, so the tool's writer set for the canonical holdings prefix overstates by one.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W83-S4",
      "adjudication row MDPF_SECCLASS-D1-C-S10"
    ],
    "remedy": "The tool distinguishes a read of a prefix constant from a write to it. Close when: comp-pipescript io lists only B_00 as the writer of CANONICAL_HOLDINGS_PREFIX, beside a control script whose real write is still listed.",
    "owner": "0.0.0_AB_MSTR",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR",
      "round": "v21"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": null
    },
    "closed": false
  }
]
```
