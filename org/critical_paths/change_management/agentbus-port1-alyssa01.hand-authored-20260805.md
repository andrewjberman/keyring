# Deploy: agentbus-port1-alyssa01

**Opened:** 2026-08-05T22:10Z by 0.0.0_AB_MSTR~Z · **Authority:** LD-0379 (Andrew-direct
2026-08-05 ~2100Z base terminal, activation verbatim recorded at
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260805_AGENTBUS_PORT1_ACTIVATION.md`;
CTO informed, NO COUNTERMAND). Execution transferred base -> site Z per Andrew-direct
~2143Z ("hand off this work to sitez MSTR~Z ... more relevant they do it anyway as its
directly relevant to them on the terminal machine").

NFRA_AGENTBUS **Port 1** first real cross-principal collaboration `alyssa01`: control-1
partition only (transport + identity + encryption). TF root
`infra/aws/terraform/nfra-agentbus-alyssa01/`, own state key `nfra-agentbus-alyssa01/tfstate`
— an apply here cannot reach sim01, Port 2, or any other channel.

**THE ACTIVATION FENCE IS NOT THE CHANNEL.** Andrew's word discharges AB-ACTIVATE for this
collaboration; the 5-control model is NOT waived. This deploy lands control 1 ONLY.
Controls 2/3/5 bind in the adapter (separate leg, not in this ledger's scope to close);
control 4 exists at `infra/aws/agentbus/control4_egress_strip.py`. **No real cross-fleet
message flows until the adapter controls are exercised — transport existing is not the
channel open.**

## Legs

- **L1 — plan reviewed.** Read before apply, not after. `10 to add, 0 to change, 0 to
  destroy`; every action `create`; **`aws_iam_access_key` count = 0**, which is the
  deny-by-default property asserted in source and now confirmed in the plan. (Base's
  handoff said 9 resources; I counted 10 and flagged it before planning — base confirmed
  the miscount was theirs, a dropped `kms_alias`. The plan settles it at 10.)
- **L2 — apply** via `.tools/safe-apply.sh` (HALTGT-gated; bare `terraform apply` is a
  NEVER). `SAFE_APPLY_TERRAFORM` override in use: `.tools/terraform.exe` does not exist on
  site Z, terraform is the WinGet install on PATH (v1.15.8). Then 0-diff re-plan.
- **L3 — tag** `agentbus-alyssa01-v0.1.0`, push `--follow-tags`.
- **L4 — LIVE verify per PRD 5.6.** `get-queue-policy` on BOTH queues (applied truth, not
  the TF's desired state) **plus an EXERCISED cross-read DENY**: assume the andrew role,
  attempt `ReceiveMessage` on alyssa's inbound — `AccessDenied` is the pass. Positive
  control run as a SEPARATE invocation (Rule 22a: a control sharing an invocation with the
  target is disarmed by the multi-resource false-deny mode).

## Completion

**CLOSED 2026-08-05T22:45Z.** All four legs landed; control 1 is live and exercised.

**L1** plan read before apply: 10 add / 0 change / 0 destroy, every action a create,
`aws_iam_access_key` count 0 — the deny-by-default property confirmed in the plan rather
than taken from the source comment.

**L2 — APPLY STRANDED 2-of-10 ON A REAL DEFECT, THEN COMPLETED.** The first apply created
the role and user, then failed `InvalidArnException` on the KMS key. Not a transient:
`aws_iam_user.fleet_alyssa` sets `path = "/agentbus/"`, so its real ARN carries the path,
while `local.user_b_arn` omitted it — the policy named a principal that does not exist.

**KMS catching it was luck.** That same ARN is the principal in BOTH SQS queue policies,
so the plausible failure was a channel that builds clean and grants Alyssa nothing:
well-formed policy documents, every config read green, and the defect surfacing only as
"messages never arrive". Fixed at the source — the path is now a local consumed by BOTH
the resource and the ARN, so they can no longer drift apart. Re-plan showed role and user
as no-op (no replacement forced); apply 8 added / 0 changed / 0 destroyed;
`plan -detailed-exitcode` returned 0. Fix committed at `6f126f900`.

**L3** tag `agentbus-alyssa01-v0.1.0` pushed with `--follow-tags`.

**L4 — LIVE VERIFY, EXERCISED NOT INFERRED.** Applied `get-queue-attributes` on both
queues shows the four partition statements carrying the CORRECTED path-bearing alyssa
ARN — the fix confirmed in APPLIED state, not merely in source. Then, as the andrew fleet
role, in three SEPARATE invocations:

- positive control — Receive on its OWN inbound: authorised (rc=0, queue empty);
- cross-read — Receive on ALYSSA'S inbound: **AccessDenied**;
- directionality — Send to its OWN inbound: **AccessDenied**.

The positive control ran first and separately on purpose: without it, the two denials are
indistinguishable from a role that simply does not work.

**Lane:** commits rode an audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`
(`infra/aws/terraform/**` is not MSTR's lane; the authority is Andrew's LD-0379 execution
transfer, not lane membership). Steady-state ownership routes to `0.7.0_AE_CloudOps`.

**NEAR-MISS, recorded because it nearly reached the remote:** the first attempt at the fix
commit passed a DIRECTORY pathspec; `safe-commit` uses `git add -f`, which overrides
`.gitignore`, and it swept in `.terraform/` — a 718 MB provider binary plus a local
tfstate. Caught before push by reading the commit's own `--stat` instead of assuming a
scoped pathspec stayed scoped. The destructive-reset guard then correctly refused to
rewrite it, so the repair was to abandon that disposable worktree and recommit from a
clean one with explicit FILE paths.

## STILL OPEN — the channel is NOT open

**This deploy landed control 1 only.** Controls 2/3/5 bind in the adapter, which is not
built. **No real cross-fleet message flows until those are exercised — the transport
existing is not the channel open.**

Held by Andrew, not by this ledger: the Alyssa credential mint (the user has ZERO access
keys by design) and the standing-Directive question.
