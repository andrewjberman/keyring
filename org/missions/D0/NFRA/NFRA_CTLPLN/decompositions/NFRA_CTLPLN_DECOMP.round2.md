# NFRA_CTLPLN decomposition -- ROUND 2, the Dell bring-up (issuer 2.0.0_SA_COO~C; drafted 2026-10-07 ~02:3xZ)

**Status: DRAFT -> ISSUED in one issuance** (the issuance commit carries the `fanout:` line).

**Cut on:** PRD v0.6 @0bab4b7532, ADMITTED (`python .tools/prd-signoff.py status NFRA_CTLPLN`: ratified-text SIGNED by `3.0.0_SA_CVO`,
current; brief half accepted). The CTO's orders: msg 105913 (cut the Dell IAM order; no access key in Terraform), 105915 (Andrew: the Dells
are on the tailnet; keys go by Taildrop, record @99b060520e; add a read of each Dell's RDP rules), 105920 (round 2 = Dell bring-up, ONE
issuance: the queues, the IAM + Taildrop, the RDP read), 105929 (priority: Andrew is waiting to pick up the keys). Round 1 closed PASS (FAST).

**Rule 24.** Domain: what a Dell's fabric manager needs to take an award -- an identity (FWD-10), a bus channel (FWD-3) and a remote desktop
locked to the tailnet (FWD-14). The register rows are DONE (`1.0.0_SA_CTO` @b186342547: dell1, dell2 with role and tailnet measured). Three
cells, one intent each. Excluded, with the reason: migrating the laptop/site Z queue pair to the per-box names (C-BUS, same-window) -- a later
round, after the Dells are on the bus; FWD-1's thread (a real round laptop -> dell1 -> site Z) -- it needs these three first.

## Measured constraints (read at the base, 2026-10-07 ~02:2xZ)

1. **Names, builder output** (NAMING_SCHEMA v1.13 @01c56eda2b; `lib/opal_naming.name`): users `cloudops-dell1-agent-user`,
   `cloudops-dell2-agent-user` (`name('cloudops', None, 'dell1-agent', 'user')`); group `cloudops-dell-agents-group`; policy
   `cloudops-dell-agent-deploy-policy`. Queues (C-BUS): `name('agentbus','global','dell1','queue')` -> `agentbus-global-dell1-queue`; the
   builder emits no FIFO form today (`qualifier='fifo'` gives `...-fifo-queue`; `.fifo` refused) -- the CTO asked `4.0.0_SA_CRO` for the
   registry change (msg 105928). The queue cell is GATED on it.
2. **Existing bus** (`infra/aws/terraform/nfra-agentbus-port2/`): two FIFO queues, content-based dedup, retention 1,209,600 s, visibility
   30 s, receive wait 20 s, max message 1,048,576 bytes, SSE-SQS managed (no CMK), no queue policy; backend
   `s3 opal-313476888478-terraform-state`, key `nfra-agentbus-port2/tfstate`, region us-east-1. `.tools/agentbus-sqs.sh` resolves every
   box's queue from `org/devices/DEVICES.json` (FWD-2 round 1), so a Dell's `inbound_queue` filled in the register is all the tool needs.
3. **Tailnet** (laptop `tailscale status`, 2026-10-07 ~01:0xZ): laptop `cloud-local` 100.96.167.100, sitez 100.99.180.19, dell1
   100.79.95.44, dell2 100.104.84.87. The laptop's three Remote Desktop inbound rules are scoped `100.64.0.0/255.192.0.0` on profile Any
   (read 01:0xZ). The Dells' rules are unread.
4. **C-IDENTITY scope:** ALLOW code and data deploys through `.tools/safe-deploy.sh` and `safe-apply` for non-IAM resources (each with the
   box's own ledger entry), trunk-only; DENY IAM user, key, role and policy changes, CloudTrail changes and production data deletes; IAM-creating
   applies at site Z only. **No `aws_iam_access_key` in Terraform** (CTO 105913): after the apply, site Z creates one key per user, sends it
   with `tailscale file cp <file> dell1:` / `dell2:`, deletes its own copy and reads it back gone (Andrew, record @99b060520e).

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `CT-b-1` | the Dell identities: a Terraform root with the group (display tag DellBoxes where IAM allows tags), two users, their membership, and the deploy policy; NO access key; a static check and a policy simulation | FWD-10 | NOT-EVALUATED | laptop (apply at site Z) | WORLD | A, `0.9.0_WK_NFRA_CTLPLN~1` |
| `CT-b-2` | the RDP lock read: a read-only check that prints each box's Remote Desktop inbound rules and whether all are scoped to the tailnet, run here on the laptop, plus a tailnet reachability probe of both Dells' 3389 | FWD-14 | NOT-EVALUATED | laptop (the on-Dell reads by each Dell's seat or Andrew) | LOCAL | B, `0.9.0_WK_NFRA_CTLPLN~2` |
| `CT-b-3` | the two Dell inbound queues: a Terraform root mirroring the existing bus queues' attributes, names from the builder's FIFO form; GATED on that form landing | FWD-3 | NOT-EVALUATED | laptop | WORLD | C, `0.9.0_WK_NFRA_CTLPLN~3` (spawned when the FIFO form lands) |

## Write sets (disjoint)

- **CT-b-1:** `infra/aws/terraform/nfra-ctlpln-identity/` (new root: `main.tf`, `iam.tf`, `dell_deploy_policy.json`, `tests/check_identity.py`,
  `tests/simulate_policy.py`).
- **CT-b-2:** `org/devices/rdp_lock_check.ps1`, `org/devices/rdp_reach_check.py`.
- **CT-b-3:** `infra/aws/terraform/nfra-ctlpln-agentbus/` (new root: `main.tf`, `sqs.tf`, `tests/check_queues.py`).
- Each: its deliverables folder and the investigation file.

**Ordering and fan-out:** `fanout: 2 of 3 chains now, cap 8` -- A and B spawn at the issuance; C is cut in the same issuance and spawns when
the FIFO form lands (its only unmet dependency is that registry change, not another cell).

## The issuer's acts after the drain (routed to site Z through `0.0.0_AB_MSTR`, one ledger entry per apply)

1. CT-b-1: `safe-apply` at site Z (an IAM-creating apply, site Z only); read back the group, users, membership and policy; then site Z's key
   step and the two Taildrop sends, its copies deleted and read back gone; tell `1.0.0_SA_CTO` both sends are done.
2. CT-b-2: each Dell's seat (or Andrew over RDP) runs `org/devices/rdp_lock_check.ps1`; the output lands in the register's tailnet fields'
   evidence.
3. CT-b-3: `safe-apply` (a non-IAM apply), read back both queues' attributes; fill each Dell's `inbound_queue` in the register; one
   `agentbus-sqs.sh send` to each Dell queue and its receive, read back.
