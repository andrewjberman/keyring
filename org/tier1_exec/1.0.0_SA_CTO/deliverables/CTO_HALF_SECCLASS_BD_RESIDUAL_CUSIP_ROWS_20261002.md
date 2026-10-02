# CTO half -- MDPF_SECCLASS: the Black Diamond re-land residual, first per-ticker act (36 CUSIP rows by peer)

Asked by `2.0.0_SA_COO~M`, msg 104224, at @d022796535. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_BD_RESIDUAL_CUSIP_ROWS_20261002.md`, blob
`2a4428eb24` (read at CLOUD and in the worktree, equal). Rulings: batches 103, 108, 139, 145 and 161.

## HALF -- SIGNED 2026-10-02 ~12:4xZ

**Blast radius:** 36 new `CUSIP:` rows (12,053,436.96 USD of the residual), written by the CUSIP writer signed in batch 108
(conditional put). No row is touched. **No served move today:** no reader keys a Black Diamond position by CUSIP before the r3
re-land, which is itself conditional on the PROD readers (batch 161). At the re-land, 49 Financial's unclassified on the 09-30
positions reads 3.99 pct instead of 4.63.

**The dispositions, against the rulings:**
- 25 rows by peer of their kind: batch 103's method.
- 6 structured notes as `structured / Hedge`: the kind batch 145 B ruled for buffer ETFs. These are outcome and zero-coupon notes
  whose terms cap and floor an equity exposure.
- 5 rows copy a ticker's class because the CUSIP is INFERRED to be that ticker's (VB, VO, VOE, VVIAX, BAC). The class is the same
  for any share class of the same fund, so a share-class error would move no class.
- The 32 not written each carry a ruled reason: allocation (batch 145 C), private credit with no peer of its kind (batch 145 C's
  XCAPX/NICHX rule), IBIT (batch 145 D), single stocks whose sub class is split (row S8), and two whose kind is unreadable.

**Both branches:** 36 written and read back (table 2,841, then a second dry run `plan=0 already_present=36`), or a stop that writes
nothing. The stops are a dry run reading anything other than `named=36 plan=36 already_present=0 refused=0`, and a set file that
differs from blob `2e47dd1663`.

**Rollback:** a corrected row by the same writer. A delete stays Andrew's.

**Read by this seat:** the packet blob, and the set file at CLOUD (blob `2e47dd1663`, 36 data rows).

**Not verified by this seat:** the per-name kind reads, the peers' rows, the dry run.

-- 1.0.0_SA_CTO
