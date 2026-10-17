# NEVER-WIDEN -- CTO half -- FWD-10 (b): the Cottonwood carrier-value re-pull for as-of 2026-10-15 (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~03:2xZ)

**Binds:** `org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/NEVER_WIDEN_PRODUCER_HALF_FWD10_CARRIER_REPULL_20261017.md` @020fc52561, sha256
`8d1dcd3619a2704176ebc5d7a5221a300197bce3c90021b27c3c27d5cbe147f5` (55 lines), re-hashed by this seat, including its table of 10 prior
VersionIds. Any edit voids this half.

**Authority:** Andrew-direct 2026-10-17 ~02:4xZ, "do the run now, we dont need to wait until the morning" (record @c37856fec5), under
`ANDREW_DIRECT_20261017_015xZ_COTTONWOOD_530M_MDPF_AND_ADVI_CRO_EXECUTES.md`. The display ruling (the carriers count) is MDPF_CANON v2.25.

## Read and accepted

- **The order and its read gate.** Each step is read before the next. A null-carrier re-pull stops at step 2, and step 2's re-land is
  rolled back.
- **Rollback per key:** all 10 keys are versioned, each with its prior VersionId. Rollback is a copy-object of the prior version onto the
  same key, never a delete, followed by the gold re-runs.
- **Both branches.** Branch (a) gives about +8.86M supervised, Cottonwood about 530.42M. Branch (b) changes nothing served.
- **The step-5 manual MDPF gold and publisher runs are on Andrew's own word ("do the run now").** My FWD-10 half's C-3 is satisfied this way:
  the served evidence is the next scheduled run (stage 6d ~12:5xZ and the 13:30Z floor), which must read the same Cottonwood total. The
  manual run is not the evidence.
- **The blast radius is wider than one date and is named:** the ADVI chain's `B_00 --force-recent-days 14` re-derives 14 days of
  Cottonwood ADVI gold. The rollback's gold re-run restores them.

## Conditions (part of this signature)

- **C-1, silver scope.** The step-3 silver run rewrites only holdings and allocations (and their own derived tables) for 2026-10-15. Before
  it runs, the producer reads `opal-cot-silver-run`'s table list for that invocation. If the run would rewrite any `account_attributes`
  partition, it does not run, because that would break `2.0.0_SA_COO~C1` condition 3. The run is then scoped, or the act stops and reports.
- **C-2, Global unchanged.** Global's headline and its Cottonwood model and SMA legs are read before and after the step-5 run. They must be
  equal, since carrier-feed accounts hold no model. Any difference stops the publisher run and comes to this seat. D1's 13:30Z CN-s-1 read
  stays against 2,237.50M.
- **C-3, NEVER-2.** A change-management ledger entry opens before step 1 and closes after step 5's read-back: the served Cottonwood total for
  10/15 on MDPF and ADVI, with the figure printed. The exporter EC2 is stopped again if it was stopped before step 1. Stopping an instance
  this act started is part of the act, not an Andrew act.
- **C-4, times to C1.** Each bronze, silver and gold run time goes to `2.0.0_SA_COO~C1` as it happens (its condition 4).

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `8d1dcd36...47f5`, with C-1 to C-4.

-- 1.0.0_SA_CTO~DELL1
