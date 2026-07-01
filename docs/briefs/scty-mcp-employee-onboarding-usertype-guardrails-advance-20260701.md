# SCTY — MCP employee-onboarding: user-type action-guardrails + advance-defense-now (Andrew-direct 2026-07-01)

**Author:** 0.5.0_AE_OpalETL | **Sovereign:** Andrew | **Issue-to:** 1.0.0_SA_CTO (owns the SCTY PRDs) | **CC:** 2.0.0_SA_COO (/security lane + decomposition owner), 3.0.0_SA_CVO (verifier-not-fixer)
**Date:** 2026-07-01 | **Type:** assessment + Andrew-refinement capture → fold-into-PRD ask (NOT a unilateral PRD edit — mirrors the 973fafc53 flow where the CTO folded Andrew's server-layer ruling)

---

## 0. Andrew-direct trigger (verbatim intent)

> "We are about to start bringing Opal employees onto MCP, which means we need to create a guardrail system for actions (relying on **user type**, keep me as **master admin at andrew@opalinvest.com or systems-level user**). Also probably time to **advance the SCTY projects to bolster defense in advance** in case somebody does something dumb and downloads a virus then has MCP access. Assess current status … update those briefs and issue to CTO."

Two purposes: **(A)** a user-type-based action-authorization/guardrail system for incoming employee MCP users, Andrew preserved as master-admin; **(B)** advance the SCTY defense projects NOW (pre-onboarding) against the compromised-employee-endpoint-with-MCP-access threat.

---

## 1. Assessment — current status (grounded: JSONs + PRDs + `git log` + `/security` tree, 2026-07-01)

The design substrate for BOTH purposes already exists and is well-architected — but the **build is stalled at "GO held for Andrew's review,"** and it is **phased as "later," which the onboarding trigger now inverts.**

| Project | What exists (DONE) | State | Blocker |
|---|---|---|---|
| **SCTY** (umbrella macro) | PRD `SCTY_PRD.md` (cc940ab0f) + REGISTRY + charter; 4 workstreams; W1 agent-supply-chain-control TO + W2 own-attack-surface self-assessment tasked to 0.7.0~B (`/security/own-attack-surface/`, `/self-assessment/` present) | active, PHASE 0 | paces alongside hot priorities; no hard blocker |
| **SCTY_PREMCP** (AUTH / perimeter layer — *who may connect, token soundness*) | PRD `SCTY_PREMCP_PRD.md` (53699876b); 8 risk-classes A-H → 3-phase resolutions; Phase-1 TOs P1a (token-revocation) / P1b (VA-sig verify=False) / P1c (/otp) / P1d (rotation-SOP) defined; /otp Option-A ruling arch-GO'd; NFRA_MSGRAPH-S2 reference-consumer perimeter items captured (253edaaa2) | active, PHASE 0 | **"Andrew-GO'd decomposition pass" HELD**; TO-P1a dispatched to 0.7.0 but 0.7.0 consumed by ETFS/STEP-C fires → not executed |
| **SCTY_MCPGUARD** (SAFETY / action layer — *how much can one authorized call destroy*) | PRD `SCTY_MCPGUARD_PRD.md` (0019b1743); 6 guardrails G1-G6 (G1 blast-radius cap = "delete-the-whole-OneDrive stopper"); contain-don't-classify; S0 destructive-surface-enum TO authored (06e08bf26); Andrew server-layer-scoping ruling integrated (973fafc53) | **decomposing** | **"GO held for Andrew's PRD review"**; S0 not GO'd, G1-G6 not cut |

**Bottom line:** ~80% of the design for both of Andrew's purposes is already on paper and cross-referenced. The gap is **(i) execution is GO-held on Andrew, (ii) the phasing treats guardrails as post-onboarding "later," and (iii) a user-TYPE/role-tier policy model — the specific thing Andrew just asked for — is under-specified in both PRDs.** This brief releases (i), inverts (ii), and specifies (iii).

---

## 2. GAP-1 (the new ask): a USER-TYPE / role-tier authorization model — currently absent

Neither PRD models user *types*. Grounded:
- **MCPGUARD §4** handles multi-user as *"incoming users get conservative DEFAULT caps; an elevated cap is an explicit per-user grant."* → **per-user cap grants, not typed roles.**
- **PREMCP** handles *per-CONSUMER* read-vs-write capability scoping (Andrew's 06-26 server-layer ruling). → **per-consumer, not per-user-role.**

Andrew's ask adds a **role-tier POLICY layer that parametrizes BOTH existing layers**: a user's *type* determines both their PREMCP gateway capability-scope AND their MCPGUARD cap/confirm profile. Proposed tiers (CTO to formalize):

| User-type | Identity | PREMCP capability scope | MCPGUARD cap/confirm profile |
|---|---|---|---|
| **MASTER-ADMIN / systems** | `andrew@opalinvest.com` (+ designated systems/service identity) | full delegated envelope (read+write, all resources) | elevated/unbounded caps; confirm-on-irreversible still on (safety, not authz); full audit |
| **STANDARD employee** | onboarding Opal staff | least-privilege default; write only where role needs it | conservative default caps (G1), confirm-on-destructive (G3), reversibility-first/no-permanent-delete (G4) — the OneDrive-stopper posture |
| **READ-ONLY / service-derive** | ingestion consumers (e.g. NFRA_MSGRAPH derive) | read-only gateway capability (Files.Read.All, never ReadWrite) — destructive *impossible* at permission layer | N/A (no write surface reaches the guard) |

**Why this is a clean fold, not a re-architecture:** MCPGUARD §4 already has the "elevated-cap-is-an-explicit-grant" primitive — Andrew simply IS that grant, and everyone else defaults conservative. PREMCP already has per-consumer scoping — user-type is the parametrization key. The addition is a **single user-type→(scope-profile, cap-profile) mapping table** consumed by both layers, resolved from the gateway's already-verified OIDC email claim (`app/identity.py` ES256-verified `x-amzn-oidc-data`). **Master-admin = andrew@opalinvest.com preserved as the sovereign identity, exempt from employee caps by tier, not by per-call exception.**

---

## 3. GAP-2 (the new ask): advance-in-priority — "later" is now "gating, do-before-onboarding"

Both PRDs currently say guardrails are *"S5-phased / aligned to NFRA_MSGRAPH S6 multi-user / not blocking."* The onboarding trigger **inverts this**: the moment non-Andrew employees hold MCP write-capability, the guardrails are the **gating dependency for safe onboarding**, and the compromised-endpoint threat (Andrew's "downloads a virus then has MCP access") is live. Recommended **do-before-onboarding minimum bar** (pull these forward from "later"):

1. **User-type model (GAP-1)** — the tiering table + master-admin pin. *(Prereq: everything else keys off it.)*
2. **MCPGUARD Phase-1** — S0 destructive-surface enum → G2 classification gate → G1 blast-radius cap → G4 reversibility-first (deny permanent-delete). PRD §5 already calls these three "make the headline catastrophe structurally impossible."
3. **PREMCP Phase-1 highest-standalone-gaps** — P1a token-revocation (a compromised endpoint's leaked refresh token needs a kill path — *directly* the virus-scenario) + the read-only-scope-token B2 (destructive-impossible for read consumers).
4. **G6 audit/alert on destructive calls** — so a compromised-endpoint mass action is loud within seconds.

Everything else (G3 confirm, G5 anomaly/rate-limit, PREMCP P1/P2 network/WAF/broker) stays fast-follow but is not a hard onboarding gate.

**The compromised-endpoint threat maps cleanly onto the existing "contain-don't-classify" axiom:** a virus driving the user's own authorized MCP session is *identical* at the guard to the hijacked-agent case MCPGUARD already contains — no new mechanism needed, it just must be BUILT and TIERED before employees arrive.

---

## 4. ASK to CTO (fold + drive)

1. **Fold GAP-1 (§2)** into `SCTY_MCPGUARD_PRD.md` (§4 access model) and `SCTY_PREMCP_PRD.md` (B-class entitlements) — add the user-type→(scope,cap) tiering table as the shared parametrization; pin `andrew@opalinvest.com` as master-admin/systems tier. Same integration flow as your 973fafc53 server-layer ruling.
2. **Fold GAP-2 (§3)** — re-phase the "do-before-onboarding minimum bar" in both PRDs' phasing sections; flip the guardrail build from "S5/later/not-blocking" to "gating for employee onboarding."
3. **Release the held GOs** — Andrew's message is the review-GO he was blocking on. Recommend authorizing COO to GO `SCTY_MCPGUARD.S0` + open the Andrew-GO'd PREMCP decomposition pass (P1a + B2 first).
4. **Confirm the lane** — S0/G1-G6 + read-only-scope-token are a CloudOps/AE gateway-surface build (0.7.0_AE_CloudOps owns the gateway; coordinate 0.8.0_AE_CloudComp who grounded the call-path). I (0.5.0_AE_OpalETL) can take a build lane if you want load spread off 0.7.0 (they're carrying ETFS/STEP-C) — your call on lane assignment.

**Not asking Andrew for anything** — his message supplied the trigger, the user-type intent, the master-admin pin, and the advance-priority directive. This is ready for CTO fold + decomposition.

---

## 5. Adjacent — workflow-scoping brief disposition (Andrew-direct 2026-07-01)

During assessment I surfaced `docs/briefs/oplmcp-workflow-scoping-20260624.md` (MSTR-owned design-riff: meter employee MCP gateway traffic → mine/rank → interview → synthesize candidate *workflows*). **It is NOT a security-guardrail artifact** — it shares the OPLMCP gateway + R8 audit-lake substrate but its purpose is workflow-mining, not action-authorization. **Andrew ruling (2026-07-01): workflow-scoping is effectively a COMPLEARN precursor — wrap it into NFRA_COMPLEARN (compiler-learning; ref `docs/briefs/nfra-complearn-brief-20260630.md`), AFTER these two guardrail projects (SCTY_MCPGUARD + SCTY_PREMCP) are handled.** Sequencing: guardrails FIRST (they gate employee onboarding); workflow-scoping folds into COMPLEARN as a follow-on. Recorded here so the disposition + ordering isn't lost; no action on it in this cycle.

---

*Grounded 2026-07-01 against: SCTY.json, SCTY_MCPGUARD.json, SCTY_PREMCP.json, SCTY_MCPGUARD_PRD.md, SCTY_PREMCP_PRD.md, `git log` SCTY, `/security` tree. No PRD was unilaterally edited (CTO-owned + /security-routing). Author: 0.5.0_AE_OpalETL.*
