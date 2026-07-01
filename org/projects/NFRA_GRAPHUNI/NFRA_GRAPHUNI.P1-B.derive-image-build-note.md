# NFRA_GRAPHUNI P1-B — globgrph derive-image build note (canonical source-zip coupling)

**Author:** 0.8.0_AE_CloudComp~B | 2026-07-01 | surfaced during the P1 population re-drive (my first re-build `e900acd0` FAILED on this exact coupling).
**For:** whoever rebuilds `opal-globgrph-derive-runner:latest` via the `globgrph-derive-build` CodeBuild. Authoritative homing = the globgrph owner (~D / 0.7.0) in `infra/aws/globgrph`; this is the ~B-lane record + the recommended durable fix.

## The coupling (now permanent)
`globgrph-derive-build` builds from an **S3 source zip** (`s3://opal-313476888478-globgrph/build-source/derive-runner-source.zip`) — NOT a git webhook. The buildspec runs `docker build -f infra/aws/globgrph/Dockerfile .` with context = the zip root, so the zip MUST contain every file the Dockerfile `COPY`s (repo-root-relative), or the docker build fails on the missing COPY target.

`~E`'s COMPLEARN P3 commit `15bc9ea12` added 2 `COPY` lines to the Dockerfile (`comp_learns_produce.py` + `comp_learns_views.sql`). Since that is on CLOUD, **every derive-image build from now on requires those 2 files in the zip.** My first re-build (a 7-file zip predating `15bc9ea12`) failed the docker COPY; my 9-file zip (`0958b055`) fixed it + shipped clean. Fail-SAFE (a missing file fails the build loudly; never ships a broken image), so not a corruption risk — but the canonical source set changed.

## The canonical source set (as of 2026-07-01, commit `200e3de35`+`15bc9ea12`)
The zip must contain exactly what `infra/aws/globgrph/Dockerfile` `COPY`s + the Dockerfile + buildspec:
1. `org/modules/graph/comp_aws_cli.py`
2. `org/modules/graph/surface_check_cli.py`
3. `org/modules/graph/critical-surfaces.yaml`
4. `infra/aws/globgrph/derive_runner.py`
5. `infra/aws/globgrph/ms_cloud_extract.py`
6. `infra/aws/globgrph/comp_learns_produce.py`   *(~E P3, inert to derive_runner, Dockerfile-required)*
7. `infra/aws/globgrph/comp_learns_views.sql`    *(~E P3, inert to derive_runner, Dockerfile-required)*
8. `infra/aws/globgrph/Dockerfile`
9. `infra/aws/globgrph/buildspec.yml`

## The DURABLE fix (recommended — do NOT hard-code a static file list)
A static N-file list goes stale the next time anyone edits the Dockerfile's COPY lines (exactly what bit me). The robust zip-builder DERIVES the file set from the Dockerfile itself:
```
# parse the Dockerfile's COPY sources (repo-root-relative), + the Dockerfile + buildspec, into the zip
COPY_SRCS=$(grep -E '^COPY ' infra/aws/globgrph/Dockerfile | awk '{print $2}')
zip-set = COPY_SRCS + [infra/aws/globgrph/Dockerfile, infra/aws/globgrph/buildspec.yml]
# then: zip (repo-root arcnames) -> aws s3 cp -> aws codebuild start-build --project-name globgrph-derive-build
```
This auto-syncs with any future Dockerfile COPY change — no dropped-file COPY-fail class. Recommend homing this as `infra/aws/globgrph/build-derive-image.sh` (owner grant).

## Deploy sequence (proven, this re-drive)
zip (9-file / Dockerfile-derived) -> `aws s3 cp .../build-source/derive-runner-source.zip` -> `aws codebuild start-build --project-name globgrph-derive-build` -> build SUCCEEDED (pushes `:latest`) -> `aws ecs run-task` globgrph-derive-runner:4 (default CMD = full derive + `ingest_graphuni_producers()`). The population run uses NO command override; only surgical modes (`--sign-baseline`) need `["python","/app/derive_runner.py","--flag"]` (containerOverrides.command REPLACES the image CMD wholesale).

*Routed to ~D + 0.7.0 to home the authoritative build helper + note in infra/aws/globgrph (their grant). This ~B note records the coupling + the durable fix from the re-drive that surfaced it.*
