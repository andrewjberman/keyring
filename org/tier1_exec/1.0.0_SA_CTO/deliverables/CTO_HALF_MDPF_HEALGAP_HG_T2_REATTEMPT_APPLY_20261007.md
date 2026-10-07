# CTO never-widen half -- MDPF_HEALGAP HG-t-2, a second target on `cot-bronze-complete` re-running `cot-rebalancer-runner` the same day

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~14:1xZ. **Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_HG_T2_REATTEMPT_APPLY_20261007.md`
@cc9f7d81d1 (COO half SIGNED by `2.0.0_SA_COO~G1`). Order `MDPF_HEALGAP.TO-HG-d2` (laptop `0.7.0_AE_CloudOps~F`).
**Andrew's words:** ACT 1 and R20, "1.) Yes, rec approved. 2.) Yes this is fine." (@e5fb41862f). R20 entry `MDPF-HEALGAP-R20-01`
@dee4061bf9, authority @2611d05917; register row X16 asked of `4.0.0_SA_CRO~DELL1`.

## VERDICT: SIGNED -- the targeted apply of the two resources in `cot_rebalancer_reattempt.tf`, under the conditions below.

## Read by this seat

- The act is a destination on an existing rule plus its invoke permission. There is no new schedule, function, output path or role
  grant (C-ONE-PIPELINE), and the existing target `CotSilverOnBronzeComplete` is untouched.
- **The whole act rests on branch A: a normal day's ~11:32Z re-run must skip.** The guard lists the stamp (`lambda_function.py:218`,
  `list_objects_v2`). `comp-iam service cot-rebalancer-runner` (TF reconciled against live) reads `s3:ListBucket` **GRANTED** on
  `arn:aws:s3:::opal-data-assets` for that call. But the skip has **never run live**: today nothing invokes the runner twice. If the
  guard failed, every normal day would make a second Black Diamond call. ACT 1 does not cover that; its REC was "at most one extra
  call a day", and only when the morning failed.
- Branch B is the outcome the PRD's FWD-1 wants, under ACT 1. Branch C is identical to today. Rollback is a destroy of the two
  resources, read back by `list-targets-by-rule`.

## Conditions

1. **Prove branch A before wiring it daily.** Before the apply, the deploying seat invokes `cot-rebalancer-runner` once with
   `{"mode":"pull"}` for today's UTC date, whose stamp exists, and reads `SKIP-IDEMPOTENT` in the response and the log, with no new
   key under `blackdiamond/cottonwood/bronze/rebalancer_*/<today>/`. That invocation is a same-day re-run of this runner, inside
   ACT 1's scope. If it pulls instead of skipping, the apply does not happen and the guard goes back to `2.0.0_SA_COO~G1` as a row.
   The probe's `on_success` silver re-conversion of the same date is the branch-A behaviour, accepted.
2. HG-t-2 is drained to CLOUD, and the gate entry `MDPF-HEALGAP-R20-01` is at HEAD (it is, @dee4061bf9) before the commit that
   carries the file.
3. The `-target` plan reads 2 to add, 0 to change, 0 to destroy: exactly the event target and the permission. Any other line stops
   the apply. The plan's lines are printed in the ledger entry. CHECKPOINT_DISABLE=1 is set on every terraform call (laptop 106231).
4. After the apply: `WIRED-OK` and `UNCHANGED-OK`; the next normal day's ~11:32Z fire is read as `SKIP-IDEMPOTENT` with no new bronze
   key (AC3). A fire that pulls on a day whose 06:00Z pull completed means rollback the same day.
5. Not covered: the FWD-1 exercise (the induced morning failure), which is its own act with its own pair, and any refill of past dates
   (FWD-3; Andrew's ACT 2 answer was no).
