# Deploy-completion ledger: mdpf-pipeline /mdpf/custody_source SSM param (TF-managed)

**Status:** OPEN (deploy in progress)
**Opened:** 2026-07-07T15:45Z
**Agent:** 0.5.0_AE_OpalETL
**Authorization:** COO GO 20260707T153523Z (drift-landmine fix, ADVI_ETLFIX.WS3 byproduct finding)

## Scope
Single additive resource: `aws_ssm_parameter` `/mdpf/custody_source` = `"schwab"` (String, Standard
tier -- Standard CANNOT carry expiration policies) in `infra/aws/terraform/mdpf-pipeline/ssm.tf`.
No Lambda code change: deployed mdpf-daily-trigger verified BYTE-IDENTICAL to repo this session
(CodeSha256 vintage 2026-07-01, diff clean), so the original fix plan's redeploy leg is unnecessary.

## Why (urgency-upgraded from landmine to armed regression)
The param existed until ~15:01Z today (trigger's GetParameter SUCCEEDED, CloudTrail evt 15:01:02Z,
stamped CUSTODY_SOURCE=schwab into the nightly dispatch) and was GONE by 15:16Z (ParameterNotFound;
describe-parameters /mdpf empty; NO DeleteParameter/DeleteParameters event in trail -- consistent
with an advanced-tier TTL expiration policy on the original hand-created param). With it absent,
the NEXT nightly fire resolves the fail-safe 'bd' -> the convergence gate keys off BD silver AND
WS-E computes the retired BD custody basis -> the served 49F custody basis silently regresses.

## Steps
- [x] Ledger opened
- [ ] ssm.tf authored + committed
- [ ] terraform plan (expect 1 add / 0 change / 0 destroy)
- [ ] safe-apply
- [ ] 0-diff plan
- [ ] Live verify: get-parameter -> schwab
- [ ] CHANGELOG + tag mdpf-pipeline-v1.2.1 + push --follow-tags
- [ ] Exercised leg: next nightly bootstrap stamps CUSTODY_SOURCE=schwab (pending -- tracked under
      the WS-3 freshness watch; RAVC notes it explicitly as the outstanding exercise)
