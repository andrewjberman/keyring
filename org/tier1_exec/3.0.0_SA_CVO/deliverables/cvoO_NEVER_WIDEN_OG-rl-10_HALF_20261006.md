# CVO never-widen half -- NFRA_OPLGTW OG-rl-10 (the r24 gateway HOTFIX, portal login) -- SIGNED

- **Seat:** 3.0.0_SA_CVO~O, 2026-10-06 ~23:48Z. Written during the fabric hold (`0.0.0_AB_MSTR~Z` msg 30374), on the
  carve-out the ask and the CTO half cite (`0.0.0_AB_MSTR~Z` msgs 30407-30418, not addressed to this seat) and the
  relay's statement that both fabrics hold behind this half (`1.0.0_SA_CTO~O` msg 30426).
- **Ask:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-10_20261006.md`
  @86dae82982 (branch `coo-o-oplgtw-r23`, read by object). COO half SIGNED in the ask; CTO half SIGNED @d274986e8d.
- **Release sha signed:** `9d3e2eb3fce3ceabbf06f6c1819451894291be05` (`rel-nfra-oplgtw-r24`), on live `2c27f3a795`.

## What this seat read itself (~23:4xZ)

1. `git rev-parse rel-nfra-oplgtw-r24` equals the release sha; its one parent is `2c27f3a795`; `EC2_MANIFEST.json`
   reads `deployed_commit` `2c27f3a795`.
2. `git diff 2c27f3a795 9d3e2eb3fc`, read whole: ONE file, `app/integrations/opal_portal/integration.py`, +6/-6.
   `AUTH_API_BASE = PORTAL_FRONT_DOOR` (moved below the constant it names); the `hosts` tuple drops the raw
   `7k3ed8px20.execute-api` host; two comments. No other line.
3. **Readers of the property.** Over `infra/aws/ec2/opal-gateway/app`, `AUTH_API_BASE` has one reader: `:137`,
   `httpx.post(AUTH_API_BASE + LOGIN_PATH, ...)` in `_PortalSession.token()`. A non-200 raises
   `IntegrationAuthError("portal login <code>")`, before and after. Every other call of this integration (`:231`,
   `:236`, `:266`, `:275`, `:282`) already posts to `PORTAL_FRONT_DOOR`, so no remaining call needs the dropped host.
4. **Does the front door carry the login?** The old comment said it did not. On a different plane from the worker's
   run: `infra/aws/terraform/portal-auth/cloudfront-distribution.tf:793-803` routes `/auth/*` to `APIGateway-portal`
   with POST allowed and no auth Lambda ("login/signup/refresh"). That is DESIRED state; the APPLIED evidence is the
   worker's on-host rehearsal with the real service secret (`login: OK` through `www.opalinvest.dev`, SSM 934f11e5,
   `ANNOUNCE_OG-rl-10.md` @601a6874e7). A real 200 is what tells the login handler from an edge validator; the
   bogus-credential 401 alone would not.
5. **Served output.** No dataset, route, grant or tool answer moves. The one behaviour change is the gateway's own
   service login going from 403 to its real answer.

## Signed for

- **The one property:** the host the `opal_portal` login is posted to. Writers: N = 1. Readers: N = 1.
- **Both branches:** 200 yields the service JWT and the upload tool proceeds; any non-200 raises `portal login
  <code>` as today and the release rolls back.
- **Egress narrows:** three allowlisted hosts instead of four; none is added.
- **Rollback:** redeploy `/c/tmp/og-rb17` at `2c27f3a795`.
- **Limit accepted as disclosed:** 63 of 72 test files not run for a one-file change.

## Conditions (each voids this half if unmet)

1. Live is re-read at the first act; if it is not `2c27f3a795`, re-cut and re-ask.
2. The post-deploy login is read from the INSTALLED code on the host (`RL10_LOGIN.json`), not from the rehearsal
   scratch; not OK rolls back in the same session.
3. The close read is `opal_data_refresh_upload(dry_run=True)` only. `confirm=True` is not run under this half: the
   real send is `0.0.3_BG_BBGTerminal`'s act on Andrew's word.
4. No grant, state-store, `.env`, secret, Terraform or IAM write. The held r23 set (`ba27a07439`) does not ship here,
   and this seat's half on `ba27a07439` (@d94f59af39) does not carry to its re-cut.

## Not signed, noted for the owner

What armed the origin gate between 12:44Z and 23:06Z is not established (the CTO half says the same). Any other
client that still posts to the raw auth host is refused the same way; that census is outside this release.

-- 3.0.0_SA_CVO~O
