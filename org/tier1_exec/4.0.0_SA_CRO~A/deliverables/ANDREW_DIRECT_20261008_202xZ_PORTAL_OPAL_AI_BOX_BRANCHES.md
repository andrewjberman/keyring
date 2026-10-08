# ANDREW_DIRECT 2026-10-08 ~20:2xZ -- the same box-branch method for the portal (into DEV) and, in advance, opal_ai

**Channel:** laptop terminal, to `4.0.0_SA_CRO~A`, after the box-sync scheduled task landed.
**Recorded by:** `4.0.0_SA_CRO~A`, same turn.

## Andrew's words, verbatim

> "On this matter, we also invariably are going to need to figure out solutions as it pertains to the portal and
> opal_ai repos. portal has DEV and PROD, where PROD is client facing, so what I'm wondering is if agents can simply just
> run the exact same methodology with box branches for portal that all integrate up to DEV. FOr opal_ai, right now its
> not as serious because there isnt a ton happening but it might make sense to get organized for that in adva nce"

Same channel, minutes later, VERBATIM:

> "Yeah the thing you probably need to do to kick this off is actually study the push activity across those repos and
> assocaited branches so that we can design a solution that is realistic for the level of activity. There most likely
> will not be the same volume as there is in ajb_workspace as ajb_workspace is the monolith and the portal and
> opal_ai repos are microproducts"

Same channel, later, VERBATIM:

> "Yeha maybe we have a "microproduct" policy that isnt as advanced/cumbersome as the monolith since there is
> significantly less volume. I know we did over 2200 commits on ajb_workspace in less than a day the other day so its a
> scope thing"

## Reading

A research question and a design: can the portal run box branches that integrate into `DEV`? `PROD` stays the
client-facing branch, promoted from `DEV` as today. opal_ai gets the same organization in advance, at lower urgency.
This is not an order to switch either repo.
The first act is a MEASURED study of push and commit activity per repo and branch (`ACTIVITY_STUDY_*` beside this file).
