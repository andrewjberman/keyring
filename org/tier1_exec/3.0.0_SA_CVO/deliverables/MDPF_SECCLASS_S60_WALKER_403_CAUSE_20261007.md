# MDPF_SECCLASS row S60 -- why the advisor Book view answers 403 on the laptop: the dev server's proxy, not the walker

**archetype:** DIAGNOSE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~17:2xZ, on `0.0.0_AB_MSTR` msg 106448 (bus 4e8eed02, from
`1.0.0_SA_CTO~DELL1`). A FILE for dell1; no row is minted here. No new login was made for this read and no token was
handled.

## Answer

**The 403 is not the walker's role, scope or token, and not the candidate. The laptop's dev server sends
`/api/scoped/partners/*` straight to the API Gateway, and the portal authorizer refuses any request that did not come
through CloudFront.** Any user on the local dev build gets the same refusal on the advisor Book view. This seat's
earlier file (@b207496c40) left the cause open; `1.0.0_SA_CTO`'s ruling 106394 read it as the walker's access. Both
are superseded by the measurement below.

## The measurement

1. **The authorizer's own log** (`/aws/lambda/opal-portal-authorizer`, read-only, any token text withheld), for the
   seconds of this seat's probe walk:
   - 16:05:31Z and 16:05:32Z, two page reads: "Token verified successfully: { email: 'opal-ui-walker@opal.test',
     tier: 'internal', role: 'admin', userType: 'Dev' }", then "User is Dev superadmin - granting ALL access", then
     "Authorization context: { ... allowedFirmIds: 'ALL' }".
   - 16:05:40Z and 16:05:41Z, the two probes of
     `/api/scoped/partners/books/advisor/dawson_moses/platinum-summary` (with and without `?firm=bd`):
     "Authorizer invoked", then **"Origin verification FAILED - request did not come through CloudFront"**. No token
     line follows: the request is refused before the token is read.
   - The walk that pressed the advisor (16:02:56Z to 16:02:57Z): 3 such lines, one per refused Book read.
   - Whole day to 17:25Z: 5 "Origin verification FAILED" lines, all five this seat's.
2. **The dev server's proxy** (`C:\tmp\portal-5174\vite.config.ts` at `fc18e50b`): `/api/scoped/advisor-intelligence`
   targets `https://d2n2nzpeqf34ge.cloudfront.net` (line 102-104); `/api/scoped/partners` targets
   `https://7k3ed8px20.execute-api.us-east-1.amazonaws.com` (line 142-143), the API Gateway itself. That is why the
   firm-level reads answer 200 and the Book read does not.
3. **The route** (`infra/aws/terraform/shared-infra/apigateway-portal/routes.tf:171-176`, `main.tf:43-51`): the
   advisor `platinum-summary` route sits behind the CUSTOM authorizer `opal-portal-authorizer`. Its simple-response
   denial is API Gateway's `{"message":"Forbidden"}`, the 23 bytes the page received.

## What dell1 asked to be recorded

| asked | value | source |
|---|---|---|
| role | admin (present) | the authorizer's "Token verified" line |
| tier, userType | internal, Dev | the same line |
| firm scope applied | allowedFirmIds 'ALL' ("Dev superadmin") | the authorizer's context line |
| firmId | opal-capital | the account's row in `opal-users-v2` (the authorizer does not print it) |
| advisorId | none on the row | the same row |

The token itself was not decoded: the walker keeps no session between walks (each walk arms, signs in and disarms), so
there is no existing token to read without a new login. The authorizer's verified claims are the same facts from the
verifier's side.

## What follows, and what does not

- **For SC10-e59-AC2:** a client page cannot be rendered on the local dev build by anyone until the proxy sends
  `/api/scoped/partners` through CloudFront, or the render is made on the deployed DEV site. The walker refuses any
  base that is not localhost, so the second route is not the walker's.
- **For "Andrew's read":** on the deployed site his requests go through CloudFront, so this refusal does not apply
  there. Whether the deployed Book view loads for him was NOT read here. On the local dev build he would get the 403.
- **Not established:** when the authorizer's origin check and the proxy target diverged; `vite.config.ts` last moved on
  2026-09-15. Whether the scoped API, once reached, serves an opal-capital admin a 49 Financial book.
- Owner of the proxy line: the portal's owner; a frontend file, so its change is a portal candidate with a review.

-- 3.0.0_SA_CVO
