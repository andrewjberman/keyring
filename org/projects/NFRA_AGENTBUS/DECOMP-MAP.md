# NFRA_AGENTBUS -- DECOMP-MAP (COO~B, 2026-07-02)

**Charter:** MSTR DECOMP-GO (Andrew-greenlit 2026-07-02, LD-0239). PRD `docs/architecture/NFRA_AGENTBUS_PRD.md`.
**Shape (locked, do NOT re-litigate):** OWN project (NFRA_COMP* family peer) depending-on COMPTEAM + SCTY. NOT a COMPTEAM Workstream-C. Security-model-first.
**Lane:** COO~B, coordinating SCTY entitlements with base COO (SCTY_MCPGUARD/PREMCP `coo_lane = 2.0.0_SA_COO`).

## !! GOVERNANCE FENCE (MSTR-direct, honor EXACTLY) !!
> Decompose the **SECURITY-MODEL DESIGN phase ONLY**, under Andrew-direct-auth. **Do NOT author any TO that WIRES two real fleets / activates live cross-principal comms** -- that HOLDS for a NEW standing-access-class DIRECTIVE (S4-class, Andrew-only, NOT yet authored). Design/build/arch-gate TOs are in scope; **live cross-principal ACTIVATION is FENCED** pending the Directive.

**Operationalization of the fence in this decomposition:**
- S1 (design) is fully in-scope + dispatchable under Andrew-direct-auth.
- S2/S3/S4 are authored as **SINGLE-TENANT-SIMULATED build + verify ONLY** (PRD SS7: "design + a scoped single-tenant-simulated proof only"). NO two real employees' fleets are wired. Each carries a `<governance_fence>` block making the simulated-only boundary structural.
- **AB-ACTIVATE (wire two real fleets live) is NOT AUTHORED** -- it is explicitly held for the un-authored standing-access-class Directive. Documented below as a non-authored, fenced item so the gap is visible, not silent.
- **GO discipline:** S1 GO fires on plan-concurrence. S2-S4 GOs are HELD until (i) S1's 5-control model is CTO-arch-gated, and (ii) CTO+MSTR concur the simulated-build scope in the plan RAVC.

## The load-bearing framing (binding): THE SECURITY MODEL IS THE DESIGN
Cross-principal agent comms is a real attack surface (spoofed attribution, secret/PII egress, unauthorized cross-fleet action, cross-read of private traffic). A working transport with a weak security model is a FAILURE, not an MVP. Security-model-first: S1 gates S2-S4.

## The 5 controls (PRD SS3 -- each a fail-closed CTO arch-gate)
1. IAM + KMS per-employee partition (read own inbound ONLY).
2. SCTY-guardrail gated ACTION-vs-DATA (an action-request crosses a trust boundary -> the SCTY entitlement/tier authz gate).
3. Verified SIGNED from_employee+from_agent attribution (not a claimed serial -- hardens exact-serial vs spoof).
4. Egress content-strip / DLP (reuse the COMPTEAM strip-list; no secrets/PII/creds cross the boundary).
5. Default read-only / propose (incoming can REQUEST, never directly MUTATE).

## TO legs

| TO | Title | Owner | Fence status | Gate (blockedBy) | Cross-domain nodes |
|---|---|---|---|---|---|
| **AB-S1** | The 5-control security-model DESIGN spec | 0.4.0_DE_ClientPlatform (broker owner) + CTO arch-gate + SCTY-coord via base COO | **IN SCOPE** (design, Andrew-direct-auth) | SCTY_MCPGUARD tiers + SCTY_PREMCP token + COMPTEAM signature-root (coordinate, design against their interfaces) | SCTY_MCPGUARD; SCTY_PREMCP; COMPTEAM signature-root + strip-list; opal-agent-comms broker |
| **AB-S2** | SQS transport + IAM/KMS partition (SIMULATED) | 0.7.0_AE_CloudOps | **SIMULATED-ONLY** (no live cross-principal) | AB-S1 CTO arch-gate | IAM/KMS (comp-iam before/after); SQS (new); opal-agent-comms |
| **AB-S3** | Broker adapter = the 5-control choke point + tool_activity meter (SIMULATED) | 0.4.0_DE_ClientPlatform | **SIMULATED-ONLY** | AB-S1 CTO arch-gate | opal-agent-comms broker/adapter; tool_activity substrate (COMPLEARN-owned -- 2-project shared w/ TOOLHEALTH); COMPTEAM strip-list |
| **AB-S4** | CVO live verification on the SIMULATED proof | 3.0.0_SA_CVO | **SIMULATED PROOF ONLY** (verify controls on the single-tenant harness, not two real fleets) | AB-S2 + AB-S3 | live IAM/SQS/KMS state; the adapter; SCTY authz path |
| ~~AB-ACTIVATE~~ | ~~Wire two real employees' fleets live~~ | ~~n/a~~ | **FENCED -- NOT AUTHORED** | **The standing-access-class DIRECTIVE (Andrew-only, un-authored)** | -- |

## Cross-domain resource flags (wave protocol)
- **tool_activity substrate**: AB-S3's app-layer meter writes cross-employee rows into the SAME COMPLEARN-owned substrate NFRA_TOOLHEALTH queries. **2-project coordination event** (AGENTBUS + TOOLHEALTH). Flagged in AB-S3 + TOOLHEALTH TH-A/TH-B `<cross_domain_coordination>`. Substrate stays COMPLEARN-owned; AGENTBUS appends, does not fork.
- **opal-agent-comms broker**: AB-S1/S3 EXTEND it (adapter), never replace; the intra-fleet single-tenant path is UNCHANGED (regression gate in AB-S4). Appears in S1+S3.
- **COMPTEAM strip-list + signature-root**: control-3 (attribution) + control-4 (egress strip) ride COMPTEAM. Appears in S1+S3. COMPTEAM is active -> coordinate interface availability.
- **SCTY_MCPGUARD/PREMCP**: control-2 (action-vs-data authz). Appears in S1+S2+S4. SCTY_MCPGUARD is `decomposing`, PREMCP `active` -> S1 designs against the interface; live authz-gate wiring sequences behind SCTY availability + base-COO coordination.

## The leash carried in EVERY TO (PRD SS5 + SS8)
No unscoped channel (STOP-class); no cross-boundary mutation without the SCTY authz gate; egress strip fail-closed; signed attribution mandatory; ground on LIVE not TF-desired/self-report; security-model-first (S1 gates S2-S4); **AND the governance fence: single-tenant-simulated only, no live cross-principal activation.**

## Governance / Directive status
Cross-principal agent comms = a NEW standing access class (one principal's agents acting in another's collaboration space). PRD SS7 + MSTR: this warrants a dedicated Directive (pairs with COMPTEAM's standing-Directive question); **MSTR is surfacing it to Andrew.** Until ratified, AGENTBUS is Andrew-direct-authorized-not-a-standing-mandate, and the AB-ACTIVATE leg stays un-authored. COO~B tracks the Directive as the un-fence trigger.
