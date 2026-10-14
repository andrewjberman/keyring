# /yearinreview -- open to all Opal employees (Andrew-direct 2026-10-14 ~22:2xZ, 4.0.0_SA_CRO~Z session)

## VERBATIM

> "where is this viewable at, mcp.opalinvest.dev/yearinreview? I need it viewable by all opal employees"

(Same session, minutes earlier: "i need it live now".)

## What changes

The viewer gate today is the owner-only roster (`YEARINREVIEW_VIEW_ALLOWED_EMAILS`, fail closed on empty; Andrew-direct
2026-10-05, record @121b7b016e). This word replaces that: every Opal employee may view the page.

One function, `infra/aws/ec2/opal-gateway/app/yearinreview_view.py` `_allowed()`:

```python
def _allowed(email: str) -> bool:
    # Andrew-direct 2026-10-14 ~22:2xZ: "I need it viewable by all opal employees". Any Opal-domain identity that is not
    # guest-form (#EXT#) is admitted -- the same predicate the gateway's Opal-users gate uses (tools._is_opal_user).
    # The roster still admits anyone listed on it; an empty roster no longer denies Opal staff.
    from .tools import _is_opal_user
    roster = _cfg.YEARINREVIEW_VIEW_ALLOWED_EMAILS
    return _is_opal_user(email) or (bool(roster) and email in roster)
```

- Who can read after: any signed-in `@opalinvest` identity (not a guest); unchanged behind the ALB authenticate-oidc
  action and GuardMiddleware identity. Non-Opal and guest identities: 403 as today.
- No route, IAM, `.env` or tool change. The 403 text "Not on the Year in Review roster." stays for non-Opal callers.
- Ship in the SAME release as OG-yr-1 (one deploy), with a test: an Opal address admitted on an empty roster; an
  `#EXT#` guest and an outside domain refused.

-- 4.0.0_SA_CRO~Z
