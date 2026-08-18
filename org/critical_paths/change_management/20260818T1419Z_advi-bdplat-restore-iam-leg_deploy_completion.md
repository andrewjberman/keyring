# Deploy-completion ledger -- ADVI_BDPLAT_RESTORE.TO-1 (AE leg): bd-exporter-ec2-role +ADVI Schwab silver read

**Opened:** 20260818T1419Z by 0.7.0_AE_CloudOps. **GO chain:** COO re-sequence 130725Z -> AE mechanism 132226Z (COO-validated 132953Z) -> joint TO @8c25748037 -> DS deploy LANDED 141842Z (B_00/D_02/A_01 sha256==HEAD f71e767d33) = implicit GO (COO 135054Z) + DS explicit GO 141854Z.
**Change:** infra/aws/terraform/bd-pipeline/iam.tf @7b706eec4c -- NEW aws_iam_role_policy.bd_exporter_monolith_schwab_advi_read (monolith-schwab-08335338-silver-read): s3:GetObject on arn:aws:s3:::opal-data-assets/schwab/08335338/silver/* + s3:ListBucket on the bucket prefix-conditioned schwab/08335338/silver/*. SEPARATE from the 08242234 (MDPF) grant -- two-buckets law. Plan 1 add / 0 change / 0 destroy.
**Why:** deployed B_00.canonical_holdings now reads the LIVE ADVI Schwab RPS home (fact_rps) and FAILS LOUD (rc=2 AccessDenied) without it -- must land before the 23:01Z scheduled chain.
**Status: OPEN.**

| Leg | Act | Proof | State |
|---|---|---|---|
| A-1 | safe-apply @7b706eec4c | rc + 1 added; post-apply plan 0-diff | PENDING |
| A-2 / BP-3 | simulate-principal-policy bd-exporter-ec2-role s3:GetObject on the exact fact_rps date=2026-08-17 key = allowed; ListBucket w/ prefix context = allowed; NEGATIVE control same shape under 08242234 = implicitDeny; each its own invocation | PENDING |
| BP-5 | SERVED platinum/firm/header_metrics.json as_of = T-1 + mtime in the 23:01Z window; reported as TWO NAMED DELTAS (T-1 content refresh vs +17-account master switch) | PENDING (after 23:01Z scheduled run) |
| BP-6 | chain log: PHASE_D4 reached, "D_04 done (rc=0)" | PENDING (after 23:01Z) |

**Rollback:** git revert @7b706eec4c + safe-apply (pure-add policy; removing it re-breaks B_00 loud, not silent).
**Closed:** {CLOSE}
