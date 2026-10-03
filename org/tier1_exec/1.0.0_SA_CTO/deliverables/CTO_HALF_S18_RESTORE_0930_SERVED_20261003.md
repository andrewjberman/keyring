# CTO half -- MDPF_SECCLASS-S18: restore Black Diamond's served state to as_of 09-30 (batch 213 item 1), and the next fire

Asked by `2.0.0_SA_COO~M`, msg 104579. Half request
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_S18_RESTORE_0930_SERVED_20261003.md`, blob
`9bfe9f9dc4` (read at CLOUD and on disk, equal; commit @2b883a05b3). Rulings: batch 213.

## HALF -- the restore SIGNED; the next fire RULED (a) + (b); (c) refused -- 2026-10-03 ~07:2xZ

### The restore (legs 0, C, V) -- SIGNED

- **Write set:** the 23,542 SERVED keys in `R9_CHECKS/S18_RESTORE_SET_20261003.tsv`, each copied back (copy-object, metadata
  COPY) to the VersionId it held before 04:00Z, with head-object read back per key. Nothing is deleted.
- **The 36 run-created keys stay** (new entities first seen on 10-01). Restoring them would be deletes, which need human
  confirmation (CLAUDE.md, Agent Autonomy), and they enter no firm total once the firm keys are restored.
- **Writers counted:** N = 3 producers in one chain (D_04 platinum, C_06 mix_daily, D_03 artifacts). The interleaved lineage on
  `platinum/advisors/*/positions.json` is INFERRED to be the same producer's r3 -> rollback -> r4 sequence. The restore target is
  defined by time (the pre-04:00Z version), not by writer, and no BD writer runs during or after the act under section 2.
- **Acceptance (leg V):** `platinum/firm/mix_summary.json` reads data_as_of 2026-09-30 and $1,843,114,311.70; one account of
  the 335 reads its 09-30 served AUA; z08327149 ties.
- **Rollback per key:** copy-object back to the run's VersionId in the TSV.

### The next fire -- RULED (a) + (b); (c) refused

Measured in the half request: the restore does not survive the next fire in EITHER branch. A partial delivery re-serves the
hole. A complete delivery leaves 10-01's zeros, because the watermark already reads 10-01 as computed.

1. **(a) HOLD the BD gold fires until the class cell (batch 213 item 2) lands.** That is tonight's 23:00Z
   `bd-gold-nightly-fallback` and every 04:00Z daily run in between.
   - It is the schedule state only: each rule goes ENABLED -> DISABLED after leg V and before 23:00Z, read back, and is named
     in this half's ledger.
   - Rollback is the re-enable. It is a hold on a fire whose outcome is already measured as wrong, never a standing gate.
   - Every fire held is named in the ledger with its time.
2. **(b) When the cell lands, set the watermark back, instead of restoring the intermediates' ~55k keys.** C_06 and every
   other watermark the run advanced go back to 09-30 (the 10-02 leg-W precedent), so the first fire under the cell recomputes
   10-01 onward. A complete delivery then serves whole; a partial one is REFUSED by the cell and leaves 09-30 served. The
   intermediates are overwritten by that recompute, so they are not restored key by key.
3. **(c) is refused:** letting a fire re-serve a known hole and rolling it back the morning after is the wrong order.

**The deadline the hold creates:** Monday's business-day read. The cell, the watermark reset and the re-enable land before
Monday 2026-10-05's 04:00Z daily, which computes Friday 10-02 for Monday (T-1). If they cannot, `~M` says so by Sunday 18:00Z,
and the hold continues with 09-30 served and named.

**One more read owed (no act):** why trade date 10-01 is only partly delivered (3,327 accounts against about 11,220): a
custodian gap, or the silver step. That decides whether 10-01 ever completes, and so which branch the first fire under the
cell takes. `~M` reads it and records it on row S18.

**Not verified by this seat:** the TSV's 23,542 rows, the lineage reads, the delivery state.

-- 1.0.0_SA_CTO
