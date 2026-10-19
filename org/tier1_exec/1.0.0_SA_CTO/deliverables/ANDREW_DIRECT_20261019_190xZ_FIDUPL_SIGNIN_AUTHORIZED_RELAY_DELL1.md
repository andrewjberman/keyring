# ANDREW-DIRECT 2026-10-19 ~19:0xZ (relayed to dell1) -- NFRA_FIDUPL: automated sign-in authorized; Fidelity lands in opal-data-assets, split per firm on the G Number

**Received by:** `1.0.0_SA_CTO~DELL1`, 18:52Z-18:53Z. The chain was the laptop `1.0.0_SA_CTO`, then bus messages b6d8224e and bc4f30b8, then
`0.0.0_AB_MSTR~DELL1`, arriving as msgs 8467, 8468 and 8469.
**The laptop records are the primary:** `ANDREW_DIRECT_20261019_190xZ_FIDUPL_SIGNIN_AUTHORIZED_AND_FIDELITY_LANDING_IN_OPAL_DATA_ASSETS.md`
(laptop 6e7a80f56f) and its addendum (laptop 6d6f14e6bc). Neither was on dell1 when this was written. This file exists so dell1's rulings can
cite the word now.

## VERBATIM (as relayed)

> "We can absolutely do the automated sign in, we are authorized users of the application. On the Fidelity storage, I would recommend that
> we drop it in opal-data-assets, using the fidelity channel and essentially pulling them to the relevant bronze buckets per client."

> "THe issue becomes whether or not we have a clear mechanism by which to do that. If we do not, and need to use alongside as a staging
> bucket for the full pull, and afterward we effectively parse out what goes to fidelity-bronze-49financial and fidelity-bronze-inflection
> and so on in the relevant paths in opal-data-assets, then so be it."

> "Yes it is based off the "G Number" for Fidelity, which seems to be their version of an account master.WE need to assess the structure of
> this, if there are clear differentiated masters that tie to different firms, or if there is just one and we have to figure out where they
> all need to be redirected after the fact."

## What it settles on dell1

- **Open act `dell1-20261019T180827Z-c3a6` (the Terms of Use word) is CLOSED on this word.** C-TOU is met, and the automated sign-in may
  proceed. The CRO's quoted clauses (@e999b31f1f) were before him, through the laptop CTO's relay of this box's finding.
- **The landing home is opal-data-assets, through the fidelity channel.** The path comes from `address('fidelity', <scope>, 'bronze', ...)`,
  which today returns `s3://opal-data-assets/fidelity/<scope>/bronze/...`. **opal-data-alongside is not provisioned.** This supersedes my
  18:39Z ruling to COO~P1 that the bucket be provisioned first.
- **The split runs on the G Number.** If the login's G numbers each map to one firm, each G number is a scope row under its firm, and the
  files land straight at `fidelity/<firm>/bronze`. If there is one G number, the full pull stages under `fidelity/alongside` and is split
  afterwards on a named field. That measurement went to `4.0.0_SA_CRO~FIDELITY` as a read-only design fork at 18:5xZ.

-- 1.0.0_SA_CTO~DELL1
