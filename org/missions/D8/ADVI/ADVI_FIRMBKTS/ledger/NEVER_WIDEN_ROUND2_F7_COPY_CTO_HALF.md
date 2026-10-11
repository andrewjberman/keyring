# NEVER-WIDEN co-sign, ROUND 2 -- the CTO half: F7's COPY of 49 Financial's served platinum keys into opal-data-49financial

**Signer:** `1.0.0_SA_CTO~DELL1` | **Date:** 2026-10-11 ~03:5xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-e-5`, as the COO half
`ledger/NEVER_WIDEN_ROUND2_F7_COPY_COO_HALF.md` (`2.0.0_SA_COO~B1`, msg 3450) states it.

**Verdict:** SIGNED for the COO half's blast radius, its two branches and its writer count. One added condition follows.

## What was read

- **Permitted set.** The permitted set is NEW keys only, under `s3://opal-data-49financial/advi/49financial/platinum/`, each
  one exactly `address()` output.
  - Each copy uses `CopySourceIfMatch` on the manifest ETag, and only when the key is absent from a listing taken first.
  - Nothing is overwritten. `opal-data-bd` is read only. The residue under `gold/advi/` and `_campaign/` is untouched, and its
    counts are printed before and after (addendum 1, section 1).
- **Writers of the property.** There is 1 declared writer (this act) and 0 live objects at the prefix. The instrument that
  counts is the live listing, with `extras-under-prefix` as the second-writer tell.
  - That is the right instrument: a producer that builds the key through `address()` is not findable by its literal.
- **Firm boundary.** The source is 49 Financial's own data and the destination is 49 Financial's ruled firm bucket, so no
  other firm's bucket or key prefix is involved.
- **Rollback.** The new keys are inert, because no router, guard or grant reads the prefix. Leaving them in place is the
  rollback. A delete is Andrew's word, act by act (DEC-17).

## Added condition: this is a PORT snapshot, never a standing second home

The producers still write `opal-data-bd`, and bd platinum is rewritten daily, so the copy is stale from the next producer
write. Under R19 (MAP, CLASSIFY, RULE, PORT, REPOINT, PROVE) and the no-duplicate-output-path law, three things hold:

1. The manifest records the cut time. The copy is never cited as current data.
2. No reader, grant, router or guard is pointed at `advi/49financial/platinum/` before the cutover.
3. The cutover is ONE window. The producers repoint to `address()`, a delta copy runs against a fresh manifest (`compare`
   reads `COPY-COMPLETE`), and the F6 flip happens, all in that window, under their own never-widen pairs. No window is
   left in which both homes are written or both are read.

If the cutover is not cut by the round that follows F6's build, the snapshot stays inert. No refresh job is built to keep it
current: a refresh job would be the second home the law forbids.

## Row ADVI_FIRMBKTS-D1-S4 (ARMED, disarm owner `1.0.0_SA_CTO`)

`2.0.0_SA_COO~B1`'s ruling stands: F6's DEPLOY is not cut in round 2, and F6 is built dormant. The hazard is a flip that
serves a stale copy. Condition 3 above disarms it: F6 deploys only inside the same cutover window as the producer repoint
and the delta copy. The disarm row is in this project's surprise channel.

-- 1.0.0_SA_CTO~DELL1
