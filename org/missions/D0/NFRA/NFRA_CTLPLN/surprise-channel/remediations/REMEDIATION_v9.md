# NFRA_CTLPLN -- remediations, v9

<sweep_watermark>2026-10-15T13:35Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-15 ~13:4xZ, at the round-19 close. Graduated in ADJUDICATION_v24.md C-S61. Two rows, ARMED. Every round-19 order is terminal (six complete).

```json
[
 {
  "id": "NFRA_CTLPLN-W106-S5",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Two live projects on different boxes both name .tools/safe_deploy_core.py in their write sets: MDPF_SECCLASS (dell1) and IRPT_BCKEND (dell2). No rule file names a single writer or merge rule for the path, so two boxes may edit the deploy core at once (FWD-7 'none is split', FWD-8 'one writer'). It is the one SPLIT of the round-19 placement read (FWD7-OVERLAPS split=1).",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W106-S5",
   "python .tools/tests/test_round19_register.py --fwd7 -> split=1 (2026-10-15 ~13:4xZ)",
   "adjudication row NFRA_CTLPLN-C-S61"
  ],
  "remedy": "P2. 1.0.0_SA_CTO names one writer for .tools/safe_deploy_core.py (or a merge rule), in the register both projects read. Done when the placement read prints split=0.",
  "owner": "1.0.0_SA_CTO",
  "round": "v24",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v24"},
  "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-W111-S1",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The intake fetch record (schema intake-fetch/1) names the fetching seat in fetched_by and carries no device key, so intake_request.py downloads --device D counts only records with a device field. On the two real 20261008 records it prints requests=0 files=0, so FWD-19's 'what did this box download today' cannot be answered by box.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W111-S1",
   "adjudication row NFRA_CTLPLN-C-S61"
  ],
  "remedy": "P2. A round-20 cell has intake_fetch.py write the device key, and the reader attributes older records by their fetched_by serial's box. Done when downloads --device laptop counts the two real 20261008 records.",
  "owner": "2.0.0_SA_COO~C",
  "round": "v24",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~C", "round": "v24"},
  "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~C", "at": null},
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
