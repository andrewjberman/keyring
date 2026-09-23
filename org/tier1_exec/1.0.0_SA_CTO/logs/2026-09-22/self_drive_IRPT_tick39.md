# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 39 (2026-09-22 ~12:5xZ)

**Arming record:** `c9ccd9f4e3`. **state: ARMED.**

## Scope

| project | stage | open orders | notes |
|---|---|---|---|
| IRPT_FNTEND | round 13 in flight at `2.0.0_SA_COO~F` | -- | FE-s-83 drained @7b3820258d; FE-s-82 and FE-s-84 resumption workers running |
| IRPT_BCKEND | round 16 closed; round 17 parked on the v0.16 sign-off | 0 | -- |

- **Sequence:** no flags (`sequence-check`). Capacity is 2 of 3 COO lanes.
- **Inbox:** 0 unread at the top level.

## Driver act this tick

**IRPT_BCKEND PRD v0.16 @`b03ad9d3b6`: the render-token addendum.**
- It carries Andrew's word *"Option 2 is preferable"* (@`29d157110d`) and the CRO research (@`55a47e2cfd`).
- It defines the render identity:
  - a separate signing key;
  - `aud` `irpt-render`;
  - an expiry of 5 minutes or less;
  - `jti` set to the render id;
  - the role `renderer`;
  - none of the admin-bypass claims.
- Tokens are minted only from the frozen `ExportBundle`.
- Only V2 and V3 accept the token, and each does so through an explicit branch scoped to the print routes.
- There are 7 acceptance arms, graded by the CVO.

**FIRM_BINDING, DECIDED on the CTO's recommendation (a design fork, researched by the CRO):**
- The token's `firmId` is the tenant firm, never `opal-capital`. No backend handler changes.
- Global cross-firm entitlement is checked when the bundle is created (B15).
- The frontend print-route branch belongs to IRPT_FNTEND. It will be amended at FNTEND's next L10, not mid-round.

**V3's missing `aud` check on the human path** is recorded as a separate standing gap, not a rider on this addendum.

## Sign-off

`prd-signoff status IRPT_BCKEND` reads **WITHHELD**. Both halves are STALE:
- the ratified-text half is owed by `3.0.0_SA_CVO~B`;
- the brief half is owed by `4.0.0_SA_CRO`.

Messages sent: 99468, 99469 and 99470 (FYI to `2.0.0_SA_COO~B`). All three were DELIVERED.

## Open calls in scope

**None.** FIRM_BINDING was closed above.

## Completion test

**NOT DONE: 0 of 2 projects complete.**

## Next

1. Both halves re-signed.
2. `2.0.0_SA_COO~B` cuts round 17.
3. The FNTEND round-13 slug arrives; this seat writes the CTO analysis, which carries the print-route render branch into the FNTEND PRD.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
