# Deploy-Completion Ledger -- COTETL DATEMODE-C: holdings daily silver cadence

- **TO:** ADVI_COTETL.AUAFIX-DATEMODE-C
- **Owner:** 0.7.0_AE_CloudOps
- **Authority:** CTO 145458Z GO (cadence ruling) + COO DATEMODE-C TO 145714Z; DS silver-side co-author 145728Z
- **Opened:** 2026-06-22T14:59:11Z
- **Status:** OPEN
- **Resource:** `aws_ssm_document.cot_silver_run` (opal-cot-silver-run) in `infra/aws/terraform/cot-pipeline/ssm.tf`
- **Module:** `infra/aws/terraform/cot-pipeline/`

## Change

Add a NON-GATING daily holdings refresh to the opal-cot-silver-run SSM runCommand chain so cot
holdings silver auto-advances daily (the AUA basis) -- closing the go-forward re-freeze gap from the
DATEMODE-A/B CurrentDay->Custom fix. holdings stays OUT of `_SILVER_STAGE_TABLES` (sentinel
unaffected; CHAINFIX intent preserved). Failure-tolerant brace-group `{ ... || echo; } &&` (DS pattern)
so a holdings failure never breaks the && chain to `--finalize` (gold still fires on the 4 gated tables).

## Steps (each marked at completion)

- [ ] ssm.tf edited (description + holdings non-gating brace-group before --finalize)
- [ ] safe-commit (ssm.tf + this ledger)
- [ ] terraform plan -- expect 1 in-place update (cot_silver_run), 0 destroy
- [ ] safe-apply (HALTGT checkpoint)
- [ ] 0-diff re-plan
- [ ] verify deployed doc (aws ssm get-document carries the holdings line)
- [ ] push --follow-tags
- [ ] RAVC CTO + COO (+ DS)

## Closeout

(Closed on apply-verified. BINDING VERIFY-GATE per the TO: served cot AUA data_as_of continues
advancing past 06-18 on tomorrow + day-after nightlies, not re-capped -- validate-on-served, no
ad-hoc gold run.)
