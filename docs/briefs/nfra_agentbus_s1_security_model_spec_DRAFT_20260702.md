# NFRA_AGENTBUS S1 -- Cross-Principal Security Model (the 5-control DESIGN SPEC)

**TO:** NFRA_AGENTBUS.S1 (`0.4.0_DE_ClientPlatform`, issued `2.0.0_SA_COO~B`, GO 2026-07-02, LD-0239). **Status:** DRAFT for the CTO arch-gate (each control = a CTO arch-gate; the arch-gate IS S1 acceptance + the S2-S4 unlock).
**Binding role:** this spec is the **binding interface** S2 (SQS transport + IAM/KMS partition) and S3 (broker adapter) build to. **Design-only** -- NO live cross-principal wiring, NO two-fleet activation (fenced for a separate Directive). PRD: `docs/architecture/NFRA_AGENTBUS_PRD.md` SS3/SS5/SS8.
**Grounds:** SCTY_MCPGUARD_PRD (tier gate), SCTY_PREMCP_PRD (entitlement token), NFRA_COMPTEAM_PRD (signature-root + strip-list), opal-agent-comms (`org/mcp/` broker -- EXTENDED, not replaced).

---

## 0. The load-bearing framing
The security model IS the design. All 5 controls apply at **ONE choke point -- the broker adapter** -- and every control is **fail-closed** (the safe state is deny/block/reject; a control that can't complete does NOT pass the message). A working transport with a weak model is a FAILURE. The intra-fleet `opal-agent-comms` path is **UNCHANGED** -- AGENTBUS is a NEW cross-principal seam only.

## 1. The choke point + the message envelope (what S2/S3 build to)
The adapter bridges each fleet's `opal-agent-comms` broker <-> the SQS queue-pair. Every cross-fleet message is an envelope:
```
AgentBusEnvelope {
  from_employee, from_agent      # control 3 -- SIGNED, resolved off the sig-root (NOT self-claimed)
  to_employee, to_agent
  subject, body
  classification                 # control 2 -- "data" | "action" (unset -> fail-closed-as-action)
  signature                      # control 3 -- over (from_employee|from_agent|to|subject|body|classification|ts)
  ts, collaboration_id
}
```
The adapter processes the envelope through the 5 controls in a **fail-closed order** (SS7). Nothing bypasses the adapter -- there is no direct fleet-to-SQS path (control 1's IAM makes the adapter's role the only sender/receiver identity).

## 2. Control 1 -- IAM + KMS per-employee partition (gates WHO can reach the wire)
- **Design:** a shared **queue-pair per collaboration** (`A->B`, `B->A`), NOT a global multi-tenant queue. Each fleet's adapter runs under an IAM identity that can `sqs:SendMessage` to the pair and `sqs:ReceiveMessage` **ONLY from its own inbound partition**. Scoping = SQS queue-policy (per-principal `Allow` on the exact queue ARN) + `sqs:` action scoping + message-group scoping + a **per-collaboration KMS key** (`kms:Decrypt` granted only to the two consenting fleets' roles).
- **Fail-closed:** an identity outside the collaboration's grant reaches nothing (no queue read, no KMS decrypt -> ciphertext-only). Default-deny queue policy; explicit two-principal allow.
- **Interface:** pure AWS IAM/SQS/KMS -- no external dependency; **S2 builds it**, S1 specifies the policy shape. Live test (arch-gate G2): fleet-B is DENIED `ReceiveMessage` on fleet-A's inbound.

## 3. Control 2 -- SCTY-gated ACTION-vs-DATA (gates WHAT THE RECEIVER MAY DO)
- **Classifier:** every envelope is `classification in {data, action}`. **DATA-share** = information, read-only-by-construction (no side effect on the receiver). **ACTION-request** = do-something, crosses a trust boundary. **Unset/unrecognized classification -> fail-closed-as-action** (treated as the higher-trust class; cannot slip through as data).
- **Authz binding (the real interfaces, layered -- SCTY_MCPGUARD_PRD SS-layering):**
  - **SCTY_PREMCP entitlement = WHO may act.** An ACTION-request must present a valid PREMCP entitlement token (RS256, no alg-downgrade, strict per-resource `aud` = the collaboration/action resource, revocable via kill-switch/per-user blocklist). No valid entitlement -> DENY.
  - **SCTY_MCPGUARD tier = HOW MUCH / HOW SAFELY.** The receiver's user-type tier (the ONE shared tiering table) sets the cap/confirm profile; MCPGUARD never RELAXES an entitlement, only further restricts (blast-radius cap + confirm-on-irreversible, tier-independent safety).
  - Composition: PREMCP decides permission, MCPGUARD decides safety of a permitted action. Both must pass before the receiving fleet may act.
- **DATA-shares bypass the authz gate** (read-only-by-construction) but still pass controls 1/3/4.
- **Fail-closed:** an ACTION without a valid entitlement, or an unclassified message, is DENIED at the adapter.

## 4. Control 3 -- Verified signed attribution (gates WHO sent it)
- **Design:** every envelope carries a `signature` over its identity+content, and `from_employee+from_agent` is **resolved off the COMPTEAM signature-verified root-of-trust** -- the SAME identity substrate the SCTY tier-model uses (no new auth). This hardens the exact-serial discipline (which today trusts a claimed serial string) against cross-principal spoof.
- **Fail-closed:** an **absent or unverifiable signature -> message REJECTED** at the inbound adapter (before any classification/action). A valid signature resolves the TRUE `from_employee+from_agent`; the claimed serial is never trusted.
- **Interface:** COMPTEAM signature-verified identity root (`NFRA_COMPTEAM_PRD` SS-identity-reuse: "unverified identity -> fail-closed, same root-of-trust"). S1 binds to it; the sign (outbound) + verify (inbound) primitives are the COMPTEAM root.

## 5. Control 4 -- Egress content-strip / DLP (gates WHAT LEAVES)
- **Design:** at the **outbound** adapter, scan the envelope body + all string fields against the **COMPTEAM strip-list** (secrets / credentials / secret-ARNs / AWS account-ids / internal hostnames + bucket-names / firm-internal PII). Reuse the COMPTEAM kit strip-list module (the fail-closed build/runtime gate) -- do NOT re-derive the patterns.
- **Fail-closed by construction:** a strip-list hit -> the field is redacted OR the message blocked (policy per hit-class). A distributed secret is unrecoverable, so the strip runs BEFORE `SendMessage` (an already-sent secret can't be un-sent). Known-bad fixture (planted secret/ARN/internal-path) MUST be redacted/blocked; a clean message flows.
- **Interface:** COMPTEAM strip-list kit (`NFRA_COMPTEAM_PRD` SS2 -- the fail-closed strip-list build gate). Reused at the AGENTBUS outbound adapter as a runtime gate.

## 6. Control 5 -- Default read-only / propose-only (gates WHAT THE RECEIVER MAY DO)
- **Design:** an incoming cross-employee message can **REQUEST, never directly MUTATE**. The receiving fleet's own agent (or a human/tier gate per control 2) adjudicates anything actionable. Default posture = propose-only; mutation requires the explicit control-2 authz path (PREMCP entitlement + MCPGUARD tier + receiver adjudication).
- **Fail-closed:** the default is the SAFE state (propose, no side effect); a mutation is only reachable through the control-2 gate. There is no default-mutate path.

## 7. Composition + the fail-closed ordering at the choke point
**WHO** = controls 1 (partitioned identity) + 3 (signed attribution). **WHAT LEAVES** = control 4 (egress strip). **WHAT THE RECEIVER MAY DO** = controls 2 (action authz) + 5 (propose-only). All five apply at the broker adapter; none optional.

Fail-closed processing order (a control that can't complete blocks the message):
- **OUTBOUND (fleet-A adapter, A->B):** (3) resolve+SIGN attribution -- can't sign -> BLOCK; then (4) STRIP egress -- hit -> redact/block; then (2) CLASSIFY (unset -> action); then (1) `SendMessage` under the scoped IAM identity.
- **INBOUND (fleet-B adapter):** (1) `ReceiveMessage` ONLY from B's inbound partition (IAM denies A's); then (3) VERIFY signature -- absent/forged -> REJECT; then (5) propose-only default; then (2) if `classification==action`, require a valid PREMCP entitlement + pass the MCPGUARD tier gate -- else DENY; `classification==data` -> delivered read-only; then app-layer METER -> `tool_activity`.

**Ordering rationale:** verify identity (3) before acting on content; strip (4) before send (unrecoverable-once-sent); classify-as-action on ambiguity (2); partition (1) is the transport-layer envelope around all of it. Any control failing -> the message does not proceed (fail-closed).

## 8. Intra-fleet path UNCHANGED (extend, not replace)
The single-tenant `opal-agent-comms` broker (port 7800 + `org/mcp/inbox/`) is untouched. Intra-fleet messages never enter the adapter, never touch SQS, never carry an AgentBusEnvelope. AGENTBUS is the CROSS-fleet seam only; a regression test (PRD AC6) asserts intra-fleet delivery is byte-identical to today.

## 9. Interface bindings + sequencing dependency (the flag COO~B asked for)
| Control | Real interface (bind, don't invent) | Spec'd? | Implementation status |
|---|---|---|---|
| 1 partition | AWS IAM/SQS/KMS (S2 builds) | yes | S2 |
| 2 authz | SCTY_PREMCP entitlement token (RS256, aud-scoped, revocable) + SCTY_MCPGUARD user-type tier gate | design spec'd | **in-flight** -- MCPGUARD decomposing; PREMCP Class-A token-lifecycle is a P0 workstream |
| 3 attribution | COMPTEAM signature-verified root-of-trust (same as SCTY tier-model identity) | design spec'd | **in-flight** -- COMPTEAM identity substrate building |
| 4 strip | COMPTEAM strip-list kit (fail-closed gate) | spec'd (COMPTEAM SS2) | **in-flight** -- COMPTEAM A1 strip-list gate |
| 5 propose-only | adapter-local default (no external dep) | yes | S3 |

**Sequencing flag (to COO~B + SCTY lane / base COO):** S1 (this DESIGN) is interface-unblocked -- all 4 dependency PRDs exist and specify the interfaces I bind to. But **S3 (the adapter BUILD) has a hard dependency on the IMPLEMENTATIONS of controls 2/3/4 being available**: PREMCP token issue/verify + MCPGUARD tier-gate API + COMPTEAM sig-verify primitive + the strip-list module. S1/S2 can proceed now; **S3 build should sequence after (or co-schedule with) SCTY_MCPGUARD's tier-gate + PREMCP's token-lifecycle + COMPTEAM's sig-root/strip-list landing** -- else S3 designs against a spec whose implementation isn't callable. Recommend the CTO/COO sequence S3 against those landings; I'll design S3's control-2/3/4 call-sites against the specified interfaces and gate the BUILD on their availability.

## 10. The 5 CTO arch-gate points (= S1 acceptance) + CVO live tests (S4)
1. **Partition provably-scoped (control 1):** fleet-B DENIED `ReceiveMessage` on fleet-A's inbound (live IAM/SQS, not TF-desired).
2. **Attribution provably-signed (control 3):** forged/absent signature REJECTED; valid resolves the true `from_employee+from_agent`.
3. **Strip fail-closed (control 4):** planted secret/ARN/internal-path redacted/blocked (known-bad passes the gate); clean message flows.
4. **Action-vs-data authz (controls 2+5):** an ACTION-request without a PREMCP entitlement DENIED; a DATA-share flows read-only; nothing mutates cross-boundary without the authz path.
5. **One choke point, all fail-closed (composition):** all 5 apply at the adapter; the intra-fleet path is unchanged; each control's failure mode is deny/block/reject.

## 11. Open questions for the CTO arch-gate
- **Q1 (control 4 redact-vs-block policy):** which strip-list hit-classes REDACT (drop the field, deliver the rest) vs BLOCK (drop the whole message)? Proposal: secrets/creds/ARNs -> BLOCK (a partial leak is still a leak); internal-hostnames/bucket-names -> REDACT; firm-PII -> BLOCK. CTO to rule.
- **Q2 (control 2 receiver-adjudication shape):** for an authorized ACTION, is the receiver-side adjudication a human confirm, a tier-gate (MCPGUARD confirm-on-irreversible), or an agent-auto within cap? Proposal: tier-gated per MCPGUARD (confirm-on-irreversible always; auto within blast-cap otherwise).
- **Q3 (signature primitive):** does control 3 reuse the SCTY RS256 signing (PREMCP's key) for the attribution signature, or a distinct COMPTEAM identity key? Proposal: the COMPTEAM sig-root (identity) -- distinct from PREMCP (entitlement) -- to keep WHO-you-are separate from WHAT-you-may-do.
- **Q4 (collaboration lifecycle):** who creates/tears-down a queue-pair + its KMS key + the two-principal grants (a collaboration onboarding step)? Likely an S2/AE + a consent gate -- flagging for the CTO/COO to home.
