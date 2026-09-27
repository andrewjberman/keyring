# Andrew-direct 2026-09-27 ~19:5xZ at the 1.0.0_SA_CTO~O terminal -- two /open-calls answers

**Recorded by:** `1.0.0_SA_CTO~O`, the same turn.

## Verbatim

> call 1 yes rec approved. call 2, yes they did start adding MFA around then, but there are ways around this that we
> have proven, which is just that you use the crawler ec2 with kimi vision and navigate captcha (if applicable) but more
> likely email OTP, which is then checked via GraphAPI, OTP input and secure the long term trust token, after which
> future lambdas or devices use that long term trust token to bypass login and go straight to REST API. That is how the
> BDAPI setup is supposed to work, so maybe there is some route that is not properly using that.

## The calls answered

**Call 1:** "Should mcp.opalinvest.dev/sprint be yours only? (a) yes, allow-list = you / (b) keep it open to the
tenant". REC (a). **ANSWERED: YES, REC APPROVED.**
- `SPRINT_VIEW_ALLOWED_EMAILS=andrew@opalinvest.com` goes into the host `.env` template that `deploy-to-ec2.sh`
  renders, because every deploy rewrites `.env`. It ships as a narrow gateway release under the two-half never-widen
  sign-off.
- `/sprint` then serves Andrew only (`sprint_view.py:173-175`, roster check; a non-roster viewer gets 403).
- Consequences:
  - The OA-g-3 Alyssa deny backfill (R2-k SERVED step 2) is SUPERSEDED. The roster covers every tenant account,
    not one person.
  - Row NFRA_OPLGTW W3-S22 disarms on this release landing.

**Call 2:** "Did the Black Diamond portal login change around 2026-06-23?" **ANSWERED: YES, BD added MFA around then.**
- **The proven route (Andrew's words):**
  - The crawler EC2 with Kimi vision logs in, handling a captcha if one appears.
  - More likely it hits an email OTP. The OTP is read via Graph API and entered.
  - The long-term trust token is then secured.
  - After that, future lambdas and devices use that token to skip the login and go straight to the REST API.
- **What exists in the estate:**
  - `infra/aws/ec2/bd-49f-auto-login/` (and `bd-cot-auto-login/`, firm-separated), project ADVI_BDAPIMIG.
  - It captures the `bd_DeviceRegistration` cookie and the session into Secrets Manager
    (`blackdiamond/<firm>/session`), and re-injects the cookie so the OTP screen is skipped.
- **The defect Andrew names:** "maybe there is some route that is not properly using that."
  - All three BD downloaders (asset-dim, fees, allocation) fail at a Playwright portal login that times out
    waiting for `bd3.bdreporting.com`. This is row NFRA_MCPINDEX-Z-S8: 69 of 119 asset-dim runs failed since
    2026-06-23.
  - They log in themselves instead of consuming the durable session or trust token.
  - That is a CODE fix in the lane, not a vendor act. MX-s-4 step 1 re-points them onto the durable path, firm by
    firm (NEVER: cot and bd are separate firms).

## Routing, the same turn

- `2.0.0_SA_COO~O`: cut the `/sprint` roster release (Call 1) and re-scope MX-s-4 step 1 (Call 2).
- `3.0.0_SA_CVO~O`: informed. It holds the second half on the roster release.
- `0.0.0_AB_MSTR~Z`: MX-s-4's reseat was keyed on "Andrew's vendor word". That word is now given.
