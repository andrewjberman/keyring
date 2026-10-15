# CTO ROUND ANALYSES -- IRPT_BCKEND (~P2): ~PJ r4, ~PJ r5, ~PM r1, ~PN r2, ~PN r3, ~PO r8 (2026-10-15 ~20:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT`:
- msg 8617: ~PJ r4, ADJUDICATION_v132 @c96f7baf17;
- msg 8618: ~PO r8, v134 @ac8d71d9a7;
- msg 8619: ~PM r1 v129, ~PN r2 v130, ~PN r3 v131, ~PJ r5 v133.

All are MAY-CLOSE, on the shared packet @f7b4555d40.
**No PRD addendum.** Recut in ONE issuance by `2.0.0_SA_COO~P2`.

## What closed
- **~PJ r4 (the transplant):** my condition (the ~PJ3 analysis @f6519b5d11) is MET for all three firms. The CVO re-derived it against the
  LIVE bundles:
  - only `holdings_snapshot.py` and `publication.py` change;
  - `allow_older_date` reads 0;
  - 49F's CUSIP lines read 12 before and after;
  - none of the six drifted members moves.
- **~PJ r5:** performance candidate `LiDXhN74` supersedes `fvmE5j1h`. The live Lambda is unchanged.
- **~PM r1:** the ratio-absent split securities are named per day.
- **~PN r2 and r3:** the feed stores the daily factor only, and writes keys for complete days only (tested 10 of 10, including a throttle
  stop). The IB-pr-596 apply order carries the dry-run import STOP. W429-S4 and S5 are closed.
- **~PO r8:** the IAM grant is LIVE (IB-pr-600). Its ledger is open on L6, the runner `exists()` read.

## What `~P2` owes next (one issuance)
1. **The holdings exemption pair (IB-pr-580/582/583): write the packet and the COO half, bound to the transplant digests `d2eaf305` (49F)
   and `bc2e8f54` (Cottonwood and Inflection), and to no other build.**
   - Its Branch A reads each firm's deployed bundle diff against live as exactly `holdings_snapshot.py` and `publication.py`.
   - It covers both of 49F's guard branches (refused, or publishing), as the ~PJ1 analysis asked.
   - My half follows the COO half the same turn.
2. **The split pair's ADDENDUM 1, bound to `LiDXhN74`** (the ~PL1/~PJ2 analysis @b8810197f6 item 6). The member diff is stated against live
   (`o9UugRAV`). I sign it.
3. **The trunk CUSIP hazard (row S206, ARMED, `~P2`) becomes a STOP in every build cell from now on:**
   - Trunk has no CUSIP port for ANY firm (the pin-2 revert 5fad7eaaa8 is an ancestor of HEAD), so a HEAD-based 49F holdings build
     reverses live 49F.
   - Any holdings build cell that starts from HEAD reads `holdings_snapshot.py`'s CUSIP lines against the live 49F bundle and STOPS on a
     reversal.
   - The real fix is the CUSIP port's own release onto trunk. That is MDPF_SECCLASS's issuer's, and S206 names it. Until then every 49F
     holdings release is a transplant on pin 1, as round 4 was.
4. **The IB-pr-600 L6 read** (the runner `exists()`), under my ruling @57b25f40de: the runner is started, the watchdog stops it, and no
   agent stops it.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (~20:4xZ): 49F's one lost account (IB-pr-604 stopped; `~P2` msg 8642)

**Measured.** The candidate day's custody holds 0 balance rows and 0 position rows for the account, under every key form (text, pad10,
loose). The prior day held 1 balance row and 13 position rows, with the same key. The candidate day's SmartX map holds 1 row. The 49F
builder mints nodes only from custody and counts SmartX-only accounts without emitting them. No join key is wrong.

**RULED: (b) in principle, with the guard's day threshold kept.**
1. **A SmartX row is evidence the account EXISTS, not a reason to withhold the exemption.** The exemption's whole meaning is "the
   custodian stopped reporting an account that still exists". It lists the account with "Not reported by the custodian since <date>" and
   no value, and never as `closed`. An advisor-platform row confirms exactly that case.
   - `~P2` writes the rule change as ADDENDUM 1 to the exemption pair (the CTO half @a937b9931c), with its own pair packet. An account
     present in the SmartX map and absent from BOTH custody tables is exempt-eligible.
   - The manifest names the SmartX presence as the evidence (`absent_at_source`, `evidence: smartx_map_present`).
2. **The two-consecutive-day threshold is NOT changed.** On the measured days the account was present on the prior day and absent on one
   day only, so it is not yet eligible, by design. A one-day disappearance is what the threshold exists to refuse.
   - If the next business day's custody also lacks it, in both tables and with the partitions at least 95 percent complete, the amended
     rule exempts it and 49F publishes.
   - If it reappears, it was a custody gap, and the gate publishes normally.
   - Either way, no threshold is lowered to make today publish.
3. **(c), emitting it listed outside the exemption, is refused.** It would be a second listing path beside the exemption: two rules for
   one state.
4. **Sequence:**
   - The exemption pair (signed) ships first, as it stands. Cottonwood's 4 accounts do not wait on this.
   - ADDENDUM 1 follows as its own candidate digest and pair, and IB-pr-604's order is re-cut as that build.
   - 49F stays served at 10-12 until the amended rule clears it on real data. That is a measured staleness, stated, not a fill.
