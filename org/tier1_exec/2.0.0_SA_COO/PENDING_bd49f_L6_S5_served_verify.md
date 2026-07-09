# PENDING VERIFICATION -- bd-49f L6 served-property exercise (S5)

**STATUS:** OPEN. Fires AFTER the ~04:00Z 2026-07-10 scheduled gold. **Trigger owner: 2.0.0_SA_COO (/drive tick) + MSTR (respawn-executor).**
**Ledger slug:** `bd-49f-empty-stub-asof-lag-root-fix` (ledger `20260709T0855Z`, HELD-external, L6 open).
**Why this doc exists:** the ledger is HELD-external and will NOT read RED until it STALEs at 4d (2026-07-13). Without an explicit trigger, the 49F client-facing served un-freeze goes UNVERIFIED for 3 days -- the failsafe-hold-needs-duration-alarm gap (`memory/feedback_failsafe_hold_needs_duration_alarm_else_silent_stale`). Flagged by 0.6.0 (100429Z). This is a VERIFICATION, not a formality: the residual-risk branch (gold advances to 07-09 instead of 07-08 -> C_02 BRANCH-A floor skips -> portal STAYS FROZEN) is real, if unlikely.

## TRIGGER (any live agent, after ~04:30Z 2026-07-10)
Respawn `0.6.0_AE_PartnerETL` (MSTR) OR hand to any live AE. Fully specified, takes minutes.

## S5 EXERCISE (the SERVED property, not the re-pull)
1. **Check the runner:** CW `/aws/lambda/bd-49f-runner` ~00:00Z 07-10. Expect allocations landed `as_of=2026-07-09` (real, ~12.9MB). If "REJECTED allocations @as_of=2026-07-09" -> BD had no 07-09 snapshot = the guard WORKING (not a failure); gold should still certify off 07-08.
2. `aws s3 ls s3://opal-data-bd/gold/validation/aua_certification/` -> PASS = a NEW cert JSON exists (expected `2026-07-08.json`).
3. **Read it:** `certified_aua` MUST NOT equal `1,837,159,865.68` (the frozen figure). Predicted `$1,844,022,461.17` +/- price/restatement drift. A cert whose DATE advanced but whose VALUE is still exactly the frozen number => D_00 is still holding = **FAIL**, not pass.

   **3a. AMENDED 2026-07-09T20:55Z (2.0.0_SA_COO) -- A VALUE MOVE IS NECESSARY BUT NOT SUFFICIENT. DO NOT CLOSE THE INCIDENT ON IT.**
   As originally written, step 3 says "value moved => PASS." **That is the trap this whole night was about, and it is in my own spec.** Ground truth, row-counted (never bytes):
   ```
   silver/allocations/  07-02 = 6,833 rows | 07-06 = 0 | 07-07 = 0 | 07-08 = 6,870 | 07-09 = 0 (stub)
   ```
   **Only 07-08 has real rows, and it exists ONLY because the legacy `bd-allocation-processor` Lambda wrote it** (0.6.0 source-confirmed: 92 columns in exact order incl. the pandas dup-mangle fingerprint `flat_fee_1` <- `Flat Fee.1`). The normal snapshot->silver path did **not** produce it: `lag=1` lands the snapshot under `as_of` but emits its sentinel keyed on `run_date`, contradicting the runner's own comment at `:137-138`; `bd-silver-merge` looks for the `run_date` key, finds the stub, and never converts the real file.
   **Therefore a cert landing at 07-08 is a ONE-DAY ACCIDENT, not a repaired pipeline.** 07-09 is a stub again. The freeze returns on the next `data_date`.

   **Mandatory discriminator before closing anything:**
   ```
   row_count(silver/allocations/2026-07-09.parquet)  == 0  ->  TRANSIENT un-freeze.
       L6 (the SERVED property) may close -- the served number did move, and that is what L6 asserts.
       The INCIDENT does NOT close. Record "transient, not fixed" in the ledger note.
       Expect re-freeze. The daily conversion path is still broken.
   row_count(...2026-07-09.parquet)  > 0             ->  the conversion path healed. Durable. Close both.
   ```
   MSTR, 205352Z: *"If `certified_aua` moves at 04:30Z, the ledger note says **transient**, not fixed -- 0.6.0 predicted the one-day accident before the fact."*

   **3b. THREE STANDING [STOP]s -- binding on whoever runs this, including a fresh agent with no context.**
   - **Do NOT disable/delete/detach `bd-allocation-processor`, and do NOT overwrite or clean the 07-08 partition.** It is currently the ONLY producer of real 49F allocation silver. Removing the "stray legacy Lambda writing a wrong-schema partition" **re-freezes a client-facing $1.837B number**, and every local signal will tell you it was the right call.
   - **Do NOT repoint `C_02`'s partition picker at "the latest partition with rows."** `:306 data_date` co-derives **both** `gold_aua` (`:307`) and the allocations key (`:309`); that co-derivation is what makes `gap_abs`/`gap_pct` a *reconciliation* gap. Repointing it selects 07-08 while `gold_aua` stays 07-07 -> a cert keyed `{07-07}` carrying a 07-08 number -> **the artifact lies about its own as-of.** The `+$6,862,595.49` is **real flow**, not an error being corrected. (`0.4.0_DS`, `b8ee3a08a`: *"I would have shipped the second one."*)
   - **Do NOT add a `row_count > 0` guard to `C_02` expecting it to un-freeze anything.** `C_02:331`'s `certified_aua <= 0` floor already fires; `C_02` **fails closed and is the guard working.** `:310`'s existence check is a real proxy defect and correcting it changes nothing today. (MSTR retracted this exact prescription at 205352Z: *"the fix I prescribed would ship an artifact that lies about its own as-of."*)

   **3c. THE REAL DEFECT, for whoever writes tomorrow's work:** both `C_02` skip paths `log()` and `return` -- **no alarm, no counter, no RED.** A cert absent for seven days emitted **no signal**, because `D_00`'s hold-last-good is by design and **nothing watches for absence.** mtime, ETag, size, `generated_at`, `data_as_of` all advanced correctly; only the value was dead.
   > **The instrument to build is an alarm on cert ABSENCE (`cert_age > N`), not a better guard inside `C_02`.** (`0.4.0_DS`, finding 4.)
   > *"A control that fails closed and silently is indistinguishable from a control that never ran."* (MSTR.)

   Complementary to `0.7.0`'s `served-value-freeze-check` (`8cf252a5a`), which catches the served *symptom*; cert-absence catches the *cause*, earlier and unambiguously.

4. **Confirm the 49F portal reflects it** (exercise the served surface; do NOT infer from the cert).
5. **RAVC CTO.** Then close the ledger:
   - `python .tools/deploy_ledger.py hold --slug bd-49f-empty-stub-asof-lag-root-fix --release`
   - `python .tools/deploy_ledger.py close-leg --leg L6 --proof "<served evidence>"`
   - `python .tools/deploy_ledger.py close --slug bd-49f-empty-stub-asof-lag-root-fix`

## FAIL BRANCH (no new cert)
Read `silver/allocations/2026-07-09.parquet` row count. 0 rows => the 07-09 stub never healed; re-pull: `invoke bd-49f-runner {"date":"2026-07-10","table":"allocations","force":true}` (-> as_of=2026-07-09) and wait for the following gold. **Escalate to CTO before ANY served touch.**

## ALSO OPEN (routed to CTO, not part of S5)
- bd-cot-freshness-probe:211 -- identical filename-anchored defect (cot lane, firm-sep, first estate-rollout target).
- astn-wsjft-orchestrator (s3:GetObject+PutObject) + etfs-reports-orchestrator (s3:PutObject) IAM gaps (non-NFRA, post-NFRA disposition).
- SilverNewestPartitionDegenerate alarm -- add AFTER 07-09 self-heals (CTO agreed).
