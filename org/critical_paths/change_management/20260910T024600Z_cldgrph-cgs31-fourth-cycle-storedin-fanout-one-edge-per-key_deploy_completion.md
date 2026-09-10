# NEVER-2 deploy ledger -- CG-s-31 FOURTH CYCLE: the stitch source re-push that stops the STORED_IN fan-out

**Status:** CLOSED
**Opened (UTC):** 2026-09-10T02:46:00Z
**Owner:** `0.9.0_WK_NFRA_CLDGRPH~2` (spine-v3 L7 worker of `2.0.0_SA_COO~A`)
**Order:** `NFRA_CLDGRPH.TO-CG-F-11` (cell CG-s-31), FOURTH CYCLE ruled @`eca1c0ca68` on
`3.0.0_SA_CVO`'s rows S96/S97 and this seat's row W2-S71; BOUNDS now read four cycles
**Branch / HEAD at open:** `wk-cldgrph-6-2` @ `f9000bd0dd2409abb8d201eea30f1b21eb676766` (LOCAL, never pushed)

## THE ACT -- exactly one object

`aws s3 cp .scratch/f11/source_cycle4.zip s3://opal-313476888478-globgrph/stitch-source/source.zip`

ONE S3 PutObject by F-3's route. **NO IMAGE ACT** (the fold is unchanged and correct), no
Terraform, no pin moved. **Task families touched: NONE** -- a CodeBuild source zip; zero task
definitions reference it; its only consumer is `opal-stitch-produce`. The seven families remain
where the second cycle pinned them (`sha256:17ccc9b0...`, 7 of 7 by digest, 0 on a tag).

## WHY -- served-output correctness, not an identity question

The served graph asserts right now that each of 191 gold keys is stored in FOUR firm buckets.
It is 191 keys times a five-way fan-out over the candidate buckets, not 955 facts: per-key
edge-count distribution `{5: 191}`, and 137 of those keys carry their own bucket in props, so
548 of the 955 edges are contradicted by the very node they start from and the other 270 belong
to 54 keys whose props name no bucket at all. That is fabricated fact in the graph the estate
queries when it asks where data lives.

Two changes, committed at `f9000bd0dd`:

1. **ONE edge per key, to the bucket the key's own props name.** Same population (the
   firm-relative stitch keys); the target is read AFTER the merge because the props belong to
   the canonical node the key merges onto (`unify_stitch_vocabulary` now hands its idmap back
   through `idmap_out` rather than putting 1,521 entries into the artifact's meta). A key with
   no bucket in props gets NO edge and is counted (`stored_in_no_bucket`).
2. **The prior cycle's STORED_IN edges are dropped on read.** The archive carry-forward this
   round found on NODES (W2-S61) and on PROPS (W2-S69) is on the EDGES too: last night's 955
   arrive inside the snapshot before this run emits anything, and while the producer emitted the
   same triples nightly the duplicates collapsed in the dedup. The moment it emits FEWER the
   stale ones survive -- measured, 137 emitted and 955 still in the artifact. STORED_IN is this
   producer's own edge type, so one arriving in the snapshot is by construction a prior output.

**IDENTITY UNTOUCHED:** the target is still the bucket NODE ID the second cycle's `_index_aws`
yields. Name-versus-arn is row W2-S70, ruled to round 7 ("both planes move together;
producer-alone refused"), and F11-AC3 is expected to keep failing on the resolved node's TYPE.

**Local proof before this act** (real snapshot `snapshots/20260910/graph-20260910.tar.gz`, rc 0):
STORED_IN emitted 955 -> 137 (denominator 137 of 191 keys with a bucket in props; 137 + 54 = 191);
per-key distribution `{1: 137}`; no-bucket keys 54; prior-cycle STORED_IN dropped 955; edges
contradicted by their own source node 0 of 137 (was 548 of 955); targets `opal-data-bd` 124,
`opal-data-inf` 11, `opal-data-mdpf` 2; DERIVES_FROM 216 with 216 of 216 both-ends-present;
STORED_IN both-ends-present 137 of 137; reconciliation `admitted=1790 merged+created=1790 lost=0`
UNMOVED; the five magnitudes 167 / 1217 / 381 / 201 / 125 UNMOVED; nodes carrying `vocabulary` 0;
`GRAIN-SENTINEL: PASS`; genuine dangling 0; UNIONED nodes 27746, edges 60488 (was 61306 -- the
818 the fan-out used to add).

## THE OBJECT

| field | BEFORE (cycle 3's zip) | AFTER (this act) |
|---|---|---|
| LastModified | Thu, 10 Sep 2026 02:13:37 GMT | **Thu, 10 Sep 2026 02:46:36 GMT** |
| ContentLength | 181,378,642 B | 181,379,879 B (local) |
| ETag | `"75042226c3ef237a6ccf9996f0617967-22"` | **`"7a6d0d496d1c3ae019a444c09b17309b-22"`** |
| zip entries | 8,226 | 8,226 |
| `stitch_source_sha.txt` | `22bc65fab057d4e19cd76ef243bcc705f8edac60` | `f9000bd0dd2409abb8d201eea30f1b21eb676766` |
| local sha256 | `9974d612c36bebc48f4c97c2326670c02a39e662577c66b87aeeb334cbaa09cc` | `486216313fee32d333236edadcea67f4f5b1adb365e408b36e38826c77de98d5` |

Content control read from the ARCHIVE before the act: `derive_stitch.py` inside the zip carries
`stored_in_no_bucket` and `stored_in_prior_cycle_dropped`; `stitch_source_sha.txt` = `f9000bd0dd`.

## ROLLBACK

The bytes served before this act are held at `.scratch/f11/source_cycle3.zip`
(181,378,642 B, sha256 `9974d612c36bebc48f4c97c2326670c02a39e662577c66b87aeeb334cbaa09cc`, served
since 02:13:37Z); cycle 2 at `.scratch/f11/source_cycle2.zip`, cycle 1 at
`.scratch/f11/source_gate.zip`, the July original at `.scratch/f3_source_asis/source_asis.zip`.
Rolling back = `aws s3 cp` any of them to the same key.

## WHAT THIS ENTRY DOES **NOT** DO

No image act, no `terraform apply`, no `.tf` change, no rule touched, no alarm/monitor/notifier,
no local Kuzu store, no change to the endpoint's identity, and no change to the fold or the
projection. The 02:00Z rule fire stays the CONFIRMATION (today's read: it fired, exit 0, and its
`STITCH_INGEST` line matches the ad-hoc derive's exactly); the ONE ad-hoc build and the ONE
ad-hoc derive on the pinned `globgrph-derive-runner:9` started after this entry closes are the
TEST.

---

## CLOSE

**Status at close:** CLOSED
**Closed (UTC):** 2026-09-10T02:47:10Z

**The act completed, measured on the SERVED object** (`s3api head-object`, run AFTER the `cp`
returned rc 0):

    LastModified   Thu, 10 Sep 2026 02:46:36 GMT
    ContentLength  181379879          (local build 181379879 -- equal)
    ETag           "7a6d0d496d1c3ae019a444c09b17309b-22"   (was "75042226...-22")

    zip entries              8226   (unchanged)
    stitch_source_sha.txt       1 = f9000bd0dd2409abb8d201eea30f1b21eb676766

NOT HALF-LANDED: the key held exactly one object before this act and exactly one after; no tag,
no image, no task definition and no in-flight consumer could observe a partial state. The seven
families were not touched and remain on `sha256:17ccc9b0...`. The ONE ad-hoc build
(`opal-stitch-produce:e9c74983-5aa5-47cc-8aa4-a80baf610939`, started 02:46:44Z) and the ONE
ad-hoc derive on `globgrph-derive-runner:9` started after this close are the TEST.
