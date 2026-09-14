# Menachem Claude requirements brief review -- 0.7.0_AE_CloudOps

**archetype:** REVIEW
**Date:** 2026-09-14
**Task Order:** Andrew-direct review of exact DOCX; verbatim request appended to ANDREW_DIRECT.md.
**Status:** COMPLETE as design review; no deployment or access grant.
**Window:** 18:41:23Z through 2026-09-14 18:49:36 UTC.
**Push state:** LOCAL. Measured origin/CLOUD: 6a5b276f8b382edca90673d1f425320a251ca0e5 (git ls-remote, ~18:48Z).

## Objective and result

Compare the exact Downloads/Claude_Remote_MCP_Requirements_Brief.docx against the existing Menachem Schwab specification. Read its complete body/table content and relationship links with the ZIP/XML parser. Hash: 87b0d6ea29020894169ab890d4c1885e1c0a7418c213c2f943a766b13d582e52. Original DOCX unchanged.

Keep the opal-gateway + account entitlement + scoped source-reader role architecture. Revision 2 incorporates a lower complete-response cap, explicit durable refresh-token rotation, front-door/authentication contracts, separate endpoint deadlines and more concrete onboarding/acceptance. Direct-Entra identifiers, Managed Auth and private tunnels are conditional alternatives, not new v1 prerequisites.

## Compiler Tools

| Tool | Command/scope | Result | Note |
| --- | --- | --- | --- |
| comp-which | DOCX/spec comparison, ALB/authentication source, precommit diff questions | PARTIAL | No curated match for first two; diff question ranked unrelated candidates. Used offered scoped comp-find fallback. |
| comp-find | requirements in owned deliverable directory | PASS | Measured zero before revision; not evidence of absent requirements in the DOCX. |
| comp-find | authenticate-oidc in infra/aws/terraform/opal-gateway | PASS | 19 hits across 22 scanned files; identified exact alb.tf forward rules. |
| comp-diff | Working-tree change impact | PASS/PARTIAL | Exit 0, 11 tracked changes; 3 owned spec paths and 8 unrelated shared changes. New evidence/review paths validated separately. |

**What worked:** exact DOCX parsing, official-source checks, scoped source inspection, account-guarded ALB Describe calls and unauthenticated public GETs. Bare compiler shims used.
**What failed:** no tool execution failure. Plain XML text concatenation initially hid Word line breaks; explicit w:br inspection confirmed the sample header is correctly separated. No formatting defect attributed to the document.
**Gap found:** source refresh handler mints replacements without consuming old refresh tokens; original chat byte cap could exceed Claude's character ceiling.
No production runtime, IAM policy, bucket or Terraform file changed.

## Deployment Sequence

| Step | Action | Result |
| --- | --- | --- |
| 1 | Sweep canonical exact-seat inbox root | No unread root Markdown messages. No new GO or peer work. |
| 2 | Read exact user DOCX and existing brief | Full body/table comparison; original file hash pinned. |
| 3 | Verify relevant current external contracts | Anthropic runtime/auth/network/setup/managed-auth/tunnel docs; RFC 9700 refresh requirements. |
| 4 | Inspect local gateway/ALB source | Hosted callback remains loopback-only; refresh source lacks old-token consumption; browser/MCP route split already designed. |
| 5 | Read live front-door metadata | Internet-facing IPv4 ALB; priority 10/20 MCP/OAuth forward rules; browser OIDC default; idle timeout 60s; access logging on. |
| 6 | Exercise unauthenticated HTTP only | /mcp 401 correct Bearer challenge at 93ms; discovery 200 at 110/109ms; no redirect. |
| 7 | Revise design artifacts and validate consistency | Limits 100000 characters AND 131072 bytes, revision 2 disabled profile, scope/CSV permissions unchanged; links/JSON/hash/diff checks pass. |
| 8 | Record and commit only owned paths | Review, evidence, spec/profile/request amendments and this log. No push, provisioning or outbound messages. |

## Evidence and limitations

requirements-review-evidence.json records live metadata and source blob hashes at HEAD 04dace74d68acd091a0115458694efb84a7413dd. Public probes came from this Codex seat, not Anthropic egress. Local resolver addresses were globally routable; this is not a separate public-DNS or real-Claude test.

No OAuth registration, token exchange, replay, authenticated initialization, user data query or download was performed. Source refresh findings are not claims of exercised production behavior or deployed source parity. Existing 41 policy simulations were not rerun: the draft IAM policy is byte-equivalent to the previous commit after newline normalization. No source customer rows, secrets or cookies were collected.

## Decisions and files

Changed SPEC.md, menachem-entitlement.proposed.json and ANDREW_DIRECT.md. Added REQUIREMENTS_REVIEW.md and requirements-review-evidence.json. This log is the sixth commit path. Source DOCX and draft IAM policy unchanged.

The revised brief is ready to guide implementation. Activation remains subject to implementation, exact initial data scope and real Claude acceptance. Original 4-7 day estimate is explicitly provisional pending durable token-state/migration scope. The user's review request grants no deployment or outbound-message authority; no repository peer broadcast sent under the higher-priority messaging constraint.

## Blockers, current state and next steps

No blocker to review completion. Return the revised brief and the concrete omissions to Andrew. Implementation has not begun. During an authorized build, address hosted callback, refresh lifecycle, data entitlement/query/export and the expanded acceptance cases together.

