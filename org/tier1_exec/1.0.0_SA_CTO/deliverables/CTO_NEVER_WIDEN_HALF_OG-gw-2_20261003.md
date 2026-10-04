# CTO never-widen half -- OG-gw-2 (grant-writer catch-up apply from af2d762970's closure)

**By:** 1.0.0_SA_CTO~O, 2026-10-03 ~19:4xZ.
**Against:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-gw-2_20261003.md` @a0778885b5
(ask msg 28966).

**VERDICT: SIGNED**, with one condition (G1). The act may touch exactly `mcportal-grant-writer-lambda`'s code. Its
rollback, the targeted re-apply of the saved deployed zip, is pre-measured to `No changes` and stands alone.

## My reads, independent of the worker and the issuer (~19:4xZ)

1. **Live function.** `get-function-configuration`: `CodeSha256` `nhz+dwJsDJLO9X3o1exvKdQ+OYE+PraxZSop2BJt9zI=`,
   `LastModified` 2026-09-30T10:58:57Z, Active/Successful, 3 environment keys. This is the ask's "before".
2. **The released contract.** `git show af2d762970:org/standards/NFRA_OPLGTW_CONTRACT.json`: datasets are `dim_position`,
   `dim_balance`, `dim_asset` and `dim_transaction`. `fields.dim_transaction` holds exactly the ask's 15 columns.

## Why the one widening is signed

- **It completes a widening already signed, rather than starting a new one.** `dim_transaction` entered the contract
  under this seat's ruling B4 (`REINSTATE_RULINGS_20260930.md`, on Andrew-direct ~07:5xZ "get MCPINDEX back online").
  MX-r-6's ANNOUNCE named the change ("it widens what a grant may name"). It released on the gateway under never-widen
  halves on 2026-09-30 18:33Z.
- **The writer is the property's second writer.** "Which grants may name `dim_transaction`" has two writers: the
  gateway's contract and the grant writer's copy of it. The grant writer still refuses only because its 09-30 build
  predates the contract change. That is a staleness accident, not a designed guard.
- **The owner gate stays.** Admission still requires the verified owner, a non-empty subset of the 15 columns, the
  explicit masters and accounts, and the four operations. A column outside the 15 is still refused (the ask's
  `bogus_col` arm).

## G1 -- no grant is written (B2, FWD-9)

- Andrew's B2 ("no auth work now") and the deferral of FWD-9 ("Andrew admits staff one at a time") still stand.
- No seat writes, changes or tests a grant naming `dim_transaction` as part of this act or this round.
- After the apply, such a grant exists only as the verified owner's own act.
- `gw2.AC1`, `gw2.AC2` and the status read are the whole verify. No portal flow is driven.

## Not covered by this half

The CVO half (REQUIRED by R1: `data_entitlement` and the contract decide whom grants admit) is `3.0.0_SA_CVO~O`'s.
