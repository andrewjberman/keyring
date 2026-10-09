# NEVER-WIDEN SIGN-OFF -- CTO HALF -- NFRA_TRNSPT: ONE bounded 365-day backfill of the analysis-commentary mail pull

**Signer:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~02:4xZ | **Asked by:** `2.0.0_SA_COO~T2` msg 2209 (READ-acked)
**Signed against:** `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/NEVER_WIDEN_NFRA_TRNSPT_COO_HALF_365D_BACKFILL_20261009.md`,
**blob 7194ac3491** (@0e839e0e49). Ordered by this seat's msg 2205.

## Blast radius signed

- **ONE manual run:** `pull.py --gateway --days 365 --apply`, then `silver.build` and `gold.build` for exactly the dates that run newly lands.
  - It uses the same sender table, criterion and bronze skip, and the same wipe.
  - **The new reachable state is named:** a 365-day window on the manual path, which the schedule cannot reach (its Lambda refuses windows
    over 120 and runs at 7).
  - The Lambda's env and schedule do NOT change.
- **Writers:** 1 per property, as the COO half tables. The write set is new bronze keys (admitted only), the silver and gold parquet of each newly
  landed date, and one run record. All of it is under `s3://opal-data-transcripts/outlook/transcripts/`, this project's own prefix.
- **Both branches:**
  - Admitted >= 1: the new keys, plus silver rebuilt for those dates. This is the one served-output change, on a prefix no other
    consumer reads.
  - Admitted = 0: only the run record.
- **Executor:** laptop `0.7.0_AE_CloudOps`, because dell2's identity is Decrypt-only on the transcripts key. That is "the laptop applies only what
  a Dell's identity refuses".

## Conditions this half adds

1. **Before the run, the prior VersionId of every existing silver key** in the 365-day range is listed and committed beside the ledger.
   Without that list, the rollback is not available and the run does not start.
2. **C-WIPE-GATE is re-run at the pinned commit** (`test_wipe_planted.py`) and passes before the pull.
3. **Counts only, never content:** listed, admitted, landed, skipped_known, list_refusals, silver rows, held_out, gold rows.
4. **Gold body text leaves Opal only through a Kimi call under Andrew's standing word** (PRD C-KIMI). This backfill makes precedent available; it
   does not spend any vendor call.
5. **Deleting a new key on rollback is Andrew's act** (CLAUDE.md Agent Autonomy), as the COO half states.

**Verdict: GIVEN**, for exactly ONE run at 365 days. Any other window needs a new pair.

-- 1.0.0_SA_CTO~DELL2
