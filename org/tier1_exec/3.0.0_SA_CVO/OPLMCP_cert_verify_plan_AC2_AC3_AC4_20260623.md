# NFRA_OPLMCP -- CVO cert verify plan (AC2 / AC3 / AC4)

**Author:** 3.0.0_SA_CVO | **2026-06-23** | **Owns (PRD S9):** per-user-scope + kill-switch + audit verify.
**Trigger:** CTO heads-up 160610Z -- IT app-reg creds delivered + stored (opal/mcp/m365-login + opal/mcp/m365-graph); OPLMCP.02 (real-Graph go-live) unblocked; AE drives OIDC swap + EC2 code-deploy + MOCK_GRAPH=0 + live /me. Execute on CTO's ".02-reaches-live-Graph" signal.
**Standard:** the hardened render/security cert -- walk the REAL user's LIVE wire-protocol path on the DEPLOYED system, to the proof; a proxy (Andrew's own creds / mock-Graph / simulated header / source-read) is necessary-but-INSUFFICIENT. grounding: SOURCE-CONFIRMED against the live deployed gateway, never a self-report.

---

## Cert scope
MINE (hard gates): **AC2** (per-user-scope -- the load-bearing security correctness), **AC3** (kill-switch + blocklist), **AC4** (audit). AWARENESS (not mine, but gate-coupled): AC1 (infra/in-repo/EC2_MANIFEST/Terraform/comp-graph = AE), AC5 (Claude-for-Work data-terms sign-off = CTO/OPLMCP.05 -- SEQUENCING-COUPLED to my AC2, see Dependencies), AC6 (Verified-Access JWT TODO implemented-or-waived).

## CTO rulings (161337Z) -- final cert scope (plan endorsed)
1. **AC5<->AC2 unblocked via SYNTHETIC mailboxes:** run AC2 on test mailboxes seeded with DISTINCT synthetic mail (A vs B). Proves per-user-scope isolation (A cannot read B's) WITHOUT egressing real M365 content -> the AC5 real-content-egress concern is NOT triggered; AC2 is NOT blocked on AC5. AC5 (data-terms RECORD, CTO/.05, Andrew attests) stays REQUIRED before any REAL non-Andrew/real-mail onboarding (production), recorded/in-flight before I read any real mailbox. **Cert on synthetic; gate real-onboarding on AC5.**
2. **Test users (Dep-1):** CTO surfacing to Andrew/IT now (IT lead-time) -- 2 non-Andrew M365 test mailboxes (A+B) in tenant 6810043e-..., synthetic-seeded; min = 1 non-Andrew + Andrew-as-the-other. Instrument in hand before the signal.
3. **KILL_WRITE = OPLMCP.04, NOT v1.** My AC3 v1 bar = global KILL_SWITCH + per-user blocklist only. KILL_WRITE / write-posture (S11.4) certs at .04.
4. **AC4 v1 bar = ON-BOX audit.jsonl** (every call -> user + redacted args, no body leak -- the security check). Lake/Athena reach = .05, gates the MACRO-close NOT the .02 go-live (separate .05 cert).

**Execute trigger:** CTO's ".02-reaches-live-Graph" signal; CTO confirms AC5-in-flight + test-users-provisioned before I touch a mailbox. Authed-MCP-session mechanics worked out with ~B (fresh OPLMCP AE lane) at execute.

## AC2 -- per-user-scope (THE non-negotiable: "shared server, NEVER shared identity")
**INSUFFICIENT proxies (must NOT cert on these -- the COT empty-page lesson):**
- Andrew's own creds (he's the app owner -- not a per-user-scope test).
- MOCK_GRAPH=1 (canned Graph -- must be MOCK_GRAPH=0, live Graph).
- A simulated identity header (the proven front-end leg used one -- proves PROPAGATION, not real Entra per-user enforcement).
- Reading the code/middleware (proves intent, not live enforcement).

**The real proof (on the deployed ALB+OIDC gateway, MOCK_GRAPH=0):**
1. A REAL non-Andrew Entra user (User A) authenticates at mcp.opalinvest.dev against Entra (ALB authenticate-oidc) -> OIDC succeeds -> identity propagates to the gateway.
2. A calls `/me` -> returns A's identity (not Andrew's, not a shared/app identity).
3. A calls `/outlook` (list mail) -> returns ONLY A's mail.
4. **CROSS-USER ISOLATION (the load-bearing assertion):** A demonstrably CANNOT reach another user's data. Strongest proof = TWO real users (A + B): A sees only A, B sees only B, neither reaches the other. Minimum = one non-Andrew user + confirm it cannot reach Andrew's mailbox (no app-only/tenant-wide path).
5. **CONCURRENCY identity-bleed (the S2.7 pure-ASGI invariant, the technical reason the stance holds under load):** two users calling CONCURRENTLY each get their OWN data -- no identity bleed across requests (BaseHTTPMiddleware would drop contextvars; pure-ASGI is required). Verify the live gateway is pure-ASGI in effect: concurrent A+B calls never cross identities in the response OR the audit.

**Instrument:** Playwright for the real Entra OIDC browser-auth at mcp.opalinvest.dev (the COT jane/john pattern), then drive the MCP tool calls as the authed user; exact authed-MCP-session mechanics worked out with AE at execute-time. Ground every assertion on the LIVE response + the audit line, never the code.

## AC3 -- kill-switch + per-user blocklist (reversible, LIVE)
1. **Global KILL_SWITCH:** trip it (AWS-side -- SSM Param Store / S3, hot-reload per S11.3; NO SSH/SSM-session into the box) -> confirm ALL users' tool calls halt (denied + audited) -> reverse -> confirm restored.
2. **Per-user blocklist:** add User A -> confirm A denied while User B continues (the discriminator: ONE blocked, OTHERS continue) -> reverse (remove A) -> confirm A restored. Hot-reload, live.
3. **(If in v1 bar) KILL_WRITE per-capability kill (S11.4):** writes disabled fabric-wide -> reverse. Confirm whether this is v1-cert or OPLMCP.04-scope.
All tripped on the LIVE gateway + observed via real tool calls -- not asserted from the middleware source.

## AC4 -- audit (user + redacted args, lake-queryable)
1. Make calls as different users -> EACH lands in `audit.jsonl` with the CORRECT user (UPN/oid) + tool + outcome + ts.
2. **REDACTION (a security check on the audit itself):** sensitive args (mail bodies, tokens, content) are REDACTED -- the audit must not itself leak M365 content. Confirm bodies are redacted, not clear-logged.
3. **LAKE reach:** audit reaches the lake / Athena-queryable (OPLMCP.05 routes it). Confirm the v1 bar -- is lake-reach gating the macro-close, or is on-box audit.jsonl AC4's first pass with lake-routing staged to OPLMCP.05?

## Dependencies + sequencing (surface EARLY -- avoid a verify-time scramble)
1. **REAL non-Andrew Entra test user(s) -- the AC2 non-negotiable instrument (COT jane/john equivalent).** Need >=1 non-Andrew M365 mailbox in the tenant (6810043e-...); ideally 2 (A+B) for the cleanest cross-user-isolation proof. WHO provisions = Andrew/IT (real tenant mailboxes or test accounts). This is the single most important dependency -- flag to CTO/Andrew now.
2. **MOCK_GRAPH=0 + a live `/me` confirmed by AE** (AC2 requires real Graph). I execute only post-.02-live.
3. **AC5 (data-terms sign-off) is SEQUENCING-COUPLED to AC2.** S8/S6: AC5 recorded "before any non-Andrew onboarding"; my AC2 test = a non-Andrew user reading real mail = M365 content egresses to the Anthropic API (via the Claude session running the verify). So AC5 (CTO/OPLMCP.05) should be recorded -- OR a dedicated test mailbox with synthetic content + AC5 explicitly acknowledged in-flight -- BEFORE I run the non-Andrew live-mail read. CTO (AC5 owner) rules the ordering.
4. **Audit-to-lake (OPLMCP.05)** for AC4's lake-reach leg.

## Verdict shape
Per-AC PASS/FAIL with grounding: SOURCE-CONFIRMED (the live deployed gateway response + the audit line cited), reserved words only on source-confirmed. AC2 is the gate-of-gates: no macro-close without the real non-Andrew cross-user-isolation proof on live Graph. RAVC CTO+COO at the verdict.
