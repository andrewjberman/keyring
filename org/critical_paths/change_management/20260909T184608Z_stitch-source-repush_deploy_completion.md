# NEVER-2 deploy ledger -- stitch-source re-push (s3://opal-313476888478-globgrph/stitch-source/source.zip)

**Status:** CLOSED
**Opened (UTC):** 2026-09-09T18:46:08Z
**Owner:** `0.9.0_WK_NFRA_CLDGRPH~2` (spine-v3 L7 worker of `2.0.0_SA_COO~A`)
**Order:** `NFRA_CLDGRPH.TO-CG-F-3` (cell CG-s-23, PRD v0.6 row S23), deliverable step 3
**Branch / HEAD at open:** `wk-cldgrph-6-2` @ `de590a7d0227fb9c14ce35b96dcec86deb68df60` (LOCAL, never pushed)

## THE ACT -- exactly one object

`aws s3 cp <local zip> s3://opal-313476888478-globgrph/stitch-source/source.zip`

ONE S3 PutObject. Nothing else is written by this seat. The CodeBuild project
`opal-stitch-produce` that consumes this key writes two further objects under its
OWN role (`stitch/stitch_graph.json`, `stitch/stitch_marker.json`,
`infra/aws/terraform/globgrph/stitch-produce.tf:100-123`); those are the build's
acts, not this entry's.

## TASK FAMILIES THIS TOUCHES: **NONE**

This is a CodeBuild **source zip**, not a container image and not a task
definition. No image is built, no tag is moved, no ECS/Fargate task family pulls
anything as a result. The CLAUDE.md NEVER-2 image clause ("an IMAGE act names in
that entry EVERY task family that pulls the tag it moves") therefore has no
members here, and the answer is stated rather than omitted: **zero task
definitions reference this object**; its only consumer is the CodeBuild project
`opal-stitch-produce` (S3 source location
`opal-313476888478-globgrph/stitch-source/source.zip`,
`stitch-produce.tf:150-152`).

## WHY (the state being repaired)

`opal-stitch-produce` has FAILED 67 of 67 builds since 2026-07-07 on an ENABLED
nightly (`cron(0 3 * * ? *)`, rule `opal-stitch-produce-nightly`). The source zip
at that key was written ONCE, by the GH-Action `.github/workflows/stitch-source-push.yml`,
on 2026-07-07 13:46:19 GMT, and has never been refreshed: that Action's portal
checkout needs `secrets.PORTAL_REPO_PAT`, and the zip it published packed **0
files from `portal/src`** (measured: 7,905 entries, `portal/` prefix count 0).
The nightly's own CloudWatch log (build
`3a5b2473-f46a-490a-ae5e-874a96c90b16`, 2026-09-09T03:00Z) ends
`ERROR: GRAIN_SENTINEL_FAIL` / `exit status 2` with
`REACT_QUERY_KEY 0 vs 32`, `PORTAL_COMPONENT 0 vs 27`.

The Action is the FIRST route and fires only on a push to CLOUD, which is
`0.0.0_AB_MSTR`'s act on Andrew's word and not this worker's. This entry covers
the SECOND route the task order names: build the zip locally with the Action's
own recipe and `aws s3 cp` it.

## THE OBJECT

**Recipe** (`.github/workflows/stitch-source-push.yml:76-92`, reproduced by
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f3_build_source_zip.py`):
`portal/src` + `org/modules` + `infra/aws` + `.tools` + `stitch_source_sha.txt`
+ every `data/*/scripts/**/*.py`; excluded `*/node_modules/*`, `*/.terraform/*`,
`*/__pycache__/*`, `*.pyc`.

`portal/` is a bare gitlink here (mode 160000, no `.gitmodules`), so `portal/src`
is taken from the main workspace's portal checkout
`C:/Users/AndrewBerman/Desktop/ajb_workspace/portal` at
`18c0c5cb6a26c2c8e9fbfa168dadf04de4344705` (435 tracked files under `src`).
That checkout is NOT at this repo's gitlink `30ca034bbaa4b9d2864d3acce826e3c2fa59be0a`,
which is not even an object in it -- recorded as surprise row NFRA_CLDGRPH-W2-S40.

| field | BEFORE (the July object) | AFTER (this act) |
|---|---|---|
| LastModified | Tue, 07 Jul 2026 13:46:19 GMT | **Wed, 09 Sep 2026 18:47:04 GMT** |
| ContentLength | 156,995,002 B | **181,338,655 B** |
| ETag | `"5e8011947ede9e0e253dc3a64d36d479-19"` | **`"b20d2d25b4a0851881d55e19af575367-22"`** |
| zip entries | 7,905 | 8,224 |
| `portal/src` files | **0** | **435** |
| `stitch_source_sha.txt` | `81064fbcae6dbf440d516eee067554f6a192becd` | `de590a7d0227fb9c14ce35b96dcec86deb68df60` |
| local sha256 | -- | `06413e9a1ae5b46dde8f745bc9804a8c19243832dd0e4ac00212510e719ab913` |

## ROLLBACK

The July object's bytes are held at
`.scratch/f3_source_asis/source_asis.zip` in this worktree (156,995,002 B,
ETag `"5e8011947ede9e0e253dc3a64d36d479-19"`, pulled 2026-09-09T18:2xZ before the
act). Rolling back = `aws s3 cp` that file back to the same key. The bucket has
no versioning read by this seat, so the local copy IS the rollback material and
is named here rather than assumed.

## WHAT THIS ENTRY DOES **NOT** DO

No `terraform apply`, no `.tf` change, no Lambda `update-function-code`, no rule
disabled, no alarm/monitor/notifier, no local Kuzu store. The nightly at 03:00Z
stays the acceptance; the ad-hoc build started after this entry closes is the
test.

---

## CLOSE

**Status at close:** CLOSED
**Closed (UTC):** 2026-09-09T18:47:30Z

**The act completed, measured on the SERVED object** (`s3api head-object`, UTC,
run AFTER the `cp` returned rc 0 and quoted verbatim above):

    LastModified   Wed, 09 Sep 2026 18:47:04 GMT
    ContentLength  181338655
    ETag           "b20d2d25b4a0851881d55e19af575367-22"

    zip entries              8224   (was 7905)
    portal/src files          435   (was 0)          <- the July zero is the control
    org/modules               425
    infra/aws                6241
    .tools                    400
    data/*/scripts/**/*.py    722
    stitch_source_sha.txt       1 = de590a7d0227fb9c14ce35b96dcec86deb68df60

NOT HALF-LANDED: the key held exactly one object before this act and exactly one
after; there is no second key, no tag, no task definition and no in-flight
consumer that could observe a partial state. The one downstream consumer
(`opal-stitch-produce`) reads the key only when a build starts.

The ad-hoc build started after this close is recorded in the order's result file
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/CG-s-23.stitch-producer-repaired.result.md`,
not here: it is the build's own role that writes `stitch/*`, not this entry's act.
