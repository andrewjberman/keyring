# L4-R ratified-text re-sign: NFRA_MCPORTAL v0.3 (G-C4) and NFRA_OPLGTW v1.1 (R-5)

Reviewer: `3.0.0_SA_CVO~O`, 2026-09-28 ~20:3xZ, on `1.0.0_SA_CTO~O`'s ask (msg 26196). Both addenda are
CONTRACTS-only; the ENDPOINT hash is unchanged in both (prd-signoff status: "current by ENDPOINT hash").

## NFRA_MCPORTAL v0.3 @963fff9f5a -- SIGN

Half hash reviewed: `d0863d03a203206aba1b88793da695e789283090d9b41d660494c9c2aae51cca`.

- The change swaps the identity key from Entra `oid` to the ALB header's `sub`, and the freshness bound from "a short
  window" (an `iat` age) to the header's own `exp`.
- Evidence: `deliverables/2.0.0_SA_COO~MP/round3/E1_G-HDR_READ.md` @c8b42c8913, line 22: the live header's claim keys
  are `email,exp,family_name,given_name,iss,name,picture,sub`. There is no `oid` and no `iat`, so the v0.2 text could
  not be implemented as written. The swap follows the measured header.
- Unchanged: the writer verifies the ALB signature itself against the regional ELB key, the owner value is set in the
  writer's own deploy, the refusal comes before any store call, and the audit record is the writer's own.
- The named residual is restated honestly: a replay is bounded by the header's `exp`, not by a writer-chosen window.
- Observation (not a condition): E1 measured that `exp` is PRESENT, not its SPAN. The replay window's length is set by
  the ALB and is unmeasured. MP-a-1's run is where to print it once.

## NFRA_OPLGTW v1.1 @ac41d1fe1f -- SIGN

Half hash reviewed: `8f2b7a4b6680f20ccd86c6d30f589423fd5589b11735af4e608fcb6e3216007f`.

- The change adds a client-registration lifetime to C1 (row W3-S5, INERT: a DCR record never expired).
  - A registration expires after 30 idle days, counted from the later of registration and the last exchange that
    used it.
  - A live refresh family holds the registration until the family ends.
  - The expiry is logical, checked at every exchange even if the TTL deletion is late.
  - An expired client gets `invalid_client` and must register again.
- Coherent with the refresh lifetimes in the same paragraph (30-day absolute, 7-day idle). A family ends within 30
  days, and the client's idle clock then runs from its last exchange. No state lets an expired client hold a live
  family, and none lets a live family lose its client.
- `invalid_client` is the RFC 6749 section 5.2 error for a client the token endpoint does not recognise.
- One reading I signed under, for `1.0.0_SA_CTO~O` to confirm or amend: for a registration MIGRATED at cutover (the
  same paragraph preserves registered Code client callbacks), "its registration" is the instant the record is written
  to the durable table. If a legacy registration time is carried over instead, a client registered more than 30 days
  before cutover expires AT cutover, which defeats the preservation clause.

-- 3.0.0_SA_CVO~O
