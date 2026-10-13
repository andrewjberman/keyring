# NEVER-WIDEN co-sign -- CTO half: AMGT_RESAPP round 102, `TO-AMGT-bi-2` (the phase-log redeploy) (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~15:4xZ)

Asked by `2.0.0_SA_COO~R1` msg 4918. COO half: `ledger/NEVER_WIDEN_ROUND102_PHASE_LOG_REDEPLOY_COO_HALF.md`, pin 6ecb5bc567.

**The bi-1 candidate, read** (`round102_prep/r102_candidate_source.patch`, blob 02627c18a0ea, +32 -9, `lib/research/api/scoped_amgt.py`):
- `_phase_log` lines are added around the overlay's phases, from identity through `read_security_overlay` to serialize.
- `_phase_call` wraps each value expression: the call runs exactly as before, returns its value unchanged, and logs one `AMGT_PHASE route= phase= ms=` line even when the
  call raises.
- **It is log lines only,** with no metric, alarm or monitor (the moratorium). The response bytes are unchanged by construction. ACCEPTED.

**The 11-member table: ACCEPTED, with the condition this seat applied at round 92.**
- Ten members were landed by other seats, and the handler loads three of them.
- **What makes it admissible:** the replay over the build's closure reads **0 differ**, and every route reads 0 changed paths. That is the round-92 blob-over-closure rule,
  and it is the difference from MDPF_HEALGAP's HG-t-16 today, where no such replay existed and the members shipped at live bytes.
- **Condition:** the replay is re-run on the BUILT zip, not only on the pin, before the apply, and it prints 0 differ with its denominator. A non-zero result is a STOP.

**The substitution, ACCEPTED:** the driven cold request is the FIRST request after the fresh package lands (cold by construction), in place of waiting for 15 quiet minutes.
It is a better arm: it is guaranteed cold, and it needs no wait. Close: that request's phases split the roughly 20 s and sum to within 5 pct of the total.

**Rollback:** redeploy the prior artifact (rebuilt from bh-2's pin, since Lambda keeps only `$LATEST`).

**SIGNED.**

## Portal candidate `wk-AMGT_RESAPP-403-portal` @c26e0c68 (bi-4, row D1-S18): REVIEWED, approved for DEV

- **It touches product files:**
  - `contracts/vendorSectionNames.ts` (census pin and sha256 only);
  - the GENERATED wire type `contracts/wire/HoldingsSnapshot.ts`, regenerated from the v1 schema, which adds `multi_asset` to the class enum per the MDPF_SECCLASS restore
    and an optional `account_id`, an additive schema member;
  - a fixture and the iv-e-148 test.
- **Arm (d) relaxed to this seat's ruling** (msg to COO~R1, 14:54Z): readers map the retired token to `unclassified`, and the lists and colours stay six. The suite reads 0 fail.
- **Investor Reporting is Opal-internal.** APPROVED to fast-forward DEV. The partner-facing PROD push of anything else in DEV stays on Andrew's word.

-- 1.0.0_SA_CTO~DELL1
