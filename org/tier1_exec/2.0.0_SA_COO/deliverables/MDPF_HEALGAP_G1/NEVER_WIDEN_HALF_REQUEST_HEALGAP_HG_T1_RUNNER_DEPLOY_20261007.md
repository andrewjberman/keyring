# Never-widen half, MDPF_HEALGAP round 1 -- the Rebalancer runner's guard-by-listing and induced-lapse hook reach the live Lambda (cell HG-t-1)

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-07 ~10:0xZ. **For:** `1.0.0_SA_CTO~DELL1`, the CTO half (laptop `1.0.0_SA_CTO`
rulings file `CTO_RULINGS_FOR_THE_DELLS_20261007_0930Z.md` @31e91d2d1e section 2: "the two never-widen halves are dell1's").
**Status: COO half SIGNED; CTO half owed.** No deploy happens before both halves are signed. Deploying seat: `0.7.0_AE_CloudOps~F` on
the laptop, under order `MDPF_HEALGAP.TO-HG-d1` and a change-management ledger entry it opens naming the laptop as the box.

## The act

Build `cot-rebalancer-runner` from CLOUD at a commit carrying `ca914096d7` (on origin CLOUD `e688467732`, ls-remote read by
`0.0.0_AB_MSTR~DELL1` msg 104), upload it to `s3://opal-313476888478-lambda-artifacts/opal-assets/cot-rebalancer-runner.zip`, and apply
`module.cot_rebalancer_runner` in `infra/aws/terraform/opal-assets` with `-target`, code only. Expected artifact sha
`QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=` (BUILD_ONLY on dell1 at `ca914096d7`). Live today: CodeSha256
`b1m7jUh6jC55tBfoUX20xRmmKAjB4P1Wvxnwvn2N/Fw=`, LastModified 2026-09-11T03:26:00Z, source `c53e48f7fb` per the source map.
`cot_rebalancer_reattempt.tf` is NOT in the act: it is not on CLOUD and its apply is held on PRD ACT 1 and an R20 exception.

## What changes, read from the producer's own rule

`lambda_function.py` @ca914096d7:
- `_already_landed(date)` decides by `list_objects_v2(Prefix=<stamp key>)`, exact key and `Size > 0`, instead of `get_object`, which
  the role cannot do (comp-iam: `s3:GetObject` UNGRANTED). Any exception -> False (pull), as before.
- `ingest(..., induce=None)`: after the guard and before the session read, `induce == "auth-lapse"` raises an HTTP 401 RuntimeError;
  any other non-empty value raises ValueError. `lambda_handler` passes `event.get("induce")`. The scheduled input is `{"mode":"pull"}`,
  which carries no `induce`.

**Writers counted.** `blackdiamond/cottonwood/bronze/rebalancer_{models,accounts,model_detail}/<date>/` and
`blackdiamond/cottonwood/meta/<date>-complete.json`: N = 1 rule (this runner's `ingest`). Silver for the date: N = 1 rule, the
`opal-assets-silver-blackdiamond` converter on the runner's `on_success` destination, which converts the date named by
`responsePayload.as_of` on BOTH verdicts (`mirror_conversion.py` `date_from_destination`, read 2026-10-07).

**Both branches, per invocation:**
- (A) The date's stamp is NOT listed (the 06:00Z scheduled fire, every day: stamps land at ~06:01Z, census 10-01..10-07). Behaviour is
  byte-for-byte the old one: session read, three feeds pulled and landed, stamp written, `BRONZE-COMPLETE`, silver converts the date.
  Served delta 0.
- (B) The date's stamp IS listed (only on a second invocation of the same UTC date; today nothing invokes it twice, because the
  re-attempt target does not exist). Old code: the guard fell open, so it re-pulled the vendor and re-landed every key, then silver
  re-converted. New code: `SKIP-IDEMPOTENT` with no secret read and no vendor call; silver still re-converts the same date from the same
  bronze. Served delta 0; one fewer Black Diamond call.
- (C) An event carrying `induce` (only by hand): raises before any secret read or vendor call; no key written; async retries repeat the
  raise; `on_success` does not fire. Served delta 0.

## Blast radius

The Lambda's code only. No IAM, no schedule, no invoke-config, no destination changes (criterion HG1-d1-AC2 reads all four after the
apply). No S3 data key is written by the act itself; the next 06:00Z run writes the same keys it writes today.

## Rollback

The artifact bucket is versioned (`get-bucket-versioning` Enabled, 2026-10-07). The prior object is version
`XeSy4IKGvKXGsEwBQRpeXUekk5qb.TYp` (2026-09-11T03:18:08Z, the `c53e48f7fb` build): restore it as the latest version of
`opal-assets/cot-rebalancer-runner.zip` and re-apply the same target, or revert `ca914096d7`'s two runner files and re-run the build pair.
Read back CodeSha256 `b1m7jUh6jC55tBfoUX20xRmmKAjB4P1Wvxnwvn2N/Fw=`. No data rollback exists to do (served delta 0 on every branch).

## Acceptance (the order's criteria, read from the live plane)

1. HG1-d1-AC1: live CodeSha256 equals the build sha (`hg_d1_deployed.py --code` -> `DEPLOYED-OK`). FAILS at the base today.
2. HG1-d1-AC2: invoke-config, the daily rule and its input, and `cot-bronze-complete`'s single target unchanged
   (`hg_d1_deployed.py --unchanged` -> `UNCHANGED-OK`). PASSES at the base today (a control).
3. The next 06:00Z run (branch A) lands its stamp as before: `meta/<next date>-complete.json` present at ~06:01Z.

## COO half -- SIGNED

`2.0.0_SA_COO~G1`, 2026-10-07, after the drain re-run (`GUARD-TESTS-OK`, `INDUCE-TESTS-OK`, `test_lambda_function.py` 17 OK, proof
VALID at `ca914096d7`), the BUILD_ONLY sha above, the live CodeSha256 and invoke-config reads, the stamp census, and the converter's
`date_from_destination`.
- **Blast radius, writers counted, rollback per key:** as above.
- **Not signed here:** the re-attempt target (`HG-t-2`), held on PRD ACT 1 and an R20 exception for `cot-bronze-complete`; the FWD-1
  exercise (the induced morning failure), held on ACT 1.
