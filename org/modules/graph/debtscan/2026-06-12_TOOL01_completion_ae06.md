# NFRA_DEBTSCAN TOOL-01 Completion + mdpf MISSING_ON_S3 finding
## 2026-06-12 — 0.6.0_AE_PartnerETL (b5050f6b2) + 2.0.0_SA_COO (exec-commit yaml)

**Provenance:** pipeline_cli.py b5050f6b2 (pushed CLOUD); comp-tools.yaml + graph-call-manifest.yaml exec-committed under COO author line.
**Tool runs:** comp-pipescript deployed (all-trees sweep) against live S3.
**Surface:** stitch graph + all 4 PIPELINE_MAP trees (bd/inf/cot/mdpf check-only).

---

## TOOL-01 DELIVERED

comp-pipescript deployed now covers all 4 pipeline trees. No-arg sweep with per-tree bucket banner:
- bd-gold -> s3://opal-data-bd: 43 MATCH
- inf-gold -> s3://opal-data-inf: 60 MATCH (1 TIMEOUT transient, re-runs clean)
- cot-gold -> s3://opal-data-cot: 47 MATCH
- mdpf -> s3://opal-data-mdpf: 15 MATCH, **3 MISSING_ON_S3**

D2-DS-01 CLOSED: the "comp-pipescript bd-only enumeration gap" finding is resolved. inf/cot/mdpf DEBTSCAN UNKNOWN-VINTAGE caveat CLOSEABLE.

---

## FINDING: TOOL-01-F01 — mdpf 3 scripts MISSING_ON_S3 (REAL, ADVISORY)

| Field | Value |
|---|---|
| family | 2a reachability + 2d compositional (stranded-deploy) |
| tool | comp-pipescript deployed --pipeline mdpf |
| scope | mdpf pipeline (opal-data-mdpf) |
| severity | ADVISORY — not yet gate-failed (fresh finding) |
| triage | REAL — 3 local mdpf scripts not found at code/scripts/<layer>/ on S3 |
| owner-lane | AE 0.6.0 or AE 0.7.0 (infra/deploy layer; mdpf layout normalization) |

**Evidence:** comp-pipescript deployed --pipeline mdpf shows 15 MATCH, 3 MISSING_ON_S3 at `s3://opal-data-mdpf/code/scripts/<layer>/` path. Root cause hypothesis: mdpf has dual S3 layout (`code/<layer>/` AND `code/scripts/<layer>/`) — the MISSING scripts are likely deployed under `code/<layer>/` (the other convention). This is the same stranded-deploy blind spot TOOL-01 was designed to surface (MDPF_COUNTS 2026-06-05 precedent).

**Resolution path:** AE follow-on TO — determine canonical mdpf S3 layout convention, normalize one path, update pipeline_cli check-only path, re-run to confirm 0 MISSING. NOT in TOOL-01 scope (ZERO mutations).

**Suppression rationale:** none — this is a real finding. Not an FP class (Deny+Principal:* / designed twin / schema alias).

---

## DEVIATION RATIFIED: mdpf as check-only tree (COO+CTO acceptance)

mdpf is NOT added to safe_deploy_core.PIPELINE_MAP. Rationale accepted:
- Rule 13 documents PIPELINE_MAP as the deploy gate (bd/inf/cot only)
- mdpf has inconsistent S3 layout (code/<layer>/ AND code/scripts/<layer>/)
- mdpf layers include backfill/feeders not in VALID_LAYERS
- Resolution: mdpf appended as explicit documented CHECK-ONLY tree in pipeline_cli
- First-class deploy-gated mdpf = separate future TO (normalize layout first)
