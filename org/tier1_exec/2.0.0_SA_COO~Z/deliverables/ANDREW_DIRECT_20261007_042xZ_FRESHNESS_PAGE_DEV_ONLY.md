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

## OUTCOME, measured by this seat 2026-10-07 ~06:15Z -- the page IS dev only on PROD

- Portal DEV: `659104f4` -> `8ddfe409`, pushed by `0.0.0_AB_MSTR~Z` on Andrew's word at its terminal ~05:41Z (msg 30657).
- Portal PROD: `ab3191d0` -> `b06863fe` (v2.1.203), promoted by `2.0.0_SA_COO~D` on Andrew's word "promote it" / "Do it" (msg 30680;
  its record @f14a8198f7). `ls-remote origin PROD` reads `b06863fe` (this seat's read).
- Source at PROD: `r77_ba27.py` AC1 and AC2 both read SERVED: YES on `src/App.tsx` at `b06863fe`.
- The SERVED bundle (`https://d2n2nzpeqf34ge.cloudfront.net`, index Last-Modified 06:03:45 GMT, bundle `index-COsqKVKD.js`, 354,011
  bytes): the /freshness nav entry carries `requiresTier:"internal",requiresDev:!0` and its route carries
  `requireInternal:!0,requireDev:!0`. Positive control on the same read: Investor Reporting's entry and route carry the mark too.
  Counts in the bundle: 2 nav entries with the mark, 3 routes with it (the page's own, Investor Reporting, its print route).
- NOT measured: a sign-in as a non-Dev internal user. The walker account is userType Dev, so the refusal is read from the served
  code (`ProtectedRoute` refuses when `userType !== 'Dev'`), not from a session.
