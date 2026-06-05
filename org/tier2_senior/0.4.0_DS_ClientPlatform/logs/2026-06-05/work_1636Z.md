# 0.4.0_DS_ClientPlatform — /work work_1636Z (NFRA_COSTRED R2 APPLIED + verified)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, DEPLOY, COORDINATE

## NFRA_COSTRED R2 — opal-data-bd S3 version-bloat cut: ASSESSED -> STAGED -> APPLIED (Option B)

Andrew-direct R2 assessment of the opal-data-bd 2.4TB bloat. Read-first, pure metadata (no gold runs, C1 honored). Brief: `docs/briefs/nfra-costred-r2-opal-data-bd-s3-bloat-assessment-20260605.md` (f0605c878).

### Findings
- Billed 2,679 GB (growing ~50 GB/day); current 60.6 GB (2.3%); **97.7% (~2,618 GB) noncurrent-version bloat** (versioning ON + daily gold overwrite + NoncurrentVersionExpiration=90d). 10.65M versions.
- **Key independent finding:** the 90d window is NOT an accidental default — it's the deliberate retention for the LIVE Portal Time Machine (DRFR_PTMCH); bd-time-machine restores gold/ via noncurrent VersionIds. Coherent window already capped at 35d by the DynamoDB opal-portal-market-data PITR. So 35-90d versions = pure over-provisioning.
- Andrew decision arc: 30d -> 35d (took my coherence flag) -> "Approve scoped cut".
- abort-MPU-7d already existed (0 incomplete MPUs); MPU cleanup yields ~0.

### Safety (the C2 gate — fired twice)
1. **Only-copy proof** (per-key, 10.82M versions): partition cat-a 104,274 / cat-b 52,246 / cat-c 0. Whole-bucket only-copy-at-risk @36d = 7.82 GB = disposable logically-deleted code (git-authoritative) + bronze intermediates. Custodian-at-risk: **schwab=0**, silver=34MB (deleted 2021 capital_gains partitions), bronze=0.6MB. STOPPED the whole-bucket cut; proposed **gold/+platinum/-scoped** variant (structurally zero custodian risk).
2. **AE pre-apply catch:** my 3-rule HCL erroneously dropped the whole-bucket 90d (would strip noncurrent expiry from silver/bronze/schwab/code). Corrected to **4-rule Option B**: KEEP 90d + ADD gold/36d + platinum/36d + abort-MPU. S3 overlap -> 36d on gold/platinum, 90d status-quo elsewhere.

### Applied (0.7.0_AE, HALTGT IaC import-then-modify) + verified live
`get-bucket-lifecycle-configuration` = 4 rules exactly: expire-noncurrent-versions-90d (prefix="") + expire-noncurrent-gold-36d (gold/) + expire-noncurrent-platinum-36d (platinum/) + abort-incomplete-mpu-7d. RAVC2 applied-confirmation -> COO (163625Z, CC CTO+AE).

### Savings (materializes on lifecycle cycle — C1, passive scheduled read)
Baseline 2,679 GB (06-04). Expected -> ~1,500 GB as gold/+platinum/ noncurrent >36d expire (~24-48h). Recovered ~1,175 GB / ~$27/mo. **TAIL ITEM:** read BucketSizeBytes trend on the next CloudWatch daily cycle (tomorrow) to confirm the realized drop. No compute / no forced deletion.

### Rebuildability (CTO add-on, seeds GLDINC)
Source (bronze/silver) retained 5+ months write-once dated keys; rebuild deterministic-plausible but = expensive c6i run (C1-barred ad-hoc) so version-restore is the only cheap/instant path -> don't go below 35d now; below-35d is GLDINC-gated.

## Next
- R2 tail: confirm storage-trend drop on next CloudWatch cycle.
- GLDINC §5 reconcile-correctness (data-semantics co with 0.6.0) — now engaging (PRD 8c9acb101).

## Compiler Tools
| Tool | Run | Result | Notes |
|---|---|---|---|
| (S3 metadata) | get-bucket-lifecycle-configuration / list-object-versions / CloudWatch BucketSizeBytes | per findings | pure metadata reads; the right verifier for a lifecycle/versioning assessment. No comp-* gold-script tool applies (S3 infra-config, not a gold data script). |
| ds-commit-gate | py_compile on the analysis scripts (.runtmp/bd_safety_age_proof.py etc.) | PASS | analysis scripts (not committed gold); compile-checked per discipline. |

work-cycle:0012
