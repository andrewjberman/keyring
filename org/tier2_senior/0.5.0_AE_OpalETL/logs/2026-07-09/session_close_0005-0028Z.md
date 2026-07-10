# Session Log -- 0.5.0_AE_OpalETL -- mdpf per-partner gate DEPLOY (close)
**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE
**window:** 2026-07-10T00:05Z -> 2026-07-10T00:28Z (since `session_2350-0005Z.md`, commit `3e632b043`)
**serial:** 0.5.0_AE_OpalETL (AE / OpalETL)

## Summary
Finished the mdpf per-partner freshness gate deploy in-session under Andrew-direct GO (CTO
`001053Z`), after 0.6.0's IAM BLOCK (`000837Z`) turned my own (C) roll-source fail-safe into a
silent forever-DEFER. Landed the IAM grant + exception-split + gate code as ONE safe-apply plan,
verified APPLIED + EXERCISED on live (not comp-iam, not my ledger), closed the deploy ledger 5/5,
tagged `mdpf-pipeline-v1.4.0`. COO independently re-verified in the deployed bytes and owns the
15:03Z outcome-verify. Standing down clean.

## What moved (3 commits, this window)
| Commit | What |
|---|---|
| `ed415e268` | `fix(mdpf gate)`: IAM `PlatinumRollSourceRead` (prefix-scoped `aggregate_aua/*`, GetObject only, no ListBucket) + `_roll_source_exists` exception-split (403 ROLL_SOURCE_UNREADABLE loud/config vs 404 ROLL_SOURCE_ABSENT data vs transient) -- closes 0.6.0 BLOCK `000837Z`. DEPLOY. |
| `08a2a614b` | `ci(mdpf-pipeline)`: mdpf-daily-trigger artifact upload, new content-sha256 (yang-lambda `source_code_hash`). |
| `ed67e1b02` | `ledger(...)`: deploy-completion ledger CLOSED 5/5. |

Per-file detail rides the commit messages above.

## Deployment Sequence (NEVER#6 -- open-at-start / close-at-completion)
1. `deploy_ledger` OPEN: `org/critical_paths/change_management/20260710T0013Z_mdpf-per-partner-gate-deploy_deploy_completion.md`
2. `commit-gate` (py_compile + ds-precommit + ruff) -> `safe-commit` -> push `ed415e268`
3. `safe-apply` ONE plan carrying IAM + Lambda -> **0 added / 2 changed / 0 destroyed**
4. 0-diff re-plan -> "No changes." ; `git tag -a mdpf-pipeline-v1.4.0` ; push `--follow-tags`
5. Verify APPLIED on live (below)
6. S3 upload dispatch + aggregate -> `comp-pipescript deployed` MATCH
7. Ledger CLOSED 5/5 (`ed67e1b02`)

## Verification (ACTUAL output -- APPLIED + EXERCISED, re-run this window post-compaction)
```
# APPLIED  -- aws iam get-role-policy mdpf-daily-trigger-lambda-role mdpf-trigger-scoped
  Sid=PlatinumRollSourceRead  Effect=Allow  Action=[s3:GetObject]
  Resource=arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/aggregate_aua/*
# EXERCISED -- aws iam simulate-principal-policy (against the ROLE, not agent creds)
  s3:GetObject  .../aggregate_aua/2026-07-06.json  ->  allowed        (was implicitDeny)
# LAMBDA   -- aws lambda get-function-configuration mdpf-daily-trigger
  CodeSha256 = Y5py4xQ3Ar4CoIy13LuGpt1gF0Oa1qQRS1jjFCKVzMU=          (was Cei1TsbP...)
# DEPLOYED -- comp-pipescript deployed (dispatch + aggregate)  ->  MATCH
```
Rule 22a satisfied on all three layers: DESIRED (iam.tf) != APPLIED (get-role-policy) != EXERCISED
(simulate). The third caught what comp-iam GREEN-lit -- it binds the action name, never the resource ARN.

## Compiler Tools
| Tool | Call | Result | Note |
|---|---|---|---|
| comp-tagauthz | safe-apply pre-apply gate (first production fire of my own gate) | PARTIAL->PASS | FAIL-CLOSED under `MSYS_NO_PATHCONV=1` (launcher `$WORKSPACE` not cygpath'd -> `python: can't open file 'C:\c\Users...'`); re-ran WITHOUT MSYS (apply had no ARN args) -> PASS clean. Denominator stated. |
| comp-pipescript | `deployed` (dispatch + aggregate) | MATCH | served bytes == source sha |
| comp-iam | (NOT consulted for the grant, by CTO order) | N/A | it reported this exact call `[GRANTED]` while live = implicitDeny; used `simulate-principal-policy` instead |

**What worked:** comp-pipescript deployed MATCH; comp-tagauthz fail-CLOSED correctly (safe direction).
**What failed:** comp-tagauthz launcher is fragile to `MSYS_NO_PATHCONV=1` -- fail-closes for the wrong
reason, indistinguishable red from a real authz DANGER.
**Gap found (routed to CTO, diff-before-land, NOT started):** MSYS leading-slash / path-arg mangling
silently defeated TWO independent verify instruments this session -- my safe-apply/comp-tagauthz gate
AND COO's `ssm get-parameter --name /mdpf/custody_source` control (query + control failed identically
-> false agreement). One class. CLAUDE.md fences this for `git push` + the aws launcher but NOT the
`.tools/` comp-launchers. Fix scope: harden every comp-tool launcher/verify path against MSYS
translation; COO's ssm case belongs in the same test matrix.

## Blockers
None open. 0.6.0's IAM BLOCK (`000837Z`) RESOLVED by `ed415e268` (grant added, simulate=allowed).
Prior reviewer blockers (A)+(B) were a dead path (custody_source=schwab), cleared in the last window.

## Current State (zero-context handoff)
- **Gate: DEPLOYED + live-verified 3 ways** (above). Lambda `mdpf-daily-trigger`
  CodeSha256=`Y5py4xQ3...`, LastModified `2026-07-10T00:17:02Z`. Env `GATE_ENFORCE=1`,
  `BD_MAX_LAG_TRADING_DAYS=2` (do NOT raise -- masks a real slip).
- **Behavior at tomorrow 15:03Z fire:** RPS 3 trading days behind (`behind=3 > max_lag=2`) ->
  `stale_partners=['49financial']` -> 49F skipped, its block ROLLS FORWARD from `2026-07-06` as a
  unit -> Inflection (spine) ADVANCES. The unconditional `if GATE_ENFORCE and not all_fresh: DEFER`
  is GONE from the deployed bytes (COO confirmed at `:521/:528/:534`).
- **Files (deployed):** `infra/aws/terraform/mdpf-pipeline/iam.tf` (`aws_iam_role_policy.mdpf_trigger_lambda`,
  +PlatinumRollSourceRead); `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py`
  (`_roll_source_exists` exception-split); `s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh`,
  `s3://opal-data-mdpf/code/scripts/gold/mdpf_aggregate_aua.py` (sha MATCH).
- **Ledger:** `...20260710T0013Z_mdpf-per-partner-gate-deploy...` CLOSED 5/5. Tag `mdpf-pipeline-v1.4.0` pushed.
- **HEAD:** `ed67e1b02` on CLOUD, pushed `--follow-tags`.

## Next Steps
- **[2.0.0_SA_COO]** OWNS the 15:03Z OUTCOME verify (`PENDING_mdpf_1503Z_inflection_advance_verify.md`,
  `ba9d219e2`): served-artifact read -- Inflection `as_of` must advance PAST `2026-07-08`; 49F freezes
  at `2026-07-06` (correct, not a compromise); do not read Sentinel-3 PASS as evidence the rolled 49F
  block is correct (coherent != correct); do not flip `/mdpf/custody_source`. NOT mine.
- **[1.0.0_SA_CTO]** owed the `.tools/` MSYS-hardening fix as a diff-before-land (comp-tagauthz launcher
  + the class linkage w/ COO's ssm case). NOT started -- fabric wound down for all but this deploy.
- **[0.6.0_AE_PartnerETL]** re-verifies post-apply (already has completion report `002140Z`).
- Standing down clean. `03_mappings/` untouched; zero 49F/Schwab/RPS code touched; no vendor calls.
