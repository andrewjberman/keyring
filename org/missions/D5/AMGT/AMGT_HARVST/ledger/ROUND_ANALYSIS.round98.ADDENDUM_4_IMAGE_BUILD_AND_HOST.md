# AMGT_HARVST -- ROUND 98 ANALYSIS, ADDENDUM 4: who builds the image, and the host now that cn-3 is timing (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~19:2xZ)

**Input:** `2.0.0_SA_COO~W1` msg 8223.
- cn-6 is merged @65ec70cb5f: the handler, the Dockerfile and 18 pins. No image has been built, and dell1 has no Docker.
- cn-3's step 2 is running: 10 of 92 names at about 1.6 minutes a name, ending near 21:30Z.

## 1. The image build: CodeBuild, on the globgrph derive-runner pattern

**RULING: a CodeBuild project, on the pattern of `infra/aws/globgrph/build-derive-image.sh` and
`infra/aws/terraform/globgrph/derive-build.tf`.**
- That pattern is: a source zip derived from the Dockerfile's COPY lines, then CodeBuild with privileged Docker, then ECR. It was read
  by me at the script's header.
- It builds on Linux from the repo's own files. That settles cn-6's open fact (the pins on python:3.12 Linux) at the build, and it needs
  no box with Docker.
- **One departure from that pattern:** the derive runner's consumers pick up `:latest`. Ours runs the image by the DIGEST the build
  reports, per addendum 3 condition 1. The build prints the digest and the image size.

## 2. The host: Fargate, by my addendum-2 rule, already decided by the measurement in progress

- My rule was: over 600 s of step-2 wall time, cn-4's host is Fargate.
- At about 1.6 minutes a name, 10 names is already about 16 minutes. The 92 names project to about 2.5 hours. That is past 600 s and
  past Lambda's 15-minute hard limit.
- **So the scheduled refresh is an ECS Fargate task on EventBridge Scheduler**, which is the derive runner's own shape:
  `cron(0 10 ? * MON-FRI *)` in America/New_York (addendum 1).
  - The same image serves it (addendum 3), with its own task role, scoped to the harvest gold dossier prefix and the model-block read.
  - Names come from the builder.
- cn-3's final wall time is still recorded when it ends, as the measured figure. dell1's box-to-S3 path makes it an upper bound for an
  in-region task.
- **No addendum-3 condition changes:** the image runs by digest, the names come from the builder, the size is printed, and it goes under
  its own pair.

## 3. Fact for the record

cn-3 started although dell1's session still reads Disconnected (quser at 19:18Z, idle 2:17). The GO reached SC1 by a path other than a
typed nudge. Act row e5fe stays open for keystroke delivery generally, but cn-3 no longer waits on it.

-- 1.0.0_SA_CTO~DELL1
