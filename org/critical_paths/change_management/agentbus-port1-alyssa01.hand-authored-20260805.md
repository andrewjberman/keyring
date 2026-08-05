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

**OPEN.**
