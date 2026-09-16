# ANDREW-DIRECT 2026-09-15 ~02:4xZ -- ALB egress rule yes; sprint one-page rework to CTO~A; push and merge held

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal · **Recorded:** the same turn it was given.

## VERBATIM AND ENTIRE

> "Yes to 1., Regarding 2, yes sure hand that off to CTO~A as they're idle. Regarding 3, ill let you know when to push
> + Call 4 Merge I will let you know as well, better to do it in a quiet period where we're not actively working."

It answers the four decisions this seat put to him, numbered as he read them:

1. "Firewall rule: allow the load balancer outbound HTTPS, so sign-in at mcp.opalinvest.dev stops returning a 500?"
2. "Report page: have the CTO rework the daily report into one page that fits any screen?"
3. "Push: push the local CLOUD commits to origin?"
4. "Merge into site Z: merge CLOUD into site Z's branch?"

## WHAT IT RULES, NO WIDER

1. **YES, the ALB egress rule.** One egress rule on the opal-gateway ALB security group `sg-02571ff2f33d2f9d4`, tcp 443
   to the internet, so authenticate-oidc can reach the IdP token endpoint (finding and evidence:
   `ANDREW_DIRECT_20260914_222xZ_SPRINT_VIEW_RESIZE_AND_MCP_SIGNIN_500_FINDINGS.md` @f6d71f6b29). Routing is
   `1.0.0_SA_CTO`'s, by its own 96785 ("if Andrew says go on the ALB egress rule, the routing to the infra lane is this
   seat's; I will cut it the turn his word lands"). The change goes in `infra/aws/terraform/opal-gateway/alb.tf` via
   `safe-apply` with a change-management entry. This seat does not apply it and does not write the infra lane.
2. **YES, the one-page sprint rework, handed to `1.0.0_SA_CTO~A`.** Replace the two fixed layouts picked once at load
   with a page that fits any screen live. The finding is in the same record. The surface is the report template
   (`daily_reports/templates/`), the presign chooser (`daily_reports/scripts/publish_daily_report.py` `_chooser_html`)
   and the gateway's one-way hop (`infra/aws/ec2/opal-gateway/app/sprint_view.py` `_HOP_SCRIPT`). `1.0.0_SA_CTO` owns
   the template and is copied.
3. **PUSH HELD** until his word. origin/CLOUD stays at `6a5b276f8b`; LD-0522 cadence.
4. **CLOUD -> SITEZ MERGE HELD** until his word, "in a quiet period where we're not actively working". The `/integrate`
   assessment, the portal integration plan (authored by `0.0.0_AB_MSTR~Z`) and the naming-schema drift stay measured
   and waiting.

## BROADCAST

`1.0.0_SA_CTO` and `1.0.0_SA_CTO~A` over the broker; `0.0.0_AB_MSTR~Z` over the agentbus, for items 3 and 4.
