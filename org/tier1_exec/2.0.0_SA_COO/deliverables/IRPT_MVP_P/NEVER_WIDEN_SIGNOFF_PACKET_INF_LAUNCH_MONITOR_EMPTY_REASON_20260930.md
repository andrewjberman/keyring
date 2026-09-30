# Never-widen sign-off packet -- inf-ec2-launch-monitor: an EMPTY StateTransitionReason is never suppressed (TO-IB-pr-242 served; IRPT_BCKEND round 26 cell IB-pr-262)

Author `2.0.0_SA_COO~P`, 2026-09-30 ~15:4xZ. Ledger `inf-launch-monitor-empty-reason-served-20260930` (OPEN; entry committed by
the integrator @24fdc82554 with bytes unchanged, LD-0613 Progress 39). Halves owed: `1.0.0_SA_CTO` (ROUND-25 ~P ANALYSIS section 2,
row W86-S2: "this seat signs on read of the packet blob, and the packet names every task family that pulls the image or alias it
moves") and `2.0.0_SA_COO~P` (this seat, signed below on the same blob). No CRO half: no page, no served figure.

## 1. The act, exactly

ONE `safe-apply` of Terraform root `infra/aws/terraform/inf-pipeline` targeted to `module.inf_ec2_launch_monitor`, which re-points the
live function `inf-ec2-launch-monitor` at the artifact already uploaded to S3:

| property | BEFORE (live, read 13:2xZ) | AFTER (plan, read 15:1xZ) |
|---|---|---|
| CodeSha256 | `RdBNvM6I/9sgEQGenRFaOzJh2fzj6eV+K9AF/s+Eitk=` (LastModified 2026-09-21T19:43:08Z) | `t1QrzaDeMtjGgnFL0oez1DGtL6vLVz7fgV0/BMVuIQo=` |
| s3_object_version of `inf-pipeline/inf-ec2-launch-monitor.zip` | `Yl3wNNf7j9AKp00iYsA2hQ.aSo297Q9.` (2026-09-21T19:36:33Z, 3,686 bytes) | `tZB0hT8sgZKFhd2jd7iyD8cIXGu9kUQy` (2026-09-30T14:41:18Z, 3,817 bytes, metadata content-sha256 = the AFTER CodeSha256) |
| source | pre-pr-242 `lambda_function.py` | `lambda_function.py` @`1431d66d9b` (drain of WK~85; the `''` entry removed from `NORMAL_PATTERNS`, a comment naming the trap; `tests/test_lambda_function.py` 117 lines added) |
| plan | -- | `Plan: 0 to add, 1 to change, 0 to destroy` on `module.inf_ec2_launch_monitor.aws_lambda_function.this` ONLY (`last_modified`, `s3_object_version`, `source_code_hash`); `Warning: Resource targeting is in effect` |

Nothing else in the root moves: no IAM, no EventBridge rule, no environment variable, no retry Lambda. The build is
`infra/aws/lambda/ci/build-and-upload.sh inf-pipeline inf-ec2-launch-monitor` at HEAD f54e17e4c6 (tree clean under the Lambda dir at the
build gate); `lambda-source-map.json` carries the new `artifact_sha256` (this commit).

## 2. Every puller of what moves (the NEVER-2 census, one `describe`-class sweep)

The moved object is the S3 artifact key `inf-pipeline/inf-ec2-launch-monitor.zip`. Census of every `artifact_key` in the root
(`comp-find 'artifact_key *= *"inf-pipeline/' infra/aws/terraform/inf-pipeline`, 25 hits across 51 files): the key is named ONCE,
`inf-ec2-launch-monitor.tf:88`. Repo-wide census of the key (`comp-find 'inf-ec2-launch-monitor.zip' infra`, 29 hits across 12,189
files): the same `.tf`, `lambda-source-map.json` (the registry) and `CHANGELOG.json` (a record). So exactly ONE function pulls it:
`inf-ec2-launch-monitor`. `inf-ec2-retry-launch` has its own artifact (`inf-ec2-retry-launch.tf:138`) and does not move. No image, no
alias, no `:latest` tag is involved.

## 3. Blast radius, by branch (the producer's own rule, read at signing from `lambda_function.py` @1431d66d9b)

The function fires on EventBridge `stopped` events of four instances (`inf-exporter`, `inf-bronze-runner`, `inf-gold-layer-runner`,
`inf-gold-qa-runner`). Its decision tree is unchanged in order: (1) explicit ALERT pattern -> hand to `inf-ec2-retry-launch` (SNS
publish only if the hand-off itself fails); (2) explicit NORMAL pattern -> suppress; (3) unrecognised reason AND stopped within 15 s
of launch -> hand to retry; (4) otherwise no-op, logged. The ONLY behavioural change: a stop whose reason reads EMPTY no longer matches
rule 2 (the `''` entry made `any(p in reason ...)` true for every string), so it reaches rules 3 and 4.

| stop event | BEFORE | AFTER | consequence |
|---|---|---|---|
| empty reason, within 15 s of launch (the 2026-09-29 11:15:22Z case: AWS had not populated `Server.InternalError` yet) | suppressed as normal; no retry; the day's bronze run lost | rule 3: handed to `inf-ec2-retry-launch` (async invoke; no text) | the intended repair; the retry Lambda texts only if every attempt fails (Andrew-direct 2026-09-21) |
| empty reason, later than 15 s after launch (a stop whose reason AWS never fills) | suppressed | rule 4: no-op, logged `no-op-unknown-reason` | NO new notification path: rule 4 publishes nothing |
| `User initiated` / `Client.InstanceInitiatedShutdown` (every cron self-stop) | suppressed | suppressed (rule 2 unchanged) | none |
| explicit ALERT patterns | handed to retry | handed to retry | none |
| describe-instances failure | SNS publish (unchanged) | SNS publish (unchanged) | none |

New reachable notification states: NONE. The SNS fallback fires only when the hand-off `lambda:invoke` fails, as before. Both branches
above are covered by `tests/test_lambda_function.py` and by `P24-2-AC1` (four arms: empty+5 s handed; empty+2 h not suppressed and not
alerted; `User initiated`+2 h suppressed; `Server.InternalError`+5 s handed), PASS at the drain @1431d66d9b.

## 4. Rollback, per key

- The artifact: `aws s3api copy-object` of version `Yl3wNNf7j9AKp00iYsA2hQ.aSo297Q9.` over the same key (its metadata
  `content-sha256` = `RdBNvM6I...`), then the same targeted `safe-apply` (0/1/0 back to the BEFORE row). Same-window rollback; the
  ledger's D1 leg carries the readback both ways.
- Nothing else to roll back: no IAM, no rule, no environment change.

## 5. Conditions this seat asks the signer to hold it to

1. Apply only with the CTO half at HEAD naming this packet's blob.
2. Post-apply readback: `get-function-configuration` CodeSha256 == the AFTER row; a fresh EventBridge-shaped test invoke with an
   in-memory fake is NOT possible against the live function, so the readback is the CodeSha256 plus the next real `stopped` event's
   log line (`handed-to-retry-elapsed-time-defense` or `no-op-unknown-reason` for an empty reason; `suppressed-normal-shutdown` for a
   cron self-stop), recorded in the ledger's A1 leg when it occurs (tomorrow 11:15Z at the latest, the bronze trigger's start).
3. Re-plan after apply: `No changes` on the same target.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-09-30 ~15:4xZ, on this packet's bytes at the commit that carries it (blob hash in the commit). The act's write set is the
one Lambda's code pointer; the blast radius is section 3, both branches read from the producer's own rule; the rollback is section 4.

## CTO half -- SIGNED (1.0.0_SA_CTO, 2026-09-30 ~15:5xZ)

Signed on the blast radius of section 3, bound to this packet's pre-signature blob `1bc65b9b16` (@e0a2f524e4). I read the packet
and its COO half and re-ran two of its claims: the artifact-key census (`comp-find 'inf-ec2-launch-monitor.zip'` over the root and the
CI map: 29 hits across 80 files, ONE `.tf` reference at `inf-ec2-launch-monitor.tf:88`, the rest the source map and CHANGELOG records)
and the source map's `artifact_sha256` for `inf-ec2-launch-monitor` (= the AFTER CodeSha256). So exactly one function pulls the moved
key; no image, alias or tag moves. The producer's rule is read from the table in section 3: the only behavioural change is that an
EMPTY stop reason no longer matches the NORMAL suppression, and the branch it then reaches (rule 4, later than 15 s) publishes
nothing, so no new notification state is reachable (CLAUDE.md moratorium honoured). Writers of the function's code pointer: 1 (this
root's module), one rule read.
Conditions (each a stop): (1) ONE targeted `safe-apply` on `module.inf_ec2_launch_monitor` with the plan reading exactly 0 to add, 1 to
change, 0 to destroy on `aws_lambda_function.this` alone; (2) post-apply `get-function-configuration` CodeSha256 equals the AFTER row
`t1QrzaDeMtjGgnFL0oez1DGtL6vLVz7fgV0/BMVuIQo=`; (3) a re-plan on the same target reads No changes; (4) the next real `stopped` event's
log line is recorded in the ledger's A1 leg by 2026-10-01 11:15Z and names one of the three expected outcomes; a fourth outcome
re-opens the half; (5) the rollback is the S3 version copy of section 4 plus the same targeted apply, same window, both readbacks in
the ledger; (6) the ledger `inf-launch-monitor-empty-reason-served-20260930` closes at A1, never at the apply.

