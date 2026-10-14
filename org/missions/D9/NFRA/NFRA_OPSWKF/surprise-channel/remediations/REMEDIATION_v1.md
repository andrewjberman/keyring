# NFRA_OPSWKF: remediations, round 1 close

<sweep_watermark>2026-10-14T13:15Z</sweep_watermark>

L10 by `3.0.0_SA_CVO~DELL2`, 2026-10-14T13:15Z. Follows ADJUDICATION_v4. Graduated, round label v2: 5 rows, all OPEN and INERT, the
enrichment list the CTO's round-N analysis cuts from at resume (~2026-10-27, or Andrew's earlier word). ARMED: 0.

```json
[
 {
  "id": "NFRA_OPSWKF-D2-S1",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "pytest over trade-workflow-handler/tests errors 3 times from test_actor_identity.py's __main__-only fixture; no round-1 cell owned it.",
  "evidence": ["investigations/INVESTIGATION_v1.md#NFRA_OPSWKF-D2-S1", "resume packet @dc5fb064c4: enrichment FWD-1 repair batch, not re-run 2026-10-14"],
  "remedy": "One small LOCAL repair cell at resume; the suite collects with 0 errors.",
  "owner": "2.0.0_SA_COO~O2",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O2", "round": "v2"},
  "closed": false
 },
 {
  "id": "NFRA_OPSWKF-D2-S2",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "parquet_exporter.py imports pyarrow at module top while the function's only layer is openpyxl; whether any live path reaches the import is unmeasured.",
  "evidence": ["investigations/INVESTIGATION_v1.md#NFRA_OPSWKF-D2-S2", "resume packet @dc5fb064c4"],
  "remedy": "At resume: measure whether a live path reaches the import; if one does, the import moves or the layer gains pyarrow.",
  "owner": "2.0.0_SA_COO~O2",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~O2", "round": "v2"},
  "closed": false
 },
 {
  "id": "NFRA_OPSWKF-D2-W5-S2",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The trade-request form's firm field starts blank and an internal login's firm id is opal-capital, so a partner firm cannot be chosen from the form.",
  "evidence": ["investigations/INVESTIGATION_v1.md#NFRA_OPSWKF-D2-W5-S2", "resume packet @dc5fb064c4: held scope item 1 (external trade request)"],
  "remedy": "Carried by the held external trade-request design (firm-scoped client and account search), cut at resume.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~DELL2", "round": "v2"},
  "closed": false
 },
 {
  "id": "NFRA_OPSWKF-D2-S8",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "FWD-9 refuses a partner-firm advisor that FWD-1's ACCEPT lets file: the two outcomes disagree on the external filer.",
  "evidence": ["investigations/INVESTIGATION_v1.md#NFRA_OPSWKF-D2-S8", "msg 5817 (owner 1.0.0_SA_CTO~DELL2)"],
  "remedy": "The round-N analysis reconciles FWD-1 and FWD-9 for the external filer as part of the held external trade-request design.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~DELL2", "round": "v2"},
  "closed": false
 },
 {
  "id": "NFRA_OPSWKF-D2-S12",
  "project": "NFRA_OPSWKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "infra/aws/terraform/trade-pipeline/secrets.auto.tfvars (80 bytes, gitignored, never tracked) sits on disk in the shared dell2 checkout.",
  "evidence": ["investigations/INVESTIGATION_v1.md#NFRA_OPSWKF-D2-S12", "CTO ruling msg 7657: no delete, no rotate", "resume packet @dc5fb064c4 (dc5fb064c4 carries the ruling)"],
  "remedy": "Per the CTO's ruling: at resume, move the value to a managed secret and out of a local tfvars file; nothing is deleted or rotated before then.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v2",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO~DELL2", "round": "v2"},
  "closed": false
 }
]
```
