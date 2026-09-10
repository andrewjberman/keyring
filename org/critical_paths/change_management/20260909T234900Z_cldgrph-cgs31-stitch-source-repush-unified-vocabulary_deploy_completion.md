# NEVER-2 deploy ledger -- stitch-source re-push, UNIFIED VOCABULARY (s3://opal-313476888478-globgrph/stitch-source/source.zip)

**Status:** CLOSED
**Opened (UTC):** 2026-09-09T23:49:00Z
**Owner:** `0.9.0_WK_NFRA_CLDGRPH~2` (spine-v3 L7 worker of `2.0.0_SA_COO~A`)
**Order:** `NFRA_CLDGRPH.TO-CG-F-11` (cell CG-s-31, PRD v0.13 row S31), deliverable step 3,
under the CTO gate GO 20260909T2305Z on row W2-S60
**Branch / HEAD at open:** `wk-cldgrph-6-2` @ `22e388d2213eef4cb815b1230855590af0a893c5` (LOCAL, never pushed)

## THE ACT -- exactly one object

`aws s3 cp .scratch/f11/source_gate.zip s3://opal-313476888478-globgrph/stitch-source/source.zip`

ONE S3 PutObject, the SECOND route of `.github/workflows/stitch-source-push.yml`
reproduced locally by
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f3_build_source_zip.py`
(CG-s-23's route, unchanged). Nothing else is written by this seat. The CodeBuild
project `opal-stitch-produce` writes `stitch/stitch_graph.json` and
`stitch/stitch_marker.json` under its OWN role; those are the build's acts.

## TASK FAMILIES THIS TOUCHES: **NONE**

A CodeBuild **source zip**, not a container image and not a task definition. No
image is built, no tag is moved. The NEVER-2 image clause has no members here and
the answer is stated rather than omitted: **zero task definitions reference this
object**; its only consumer is `opal-stitch-produce`
(`infra/aws/terraform/globgrph/stitch-produce.tf:150-152`).

## WHY

CG-s-31 unifies the stitch vocabulary AT THE PRODUCER: `extract_portal_stitch.py`
emits the projection's own type names and `derive_stitch.unify_stitch_vocabulary`
merges each member onto its canonical identity or carries it under the canonical
type with `origin=stitch`. The producer runs from THIS zip, so the unification
reaches the nightly only when the zip carries it.

The first attempt at this push was REFUSED BY THIS SEAT and not made
(row W2-S60): retiring the four provisional names drove their CERTIFIED
grain-baseline counts to 0 and AC-GRAIN.2 refuses on a zero, so the unified
producer could not publish and pushing the zip would have re-broken the producer
CG-s-23 had just repaired. The CTO's gate GO 20260909T2305Z recertified the nine
entries (four retired names to 0, five canonical classes at their first
post-unification magnitudes, one CVO sign pending on all nine), committed here at
`22e388d221`. The local run against the real snapshot then printed
`GRAIN-SENTINEL: PASS`, rc 0, with 0 of the four provisional names.

## THE OBJECT

| field | BEFORE (CG-s-23's zip, still served) | AFTER (this act) |
|---|---|---|
| LastModified | Wed, 09 Sep 2026 18:47:04 GMT | **Wed, 09 Sep 2026 23:49:34 GMT** |
| ContentLength | 181,338,655 B | 181,376,411 B (local) |
| ETag | `"b20d2d25b4a0851881d55e19af575367-22"` | **`"79e1d9b4e25ed076371701eb8a9a1141-22"`** |
| zip entries | 8,224 | 8,226 |
| `portal/src` files | 435 | 435 |
| `stitch_source_sha.txt` | `de590a7d0227fb9c14ce35b96dcec86deb68df60` | `22e388d2213eef4cb815b1230855590af0a893c5` |
| local sha256 | `06413e9a1ae5b46dde8f745bc9804a8c19243832dd0e4ac00212510e719ab913` | `7562583585165e2f74ae5113164f993eea021d0bcfdec8ef865c31250ce8979f` |

Portal layer: `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal` @
`5907cbca98eb091124e38a32debefa355c1d4376`, 435 tracked files under `src`. That
checkout moved during this round (row W2-S63); the head is recorded here so the
next comparison across cells is possible at all.

Content control on the zip BEFORE the act (read from the archive, not from the
filesystem): `infra/aws/globgrph/derive_stitch.py` carries
`_collapse_stitch_copies`; `org/modules/graph/grain_baseline.json` carries
GOLD_SCRIPT 0 / S3_DATA_KEY 0 / PORTAL_COMPONENT 0 / REACT_QUERY_KEY 0 /
PipelineScript 167 / PipelineFunction 1217 / S3Key 381 / Component 201 /
ReactQueryKey 125; `stitch_source_sha.txt` = `22e388d221...`.

## ROLLBACK

The bytes currently served are held at `.scratch/f3_push/source_new.zip` in this
worktree (181,338,655 B, sha256
`06413e9a1ae5b46dde8f745bc9804a8c19243832dd0e4ac00212510e719ab913`, the object
this key has served since 18:47:04Z), and the July original at
`.scratch/f3_source_asis/source_asis.zip`. Rolling back = `aws s3 cp` either file
back to the same key. No bucket versioning is read by this seat, so the local
copies ARE the rollback material and are named rather than assumed.

## WHAT THIS ENTRY DOES **NOT** DO

No `terraform apply`, no `.tf` change, no Lambda `update-function-code`, no rule
enabled or disabled, no alarm/monitor/notifier, no local Kuzu store. The 03:00Z
nightly stays the acceptance; the ONE ad-hoc build started after this entry closes
is the test, under the issuer's manual-trigger amendment (no waiting on a
scheduled fire).

---

## CLOSE

**Status at close:** CLOSED
**Closed (UTC):** 2026-09-09T23:49:40Z

**The act completed, measured on the SERVED object** (`s3api head-object`, UTC,
run AFTER the `cp` returned rc 0):

    LastModified   Wed, 09 Sep 2026 23:49:34 GMT
    ContentLength  181376411          (local build 181376411 -- equal)
    ETag           "79e1d9b4e25ed076371701eb8a9a1141-22"   (was "b20d2d25...-22")

    zip entries              8226   (was 8224)
    portal/src files          435   (unchanged; portal @ 5907cbca98)
    org/modules               427
    infra/aws                6242
    .tools                    399
    data/*/scripts/**/*.py    722
    stitch_source_sha.txt       1 = 22e388d2213eef4cb815b1230855590af0a893c5

NOT HALF-LANDED: the key held exactly one object before this act and exactly one
after; there is no second key, no tag, no task definition and no in-flight
consumer that could observe a partial state. The one downstream consumer
(`opal-stitch-produce`) reads the key only when a build starts, and the ONE
ad-hoc build this order runs was started AFTER this close.
