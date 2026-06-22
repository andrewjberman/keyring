# Deploy-Completion Ledger -- COTETL DATEMODE-C: holdings daily silver cadence

- **TO:** ADVI_COTETL.AUAFIX-DATEMODE-C
- **Owner:** 0.7.0_AE_CloudOps
- **Authority:** CTO 145458Z GO (cadence ruling) + COO DATEMODE-C TO 145714Z; DS silver-side co-author 145728Z
- **Opened:** 2026-06-22T14:59:11Z
- **Status:** CLOSED (apply-verified 2026-06-22T15:00Z; commit ded252bae)
- **Resource:** `aws_ssm_document.cot_silver_run` (opal-cot-silver-run) in `infra/aws/terraform/cot-pipeline/ssm.tf`
- **Module:** `infra/aws/terraform/cot-pipeline/`

## Change

Add a NON-GATING daily holdings refresh to the opal-cot-silver-run SSM runCommand chain so cot
holdings silver auto-advances daily (the AUA basis) -- closing the go-forward re-freeze gap from the
DATEMODE-A/B CurrentDay->Custom fix. holdings stays OUT of `_SILVER_STAGE_TABLES` (sentinel
unaffected; CHAINFIX intent preserved). Failure-tolerant brace-group `{ ... || echo; } &&` (DS pattern)
so a holdings failure never breaks the && chain to `--finalize` (gold still fires on the 4 gated tables).

## Steps (each marked at completion)

- [x] ssm.tf edited (description + holdings non-gating brace-group before --finalize)
- [x] safe-commit (ssm.tf + this ledger) -- ded252bae
- [x] terraform plan -- 1 in-place update (cot_silver_run), 0 add / 0 destroy
- [x] safe-apply (HALTGT checkpoint clean) -- Apply complete: 0 added, 1 changed, 0 destroyed
- [x] 0-diff re-plan -- "No changes. Your infrastructure matches the configuration."
- [x] verify deployed doc -- live opal-cot-silver-run runCommand carries the holdings non-gating brace-group
- [x] push --follow-tags
- [x] RAVC CTO + COO (+ DS)

## Closeout

CLOSED apply-verified 2026-06-22T15:00Z. The live opal-cot-silver-run SSM doc now runs
`{ cot_silver_merge.py --table holdings || echo WARN; } &&` between --table unrealized and --finalize
(non-gating, sentinel-decoupled). No stranded leg; single in-place SSM-doc update, 0 destroy.

BINDING VERIFY-GATE (rides the next 2 nightlies, NOT part of this ledger close): served cot AUA
data_as_of continues advancing past 06-18 on tomorrow (06-23) + day-after (06-24) nightlies, not
re-capped -- validate-on-served, no ad-hoc gold run. RAVC COO on each.
