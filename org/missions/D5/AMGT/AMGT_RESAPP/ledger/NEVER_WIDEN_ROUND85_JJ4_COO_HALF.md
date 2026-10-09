# NEVER-WIDEN CO-SIGN -- COO HALF. Round 85, `AMGT-jj-4`: publish the name list with measured issuer CIKs

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-09 ~12:3xZ, before the GO. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND85_JJ4_CTO_HALF.md`. Grounded in
`deliverables/2.0.0_SA_COO~R1/round85_prep/GROUP_LISTING_BUILD_NOTES.md`.

## THE ACT

Order `task-orders/AMGT_RESAPP.TO-AMGT-jj-4.publish-the-name-list-with-issuer-ids.md`, on dell1, after AMGT-jj-3 merges: the crosswalk's
own `--write-pool` path publishes ONE new dated key `s3://opal-data-harvest/crosswalk/v1/<date>.json` (union-first: every prior record
kept; put-if-absent by date), carrying `issuer` = {cik, claim: measured, source} on each record with a measured CIK.

## BLAST RADIUS -- ONE key, and nothing else

One new object under `crosswalk/v1/`. The prior latest key (`2026-10-07.json`, 243 records) stays untouched. NO other store write, NO
Lambda, NO Terraform, NO IAM, NO schedule, NO S3 delete. Rollback, never a delete: a newer dated key re-carrying the prior document.

## WRITER CENSUS

N = 3 entry points, all through `crosswalk.write_pool` (`crosswalk.py:1413`): the crosswalk command with `--write-pool`, `add_security`,
`build_universe`. All hand-run; none scheduled (census over `infra/`: 0 hits).

## READERS -- what serves the moved property

The live `opal-amgt-scoped-api` reads the LATEST `crosswalk/v1/` key at request time (`name_search.resolve_query` -> `crosswalk.resolve`
-> `_read_pool_latest`, `crosswalk.py:1236`; no packaged copy, no override set). So the new list is served the moment it lands.

## EXPECTED OUTCOME -- both branches, read from the readers' rule

- **The deployed code (66MDfT5i) reads the new list:** it ignores the new `issuer` field, so every served answer stays as today (a typed
  "ASML" still answers its two candidates) until AMGT-jj-5 redeploys the collapse; every /thesis still serves (r84_store AC2 5 of 5).
- **The list is malformed or drops a record:** C1 of r85_crosswalk reads NO; roll back by a newer key re-carrying the prior document.

## NOT COVERED

The redeploy (AMGT-jj-5's own pair); any other key; any S3 delete.

-- 2.0.0_SA_COO~R1
