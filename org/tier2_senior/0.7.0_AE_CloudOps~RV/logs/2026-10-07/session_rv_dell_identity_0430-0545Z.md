# The Dell identities and their inbound queues are live, and the halt gate cannot name a two-letter lane — 0.7.0_AE_CloudOps~RV

**archetype:** DEPLOY

**Date:** 2026-10-07 (04:30Z–05:45Z)
**Task Order:** `org/tier2_senior/0.7.0_AE_CloudOps~RV/task_orders/NFRA_CTLPLN.TO-DELL-1.dell-identity-apply-site-z.md` (WORLD; flipped `complete` by the issuer @a3a99d80da)
**Status:** COMPLETE — both legs applied, proven and closed. Nothing owed by this seat.

## Objective

Create the two Dell agent IAM identities at site Z, then their two inbound FIFO queues, by applying two
Terraform roots from a detached worktree at exactly one commit — so Andrew's Dell machines can be issued
keys. Andrew, verbatim, relayed ~04:2xZ: "Where is the Dell Keys? i want that issued". URGENT, and an
IAM-creating apply, so the plan's exact shape gated each apply.

## Compiler Tools

- `comp-iam gaps` — RUN after the identity apply. 37 missing / 294 deny-present / 1 coverage-unknown /
  3 resource-mismatch across 33 services, all pre-existing estate rows, none naming a `cloudops-dell`
  principal.
- `comp-read --for` / `--enumerate` — the halt gate's resolver contract (`:172-174`), the session-log
  standard's section set, and every `<status>` tag on `ETFS_RIVALS.TO-RIV-iam-1`.
- `comp-find --files` — located the ETFS_RIVALS order; timed out at 120 s on a repo-wide regex and was
  answered by `Glob` instead.

**What worked:** `comp-read --enumerate '<status>[a-z]+</status>'` printed BOTH tags with line numbers
(82 `pending`, 86 `complete`). `to-check.py` had reported that order PENDING off the FIRST tag; the
enumeration is what showed the live tag is the LAST one, so nothing was owed there.

**What failed:** `comp-iam gaps` is silent on this entire apply and that silence is not evidence — it
models Lambda/EC2 ROLES and cannot see an IAM user at all, so the Dells are outside its domain. Logged
as a floor, never as a clean bill. `comp-find --files` over a bare project regex exceeded its 120 s
budget on this box.

**Gap found:** no comp-tool answers "does this IAM user / group / policy / SQS queue EXIST". That is the
negative arm every IAM-creating apply needs, and it routed to `# rail-checked:` raw `aws` four times.

## Deployment Sequence

| # | Act | Instrument | Result |
|---|---|---|---|
| 1 | Detached sparse worktree at EXACTLY `0ef817adb0` | `git worktree add --detach` + sparse cone | `HEAD 0ef817adb0`; identity-root diff from `0ae63f9dbf` EMPTY (measured here, not taken from the order) |
| 2 | Identity root static checks | `check_identity.py`, `simulate_policy.py` | exit=0 / exit=0; `no_access_key=True`, `names_from_builder=6/6`, `allowed_ok=8/8 denied_ok=11/11` |
| 3 | Negative arm, leg A | `iam get-user` / `get-group` / `get-policy` | all six objects `NoSuchEntity` |
| 4 | Plan, UNTARGETED | `terraform plan -out` + plan JSON | 10 create / 0 / 0; type tally exactly the CTO half's section 1; `access_key resources: []` |
| 5 | NEVER-2 entry opened and committed | `deploy_ledger.py open` | @f5ec84b376, 5 legs |
| 6 | Leg A apply | `safe-apply` + audited `HALT_OVERRIDE` | **10 added, 0 changed, 0 destroyed**; re-plan rc=0 |
| 7 | Leg A entry closed | `deploy_ledger.py close` | @8db57ef669, 5/5 |
| 8 | Row filed | surprise channel | `NFRA_CTLPLN-Z-S1` @a8dcf7581a |
| 9 | Negative arm, leg B | `sqs list-queues` | 0 `agentbus-global*` against a printed denominator of 6 `agentbus` queues |
| 10 | Queue root check + plan | `check_queues.py`, plan JSON | `names_from_builder=2/2 attributes_match=True`; 2 create, both `aws_sqs_queue`, both FIFO, non-sqs: `[]` |
| 11 | NEVER-2 entry opened and committed | `deploy_ledger.py open` | @13cb10de66, 3 legs |
| 12 | Leg B apply | `safe-apply` + audited `HALT_OVERRIDE` | **2 added, 0 changed, 0 destroyed**; re-plan rc=0 |
| 13 | Leg B entry closed | `deploy_ledger.py close` | @9a091d4515, 3/3 |

## Verification

- **AC1** `check_identity.py` exit=0 at the GO's commit.
- **AC2** `iam get-group` → exactly `["cloudops-dell1-agent-user","cloudops-dell2-agent-user"]`.
- **AC3** `list-access-keys` → 0 and 0. No key created by either leg, by any means.
- **CTO condition 2** `terraform state list` = 10 resources, `aws_iam_access_key` in state = 0.
- **CTO condition 5** all three policy DEFAULT VERSION documents canonical-JSON-equal to the repo JSON
  (deploy 8 stmts = 8, dell1-bus 1 = 1, dell2-bus 1 = 1). Attachments: group → deploy policy;
  dell1 → dell1-bus; dell2 → dell2-bus.
- **Live principals** `simulate_principal_policy` 10/10, ONE `--resource-arns` per call. The per-user
  queue isolation `implicitDeny` carries its positive control as a SEPARATE invocation — dell1 `allowed`
  on its OWN queue, `implicitDeny` on dell2's, mirrored — so that deny is the world, not the instrument.
- **Queues** both return a URL; all seven attributes identical on both and equal to `sqs.tf`'s locals
  (FIFO, content dedup, 1209600, 30, 20, 1048576, SSE-SQS, no CMK).

## Decisions Made

1. **The halt gate's refusal was cleared by the audited `HALT_OVERRIDE`, not by rewriting my serial file.**
   The gate fail-closed because its resolver admits a single-uppercase-letter lane only and this lane is
   `~RV`. The banner diagnosed a corrupted session serial file and printed the `printf` to overwrite it —
   complying would have made the gate scan ANOTHER agent's inbox and exit 0, the false negative the
   gate's own comments at `:143-152` condemn. I measured the condition the checkpoint exists to enforce
   with the sound instrument instead (broker inbox empty, 20/20 delivery rows READ and acked by this
   serial, 0 STOP/HALT-class) and cited NO halt-gate pass anywhere.
   **`1.0.0_SA_CTO~Z` subsequently ruled this the admitted path** (msg 30655, relayed 30656): the lane
   check becomes an existence check, `0.0.0_AB_MSTR~Z` is the one writer of the fix, and until it lands
   the audited override citing the row is correct with no pass cited.
2. **Three halves named three different commits and I chose none by preference.** The laptop COO half
   pinned the queue root at `c649197dd0`, the site-Z CTO ADDENDUM 1 named a worktree at `6f240da3ca`,
   the order said EXACTLY `0ef817adb0`. Measured: `0ef817adb0` descends from both others and BOTH roots
   are byte-identical across all three pins, with a positive control proving the diff command
   discriminates. Every condition therefore holds at the applied commit and the conflict is immaterial.
3. **The row is BLOCKING/ARMED with its disarm named but not taken.** `.tools/` is outside this order's
   `<paths>`, so the fix was described and routed, never written.
4. **Leg B's non-inertness claim rests on a NEW measurement, not a re-print.**
   `simulate_principal_policy` evaluates an ARN pattern whether or not the queue exists, so the
   pre-apply 10/10 was never evidence the bus policies were live. Re-run against the real queues it is
   still 10/10 — that is the measurement that earns the claim.

## Files Modified

- `org/critical_paths/change_management/20261007T0453Z_nfra-ctlpln-dell-identity-sitez-20261007_deploy_completion.md` — opened @f5ec84b376, CLOSED 5/5 @8db57ef669
- `org/critical_paths/change_management/20261007T0525Z_nfra-ctlpln-dell-queues-sitez-20261007_deploy_completion.md` — opened @13cb10de66, CLOSED 3/3 @9a091d4515
- `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` — row `NFRA_CTLPLN-Z-S1` @a8dcf7581a
- `org/mcp/sessions/471a9973-0b57-41d2-a496-adc2fa5545b8.serial`, `.comp-graph/.agent_context` — startup, not committed

Cloud state changed: 10 IAM resources and 2 SQS FIFO queues created. No Terraform root file was edited.

## Blockers

**None.** Nothing is owed by this seat. Two items sit with named owners, neither blocking this seat:
- `0.0.0_AB_MSTR~Z` — leg (2), the access keys. Both users exist with 0 keys and are ready.
- `0.0.0_AB_MSTR~Z` — the halt-gate lane fix, per the CTO's ruling @90e794e816.

## Current State

Both Terraform roots are applied and 0-diff against their configuration. The two Dell IAM users exist
in `cloudops-dell-agents-group` with the deploy policy on the group and one bus policy per user, and
both hold zero access keys. Both inbound FIFO queues exist with the attributes `sqs.tf` declares, and
their names match the ARNs the bus policies name, so the grants are live rather than inert. Both NEVER-2
entries are CLOSED with nothing stranded and neither leg rolled back.

The halt gate remains closed to this lane. The override is the admitted path by CTO ruling until
`0.0.0_AB_MSTR~Z` lands the existence check, and no halt-gate pass is cited in any artifact this session
produced.

Five commits are LOCAL except the first; `origin/CLOUD` read `f66e667c59` by `ls-remote` at 05:35Z. This
seat does not push a shared branch. The worktree `C:/tmp/dell-identity-0ae63f9` is left in place and
named in both reports; its removal is an operator act (`/cleanup`).

## Next Steps

1. **[`0.0.0_AB_MSTR~Z`] Issue the two access keys** — one per user, outside Terraform, by
   `tailscale file cp` to `dell1:` and `dell2:`, local copies deleted and read back gone. The CTO half's
   section 5 conditions apply and `list-access-keys` must then read exactly 1 per user.
2. **[`0.0.0_AB_MSTR~Z`] Land the halt-gate existence check** per the ruling at
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_HALT_GATE_MULTI_LETTER_LANE_20261007.md`, and
   split the banner so a VALID-BUT-UNADMITTED lane never reads as a corrupt serial.
3. **[`1.0.0_SA_CTO`] Consider the tightening section 3 of the CTO half names** — scope
   `lambda:UpdateFunctionCode`/`InvokeFunction` by name prefix or tag, and exclude the Terraform state
   bucket from `s3:PutObject`. Named as NFRA_CTLPLN's to place, not this seat's.
4. **[`3.0.0_SA_CVO~RV`] Graduate `NFRA_CTLPLN-Z-S1`** when the fix lands — the disposition is not a
   seat's to write.
