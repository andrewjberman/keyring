# CVO~B C3-WAF behavioral cert (m365-mcp-gateway) — **PASS on checks 1-4** (applied + FP-safe, live-grounded). Check 5 (flood) = config-verified + behavioral-trip PROPORTIONALITY-DEFERRED (prod-user-impact risk).

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0937–0945Z
**Subject (independently grounded on live AWS, Rule 22a — not the AE ledger self-report):** WAFv2 WebACL `m365-mcp-gateway-waf` (id bd26daa0-...) on the internet-facing ALB `m365-mcp-gateway`. CTO 5-part behavioral scope. Day-1 apply cert (the flip-to-BLOCK is a separate later re-cert).

## VERDICT: **PASS (day-1 apply) — the WAF is correctly applied + FP-safe.** Checks 1-4 GREEN, live-exercised. Check 5 (rate-flood behavioral trip) = applied-config-verified; the flood exercise is PROPORTIONALITY-DEFERRED to a coordinated run (honest could-not-exercise, not a silent pass).

### CHECK 1 — WAF↔ALB association: PASS (applied)
`aws wafv2 get-web-acl-for-resource` on the ALB (`.../app/m365-mcp-gateway/62a54b61dc4634dd`, internet-facing) → returns `m365-mcp-gateway-waf` (bd26daa0-...). Associated live.

### CHECK 2 — rule ACTIONS: PASS (applied, matches CTO spec exactly)
`aws wafv2 get-web-acl` (REGIONAL, live):
- default action: **Allow**.
- #0 `rate-based-ip` → **Block**, RateBasedStatement limit **2000 / 300s / IP** ✓ (the one signature-independent active-block control).
- #1 `ip-reputation` → OverrideAction **None** = the managed IpReputation group's NATIVE actions apply = effectively **BLOCK** ✓ (correct WAFv2 idiom for "let the managed group block"; not overridden to Count).
- #2 `known-bad-inputs` → OverrideAction **Count** ✓.
- #3 `common-rule-set` → OverrideAction **Count** ✓, with EXACTLY the 3 spec'd exclusions set to Allow: `SizeRestrictions_BODY`, `CrossSiteScripting_BODY`, `NoUserAgent_HEADER` ✓ (protects 1MiB MCP JSON-RPC bodies / XSS-body / no-UA per 0.7.0~A's grounded request shapes).

### CHECK 3 — logging + redaction: PASS (applied; COUNT logs are credential-safe)
`aws wafv2 get-logging-configuration` (live): dest = `aws-waf-logs-m365-mcp-gateway` CW group; **6 RedactedFields**: authorization, cookie, x-amzn-ava-user-context, x-amzn-oidc-accesstoken, x-amzn-oidc-data, x-amzn-oidc-identity. So the COUNT-mode logs (which record matched requests for the flip-observation) never persist the auth/OIDC credentials — safe to rely on. ✓

### CHECK 4 — FP-safety (legit MCP + OAuth flows PASS): PASS (EXERCISED on real traffic)
Exercised a REAL legit m365 MCP flow through the WAF-protected gateway: `mcp__m365__whoami` → returned the signed-in profile (Andrew@opalinvest.com) successfully. This proves, on live traffic:
- a legit MCP JSON-RPC flow (custom Mcp-Session-Id / MCP-Protocol-Version headers, JSON body) PASSES the WAF (no false-positive block), AND
- the OAuth-authenticated flow works: the gateway is OIDC-protected (x-amzn-oidc-* headers), the call succeeded, and the x-amzn-oidc-* header REDACTION does not break the authenticated flow.
Corroborating: #2/#3 are COUNT (structurally cannot block), and #0/#1 don't trigger on a single legit low-rate request from a good IP → legit traffic is not false-positive-blocked. FP-safety confirmed.

### CHECK 5 — synthetic volumetric flood trips #0 rate-based: config-verified; behavioral trip PROPORTIONALITY-DEFERRED
- APPLIED-config verified (check 2): #0 is Block at 2000/300s/IP live — the rule is deployed to block volumetric abuse day-1.
- Behavioral flood-trip NOT self-initiated, on proportionality: the rate rule is PER-IP, and the m365 gateway serves Andrew's LIVE production m365/Teams traffic. If my gateway requests share an office egress IP with Andrew's live client, a 2000-request flood would rate-limit HIS production m365/Teams for the 5-min window — an outward-facing, user-impacting disruption to verify a control whose config is already applied-verified. Per the "confirm-first for disruptive/outward-facing actions + proportionality" discipline, I do NOT self-initiate a prod flood.
- RECOMMEND (routed to AE~B + CTO): run the flood-trip in a COORDINATED manner — confirm no shared-egress-IP with an active user (or run off-hours / from an isolated source IP / against a staging listener), then observe the 403 WAF-block when the limit trips. This is the one behavioral item; the day-1 apply cert does not gate on it (the rule is config-Block-verified). Honest could-not-exercise-on-proportionality — NOT a silent pass.

## Disposition
C3-WAF day-1 apply = PASS. The WAF is correctly associated, the rule actions match the CTO spec (BLOCK #0/#1, COUNT #2/#3 with the 3 exclusions), logging is credential-safe (6-header redaction), and legit MCP+OAuth traffic is not false-positive-blocked (exercised live). The one behavioral residual — the rate-flood trip — is config-verified and deferred to a coordinated exercise (shared-egress-IP prod-impact risk); it does not gate the day-1 apply cert. The staggered flip-to-BLOCK for #2/#3 (>=3d / >=7d COUNT observation) is a separate later re-cert.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-which "verify a WAF WebACL..."` | rail check for a WAF comp-tool | no fit (near-ties comp-freshness/comp-platinum) → raw aws sanctioned (rail-checked) |
| `aws wafv2 get-web-acl-for-resource` (live, rail-checked) | check 1 association | m365-mcp-gateway-waf associated to the ALB |
| `aws wafv2 get-web-acl` (live, rail-checked) | check 2 rule actions | #0 Block/2000/5min/IP, #1 native-Block, #2/#3 Count + 3 exclusions |
| `aws wafv2 get-logging-configuration` (live, rail-checked) | check 3 redaction | aws-waf-logs group + 6 auth headers redacted |
| `mcp__m365__whoami` (real MCP flow) | check 4 FP-safety, exercised | legit MCP+OAuth PASSES the WAF (no FP block) |

What worked: grounding every applied claim on the live wafv2 primitives (not the AE deploy-ledger), and exercising FP-safety with REAL m365 MCP traffic (a live whoami through the WAF) rather than a synthetic request. The proportionality call on check 5 — declining to self-initiate a prod flood that could rate-limit Andrew's shared-egress-IP live m365/Teams — is the honest CVO move: config-verify the rule + route the behavioral flood to a coordinated exercise, don't degrade prod to check a box. Gap: the rate-flood behavioral trip is deferred (config-verified); routed to AE~B/CTO for a coordinated run.

— 3.0.0_SA_CVO
