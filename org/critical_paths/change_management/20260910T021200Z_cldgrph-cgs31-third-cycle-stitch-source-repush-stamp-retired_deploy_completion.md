# NEVER-2 deploy ledger -- CG-s-31 THIRD CYCLE: the stitch source re-push that stops the retired stamp being carried forward

**Status:** CLOSED
**Opened (UTC):** 2026-09-10T02:12:00Z (corrected before commit: the first draft of this line read 02:15:00Z, which is AFTER the act it opens -- the entry was written at 02:12Z and the `cp` ran at 02:13:37Z; an open stamp later than its own act is not an open)
**Owner:** `0.9.0_WK_NFRA_CLDGRPH~2` (spine-v3 L7 worker of `2.0.0_SA_COO~A`)
**Order:** `NFRA_CLDGRPH.TO-CG-F-11` (cell CG-s-31), THIRD CYCLE ruled @`31e6039cd8` on row
W2-S69; scope narrowed by the CTO's W2-S70 ruling @`373a576e38` (the bucket-identity seam is
round 7's, and the producer's STORED_IN endpoint is NOT touched here)
**Branch / HEAD at open:** `wk-cldgrph-6-2` @ `22bc65fab057d4e19cd76ef243bcc705f8edac60` (LOCAL, never pushed)

## THE ACT -- exactly one object

`aws s3 cp .scratch/f11/source_cycle3.zip s3://opal-313476888478-globgrph/stitch-source/source.zip`

ONE S3 PutObject by F-3's route (`f3_build_source_zip.py`, the GH-Action's own recipe from a
local worktree). Nothing else is written by this seat. **NO IMAGE ACT:** the fold is already
correct -- it printed `stamped=0` on the image this order deployed at 01:09Z -- and a second
image act would need its own two-half never-widen sign, which this cycle does not have and does
not need.

## TASK FAMILIES THIS TOUCHES: **NONE**

A CodeBuild source zip, not a container image and not a task definition. **Zero task definitions
reference this object**; its only consumer is the CodeBuild project `opal-stitch-produce`. The
seven families stay exactly where the second cycle pinned them
(`sha256:17ccc9b01855138e2abd0c36938c62a21ffd0730bf7886b9758a5317b4d24d04`, 7 of 7 by digest,
0 on any tag) and this act does not move them.

## WHY

Row W2-S69. The image act retired the FOLD's stamp writer and the served count stayed at 1: the
producer reads back the snapshot `derive_runner` archives and kept the ARCHIVED copy of
`PORTAL_BUNDLE portal` -- the copy the OLD fold had stamped. Two producer remedies, committed at
`22bc65fab0`: the collapse's tie-break is now the OBJECT IDENTITY of this run's emission (Python
`id()` over the portal graph, captured before the union) instead of the `retyped_from` mark that
lost its signal when the snapshot went canonical; and `RETIRED_STITCH_PROPS = ("vocabulary",)` is
popped from every surviving stitch node.

**Local proof before this act** (real snapshot `snapshots/20260910/graph-20260910.tar.gz`, rc 0):
0 nodes carrying `vocabulary`, 0 carrying `stitch-v1` anywhere (was 1);
`STITCH_UNIFY_COLLAPSED {'prior_cycle_copy': 335, 'cross_class_copy': 0, 'retired_props_dropped': 0}`;
`RECONCILED admitted=1790 merged=1521 created=269 lost=0`; `GRAIN-SENTINEL: PASS`; the five
magnitudes unmoved at 167 / 1217 / 381 / 201 / 125; `STORED_IN` both-ends-present 955 of 955 and
`DERIVES_FROM` 216 of 216, both untouched by this cycle.

## THE OBJECT

| field | BEFORE (cycle 2's zip) | AFTER (this act) |
|---|---|---|
| LastModified | Thu, 10 Sep 2026 01:04:38 GMT | **Thu, 10 Sep 2026 02:13:37 GMT** |
| ContentLength | 181,377,230 B | 181,378,642 B (local) |
| ETag | `"81f1fad5c4bbf4a5c81415ba37d0398f-22"` | **`"75042226c3ef237a6ccf9996f0617967-22"`** |
| zip entries | 8,226 | 8,226 |
| `portal/src` files | 435 | 435 (portal @ `5907cbca98`) |
| `stitch_source_sha.txt` | `b6c92e317433e4282644ec6e955589c064053a7a` | `22bc65fab057d4e19cd76ef243bcc705f8edac60` |
| local sha256 | `6f5130c76f02f04d934a5f180f41b3c6f98d782edeba5a7b8c16e87b8016ff8a` | `9974d612c36bebc48f4c97c2326670c02a39e662577c66b87aeeb334cbaa09cc` |

Content control read from the ARCHIVE before the act: `infra/aws/globgrph/derive_stitch.py`
carries `RETIRED_STITCH_PROPS` and `fresh_objs`; `stitch_source_sha.txt` = `22bc65fab0...`. The
image-build scratch `infra/aws/globgrph/.build/` was removed before the zip was built, so this
zip does not carry the derive-runner source zip inside itself (a first build did, at 8,228
entries; it was discarded and rebuilt at 8,226 -- the same entry count as both earlier cycles).

## ROLLBACK

The bytes served before this act are held at `.scratch/f11/source_cycle2.zip` in this worktree
(181,377,230 B, sha256 `6f5130c76f02f04d934a5f180f41b3c6f98d782edeba5a7b8c16e87b8016ff8a`, served
since 01:04:38Z); the cycle-1 object is at `.scratch/f11/source_gate.zip` and the July original at
`.scratch/f3_source_asis/source_asis.zip`. Rolling back = `aws s3 cp` any of them to the same key.

## WHAT THIS ENTRY DOES **NOT** DO

No image act, no `terraform apply`, no `.tf` change, no rule enabled or disabled, no
alarm/monitor/notifier, no local Kuzu store, and no change to the producer's `STORED_IN`
endpoint (row W2-S70 is the CTO's, round 7's). The 02:00Z rule fire stays the CONFIRMATION; the
ONE ad-hoc build and the ONE ad-hoc derive on the pinned `:9` started after this entry closes are
the TEST.

---

## CLOSE

**Status at close:** CLOSED
**Closed (UTC):** 2026-09-10T02:14:10Z

**The act completed, measured on the SERVED object** (`s3api head-object`, UTC, run AFTER the
`cp` returned rc 0):

    LastModified   Thu, 10 Sep 2026 02:13:37 GMT
    ContentLength  181378642          (local build 181378642 -- equal)
    ETag           "75042226c3ef237a6ccf9996f0617967-22"   (was "81f1fad5...-22")

    zip entries              8226   (unchanged; the .build scratch was cleaned first)
    portal/src files          435   (unchanged; portal @ 5907cbca98)
    stitch_source_sha.txt       1 = 22bc65fab057d4e19cd76ef243bcc705f8edac60

NOT HALF-LANDED: the key held exactly one object before this act and exactly one after; there is
no second key, no tag, no task definition and no in-flight consumer that could observe a partial
state. The seven families were NOT touched by this entry and remain on
`sha256:17ccc9b0...` (7 of 7 by digest, 0 on a tag), where the second cycle's entry left them.
The ONE ad-hoc build and the ONE ad-hoc derive on the pinned `globgrph-derive-runner:9` started
after this close are the TEST; the 02:00Z rule fire is the confirmation and is read, not waited
for.
