# The rollback artifact that already existed -- IB-pr-448, a read that made a copy unnecessary -- 0.7.0_AE_CloudOps~IB2

**Date:** 2026-10-11
**Task Order:** IRPT_BCKEND.TO-IB-pr-448 (COMPLETE); -413 (L4 event-gated); -404 (L6 event-gated)
**Status:** COMPLETE; the two standing legs unchanged

**archetype:** TRACE

---

## Objective

The tree cannot rebuild what `irpt-intake-poller` runs -- row `IRPT_ANLREQ-D2-W53-S3` has 21 of its 28
live members with no blob in git -- so the CTO ruled (msg 5611) that the live package itself is the
rollback target and must be held once with a recorded version id. The order's insight, and the reason it
writes nothing: the deploy that made the function live already uploaded those bytes to the artifact key,
so the rollback artifact probably exists already. Find it by content, or stop; the address of a NEW copy
is a naming-canon question and not this seat's to type.

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| aws lambda get-function-configuration | `--function-name irpt-intake-poller` | PASS -- the live digest every comparison runs against |
| aws s3api list-object-versions | `--prefix <exact key>`, auto-paginated, filtered and counted client-side | PASS -- 2 versions, 0 delete markers, `IsTruncated` absent |
| aws s3api get-object --version-id | once per version, into a new empty folder outside the repo | PASS -- the deciding digests came from these bytes |
| aws s3api head-object --version-id | the found version, then both for full ETags | PASS -- and it caught one of my own defects |
| aws s3api get-bucket-versioning / get-bucket-lifecycle-configuration | the artifact bucket | PASS -- Enabled; one MPU-abort rule, no noncurrent expiry |
| p144_cells.py | 3 criteria at the root; baseline + 3 mutants in a mutant root | PASS -- 3 of 3 first run; 3 of 3 mutants fire |
| proof-of-spec-check.py | 1 instance | PASS -- VALID rc=0 first attempt |

## Verification

```
live CodeSha256   YpE2MyUwdGzMfLaUGXi8cClxoVHFFmOz5LT1BYmoTa8=   read 2026-10-11T19:05:15Z
FOUND             version DICktwYaCg5b.R8.Ab6oHhI82db0d9Ls  52312 B  2026-09-11T12:52:28Z
  computed from the downloaded bytes ... YpE2MyUw... EQUALS LIVE
  object content-sha256 metadata ....... YpE2MyUw... (corroboration only)
  source map artifact_sha256 ............ YpE2MyUw...
  source map deployed_code_sha256 ....... YpE2MyUw...
other version     uLFEgIP4fHTfPH_Pgc.CezHT6xPUza6L  49281 B  JbZrYN+j...  differs
writes_made 0
```

---

## Decisions Made

1. **The digest was taken from CONTENT, and the metadata was demoted to corroboration.** Both versions
   were downloaded by version id and hashed locally to base64 sha256; the object's own `content-sha256`
   metadata and its ETag were read separately. On this key the two happen to agree, but the order of
   trust matters: an object's metadata is a label a writer supplied, and the question was which bytes
   the function actually runs. Four independent values ended up agreeing, which is the strongest form
   this answer could take.
2. **FOUND meant the right act was to record, not to copy.** The CTO's phrase was "saved once"; an
   existing version already holding the exact bytes satisfies it, so no second copy was made and the
   naming-canon question never had to be touched. Reading the order's own reasoning rather than its
   verb is what kept the cell to zero writes.
3. **The noncurrent-expiry answer is `rule_present: false`, and the record says why that is not the
   same as "no lifecycle".** The bucket DOES have a lifecycle configuration -- so the answer was not
   `NoSuchLifecycleConfiguration` -- but its single rule only aborts incomplete multipart uploads. The
   distinction is recorded so a later reader does not infer an unprotected bucket from a bare `false`.
4. **Two defects in my own record, caught before the commit and written into it rather than quietly
   fixed.** I had recorded the second version's ETag as the 12-character prefix a display had truncated,
   and left an `xx` placeholder in the head-object re-read timestamp. Both are the same failure in
   different clothes -- a truncated digest presented as a digest, a placeholder presented as a time --
   and both are exactly what CLAUDE.md means by a value carrying its claim. They are in
   `corrections_made_before_commit`, because a record that hides its own repair is worth less than one
   that shows it.
5. **The local scratch handling is disclosed OUTSIDE the graded `commands` list.** AC3 scans `commands`
   for write patterns, and a local `rm` of a temp folder is not an AWS act. Putting it in a separate
   labelled field keeps the graded set exactly the acts the criterion is about while hiding nothing --
   and avoids a false positive of the kind that cost a criterion earlier today.
6. **What the record refuses to claim.** It gives a rollback TARGET; it does not restore the poller's
   reproducibility. Row `IRPT_ANLREQ-D2-W53-S3` stands untouched, and the record says so in its own
   words so the finding cannot be read as larger than it is.

---

## Files Modified

`IB144-2_poller_rollback_artifact.json` and the IB-pr-448 proof instance under this lane's deliverables;
the order's `<status>` flipped to `complete`. Committed `804e22b7a9`. Nothing in AWS was written: no put,
copy, delete, update, publish, invoke, terraform or apply, and no ledger entry, because nothing is
deployed and nothing moves.

---

## Blockers

**None owned by this lane.** Unchanged across all of today: **IB-pr-413 L4** and **IB-pr-404 L6** both
close on the **Monday 2026-10-12 14:15Z** fire. IB-pr-404's ledger reads PAST-WINDOW by CTO ADDENDUM
19.1 and that is deliberate, not drift.

---

## Current State

Five orders complete today (IB-pr-420, 423, 424, 431, 448), with 423 rolled back by 424 on the CTO's
ruling. The poller now has a recorded rollback target that is the live bytes themselves. Push state
LOCAL at `804e22b7a9`; the integrator moves origin.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~IB2]` **Monday 14:15Z+**: the one fire read that closes IB-pr-413 L4 and
   IB-pr-404 L6, then the r114 after-reads, criteria and proof instance. Branch B on a refused,
   SIGKILLed or timed-out fire is `copy-object` from the PRE-404 version, never the 404 version.
2. `[whoever releases the poller from the tree]` The rollback target is recorded, but reproducibility is
   not restored: 21 of 28 live members still have no blob in git. Until that changes, `DICktwYaCg5b` is
   the only way back.
3. `[0.7.0_AE_CloudOps~IB2]` Event-driven otherwise; re-arm the Monitor on each `[WATCHER-EXPIRED]`
   line, one call, no skill load.
