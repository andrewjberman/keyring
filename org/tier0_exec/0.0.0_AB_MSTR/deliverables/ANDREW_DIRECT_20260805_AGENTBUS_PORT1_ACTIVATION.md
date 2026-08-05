# ANDREW-DIRECT — AGENTBUS Port 1 activation, 2026-08-05 ~2100Z, base MSTR terminal

**Channel:** base MSTR terminal, immediately following the Port-1/Port-2 explanation
(can Alyssa's agents reach MSTR~Z; answer: Port 1 is the designed home, design-not-shipped).

**VERBATIM:**
> "I want it stood up, do not bother CTO with it as they are busy you have sovereign
> egress to get started."

## Reading (recorded, not widened)
- **"it" = Port 1**, the inter-colleague bus (the antecedent of the whole exchange:
  Alyssa's fleet talking to Andrew's fleet).
- **"stood up" + "sovereign egress to get started"** = the activation authorization the
  module's own fence names (the AB-ACTIVATE gate anticipated a Directive as the vehicle;
  a sovereign direct word is the superior form of the same authority). It authorizes
  STANDING UP the channel; it does NOT waive the 5-control security model — the PRD's own
  binding framing ("the security model IS the design") stands, and the build is to-spec,
  fail-closed on every control.
- **"do not bother CTO"** = the work does not route through CTO's desk and the CTO
  arch-gate step is discharged by his word for getting started; INFORMING CTO is the
  record+broadcast LAW and is not "bothering" — done same turn.
- Executor: base MSTR (confirmed to MSTR~Z on the bus, their seat clear).

## Two design inputs adopted from the fabric (recorded)
- MSTR~Z: any standing egress ships DENY-BY-DEFAULT (availability is not authorization);
  no open-with-audit posture.
- MSTR~Z: a control that ERRORS must be distinguishable from a control that DENIES —
  fail-closed is only meaningful with that distinction surfaced.

## Execution plan (Phase A tonight, per the existing S1 spec + module)
1. New TF root `infra/aws/terraform/nfra-agentbus-alyssa01/` (separate state key per the
   Port-2 precedent: a Port-1-collab apply can never reach another channel's state):
   queue-pair + per-collaboration KMS key + partitioned identities. Fleet A = Andrew's
   fleet (role assumable by Andrew_Berman, sim01 shape); Fleet B = Alyssa's fleet (IAM
   user, NO access keys minted — credential mint + handoff is Andrew's act, deny-by-default).
2. The module fence (`simulated` validation) amended to accept a real activation ONLY
   with an explicit authorization reference — this record + LD-0379.
3. Controls: 1 (partition) lands tonight in TF; 4 (strip) exists implemented+tested and
   binds at the sender-side gate per Amendment B's AC-1 disposition; 2/3/5 bind in the
   adapter build that follows — NO live cross-fleet message flows until the adapter's
   controls are exercised (the channel exists; the first real message waits on the
   controls being verifiable, which honors both his "stood up" and the PRD's fail-closed).
4. Live verification per PRD §5.6: get-queue-policy + a cross-read DENY exercise, never
   TF-desired.
