# NEVER-WIDEN -- CTO HALF: `HVST-co-7`, the deliberate gold rebuild run on Fargate (round 100)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-20 ~21:5xZ.

**Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/staged/NEVER_WIDEN_HALF_COO_CO7_GOLD_REBUILD_DELIBERATE_RUN_DRAFT.md`
as committed at 751f30e87e, sha256 `f05b443bc4bfe87fca8a4d6a3889c1fe94788675b73ee491520601d17c3cd2a4` (re-hashed by me on disk and at
the pin; equal). The COO signs its half at these bytes and copies it into `ledger/`. Any edit to that file voids this half.

**Binds the Terraform bytes:** `infra/aws/terraform/harvest/gold-refresh.tf` sha256
`73e78ba97c3edc67a77b3cfcff116fdf04d7ce4b01adbe8311d56aaf4fee247b` (re-hashed by me at HEAD, last commit 2140a014d0b).

**Binds the ruling it runs under:** `XA-20261020T184817Z-72a8`, (a) Fargate, with its four conditions (dell1 copy
`org/tier1_exec/1.0.0_SA_CTO/deliverables/XADJ_72a8_RULED_COPY_20261020.md`).

## What I read at signing

- **The host.** The first table measured 2715 s from dell1 (about 1550 s in-region), past the 900 s Lambda cap, so Fargate under the
  ruling. The import closure is 207.34 MB and is not the binding limit.
- **The task role** (`gold-refresh.tf:343-372`): `s3:ListBucket` on the harvest bucket, `s3:GetObject` on `harvest/*`, and
  `s3:PutObject` only under the three gold prefixes (`WriteGoldPrefixesOnly`, line 366). No Delete action appears in the file (line 343
  says so, and my grep for `Delete` found none).
- **The task definition** (line 423) names the image by sha256 DIGEST, validated by regex (line 119), never a tag. Its command is
  `--write --require-trading-day` (line 427).
- **The schedule** is DISABLED by default (line 507) and is not this act: enabling it is its own addendum.
- **Writers of the property (N = 2 entry points, one rule).** `publication_gold.py::main` and `gold_refresh.py::main` both reach the
  same three `write_gold` calls (lines 1066, 1314, 1792), and `write_gold` (line 534) puts with `IfNoneMatch="*"` (line 552): add-only,
  a full snapshot per build. The expected outcome, read from that rule: three NEW objects, none changed or deleted. Both branches of
  the COO half rest on it.
- **Names** are `name()` output (`gold-refresh.tf:35-59`, thirteen names).
- **The run is deliberate, not scheduled:** a seat `--write` after the build and run halves are applied, as cn-7 was run.

## Blast radius

- **16 AWS resources are created and none changed or destroyed:** 5 in the build half and 11 in the run half, in the harvest root and
  state. That adds one ECR image, one CodeBuild run and one ECS task run.
- **Three gold objects are ADDED**, one per table, under `amgt/harvest/gold/{article_security_mention,chatter_daily,chatter_event}/`.
  Because the gateway's pick reads the newest snapshot, each lands in the served chatter figures at once. Nothing existing is changed.
- **Order holds the hazard:** mention, then daily, then event. A failure after the first write leaves an earlier table newer than a
  later one until a repeat run; Branch B names which objects exist and stops.
- Nothing else moves: no other table or prefix, no IAM outside the new roles, no schedule, Bloomberg, Terminal or site Z host.

## Rollback, per key

Each new object is addressed by its receipt key. Removing it returns the pick to the previous snapshot of that table. An S3 delete
needs Andrew's word, so if rollback is needed I card the three keys to him. Until then the previous snapshots stay in place and
unchanged (check A-4), so nothing is lost by waiting.

## Conditions on the seat (`0.7.0_AE_CloudOps~SC1`)

1. Every start condition (a) to (e) of the COO half reads true and is printed, (b) satisfied by the dell1 copy named above.
2. Each stage is its own ledger leg; the image digest and the run date are bound by addenda at the stage they become known, as cn-7's
   were, and I countersign each.
3. Site Z is told before the write, through `0.0.0_AB_MSTR~DELL1`.
4. No second `--write` run under this half. A repeat needs a new GO.

**VERDICT: SIGNED (CTO half).** The act may proceed once the COO half is signed at the bound bytes and on file beside this one.

-- 1.0.0_SA_CTO~DELL1
