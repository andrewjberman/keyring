# CTO never-widen half -- MDPF_HEALGAP FWD-1 exercise (TO-HG-d3): one morning's Cottonwood Rebalancer pull induced to fail, healed by the ~11:32Z re-run

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~14:3xZ. **Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_FWD1_EXERCISE_20261008.md`
@8118554234 (COO half SIGNED). **Andrew's word:** ACT 1 @e5fb41862f, which names the exercise. **PRD:** FWD-1's DONE WHEN, "one morning
pull deliberately made to fail ... the next naturally failed morning is the negative arm, never the test".

## VERDICT: SIGNED, under the conditions below.

## Read by this seat

- This is the PRD's own bar for FWD-1, and ACT 1 covers the one Black Diamond pull of the re-run. The induce branch sits after the
  guard and before any secret read (verified in the HG-t-1 diff @ca914096d7), so the 06:00Z fire and its two retries write nothing and
  call nothing.
- **It is a deliberate served delay, named plainly.** That date's Cottonwood model-portfolio data lands ~5.5 hours late (branch A),
  or is absent until a manual remedy (branch B). Whether it makes the 13:30Z floor is not predicted. If it does not, that date's
  served MDPF point is late by a day. The shipped gold catch-up (`mdpf_gold_catchup.py`, in the daily consolidator) is the existing
  path that values it at the next run. That consequence is accepted for one date as the cost of the outcome's only real test.
- The input change is out of band of Terraform for at most ~25 minutes, on a target Terraform manages. No CLAUDE.md NEVER names
  `events put-targets`; the drift is bounded and read back (condition 3).

## Conditions

1. **GO only after TO-HG-d2 is complete with its pre-apply SKIP probe passed** (CTO half @a79f7ea1b7, condition 1) and `WIRED-OK`.
   An exercise on an unproven guard is not this act.
2. A ledger entry opens before step 1 and records each `put-targets` with its time and read-back. Step 3's restore is read
   `RESTORED-OK` before 06:20Z, and in no case later than 05:59Z on 2026-10-09.
3. After the restore, a targeted `terraform plan` on the daily rule's target in `opal-assets` reads no change (`CHECKPOINT_DISABLE=1`).
   A diff means the restore did not match the declared input; it is fixed the same morning.
4. **The served read is part of the grade:** the issuer reads the Cottonwood served figures for the date at end of day, and also
   records whether the 13:30Z floor was met (yes/no with the times read). A miss is a FWD-1 note and a row, not a failure of the
   outcome as worded ("by the end of the same day").
5. Branch B's remedy (one manual `{"mode":"pull"}` invoke for the date) stays inside ACT 1. It is done the same day and recorded.
   FWD-1 then grades NOT REALIZED for the date.
6. One date only. A second exercise is its own act with its own pair.
