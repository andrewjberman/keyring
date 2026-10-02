# 2.0.0_SA_COO~X -- /canonical-drive AMGT_CORPUS 30m -- 2026-10-02 14Z to 17Z (rounds 32 and 33)

**archetype:** MIXED

## Round 32: released, built, served and closed

- **14:48Z released.** The CTO lifted the AMGT Friday freeze (RESAPP addendum `0ce76710dc`). One ask went to CTO~Z, and RULED msg
  28540 answered it:
  - round 32 = Z-S74 (LOCAL) plus the BEST_DIV_YLD label (SERVED);
  - Z-W4-S6's Peers lookup goes to RESAPP.
- **Issued:** `cc061e1d95`.
- **ah-1 (Z-S74), `75ea254ddc`:** 11 units and 11 signs over 100 served blocks now read UNRESOLVED.
- **ah-2 (BEST_DIV_YLD identity), `b2aee0c0f2`.**
- **ah-3, the paired served act:**
  - pair COO `c216d1a52f` / CTO `b859ebff4c`;
  - ledger `amgt-corpus-r32-ah3` CLOSED, 5 legs, last commit `8a7f8a78fa`;
  - census: BEST_DIV_YLD DECIMAL 12 -> 0, 4 blocks moved, 0 values;
  - GOOGL's 3 EQY_DVD_YLD_IND moves were accepted by name (row Z-S82).
- **Analysis:** the CVO's v38 adjudication fed the CTO's round-32 analysis `ac45eeeef8` (16:4xZ), which CLOSED round 32 and named
  Z-S81 as round 33.

## Round 33: issued 16:5xZ (`62504f5f9c`)

- **Measured at the cut:** 60 of Z-S81's 77 figures needed only the round-26 series rule. Their map entries were single samples
  from before it.
- **ai-1, `f64efce667`.** EQY_DVD_YLD_IND is now decided by its fiscal rows' dividend / price band. Every other percent field
  under 0.3 with no ground reads UNRESOLVED.
  - AMENDMENT 1: the band (0.5, 2.0), measured on PWR, BA and GOOGL rows.
  - 4 test assertions that pinned the ruled-away DECIMAL guess were updated; 93 tests pass.
- **ai-2 dry run over 100 keys:** 11 blocks move, unit 77 / sign 8, 0 values. The COO half is `e748581d10`.
- **The CTO half is owed.** The ask (msg 28589) reads OFFER-EXHAUSTED on the broker, while its file is in `1.0.0_SA_CTO/~Z/read/`.
  It gets a nudge at the next tick if no half lands.

## Notes

- **Peer staging in the shared index.** Several commits met another seat's staged files (a never-rules-gate.sh fix, a CTO log),
  a peer's open merge, or `index.lock`. Each was handled by waiting, or by safe-commit's pathspec-limited `--force`
  (audit-logged). A peer's staged work was never unstaged or committed.
- **The inbox watcher was stopped from the operator's side at ~16:2xZ.** It was not re-armed; mail now arrives on the heartbeat
  piggyback.
- **Push state:** the round-32 and round-33 commits are LOCAL. The CLOUD push is MSTR~Z's, on Andrew's word (open call 1 of this
  lane).
