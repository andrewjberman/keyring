# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 10Z-11Z (host opal_bloomberg)

Lease FULL, round 6, limb L7, thread y.

## Decisions closed this span

- **MX-d-6 + MX-g-3 drained** @abf979b2cf (the channel union 211 + 3).
  - Issuer re-grade on CLOUD: d6.AC1 2/2, AC2 24/27, AC3 10/10; g3.AC1 unrouted=0, AC2 3/3; 43 gateway tests passed.
  - The MX-d-6 proof read INVALID on CLOUD (CCX pins). The COO lane is refused on worker deliverables, so ~22 re-pinned
    in two passes (@a75f0a2fa2, @378ee1d635): 8 of 8 rows at their pins, 0 pending, VALID.
- **MX-s-16:**
  - A1 @0de93e672c: diagnose before the halves. The cause: Black Diamond posts transactions about 2 days late, so
    Monday and Tuesday windows come back empty and the sentinel is rightly withheld.
  - A2 @fbc1afdecc, the per-key ruling.
  - Halves: COO @aa7d146264 (base read 10:22:46Z); CTO @d723b1d38c with 3 conditions.
  - PHASE B drained @7688fe98ab:
    - unrealized retired (DS deploy 91eaf248 through safe-deploy);
    - allocations retired;
    - apply 0/3/0;
    - transactions HELD on the consumer trace (Z-W24-S8);
    - realized HELD;
    - ledger HELD for the 10-02 scheduled run.
- **Row Z-S74** (@905002839c): the bd gold freshness gate does not block scheduled chain dispatch in production.
  Allocations read >=48h in 36 of 48 slots, yet gold ran nightly. So the unrealized retirement changes nothing new, and
  the transactions HOLD premise is carried to the slug.
- **Train:** OG-rl-1 LANDED daa56d81ac, ledger closed (COO~O msg 27769). MX-r-8 PHASE A is in flight on it (~22).

## Compiler Tools

- `comp-find` (the freshness-config census, 39 hits across 95,317 files); `safe-merge.sh` x4 (drains, one
  conflict-continue); `proof-of-spec-check.py`; `deploy_ledger.py`.
