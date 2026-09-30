# MDPF_SECCLASS rounds 4 and 5 (chain A) -- the CTO's L10 analysis

**Author:** 1.0.0_SA_CTO, 2026-09-30 ~19:1xZ. **Input:** `3.0.0_SA_CVO`'s slug 103380,
`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R4_R5_REVIEW_20260930.md` @0ae356c411 (ADJUDICATION_v3 C-S8..C-S10,
REMEDIATION_v3 S4; S3 and W5-S3 closed in REMEDIATION_v2; watermark 14:39Z). Also read: `2.0.0_SA_COO~M`'s rollback escalation 103368
(row S5, BLOCKING) and this seat's rulings on it and on round 5's placement (103327, the reply to 103368). The previous analysis:
`ROUND2_3_ANALYSIS_MDPF_SECCLASS_20260930.md` @0a8deabc8e.

## 1. What rounds 4 and 5 proved (the CVO's live reads)

- **FWD-3's first correction served:** VNQI reads alternatives / International Real Estate, `classified_by` seed (13:48:39Z).
- **The CUSIP act served as signed:** 348 `CUSIP:`-keyed rows of 2,657; the 349th refused by design (one CUSIP held by two firms).
  The guard holds against real rows: 0 `CUSIP:` keys in `bd-securities` (10,929 scanned; control 293). My condition 3 is met.
- **S3 closed** on its own disarm test (319 passed at HEAD, IB-mr-291 drained); **W5-S3 closed** (0 behind origin).
- **Not yet served:** MODEL_ROWS (`classified_by = model` 0 live), consistent with its unsigned half; BD_THREAD_R2 rolled back at
  18:16Z (below). Q3 is right: S3's closure grades the suite, and the one-window release is graded at its own ledger close.

## 2. Rulings

1. **Q1, a parked order pinned every later slug: fixed in the gate, not by re-homing the order.** The row gate now reads `parked` as
   not-open (@867189a633): a parked order sits outside the round by ruling and re-enters on a status flip, so the census never loses it.
   Self-test 187 of 187; live control: MDPF_SECCLASS reads 0 open of 18 with the change and TO-SC-e12 open without it. Round 6's
   watermark can advance past 14:39Z. Re-homing was rejected because moving a live order out of `task-orders/` breaks every path that
   cites it.
2. **Q2, who reads the model flag: Andrew's word governs, and the half must prove the readers tolerate it.** His word (round 4's
   source, recorded @6a861c4e18): "We don't need a human review for that, what would be better is a flag if Kimi has lower confidence."
   So flagged rows are WRITTEN and SERVED, not held back; that trade is his, and C-CLASSES's "nothing is guessed" is read beside it.
   The MODEL_ROWS half, before this seat signs, carries a census of every reader of `etf-classifications` (the Holdings producer, the BD
   library, the portal's asset-class mapping, IRPT_DASHBD's C-CLASSES consumer) and each reader's behaviour on `classified_by = model`
   and on the `low_confidence` attribute: no reader may crash, refuse the row, or fail a strict contract on the new enum value (the
   Holdings contract's `additionalProperties:false`, W93-S1, is the named risk). A display distinction for a low-confidence class is a
   design enrichment for DSGN_IRPTV1, not a precondition.
3. **S5, BD_THREAD_R2 rolled back (ruled 18:3xZ, recorded here):** the rollback is the signed half's own branch; the fix-forward is
   round 6 cell 1 under a new half; E_18 stays deployed and its 2026-10-01 04:00Z import crash is the recorded negative control; the
   E18 half's acceptance moves to the first scheduled run after the fix-forward.
4. **S4 (latent: an update on a missing key would mint a skeleton row):** round-6 hygiene as the CVO graduated it: each
   ConditionExpression in `label-legacy-classified-by.py:89` and `set-instrument-kind.py:96` gains `attribute_exists(ticker)`.
5. **W8-S2, un-pathed worker searches:** closed in the worker definition @40a3c9d7dd (every Grep, Glob and Read names the worktree).
6. **W6-S2 stays ARMED** with its remedy TO-SC-e12 parked on 0.7.0_AE_CloudOps (103327); unchanged.

## 3. Outcome read

FWD-3 is served for its first correction (VNQI) and its write path is proven; not REALIZED until the scheduled classifier's first real
fire is read (FWD-7). FWD-4 moves on the CUSIP rows (348 served) and on MODEL_ROWS once signed. The BD thread (FWD-1's BD page) is
back to its pre-window bytes; it re-attempts after cell 1.

## 4. Enrichment for round 6 (~M; one issuance)

1. **The fix-forward (cell 1):** ship the shared classifier client inside the gold code bundle (the IRPT closure's pattern), covering
   C_06, D_03, D_04 and E_18; a criterion imports it from the DEPLOYED flat layout on the runner (the issuer rule, 103370); a new half
   for the redeploy and the re-run of the one window's BD legs.
2. **The two CUSIP reader guards** (my CUSIP half's condition 5): the `find_by_*` filter in the client and its two copies; the seed
   scripts' PRE-READ count excluding `CUSIP:` rows.
3. **S4 hygiene** (ruling 4).
4. **MODEL_ROWS**, the reader census first (ruling 2), then the half.
5. **FWD-7:** the scheduled classifier's first real fire, read from its log.
6. Carried: W5-S2 enum consolidation at the drain; TO-SC-e12 parked.

-- 1.0.0_SA_CTO
