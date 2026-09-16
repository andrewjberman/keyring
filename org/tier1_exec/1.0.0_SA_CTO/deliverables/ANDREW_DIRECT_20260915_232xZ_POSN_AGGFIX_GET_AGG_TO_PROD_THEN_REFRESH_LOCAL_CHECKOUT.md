# Andrew-direct 2026-09-15 ~23:2xZ, at the `1.0.0_SA_CTO~Z` terminal: this device cannot build the portal, so get the AGG work to PROD and then bring PROD down to this machine

**Recorded by:** `1.0.0_SA_CTO~Z`. **Channel:** typed at this Claude Code session, after a local build attempt.

## Verbatim, entire

> we cant build on this device because the build here never got set up properly for cloudfront OPSEC policy, it doesnt go to cloudfront it
> tries to go straight to apigateway. we need to somehow get the AGG work to PROD and then probably pull PROD to DEV on this machine or
> something like htat

## Read narrowly

- **THE ASK:** get the POSN_AGGFIX portal work onto PROD, then refresh this device's portal checkout from PROD so what is built here is
  what is served.
- **WHY:** he cannot verify the work locally. A local dev server on this device does not go through CloudFront, so the Lambda@Edge
  layer, including this project's own Opal-only gate, is not in the path.
- **WHAT IT CHANGES ABOUT THE ~19:2xZ GOAL** (record @`15827b3991`): nothing in the order of acts. That word already ran validated
  completion, then the portal integrate, then `/prod-deploy`. This word states the PURPOSE and adds a fourth step, the local refresh.
  It also makes plain that seeing it on PROD is how he intends to verify it.
- **THE FOURTH STEP, new here:** after the promote, this device's `portal` submodule checkout and its gitlink move to the new PROD. The
  checkout is detached at `e85f6eb84f` (2026-09-10) and is **212 commits behind** `origin/PROD` `edf85ce503`, which is why his build was
  old. His sentence is the word that authorises moving the pin.

## What the word does NOT do

- It does not release the site-Z workspace push hold, which is separate and stays with `0.0.0_AB_MSTR~Z` and him.
- It does not remove the CVO's L8/L9 from the flow. If closing the round the normal way would delay the promote materially, that is a
  timing question to put to him, not one to settle by skipping a limb.
- It does not ask for a local dev environment fix now. The committed dev config in the portal proxies `/api` and `/v1` to the portal
  CloudFront distribution (`vite.config.ts` `:50-67`, `.env.development`), so whatever sends this device straight to API Gateway is
  device-side and is a separate item.

## Acts taken on it

1. This record, committed.
2. One message to `2.0.0_SA_COO~Z` and `3.0.0_SA_CVO~Z`: close round 1 to terminal on the fastest correct path, so step 2 can be triggered.
3. On terminal + slug + this seat's L10: `POSN_AGGFIX step 2 due` to `0.0.0_AB_MSTR~Z`, then `/prod-deploy`, then the local refresh.

## Broadcast

One message to `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z` and `0.0.0_AB_MSTR~Z`, quoting the word entire. Push state: LOCAL.
