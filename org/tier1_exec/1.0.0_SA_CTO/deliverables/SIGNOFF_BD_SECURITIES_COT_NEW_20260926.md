# SIGN-OFF (1.0.0_SA_CTO half) -- bd-securities COT-new write (Part 1 now; Part 2 on its conditions)

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_COT_NEW_WRITE_20260926.md`
@`e4a6b03473` (2.0.0_SA_COO~M msg 101107). **Rules:**
- Andrew ~02:3xZ @`c3dde578b9`: established equities stay equities, and `other` is personal or held-away only.
- CALL 2 @`37025a10e9`: one run, the write under a half.

**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~03:1xZ, under the self-drive arm @`ce6aa15a17`.

## Part 1 (941 keys) -- SIGNED, with ONE added precondition

**The act:**
- A conditional PutItem per key, `attribute_not_exists(ticker)`, carrying `classified_run = irpt-m-cot-new-20260926`.
- The literal list, sha c96398886f143f54...
- The census re-runs first, and the act refuses on a sha mismatch.

**What moves, read from the producer's rule:**
- COT C_06: $12.11M equity -> fixed_income and $0.88M equity -> alternatives, 90 relationships.
- BD C_06: $6.85M equity -> fixed_income and $0.46M equity -> alternatives, 652 accounts.

All of these are corrections by name.

**Excluded, per Andrew's rules and ~M's REC:**
- R2b: 35 securities the model called `other`.
- R1: 7 established equities.
- R3: 10 name-assigned non-equities.

**Added precondition: measure a07.**
- a07 `dim_asset_classification` (the 49F/INF/COT union dim, on an ENABLED schedule) is a reader whose move the
  request marks NOT MEASURED. A never-widen half cannot sign an unmeasured served reader.
- Before the first PutItem, run a07's classify over its current inputs with the new items added to the loader, as a
  dry build with no upload. State the per-firm delta (49F, INF, COT), with count and dollars, in the ledger.
- If any 49F or INF value moves that is not one of these same keys moving by the same rule, stop and send it back.

**Rollback:** per key, a conditional DeleteItem on `classified_run`, with a human confirmation.

## Part 2 (26 `other` keys) -- SIGNED, on both conditions

It lands only after:
1. the act-1 read-back (Monday's first COT run shows `other` in the mix at 0);
2. ~D's IR `other` mapping is on origin DEV. The render condition is MET (PROD 36a37afc).

Part 2 carries the same a07 measurement. Read-back: z09305589 shows its Other slice at $19,653,063.27 on the portal,
read by ~D.

## Withdrawn

Batch B act 2 (@`4fdc4284c9`) is withdrawn and superseded by Part 2. The fixed COT B_01b deploys only as its own act,
after Part 1, with its prompt amended to rule 2 and a dry run.
