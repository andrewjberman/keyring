# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-09-30 12Z-13Z (host opal_bloomberg)

Lease FULL, round 5, limb L7. Thread y.

## Decisions closed this span

- **MX-r-6 v1 VOID (~12:2xZ).**
  - The live gateway moved to 288fa78c93 (NFRA_MCPMSP MS-d-1, 11:37Z) after PHASE A read 093fc247c6.
  - 3.0.0_SA_CVO~O refused the second half (msg 27131). 1.0.0_SA_CTO~O withdrew the CTO half (msg 27132).
  - **My COO half was VOID too:** it signed a base carried from the worker's read, not re-measured at signing.
  - A4 @fc97abbdf7 orders a re-cut on the live base, re-read before the ANNOUNCE and before the deploy.
- **Andrew-direct ~13:0xZ (relayed as msg 27162; record @1eba868308).** Verbatim: "yes thats fine on naming exception.
  Regarding schwab, sure. advi tool, what not yet are you referring to? but yeah certainly whatever needs to be lifted
  should be lifted".
  - MX-t-12 is RELEASED (A1).
  - MX-r-6 A5 allows one existing grant to be widened to `dim_transaction` (commit @d4753af0d2).
  - MX-t-10, MX-t-13 and MX-r-7 stay HELD until the naming gate honours the R20 entry; the gate owner has been asked.
- **MX-t-10 gate run, issuer, ~13:1xZ.** With the ETFS_CANON row on HEAD (fd3b3b7bf2), `naming-gate.py --diff` on
  03a19ac282 reads REFUSE 3 (NEW out-of-pattern). Told the CTO (msg 27173).
- **MX-r-6 v2.**
  - ~19 re-cut on live 288fa78c93: release 63d6094823 / deploy-only 2e2254156e / rollback mx-rb8. MCPMSP's 13 files
    are preserved (11 equal, 2 merged). Tools 52 -> 58. Targeted plan 0/1/0.
  - **Issuer base read at 13:15:59Z:** S3 -latest = 288fa78c93, host 5 ids, 0 gateway ledgers.
  - v2 ask with the COO half @17259505a2.
  - CTO G-A and half @16998169d5. CVO second half @5ac4f48aea, guards G1-G3.
  - Issuer re-read at 13:42:31Z: base unchanged. **GO** at ~13:4xZ: ~19 on PHASE B.
- **Drain of wk-nfra_mcpindex-5-19 ABORTED by the issuer.**
  - The branch carries the release's `deploy-to-ec2.sh` `+schwab` edit. On CLOUD before the halves, it would let any
    seat's CLOUD-based gateway deploy enable Schwab unsigned.
  - An evidence-only carry was then refused by the row gate (W-coordinate rows) and by owned-paths (a worker's
    deliverables dir). My byte-identical copies were removed from the shared tree, and it is clean.
  - Everything drains with the branch after PHASE B.
- **FINDING (~13:4xZ):**
  - `gateway-access-state-table` holds ONE active grant: Alyssa's, portal-only, with no masters or datasets.
  - `data_entitlement.decide` denies every Schwab tool without a grant naming Schwab masters and datasets.
  - So no existing Schwab grant exists for A5 to widen. Asked the CTO to carry a NEW grant to Andrew (admission,
    FWD-9). I will not widen Alyssa's portal-only grant.
  - The deploy is still safe: the tools are hidden and denied for all principals.
- **MX-t-12:** ~20 spawned ~13:2xZ; it dry-runs the naming gate on the advi key first.

## State at 13:50Z

- Round 5: 3 of 7 complete.
- MX-r-6: PHASE B in flight (~19). MX-t-12: in flight (~20).
- HELD: MX-t-13 and MX-r-7 (R20 gate edit).
- Round 4: MX-t-10 (same edit); MX-s-14 (its fires).

## Compiler Tools
- None. The reads were S3 list-objects, SSM host reads (via the r6.AC2 check), `deploy_ledger.py list`, a DynamoDB
  scan/query of the access-state table (read-only), and the naming gate's `--diff` dry run.
