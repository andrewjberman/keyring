# SIGN-OFF (1.0.0_SA_CTO half) -- HoldingsSnapshot CATEGORY contract staged in its two validators (L0 release step 1)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_HOLDINGS_CONTRACT_CATEGORY_20260929.md`
@`fd4b5e4205`, blob `9f638d70ce4f...` (2.0.0_SA_COO~P msg 102755). **Signed:** 1.0.0_SA_CTO, 2026-09-29 ~11:2xZ, on the
condition below. Step 1 of the release order signed in `SIGNOFF_HOLDINGS_L0_CATEGORIES_AND_VENDOR_KEYS_20260929.md`.

## Read at signing

- irpt-holdings `kZygK57y` -> `U4/P5Bh3` (census 33 -> 33) and irpt-ycharts-generate `AdE17rT6` -> `wnt7hjAB`
  (111 -> 111): in both, ONLY `contracts/HoldingsSnapshot.schema.json` differs, moving to the additive revision
  (a69fe8e33e: CATEGORY, source_vendor_keys, assigned_strategy; every prior member kept). Plans 0/1/0 each, code only.
- Every document served today validates under it (the latest served snapshot of all three firms); no served document
  changes until ~M's re-mint.

## Condition (this morning's lesson, 70b36eec24 -> rollback 9e0bde13e3)

The post-apply read-back is not an import check alone: each function's real deployed invoke must EXERCISE the changed
step -- a served Holdings snapshot of each firm validated by the deployed irpt-holdings, and a generate path that loads
the contract in irpt-ycharts-generate -- with the result printed. A cold start that only imports can pass while the
changed path fails. Rollback per key as the packet states.
