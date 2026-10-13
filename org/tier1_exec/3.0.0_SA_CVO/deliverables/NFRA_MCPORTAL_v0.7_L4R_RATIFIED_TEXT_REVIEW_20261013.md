# L4-R review -- NFRA_MCPORTAL v0.7, ratified-text half

**By:** `3.0.0_SA_CVO~Z`, 2026-10-13 ~00:5xZ, on `1.0.0_SA_CTO~Z` msgs 33508 to 33540 (acked). **PRD:**
`org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md` @cdb5ff66b1, half_hash e72566300b2c. **Last signed by this lane:**
v0.5 @cecf26d2c9.

**Late, stated plainly:** delivered 21:02Z, signed ~00:5xZ. The deliveries queued while this session was idle and were
taken only now (all 13 read OFFER-EXHAUSTED until acked). Andrew's first outcome was held for about four hours by this seat.

## What changed in the half since v0.5

Section-wise diff, cecf26d2c9 to cdb5ff66b1:
- **ENDPOINT:** ONE block added, FWD-20 (9 lines). Nothing else in ENDPOINT moved.
- **CONTRACTS:** 0 lines changed. The v0.6 C17 addendum @fc09ade4ea sits outside the CONTRACTS section.

## FWD-20 against its authority

Andrew-direct ~20:5xZ 2026-10-12, verbatim in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md` (in cdb5ff66b1):
> "a full breakdown of the vendors/channels available via the gateway, what tools/indexes exist for each, and current state of
> entitlements. The easiest way to manage this would be via the MCPORTAL, and this is what I think should be the first distinct
> outcome of the MCPORTAL project."

FWD-20 carries exactly his three parts: every vendor or channel, the tools and indexes on each, and who is entitled today.
Its "first outcome cut" is his "first distinct outcome". The DONE WHEN arm is Andrew reading the page, with one channel's tools
checked against the deployed code and one person's entitlements against the grant store. That is a driven act, not a
wait. The ACCEPT line binds generation to C15 (the map is generated from the deployed gateway's definitions; present in the
PRD's ratified addendum) and the entitlement read to C4 (present in CONTRACTS). 'A channel with no grant reads "no one",
never blank' is the right negative arm. No seat name and no history sits inside the block; "(v0.7)" is the PRD's own
version-tag convention.

## Verdict

**SIGNED.** One carried note, not grounds: the CTO's ruling @msg 33520 adds an SPA-fallback cell (direct loads of
/control-plane and /open-calls are 404 at every served release since 1e32562729) to the FWD-20 issuance. That is a build
fix inside FWD-20's page route, and it needs no ENDPOINT text.

-- 3.0.0_SA_CVO~Z
