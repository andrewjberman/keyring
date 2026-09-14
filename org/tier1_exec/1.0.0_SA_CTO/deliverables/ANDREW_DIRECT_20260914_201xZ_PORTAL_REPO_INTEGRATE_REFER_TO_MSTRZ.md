# ANDREW-DIRECT 2026-09-14 ~20:1xZ (~4:1x PM ET) -- the portal repo needs an /integrate merge too; refer the plan to 0.0.0_AB_MSTR~Z

**Received at:** the `1.0.0_SA_CTO~Z` terminal, in-session, after this seat served the POSN portal view on `localhost:5173`.
**Recorded by:** `1.0.0_SA_CTO~Z`, same turn.

## HIS WORDS -- VERBATIM AND ENTIRE

> "On this device we are still having an issue with the login from the localhost not going to the proper cloudfront. I
> realize that what this really entails is that there also needs to be an /integrate merge action of the Portal Repo, not
> just the ajb_workspace repo. This may be a bit complicated because there has been a lot of portal work on the laptop
> fabric, so we need to figure out a plan on how to properly execute this integration, please refer this matter to MSTR~Z
> (there is no portal-specific branch for sitez vs laptop as far as I am aware)."

## READING -- stated narrowly

1. **Symptom:** on site Z, logging in from a localhost portal build does not reach the proper CloudFront.
2. **His diagnosis:** the portal repo itself needs an `/integrate` merge between the fabrics, not only `ajb_workspace`.
3. **Asked of `1.0.0_SA_CTO~Z`:** REFER the matter to `0.0.0_AB_MSTR~Z` (the integrator) to figure out a PLAN. Not to execute
   a merge, move a gitlink, push, or promote. The portal freeze (no promote, no DEV/PROD push, no gitlink move) is untouched by
   this word; any act that would cross it is for the plan to name and for Andrew to approve.
4. **His stated belief, carried as his and not verified here:** there is no portal-specific branch separating site Z from the
   laptop fabric.
5. **Standing context the plan must respect:** round-5 POSN portal work is committed on portal refs behind the freeze
   (`refs/drains/posn-5-portal`, worker branch `wk-posn-5-22-portal`), and AMGT_RESAPP's frontend sits on
   `refs/drains/rg-2-portal`. Measured facts for the plan are sent with the referral.
