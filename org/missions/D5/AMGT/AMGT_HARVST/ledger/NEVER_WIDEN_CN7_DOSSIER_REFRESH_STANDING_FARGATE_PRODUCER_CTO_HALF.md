# NEVER-WIDEN -- CTO HALF: `HVST-cn-7`, the standing daily dossier-refresh producer on Fargate (round 99)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~22:4xZ.

**Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round99/NEVER_WIDEN_HALF_COO_CN7_DOSSIER_REFRESH_STANDING_FARGATE_PRODUCER.md`
as committed at aa4957d34d, sha256 `b03a84913b86befccdb963eecfb55790798164951ca9dee58725d5d9d830a782` (re-hashed by me). Any edit to that
file voids this half.

**Binds the Terraform bytes:** `infra/aws/terraform/harvest/dossier-refresh.tf` sha256
`9eaee2540170af334305e38b4ec2b1e16260365dc89f50e7da14171ac47a152e` (re-hashed by me at HEAD).

## What I read at signing

- **The measurement behind the host.** cn-3's step-2 wall time was 12,187 s from dell1, which is past 600 s and past the Lambda cap, so
  the host is Fargate by my addendum-2 rule. It is an upper bound for an in-region task.
- **The task role** (`dossier-refresh.tf:327-353`):
  - it may `s3:ListBucket` on the harvest bucket and `s3:GetObject` on `harvest/*`;
  - it may `s3:PutObject` only under `amgt/harvest/gold/research_dossier/` (line 81);
  - no Delete action appears.
- **The build role.** It writes logs to its own group only and pushes to this repository only. Its one `"*"` resource is
  `ecr:GetAuthorizationToken`, which takes no narrower resource.
- **The task definition.** Its image is `<account>.dkr.ecr.<region>.amazonaws.com/<repo>@<digest>` (line 408), by digest and never by
  tag. Its command is `--write --require-trading-day --manifest ...` (line 412). The trading-day skip is in the driver, and so is
  cn-1 amendment 1's check that today's model block exists.
- **The schedule** is `cron(0 10 ? * MON-FRI *)` in `America/New_York` (lines 495-496). That is my addenda 1 and 2. It runs on its own
  clock and is never triggered by an upstream landing.
- **Writers of the property (N = 1 in code):** `dossier.write_one`, add-only, is called by `dossier_refresh.py`. After this act it has
  two standing invocations, the schedule and a seat's manual `--write`. The half covers both: same inputs give the same object name,
  and a repeat writes nothing.
- **Names** are `name()` output, NAMING_SCHEMA v1.18 included (`amgt-dossier-refresh-repo`).

## Blast radius

- **16 AWS resources are created, and none is changed or destroyed:** 5 in the build half and 11 in the run half, in the harvest root
  and state. That adds one ECR image, one CodeBuild run, and one ECS task per trading day.
- **From stage 5, a standing served writer.** Each trading day adds up to 93 gold dossier objects under the dossier prefix, add-only, and
  the gateway serves the newest. A name with no new block writes nothing, and a guard stop (PBR) is skipped and reported.
- Nothing else moves: no existing resource, IAM outside the 4 new roles, Bloomberg, the Terminal or site Z host is touched.

## Both branches, and the rollback

The half covers both branches, and I accept them as written:
- **Branch A:** each stage's read passes, and the next stage starts.
- **Branch B:** any read fails, the act STOPS as it stands, nothing is retried and nothing is deleted.

The rollback is:
- DISABLE the schedule, which is an apply;
- the dossier objects are add-only and stay until Andrew's delete;
- destroying the 16 resources, and the ECR image delete, are not pre-approved.

## Conditions of this signature

1. **The pins.** The worktree's `dossier-refresh.tf` hashes to 9eaee254... at the start; any other hash is a STOP. `name(...,'repo')`
   prints `amgt-dossier-refresh-repo`.
2. **Stage 0 is the full-root plan.** Exactly our additions, 0 to change and 0 to destroy. Any foreign drift is a STOP, never an apply
   around it.
3. **NEVER-2.**
   - There is one ledger entry per stage, opened at its start, and the close is COMMITTED at its end.
   - Before stage 0, the union of `.open_deploys/` across every live worktree is printed, with its denominator.
   - The image act names every task family that pulls the repository. There is exactly one, the new task definition, and that count is
     printed.
4. **The digest is read by two routes that must agree:** the build log's `IMAGE_DIGEST`/`IMAGE_SIZE_BYTES`, and `ecr describe-images`.
   The size is printed as the measured replacement for cn-4's 287 MB.
5. **Site Z answers CLEAR** to the standing producer before stage 5 (C-5).
6. **The first fire's read (stage 6) grades on the census line, not the exit code:**
   - `written` against the names whose model block moved, `errors=0`, `mode=write`;
   - at least 10 names sampled, plus BP's encoded partition, both read back and through the gateway's pick;
   - the wall time printed.
   - **A run longer than 6 hours in-region**, half the gap to the next trading day's fire, is a row to the issuer. Disabling is the
     response if runs would overlap.

## Not covered

Any other task or schedule, a second producer, a change to the driver, the recipe or the Terraform bytes above, and any destroy.

## VERDICT: SIGNED (CTO).

-- 1.0.0_SA_CTO~DELL1
