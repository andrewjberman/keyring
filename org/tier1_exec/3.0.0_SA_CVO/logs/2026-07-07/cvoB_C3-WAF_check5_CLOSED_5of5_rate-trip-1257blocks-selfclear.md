# CVO~B C3-WAF check-5 CLOSURE — **rate-flood trip CONFIRMED (5/5).** Behavioral + metric, CVO-independent. C3-WAF fully exercised.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~1110–1116Z
**Subject:** the deferred check-5 (rate-flood behavioral trip) from cert `5b3090dbf`. AE~B ran the sanctioned flood (`~18k req/5min`, single IP) in a no-traffic window Andrew CLEARED directly (7am, zero live m365 traffic → my shared-IP concern moot in this window). I independently confirmed the trip + self-clear + metric.

## VERDICT: **CHECK 5 CLOSED — #0 rate-based trips + blocks at volume, confirmed independently. C3-WAF = 5/5** (all CTO checks CVO-independently exercised).

### Independent behavioral confirmation (not AE's curl)
- MY OWN `GET /` to the ALB during the block → **HTTP 403, server=awselb/2.0, no OIDC Location** = WAF-generated block page (not the app). The pre-flood baseline was 302 (OIDC redirect); the 302→403 transition is the #0 rate-based trip. Confirmed from my own request.
- **SELF-CLEAR:** armed a poll (`GET /` until 302); it flipped to **302 at 11:14:03Z** (~5 min after the flood stopped ~11:09Z) → the per-IP rate block auto-cleared. Self-healing as designed, independently observed.

### Independent metric confirmation (applied-truth) — with a dimension-label catch
- FIRST query `Rule=rate-based-ip` → 0 datapoints. I did NOT accept "0 = didn't block" (behavioral 403 said otherwise). `list-metrics` revealed the published Rule dimension is the WebACL-PREFIXED name `m365-mcp-gateway-rate-based-ip`, not bare `rate-based-ip`.
- Correct query: **BlockedRequests `Rule=m365-mcp-gateway-rate-based-ip` = 1257** (7 datapoints, peak 358/min) during the flood window → the #0 rate-based rule blocked 1257 requests. Authoritative applied-truth. `Rule=ALL` = 1293 (WebACL aggregate), consistent.

### BONUS — #1 ip-reputation confirmed block-ACTIVE (behavioral, beyond check-2 config)
BlockedRequests `Rule=m365-mcp-gateway-ip-reputation` = **36** during the flood → #1 ip-reputation is not just config-Block (check 2's override:None), it BLOCKED live. The vast majority (1257) is rate-based (confirming it's the volume-blocker); the 36 ip-reputation blocks independently corroborate #1's native-Block is live-active. Both BLOCK rules exercised.

### Proportionality validation (banked)
My own 403 during the block proves my egress IP was the SAME one AE flooded from → the per-IP block WOULD have rate-limited Andrew's live m365/Teams had he been using it. This VALIDATES the proportionality flag I raised (declining to self-initiate the flood) — it was correctly gated on Andrew's zero-traffic clearance, not a box-check. The right call held.

## Disposition — C3-WAF 5/5 CLOSED
1 association ✓ · 2 rule-actions ✓ · 3 redaction ✓ · 4 FP-safety (live m365 whoami) ✓ · 5 rate-trip ✓ (1257 rate-based blocks + my 403 + self-clear). All CTO checks CVO-independently exercised. The staggered flip-to-BLOCK for #2/#3 (COUNT >=3d/>=7d) remains a separate later re-cert. C3-WAF day-1 apply is fully certified.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| my own `curl GET /` (during + after block) | independent behavioral trip + self-clear | 403 (block) → 302 at 11:14Z (self-cleared) |
| `aws cloudwatch list-metrics` (rail-checked) | resolve the metric-0 dimension nuance | Rule label is prefixed `m365-mcp-gateway-rate-based-ip` |
| `aws cloudwatch get-metric-statistics BlockedRequests` (rail-checked) | applied-truth block count per rule | rate-based=1257, ip-reputation=36, ALL=1293 |

What worked: NOT accepting the first metric query's "0 datapoints" as "the rule didn't block" — the behavioral 403 forced me to investigate, and list-metrics exposed the prefixed-dimension label (the real metric had 1257 blocks). Sharpest-test-binds: my own 403 + the self-clear + the 1257-block metric each independently confirm the trip. And the shared-IP proportionality flag was validated by my own 403 — the deferral was correct, closed on Andrew's clearance. Gap: none — C3-WAF 5/5.

— 3.0.0_SA_CVO
