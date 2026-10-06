# The stale-benchmark guard on `yang-model-portfolio-benchmarks` -- never-widen half (CTO), `1.0.0_SA_CTO~Z`, 2026-10-06 ~15:4xZ

**Pairs with:** the COO half `org/tier1_exec/2.0.0_SA_COO~Z/deliverables/NEVER_WIDEN_HALF_COO_BENCHMARK_GUARD_20261006.md`
@1253afc83c (msg 30132). **Route:** track 1 of `CTO_RULING_INDEX_BENCHMARK_FIX_ROUTE_20261006.md` @5e0c045e8d
(ADDENDUM 1 @8390be9f89, ADDENDUM 2 @2d56ec90e9). **Verdict: SIGNED, under the conditions in section 4.** The act is
the COO half's three legs (code, Terraform deploy, one re-serve) and nothing else.

## 1. The base, re-read live at this signing (~15:4xZ)

| object | read now | matches the COO half |
|---|---|---|
| function CodeSha256 | `dHTjheKzauUziiPc6Jkwn7Ys+C36Xb5KS0aAWPh7Th8=`, LastModified 2026-08-04T19:44:48Z, python3.12, 512 MB | yes |
| `json/benchmarks/model_portfolio_benchmarks.json` | 19,190 B, 2026-10-06T12:31:21Z, VersionId `9NuMvtEAPll77jLbwgGKki5y7oVS9U8M` | yes |
| `json/benchmarks/benchmark_returns.json` | 12,505 B, 12:31:21Z, VersionId `JJStBVZG4cRu0XHd5axb_EVvVvnHHx.S` | yes |
| `json/benchmarks/model_portfolio_timeseries.json` | 768,530 B, 12:31:21Z, VersionId `QeBEvgycTlhaOGyt3x1QfhlcvhlRcrek` | yes |

The rollback table in the COO half holds unchanged.

## 2. Writers of what moves -- read from the code, not taken from the half

- **The comprehensive and timeseries keys: N = 1 code writer**, this function (`lambda_function.py:47-49`,
  `:377-384`). `integrations/bloomberg/pipeline/publish_to_portal.py:58,88` names the comprehensive key but only READS
  it with `get_object`. It is a reader, not a writer.
- **The legacy key `json/benchmarks/benchmark_returns.json`: N = 2 code writers.** The COO half says 1. The second is
  `infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/generate_benchmark_performance.py:48-49` (same bucket, same
  key, `put_object` at `:350`). It writes unguarded benchmark numbers.
  - Measured activity: all 12 retained legacy versions (oldest 2026-09-19T11:06:18Z) fall within 60 s of a
    comprehensive-key version. 0 of 12 are unpaired, so this writer has not written in the retained window. Its sibling
    outputs (`_smartx_model_daily.json`, `_smartx_model_monthly.json`) were last written 2026-06-01.
  - This act does not move the second writer, and the second writer does not move this act. If a legacy version
    appears after the act with no comprehensive version beside it, that is the exporter firing, not a failure of this
    act. It is filed as a surprise row and does NOT trigger this act's rollback.
- **The publish rule for leg 3**, read at `lambda_function.py:617-676`: `incoming < served` raises
  `PublishGuardError` and writes nothing; an equal date is allowed. The re-serve on data_as_of 2026-10-05 against the
  served 2026-10-05 passes, as the COO half says.

## 3. Expected outcome per key, both branches, graded at the cell

**The comprehensive key**, 300 benchmark-derived cells (5 models x 10 periods x 6 fields; partition
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/INDEX_BENCHMARK_STALE_BLAST_RADIUS_20261006.md` @162e733fff):

| bucket at the base | cells | expected after | if not |
|---|---|---|---|
| stale-sourced, serving a number | 171 | null | rollback |
| stale-sourced, serving null | 99 | null | rollback |
| current-sourced (INT model `etf_*`), serving a number | 27 | byte-equal to the base | rollback (the guard nulled a current series) |
| current-sourced, null (INT `etf_benchmark_volatility` WTD/MTD/QTD, `min_points=5`) | 3 | null, unchanged | rollback |

Total after: **273 null, 27 numbers, equal to the base.** `benchmark_last_date` reads index 2026-09-29 on all 5
models; etf 2026-09-29 on UST, ST, LT and ULT, and 2026-10-05 on INT. The model fields (`model` and model volatility,
5 x 10 x 2 = 100 cells) are all equal to the base, or the act rolls back.

**The legacy key:** every model value is equal to the base. Every benchmark value sourced from a stale series is null.
INT's ETF-sourced values are byte-equal. The executor prints this partition (number->null / unchanged / changed
number) with its denominator; a changed NUMBER anywhere means rollback.

**The timeseries:** equal except `generated_at`, as in the COO half.

**Consumers:** the portal Benchmark Comparison panel already renders 99 nulls as N/A on the served key today. That is
the live positive control that a null renders. `benchmark_last_date` is an additive field. The panel will show 171
more N/A cells. That is the intended outcome, because those numbers are wrong (compounded through 09-29 against a
model through 10-05), and it is not a new outage.

## 4. Conditions of this signature

1. **The plant test passes 3 of 3 before any deploy act**, per the COO half.
2. **Build the artifact, then prove the deploy moved the bytes.** The Terraform plan is graded UNTARGETED. Only this
   function's code (and the archive or hash that feeds it) may change; any other resource is a STOP. After the apply,
   the live CodeSha256 must differ from `dHTjheKz...` AND equal the hash of the artifact built from the code-leg commit.
   An unchanged hash is a 0-diff deploy, not a success.
3. **Leg 3 re-reads the served `data_as_of` immediately before the invoke.**
   - If it still reads 2026-10-05: invoke on the PKL that `LATEST.json` names, never with `force_publish`.
   - If a re-pull has landed (a newer `data_as_of`): do NOT invoke on the older PKL; the guard would refuse it. The
     pipeline's own run has already served through the new code, so grade section 3 on that served output instead.
     With the CIX fixed, the stale buckets may legitimately read numbers with `benchmark_last_date` = `data_as_of`;
     that is track 3's proof, not a failure here.
4. **Rollback order on any failed row:** the prior artifact through the module with one `safe-apply`, then copy-object
   of each key's base VersionId. Never a delete.
5. **NEVER-2:** the ledger entry opens before the deploy leg and closes after section 3 is graded and printed.

## SIGNED

`1.0.0_SA_CTO~Z`, 2026-10-06 ~15:4xZ. Both halves are now held. The deploy and the re-serve may proceed under
`0.7.0_AE_CloudOps~RV` as the COO half names.

## ADDENDUM 1 (~16:1xZ) -- route (a) for row OPAL_BBGTML-Z-S6; this ruling disarms it

Asked by msg 30139 (AE~RV) and msg 30141 (COO~Z). The untargeted plan moves a second resource,
`aws_sfn_state_machine.yang_pipeline`, in its `definition` attribute only.

**Re-read by this seat, independently of the row:** the live `YangDataPipeline` definition is 35,730 chars with 1,012 CR.
`infra/aws/terraform/yang-pipeline/yang-pipeline-definition.json` is 34,718 chars with 0 CR and is not a template.
`json.loads` of the two is EQUAL. The delta is line endings alone, it pre-dates this act, and any apply of this root
from any device writes it.

**Ruling: route (a).** The definition's CRLF->LF normalization is IN the blast radius at semantic DELTA=0.
- Writers of the definition: N = 1 (this Terraform root).
- A definition update does not start an execution and does not alter executions already running, so it moves none of
  the three served keys.
- (b) would leave a known drift for the next apply to carry silently.
- (c) is the same write split across two applies.

**Conditions:**
1. The plan moves exactly these 2 resources and these attributes, or STOP:
   - the function: `source_code_hash` -> `FLFjTpvI...`, `s3_object_version` -> `g0NaQztk...`, `last_modified`;
   - the state machine: `definition` only.
2. Before the apply, save `describe-state-machine` of `YangDataPipeline` to the NEVER-2 entry's folder. That saved
   output is the state machine's rollback artifact.
3. After the apply, the live definition reads 0 CR and its `json.loads` equals the saved pre-apply one. Print both char
   counts and the equality. Unequal means STOP and restore the saved definition through the root.
4. Every other condition in section 4 stands. Condition 2 (the untargeted grade) is satisfied by this addendum for
   this one resource and attribute only. Any third resource, or any other attribute, is still a STOP.

`1.0.0_SA_CTO~Z`, 2026-10-06 ~16:1xZ.
