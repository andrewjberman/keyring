# NEVER-2 deploy ledger -- CG-s-31 SECOND CYCLE: the stitch source re-push AND the derive-runner image act (seven families re-pinned by digest)

**Status:** CLOSED
**Opened (UTC):** 2026-09-10T01:15:00Z
**Owner:** `0.9.0_WK_NFRA_CLDGRPH~2` (spine-v3 L7 worker of `2.0.0_SA_COO~A`)
**Order:** `NFRA_CLDGRPH.TO-CG-F-11` (cell CG-s-31), SECOND CYCLE ruled @`d5d7d8b6aa` (row
W2-S68) and the IMAGE ACT GO @`f3b17ade51` (row W2-S67; the never-widen sign is BOTH halves --
`2.0.0_SA_COO~A` 94807 and `1.0.0_SA_CTO` 94809)
**Branch / HEAD at open:** `wk-cldgrph-6-2` @ `b6c92e317433e4282644ec6e955589c064053a7a` (LOCAL, never pushed)

## THE TWO ACTS THIS ENTRY COVERS

**ACT 1 -- the CodeBuild source zip** (`s3://opal-313476888478-globgrph/stitch-source/source.zip`),
carrying the STORED_IN identity fix. ONE PutObject. **Task families touched: NONE** -- a source
zip is not an image and no task definition references it; its only consumer is the CodeBuild
project `opal-stitch-produce`.

**ACT 2 -- the derive-runner IMAGE and the seven-family digest re-pin.** The image is rebuilt
from HEAD's `derive_runner.py`, whose only change on the served plane is the stamp retirement
(F11-AC4: `STAMP_WRITTEN_BY_FOLD=false`), and the SEVEN globgrph task families that pull it are
re-pinned BY DIGEST (R13 -- never a mutable tag). This is the act the never-widen sign covers
and no wider: a second props change, a family missing from this entry, or a pin by tag is
OUTSIDE it.

## THE SEVEN TASK FAMILIES, BY TRUE NAME, WITH THE DIGEST BEFORE

Read live with `describe-task-definition` per family before the act (the census is the read, not
the Terraform file). All seven pull
`313476888478.dkr.ecr.us-east-1.amazonaws.com/opal-globgrph-derive-runner@<digest>`:

| # | task family (TRUE name) | rev BEFORE -> AFTER | digest BEFORE | digest AFTER | launcher |
|---|---|---|---|---|---|
| 1 | `globgrph-derive-runner` | 8 -> 9 | `sha256:478d0a43...` | `sha256:17ccc9b0...` | EventBridge rule opal-globgrph-derive-runner-nightly, cron(0 2 * * ? *) |
| 2 | `globgrph-cse-producer` | 3 -> 4 | `sha256:478d0a43...` | `sha256:17ccc9b0...` | EventBridge Scheduler globgrph-cse-producer-nightly, cron(30 3 * * ? *) |
| 3 | `globgrph-comp-learns-producer` | 3 -> 4 | `sha256:478d0a43...` | `sha256:17ccc9b0...` | EventBridge rule opal-globgrph-comp-learns-producer-nightly, cron(0 4 * * ? *) |
| 4 | `globgrph-fedobs-producer` | 3 -> 4 | `sha256:478d0a43...` | `sha256:17ccc9b0...` | EventBridge rule opal-globgrph-fedobs-producer-nightly, cron(30 4 * * ? *) |
| 5 | `globgrph-resource-summaries-producer` | 3 -> 4 | `sha256:478d0a43...` | `sha256:17ccc9b0...` | NONE declared -- hand-run ecs run-task (row W1-S28) |
| 6 | `globgrph-projection-worker` | 5 -> 6 | `sha256:478d0a43...` | `sha256:17ccc9b0...` | EventBridge Pipe opal-globgrph-projection-worker (Nessie branch-head write) |
| 7 | `globgrph-serving` | 3 -> 4 | `sha256:478d0a43...` | `sha256:17ccc9b0...` | ECS service aws_ecs_service.globgrph_serving (always-on) |

**7 of 7 on the new digest, 0 of 7 on the old, 0 of 7 on ANY tag** -- read live with
`describe-task-definition` AFTER the apply, not from the plan and not from the .tf.
`globgrph-nessie` and `globgrph-trino` are the other two ACTIVE families in the account
and pull other images entirely: 9 active, 7 in this population, named rather than omitted.
The census output is captured verbatim at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f11_families_before.json`
and, after the act, `f11_families_after.json`.

## WHY

* ACT 1: W2-S68 -- the STORED_IN boundary edge named `arn:aws:s3:::<bucket>` while the
  S3_BUCKET node id is the bucket name, so 0 of 955 edges resolved and none has ever reached the
  served graph (measured identical on the pre-unification artifact). Fixed at
  `derive_stitch._index_aws`; local proof on the real snapshot: **STORED_IN both-ends-present
  955 of 955**, DERIVES_FROM 216 of 216, reconciliation unchanged (1790 = 1521 + 269, lost 0),
  `GRAIN-SENTINEL: PASS`, the five canonical magnitudes unchanged.
* ACT 2: W2-S67 -- the `vocabulary=stitch-v1` stamp is retired in the code at HEAD and still
  written by the DEPLOYED image `globgrph-derive-runner:8` (digest `sha256:478d0a43...`), which
  stamped one node (`PORTAL_BUNDLE` `portal`) in the 23:57Z derive. Only a new image retires it
  on the served plane.

## ROLLBACK

* ACT 1: the bytes served before this act are held at `.scratch/f11/source_gate.zip` in this
  worktree (181,376,411 B, sha256
  `7562583585165e2f74ae5113164f993eea021d0bcfdec8ef865c31250ce8979f`, ETag
  `"79e1d9b4e25ed076371701eb8a9a1141-22"`, served since 23:49:34Z). `aws s3 cp` it back.
* ACT 2: re-pin `local.globgrph_image_digest` in
  `infra/aws/terraform/globgrph/serving.tf` to the PREVIOUS digest, named in the close below,
  and `safe-apply` the same address set. The ECR tag is NOT moved by this act, so no rollback is
  needed there -- the digest the seven families pulled before this act remains addressable.

## WHAT THIS ENTRY DOES **NOT** DO

No Lambda `update-function-code`, no rule enabled or disabled, no alarm/monitor/notifier, no
local Kuzu store, no schema change, no props change beyond the stamp retirement the sign names.
The 02:00Z rule fire stays the CONFIRMATION; the ONE ad-hoc derive on the new digest is the TEST.

---

## CLOSE

**Status at close:** CLOSED
**Closed (UTC):** 2026-09-10T01:16:30Z

### ACT 1 -- the source zip, measured on the SERVED object after the `cp` returned rc 0

    LastModified   Thu, 10 Sep 2026 01:04:38 GMT
    ContentLength  181377230          (local build 181377230 -- equal)
    ETag           "81f1fad5c4bbf4a5c81415ba37d0398f-22"   (was "79e1d9b4...-22")
    zip entries    8226 ; portal/src 435 ; stitch_source_sha.txt = b6c92e317433e4282644ec6e955589c064053a7a
    local sha256   6f5130c76f02f04d934a5f180f41b3c6f98d782edeba5a7b8c16e87b8016ff8a

The ONE ad-hoc build `opal-stitch-produce:ce8aaaa3-c8aa-4afb-8df3-758082c1924a` SUCCEEDED and
its marker reads `producer=stitch-codebuild built_at=2026-09-10T01:06:24Z
git_sha=b6c92e317433e4282644ec6e955589c064053a7a total_nodes=27745 total_edges=61304` --
the local run's figures to the unit.

### ACT 2 -- the image and the re-pin

    CodeBuild        globgrph-derive-build:9bb38966-d818-4da7-bb71-977367518247  SUCCEEDED
    source commit    b6c92e317433e4282644ec6e955589c064053a7a (HEAD; the zip is DERIVED from
                     the Dockerfile's COPY lines, 37 entries, never a static list)
    ECR :latest      BEFORE sha256:478d0a43...  ->  AFTER sha256:17ccc9b0...
                     new tags 20260910-010924 + latest, pushed 2026-09-10T01:09:39Z
    the tag MOVED and NOTHING PULLS IT: 0 of 7 families reference a tag (R13 working).
    pin              infra/aws/terraform/globgrph/serving.tf local.globgrph_image_digest,
                     478d0a43... -> 17ccc9b0..., its comment re-stated for the new image
    apply            bash .tools/safe-apply.sh -chdir=infra/aws/terraform/globgrph apply
                     -auto-approve with EIGHTEEN -target flags; rc 0;
                     "Apply complete! Resources: 7 added, 11 changed, 7 destroyed."
    NOT applied      4 FOREIGN addresses left exactly as found, censused from an UNSCOPED plan
                     that was never applied: aws_glue_partition.tool_activity["rolling_log"],
                     ["rolling_log_summary"], ["routing"], and
                     aws_sns_topic_subscription.critical_surface_alerts_email -- the last is an
                     alert destination the C3 moratorium forbids this order to land, and an
                     unscoped apply would have created it (the same finding as row W2-S52).

**ROLLBACK, named and still addressable:** re-pin `local.globgrph_image_digest` to
`sha256:478d0a43742b2ed5a44631c6352b5713c5ba22f015d82a673cfb93428a9dae20` (in ECR under tag
`20260909-203936`) and re-run the same eighteen-address apply.

NOT HALF-LANDED: all seven families read the new digest and none reads a tag, measured after the
apply by `describe-task-definition` (`f11_families_after.json`). The ONE ad-hoc derive on
`globgrph-derive-runner:9` started after this close is the TEST for both W2-S67 and W2-S68; the
02:00Z rule fire is the confirmation, never a gate.
