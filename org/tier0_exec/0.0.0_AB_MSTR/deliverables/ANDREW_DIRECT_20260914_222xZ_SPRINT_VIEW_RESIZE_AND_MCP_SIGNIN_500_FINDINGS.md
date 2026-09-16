# ANDREW-DIRECT 2026-09-14 ~22:0xZ-~22:2xZ -- why the sprint link does not resize; why mcp sign-in returns 500

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal · **Recorded:** the same turn, with the findings.

## VERBATIM

> "something I want to understand is why does the daily sprint not automatically resize based on mobile or desktop
> viewer when im viewing the presigned link? look into that."

> "Interesting also need to understand why we get a 500 server error when signing in post authentication via the mcp
> subdomain."

Both are asks to investigate. Nothing was changed in infrastructure or in the report templates on these words.

## FINDING 1 -- the presigned link is two fixed layouts picked once, not one page that reflows

- The chooser (`daily-reports/latest/index.html`, written by `publish_daily_report.py` `_chooser_html`) runs a single
  `location.replace` at load: a phone or touch device goes to the Mobile page, everything with a mouse to Desktop.
  Nothing re-picks on a window resize or a phone rotation.
- The two pages are separate designs. Measured in a browser at 1280 / 1024 / 900 / 390 px:
  - Desktop page: fits at 1280, 1024 and 900 (it stacks below 940 px). At 390 px it overflows sideways, 586 px of
    content in a 386 px window: the card rail and the no-wrap lines stick out.
  - Mobile page: fits at 390 px; at every desktop width it stays a 520 px column, by design.
- So a Desktop page on a narrow window, or a Mobile page on a wide one, never adapts. The /sprint route on
  mcp.opalinvest.dev adds a one-way hop (desktop to mobile under 700 px) but also never goes back.
- The durable fix is one page carrying both layouts with CSS choosing at every width. That is the report template,
  which is the CTO's frozen design surface, so it is a proposal, not an act of this seat.

## FINDING 2 -- the 500 is the load balancer timing out on Microsoft's token endpoint

- ALB access log (`s3://opal-data-security/waf-logs/alb-opal-gateway/`, 2026-09-14): `/oauth2/idpresponse` returned
  **500 with error_reason=AuthTokenEpRequestTimeout** at 22:15:37Z, 22:15:43Z and 22:17:04Z, target `-` (the gateway
  was never reached). The 401s around them (`AuthInvalidStateParam`, `AuthInvalidAWSALBAuthNonce`) are the retries of
  a failed attempt.
- CloudWatch on `app/opal-gateway/89166a68f337e5a4`, 19:00Z-23:59Z: HTTPCode_ELB_500 = 3, HTTPCode_Target_5XX = 0,
  ELBAuthError = 3, ELBAuthFailure = 6, **ELBAuthSuccess = 0**, ELBAuthUserClaimsSizeExceeded = 0.
- Cause: the ALB security group `sg-02571ff2f33d2f9d4` allows ONE egress rule, tcp 8080 to 172.31.0.0/16 (the
  gateway). Declared that way in `infra/aws/terraform/opal-gateway/alb.tf:37-43` and applied that way live. With
  authenticate-oidc the ALB itself must call the IdP token endpoint over HTTPS, and no egress rule allows it.
- What it is NOT: the redirect URI. Microsoft accepted it and returned the user with a code (the callback reached the
  ALB). Not the gateway code either: `sprint_view.py` never returns 500, and the identity check turns every failure
  into a 401.
- Fix (proposed, not applied): one egress rule on the ALB SG, tcp 443 to 0.0.0.0/0, in `alb.tf`, applied with
  `safe-apply` under a change-management entry. That widens egress, so it is Andrew's call and an infrastructure
  lane's act.
