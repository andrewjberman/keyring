# MDPF_SECCLASS -- round 1 remediations

<sweep_watermark>2026-09-30T02:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30. Graduated at round 1's L9 (ADJUDICATION_v1.md).

```json
[
  {
    "id": "MDPF_SECCLASS-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The FWD-7 backfill has no ticker-keyed cottonwood source and a 2026-08-07 inflection source, so it cannot resolve cottonwood's tickers; IRPT_BCKEND IB-mr-251's cottonwood refusals survive it.",
    "evidence": [
      "R1_BACKFILL_CENSUS_20260929.json: cottonwood held 0, inflection as_of 2026-08-07",
      "investigation row MDPF_SECCLASS-S2 (2.0.0_SA_COO~M, 2026-09-30T00:25Z)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P1: a firm-tree caller of the scheduled classification for cottonwood and a current one for inflection (C-FIRM); the IR Holdings producer's per-firm symbol sets are the nearest ticker-keyed source. Disarm when the census reads held tickers for all three firms with a current as_of.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v2"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C-WRITER names two writers and two classified_by values, but 238 of 2,309 live rows carry no classified_by at all: the constituents seeder's rows (CTO 103050 ruled it 'any other writer') and any earlier hand-written row.",
    "evidence": [
      "aws dynamodb scan etf-classifications by this seat 2026-09-30 02:4xZ: 2,309 rows, one page; classified_by seed 137, scheduled 1,934, absent 238",
      "investigation row MDPF_SECCLASS-S1 (2.0.0_SA_COO~M); CTO ruling 103050 on the constituents seeder",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P2: label or re-seed the 238 rows so every row carries one of the two values, or 1.0.0_SA_CTO amends C-WRITER to name the constituents seeder. Disarm when the scan reads 0 absent.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W2-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "instrument_kind is absent on 2,163 of 2,309 rows (present: fund 135, single_security 11). The seed path writes it only on net-new rows and the backfill wrote none, so FWD-8's ACCEPT ('each entry says fund or individual stock') is far from met.",
    "evidence": [
      "the same scan: instrument_kind absent 2,163, fund 135, single_security 11",
      "investigation row MDPF_SECCLASS-W2-S3 (0.9.0_WK_MDPF_SECCLASS~2)",
      "DRAIN_END_R1_20260930.md carried item 3",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P1: an instrument_kind-only update mode over the 157 constituent rows and the 1,934 scheduled rows, with the Schwab and GICS inputs wired; read back by the same scan.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W3-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "D_04.build_advisor_positions._classify_ticker is a fourth classify site; platinum/advisors/{id}/positions.json still carries only the coarse asset_class.",
    "evidence": [
      "row W3-S3; the cell's never-widen half, blast radius section 2",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P2: route build_advisor_positions through _classify_with_canonical, or the issuer rules the frozen ADVI_49EXEC.md Section 4.5 wire contract out of scope; either way FWD-4's census must list the site until then.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    },
    "closed": false
  }
]
```
