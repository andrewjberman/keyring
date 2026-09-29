# Never-widen SECOND half: NFRA_OPLGTW OG-m-3 (= OG-m-2b, the chain-log classifier) -- SIGNED, with 3 GO guards

Signer: `3.0.0_SA_CVO~O` (the non-acting half), 2026-09-29 ~02:5xZ.
Ask: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-m-3_20260929.md` @bd0e06fe4c
(msg 26403). The ask's blast radius is the DELTA over the live OG-m-2a.

## What I read

- **The ask, sections 1-5.**
- **The bytes.** `sha256sum` of the worker's `og-m-2b_candidate_frozen.patch` and of the CTO pin
  `OG-m-2b_candidate_vs_8340c65376.patch` (@5b44ba518d) gives `600a4b6da9e75c65...` for BOTH. The patch touches 2
  files: `lambda_function.py` and `advi_49f_floor.tf`.
- **The patch's added lines naming a bucket, ARN, action or s3 command.** Every one is inside the ask's stated delta:
  - `s3:GetObject` on `${local.advi_49f_bucket}/${local.advi_49f_chain_log_prefix}*`;
  - the 2a marker statement, already live;
  - `CHAIN_LOG_BUCKET = local.advi_49f_bucket`;
  - the SSM document's upload line, now reading the local.

  There is no `ListBucket`, no other bucket, and no wildcard action.
- **The writers of the chain-log prefix, from the ask's section 2 census:** N = 1, the SSM document. This act changes
  its SOURCE but not its rendered bytes. It adds 1 reader, the dispatcher. The 2a gate is byte-unchanged.

## Blast radius as signed

The ask's section 1 table: four keys on the dispatcher (artifact, code, environment, inline policy), each with its
rollback to 2a:
- artifact VersionId `3qOKR75B...`;
- `CodeSha256` `KqlIoAJs...`;
- the environment back to its 3 prior variables;
- the policy back to 2a's single s3 statement.

Not touched, by name: the marker writer, `silver.tf` and the notification, the SSM document's rendered body, the floor
schedule (still the production trigger), the host, the chain code, and 2a's gate. Nothing served is written.

## Both branches, read from the classifier's rule in the frozen bytes

- **Deploy succeeds:** a terminal invocation is graded from its chain log. The last `CHAIN ` line gives OK, REFUSED or
  ABORT. Otherwise the result is UNKNOWN, with the reason named: `absent` (AccessDenied without ListBucket), `no
  terminal line`, or `unconfigured`. No branch calls `send_command` again or retries.
- **Deploy fails:** roll back per key to 2a. The 2a gate keeps running either way.

Observation, not a condition: the log key is the host script's own timestamp, and the classifier tries
`ExecutionStartDateTime` plus or minus 1 s. If host start-up skews more than 1 s, a completed chain still reads
`UNKNOWN(chain_log=absent)`. That branch is covered and harmless, but it defeats E11's purpose. The close run should
report how many terminal invocations graded OK, not only that the code deployed.

## GO guards (read by the issuer before PHASE B)

- **P1.** The graded commit's diff of the two files against `8340c65376` equals the frozen patch, sha256 `600a4b6d...`.
  It is re-applied UNMODIFIED. Any other byte voids this half.
- **P2.** The targeted plan lists only `module.advi_49f_gold_dispatch` (code and environment) and
  `aws_iam_role_policy.advi_49f_gold_dispatch`. Anything else STOPS the cell, including `aws_ssm_document.*`, which is
  the ask's own stop.
- **P3.** After the apply, read back live:
  - the policy is 2a's statement plus exactly `ReadTheChainLog` = `s3:GetObject` on
    `arn:aws:s3:::opal-data-49financial/gold/advi/_logs/chain_*`, with no ListBucket;
  - the environment is the 3 prior variables plus exactly `CHAIN_LOG_BUCKET=opal-data-49financial` and
    `CHAIN_LOG_PREFIX=gold/advi/_logs/chain_`.

  Anything more: roll back.

Naming note: `OPLGTW-LEGACY-READ-01` has a cutoff of 2026-10-06. After that date, a further edit of this local is
refused, and the prefix's migration is ADVI_FIRMBKTS's.

-- 3.0.0_SA_CVO~O
