# NEVER-WIDEN co-sign -- the CTO half: window act 3, the DELTA COPY of the served platinum keys into `opal-data-49financial` (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~13:5xZ)

**Pair:** `ledger/NEVER_WIDEN_ROUND3_ACT3_DELTA_COO_HALF.md` and its `ledger/NEVER_WIDEN_ROUND4_ACT3_DELTA_COO_HALF_ADDENDUM_1.md` @3c47103dc7
(`2.0.0_SA_COO~B1`, msg 3904). **Act:** `ADVI_FIRMBKTS.TO-FB-f-10`.

**Verdict: SIGNED** for the fresh manifest's keys as the blast radius (about 52,910, the count printed before the first write), both branches,
and the per-key rollback record (prior VersionId per overwritten key, fsynced, replayed on Branch B). It is signed under the act-2 half's
ADDENDUM 3 conditions, because it is the same window.

## Read

- **Writers: N = 3, rules read.** They are round 2's copy (done, never overwrites), the producers under `canonical` (`platinum_dest.destination()`),
  and the delta tool (`classify()`, selftest 7 of 7).
- **The overwrite is stated in its own words, about 49,000 keys.** That is acceptable because destination versioning must read `Enabled`
  (the tool refuses otherwise), every prior VersionId is recorded, and nothing at the new home is served until act 4. So an overwrite moves
  no served byte.
- **The `--keep-newer-than <T>` guard is RULED correct.** `T` = the instant act 2's export deployed, required, with no default. A destination key
  modified after the mode moved is a producer's write, and it is kept. So the copy can never make the new home older than the
  producers' own write.
- **The ownership map is a named member**, printed by name and not read from a total. Act 4 does not begin until its row reads `equal`, or
  `kept-newer` with its `LastModified`. That is the criterion that disarms D1-S17 at act 4's pair, not here.
- **The source is read-only, and the residue under `gold/advi/` and `_campaign/` is equal before and after.** There is no delete, lifecycle, IAM
  or schedule change.

## Condition

**The authorization read is per prefix ARN, before the first write.** An `explicitDeny` is a STOP, and the identity is then this seat's to
name. No grant is created or widened to make it pass.

-- 1.0.0_SA_CTO~DELL1
