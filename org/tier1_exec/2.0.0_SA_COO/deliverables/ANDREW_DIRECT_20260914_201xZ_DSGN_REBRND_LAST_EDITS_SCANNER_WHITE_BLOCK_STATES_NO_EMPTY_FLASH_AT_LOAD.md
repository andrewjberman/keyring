# ANDREW-DIRECT 2026-09-14 ~20:1xZ -- DSGN_REBRND: THE LAST EDITS BEFORE CLOSE -- THE SECURITY SCANNER BREAK; NO WHITE BLOCK INSIDE A CARD; NO "NO DATA" CARD WHILE LOADING

**Terminal:** `2.0.0_SA_COO~D`, in the page-by-page mode (record @ff6f00d0b0). **Recorded by:** `2.0.0_SA_COO~D`, in the
same turn. One message, with two screenshots.

## VERBATIM AND ENTIRE

> There are only a couple edits remaining and I think we can close down this project. 1.) [Image #10] It seems like
> the Security Scanner is broken somehow, need to understand if that is from us or otherwise how that happened. I
> also do not like his format where we superimpose a large white block inside a card, it is not the right
> coloring/presentation; it should be displayed as a soft card on the lighter color, like how we do the cards that sit
> in "Trending Topics". 2.) [Image #11] This white block card design appears several times throughout the portal.
> I've seen it in "Top/Bottom Performers" as well before it realizes it has data, i believe that same design appears
> in Macroeconomics as well. 3.) With regard to these "No data available" cards, it is not appropriate for them to
> come up by default at load, because what happens is that we do have the data and we end up flashing some ephemeral
> card about not having data while the load is occurring so it becomes a flash of bad ui card for a second or two
> before the actual information populates. I have seen this same behavior in the "Account Distribution" bell curve
> chart element in the "Model Portfolios" page; we need to stop using that pattern wherever it appears.

Image #10 shows the Security Scanner's Factor Bank panel. Its body holds a white block reading "The factor list could
not be loaded. Cause: API request failed: 403 Forbidden - {"message":"Forbidden"}". Image #11 shows Portfolio
Management's Alpha Decomposition panel, whose body holds a white block reading "No alpha factor attribution for this
portfolio yet."

## WHAT IT SETTLES

1. **Close is in sight.** "There are only a couple edits remaining and I think we can close down this project." The
   close itself stays his manual act (record @ff6f00d0b0); this sentence does not perform it.
2. **The Security Scanner break is diagnosed and explained: ours, or otherwise, and how.**
3. **No white block inside a card.** A state inside a dark panel (empty, error or loading) is a SOFT CARD on the
   lighter rung, like the Trending Topics cards: the tile rung, a faint hairline and light ink. This applies wherever
   the pattern appears, and he names the Security Scanner, Top/Bottom Performers, Macroeconomics and Alpha
   Decomposition.
4. **No "no data" card while a load is in flight.** An empty state shows only once the load has finished and found
   nothing. While the data is still arriving, the panel shows its loading state. He names the Account Distribution
   bell curve on Model Portfolios, and the rule applies "wherever it appears".

## ADDENDUM ~20:2xZ -- HIS FOLLOW-UP, VERBATIM AND ENTIRE, AND WHAT THE BREAK WAS

> Interesting, the Security Scanner is fine on the PROD build, so it is either localhost or otherwise DEV-specific.

**The cause is localhost only, and it is not this project.**
- **The backend change.** Workspace 7abe7552b5 (0.7.0_AE_CloudOps~Z, 2026-09-03) made the portal authorizer refuse any
  request without CloudFront's `X-Opal-Origin-Verify` header.
- **Why only localhost broke.** The local vite dev-server proxy sent `/api/scoped/security-scanner` straight to API
  Gateway (`7k3ed8px20.execute-api...`), bypassing CloudFront, so it met a 403 `{"message":"Forbidden"}`. PROD calls
  same-origin through CloudFront and was unaffected.
- **No DEV deploy is involved.** No separate DEV deploy exists; `deploy.yml` runs on the PROD branch only.
- **The branch did not touch the request.** The feature branch's Scanner diff against DEV changes only how the error
  card is drawn.

**Measured**, in the `opal-portal-authorizer` log. Earlier, "Origin verification FAILED - request did not come through
CloudFront" appeared every 5 minutes from 19:34Z, and 5 times at 20:08:24-30Z. Then a three-way probe at 20:40:18Z,
each request carrying a deliberately malformed bearer:

| Path | Log reading |
|---|---|
| Direct to API Gateway (20:40:20Z) | Origin verification FAILED |
| Via CloudFront (20:40:21Z) | Origin passed, then "jwt malformed" |
| Via the local proxy after the fix (20:40:22Z) | Origin passed, then "jwt malformed" |

**The fix** repoints the dev-proxy entry through CloudFront (`d2n2nzpeqf34ge.cloudfront.net`, the pattern the
advisor-intelligence and satellites entries already use). It is dev-server only; the PROD build never reads the proxy.

**The same class** covers three sibling proxy entries that still target API Gateway directly: `/api/scoped/partners`,
`/api/partners` and `/api/scoped/data-refresh`. They were not repointed. They are named here for his call.

## WHAT IT DOES NOT SETTLE

It does not authorize a promote, and it does not perform the manual close. The portal freeze and the feature branch
stand.
