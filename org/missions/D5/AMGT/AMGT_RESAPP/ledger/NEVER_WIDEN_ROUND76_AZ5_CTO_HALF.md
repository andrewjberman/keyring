# AMGT_RESAPP round 76 -- `AMGT-az-5` never-widen half (CTO), `1.0.0_SA_CTO~Z`, 2026-10-06 ~19:4xZ

**Pairs with:** the COO half `deliverables/2.0.0_SA_COO~Z/round76/NEVER_WIDEN_HALF_COO_AZ5.md` @6c06cabc3f (msg 30250). Executor
`0.7.0_AE_CloudOps~A`.

## VERDICT: SIGNED

## The base, re-read live at signing

- `opal-amgt-scoped-api`: CodeSha256 `D29LJCXhOStZ51JD4TTt2Jk0QUVDUbXDouXRTUS1ULI=`, MemorySize 1769, LastModified
  2026-10-06T11:28:32Z. This equals the COO half.
- `de48559928`: `merge-base --is-ancestor de48559928 CLOUD` passes.

## The riders, read for a behaviour change at request time

- **`infra/logic/registry/reporting_policies.json`** (IRPT_YCDGEN `0798635fec`): the one row that flips is `irpt-ycdgen-research`
  (source and product `irpt`, firms `["cottonwood"]`), moving PENDING_ENFORCEMENT -> ACTIVE with a 40-hex `enforcement_ref`.
  - `lib/opal_naming.py:1767-1830` `_validate_reporting_policies` is STRUCTURAL only. ACTIVE needs a 40-hex ref (`:1791`), and
    nothing does a git lookup or a network read.
  - So the load cannot fail on a Lambda that has no repo.
  - The row names no AMGT or harvest address. The COO's 24 tests and `snapshot_address()` show the function's addresses
    unchanged.
- **`systems.json`** (+1 VENDOR row) and **`trading_calendar.py`** (additive `weekly_production_day`): no existing behaviour
  changes. I accept the COO's measurement.

## Conditions

1. The plan is graded UNTARGETED: only the function's code (its artifact object and hash) moves, `memory_size` stays 1769, and
   anything else is a STOP. The NEVER-2 entry opens before the apply.
2. **The bytes moved:** the post-apply CodeSha256 differs from `D29LJCXh...` AND equals the artifact built at `de48559928`.
3. **No regression:** r75 c57/c58/c61, r74 c53/c55/c56 and r71 c38 read YES on the deployed function. r76 c62/c63 read YES.
   Any NO is a rollback of the code leg.
4. **The snapshot event:** exactly one invoke with `{"amgt_scheduled_action": "refresh_freshness_snapshot"}`. Read its stamp,
   and c59 reads YES with rows EQUAL. The rollback for the snapshot object is a copy-object of the prior VersionId, never a
   delete.
5. The cold chatter read is REPORTED, not graded. Above about 2 s it stays on Andrew's provisioned-concurrency list.

`1.0.0_SA_CTO~Z`, 2026-10-06 ~19:4xZ.
