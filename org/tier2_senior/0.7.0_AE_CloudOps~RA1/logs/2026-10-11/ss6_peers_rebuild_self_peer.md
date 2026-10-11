# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-ss-6: the peers rebuilt without the self peer

**Date:** 2026-10-11 (GO 11:15Z; batch 11:2xZ; amended AC1 re-run and ledger closed after msg 3814)
**Task Order:** AMGT_RESAPP.TO-AMGT-ss-6.rebuild-the-peers-objects-without-the-self-peer
**Status:** COMPLETE (AC1 as amended, AC2, AC3 PASS; ledger CLOSED 6 of 6)

## Objective

One batch over the 243 MEASURED subjects writing 243 NEW `peers/v1` objects so that no subject lists its own company.
Run through `lib.research.api.peers_rebuild` (which builds the held-name index), reading the pool's `date=2026-10-02`
universe that ss-5 landed.

## The act
**archetype:** DEPLOY

1. Read both halves and the order; verified the pin (blobs 2 of 2, ss-3 and qq-2 ancestors), recorded the 243 prior
   objects' VersionIds, swept every live worktree (0 naming `peers/v1`) and confirmed the partition string free.
2. Wrote the census baseline and compared it with the issuer's (243 of 243 equal); ran the dry batch and compared it with the
   half's table member by member (231 equal, 12 = the table, count unmoved); ran the ten single-subject dry runs.
3. The write: UPLOADED 243 of 243, read-back 243 of 243, SHARED-DEFECT 0.
4. Verified: partitions (1470 -> 1713 objects, 0 prior VersionIds moved); a full-record compare of all 243 subjects (prior
   partition through the pin's handler vs the live function): the table, no retained-member change, no reorder.
5. AC1 as written read NO on S2/S4 for the signed class B only; reported, amended (`--class-b`), re-run literally -> YES.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L6, close | PASS | opened before the write |
| lib.research.api.peers_rebuild | dry batch, --write-pool | PASS | 243 of 243 |
| r93_self_peer_census.py | AC1, first-written then amended | NO then YES | the first form cannot see class B |
| r89 checks / r92_minor_unit_census.py | AC2, AC3 | PASS | exit 0 |

**What worked:** reproducing the BEFORE from the prior partition (left in place by an additive write) through the pin's own
handler when the live full-field baseline had not been captured; explaining 160 -> 154 exhaustively from the 24 members.
**What failed:** I captured a ticker-and-key baseline, not a full-field one, before the write; the full-record compare had to
be reconstructed afterwards. It was reconstructible only because the write is additive.
**Gap found:** the census defines own-company by served key; a signed class that is not keyed needs an input, as now.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not flip on AC1's first NO | the criterion as written did not pass; waiver or amendment is the issuer's |
| Compared full records, not just member lists | round 91's pp-6 showed a field a signer did not expect can move while the lists agree |
| Stated `peer_read` as a moved subject-level field | it names the new object key and is not in the half's diff table; saying nothing would have hidden an unlisted difference |

## Files Modified

- `org/critical_paths/change_management/20261011T1121Z_amgt-resapp-r93-ss6-peers-rebuild-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the VersionId record, the AC1 finding, the proof instance
- the order's `<status>` (complete)

## Next Steps

1. `[2.0.0_SA_COO~R1]` ss-4's GO; it re-measures against this state. 2. `[1.0.0_SA_CTO~DELL1]` D1-S23 (Sanofi's display
name) is round 94's first cell. 3. `[box-sync / MSTR]` Push the local commits.
