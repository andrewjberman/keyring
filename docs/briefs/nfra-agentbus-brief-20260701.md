# NFRA_AGENTBUS — Brief (MSTR charter → CTO PRD)

**A metered, secured SQS bus for cross-Opal-employee agent collaboration (parallel fleets talking + working together).**

- **Type:** project (candidate `NFRA_AGENTBUS`; CTO names/scopes) — an inter-principal agent-comms bus; sibling of NFRA_COMPTEAM, rides SCTY.
- **Origin:** Andrew-direct 2026-07-01 (discussion w/ MSTR). Verbatim intent: *"I'm curious if we can make an SQS queue and associated thread where my agents could talk to agents from another Opal Employee, even having our agents collaborating in parallel. How could we meter that and secure that?"*
- **Author:** 0.0.0_AB_MSTR (scope) | **Issued to:** 1.0.0_SA_CTO (PRD + decomposition)
- **Ledger:** LD-0239 (`andrew_instruction`; S2; reversible) | **Status:** brief → CTO PRD.

## The premise + the architectural read

Today `opal-agent-comms` (broker port 7800 + inbox) is single-user / single-workspace. This is the **multi-tenant, inter-principal extension** — a comms bus between one employee's agent fleet and another's, enabling parallel collaboration. It rides directly on **NFRA_COMPTEAM (onboarding)** + **SCTY (entitlements/guardrails)** — not a new stack.

## What to build

**TRANSPORT = SQS** (durable, decoupled, AWS-native, CloudWatch-metered). A shared queue / queue-pair per collaboration between fleet-A and fleet-B. Parallel collaboration works because both fleets read their scoped slice of the shared graph (COMPTEAM Component-B read-partitions) + coordinate via the queue.

**METER (2 layers, both cheap):**
1. SQS-native CloudWatch — MessagesSent/Received/Deleted, ApproximateAgeOfOldestMessage, per-queue.
2. App-layer — a broker logs every cross-employee message (from_employee/from_agent/to/subject/size/ts) into the SAME `tool_activity` telemetry substrate → cross-employee collaboration is metered exactly like tool-use, one query surface (ties to NFRA_TOOLHEALTH).

**SECURE (5 controls — cross-PRINCIPAL agent comms is a real attack surface):**
1. **IAM-scoped per employee** — send to the shared queue, read ONLY own partition (SQS + KMS + message-group scoping); no cross-read of the other's private traffic.
2. **SCTY-guardrail gated** — an ACTION-request (vs. DATA-share) crosses a trust boundary → the SCTY entitlement/tier authz gate (different trust classes; this is SCTY_MCPGUARD/PREMCP territory).
3. **Verified attribution** — every cross-employee message carries a SIGNED from_employee+from_agent identity (not a claimed serial) — hardens the exact-serial discipline against spoof.
4. **Egress content-strip / DLP** — no secrets/PII/creds cross the employee boundary (same strip-list as the COMPTEAM kit).
5. **Default read-only / propose** — an incoming cross-employee message can REQUEST, not directly MUTATE; the receiving fleet's own agent (or a human/tier gate) adjudicates anything actionable.

## Scope / boundaries (the leash)
- IN: the SQS bus design; the per-employee IAM+KMS partition model; the 5 security controls; the metering fold-in.
- Rides COMPTEAM (onboarding) + SCTY (entitlements) — coordinate, don't duplicate. Metering feeds the same telemetry substrate as NFRA_TOOLHEALTH.
- OUT: shipping an UNSCOPED cross-employee channel (security-gated); anything write/mutating across the boundary without the SCTY authz gate; MSTR editing code.
- **Surface-flag:** cross-principal agent comms is a governance + security surface — likely warrants coordination with (or gating on) the SCTY program + possibly the same standing-Directive question as COMPTEAM.

## CTO handoff
CTO owns the PRD, whether this is a COMPTEAM Workstream-C or its own project, arch-gates, lanes (AE-cloud for SQS/IAM + SCTY-coord + DE for the broker/attribution), cross-domain coordination (COMPTEAM/SCTY/opal-agent-comms). Push back on operational grounds. The security model is the load-bearing design decision — get the entitlement + attribution + strip right before any two fleets touch.
