# ANDREW-DIRECT 2026-09-30 ~06:2xZ -- NFRA_MCPMSP: the portal-v2 residual accepted for the Inflection-only pilot

**Channel:** Andrew, in the 1.0.0_SA_CTO~O Claude Code session (site Z), 2026-09-30 ~06:2xZ, answering this seat's
one-card `/open-calls` on 3.0.0_SA_CVO~O finding F2 (msg 26963).
**Recorded by:** 1.0.0_SA_CTO~O, same turn.

## The card as put

> **During the Inflection pilot, may the gateway keep its read access to the shared portal figures? (yes / no)**
> Your s.8 rule: the gateway reads no firm data. It already can't read the firm buckets, but blocking it from the
> shared portal bucket would change what the internal Analyst serves, so that block comes in a later round. Until
> then, only the tenant lookup, not AWS, would stop a bug from showing one firm another firm's portal figures.
> **REC --** Yes for the Inflection-only pilot, on the condition that the block lands before Cottonwood goes live
> (FWD-2). With one partner live there's no other partner to leak to, and FWD-2's cross-firm test is exactly where AWS
> needs to enforce it.

## Verbatim

> "Yes, rec approved"

## What it binds

- NFRA_MCPMSP C5's v0.3 staging is ACCEPTED for live partner traffic while Inflection is the only live partner firm.
- **Condition:** the gateway identity's `opal-data-portal-v2` zero-read, which is the enrichment round that first builds
  an Opal-internal reader role under never-widen sign-off, lands BEFORE Cottonwood (or any second partner firm) goes
  live. FWD-2 is not graded, and G-FIRM for a second firm is not taken, until it has landed.
- It narrows record s.8 ("the server's own identity reads no firm data") for the Inflection-only pilot and for nothing
  else.
