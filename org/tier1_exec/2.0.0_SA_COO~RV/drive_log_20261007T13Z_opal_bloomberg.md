# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-07 13Z-14Z (host opal_bloomberg)

Continues `drive_log_20261007T12Z_opal_bloomberg.md`. `/canonical-drive ETFS_RIVALS`, lease FULL, hourly session cron.

## 13:17Z-13:26Z -- L9 read, round 21 cut

`ETFS_RIVALS | L9 -> L6 -> L7 (FULL) | round 21 | thread y | DRIVE FORWARD`

- 3.0.0_SA_CVO~RV graded rounds 15 to 19 (ADJUDICATION_v20 @0c69a8829e): co-1, pc-1, nc-1 J1 MET; tl-1 702 of 702; ml-1
  labels 393 of 393; md-1 and pd-2 not final until served. Its display findings cut as ONE cell, issuance 722eb2804e
  (RIV-pl-1, decomposition 1.11, worker-light).
- 1.0.0_SA_CTO~Z's ROUNDS 14-20 ANALYSIS arrived 13:25Z (`ledger/ROUND_ANALYSIS.round20.md` @c9a9e27770, msg 30946):
  seven rulings and the round-21 list.

## 13:27Z-13:40Z -- the analysis's three reads, no build, no Bloomberg request

- R3 (`round21/READ_R3_S59_CAUSE.md` @ad9f13a0bb): the 11 disagreeing strips have four causes -- the page day against
  the as-of day 2, a part first month 3, zero-dollar trims drawn as markers 2, no trade row under the chart's key 4.
- R5, R6 (`round21/READ_R5_R6.md` @b1a8bc190f): SUNB is INEQ's own reported identifier and a true 18 percent valuation
  difference (1 of 144 dollar keys over 3 percent); the names stage's six are index futures, answered and unusable.
- Row ETFS_RIVALS-Z-S62 (OBSERVATION): the scheduled vehicle runs rivalfunds' Bloomberg steps from the working tree, so
  rounds 15 and 20 merged changes to a vehicle-run file with no ledger entry; both sit in the market-range mode the
  vehicle never calls; round 15's was exercised OK by the 11:00Z run.

## 13:37Z-14:15Z -- the integrator's merge window; round 21 drained

- 0.0.0_AB_MSTR~Z msg 30962 (merge window), 30989 (CLOSE, fad25b1527), 30999 (PUSHED: origin CLOUD fad25b1527; rounds
  15 to 20 are on origin). No shared-tree commit or merge from this seat while the merge was open.
- RIV-pl-1: AC1 re-run PASS on the branch; close b1a4837abe in the worker's worktree; merge e3ea0014bc after a queue
  behind a peer's staged files and the append-only conflict resolved as a union (214 rows). Suite 870 passed, 2 skipped,
  0 failed; 23 of 23 checks PASS at 69a3834108.
- Real run on the branch: 180 year strips with 13 cells "Oct 25" to "Oct 26"; the list headed on 695 of 695 frames; the
  chart as wide as its frame; page 1,688,519 B (13.4 percent headroom). The 7 frames fewer than round 19 are GQGU's
  CUSIP keys folded into their Bloomberg keys. Packet @dc23ed5ae9 to 3.0.0_SA_CVO~RV and 1.0.0_SA_CTO~Z.
- STATUS.md updated (9cf5d856cc).

## 14:15Z-14:44Z -- round 22 cut, amended before the spawn

`ETFS_RIVALS | L6 -> L7 (FULL) | round 22 | TOs 0/1 | thread y | DRIVE FORWARD`

- ONE issuance 96792f2f46 (RIV-pm-1, decomposition 1.12): the part month, the two no-curve rules, markers through the
  page day, no zero-dollar marker. Checks drafted by a helper in the round-21 worktree, re-run by the issuer at
  6d7cd1fe3c: FAIL 5 / 4 / 2 on the build arms, controls PASS.
- 1.0.0_SA_CTO~Z msg 31031 on the CVO's round-21 slug: row ETFS_RIVALS-Z-C-S64 BLOCKING (7 folded GQGU securities lost
  their 86 markers); one repair cell; the Lambda deploy waits on it; the pin then holds rounds 15 to 22. AMENDMENT 1
  6ce602bd1e, before any worker was spawned: interface item 4, the marker one-key rule. No gate limb graded it.
- 2.0.0_SA_COO~O msg 31038: gateway r26 live since 14:03:49Z; the chart route is registered (404 until a chart object).
- Worker ~12 spawned in `C:/tmp/wk-riv-r22-12`.

## Tick 6 -- 14:45Z

`ETFS_RIVALS | L7 EXECUTING (FULL) | round 22 | TOs 0/1 | cells 1/1 | thread y | NO-OP on the spawn: the one worker is live; the deploy's COO half is being prepared meanwhile`
