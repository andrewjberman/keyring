# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-pp-3: 243 peers/v1 objects rebuilt (option B), ledger closed

**Date:** 2026-10-11 (GO 06:53Z; STOP 06:59Z; amended GO 07:02Z; write 07:07Z partition; ledger closed after AC2)
**Task Order:** AMGT_RESAPP.TO-AMGT-pp-3.rebuild-the-peers-objects-against-the-current-scanner
**Status:** COMPLETE (AC1, AC2 PASS; ledger CLOSED 7 of 7)

## Objective

Rebuild every keyed name's `peers/v1` object against the scanner now at asOf 2026-10-02, with the producer's own entry
points, under the pair's never-widen sign-off. The GO's step 1 wrote a fixed existing key, so this seat stopped; the issuer
and the CTO ruled option B (local universe cache, the 243 peers writes only) and the act ran under that.

## The act
**archetype:** DEPLOY

1. Read both halves, the order and the producer. Measured, before any write: producer blobs 5 of 5 equal the GO table,
   scanner asOf 2026-10-02 on six files, 243 prior keys, the latest `universe/v1` key, a 22-worktree open-deploy sweep (0 hits).
2. Resolved step 1's write target (`universe._resolve_home()`): a constant-dated key that EXISTS. STOPPED, wrote the evidence,
   asked both seats. Ruling B in one message from each (msgs 3584, 3586).
3. Opened the entry, ran step 1 into one local cache file (pool object head identical before and after), step 2 dry run
   (DERIVED 194, ABSENT 49, 0 violations; 243 of 243 names equal the issuer's table), a no-collision LIST of all 243
   prefixes, then step 3 `--write-pool`: UPLOADED 243 of 243, read-back 243 of 243.
4. AC1 P1-P6 PASS; AC2 FWD-8 YES on three names, member cap_vintage 2026-10-02 (5 trading days behind), caveat served.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L7, close | PASS | entry opened before the first write |
| lib.research.peers.universe | --refresh under AMGT_PEER_UNIVERSE_CACHE | PASS | no pool put; pool head unchanged |
| lib.research.peers.engine | dry run, then --write-pool | PASS | 243 of 243 uploaded and read back |
| r91_peers_rebuilt.py | AC1 | PASS | P1-P6, exit=0 |
| r90_whole_page_read.py | AC2 | PASS | exit=0 |
| comp-rail hook | a recursive grep over lib/ | DENIED | used the native Grep tool |

**What worked:** resolving the write address from the producer's own function before running its command, which turned a
silent overwrite into a STOP; a LIST-based no-collision pre-check; comparing the dry run with the issuer's table per name.
**What failed:** nothing in the act. One recursive grep was denied by the rail (F1).
**Gap found:** the signed halves described step 1's write as a new `universe/v1/` object; the producer writes a fixed key.
Round 92 cell 1 (key dated by scanner asOf) is the CTO's fix.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Stopped at step 1 instead of overwriting under the pair | BOUNDS 2 and both halves forbid a same-key put; the bucket's versioning is not the pair's rollback |
| Ran the producer from a detached worktree at the pin | the shared tree is dirty and other seats edit it; the five producer blobs are equal in both |
| Archived the 3.7 MB cache beside the entry | AMENDMENT 1 asks for the file and its sha256; a later engine run must use the same bytes |

## Files Modified

- `org/critical_paths/change_management/20261011T0702Z_amgt-resapp-r91-pp3-peers-rebuild-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` PP3 files: prior keys, STOP evidence, whole-page read,
  universe cache archive, proof instance
- the order's `<status>` (complete)

## Next Steps

1. `[2.0.0_SA_COO~R1]` pp-6 re-measures its table against the state this act leaves. 2. `[1.0.0_SA_CTO~DELL1]` Round 92 cell 1,
and the FWD-38 grade on the caveat plus per-member cap_vintage. 3. `[box-sync / MSTR]` Push the local commits.
