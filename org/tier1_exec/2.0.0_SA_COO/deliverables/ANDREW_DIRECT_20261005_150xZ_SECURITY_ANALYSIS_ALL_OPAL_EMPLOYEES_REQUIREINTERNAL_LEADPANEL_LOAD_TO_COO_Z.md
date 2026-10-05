# ANDREW-DIRECT 2026-10-05 ~15:0xZ -- Security Analysis visible to all Opal employees (requireInternal); the slow Lead Panel load to COO~Z

- **Channel:** the site-Z terminal of `2.0.0_SA_COO~D` (session 6c9ea2f7-a212-40bf-aefa-ce51b8750285), typed by Andrew.
- **Time:** 2026-10-05 ~15:00Z-15:02Z (three messages).
- **Recorded by:** `2.0.0_SA_COO~D`, same turn.

## Verbatim

1. "I want you to check the frontend tsx for the "Security Analysis" page, specifically who it is gated to. It should be visible for
   all Opal Employees. Look at other functions that are opal-specific to see the pattern on how to structure that. Beyond that, the
   load time is very slow, so we need to figure out why that is. I suspect that some lambdas are doing live computation when the
   served file should be precomputed. Specifically what I'm referring to on that basis is what appears in the lead panel; the
   chatter/price views take almost a minute to load. I would make a note of this for COO~Z to pursue in depth, you just focus on the
   frontend view permissions."
2. "Yeah should not require admin access to see."
3. "but yes, requireInternal is the correct approac"

## What it changes (surfaced, not adjudicated)

- **Supersedes** the Security Analysis gate words of 2026-09-17 ("make the security analysis page appear as dev only admin only") and
  2026-09-22 ("Make sure that the Security Analysis and Investor Reporting pages are marked in tsx for admin and isDev only") for the
  **Security Analysis page only**. Investor Reporting's gate is not named here and is unchanged.
- **The gate found** (portal DEV 481b3bcc, `src/App.tsx`):
  - nav entry `{ path: '/security-analysis', ..., requiresDev: true, requiresAdmin: true }` (:134);
  - routes `/security-analysis` and `/security-analysis/:securityKey` behind `<ProtectedRoute requireDev requireAdmin>` (:470-471).
- **The Opal-specific pattern** (Ticket Center): `<ProtectedRoute requireInternal>`, where `requireInternal` is
  `claims?.firmId === 'opal-capital'` (ProtectedRoute.tsx:119), plus the firm allowlist (`src/lib/firmAccess.ts`). The allowlist
  admits everything for opal-capital and is deny-by-default for partner firms. In the nav, the internal tier reads
  `requiresTier: 'internal'`.
- **The edit:** the nav entry and both routes change to the internal-tier / `requireInternal` gate, with no Dev or admin requirement.
- **The DSGN sequencing with r39** (MSTR~Z msg 29616, Andrew "yes, coordinate with COO~D ..."): answered (a). 71097b53 pushes first; the
  access edit stacks on it as its own candidate (CTO review, then the DEV push on Andrew's word).
- **The Lead Panel load time** (chatter/price faces take almost a minute): routed to `2.0.0_SA_COO~Z` (AMGT_RESAPP owns the Lead Panel
  routes) to pursue in depth. Andrew's suspicion, as written: lambdas doing live computation where the served file should be precomputed.
