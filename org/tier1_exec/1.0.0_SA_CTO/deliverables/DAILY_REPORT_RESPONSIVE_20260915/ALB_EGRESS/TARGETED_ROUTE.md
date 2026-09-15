# Approved saved-plan route

Recorded by `1.0.0_SA_CTO~A` on 2026-09-15 after reading and acknowledging CTO Msg96877.

Authority: Andrew's item-1 approval in `cfcb13e03f`, CTO assignment Msg96866, and the explicit scoped-plan adjudication in Msg96877 from `1.0.0_SA_CTO` to `1.0.0_SA_CTO~A`.

Exact adjudication message: `20260915T035737Z_1.0.0_SA_CTO_GO__apply_the_saved_SG-only_plan__00715c.md` in this exact seat's canonical inbox (or its `read/` archive after completion).

The message authorizes applying the existing saved plan through `.tools/safe-apply.sh`, with SHA-256 `00715c0dac2a7f5481d06e8fd352ac247531f94681ae85feafe568207c9d5a2b`. It explicitly says: "Apply that saved file, not a fresh plan."

Scope is exactly 0 add, 1 in-place update, 0 destroy: `aws_security_group.alb`, egress only. Preserve TCP8080 to `172.31.0.0/16`; add TCP443 to `0.0.0.0/0`. Ingress is unchanged.

The two WAF IP sets `aws_wafv2_ip_set.opal_blocked_ips_regional_v4` and `aws_wafv2_ip_set.opal_blocked_ips_regional_v6` must remain untouched. Their description-only differences on empty sets are known, deliberately unapplied full-tree differences. The scoped postcondition is a security-group-only re-plan with no changes; no full-tree zero-diff claim is authorized or expected.

APPLIED requires live `describe-security-groups` evidence of both rules and the scoped zero-diff re-plan. Andrew and MSTR must then receive the retry link `https://mcp.opalinvest.dev/sprint`. EXERCISED separately requires Andrew's real sign-in, positive `ELBAuthSuccess`, and no `AuthTokenEp*` errors in the ALB log. This record does not claim either outcome before evidence is collected.

CLOUD push and CLOUD-to-SITEZ merge remain held.
