# AMGT_CORPUS -- round 40 remediations (dell1)

<sweep_watermark>2026-10-09T16:28Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T16:28:00Z. Graduated from ADJUDICATION_v47 (held there): 3 rows, all INERT.

```json
[
  {
    "id": "AMGT_CORPUS-Z-S90",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The read-only code census resolves 80 of 86 write-like calls and leaves 6 'unresolved' in the induction request/scheduled files, so test_code_census_arm_leaves_no_amgt_corpus_entry exits 1 on the shared tree.",
    "evidence": [
      "investigation row AMGT_CORPUS-Z-S90",
      "ADJUDICATION_v47 @14b9c9ac52 (held there)"
    ],
    "remedy": "Classify the six (legitimate opt-in writes the census learns to resolve, or a regression of the read-only bound that is reverted). Close when: the census test passes on the shared tree with the six named",
    "owner": "2.0.0_SA_COO~X",
    "round": "v41",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~X",
      "round": "v41"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~X",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_CORPUS-Z-W2-S22",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ap6_check.py arm b4 (pdf dash) reads 1 with or without the amendment, because its lines carry no bold_all and no above-median size, so the check cannot see the pdf half of the rule.",
    "evidence": [
      "investigation row AMGT_CORPUS-Z-W2-S22",
      "ADJUDICATION_v47 @14b9c9ac52 (held there)"
    ],
    "remedy": "Give arm b4 a line the pdf heading rule would flag without the amendment. Close when: b4 reads 0 on the pre-amendment code and 1 on the amended code",
    "owner": "2.0.0_SA_COO~X",
    "round": "v41",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~X",
      "round": "v41"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~X",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_CORPUS-D1-S1",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "build_unit_map writes 'no value returned' for the dispersion fields on names never requested for them (outside the 96 the daily fire refreshes, raw older than CRPS-ap-7), so not-requested reads the same as requested-and-empty.",
    "evidence": [
      "investigation row AMGT_CORPUS-D1-S1",
      "ADJUDICATION_v47 @14b9c9ac52 (held there)"
    ],
    "remedy": "Give the builder's reason text separate values for not-requested and requested-and-empty. Close when: NVDA US, CAT US, CSL AU, 6861 JP read not-requested and a requested-and-empty name still reads no value returned",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v41",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v41"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": false
  }
]
```
