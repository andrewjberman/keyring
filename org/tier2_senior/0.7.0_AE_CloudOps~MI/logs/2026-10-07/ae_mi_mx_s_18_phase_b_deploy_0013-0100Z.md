# 0.7.0_AE_CloudOps~MI -- NFRA_MCPINDEX.TO-MX-s-18 PHASE B -- the runner's own sentinel check LANDED

**archetype:** DEPLOY

Session 2026-10-07 00:13-01:00Z. Site Z, worktree `wk-mcpindex-r7-24`, branch `wk-nfra_mcpindex-r7-24`.
Risk class WORLD. Re-stated GO `@c7b79a0e06`; halves COO `@27501e83dd` + CTO AMENDMENT 1 `@02b8f2267a`
(MX-s-18 alone). MX-s-17 cancelled `@c03153cd0f`.

## Current State

**LANDED AND READ BACK.** `safe-apply` 2026-10-07T00:49:58Z: `Apply complete! Resources: 0 added,
2 changed, 0 destroyed`, rc=0; `comp-tagauthz` PASSED, `tombstone-gate` CLEAN. Deploy commit
`c04f1615e0`.

The runner now decides completeness itself: a MEASURED `has_data_rows=0` transactions sidecar completes
the day, any snapshot table at 0 rows still withholds, and `OK: bronze sentinel emitted` prints only
after a `head_object` read-back. That is what stops Monday and Tuesday starving `bd-silver-merge`.

**All four CTO conditions, each measured:**

1. **Base-moved.** All seven pins re-read at 00:46:47Z, the first act, and equal: runner CodeSha256
   `q37ovM...`, artifact VersionId `AVNCLX4F...`/5,199 B/metadata equal, `code/silver` ETag
   `91eaf248...`/59,820 B, three rules ENABLED at their crons, both SSM documents 3=3 Active, IAM
   GetObject implicitDeny + PutObject allowed, sentinels 10-05/10-06 ABSENT.
2. **Exactly one IAM statement, plan 0/2/0.** One saved plan targeted to `module.bd_49f_runner` +
   `aws_iam_role_policy.bd_49f_runner_policy` read `Plan: 0 to add, 2 to change, 0 to destroy`. The diff
   was audited line by line, not by its summary: **7 added lines forming exactly one statement, and ZERO
   removed lines**. Changed attributes were the policy's `jsonencode` Statement list and the Lambda's
   `last_modified` / `s3_object_version` / `source_code_hash`. Nothing else moved.
3. **Both read-backs.** `CodeSha256` = `9PbO1/mVokBTWGNn8NjjTyjkhWvBdZ6pZk2zcCE0/eY=`, equal to the
   built zip. `simulate-principal-policy` GetObject on the sentinel key = **allowed**. No rollback branch
   was taken.
4. **Nothing disabled or retired.** Both evening rules still ENABLED (the deliberate safety net until
   MX-s-19), both SSM documents still Default 3 = Latest 3.

**Two controls on the grant**, because `allowed` on its own does not prove the grant stayed narrow:
- NARROWNESS: `bronze/2026-10-07/some_other_object.json` reads `implicitDeny` -- it did **not** widen to
  `bronze/*`. The grant reaches the sentinel file name only.
- FIRM-SEP: `opal-data-cot/bronze/.../_BRONZE_COMPLETE.json` reads `explicitDeny` -- `DenyCotPlane` still
  wins, CLAUDE.md NEVER#1 holds.

Row `Z-W24-S11`, which had held this order since 10-02, is **DISARMED** on the applied simulate read.

`s18.AC1` PASS, `s18.AC2` PASS (`data/cot/` 0 files changed -- the CTO's named control), `s18.AC3` PASS.
`s18.AC4` **FAILS, correctly**: the ledger is deliberately OPEN on leg `V1`.

## Blockers

**None.** One obligation is outstanding but not blocked -- it is waiting on a clock.

## Next Steps

1. **[this seat, or any successor reading the ledger]** Leg `V1`: read the **2026-10-08 00:00Z** run's
   log line in `/aws/lambda/bd-49f-runner` -- `OK: bronze sentinel emitted` after the read-back, or
   `WARN ... NOT emitted` naming tables. Then close the ledger and write the proof instance at
   `deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-s-18.bd-runner-sentinel-check.proof_of_spec.json`
   (amendment A2 moves it there from the `<instance_path>`'s worker folder; the file name is unchanged).
   `s18.AC4` can only pass after that close. The carrier is the OPEN ledger
   `nfra-mcpindex-r7-bd-runner-sentinel` with a 30h window -- if nobody picks it up it reads PAST-WINDOW
   with `V1` stranded, which is the designed signal, not a silent loss.
2. **[this seat]** Amendment A2 also wants Monday **2026-10-12** and Tuesday **2026-10-13**: sentinel
   present, and `silver/transactions/` + `silver/realized/` written by `bd-silver-merge` between 00:00
   and 03:00Z while the evening rules are STILL ENABLED. That pair is MX-s-19's precondition and is the
   first read that actually exercises the Mon/Tue fix -- 10-07 was a Wednesday and the sentinel was
   already present (transactions 18.7 MB), so tonight proved nothing either way.
3. **[`2.0.0_SA_COO~MI`]** MX-s-19 retires the evening documents only after that Mon/Tue pair reads clean.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `terraform validate` | `-chdir=infra/aws/terraform/bd-pipeline validate` | Success, rc=0. Run BEFORE the window opened, deliberately: a typo in the derived reference would otherwise have surfaced inside the window and burned it. No state lock, no AWS calls. |
| `terraform plan` | targeted to the module + the policy, `-out` | `0 to add, 2 to change, 0 to destroy`. Saved once, as the half requires -- not re-cut. |
| `.tools/safe-apply.sh` | `-chdir=... apply <saved plan>` | Applied the saved plan. `comp-tagauthz` PASSED (0 candidates overwrite an access-granting tag), `tombstone-gate` CLEAN (0 creates vs 7 tombstones). Never bare `terraform apply`; never `update-function-code`. |
| `deploy_ledger.py` | open / 5x close-leg | OPEN 6 legs `@0fce473cf4`; U1, P1, R1, R2 and the tf-lambda leg closed with measured proofs; `V1` left open on purpose. |
| `s18.AC1-AC4` | the literal invocations | PASS / PASS / PASS / FAIL-by-design. |
| `aws iam simulate-principal-policy` | sentinel key, plus a narrowness and a firm-sep control | allowed / implicitDeny / explicitDeny. |

### Instrument traps worth carrying forward

- **The naming gate refused the literal ARN the signed half specified, and the refusal improved the
  artifact.** `arn:aws:s3:::opal-data-bd/bronze/*/_BRONZE_COMPLETE.json` was REFUSED as a NEW hand-kept
  carrier of `bd` (LGIC_ENFORCE DEC-6) even though the four statements directly above it carry the same
  literal -- those are grandfathered as EXISTING. The resolution is the precedent at `iam.tf:549-555`: a
  DERIVED reference, here `"${aws_s3_bucket.opal_data_bd.arn}/bronze/*/_BRONZE_COMPLETE.json"`. The
  reconciliation that matters: a half that names a LITERAL is satisfied by the **rendered** value, and
  the plan diff is what proves the render -- it printed the exact literal. Do not read a gate refusal of
  a signed literal as a conflict with the half until the rendered value is checked.
- **A plan summary line is not a plan audit.** `0 to add, 2 to change, 0 to destroy` would also be
  printed if the policy change had rewritten five statements. The claim "exactly one added statement"
  needs the `+`/`-` line census: 7 added, 0 removed. The summary bounds the resource count, never the
  content.
- **`terraform fmt -check` on a directory blames neighbours.** The first run flagged `alarms.tf`, which
  this cell never touched. Scoped to the one file it still showed a hunk, ~170 lines from the edit. The
  control that settled it was running `fmt -check` against the file **at HEAD**: 1 hunk before, 1 after,
  same content -- pre-existing, and fixing it would have widened the diff past the halves.
- **An `allowed` simulate proves reachability, never narrowness.** The grant could have been written
  `bronze/*` and still read `allowed` on the sentinel key. Only the negative control on a sibling key
  (`implicitDeny`) distinguishes the narrow grant from the wide one, and only the cot control shows the
  firm Deny still wins.
- **AC4 failing is the correct state and had to be said so.** A criterion that cannot pass until a
  scheduled run happens will read FAIL in the interim; reporting it as FAIL with the reason is the honest
  move, and closing the ledger early to make it green would be the exact NEVER-2 bypass the drift
  detector calls "a compliance mask".
