# ANDREW-DIRECT 2026-10-07 ~04:2xZ -- the /freshness page is dev only

**Channel:** typed at the `2.0.0_SA_COO~Z` terminal (site Z), 2026-10-07 ~04:2xZ (12:2x AM ET).

**VERBATIM:** "is freshness page dev only? if not it should be"

## Measured answer to the question (the issuer, at the time of the word)

- **No.** Portal `origin/PROD` `ab3191d0` carries the page (`src/pages/Freshness/`, 4 files; `6de76f05` is an ancestor of PROD).
- Its nav entry reads `{ path: '/freshness', ..., requiresTier: 'internal' }` (`src/App.tsx:136`) and its route reads
  `<ProtectedRoute requireInternal>` (`src/App.tsx:473`). So on PROD it is shown to every Opal-internal user, not to Dev users only.
- `origin/DEV` `659104f4` reads the same two lines.
- The portal already has a dev-only mark: `requiresDev: true` on a nav item and `requireDev` on a route, checked against
  `claims.userType === 'Dev'` (`App.tsx:338-373`, `ProtectedRoute.tsx:120`). Investor Reporting carries it, on Andrew's word of
  2026-09-22 ("marked in tsx for admin and isDev only").

## How this seat reads the word, and what it does NOT decide

- **Applied reading:** "dev only" = the portal's existing dev-only mark. The page's nav entry gains `requiresDev: true` and its
  route gains `requireDev`, so only a user whose `userType` is `Dev` sees or opens it, on DEV and on PROD alike.
- **The other reading, NOT taken and not ruled out:** the page should not be on the PROD branch at all. That is a revert on PROD,
  not a mark. If that is what the word means, it is Andrew's to say; the mark is the smaller, reversible act and does not block it.
- **Scope is not widened:** this covers the /freshness page only. No other page is touched.

## What follows

1. AMGT_RESAPP direct act `AMGT-ba-27` (decomposition s.85 ADDENDUM 1): the two-token mark, built on the approved /freshness
   candidate `504ddb3d` merged onto DEV `659104f4`, so ONE candidate carries the page and its mark.
2. The CTO's render review (the candidate touches a product file, `App.tsx`).
3. The DEV push, then a PROD promote: PROD is where the page is visible to non-Dev users today, so the mark takes effect only
   when it reaches PROD. Both are Andrew's word through the existing routes (`0.0.0_AB_MSTR~Z` for DEV; `/prod-deploy` for PROD).

Recorded by `2.0.0_SA_COO~Z`. One line to `1.0.0_SA_CTO~Z` names this path.
