# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-ss-5: the candidate universe at its own dated key

**Date:** 2026-10-11 (GO 11:07Z; write 11:11:09Z; ledger closed after AC1/AC2)
**Task Order:** AMGT_RESAPP.TO-AMGT-ss-5.the-candidate-universe-takes-the-scanners-vintage-as-its-own-key
**Status:** COMPLETE (AC1 and AC2 PASS; ledger CLOSED 5 of 5)

## Objective

One additive store write: the candidate universe at `candidate_universe/date=2026-10-02/`, the option C that round 91's
ADDENDUM 2 owed (the key now carries the scanner's own date). The old key `date=2026-08-06` is untouched.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin (universe.py `fcd61615156e`, qq-2 an ancestor), the six scanner
   files' asOf (all 2026-10-02), the old key's VersionId, the new key's absence and the open-deploy sweep (0 hits).
2. Dry build in memory at the pin: 2856 rows, 3759160 bytes, sha256 `8e652b08..`, equal to the pair's and to round 91's
   archived cache after pooling. Compared BEFORE the put.
3. The one write: `universe --refresh`, cache override unset. Read back: 3759160 bytes, digest equal, one version; the old
   key's VersionId unchanged.
4. AC1 (U1-U4) YES; AC2 YES with the function's CodeSha256 unchanged.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L5, close | PASS | opened before the write |
| lib.research.peers.universe | dry build; --refresh | PASS | digest equal before the put |
| r93_universe_pool.py | AC1 | PASS | base NO (U1, U2, U4 FAIL), after YES |
| r89 checks | AC2 | PASS | exit 0 |

**What worked:** comparing the digest in memory first, so the put was a confirmation and not an experiment; reading the
model-block directory against the checkout instead of taking "machine-dependent" as given.
**What failed:** nothing.
**Gap found:** the COO half called the two model-block-only rows device-dependent; they are tracked at the pin. A future
half can state the digest is reproducible from the commit.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Verified the model-block input by reading the directory | the half's own STOP list turns on that digest; the answer changes what a different device would do |
| Left the old key alone, did not touch the PP3 cache file | the cache file is round 91's record and its sha256 is cited by two entries |

## Files Modified

- `org/critical_paths/change_management/20261011T1110Z_amgt-resapp-r93-ss5-universe-key-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the proof instance
- the order's `<status>` (complete)

## Next Steps

1. `[2.0.0_SA_COO~R1]` AMGT-ss-6 (the peers rebuild) reads this key; it re-measures against the current peers state.
2. `[1.0.0_SA_CTO~DELL1]` The pp-3 cache-file rule retires with this object. 3. `[box-sync / MSTR]` Push the local commits.
