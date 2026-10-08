# Never-widen half: MDPF_HEALGAP round 2, drain act 1 -- deploy the runner code (HG-t-3 per-feed result, PartialDay, drop-feed induce)

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-08 ~16:2xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Status:** COO half SIGNED; CTO half owed. Acting seat: `2.0.0_SA_COO~G1` on dell1, under a change-management entry opened
before the upload and closed after the reads.

## The act

1. `bash infra/aws/lambda/ci/build-and-upload.sh opal-assets cot-rebalancer-runner` builds and uploads from CLOUD at or after
   `0934cb05d1`. The `BUILD_ONLY` dry build read `sha256=NFG8dbELEHHI34OSdq49kTBNHdtKyeRrUNZ9K0uzMZY=` at that commit.
2. `.tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=module.cot_rebalancer_runner`.
   - Condition: the plan reads only the function's code hash in place, and nothing else in the module. Any other line refuses
     the act.
   - HG-t-5's rule hunk is outside this module target and stays held (row D1-S7).

The zip carries `lambda_function.py` (the changed handler) and `landing_guard.py` (unchanged). It also carries `repair.py`,
`mark_missing.py` and `retry_schedule.py`, which no handler path imports; their presence changes nothing at runtime.

## What changes, read from the handler's own rule (diff 8af853ce59..HEAD, `lambda_function.py`)

**Writers counted.**
- The new key `blackdiamond/cottonwood/meta/<D>-result.json` has N = 1 writer: this handler. `mark_missing.py` writes
  `<D>-missing.json`, a different key, and only from an operator run.
- The stamp `<D>-complete.json` keeps N = 1 writer: this handler.

**Triggers on the new key: none.**
- Census of 152 EventBridge rules: none matches `opal-data-assets` or `cottonwood`. `cot-bronze-complete` matches the suffix
  `_BRONZE_COMPLETE.json` in bucket `opal-data-cot`.
- The `opal-data-assets` S3 notifications on the cottonwood prefix fire only on `blackdiamond/cottonwood/bronze/` and the
  suffix `.xlsx`. EventBridge delivery on the bucket is off.
- The guard matches the exact stamp key `<D>-complete.json` (`lambda_function.py:207-208`), so `-result.json` is never read as
  a stamp.

**Branches, per day:**
- **(A) All three feeds land (every day 10-01..10-08 except the induced 10-08 06:00Z fire).**
  - The handler writes one extra key, the result, with `verdict COMPLETE`.
  - Then it writes the stamp and returns exactly as before, and `on_success` fires silver as before.
  - Served delta 0.
- **(B) A feed lists nothing after the pull (today reachable only by the new `drop-feed:<feed>` induce, or by a vendor
  returning an empty feed).**
  - **Before:** the stamp was written, the invoke succeeded, and silver ran on two of three feeds.
  - **Now:** the result is written with `verdict PARTIAL`. There is no stamp. `PartialDay` is raised, so the invoke fails and
    `on_success` does not fire. The async engine retries twice, about 60 s and 120 s apart, now bounded by the 900 s age.
    The day's next trigger (the re-attempt or the next fire) pulls again.
  - **Served effect on this branch only:** that day's silver and gold are withheld rather than built from partial bronze. This
    is FWD-2's specified behaviour (PRD v0.2) and the reason for the cell.
  - Readers of the day's bronze between the failure and the heal see what they saw before on a failed day (row D1-S7 names
    the satellites producer).
- **(C) The pull raises (auth lapse or vendor error).**
  - Unchanged, except that the handler first tries to write the result. The write fails soft: it prints a `WARN` line and
    never masks the original error.
  - `healed_at` reads `null` live: the role has no `s3:GetObject` on `meta/` (ruling R2-1, row D1-W3-S1).

**Vendor calls.** The number of calls per invoke is unchanged on branches A and C. On branch B, a `drop-feed` invoke makes
fewer calls (the dropped feed is skipped). A retry re-pulls exactly as any failed invoke did before.

## Blast radius

- **Code:** one function's code.
- **Keys:** one new S3 key per date under `meta/`.
- **Silver:** one changed outcome, the partial-day branch, as stated above.
- **Untouched:** IAM, triggers, destinations, schedules and inputs.

## Rollback

| what | state today |
|---|---|
| Lambda CodeSha256 | `QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=`, LastModified 2026-10-07T10:44:25Z |
| artifact `opal-assets/cot-rebalancer-runner.zip` | version `uNNJvohJ8HVjIlEcIjEmpouzIRxLROD8`, 2026-10-07T10:34:55Z |

The artifact bucket has versioning Enabled. To roll back: rebuild at `8af853ce59`, or restore that object version; then
re-apply the same target and read back the CodeSha256. The `-result.json` keys a rolled-back runner leaves behind are inert:
there is no trigger and no reader.

## Acceptance

1. The live `CodeSha256` equals the build's sha256, read from the build input and not by filename.
2. `LastUpdateStatus` reads `Successful`.
3. The first scheduled fire after the deploy (2026-10-09 06:00Z) reads branch A:
   - `meta/2026-10-09-result.json` reads `verdict COMPLETE`;
   - the stamp is present;
   - silver fires;
   - at 07:00Z the satellites producer writes `as_of 2026-10-09`.
