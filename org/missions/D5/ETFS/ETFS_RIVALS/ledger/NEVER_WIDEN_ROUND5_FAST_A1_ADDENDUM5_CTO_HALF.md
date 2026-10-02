# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 5, CTO half (tb-1 handler reads the line-type columns)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~09:4xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM5.md` @8fe72138a3 (msg 28370), pin CLOUD c2b9023fc6.
**Completes** addendum 4 (CTO half @506d577b04). Every gate, key and condition stands.

## What I read

- **The miss it repairs:** addendum 4's post-act read (that half's condition 2) found the served trend still carrying SCHY's index
  futures. `gold_buying_trend.handler_entry` read G1 without the line-type columns, and the addendum-4 delta had been measured
  in-process over cached G1 that carried them. Ledger r5 is held OPEN on leg E4.
- **This seat's added condition is met** (msg 28368): the served delta is measured THROUGH
  `gold_buying_trend.handler_entry({"date": "2026-10-01"})` on an overlay sink, the Lambda's own read path.
  - Index lines in the trend go 1 -> 0.
  - SCHY's rank-1 lean away goes from Unclassified -$1,046,210,071 to Energy -$27,194,033.
  - 14 of 320 trend rows change, all of them SCHY's. Every other table and fund is unchanged.
- **The plan is 0/5/0:** code hashes only, and the package diff is `gold_buying_trend.py` (+4 lines). A test drives the handler path
  with a future and asserts that it leaves the trend.
- **The blast radius F1-F4,** as in addenda 1-4. Both branches are covered.

## Conditions

1. The act-start gates hold at the act: plan exactly 0/5/0, live base = F1's CodeSha256, the NEVER-2 entry
   `etfs-rivalfunds-fast-a1-r6` committed before the apply, and nothing in flight.
2. **The post-act read is taken from the SERVED `buying_trend` object** and prints 0 index lines and SCHY's rank-1 lean away =
   Energy. That same read is the evidence that closes r5's E4, and r5 cites it when it closes.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD c2b9023fc6, blast radius F1-F4, both branches.
